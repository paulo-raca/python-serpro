from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SituacaoCadastralResult")


@attr.s(auto_attribs=True)
class SituacaoCadastralResult:
    """
    Attributes:
        codigo (Union[Unset, bool]):
        data (Union[Unset, bool]):
        motivo (Union[Unset, bool]):
        motivo_similaridade (Union[Unset, float]):
    """

    codigo: Union[Unset, bool] = UNSET
    data: Union[Unset, bool] = UNSET
    motivo: Union[Unset, bool] = UNSET
    motivo_similaridade: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        codigo = self.codigo
        data = self.data
        motivo = self.motivo
        motivo_similaridade = self.motivo_similaridade

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if codigo is not UNSET:
            field_dict["codigo"] = codigo
        if data is not UNSET:
            field_dict["data"] = data
        if motivo is not UNSET:
            field_dict["motivo"] = motivo
        if motivo_similaridade is not UNSET:
            field_dict["motivo_similaridade"] = motivo_similaridade

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        codigo = d.pop("codigo", UNSET)

        data = d.pop("data", UNSET)

        motivo = d.pop("motivo", UNSET)

        motivo_similaridade = d.pop("motivo_similaridade", UNSET)

        situacao_cadastral_result = cls(
            codigo=codigo,
            data=data,
            motivo=motivo,
            motivo_similaridade=motivo_similaridade,
        )

        situacao_cadastral_result.additional_properties = d
        return situacao_cadastral_result

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
