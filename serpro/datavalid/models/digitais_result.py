from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.digital_result import DigitalResult
from ..types import UNSET, Unset

T = TypeVar("T", bound="DigitaisResult")


@attr.s(auto_attribs=True)
class DigitaisResult:
    """
    Attributes:
        disponivel (Union[Unset, bool]): Indicates whether there are fingerprints biometrics for the CPF on the official
            government base
        digitais (Union[Unset, List[DigitalResult]]):
    """

    disponivel: Union[Unset, bool] = UNSET
    digitais: Union[Unset, List[DigitalResult]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        disponivel = self.disponivel
        digitais: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.digitais, Unset):
            digitais = []
            for digitais_item_data in self.digitais:
                digitais_item = digitais_item_data.to_dict()

                digitais.append(digitais_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disponivel is not UNSET:
            field_dict["disponivel"] = disponivel
        if digitais is not UNSET:
            field_dict["digitais"] = digitais

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        disponivel = d.pop("disponivel", UNSET)

        digitais = []
        _digitais = d.pop("digitais", UNSET)
        for digitais_item_data in _digitais or []:
            digitais_item = DigitalResult.from_dict(digitais_item_data)

            digitais.append(digitais_item)

        digitais_result = cls(
            disponivel=disponivel,
            digitais=digitais,
        )

        digitais_result.additional_properties = d
        return digitais_result

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
