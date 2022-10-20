import asyncio
import base64
from datetime import date

import attr
import httpx

from serpro import ConsultaCpfApi, ConsultaCpfAsyncApi, DatavalidApi, DatavalidAsyncApi
from serpro.auth import SerproAuth
from serpro.datavalid.models.pf_basica_answer import PFBasicaAnswer
from serpro.datavalid.models.pf_basica_answer_sexo import PFBasicaAnswerSexo
from serpro.datavalid.models.pf_basica_input import PFBasicaInput
from serpro.datavalid.models.pf_key import PFKey

credentials = {
    "consumer_key": "...",
    "consumer_secret": "...",
}

async def main():
    consulta_cpf = ConsultaCpfAsyncApi(
        "https://gateway.apiserpro.serpro.gov.br/consulta-cpf-df/v1",
        **credentials
    )

    datavalid = DatavalidAsyncApi(
        "https://gateway.apiserpro.serpro.gov.br/datavalid",
        **credentials
    )

    print(
        "Consulta CPF", 
        await consulta_cpf.cpf.get_cpf_ni(ni="45317828791"))

    print(
        "datavalid.pf_basica",
        await datavalid.v3.pf_basica(
            json_body=PFBasicaInput(
                key=PFKey(cpf="453.178.287-91"),
                answer=PFBasicaAnswer(
                    nome="JAIR MESSIAS BOLSONARO", data_nascimento=date(1987, 10, 24), sexo=PFBasicaAnswerSexo.M
                ),
            )
        )
    )


asyncio.run(main())
