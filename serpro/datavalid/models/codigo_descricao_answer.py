from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodigoDescricaoAnswer")


@attr.s(auto_attribs=True)
class CodigoDescricaoAnswer:
    """
    Attributes:
        codigo (Union[Unset, str]):
        descricao (Union[Unset, str]):
    """

    codigo: Union[Unset, str] = UNSET
    descricao: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        codigo = self.codigo
        descricao = self.descricao

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if codigo is not UNSET:
            field_dict["codigo"] = codigo
        if descricao is not UNSET:
            field_dict["descricao"] = descricao

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        codigo = d.pop("codigo", UNSET)

        descricao = d.pop("descricao", UNSET)

        codigo_descricao_answer = cls(
            codigo=codigo,
            descricao=descricao,
        )

        codigo_descricao_answer.additional_properties = d
        return codigo_descricao_answer

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
