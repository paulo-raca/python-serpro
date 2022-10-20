from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.endereco_answer_uf import EnderecoAnswerUf
from ..types import UNSET, Unset

T = TypeVar("T", bound="EnderecoAnswer")


@attr.s(auto_attribs=True)
class EnderecoAnswer:
    """
    Attributes:
        logradouro (Union[Unset, str]):
        numero (Union[Unset, str]):
        complemento (Union[Unset, str]):
        bairro (Union[Unset, str]):
        cep (Union[Unset, str]):
        municipio (Union[Unset, str]):
        uf (Union[Unset, EnderecoAnswerUf]): AC, AL, AM, AP, BA, CE, DF, ES, GO, MA, MT, MS, MG, PA, PB, PR, PE, PI, RJ,
            RN, RS, RO, RR, SC, SP, SE, TO
    """

    logradouro: Union[Unset, str] = UNSET
    numero: Union[Unset, str] = UNSET
    complemento: Union[Unset, str] = UNSET
    bairro: Union[Unset, str] = UNSET
    cep: Union[Unset, str] = UNSET
    municipio: Union[Unset, str] = UNSET
    uf: Union[Unset, EnderecoAnswerUf] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        logradouro = self.logradouro
        numero = self.numero
        complemento = self.complemento
        bairro = self.bairro
        cep = self.cep
        municipio = self.municipio
        uf: Union[Unset, str] = UNSET
        if not isinstance(self.uf, Unset):
            uf = self.uf.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if logradouro is not UNSET:
            field_dict["logradouro"] = logradouro
        if numero is not UNSET:
            field_dict["numero"] = numero
        if complemento is not UNSET:
            field_dict["complemento"] = complemento
        if bairro is not UNSET:
            field_dict["bairro"] = bairro
        if cep is not UNSET:
            field_dict["cep"] = cep
        if municipio is not UNSET:
            field_dict["municipio"] = municipio
        if uf is not UNSET:
            field_dict["uf"] = uf

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        logradouro = d.pop("logradouro", UNSET)

        numero = d.pop("numero", UNSET)

        complemento = d.pop("complemento", UNSET)

        bairro = d.pop("bairro", UNSET)

        cep = d.pop("cep", UNSET)

        municipio = d.pop("municipio", UNSET)

        _uf = d.pop("uf", UNSET)
        uf: Union[Unset, EnderecoAnswerUf]
        if isinstance(_uf, Unset):
            uf = UNSET
        else:
            uf = EnderecoAnswerUf(_uf)

        endereco_answer = cls(
            logradouro=logradouro,
            numero=numero,
            complemento=complemento,
            bairro=bairro,
            cep=cep,
            municipio=municipio,
            uf=uf,
        )

        endereco_answer.additional_properties = d
        return endereco_answer

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
