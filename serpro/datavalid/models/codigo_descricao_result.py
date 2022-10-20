from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodigoDescricaoResult")


@attr.s(auto_attribs=True)
class CodigoDescricaoResult:
    """
    Attributes:
        codigo (Union[Unset, bool]):
        descricao (Union[Unset, bool]):
        descricao_similaridade (Union[Unset, float]):
    """

    codigo: Union[Unset, bool] = UNSET
    descricao: Union[Unset, bool] = UNSET
    descricao_similaridade: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        codigo = self.codigo
        descricao = self.descricao
        descricao_similaridade = self.descricao_similaridade

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if codigo is not UNSET:
            field_dict["codigo"] = codigo
        if descricao is not UNSET:
            field_dict["descricao"] = descricao
        if descricao_similaridade is not UNSET:
            field_dict["descricao_similaridade"] = descricao_similaridade

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        codigo = d.pop("codigo", UNSET)

        descricao = d.pop("descricao", UNSET)

        descricao_similaridade = d.pop("descricao_similaridade", UNSET)

        codigo_descricao_result = cls(
            codigo=codigo,
            descricao=descricao,
            descricao_similaridade=descricao_similaridade,
        )

        codigo_descricao_result.additional_properties = d
        return codigo_descricao_result

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
