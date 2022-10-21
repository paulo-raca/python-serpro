from datetime import date

import pytest

from serpro import Datavalid
from serpro.datavalid.models import PFBasicaAnswer, PFBasicaAnswerSexo, PFBasicaInput, PFBasicaResult, PFKey

from .credentials import serpro_credentials


def test_demo_sync():
    datavalid = Datavalid.Sync(Datavalid.TEST_ENDPOINT, token=Datavalid.TEST_TOKEN)

    result = datavalid.v3.pf_basica(
        json_body=PFBasicaInput(
            key=PFKey(cpf="257.744.350-16"),
            answer=PFBasicaAnswer(
                nome="Manuela Elisa da Mota",
                data_nascimento=date(1975, 6, 4),
                sexo=PFBasicaAnswerSexo.F,
            ),
        )
    )
    assert isinstance(result, PFBasicaResult)
    assert result.nome is True
    assert result.nome_similaridade == 1.0
    assert result.data_nascimento is True
    assert result.sexo is True


@pytest.mark.asyncio
async def test_demo_async():
    datavalid = Datavalid.Async(Datavalid.TEST_ENDPOINT, token=Datavalid.TEST_TOKEN)

    result = await datavalid.v3.pf_basica(
        json_body=PFBasicaInput(
            key=PFKey(cpf="257.744.350-16"),
            answer=PFBasicaAnswer(
                nome="Manuela Elisa da Mota",
                data_nascimento=date(1975, 6, 4),
                sexo=PFBasicaAnswerSexo.F,
            ),
        )
    )
    assert isinstance(result, PFBasicaResult)
    assert result.nome is True
    assert result.nome_similaridade == 1.0
    assert result.data_nascimento is True
    assert result.sexo is True


def test_prod_sync():
    datavalid = Datavalid.Sync(Datavalid.PROD_ENDPOINT, **serpro_credentials())

    result = datavalid.v3.pf_basica(
        json_body=PFBasicaInput(
            key=PFKey(cpf="913.192.189-20"),
            answer=PFBasicaAnswer(
                nome="Silvio Santos",
                data_nascimento=date(1976, 6, 4),
                sexo=PFBasicaAnswerSexo.M,
            ),
        )
    )
    assert isinstance(result, PFBasicaResult)
    assert result.nome is True
    assert result.nome_similaridade == 1.0
    assert result.data_nascimento is True
    assert result.sexo is True


@pytest.mark.asyncio
async def test_prod_async():
    datavalid = Datavalid.Async(Datavalid.PROD_ENDPOINT, **serpro_credentials())

    result = await datavalid.v3.pf_basica(
        json_body=PFBasicaInput(
            key=PFKey(cpf="913.192.189-20"),
            answer=PFBasicaAnswer(
                nome="Silvio Santos",
                data_nascimento=date(1976, 6, 4),
                sexo=PFBasicaAnswerSexo.M,
            ),
        )
    )
    assert isinstance(result, PFBasicaResult)
    assert result.nome is True
    assert result.nome_similaridade == 1.0
    assert result.data_nascimento is True
    assert result.sexo is True
    print(result)
