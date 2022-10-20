import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.face_result import FaceResult
from ..types import UNSET, Unset

T = TypeVar("T", bound="CNHCdvResult")


@attr.s(auto_attribs=True)
class CNHCdvResult:
    """
    Attributes:
        numero_registro (Union[Unset, bool]):
        numero_registro_ocr (Union[Unset, str]):
        nome (Union[Unset, bool]):
        nome_similaridade (Union[Unset, float]):
        nome_ocr (Union[Unset, str]):
        identidade (Union[Unset, bool]):
        identidade_similaridade (Union[Unset, float]):
        identidade_ocr (Union[Unset, str]):
        data_nascimento (Union[Unset, bool]):
        data_nascimento_ocr (Union[Unset, datetime.date]):
        data_primeira_habilitacao (Union[Unset, bool]):
        data_primeira_habilitacao_ocr (Union[Unset, datetime.date]):
        data_ultima_emissao (Union[Unset, bool]):
        data_ultima_emissao_ocr (Union[Unset, datetime.date]):
        data_validade (Union[Unset, bool]):
        data_validade_ocr (Union[Unset, datetime.date]):
        retrato (Union[Unset, FaceResult]):
    """

    numero_registro: Union[Unset, bool] = UNSET
    numero_registro_ocr: Union[Unset, str] = UNSET
    nome: Union[Unset, bool] = UNSET
    nome_similaridade: Union[Unset, float] = UNSET
    nome_ocr: Union[Unset, str] = UNSET
    identidade: Union[Unset, bool] = UNSET
    identidade_similaridade: Union[Unset, float] = UNSET
    identidade_ocr: Union[Unset, str] = UNSET
    data_nascimento: Union[Unset, bool] = UNSET
    data_nascimento_ocr: Union[Unset, datetime.date] = UNSET
    data_primeira_habilitacao: Union[Unset, bool] = UNSET
    data_primeira_habilitacao_ocr: Union[Unset, datetime.date] = UNSET
    data_ultima_emissao: Union[Unset, bool] = UNSET
    data_ultima_emissao_ocr: Union[Unset, datetime.date] = UNSET
    data_validade: Union[Unset, bool] = UNSET
    data_validade_ocr: Union[Unset, datetime.date] = UNSET
    retrato: Union[Unset, FaceResult] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        numero_registro = self.numero_registro
        numero_registro_ocr = self.numero_registro_ocr
        nome = self.nome
        nome_similaridade = self.nome_similaridade
        nome_ocr = self.nome_ocr
        identidade = self.identidade
        identidade_similaridade = self.identidade_similaridade
        identidade_ocr = self.identidade_ocr
        data_nascimento = self.data_nascimento
        data_nascimento_ocr: Union[Unset, str] = UNSET
        if not isinstance(self.data_nascimento_ocr, Unset):
            data_nascimento_ocr = self.data_nascimento_ocr.isoformat()

        data_primeira_habilitacao = self.data_primeira_habilitacao
        data_primeira_habilitacao_ocr: Union[Unset, str] = UNSET
        if not isinstance(self.data_primeira_habilitacao_ocr, Unset):
            data_primeira_habilitacao_ocr = self.data_primeira_habilitacao_ocr.isoformat()

        data_ultima_emissao = self.data_ultima_emissao
        data_ultima_emissao_ocr: Union[Unset, str] = UNSET
        if not isinstance(self.data_ultima_emissao_ocr, Unset):
            data_ultima_emissao_ocr = self.data_ultima_emissao_ocr.isoformat()

        data_validade = self.data_validade
        data_validade_ocr: Union[Unset, str] = UNSET
        if not isinstance(self.data_validade_ocr, Unset):
            data_validade_ocr = self.data_validade_ocr.isoformat()

        retrato: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.retrato, Unset):
            retrato = self.retrato.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if numero_registro is not UNSET:
            field_dict["numero_registro"] = numero_registro
        if numero_registro_ocr is not UNSET:
            field_dict["numero_registro_ocr"] = numero_registro_ocr
        if nome is not UNSET:
            field_dict["nome"] = nome
        if nome_similaridade is not UNSET:
            field_dict["nome_similaridade"] = nome_similaridade
        if nome_ocr is not UNSET:
            field_dict["nome_ocr"] = nome_ocr
        if identidade is not UNSET:
            field_dict["identidade"] = identidade
        if identidade_similaridade is not UNSET:
            field_dict["identidade_similaridade"] = identidade_similaridade
        if identidade_ocr is not UNSET:
            field_dict["identidade_ocr"] = identidade_ocr
        if data_nascimento is not UNSET:
            field_dict["data_nascimento"] = data_nascimento
        if data_nascimento_ocr is not UNSET:
            field_dict["data_nascimento_ocr"] = data_nascimento_ocr
        if data_primeira_habilitacao is not UNSET:
            field_dict["data_primeira_habilitacao"] = data_primeira_habilitacao
        if data_primeira_habilitacao_ocr is not UNSET:
            field_dict["data_primeira_habilitacao_ocr"] = data_primeira_habilitacao_ocr
        if data_ultima_emissao is not UNSET:
            field_dict["data_ultima_emissao"] = data_ultima_emissao
        if data_ultima_emissao_ocr is not UNSET:
            field_dict["data_ultima_emissao_ocr"] = data_ultima_emissao_ocr
        if data_validade is not UNSET:
            field_dict["data_validade"] = data_validade
        if data_validade_ocr is not UNSET:
            field_dict["data_validade_ocr"] = data_validade_ocr
        if retrato is not UNSET:
            field_dict["retrato"] = retrato

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        numero_registro = d.pop("numero_registro", UNSET)

        numero_registro_ocr = d.pop("numero_registro_ocr", UNSET)

        nome = d.pop("nome", UNSET)

        nome_similaridade = d.pop("nome_similaridade", UNSET)

        nome_ocr = d.pop("nome_ocr", UNSET)

        identidade = d.pop("identidade", UNSET)

        identidade_similaridade = d.pop("identidade_similaridade", UNSET)

        identidade_ocr = d.pop("identidade_ocr", UNSET)

        data_nascimento = d.pop("data_nascimento", UNSET)

        _data_nascimento_ocr = d.pop("data_nascimento_ocr", UNSET)
        data_nascimento_ocr: Union[Unset, datetime.date]
        if isinstance(_data_nascimento_ocr, Unset):
            data_nascimento_ocr = UNSET
        else:
            data_nascimento_ocr = isoparse(_data_nascimento_ocr).date()

        data_primeira_habilitacao = d.pop("data_primeira_habilitacao", UNSET)

        _data_primeira_habilitacao_ocr = d.pop("data_primeira_habilitacao_ocr", UNSET)
        data_primeira_habilitacao_ocr: Union[Unset, datetime.date]
        if isinstance(_data_primeira_habilitacao_ocr, Unset):
            data_primeira_habilitacao_ocr = UNSET
        else:
            data_primeira_habilitacao_ocr = isoparse(_data_primeira_habilitacao_ocr).date()

        data_ultima_emissao = d.pop("data_ultima_emissao", UNSET)

        _data_ultima_emissao_ocr = d.pop("data_ultima_emissao_ocr", UNSET)
        data_ultima_emissao_ocr: Union[Unset, datetime.date]
        if isinstance(_data_ultima_emissao_ocr, Unset):
            data_ultima_emissao_ocr = UNSET
        else:
            data_ultima_emissao_ocr = isoparse(_data_ultima_emissao_ocr).date()

        data_validade = d.pop("data_validade", UNSET)

        _data_validade_ocr = d.pop("data_validade_ocr", UNSET)
        data_validade_ocr: Union[Unset, datetime.date]
        if isinstance(_data_validade_ocr, Unset):
            data_validade_ocr = UNSET
        else:
            data_validade_ocr = isoparse(_data_validade_ocr).date()

        _retrato = d.pop("retrato", UNSET)
        retrato: Union[Unset, FaceResult]
        if isinstance(_retrato, Unset):
            retrato = UNSET
        else:
            retrato = FaceResult.from_dict(_retrato)

        cnh_cdv_result = cls(
            numero_registro=numero_registro,
            numero_registro_ocr=numero_registro_ocr,
            nome=nome,
            nome_similaridade=nome_similaridade,
            nome_ocr=nome_ocr,
            identidade=identidade,
            identidade_similaridade=identidade_similaridade,
            identidade_ocr=identidade_ocr,
            data_nascimento=data_nascimento,
            data_nascimento_ocr=data_nascimento_ocr,
            data_primeira_habilitacao=data_primeira_habilitacao,
            data_primeira_habilitacao_ocr=data_primeira_habilitacao_ocr,
            data_ultima_emissao=data_ultima_emissao,
            data_ultima_emissao_ocr=data_ultima_emissao_ocr,
            data_validade=data_validade,
            data_validade_ocr=data_validade_ocr,
            retrato=retrato,
        )

        cnh_cdv_result.additional_properties = d
        return cnh_cdv_result

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
