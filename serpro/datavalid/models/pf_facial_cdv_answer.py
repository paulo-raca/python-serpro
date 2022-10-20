from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.arquivo_answer import ArquivoAnswer
from ..models.face_answer import FaceAnswer
from ..types import UNSET, Unset

T = TypeVar("T", bound="PFFacialCdvAnswer")


@attr.s(auto_attribs=True)
class PFFacialCdvAnswer:
    """
    Attributes:
        documento (Union[Unset, ArquivoAnswer]):
        documento_verso (Union[Unset, ArquivoAnswer]):
        biometria_face (Union[Unset, FaceAnswer]):
    """

    documento: Union[Unset, ArquivoAnswer] = UNSET
    documento_verso: Union[Unset, ArquivoAnswer] = UNSET
    biometria_face: Union[Unset, FaceAnswer] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        documento: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.documento, Unset):
            documento = self.documento.to_dict()

        documento_verso: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.documento_verso, Unset):
            documento_verso = self.documento_verso.to_dict()

        biometria_face: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.biometria_face, Unset):
            biometria_face = self.biometria_face.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if documento is not UNSET:
            field_dict["documento"] = documento
        if documento_verso is not UNSET:
            field_dict["documento_verso"] = documento_verso
        if biometria_face is not UNSET:
            field_dict["biometria_face"] = biometria_face

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _documento = d.pop("documento", UNSET)
        documento: Union[Unset, ArquivoAnswer]
        if isinstance(_documento, Unset):
            documento = UNSET
        else:
            documento = ArquivoAnswer.from_dict(_documento)

        _documento_verso = d.pop("documento_verso", UNSET)
        documento_verso: Union[Unset, ArquivoAnswer]
        if isinstance(_documento_verso, Unset):
            documento_verso = UNSET
        else:
            documento_verso = ArquivoAnswer.from_dict(_documento_verso)

        _biometria_face = d.pop("biometria_face", UNSET)
        biometria_face: Union[Unset, FaceAnswer]
        if isinstance(_biometria_face, Unset):
            biometria_face = UNSET
        else:
            biometria_face = FaceAnswer.from_dict(_biometria_face)

        pf_facial_cdv_answer = cls(
            documento=documento,
            documento_verso=documento_verso,
            biometria_face=biometria_face,
        )

        pf_facial_cdv_answer.additional_properties = d
        return pf_facial_cdv_answer

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
