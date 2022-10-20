from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.face_result_probabilidade import FaceResultProbabilidade
from ..types import UNSET, Unset

T = TypeVar("T", bound="FaceResult")


@attr.s(auto_attribs=True)
class FaceResult:
    """
    Attributes:
        disponivel (Union[Unset, bool]): Indicates whether there is face biometry for the CPF at the official government
            base
        probabilidade (Union[Unset, FaceResultProbabilidade]): Altíssima probabilidade, Alta probabilidade, Baixa
            probabilidade, Baixíssima probabilidade
        similaridade (Union[Unset, float]):
    """

    disponivel: Union[Unset, bool] = UNSET
    probabilidade: Union[Unset, FaceResultProbabilidade] = UNSET
    similaridade: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        disponivel = self.disponivel
        probabilidade: Union[Unset, str] = UNSET
        if not isinstance(self.probabilidade, Unset):
            probabilidade = self.probabilidade.value

        similaridade = self.similaridade

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if disponivel is not UNSET:
            field_dict["disponivel"] = disponivel
        if probabilidade is not UNSET:
            field_dict["probabilidade"] = probabilidade
        if similaridade is not UNSET:
            field_dict["similaridade"] = similaridade

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        disponivel = d.pop("disponivel", UNSET)

        _probabilidade = d.pop("probabilidade", UNSET)
        probabilidade: Union[Unset, FaceResultProbabilidade]
        if isinstance(_probabilidade, Unset):
            probabilidade = UNSET
        else:
            probabilidade = FaceResultProbabilidade(_probabilidade)

        similaridade = d.pop("similaridade", UNSET)

        face_result = cls(
            disponivel=disponivel,
            probabilidade=probabilidade,
            similaridade=similaridade,
        )

        face_result.additional_properties = d
        return face_result

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
