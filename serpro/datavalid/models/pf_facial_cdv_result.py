from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.cnh_cdv_result import CNHCdvResult
from ..models.face_result import FaceResult
from ..models.pf_facial_cdv_result_documento import PFFacialCdvResultDocumento
from ..types import UNSET, Unset

T = TypeVar("T", bound="PFFacialCdvResult")


@attr.s(auto_attribs=True)
class PFFacialCdvResult:
    """
    Attributes:
        documento (Union[Unset, PFFacialCdvResultDocumento]):
        cnh (Union[Unset, CNHCdvResult]):
        biometria_face (Union[Unset, FaceResult]):
    """

    documento: Union[Unset, PFFacialCdvResultDocumento] = UNSET
    cnh: Union[Unset, CNHCdvResult] = UNSET
    biometria_face: Union[Unset, FaceResult] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        documento: Union[Unset, str] = UNSET
        if not isinstance(self.documento, Unset):
            documento = self.documento.value

        cnh: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cnh, Unset):
            cnh = self.cnh.to_dict()

        biometria_face: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.biometria_face, Unset):
            biometria_face = self.biometria_face.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if documento is not UNSET:
            field_dict["documento"] = documento
        if cnh is not UNSET:
            field_dict["cnh"] = cnh
        if biometria_face is not UNSET:
            field_dict["biometria_face"] = biometria_face

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _documento = d.pop("documento", UNSET)
        documento: Union[Unset, PFFacialCdvResultDocumento]
        if isinstance(_documento, Unset):
            documento = UNSET
        else:
            documento = PFFacialCdvResultDocumento(_documento)

        _cnh = d.pop("cnh", UNSET)
        cnh: Union[Unset, CNHCdvResult]
        if isinstance(_cnh, Unset):
            cnh = UNSET
        else:
            cnh = CNHCdvResult.from_dict(_cnh)

        _biometria_face = d.pop("biometria_face", UNSET)
        biometria_face: Union[Unset, FaceResult]
        if isinstance(_biometria_face, Unset):
            biometria_face = UNSET
        else:
            biometria_face = FaceResult.from_dict(_biometria_face)

        pf_facial_cdv_result = cls(
            documento=documento,
            cnh=cnh,
            biometria_face=biometria_face,
        )

        pf_facial_cdv_result.additional_properties = d
        return pf_facial_cdv_result

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
