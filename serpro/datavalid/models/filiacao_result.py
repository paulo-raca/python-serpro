from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FiliacaoResult")


@attr.s(auto_attribs=True)
class FiliacaoResult:
    """
    Attributes:
        nome_mae (Union[Unset, bool]):
        nome_mae_similaridade (Union[Unset, float]):
        nome_pai (Union[Unset, bool]):
        nome_pai_similaridade (Union[Unset, float]):
    """

    nome_mae: Union[Unset, bool] = UNSET
    nome_mae_similaridade: Union[Unset, float] = UNSET
    nome_pai: Union[Unset, bool] = UNSET
    nome_pai_similaridade: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nome_mae = self.nome_mae
        nome_mae_similaridade = self.nome_mae_similaridade
        nome_pai = self.nome_pai
        nome_pai_similaridade = self.nome_pai_similaridade

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nome_mae is not UNSET:
            field_dict["nome_mae"] = nome_mae
        if nome_mae_similaridade is not UNSET:
            field_dict["nome_mae_similaridade"] = nome_mae_similaridade
        if nome_pai is not UNSET:
            field_dict["nome_pai"] = nome_pai
        if nome_pai_similaridade is not UNSET:
            field_dict["nome_pai_similaridade"] = nome_pai_similaridade

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        nome_mae = d.pop("nome_mae", UNSET)

        nome_mae_similaridade = d.pop("nome_mae_similaridade", UNSET)

        nome_pai = d.pop("nome_pai", UNSET)

        nome_pai_similaridade = d.pop("nome_pai_similaridade", UNSET)

        filiacao_result = cls(
            nome_mae=nome_mae,
            nome_mae_similaridade=nome_mae_similaridade,
            nome_pai=nome_pai,
            nome_pai_similaridade=nome_pai_similaridade,
        )

        filiacao_result.additional_properties = d
        return filiacao_result

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
