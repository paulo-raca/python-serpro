from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.integration import Integration
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    x_request_tag: Union[Unset, str] = UNSET,
    x_request_trace_id: Union[Unset, str] = UNSET,
    x_signature: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v2/status".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_request_tag, Unset):
        headers["x-request-tag"] = x_request_tag

    if not isinstance(x_request_trace_id, Unset):
        headers["x-request-trace-id"] = x_request_trace_id

    if not isinstance(x_signature, Unset):
        headers["x-signature"] = x_signature

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Integration]]:
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    if response.status_code == HTTPStatus.SERVICE_UNAVAILABLE:
        response_503 = Integration.from_dict(response.json())

        return response_503
    if response.status_code == HTTPStatus.GATEWAY_TIMEOUT:
        response_504 = cast(Any, None)
        return response_504
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Integration]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    x_request_tag: Union[Unset, str] = UNSET,
    x_request_trace_id: Union[Unset, str] = UNSET,
    x_signature: Union[Unset, str] = UNSET,
) -> Response[Union[Any, Integration]]:
    """Checks whether the Datavalid service is functional

     It allows obtaining information about the availability of the service, where it is obtained through
    the HTTP status code

    Args:
        x_request_tag (Union[Unset, str]):
        x_request_trace_id (Union[Unset, str]):
        x_signature (Union[Unset, str]):

    Returns:
        Response[Union[Any, Integration]]
    """

    kwargs = _get_kwargs(
        client=client,
        x_request_tag=x_request_tag,
        x_request_trace_id=x_request_trace_id,
        x_signature=x_signature,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    x_request_tag: Union[Unset, str] = UNSET,
    x_request_trace_id: Union[Unset, str] = UNSET,
    x_signature: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, Integration]]:
    """Checks whether the Datavalid service is functional

     It allows obtaining information about the availability of the service, where it is obtained through
    the HTTP status code

    Args:
        x_request_tag (Union[Unset, str]):
        x_request_trace_id (Union[Unset, str]):
        x_signature (Union[Unset, str]):

    Returns:
        Response[Union[Any, Integration]]
    """

    return sync_detailed(
        client=client,
        x_request_tag=x_request_tag,
        x_request_trace_id=x_request_trace_id,
        x_signature=x_signature,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    x_request_tag: Union[Unset, str] = UNSET,
    x_request_trace_id: Union[Unset, str] = UNSET,
    x_signature: Union[Unset, str] = UNSET,
) -> Response[Union[Any, Integration]]:
    """Checks whether the Datavalid service is functional

     It allows obtaining information about the availability of the service, where it is obtained through
    the HTTP status code

    Args:
        x_request_tag (Union[Unset, str]):
        x_request_trace_id (Union[Unset, str]):
        x_signature (Union[Unset, str]):

    Returns:
        Response[Union[Any, Integration]]
    """

    kwargs = _get_kwargs(
        client=client,
        x_request_tag=x_request_tag,
        x_request_trace_id=x_request_trace_id,
        x_signature=x_signature,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    x_request_tag: Union[Unset, str] = UNSET,
    x_request_trace_id: Union[Unset, str] = UNSET,
    x_signature: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, Integration]]:
    """Checks whether the Datavalid service is functional

     It allows obtaining information about the availability of the service, where it is obtained through
    the HTTP status code

    Args:
        x_request_tag (Union[Unset, str]):
        x_request_trace_id (Union[Unset, str]):
        x_signature (Union[Unset, str]):

    Returns:
        Response[Union[Any, Integration]]
    """

    return (
        await asyncio_detailed(
            client=client,
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
        )
    ).parsed
