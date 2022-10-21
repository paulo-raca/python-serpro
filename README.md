Neat python clients for serpro APIs

This project is just an OpenAPI wrapper for some of Serpro's APIs, built using [openapi-python-client](https://github.com/openapi-generators/openapi-python-client), which makes using these APIs very straightforward.

# Usage

## Instantiating the clients:
```
from serpro import ConsultaCpf, Datavalid

# Create clients
consulta_cpf = ConsultaCpf.Sync(ConsultaCpf.PROD_ENDPOINT, consumer_key=..., consumer_secret=...)
datavalid = Datavalid.Sync(Datavalid.PROD_ENDPOINT, consumer_key=..., consumer_secret=...)
```

### Demo endpoints

Serpro also provides test endpoints for evaluation and testing:

```
consulta_cpf = ConsultaCpf.Sync(ConsultaCpf.TEST_ENDPOINT, token=ConsultaCpf.TEST_TOKEN)
datavalid = Datavalid.Sync(Datavalid.TEST_ENDPOINT, token=Datavalid.TEST_TOKEN)
```

## Calling the endpoints

### Consulta CPF

```
result_cpf = consulta_cpf.cpf.get_cpf_ni(ni="91319218920")
print(result_cpf)
```
results in :
```
CPF(
    ni='91319218920', 
    nome='SILVIO SANTOS', 
    situacao={
        'codigo': '0', 
        'descricao': 'Regular'
    }, 
    nascimento='04061976', 
)
```

### Datavalid

```
result_datavalid = datavalid.v3.pf_basica(
    json_body=PFBasicaInput(
        key=PFKey(cpf="913.192.189-20"),
        answer=PFBasicaAnswer(
            nome="Silvio Santos",
            data_nascimento=date(1976, 6, 4),
            sexo=PFBasicaAnswerSexo.M,
        ),
    )
)
print(result_datavalid)
```

results in:
```
PFBasicaResult(
    cpf_disponivel=True, 
    nome=True, 
    nome_similaridade=1.0,
    data_nascimento=True, 
    sexo=True, 
    cnh_disponivel=True, 
    cnh=CNHResult(...), 
    filiacao=FiliacaoResult(...),
    documento=DocumentoResult(...),
    endereco=EnderecoResult(...)
)
```


## Async support

Yes! 

Just replace it with `ConsultaCpf.Async(...)` and `Datavalid.Async(...)`.

And use `await` when calling the endpoints:

```
consulta_cpf = ConsultaCpf.Async(...)
datavalid = Datavalid.Sync(...)

result_cpf = await consulta_cpf.cpf.get_cpf_ni(ni=...)
result_datavalid = await datavalid.v3.pf_basica(json_body=...)
```
