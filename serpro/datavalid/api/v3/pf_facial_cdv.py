from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.pf_facial_cdv_input import PFFacialCdvInput
from ...models.pf_facial_cdv_result import PFFacialCdvResult
from ...models.violation import Violation
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: PFFacialCdvInput,
    x_request_tag: Union[Unset, str] = UNSET,
    x_request_trace_id: Union[Unset, str] = UNSET,
    x_signature: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v3/validate/pf-facial-cdv".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    if not isinstance(x_request_tag, Unset):
        headers["x-request-tag"] = x_request_tag

    if not isinstance(x_request_trace_id, Unset):
        headers["x-request-trace-id"] = x_request_trace_id

    if not isinstance(x_signature, Unset):
        headers["x-signature"] = x_signature

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[Violation], PFFacialCdvResult]]:
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.REQUEST_ENTITY_TOO_LARGE:
        response_413 = cast(Any, None)
        return response_413
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = []
        _response_422 = response.json()
        for response_422_item_data in _response_422:
            response_422_item = Violation.from_dict(response_422_item_data)

            response_422.append(response_422_item)

        return response_422
    if response.status_code == HTTPStatus.OK:
        response_200 = PFFacialCdvResult.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[Violation], PFFacialCdvResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: PFFacialCdvInput,
    x_request_tag: Union[Unset, str] = UNSET,
    x_request_trace_id: Union[Unset, str] = UNSET,
    x_signature: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List[Violation], PFFacialCdvResult]]:
    """Validation and returning OCR atributes of information extracted from the corresponding document

     It receives in the body of the request a key with the CPF of the individual (object
    <code>key</code>) and the object <code>answer</code> that contains the images of the front of the
    document (mandatory), the back of the document (optional) and the face (optional). All images must
    be sent encoded with <a href='https://pt.wikipedia.org/wiki/Base64'
    target='_blank'>Base64</a>.<br>Returns which document was identified and whether or not each of the
    data is valid, along with the probability and percentage of similarity for biometric
    validation.<br>For text type data, the percentage of similarity between the data extracted from the
    document and the official data available in government databases is also returned.<br>The biometric
    validation will be performed based on the portrait extracted from the document and the face sent
    (optional).<br><br>This named resource can be used to remotely validate a document.<br>The
    extraction of data of the document is not a deterministic resource, and it is up to the service user
    to use the values returned in the response to decide on the authenticity of the sent
    document.<br><br>Biometrics is not a deterministic resource, so it is up to the user using the
    service to use the values returned in the response to decide on the authenticity of the biometrics
    sent. In any case, it is important to mention that in tests performed, in approximately 99% of the
    validations that returned high or very high probability, the pair of biometrics compared were from
    the same person.

    Args:
        x_request_tag (Union[Unset, str]):
        x_request_trace_id (Union[Unset, str]):
        x_signature (Union[Unset, str]):
        json_body (PFFacialCdvInput):

    Returns:
        Response[Union[Any, List[Violation], PFFacialCdvResult]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
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
    json_body: PFFacialCdvInput,
    x_request_tag: Union[Unset, str] = UNSET,
    x_request_trace_id: Union[Unset, str] = UNSET,
    x_signature: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List[Violation], PFFacialCdvResult]]:
    """Validation and returning OCR atributes of information extracted from the corresponding document

     It receives in the body of the request a key with the CPF of the individual (object
    <code>key</code>) and the object <code>answer</code> that contains the images of the front of the
    document (mandatory), the back of the document (optional) and the face (optional). All images must
    be sent encoded with <a href='https://pt.wikipedia.org/wiki/Base64'
    target='_blank'>Base64</a>.<br>Returns which document was identified and whether or not each of the
    data is valid, along with the probability and percentage of similarity for biometric
    validation.<br>For text type data, the percentage of similarity between the data extracted from the
    document and the official data available in government databases is also returned.<br>The biometric
    validation will be performed based on the portrait extracted from the document and the face sent
    (optional).<br><br>This named resource can be used to remotely validate a document.<br>The
    extraction of data of the document is not a deterministic resource, and it is up to the service user
    to use the values returned in the response to decide on the authenticity of the sent
    document.<br><br>Biometrics is not a deterministic resource, so it is up to the user using the
    service to use the values returned in the response to decide on the authenticity of the biometrics
    sent. In any case, it is important to mention that in tests performed, in approximately 99% of the
    validations that returned high or very high probability, the pair of biometrics compared were from
    the same person.

    Args:
        x_request_tag (Union[Unset, str]):
        x_request_trace_id (Union[Unset, str]):
        x_signature (Union[Unset, str]):
        json_body (PFFacialCdvInput):

    Returns:
        Response[Union[Any, List[Violation], PFFacialCdvResult]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        x_request_tag=x_request_tag,
        x_request_trace_id=x_request_trace_id,
        x_signature=x_signature,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: PFFacialCdvInput,
    x_request_tag: Union[Unset, str] = UNSET,
    x_request_trace_id: Union[Unset, str] = UNSET,
    x_signature: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List[Violation], PFFacialCdvResult]]:
    """Validation and returning OCR atributes of information extracted from the corresponding document

     It receives in the body of the request a key with the CPF of the individual (object
    <code>key</code>) and the object <code>answer</code> that contains the images of the front of the
    document (mandatory), the back of the document (optional) and the face (optional). All images must
    be sent encoded with <a href='https://pt.wikipedia.org/wiki/Base64'
    target='_blank'>Base64</a>.<br>Returns which document was identified and whether or not each of the
    data is valid, along with the probability and percentage of similarity for biometric
    validation.<br>For text type data, the percentage of similarity between the data extracted from the
    document and the official data available in government databases is also returned.<br>The biometric
    validation will be performed based on the portrait extracted from the document and the face sent
    (optional).<br><br>This named resource can be used to remotely validate a document.<br>The
    extraction of data of the document is not a deterministic resource, and it is up to the service user
    to use the values returned in the response to decide on the authenticity of the sent
    document.<br><br>Biometrics is not a deterministic resource, so it is up to the user using the
    service to use the values returned in the response to decide on the authenticity of the biometrics
    sent. In any case, it is important to mention that in tests performed, in approximately 99% of the
    validations that returned high or very high probability, the pair of biometrics compared were from
    the same person.

    Args:
        x_request_tag (Union[Unset, str]):
        x_request_trace_id (Union[Unset, str]):
        x_signature (Union[Unset, str]):
        json_body (PFFacialCdvInput):

    Returns:
        Response[Union[Any, List[Violation], PFFacialCdvResult]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
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
    json_body: PFFacialCdvInput,
    x_request_tag: Union[Unset, str] = UNSET,
    x_request_trace_id: Union[Unset, str] = UNSET,
    x_signature: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List[Violation], PFFacialCdvResult]]:
    """Validation and returning OCR atributes of information extracted from the corresponding document

     It receives in the body of the request a key with the CPF of the individual (object
    <code>key</code>) and the object <code>answer</code> that contains the images of the front of the
    document (mandatory), the back of the document (optional) and the face (optional). All images must
    be sent encoded with <a href='https://pt.wikipedia.org/wiki/Base64'
    target='_blank'>Base64</a>.<br>Returns which document was identified and whether or not each of the
    data is valid, along with the probability and percentage of similarity for biometric
    validation.<br>For text type data, the percentage of similarity between the data extracted from the
    document and the official data available in government databases is also returned.<br>The biometric
    validation will be performed based on the portrait extracted from the document and the face sent
    (optional).<br><br>This named resource can be used to remotely validate a document.<br>The
    extraction of data of the document is not a deterministic resource, and it is up to the service user
    to use the values returned in the response to decide on the authenticity of the sent
    document.<br><br>Biometrics is not a deterministic resource, so it is up to the user using the
    service to use the values returned in the response to decide on the authenticity of the biometrics
    sent. In any case, it is important to mention that in tests performed, in approximately 99% of the
    validations that returned high or very high probability, the pair of biometrics compared were from
    the same person.

    Args:
        x_request_tag (Union[Unset, str]):
        x_request_trace_id (Union[Unset, str]):
        x_signature (Union[Unset, str]):
        json_body (PFFacialCdvInput):

    Returns:
        Response[Union[Any, List[Violation], PFFacialCdvResult]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
        )
    ).parsed
