from inspect import isawaitable
from typing import Any, Awaitable, Callable, Dict, List, Optional, Union, cast

import attr

from ...client import Client
from ...models.cpf import CPF
from ...models.get_cpf_ni_response_400 import GetCpfNiResponse400
from ...types import UNSET, Response, Unset


@attr.s(auto_attribs=True)
class Endpoints:
    _client: Union[Client, Callable[[], Client]]

    def _get_client(self) -> Client:
        client = self._client
        if callable(client):
            client = client()
        assert isinstance(client, Client)
        return client

    def get_cpf_ni_detailed(
        self,
        ni: str,
        *,
        x_signature: Union[Unset, str] = UNSET,
        x_request_tag: Union[Unset, str] = UNSET,
    ) -> Response[Union[Any, CPF, GetCpfNiResponse400]]:
        """Retorna os dados do Cadastro de Pessoa Física (CPF)

         Chaves para degustação? &nbsp; [Acesse
        aqui](https://apicenter.estaleiro.serpro.gov.br/documentacao/consulta-cpf/pt/quick_start/#como-
        utilizar-a-api-cpf-demonstracao)

        Args:
            ni (str):
            x_signature (Union[Unset, str]):
            x_request_tag (Union[Unset, str]):

        Returns:
            Response[Union[Any, CPF, GetCpfNiResponse400]]
        """

        from . import get_cpf_ni as _endpoint

        return _endpoint.sync_detailed(
            ni=ni,
            x_signature=x_signature,
            x_request_tag=x_request_tag,
            client=self._get_client(),
        )

    def get_cpf_ni(
        self,
        ni: str,
        *,
        x_signature: Union[Unset, str] = UNSET,
        x_request_tag: Union[Unset, str] = UNSET,
    ) -> Optional[Union[Any, CPF, GetCpfNiResponse400]]:
        """Retorna os dados do Cadastro de Pessoa Física (CPF)

         Chaves para degustação? &nbsp; [Acesse
        aqui](https://apicenter.estaleiro.serpro.gov.br/documentacao/consulta-cpf/pt/quick_start/#como-
        utilizar-a-api-cpf-demonstracao)

        Args:
            ni (str):
            x_signature (Union[Unset, str]):
            x_request_tag (Union[Unset, str]):

        Returns:
            Response[Union[Any, CPF, GetCpfNiResponse400]]
        """

        from . import get_cpf_ni as _endpoint

        return _endpoint.sync(
            ni=ni,
            x_signature=x_signature,
            x_request_tag=x_request_tag,
            client=self._get_client(),
        )


@attr.s(auto_attribs=True)
class AsyncEndpoints:
    _client: Union[Client, Callable[[], Client], Callable[[], Awaitable[Client]]]

    async def _get_client(self) -> Client:
        client = self._client
        if callable(client):
            client = client()  # type: ignore
        if isawaitable(client):
            client = await client
        assert isinstance(client, Client)
        return client

    async def get_cpf_ni_detailed(
        self,
        ni: str,
        *,
        x_signature: Union[Unset, str] = UNSET,
        x_request_tag: Union[Unset, str] = UNSET,
    ) -> Response[Union[Any, CPF, GetCpfNiResponse400]]:
        """Retorna os dados do Cadastro de Pessoa Física (CPF)

         Chaves para degustação? &nbsp; [Acesse
        aqui](https://apicenter.estaleiro.serpro.gov.br/documentacao/consulta-cpf/pt/quick_start/#como-
        utilizar-a-api-cpf-demonstracao)

        Args:
            ni (str):
            x_signature (Union[Unset, str]):
            x_request_tag (Union[Unset, str]):

        Returns:
            Response[Union[Any, CPF, GetCpfNiResponse400]]
        """

        from . import get_cpf_ni as _endpoint

        return await _endpoint.asyncio_detailed(
            ni=ni,
            x_signature=x_signature,
            x_request_tag=x_request_tag,
            client=await self._get_client(),
        )

    async def get_cpf_ni(
        self,
        ni: str,
        *,
        x_signature: Union[Unset, str] = UNSET,
        x_request_tag: Union[Unset, str] = UNSET,
    ) -> Optional[Union[Any, CPF, GetCpfNiResponse400]]:
        """Retorna os dados do Cadastro de Pessoa Física (CPF)

         Chaves para degustação? &nbsp; [Acesse
        aqui](https://apicenter.estaleiro.serpro.gov.br/documentacao/consulta-cpf/pt/quick_start/#como-
        utilizar-a-api-cpf-demonstracao)

        Args:
            ni (str):
            x_signature (Union[Unset, str]):
            x_request_tag (Union[Unset, str]):

        Returns:
            Response[Union[Any, CPF, GetCpfNiResponse400]]
        """

        from . import get_cpf_ni as _endpoint

        return await _endpoint.asyncio(
            ni=ni,
            x_signature=x_signature,
            x_request_tag=x_request_tag,
            client=await self._get_client(),
        )
