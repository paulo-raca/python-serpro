""" Contains methods for accessing the API """

from functools import cached_property
from typing import Awaitable, Callable, Union

import attr

from ..client import Client
from . import cpf as tag_cpf
from . import status as tag_status


@attr.s(auto_attribs=True)
class SyncApi:
    _client: Union[Client, Callable[[], Client]]

    @cached_property
    def cpf(self) -> tag_cpf.Endpoints:
        """Group of endpoints tagged with cpf"""
        return tag_cpf.Endpoints(self._client)

    @cached_property
    def status(self) -> tag_status.Endpoints:
        """Group of endpoints tagged with status"""
        return tag_status.Endpoints(self._client)


@attr.s(auto_attribs=True)
class AsyncApi:
    _client: Union[Client, Callable[[], Client], Callable[[], Awaitable[Client]]]

    @cached_property
    def cpf(self) -> tag_cpf.AsyncEndpoints:
        """Group of endpoints tagged with cpf"""
        return tag_cpf.AsyncEndpoints(self._client)

    @cached_property
    def status(self) -> tag_status.AsyncEndpoints:
        """Group of endpoints tagged with status"""
        return tag_status.AsyncEndpoints(self._client)


__all__ = (
    "Api",
    "AsyncApi",
)
