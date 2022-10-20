from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.pf_key import PFKey
from ..models.pf_vbeta_1_answer import PFVbeta1Answer

T = TypeVar("T", bound="PFVbeta1Input")


@attr.s(auto_attribs=True)
class PFVbeta1Input:
    """
    Attributes:
        key (PFKey):
        answer (PFVbeta1Answer):
    """

    key: PFKey
    answer: PFVbeta1Answer
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
        key = PFKey.from_dict(d.pop("key"))

        answer = PFVbeta1Answer.from_dict(d.pop("answer"))

        pf_vbeta_1_input = cls(
            key=key,
            answer=answer,
        )

        pf_vbeta_1_input.additional_properties = d
        return pf_vbeta_1_input

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
