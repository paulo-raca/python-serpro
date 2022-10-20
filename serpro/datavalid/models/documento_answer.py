from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.documento_answer_tipo import DocumentoAnswerTipo
from ..models.documento_answer_uf_expedidor import DocumentoAnswerUfExpedidor
from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentoAnswer")


@attr.s(auto_attribs=True)
class DocumentoAnswer:
    """
    Attributes:
        tipo (Union[Unset, DocumentoAnswerTipo]): 1 - identity card, 2 - professional card, 3 - passport, 4 - reservist
            card
        numero (Union[Unset, str]):
        orgao_expedidor (Union[Unset, str]):
        uf_expedidor (Union[Unset, DocumentoAnswerUfExpedidor]): AC, AL, AM, AP, BA, CE, DF, ES, GO, MA, MT, MS, MG, PA,
            PB, PR, PE, PI, RJ, RN, RS, RO, RR, SC, SP, SE, TO
    """

    tipo: Union[Unset, DocumentoAnswerTipo] = UNSET
    numero: Union[Unset, str] = UNSET
    orgao_expedidor: Union[Unset, str] = UNSET
    uf_expedidor: Union[Unset, DocumentoAnswerUfExpedidor] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tipo: Union[Unset, int] = UNSET
        if not isinstance(self.tipo, Unset):
            tipo = self.tipo.value

        numero = self.numero
        orgao_expedidor = self.orgao_expedidor
        uf_expedidor: Union[Unset, str] = UNSET
        if not isinstance(self.uf_expedidor, Unset):
            uf_expedidor = self.uf_expedidor.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if tipo is not UNSET:
            field_dict["tipo"] = tipo
        if numero is not UNSET:
            field_dict["numero"] = numero
        if orgao_expedidor is not UNSET:
            field_dict["orgao_expedidor"] = orgao_expedidor
        if uf_expedidor is not UNSET:
            field_dict["uf_expedidor"] = uf_expedidor

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _tipo = d.pop("tipo", UNSET)
        tipo: Union[Unset, DocumentoAnswerTipo]
        if isinstance(_tipo, Unset):
            tipo = UNSET
        else:
            tipo = DocumentoAnswerTipo(_tipo)

        numero = d.pop("numero", UNSET)

        orgao_expedidor = d.pop("orgao_expedidor", UNSET)

        _uf_expedidor = d.pop("uf_expedidor", UNSET)
        uf_expedidor: Union[Unset, DocumentoAnswerUfExpedidor]
        if isinstance(_uf_expedidor, Unset):
            uf_expedidor = UNSET
        else:
            uf_expedidor = DocumentoAnswerUfExpedidor(_uf_expedidor)

        documento_answer = cls(
            tipo=tipo,
            numero=numero,
            orgao_expedidor=orgao_expedidor,
            uf_expedidor=uf_expedidor,
        )

        documento_answer.additional_properties = d
        return documento_answer

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
