""" Contains methods for accessing the API """

from functools import cached_property
from typing import Awaitable, Callable, Union

import attr

from ..client import Client
from . import v1 as tag_v1
from . import v2 as tag_v2
from . import v3 as tag_v3
from . import vbeta1 as tag_vbeta1


@attr.s(auto_attribs=True)
class Api:
    _client: Union[Client, Callable[[], Client]]

    @cached_property
    def v1(self) -> tag_v1.Endpoints:
        """Group of endpoints tagged with v1"""
        return tag_v1.Endpoints(self._client)

    @cached_property
    def v2(self) -> tag_v2.Endpoints:
        """Group of endpoints tagged with v2"""
        return tag_v2.Endpoints(self._client)

    @cached_property
    def v3(self) -> tag_v3.Endpoints:
        """Group of endpoints tagged with v3"""
        return tag_v3.Endpoints(self._client)

    @cached_property
    def vbeta1(self) -> tag_vbeta1.Endpoints:
        """Group of endpoints tagged with vbeta1"""
        return tag_vbeta1.Endpoints(self._client)


@attr.s(auto_attribs=True)
class AsyncApi:
    _client: Union[Client, Callable[[], Client], Callable[[], Awaitable[Client]]]

    @cached_property
    def v1(self) -> tag_v1.Endpoints:
        """Group of endpoints tagged with v1"""
        return tag_v1.AsyncEndpoints(self._client)

    @cached_property
    def v2(self) -> tag_v2.Endpoints:
        """Group of endpoints tagged with v2"""
        return tag_v2.AsyncEndpoints(self._client)

    @cached_property
    def v3(self) -> tag_v3.Endpoints:
        """Group of endpoints tagged with v3"""
        return tag_v3.AsyncEndpoints(self._client)

    @cached_property
    def vbeta1(self) -> tag_vbeta1.Endpoints:
        """Group of endpoints tagged with vbeta1"""
        return tag_vbeta1.AsyncEndpoints(self._client)


__all__ = (
    "Api",
    "AsyncApi",
)
