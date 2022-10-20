from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCpfNiResponse400")


@attr.s(auto_attribs=True)
class GetCpfNiResponse400:
    """
    Attributes:
        mensagem (Union[Unset, str]): Mensagem de retorno de validação Example: CPF <12345678901> inválido!.
    """

    mensagem: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mensagem = self.mensagem

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mensagem is not UNSET:
            field_dict["mensagem"] = mensagem

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mensagem = d.pop("mensagem", UNSET)

        get_cpf_ni_response_400 = cls(
            mensagem=mensagem,
        )

        get_cpf_ni_response_400.additional_properties = d
        return get_cpf_ni_response_400

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
