from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CPF")


@attr.s(auto_attribs=True)
class CPF:
    """
    Attributes:
        ni (Union[Unset, str]): Número de Inscrição do contribuinte Example: 99999999999.
        nome (Union[Unset, str]): Nome do contribuinte Example: PESSOA FISICA DA SILVA.
        situacao (Union[Unset, Any]):
        nascimento (Union[Unset, str]): Data de nascimento do contribuinte Example: 31011800.
        obito (Union[Unset, str]): Ano de óbito do contribuinte Example: 1800.
    """

    ni: Union[Unset, str] = UNSET
    nome: Union[Unset, str] = UNSET
    situacao: Union[Unset, Any] = UNSET
    nascimento: Union[Unset, str] = UNSET
    obito: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ni = self.ni
        nome = self.nome
        situacao = self.situacao
        nascimento = self.nascimento
        obito = self.obito

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ni is not UNSET:
            field_dict["ni"] = ni
        if nome is not UNSET:
            field_dict["nome"] = nome
        if situacao is not UNSET:
            field_dict["situacao"] = situacao
        if nascimento is not UNSET:
            field_dict["nascimento"] = nascimento
        if obito is not UNSET:
            field_dict["obito"] = obito

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ni = d.pop("ni", UNSET)

        nome = d.pop("nome", UNSET)

        situacao = d.pop("situacao", UNSET)

        nascimento = d.pop("nascimento", UNSET)

        obito = d.pop("obito", UNSET)

        cpf = cls(
            ni=ni,
            nome=nome,
            situacao=situacao,
            nascimento=nascimento,
            obito=obito,
        )

        cpf.additional_properties = d
        return cpf

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
