from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TelefoneAnswer")


@attr.s(auto_attribs=True)
class TelefoneAnswer:
    """
    Attributes:
        ddd (Union[Unset, str]):
        numero (Union[Unset, str]):
    """

    ddd: Union[Unset, str] = UNSET
    numero: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ddd = self.ddd
        numero = self.numero

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ddd is not UNSET:
            field_dict["ddd"] = ddd
        if numero is not UNSET:
            field_dict["numero"] = numero

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ddd = d.pop("ddd", UNSET)

        numero = d.pop("numero", UNSET)

        telefone_answer = cls(
            ddd=ddd,
            numero=numero,
        )

        telefone_answer.additional_properties = d
        return telefone_answer

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
