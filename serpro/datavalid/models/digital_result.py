from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.digital_result_posicao import DigitalResultPosicao
from ..models.digital_result_probabilidade import DigitalResultProbabilidade
from ..types import UNSET, Unset

T = TypeVar("T", bound="DigitalResult")


@attr.s(auto_attribs=True)
class DigitalResult:
    """
    Attributes:
        posicao (Union[Unset, DigitalResultPosicao]): 0 - right hand thumb, 1 - right hand index, 2 - middle finger of
            the right hand, 3 - ring finger of the right hand, 4 - little finger of the right hand, 5 - left hand thumb, 6 -
            left hand index, 7 - middle finger of left hand, 8 - left hand ring finger, 9 - little finger of the left hand
        probabilidade (Union[Unset, DigitalResultProbabilidade]): Altíssima probabilidade, Alta probabilidade, Baixa
            probabilidade, Baixíssima probabilidade
        similaridade (Union[Unset, float]):
    """

    posicao: Union[Unset, DigitalResultPosicao] = UNSET
    probabilidade: Union[Unset, DigitalResultProbabilidade] = UNSET
    similaridade: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        posicao: Union[Unset, int] = UNSET
        if not isinstance(self.posicao, Unset):
            posicao = self.posicao.value

        probabilidade: Union[Unset, str] = UNSET
        if not isinstance(self.probabilidade, Unset):
            probabilidade = self.probabilidade.value

        similaridade = self.similaridade

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if posicao is not UNSET:
            field_dict["posicao"] = posicao
        if probabilidade is not UNSET:
            field_dict["probabilidade"] = probabilidade
        if similaridade is not UNSET:
            field_dict["similaridade"] = similaridade

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _posicao = d.pop("posicao", UNSET)
        posicao: Union[Unset, DigitalResultPosicao]
        if isinstance(_posicao, Unset):
            posicao = UNSET
        else:
            posicao = DigitalResultPosicao(_posicao)

        _probabilidade = d.pop("probabilidade", UNSET)
        probabilidade: Union[Unset, DigitalResultProbabilidade]
        if isinstance(_probabilidade, Unset):
            probabilidade = UNSET
        else:
            probabilidade = DigitalResultProbabilidade(_probabilidade)

        similaridade = d.pop("similaridade", UNSET)

        digital_result = cls(
            posicao=posicao,
            probabilidade=probabilidade,
            similaridade=similaridade,
        )

        digital_result.additional_properties = d
        return digital_result

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
