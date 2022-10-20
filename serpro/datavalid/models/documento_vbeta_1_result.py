from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentoVbeta1Result")


@attr.s(auto_attribs=True)
class DocumentoVbeta1Result:
    """
    Attributes:
        tipo (Union[Unset, bool]):
        numero (Union[Unset, bool]):
        orgao_expedidor (Union[Unset, bool]):
        uf_expedidor (Union[Unset, bool]):
    """

    tipo: Union[Unset, bool] = UNSET
    numero: Union[Unset, bool] = UNSET
    orgao_expedidor: Union[Unset, bool] = UNSET
    uf_expedidor: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tipo = self.tipo
        numero = self.numero
        orgao_expedidor = self.orgao_expedidor
        uf_expedidor = self.uf_expedidor

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
        tipo = d.pop("tipo", UNSET)

        numero = d.pop("numero", UNSET)

        orgao_expedidor = d.pop("orgao_expedidor", UNSET)

        uf_expedidor = d.pop("uf_expedidor", UNSET)

        documento_vbeta_1_result = cls(
            tipo=tipo,
            numero=numero,
            orgao_expedidor=orgao_expedidor,
            uf_expedidor=uf_expedidor,
        )

        documento_vbeta_1_result.additional_properties = d
        return documento_vbeta_1_result

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
