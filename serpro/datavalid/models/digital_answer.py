from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.digital_answer_formato import DigitalAnswerFormato
from ..models.digital_answer_posicao import DigitalAnswerPosicao
from ..types import UNSET, Unset

T = TypeVar("T", bound="DigitalAnswer")


@attr.s(auto_attribs=True)
class DigitalAnswer:
    """
    Attributes:
        posicao (Union[Unset, DigitalAnswerPosicao]): 0 - right hand thumb, 1 - right hand index, 2 - middle finger of
            the right hand, 3 - ring finger of the right hand, 4 - little finger of the right hand, 5 - left hand thumb, 6 -
            left hand index, 7 - middle finger of left hand, 8 - left hand ring finger, 9 - little finger of the left hand
        formato (Union[Unset, DigitalAnswerFormato]):
        base64 (Union[Unset, str]): Base64 encoded ISO, JPG, PNG or WSQ formats only without line breaks
    """

    posicao: Union[Unset, DigitalAnswerPosicao] = UNSET
    formato: Union[Unset, DigitalAnswerFormato] = UNSET
    base64: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        posicao: Union[Unset, int] = UNSET
        if not isinstance(self.posicao, Unset):
            posicao = self.posicao.value

        formato: Union[Unset, str] = UNSET
        if not isinstance(self.formato, Unset):
            formato = self.formato.value

        base64 = self.base64

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if posicao is not UNSET:
            field_dict["posicao"] = posicao
        if formato is not UNSET:
            field_dict["formato"] = formato
        if base64 is not UNSET:
            field_dict["base64"] = base64

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _posicao = d.pop("posicao", UNSET)
        posicao: Union[Unset, DigitalAnswerPosicao]
        if isinstance(_posicao, Unset):
            posicao = UNSET
        else:
            posicao = DigitalAnswerPosicao(_posicao)

        _formato = d.pop("formato", UNSET)
        formato: Union[Unset, DigitalAnswerFormato]
        if isinstance(_formato, Unset):
            formato = UNSET
        else:
            formato = DigitalAnswerFormato(_formato)

        base64 = d.pop("base64", UNSET)

        digital_answer = cls(
            posicao=posicao,
            formato=formato,
            base64=base64,
        )

        digital_answer.additional_properties = d
        return digital_answer

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
