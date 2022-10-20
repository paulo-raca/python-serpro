cd serpro
rm -rf datavalid consulta_cpf
openapi-python-client generate --config ../datavalid.yaml --meta none --url https://apidocs.datavalidp.estaleiro.serpro.gov.br/api-doc/?lang=en
openapi-python-client generate --config ../consulta_cpf.yaml --meta none --url https://apicenter.estaleiro.serpro.gov.br/documentacao/dist/swaggers/consulta-cpf-df.yaml
