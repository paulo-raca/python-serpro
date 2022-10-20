import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.situacao_cadastral_answer_codigo import SituacaoCadastralAnswerCodigo
from ..types import UNSET, Unset

T = TypeVar("T", bound="SituacaoCadastralAnswer")


@attr.s(auto_attribs=True)
class SituacaoCadastralAnswer:
    """
    Attributes:
        codigo (Union[Unset, SituacaoCadastralAnswerCodigo]): 2 - ativa, 3 - suspensa, 4 - inapta, 8 - baixada
        data (Union[Unset, datetime.date]):
        motivo (Union[Unset, str]):
    """

    codigo: Union[Unset, SituacaoCadastralAnswerCodigo] = UNSET
    data: Union[Unset, datetime.date] = UNSET
    motivo: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        codigo: Union[Unset, int] = UNSET
        if not isinstance(self.codigo, Unset):
            codigo = self.codigo.value

        data: Union[Unset, str] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.isoformat()

        motivo = self.motivo

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if codigo is not UNSET:
            field_dict["codigo"] = codigo
        if data is not UNSET:
            field_dict["data"] = data
        if motivo is not UNSET:
            field_dict["motivo"] = motivo

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _codigo = d.pop("codigo", UNSET)
        codigo: Union[Unset, SituacaoCadastralAnswerCodigo]
        if isinstance(_codigo, Unset):
            codigo = UNSET
        else:
            codigo = SituacaoCadastralAnswerCodigo(_codigo)

        _data = d.pop("data", UNSET)
        data: Union[Unset, datetime.date]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = isoparse(_data).date()

        motivo = d.pop("motivo", UNSET)

        situacao_cadastral_answer = cls(
            codigo=codigo,
            data=data,
            motivo=motivo,
        )

        situacao_cadastral_answer.additional_properties = d
        return situacao_cadastral_answer

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
