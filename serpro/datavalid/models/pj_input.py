from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.pj_answer import PJAnswer
from ..models.pj_key import PJKey

T = TypeVar("T", bound="PJInput")


@attr.s(auto_attribs=True)
class PJInput:
    """
    Attributes:
        key (PJKey):
        answer (PJAnswer):
    """

    key: PJKey
    answer: PJAnswer
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key.to_dict()

        answer = self.answer.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "answer": answer,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = PJKey.from_dict(d.pop("key"))

        answer = PJAnswer.from_dict(d.pop("answer"))

        pj_input = cls(
            key=key,
            answer=answer,
        )

        pj_input.additional_properties = d
        return pj_input

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
