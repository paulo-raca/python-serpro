""" A client library for accessing Consulta CPF """
from .api import AsyncApi, SyncApi
from .client import AuthenticatedClient, Client

__all__ = (
    "Client",
    "AuthenticatedClient",
    "SyncApi",
    "AsyncApi",
)
