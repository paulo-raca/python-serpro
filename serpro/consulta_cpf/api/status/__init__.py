from inspect import isawaitable
from typing import Any, Awaitable, Callable, Dict, List, Optional, Union

import attr

from ...client import Client
from ...types import UNSET, Response


@attr.s(auto_attribs=True)
class Endpoints:
    _client: Union[Client, Callable[[], Client]]

    def _get_client(self) -> Client:
        client = self._client
        if callable(client):
            client = client()
        return client

    def get_status_detailed(
        self,
    ) -> Response[Any]:
        """Retorna o status da API CPF

        Returns:
            Response[Any]
        """

        from . import get_status as _endpoint

        return _endpoint.sync_detailed(
            client=self._get_client(),
        )


@attr.s(auto_attribs=True)
class AsyncEndpoints:
    _client: Union[Client, Callable[[], Client], Callable[[], Awaitable[Client]]]

    async def _get_client(self) -> Client:
        client = self._client
        if callable(client):
            client = client()
        if isawaitable(client):
            client = await client
        return client

    async def get_status_detailed(
        self,
    ) -> Response[Any]:
        """Retorna o status da API CPF

        Returns:
            Response[Any]
        """

        from . import get_status as _endpoint

        return await _endpoint.asyncio_detailed(
            client=await self._get_client(),
        )
