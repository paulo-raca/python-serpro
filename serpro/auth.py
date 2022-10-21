import asyncio
import base64
import importlib
import ssl
import threading
from dataclasses import dataclass
from datetime import datetime, timedelta
from time import perf_counter_ns
from typing import Dict, Generic, Optional, TypeVar, Union, overload

import attr
import httpx

from . import consulta_cpf, datavalid

AuthenticatedClient = TypeVar("AuthenticatedClient", consulta_cpf.AuthenticatedClient, datavalid.AuthenticatedClient)


@dataclass(kw_only=True)
class ExpiringClient(Generic[AuthenticatedClient]):
    client: AuthenticatedClient
    expires_at_ns: int  # timestamp from perf_counter_ns

    @property
    def expires_in(self) -> timedelta:
        return timedelta(seconds=(self.expires_at_ns - perf_counter_ns()) * 10e-9)

    @property
    def expires_at(self) -> timedelta:
        return datetime.now() + self.expires_in

    def __bool__(self):
        return self.expires_at_ns > perf_counter_ns()


@dataclass(kw_only=True)
class SerproAuth(Generic[AuthenticatedClient]):
    base_client: AuthenticatedClient
    consumer_key: str
    consumer_secret: str

    _expiring_client: Optional[ExpiringClient] = None
    _lock: threading.Lock = threading.Lock()
    _async_lock: asyncio.Lock = asyncio.Lock()

    def client(self) -> AuthenticatedClient:
        return self.expiring_client().client

    async def client_async(self) -> AuthenticatedClient:
        return (await self.expiring_client_async()).client

    def expiring_client(self) -> ExpiringClient:
        expiring_client = self._expiring_client
        if expiring_client:
            return expiring_client

        with self._lock:
            expiring_client = self._expiring_client
            if expiring_client:
                return expiring_client

            with httpx.Client() as client:
                response = client.post(
                    url="https://gateway.apiserpro.serpro.gov.br/token",
                    headers={
                        "Authorization": "Basic "
                        + base64.b64encode(f"{self.consumer_key}:{self.consumer_secret}".encode()).decode(),
                        "Content-Type": "application/x-www-form-urlencoded",
                    },
                    data={"grant_type": "client_credentials"},
                )
                if response.status_code != httpx.codes.OK:
                    raise IOError(f"Failed to retrieve Bearer Token: {response.status_code} - {response.text}")

                json = response.json()
                expiring_client = ExpiringClient[AuthenticatedClient](
                    client=attr.evolve(
                        self.base_client,
                        auth_header_name="Authorization",
                        token=json["access_token"],
                        prefix=json["token_type"],
                    ),
                    # Nanosecs until expiration, subtracts 30s for safety
                    expires_at_ns=perf_counter_ns() + 10e9 * max(0, json["expires_in"] - 30),
                )
                self._expiring_client = expiring_client
                return expiring_client

    async def expiring_client_async(self) -> ExpiringClient:
        expiring_client = self._expiring_client
        if expiring_client:
            return expiring_client

        async with self._async_lock:
            expiring_client = self._expiring_client
            if expiring_client:
                return expiring_client

            async with httpx.AsyncClient() as client:
                response = await client.post(
                    url="https://gateway.apiserpro.serpro.gov.br/token",
                    headers={
                        "Authorization": "Basic "
                        + base64.b64encode(f"{self.consumer_key}:{self.consumer_secret}".encode()).decode(),
                        "Content-Type": "application/x-www-form-urlencoded",
                    },
                    data={"grant_type": "client_credentials"},
                )
                if response.status_code != httpx.codes.OK:
                    raise IOError(f"Failed to retrieve Bearer Token: {response.status_code} - {response.text()}")

                json = response.json()
                expiring_client = ExpiringClient[AuthenticatedClient](
                    client=attr.evolve(
                        self.base_client,
                        auth_header_name="Authorization",
                        token=json["access_token"],
                        prefix=json["token_type"],
                    ),
                    # Nanosecs until expiration, subtracts 30s for safety
                    expires_at_ns=perf_counter_ns() + 10e9 * max(0, json["expires_in"] - 30),
                )
                print("Token:", json["access_token"])
                self._expiring_client = expiring_client
                return expiring_client


class AuthApiMixin:
    @overload
    def __init__(
        self,
        base_url: str,
        *,
        token: str,
        cookies: Dict[str, str] = {},
        headers: Dict[str, str] = {},
        timeout: float = 5,
        verify_ssl: Union[str, bool, ssl.SSLContext] = True,
    ):
        ...

    @overload
    def __init__(
        self,
        base_url: str,
        *,
        consumer_key: str = None,
        consumer_secret: str = None,
        cookies: Dict[str, str] = {},
        headers: Dict[str, str] = {},
        timeout: float = 5,
        verify_ssl: Union[str, bool, ssl.SSLContext] = True,
    ):
        ...

    def __init__(
        self,
        base_url: str,
        *,
        token: Optional[str] = None,
        consumer_key: Optional[str] = None,
        consumer_secret: Optional[str] = None,
        **kwargs,
    ):
        assert (consumer_key is None) == (consumer_secret is None), "Must use both consumer_key and consumer_secret"
        assert (token is not None) != (
            consumer_key is not None
        ), "Must use either token or consumer_key/consumer_secret"
        if token is None:
            token = "..."
        # if base_url is ...:
        #    base_url = self.DEFAULT_ENDPOINT

        ApiClass = [
            cls
            for cls in self.__class__.mro()
            if cls is not self.__class__ and cls.__module__.endswith(".api") and cls.__name__.endswith("Api")
        ][0]
        is_async = ApiClass.__name__ == "AsyncApi"
        AuthenticatedClient = importlib.import_module("..client", ApiClass.__module__).AuthenticatedClient

        client = AuthenticatedClient(base_url=base_url, token=token, **kwargs)
        if consumer_key is not None:
            auth = SerproAuth(base_client=client, consumer_key=consumer_key, consumer_secret=consumer_secret)
            client = auth.client_async if is_async else auth.client

        self._client = client
