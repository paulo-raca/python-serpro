from serpro import consulta_cpf, datavalid

from .auth import AuthApiMixin


# Consulta CPF
class ConsultaCpf:
    """
    Client para a API de consulta de CPF

    Documentação: https://apicenter.estaleiro.serpro.gov.br/documentacao/consulta-cpf
    Descriptor OpenAPI: https://apidocs.datavalidp.estaleiro.serpro.gov.br/api-doc/
    """

    PROD_ENDPOINT = "https://gateway.apiserpro.serpro.gov.br/consulta-cpf-df/v1"
    TEST_ENDPOINT = "https://gateway.apiserpro.serpro.gov.br/consulta-cpf-df-trial/v1"
    TEST_TOKEN = "06aef429-a981-3ec5-a1f8-71d38d86481e"

    class Sync(AuthApiMixin, consulta_cpf.SyncApi):
        ...

    class Async(AuthApiMixin, consulta_cpf.AsyncApi):
        ...


# Datavalid
class Datavalid:
    """
    Client para a API de validação de dados cadastrais Datavalid

    Documentação: https://apidocs.datavalidp.estaleiro.serpro.gov.br/
    Descriptor OpenAPI: https://apicenter.estaleiro.serpro.gov.br/documentacao/dist/swaggers/consulta-cpf-df.yaml
    """

    PROD_ENDPOINT = "https://gateway.apiserpro.serpro.gov.br/datavalid"
    TEST_ENDPOINT = "https://gateway.apiserpro.serpro.gov.br/datavalid-demonstracao"
    TEST_TOKEN = "06aef429-a981-3ec5-a1f8-71d38d86481e"

    class Sync(AuthApiMixin, datavalid.SyncApi):
        ...

    class Async(AuthApiMixin, datavalid.AsyncApi):
        ...
