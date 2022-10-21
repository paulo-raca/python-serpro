import pytest

from serpro import ConsultaCpf
from serpro.consulta_cpf.models import CPF

from .credentials import serpro_credentials


def test_demo_sync():
    consulta_cpf = ConsultaCpf.Sync(ConsultaCpf.TEST_ENDPOINT, token=ConsultaCpf.TEST_TOKEN)

    result = consulta_cpf.cpf.get_cpf_ni(ni="40442820135")
    assert isinstance(result, CPF)
    assert result.ni == "40442820135"
    assert result.nome == "Nome do CPF 404.428.201-35"
    assert result.situacao == {"codigo": "0", "descricao": "Regular"}
    assert result.nascimento == "14111970"


@pytest.mark.asyncio
async def test_demo_async():
    consulta_cpf = ConsultaCpf.Async(ConsultaCpf.TEST_ENDPOINT, token=ConsultaCpf.TEST_TOKEN)

    result = await consulta_cpf.cpf.get_cpf_ni(ni="40442820135")
    assert isinstance(result, CPF)
    assert result.ni == "40442820135"
    assert result.nome == "Nome do CPF 404.428.201-35"
    assert result.situacao == {"codigo": "0", "descricao": "Regular"}
    assert result.nascimento == "14111970"


def test_prod_sync():
    consulta_cpf = ConsultaCpf.Sync(ConsultaCpf.PROD_ENDPOINT, **serpro_credentials())

    result = consulta_cpf.cpf.get_cpf_ni(ni="91319218920")
    assert isinstance(result, CPF)
    assert result.ni == "91319218920"
    assert result.nome == "SILVIO SANTOS"
    # assert result.situacao == {"codigo": "0", "descricao": "Regular"}
    assert result.nascimento == "04061976"


@pytest.mark.asyncio
def test_prod_async():
    consulta_cpf = ConsultaCpf.Async(ConsultaCpf.PROD_ENDPOINT, **serpro_credentials())

    result = consulta_cpf.cpf.get_cpf_ni(ni="91319218920")
    assert isinstance(result, CPF)
    assert result.ni == "91319218920"
    assert result.nome == "SILVIO SANTOS"
    # assert result.situacao == {"codigo": "0", "descricao": "Regular"}
    assert result.nascimento == "04061976"
