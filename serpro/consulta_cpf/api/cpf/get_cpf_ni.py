from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.cpf import CPF
from ...models.get_cpf_ni_response_400 import GetCpfNiResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ni: str,
    *,
    client: Client,
    x_signature: Union[Unset, str] = UNSET,
    x_request_tag: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/cpf/{ni}".format(client.base_url, ni=ni)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_signature, Unset):
        headers["x-signature"] = x_signature

    if not isinstance(x_request_tag, Unset):
        headers["x-request-tag"] = x_request_tag

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, CPF, GetCpfNiResponse400]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = CPF.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.PARTIAL_CONTENT:
        response_206 = cast(Any, None)
        return response_206
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = GetCpfNiResponse400.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, CPF, GetCpfNiResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    ni: str,
    *,
    client: Client,
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

    kwargs = _get_kwargs(
        ni=ni,
        client=client,
        x_signature=x_signature,
        x_request_tag=x_request_tag,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    ni: str,
    *,
    client: Client,
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

    return sync_detailed(
        ni=ni,
        client=client,
        x_signature=x_signature,
        x_request_tag=x_request_tag,
    ).parsed


async def asyncio_detailed(
    ni: str,
    *,
    client: Client,
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

    kwargs = _get_kwargs(
        ni=ni,
        client=client,
        x_signature=x_signature,
        x_request_tag=x_request_tag,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    ni: str,
    *,
    client: Client,
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

    return (
        await asyncio_detailed(
            ni=ni,
            client=client,
            x_signature=x_signature,
            x_request_tag=x_request_tag,
        )
    ).parsed
