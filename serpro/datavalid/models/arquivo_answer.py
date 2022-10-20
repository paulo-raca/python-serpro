from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.arquivo_answer_formato import ArquivoAnswerFormato
from ..types import UNSET, Unset

T = TypeVar("T", bound="ArquivoAnswer")


@attr.s(auto_attribs=True)
class ArquivoAnswer:
    """
    Attributes:
        formato (Union[Unset, ArquivoAnswerFormato]):
        base64 (Union[Unset, str]): Base64 encoded JPG, PDF or PNG formats only without line breaks
    """

    formato: Union[Unset, ArquivoAnswerFormato] = UNSET
    base64: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        formato: Union[Unset, str] = UNSET
        if not isinstance(self.formato, Unset):
            formato = self.formato.value

        base64 = self.base64

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if formato is not UNSET:
            field_dict["formato"] = formato
        if base64 is not UNSET:
            field_dict["base64"] = base64

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _formato = d.pop("formato", UNSET)
        formato: Union[Unset, ArquivoAnswerFormato]
        if isinstance(_formato, Unset):
            formato = UNSET
        else:
            formato = ArquivoAnswerFormato(_formato)

        base64 = d.pop("base64", UNSET)

        arquivo_answer = cls(
            formato=formato,
            base64=base64,
        )

        arquivo_answer.additional_properties = d
        return arquivo_answer

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
