from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnderecoResult")


@attr.s(auto_attribs=True)
class EnderecoResult:
    """
    Attributes:
        logradouro (Union[Unset, bool]):
        logradouro_similaridade (Union[Unset, float]):
        complemento (Union[Unset, bool]):
        complemento_similaridade (Union[Unset, float]):
        numero (Union[Unset, bool]):
        numero_similaridade (Union[Unset, float]):
        bairro (Union[Unset, bool]):
        bairro_similaridade (Union[Unset, float]):
        cep (Union[Unset, bool]):
        municipio (Union[Unset, bool]):
        municipio_similaridade (Union[Unset, float]):
        uf (Union[Unset, bool]):
    """

    logradouro: Union[Unset, bool] = UNSET
    logradouro_similaridade: Union[Unset, float] = UNSET
    complemento: Union[Unset, bool] = UNSET
    complemento_similaridade: Union[Unset, float] = UNSET
    numero: Union[Unset, bool] = UNSET
    numero_similaridade: Union[Unset, float] = UNSET
    bairro: Union[Unset, bool] = UNSET
    bairro_similaridade: Union[Unset, float] = UNSET
    cep: Union[Unset, bool] = UNSET
    municipio: Union[Unset, bool] = UNSET
    municipio_similaridade: Union[Unset, float] = UNSET
    uf: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        logradouro = self.logradouro
        logradouro_similaridade = self.logradouro_similaridade
        complemento = self.complemento
        complemento_similaridade = self.complemento_similaridade
        numero = self.numero
        numero_similaridade = self.numero_similaridade
        bairro = self.bairro
        bairro_similaridade = self.bairro_similaridade
        cep = self.cep
        municipio = self.municipio
        municipio_similaridade = self.municipio_similaridade
        uf = self.uf

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logradouro is not UNSET:
            field_dict["logradouro"] = logradouro
        if logradouro_similaridade is not UNSET:
            field_dict["logradouro_similaridade"] = logradouro_similaridade
        if complemento is not UNSET:
            field_dict["complemento"] = complemento
        if complemento_similaridade is not UNSET:
            field_dict["complemento_similaridade"] = complemento_similaridade
        if numero is not UNSET:
            field_dict["numero"] = numero
        if numero_similaridade is not UNSET:
            field_dict["numero_similaridade"] = numero_similaridade
        if bairro is not UNSET:
            field_dict["bairro"] = bairro
        if bairro_similaridade is not UNSET:
            field_dict["bairro_similaridade"] = bairro_similaridade
        if cep is not UNSET:
            field_dict["cep"] = cep
        if municipio is not UNSET:
            field_dict["municipio"] = municipio
        if municipio_similaridade is not UNSET:
            field_dict["municipio_similaridade"] = municipio_similaridade
        if uf is not UNSET:
            field_dict["uf"] = uf

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        logradouro = d.pop("logradouro", UNSET)

        logradouro_similaridade = d.pop("logradouro_similaridade", UNSET)

        complemento = d.pop("complemento", UNSET)

        complemento_similaridade = d.pop("complemento_similaridade", UNSET)

        numero = d.pop("numero", UNSET)

        numero_similaridade = d.pop("numero_similaridade", UNSET)

        bairro = d.pop("bairro", UNSET)

        bairro_similaridade = d.pop("bairro_similaridade", UNSET)

        cep = d.pop("cep", UNSET)

        municipio = d.pop("municipio", UNSET)

        municipio_similaridade = d.pop("municipio_similaridade", UNSET)

        uf = d.pop("uf", UNSET)

        endereco_result = cls(
            logradouro=logradouro,
            logradouro_similaridade=logradouro_similaridade,
            complemento=complemento,
            complemento_similaridade=complemento_similaridade,
            numero=numero,
            numero_similaridade=numero_similaridade,
            bairro=bairro,
            bairro_similaridade=bairro_similaridade,
            cep=cep,
            municipio=municipio,
            municipio_similaridade=municipio_similaridade,
            uf=uf,
        )

        endereco_result.additional_properties = d
        return endereco_result

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
