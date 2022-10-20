import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CNHBiometryVbeta1Answer")


@attr.s(auto_attribs=True)
class CNHBiometryVbeta1Answer:
    """
    Attributes:
        categoria (Union[Unset, str]):
        numero_registro (Union[Unset, str]):
        data_primeira_habilitacao (Union[Unset, datetime.date]):
        data_validade (Union[Unset, datetime.date]):
    """

    categoria: Union[Unset, str] = UNSET
    numero_registro: Union[Unset, str] = UNSET
    data_primeira_habilitacao: Union[Unset, datetime.date] = UNSET
    data_validade: Union[Unset, datetime.date] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        categoria = self.categoria
        numero_registro = self.numero_registro
        data_primeira_habilitacao: Union[Unset, str] = UNSET
        if not isinstance(self.data_primeira_habilitacao, Unset):
            data_primeira_habilitacao = self.data_primeira_habilitacao.isoformat()

        data_validade: Union[Unset, str] = UNSET
        if not isinstance(self.data_validade, Unset):
            data_validade = self.data_validade.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categoria is not UNSET:
            field_dict["categoria"] = categoria
        if numero_registro is not UNSET:
            field_dict["numero_registro"] = numero_registro
        if data_primeira_habilitacao is not UNSET:
            field_dict["data_primeira_habilitacao"] = data_primeira_habilitacao
        if data_validade is not UNSET:
            field_dict["data_validade"] = data_validade

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        categoria = d.pop("categoria", UNSET)

        numero_registro = d.pop("numero_registro", UNSET)

        _data_primeira_habilitacao = d.pop("data_primeira_habilitacao", UNSET)
        data_primeira_habilitacao: Union[Unset, datetime.date]
        if isinstance(_data_primeira_habilitacao, Unset):
            data_primeira_habilitacao = UNSET
        else:
            data_primeira_habilitacao = isoparse(_data_primeira_habilitacao).date()

        _data_validade = d.pop("data_validade", UNSET)
        data_validade: Union[Unset, datetime.date]
        if isinstance(_data_validade, Unset):
            data_validade = UNSET
        else:
            data_validade = isoparse(_data_validade).date()

        cnh_biometry_vbeta_1_answer = cls(
            categoria=categoria,
            numero_registro=numero_registro,
            data_primeira_habilitacao=data_primeira_habilitacao,
            data_validade=data_validade,
        )

        cnh_biometry_vbeta_1_answer.additional_properties = d
        return cnh_biometry_vbeta_1_answer

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
