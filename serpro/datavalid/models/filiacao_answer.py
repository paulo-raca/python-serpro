from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FiliacaoAnswer")


@attr.s(auto_attribs=True)
class FiliacaoAnswer:
    """
    Attributes:
        nome_mae (Union[Unset, str]):
        nome_pai (Union[Unset, str]):
    """

    nome_mae: Union[Unset, str] = UNSET
    nome_pai: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nome_mae = self.nome_mae
        nome_pai = self.nome_pai

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nome_mae is not UNSET:
            field_dict["nome_mae"] = nome_mae
        if nome_pai is not UNSET:
            field_dict["nome_pai"] = nome_pai

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        nome_mae = d.pop("nome_mae", UNSET)

        nome_pai = d.pop("nome_pai", UNSET)

        filiacao_answer = cls(
            nome_mae=nome_mae,
            nome_pai=nome_pai,
        )

        filiacao_answer.additional_properties = d
        return filiacao_answer

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
