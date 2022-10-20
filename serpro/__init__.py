from serpro import consulta_cpf, datavalid

from .auth import AuthApiMixin


class DatavalidApi(AuthApiMixin, datavalid.Api):
    ...


class DatavalidAsyncApi(AuthApiMixin, datavalid.AsyncApi):
    ...


class ConsultaCpfApi(AuthApiMixin, consulta_cpf.Api):
    ...


class ConsultaCpfAsyncApi(AuthApiMixin, consulta_cpf.AsyncApi):
    ...
