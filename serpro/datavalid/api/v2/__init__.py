from inspect import isawaitable
from typing import Any, Awaitable, Callable, Dict, List, Optional, Union, cast

import attr

from ...client import Client
from ...models.integration import Integration
from ...models.pf_digitais_v2_input import PFDigitaisV2Input
from ...models.pf_digitais_v2_result import PFDigitaisV2Result
from ...models.pf_face_v2_input import PFFaceV2Input
from ...models.pf_face_v2_result import PFFaceV2Result
from ...models.pf_imagem_v2_input import PFImagemV2Input
from ...models.pf_imagem_v2_result import PFImagemV2Result
from ...models.pfv2_input import PFV2Input
from ...models.pfv2_result import PFV2Result
from ...models.pj_input import PJInput
from ...models.pj_result import PJResult
from ...models.violation import Violation
from ...types import UNSET, Response, Unset


@attr.s(auto_attribs=True)
class Endpoints:
    _client: Union[Client, Callable[[], Client]]

    def _get_client(self) -> Client:
        client = self._client
        if callable(client):
            client = client()
        return client

    def pf_1_detailed(
        self,
        *,
        json_body: PFV2Input,
        x_request_tag: Union[Unset, str] = UNSET,
        x_request_trace_id: Union[Unset, str] = UNSET,
        x_signature: Union[Unset, str] = UNSET,
    ) -> Response[Union[Any, List[Violation], PFV2Result]]:
        """Validation of the basic information of an individual

         It receives in the body of the request a key with the CPF of the individual (object
        <code>key</code>) and the data that will be validated (object <code>answer</code>) and returns if
        each data is or not valid.<br>For text type data, the percentage of similarity between the data sent
        and the official data available on government bases is also returned.

        Args:
            x_request_tag (Union[Unset, str]):
            x_request_trace_id (Union[Unset, str]):
            x_signature (Union[Unset, str]):
            json_body (PFV2Input):

        Returns:
            Response[Union[Any, List[Violation], PFV2Result]]
        """

        from . import pf_1 as _endpoint

        return _endpoint.sync_detailed(
            json_body=json_body,
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
            client=self._get_client(),
        )

    def pf_1(
        self,
        *,
        json_body: PFV2Input,
        x_request_tag: Union[Unset, str] = UNSET,
        x_request_trace_id: Union[Unset, str] = UNSET,
        x_signature: Union[Unset, str] = UNSET,
    ) -> Optional[Union[Any, List[Violation], PFV2Result]]:
        """Validation of the basic information of an individual

         It receives in the body of the request a key with the CPF of the individual (object
        <code>key</code>) and the data that will be validated (object <code>answer</code>) and returns if
        each data is or not valid.<br>For text type data, the percentage of similarity between the data sent
        and the official data available on government bases is also returned.

        Args:
            x_request_tag (Union[Unset, str]):
            x_request_trace_id (Union[Unset, str]):
            x_signature (Union[Unset, str]):
            json_body (PFV2Input):

        Returns:
            Response[Union[Any, List[Violation], PFV2Result]]
        """

        from . import pf_1 as _endpoint

        return _endpoint.sync(
            json_body=json_body,
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
            client=self._get_client(),
        )

    def pf_digitais_1_detailed(
        self,
        *,
        json_body: PFDigitaisV2Input,
        x_request_tag: Union[Unset, str] = UNSET,
        x_request_trace_id: Union[Unset, str] = UNSET,
        x_signature: Union[Unset, str] = UNSET,
    ) -> Response[Union[Any, List[Violation], PFDigitaisV2Result]]:
        """Validation of the basic information of an individual and the biometrics of the corresponding
        fingerprints

         It receives in the body of the request a key with the CPF of the individual (object
        <code>key</code>) and the data that will be validated (object <code>answer</code>) and returns if
        each data is or not valid.<br>For text type data, the percentage of similarity between the data sent
        and the official data available on government bases is also returned.<br><br>To perform biometrics
        digital, the attribute <code>digitais</code> inside the object is answer a String with one or more
        photos of the fingerprints encoded with <a href='https://wikipedia.org/wiki/Base64'
        target='_blank'>Base64</a>. The digital images sent must correspond to the fingers according to the
        following index:<br><table><thead><tr><th><b>Position</b></th><th><b>Corresponding
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
            json_body (PFDigitaisV2Input):

        Returns:
            Response[Union[Any, List[Violation], PFDigitaisV2Result]]
        """

        from . import pf_digitais_1 as _endpoint

        return _endpoint.sync_detailed(
            json_body=json_body,
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
            client=self._get_client(),
        )

    def pf_digitais_1(
        self,
        *,
        json_body: PFDigitaisV2Input,
        x_request_tag: Union[Unset, str] = UNSET,
        x_request_trace_id: Union[Unset, str] = UNSET,
        x_signature: Union[Unset, str] = UNSET,
    ) -> Optional[Union[Any, List[Violation], PFDigitaisV2Result]]:
        """Validation of the basic information of an individual and the biometrics of the corresponding
        fingerprints

         It receives in the body of the request a key with the CPF of the individual (object
        <code>key</code>) and the data that will be validated (object <code>answer</code>) and returns if
        each data is or not valid.<br>For text type data, the percentage of similarity between the data sent
        and the official data available on government bases is also returned.<br><br>To perform biometrics
        digital, the attribute <code>digitais</code> inside the object is answer a String with one or more
        photos of the fingerprints encoded with <a href='https://wikipedia.org/wiki/Base64'
        target='_blank'>Base64</a>. The digital images sent must correspond to the fingers according to the
        following index:<br><table><thead><tr><th><b>Position</b></th><th><b>Corresponding
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
            json_body (PFDigitaisV2Input):

        Returns:
            Response[Union[Any, List[Violation], PFDigitaisV2Result]]
        """

        from . import pf_digitais_1 as _endpoint

        return _endpoint.sync(
            json_body=json_body,
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
            client=self._get_client(),
        )

    def pf_face_1_detailed(
        self,
        *,
        json_body: PFFaceV2Input,
        x_request_tag: Union[Unset, str] = UNSET,
        x_request_trace_id: Union[Unset, str] = UNSET,
        x_signature: Union[Unset, str] = UNSET,
    ) -> Response[Union[Any, List[Violation], PFFaceV2Result]]:
        """Validation of the basic information of an individual and the biometry of the corresponding face

         It receives in the body of the request a key with the CPF of the individual (object
        <code>key</code>) and the data that will be validated (object <code>answer</code>) and returns if
        each data is or not valid.<br>For text type data, the percentage of similarity between the data sent
        and the official data available on government bases is also returned.<br><br>To perform facial
        biometrics, the attribute <code>biometria_face</code> inside the object is answer a String with the
        photo of the face  encoded with <a href='https://pt.wikipedia.org/wiki/Base64'
        target='_blank'>Base64</a>.<br><br>This so-called feature can be used to remotely validate a
        person's identity.<br>Biometrics is not a deterministic resource, so it is up to the user using the
        service to use the values returned in the response to decide on the authenticity of the biometrics
        sent. In any case, it is important to mention that in tests performed, in approximately 99% of the
        validations that returned high or very high probability, the pair of biometrics compared were from
        the same person.

        Args:
            x_request_tag (Union[Unset, str]):
            x_request_trace_id (Union[Unset, str]):
            x_signature (Union[Unset, str]):
            json_body (PFFaceV2Input):

        Returns:
            Response[Union[Any, List[Violation], PFFaceV2Result]]
        """

        from . import pf_face_1 as _endpoint

        return _endpoint.sync_detailed(
            json_body=json_body,
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
            client=self._get_client(),
        )

    def pf_face_1(
        self,
        *,
        json_body: PFFaceV2Input,
        x_request_tag: Union[Unset, str] = UNSET,
        x_request_trace_id: Union[Unset, str] = UNSET,
        x_signature: Union[Unset, str] = UNSET,
    ) -> Optional[Union[Any, List[Violation], PFFaceV2Result]]:
        """Validation of the basic information of an individual and the biometry of the corresponding face

         It receives in the body of the request a key with the CPF of the individual (object
        <code>key</code>) and the data that will be validated (object <code>answer</code>) and returns if
        each data is or not valid.<br>For text type data, the percentage of similarity between the data sent
        and the official data available on government bases is also returned.<br><br>To perform facial
        biometrics, the attribute <code>biometria_face</code> inside the object is answer a String with the
        photo of the face  encoded with <a href='https://pt.wikipedia.org/wiki/Base64'
        target='_blank'>Base64</a>.<br><br>This so-called feature can be used to remotely validate a
        person's identity.<br>Biometrics is not a deterministic resource, so it is up to the user using the
        service to use the values returned in the response to decide on the authenticity of the biometrics
        sent. In any case, it is important to mention that in tests performed, in approximately 99% of the
        validations that returned high or very high probability, the pair of biometrics compared were from
        the same person.

        Args:
            x_request_tag (Union[Unset, str]):
            x_request_trace_id (Union[Unset, str]):
            x_signature (Union[Unset, str]):
            json_body (PFFaceV2Input):

        Returns:
            Response[Union[Any, List[Violation], PFFaceV2Result]]
        """

        from . import pf_face_1 as _endpoint

        return _endpoint.sync(
            json_body=json_body,
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
            client=self._get_client(),
        )

    def pf_imagem_1_detailed(
        self,
        *,
        json_body: PFImagemV2Input,
        x_request_tag: Union[Unset, str] = UNSET,
        x_request_trace_id: Union[Unset, str] = UNSET,
        x_signature: Union[Unset, str] = UNSET,
    ) -> Response[Union[Any, List[Violation], PFImagemV2Result]]:
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
            json_body (PFImagemV2Input):

        Returns:
            Response[Union[Any, List[Violation], PFImagemV2Result]]
        """

        from . import pf_imagem_1 as _endpoint

        return _endpoint.sync_detailed(
            json_body=json_body,
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
            client=self._get_client(),
        )

    def pf_imagem_1(
        self,
        *,
        json_body: PFImagemV2Input,
        x_request_tag: Union[Unset, str] = UNSET,
        x_request_trace_id: Union[Unset, str] = UNSET,
        x_signature: Union[Unset, str] = UNSET,
    ) -> Optional[Union[Any, List[Violation], PFImagemV2Result]]:
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
            json_body (PFImagemV2Input):

        Returns:
            Response[Union[Any, List[Violation], PFImagemV2Result]]
        """

        from . import pf_imagem_1 as _endpoint

        return _endpoint.sync(
            json_body=json_body,
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
            client=self._get_client(),
        )

    def pj_1_detailed(
        self,
        *,
        json_body: PJInput,
        x_request_tag: Union[Unset, str] = UNSET,
        x_request_trace_id: Union[Unset, str] = UNSET,
        x_signature: Union[Unset, str] = UNSET,
    ) -> Response[Union[Any, List[Violation], PJResult]]:
        """Validation of the basic information of a legal entity

         It receives in the body of the request a key with the CNPJ of the legal entity (object <code> key
        </code>) and the data to be validated (object <code> answer </code>) and returns if each data is or
        not valid.<br>For text type data, the percentage of similarity between the data sent and the
        official data available on government bases is also returned.

        Args:
            x_request_tag (Union[Unset, str]):
            x_request_trace_id (Union[Unset, str]):
            x_signature (Union[Unset, str]):
            json_body (PJInput):

        Returns:
            Response[Union[Any, List[Violation], PJResult]]
        """

        from . import pj_1 as _endpoint

        return _endpoint.sync_detailed(
            json_body=json_body,
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
            client=self._get_client(),
        )

    def pj_1(
        self,
        *,
        json_body: PJInput,
        x_request_tag: Union[Unset, str] = UNSET,
        x_request_trace_id: Union[Unset, str] = UNSET,
        x_signature: Union[Unset, str] = UNSET,
    ) -> Optional[Union[Any, List[Violation], PJResult]]:
        """Validation of the basic information of a legal entity

         It receives in the body of the request a key with the CNPJ of the legal entity (object <code> key
        </code>) and the data to be validated (object <code> answer </code>) and returns if each data is or
        not valid.<br>For text type data, the percentage of similarity between the data sent and the
        official data available on government bases is also returned.

        Args:
            x_request_tag (Union[Unset, str]):
            x_request_trace_id (Union[Unset, str]):
            x_signature (Union[Unset, str]):
            json_body (PJInput):

        Returns:
            Response[Union[Any, List[Violation], PJResult]]
        """

        from . import pj_1 as _endpoint

        return _endpoint.sync(
            json_body=json_body,
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
            client=self._get_client(),
        )

    def get_1_detailed(
        self,
        *,
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

        from . import get_1 as _endpoint

        return _endpoint.sync_detailed(
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
            client=self._get_client(),
        )

    def get_1(
        self,
        *,
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

        from . import get_1 as _endpoint

        return _endpoint.sync(
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
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

    async def pf_1_detailed(
        self,
        *,
        json_body: PFV2Input,
        x_request_tag: Union[Unset, str] = UNSET,
        x_request_trace_id: Union[Unset, str] = UNSET,
        x_signature: Union[Unset, str] = UNSET,
    ) -> Response[Union[Any, List[Violation], PFV2Result]]:
        """Validation of the basic information of an individual

         It receives in the body of the request a key with the CPF of the individual (object
        <code>key</code>) and the data that will be validated (object <code>answer</code>) and returns if
        each data is or not valid.<br>For text type data, the percentage of similarity between the data sent
        and the official data available on government bases is also returned.

        Args:
            x_request_tag (Union[Unset, str]):
            x_request_trace_id (Union[Unset, str]):
            x_signature (Union[Unset, str]):
            json_body (PFV2Input):

        Returns:
            Response[Union[Any, List[Violation], PFV2Result]]
        """

        from . import pf_1 as _endpoint

        return await _endpoint.asyncio_detailed(
            json_body=json_body,
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
            client=await self._get_client(),
        )

    async def pf_1(
        self,
        *,
        json_body: PFV2Input,
        x_request_tag: Union[Unset, str] = UNSET,
        x_request_trace_id: Union[Unset, str] = UNSET,
        x_signature: Union[Unset, str] = UNSET,
    ) -> Optional[Union[Any, List[Violation], PFV2Result]]:
        """Validation of the basic information of an individual

         It receives in the body of the request a key with the CPF of the individual (object
        <code>key</code>) and the data that will be validated (object <code>answer</code>) and returns if
        each data is or not valid.<br>For text type data, the percentage of similarity between the data sent
        and the official data available on government bases is also returned.

        Args:
            x_request_tag (Union[Unset, str]):
            x_request_trace_id (Union[Unset, str]):
            x_signature (Union[Unset, str]):
            json_body (PFV2Input):

        Returns:
            Response[Union[Any, List[Violation], PFV2Result]]
        """

        from . import pf_1 as _endpoint

        return await _endpoint.asyncio(
            json_body=json_body,
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
            client=await self._get_client(),
        )

    async def pf_digitais_1_detailed(
        self,
        *,
        json_body: PFDigitaisV2Input,
        x_request_tag: Union[Unset, str] = UNSET,
        x_request_trace_id: Union[Unset, str] = UNSET,
        x_signature: Union[Unset, str] = UNSET,
    ) -> Response[Union[Any, List[Violation], PFDigitaisV2Result]]:
        """Validation of the basic information of an individual and the biometrics of the corresponding
        fingerprints

         It receives in the body of the request a key with the CPF of the individual (object
        <code>key</code>) and the data that will be validated (object <code>answer</code>) and returns if
        each data is or not valid.<br>For text type data, the percentage of similarity between the data sent
        and the official data available on government bases is also returned.<br><br>To perform biometrics
        digital, the attribute <code>digitais</code> inside the object is answer a String with one or more
        photos of the fingerprints encoded with <a href='https://wikipedia.org/wiki/Base64'
        target='_blank'>Base64</a>. The digital images sent must correspond to the fingers according to the
        following index:<br><table><thead><tr><th><b>Position</b></th><th><b>Corresponding
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
            json_body (PFDigitaisV2Input):

        Returns:
            Response[Union[Any, List[Violation], PFDigitaisV2Result]]
        """

        from . import pf_digitais_1 as _endpoint

        return await _endpoint.asyncio_detailed(
            json_body=json_body,
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
            client=await self._get_client(),
        )

    async def pf_digitais_1(
        self,
        *,
        json_body: PFDigitaisV2Input,
        x_request_tag: Union[Unset, str] = UNSET,
        x_request_trace_id: Union[Unset, str] = UNSET,
        x_signature: Union[Unset, str] = UNSET,
    ) -> Optional[Union[Any, List[Violation], PFDigitaisV2Result]]:
        """Validation of the basic information of an individual and the biometrics of the corresponding
        fingerprints

         It receives in the body of the request a key with the CPF of the individual (object
        <code>key</code>) and the data that will be validated (object <code>answer</code>) and returns if
        each data is or not valid.<br>For text type data, the percentage of similarity between the data sent
        and the official data available on government bases is also returned.<br><br>To perform biometrics
        digital, the attribute <code>digitais</code> inside the object is answer a String with one or more
        photos of the fingerprints encoded with <a href='https://wikipedia.org/wiki/Base64'
        target='_blank'>Base64</a>. The digital images sent must correspond to the fingers according to the
        following index:<br><table><thead><tr><th><b>Position</b></th><th><b>Corresponding
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
            json_body (PFDigitaisV2Input):

        Returns:
            Response[Union[Any, List[Violation], PFDigitaisV2Result]]
        """

        from . import pf_digitais_1 as _endpoint

        return await _endpoint.asyncio(
            json_body=json_body,
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
            client=await self._get_client(),
        )

    async def pf_face_1_detailed(
        self,
        *,
        json_body: PFFaceV2Input,
        x_request_tag: Union[Unset, str] = UNSET,
        x_request_trace_id: Union[Unset, str] = UNSET,
        x_signature: Union[Unset, str] = UNSET,
    ) -> Response[Union[Any, List[Violation], PFFaceV2Result]]:
        """Validation of the basic information of an individual and the biometry of the corresponding face

         It receives in the body of the request a key with the CPF of the individual (object
        <code>key</code>) and the data that will be validated (object <code>answer</code>) and returns if
        each data is or not valid.<br>For text type data, the percentage of similarity between the data sent
        and the official data available on government bases is also returned.<br><br>To perform facial
        biometrics, the attribute <code>biometria_face</code> inside the object is answer a String with the
        photo of the face  encoded with <a href='https://pt.wikipedia.org/wiki/Base64'
        target='_blank'>Base64</a>.<br><br>This so-called feature can be used to remotely validate a
        person's identity.<br>Biometrics is not a deterministic resource, so it is up to the user using the
        service to use the values returned in the response to decide on the authenticity of the biometrics
        sent. In any case, it is important to mention that in tests performed, in approximately 99% of the
        validations that returned high or very high probability, the pair of biometrics compared were from
        the same person.

        Args:
            x_request_tag (Union[Unset, str]):
            x_request_trace_id (Union[Unset, str]):
            x_signature (Union[Unset, str]):
            json_body (PFFaceV2Input):

        Returns:
            Response[Union[Any, List[Violation], PFFaceV2Result]]
        """

        from . import pf_face_1 as _endpoint

        return await _endpoint.asyncio_detailed(
            json_body=json_body,
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
            client=await self._get_client(),
        )

    async def pf_face_1(
        self,
        *,
        json_body: PFFaceV2Input,
        x_request_tag: Union[Unset, str] = UNSET,
        x_request_trace_id: Union[Unset, str] = UNSET,
        x_signature: Union[Unset, str] = UNSET,
    ) -> Optional[Union[Any, List[Violation], PFFaceV2Result]]:
        """Validation of the basic information of an individual and the biometry of the corresponding face

         It receives in the body of the request a key with the CPF of the individual (object
        <code>key</code>) and the data that will be validated (object <code>answer</code>) and returns if
        each data is or not valid.<br>For text type data, the percentage of similarity between the data sent
        and the official data available on government bases is also returned.<br><br>To perform facial
        biometrics, the attribute <code>biometria_face</code> inside the object is answer a String with the
        photo of the face  encoded with <a href='https://pt.wikipedia.org/wiki/Base64'
        target='_blank'>Base64</a>.<br><br>This so-called feature can be used to remotely validate a
        person's identity.<br>Biometrics is not a deterministic resource, so it is up to the user using the
        service to use the values returned in the response to decide on the authenticity of the biometrics
        sent. In any case, it is important to mention that in tests performed, in approximately 99% of the
        validations that returned high or very high probability, the pair of biometrics compared were from
        the same person.

        Args:
            x_request_tag (Union[Unset, str]):
            x_request_trace_id (Union[Unset, str]):
            x_signature (Union[Unset, str]):
            json_body (PFFaceV2Input):

        Returns:
            Response[Union[Any, List[Violation], PFFaceV2Result]]
        """

        from . import pf_face_1 as _endpoint

        return await _endpoint.asyncio(
            json_body=json_body,
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
            client=await self._get_client(),
        )

    async def pf_imagem_1_detailed(
        self,
        *,
        json_body: PFImagemV2Input,
        x_request_tag: Union[Unset, str] = UNSET,
        x_request_trace_id: Union[Unset, str] = UNSET,
        x_signature: Union[Unset, str] = UNSET,
    ) -> Response[Union[Any, List[Violation], PFImagemV2Result]]:
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
            json_body (PFImagemV2Input):

        Returns:
            Response[Union[Any, List[Violation], PFImagemV2Result]]
        """

        from . import pf_imagem_1 as _endpoint

        return await _endpoint.asyncio_detailed(
            json_body=json_body,
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
            client=await self._get_client(),
        )

    async def pf_imagem_1(
        self,
        *,
        json_body: PFImagemV2Input,
        x_request_tag: Union[Unset, str] = UNSET,
        x_request_trace_id: Union[Unset, str] = UNSET,
        x_signature: Union[Unset, str] = UNSET,
    ) -> Optional[Union[Any, List[Violation], PFImagemV2Result]]:
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
            json_body (PFImagemV2Input):

        Returns:
            Response[Union[Any, List[Violation], PFImagemV2Result]]
        """

        from . import pf_imagem_1 as _endpoint

        return await _endpoint.asyncio(
            json_body=json_body,
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
            client=await self._get_client(),
        )

    async def pj_1_detailed(
        self,
        *,
        json_body: PJInput,
        x_request_tag: Union[Unset, str] = UNSET,
        x_request_trace_id: Union[Unset, str] = UNSET,
        x_signature: Union[Unset, str] = UNSET,
    ) -> Response[Union[Any, List[Violation], PJResult]]:
        """Validation of the basic information of a legal entity

         It receives in the body of the request a key with the CNPJ of the legal entity (object <code> key
        </code>) and the data to be validated (object <code> answer </code>) and returns if each data is or
        not valid.<br>For text type data, the percentage of similarity between the data sent and the
        official data available on government bases is also returned.

        Args:
            x_request_tag (Union[Unset, str]):
            x_request_trace_id (Union[Unset, str]):
            x_signature (Union[Unset, str]):
            json_body (PJInput):

        Returns:
            Response[Union[Any, List[Violation], PJResult]]
        """

        from . import pj_1 as _endpoint

        return await _endpoint.asyncio_detailed(
            json_body=json_body,
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
            client=await self._get_client(),
        )

    async def pj_1(
        self,
        *,
        json_body: PJInput,
        x_request_tag: Union[Unset, str] = UNSET,
        x_request_trace_id: Union[Unset, str] = UNSET,
        x_signature: Union[Unset, str] = UNSET,
    ) -> Optional[Union[Any, List[Violation], PJResult]]:
        """Validation of the basic information of a legal entity

         It receives in the body of the request a key with the CNPJ of the legal entity (object <code> key
        </code>) and the data to be validated (object <code> answer </code>) and returns if each data is or
        not valid.<br>For text type data, the percentage of similarity between the data sent and the
        official data available on government bases is also returned.

        Args:
            x_request_tag (Union[Unset, str]):
            x_request_trace_id (Union[Unset, str]):
            x_signature (Union[Unset, str]):
            json_body (PJInput):

        Returns:
            Response[Union[Any, List[Violation], PJResult]]
        """

        from . import pj_1 as _endpoint

        return await _endpoint.asyncio(
            json_body=json_body,
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
            client=await self._get_client(),
        )

    async def get_1_detailed(
        self,
        *,
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

        from . import get_1 as _endpoint

        return await _endpoint.asyncio_detailed(
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
            client=await self._get_client(),
        )

    async def get_1(
        self,
        *,
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

        from . import get_1 as _endpoint

        return await _endpoint.asyncio(
            x_request_tag=x_request_tag,
            x_request_trace_id=x_request_trace_id,
            x_signature=x_signature,
            client=await self._get_client(),
        )
