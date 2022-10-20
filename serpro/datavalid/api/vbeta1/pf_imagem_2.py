from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.pf_imagem_vbeta_1_input import PFImagemVbeta1Input
from ...models.pf_imagem_vbeta_1_result import PFImagemVbeta1Result
from ...models.violation import Violation
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: PFImagemVbeta1Input,
    x_request_tag: Union[Unset, str] = UNSET,
    x_request_trace_id: Union[Unset, str] = UNSET,
    x_signature: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/vbeta1/validate/pf-imagem".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[Violation], PFImagemVbeta1Result]]:
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
        response_200 = PFImagemVbeta1Result.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[Violation], PFImagemVbeta1Result]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: PFImagemVbeta1Input,
    x_request_tag: Union[Unset, str] = UNSET,
    x_request_trace_id: Union[Unset, str] = UNSET,
    x_signature: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List[Violation], PFImagemVbeta1Result]]:
    """Validation of the basic information of an individual and the biometrics of the face and
    corresponding fingerprints

     It receives in the body of the request a key with the CPF of the individual (object
    <code>key</code>) and the data that will be validated (object <code>answer</code>) and returns if
    each data is or not valid.<br>For text type data, the percentage of similarity between the data sent
    and the official data available on government bases is also returned.<br><br>To perform digital and
    facial biometrics, the attributes are used respectively <code>digitais</code> and
    <code>biometria_face</code> within the object <code>answer</code> a String with the face photo
    and/or one or more photos of the fingerprints encoded with <a
    href='https://wikipedia.org/wiki/Base64' target='_blank'>Base64</a>. The digital images sent must
    correspond to the fingers according to the following
    index:<br><table><thead><tr><th><b>Position</b></th><th><b>Corresponding
    finger</b></th></tr></thead><tbody><tr><td>0</td><td>right hand
    thumb</td></tr><tr><td>1</td><td>right hand index</td></tr><tr><td>2</td><td>middle finger of the
    right hand</td></tr><tr><td>3</td><td>ring finger of the right
    hand</td></tr><tr><td>4</td><td>little finger of the right hand</td></tr><tr><td>5</td><td>left hand
    thumb</td></tr><tr><td>6</td><td>left hand index</td></tr><tr><td>7</td><td>middle finger of left
    hand</td></tr><tr><td>8</td><td>left hand ring finger</td></tr><tr><td>9</td><td>little finger of
    the left hand</td></tr></tbody></table><br><br>This so-called feature can be used to remotely
    validate a person's identity.<br>Biometrics is not a deterministic resource, so it is up to the user
    using the service to use the values returned in the response to decide on the authenticity of the
    biometrics sent. In any case, it is important to mention that in tests performed, in approximately
    99% of the validations that returned high or very high probability, the pair of biometrics compared
    were from the same person.

    Args:
        x_request_tag (Union[Unset, str]):
        x_request_trace_id (Union[Unset, str]):
        x_signature (Union[Unset, str]):
        json_body (PFImagemVbeta1Input):

    Returns:
        Response[Union[Any, List[Violation], PFImagemVbeta1Result]]
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
    json_body: PFImagemVbeta1Input,
    x_request_tag: Union[Unset, str] = UNSET,
    x_request_trace_id: Union[Unset, str] = UNSET,
    x_signature: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List[Violation], PFImagemVbeta1Result]]:
    """Validation of the basic information of an individual and the biometrics of the face and
    corresponding fingerprints

     It receives in the body of the request a key with the CPF of the individual (object
    <code>key</code>) and the data that will be validated (object <code>answer</code>) and returns if
    each data is or not valid.<br>For text type data, the percentage of similarity between the data sent
    and the official data available on government bases is also returned.<br><br>To perform digital and
    facial biometrics, the attributes are used respectively <code>digitais</code> and
    <code>biometria_face</code> within the object <code>answer</code> a String with the face photo
    and/or one or more photos of the fingerprints encoded with <a
    href='https://wikipedia.org/wiki/Base64' target='_blank'>Base64</a>. The digital images sent must
    correspond to the fingers according to the following
    index:<br><table><thead><tr><th><b>Position</b></th><th><b>Corresponding
    finger</b></th></tr></thead><tbody><tr><td>0</td><td>right hand
    thumb</td></tr><tr><td>1</td><td>right hand index</td></tr><tr><td>2</td><td>middle finger of the
    right hand</td></tr><tr><td>3</td><td>ring finger of the right
    hand</td></tr><tr><td>4</td><td>little finger of the right hand</td></tr><tr><td>5</td><td>left hand
    thumb</td></tr><tr><td>6</td><td>left hand index</td></tr><tr><td>7</td><td>middle finger of left
    hand</td></tr><tr><td>8</td><td>left hand ring finger</td></tr><tr><td>9</td><td>little finger of
    the left hand</td></tr></tbody></table><br><br>This so-called feature can be used to remotely
    validate a person's identity.<br>Biometrics is not a deterministic resource, so it is up to the user
    using the service to use the values returned in the response to decide on the authenticity of the
    biometrics sent. In any case, it is important to mention that in tests performed, in approximately
    99% of the validations that returned high or very high probability, the pair of biometrics compared
    were from the same person.

    Args:
        x_request_tag (Union[Unset, str]):
        x_request_trace_id (Union[Unset, str]):
        x_signature (Union[Unset, str]):
        json_body (PFImagemVbeta1Input):

    Returns:
        Response[Union[Any, List[Violation], PFImagemVbeta1Result]]
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
    json_body: PFImagemVbeta1Input,
    x_request_tag: Union[Unset, str] = UNSET,
    x_request_trace_id: Union[Unset, str] = UNSET,
    x_signature: Union[Unset, str] = UNSET,
) -> Response[Union[Any, List[Violation], PFImagemVbeta1Result]]:
    """Validation of the basic information of an individual and the biometrics of the face and
    corresponding fingerprints

     It receives in the body of the request a key with the CPF of the individual (object
    <code>key</code>) and the data that will be validated (object <code>answer</code>) and returns if
    each data is or not valid.<br>For text type data, the percentage of similarity between the data sent
    and the official data available on government bases is also returned.<br><br>To perform digital and
    facial biometrics, the attributes are used respectively <code>digitais</code> and
    <code>biometria_face</code> within the object <code>answer</code> a String with the face photo
    and/or one or more photos of the fingerprints encoded with <a
    href='https://wikipedia.org/wiki/Base64' target='_blank'>Base64</a>. The digital images sent must
    correspond to the fingers according to the following
    index:<br><table><thead><tr><th><b>Position</b></th><th><b>Corresponding
    finger</b></th></tr></thead><tbody><tr><td>0</td><td>right hand
    thumb</td></tr><tr><td>1</td><td>right hand index</td></tr><tr><td>2</td><td>middle finger of the
    right hand</td></tr><tr><td>3</td><td>ring finger of the right
    hand</td></tr><tr><td>4</td><td>little finger of the right hand</td></tr><tr><td>5</td><td>left hand
    thumb</td></tr><tr><td>6</td><td>left hand index</td></tr><tr><td>7</td><td>middle finger of left
    hand</td></tr><tr><td>8</td><td>left hand ring finger</td></tr><tr><td>9</td><td>little finger of
    the left hand</td></tr></tbody></table><br><br>This so-called feature can be used to remotely
    validate a person's identity.<br>Biometrics is not a deterministic resource, so it is up to the user
    using the service to use the values returned in the response to decide on the authenticity of the
    biometrics sent. In any case, it is important to mention that in tests performed, in approximately
    99% of the validations that returned high or very high probability, the pair of biometrics compared
    were from the same person.

    Args:
        x_request_tag (Union[Unset, str]):
        x_request_trace_id (Union[Unset, str]):
        x_signature (Union[Unset, str]):
        json_body (PFImagemVbeta1Input):

    Returns:
        Response[Union[Any, List[Violation], PFImagemVbeta1Result]]
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
    json_body: PFImagemVbeta1Input,
    x_request_tag: Union[Unset, str] = UNSET,
    x_request_trace_id: Union[Unset, str] = UNSET,
    x_signature: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, List[Violation], PFImagemVbeta1Result]]:
    """Validation of the basic information of an individual and the biometrics of the face and
    corresponding fingerprints

     It receives in the body of the request a key with the CPF of the individual (object
    <code>key</code>) and the data that will be validated (object <code>answer</code>) and returns if
    each data is or not valid.<br>For text type data, the percentage of similarity between the data sent
    and the official data available on government bases is also returned.<br><br>To perform digital and
    facial biometrics, the attributes are used respectively <code>digitais</code> and
    <code>biometria_face</code> within the object <code>answer</code> a String with the face photo
    and/or one or more photos of the fingerprints encoded with <a
    href='https://wikipedia.org/wiki/Base64' target='_blank'>Base64</a>. The digital images sent must
    correspond to the fingers according to the following
    index:<br><table><thead><tr><th><b>Position</b></th><th><b>Corresponding
    finger</b></th></tr></thead><tbody><tr><td>0</td><td>right hand
    thumb</td></tr><tr><td>1</td><td>right hand index</td></tr><tr><td>2</td><td>middle finger of the
    right hand</td></tr><tr><td>3</td><td>ring finger of the right
    hand</td></tr><tr><td>4</td><td>little finger of the right hand</td></tr><tr><td>5</td><td>left hand
    thumb</td></tr><tr><td>6</td><td>left hand index</td></tr><tr><td>7</td><td>middle finger of left
    hand</td></tr><tr><td>8</td><td>left hand ring finger</td></tr><tr><td>9</td><td>little finger of
    the left hand</td></tr></tbody></table><br><br>This so-called feature can be used to remotely
    validate a person's identity.<br>Biometrics is not a deterministic resource, so it is up to the user
    using the service to use the values returned in the response to decide on the authenticity of the
    biometrics sent. In any case, it is important to mention that in tests performed, in approximately
    99% of the validations that returned high or very high probability, the pair of biometrics compared
    were from the same person.

    Args:
        x_request_tag (Union[Unset, str]):
        x_request_trace_id (Union[Unset, str]):
        x_signature (Union[Unset, str]):
        json_body (PFImagemVbeta1Input):

    Returns:
        Response[Union[Any, List[Violation], PFImagemVbeta1Result]]
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
