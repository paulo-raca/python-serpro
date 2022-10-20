import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.cnhv1_answer_codigo_situacao import CNHV1AnswerCodigoSituacao
from ..types import UNSET, Unset

T = TypeVar("T", bound="CNHV1Answer")


@attr.s(auto_attribs=True)
class CNHV1Answer:
    """
    Attributes:
        categoria (Union[Unset, str]):
        numero_registro (Union[Unset, str]):
        data_primeira_habilitacao (Union[Unset, datetime.date]):
        data_validade (Union[Unset, datetime.date]):
        registro_nacional_estrangeiro (Union[Unset, str]):
        data_ultima_emissao (Union[Unset, datetime.date]):
        codigo_situacao (Union[Unset, CNHV1AnswerCodigoSituacao]): 2 - in issue, 3 - issued, A - canceled
    """

    categoria: Union[Unset, str] = UNSET
    numero_registro: Union[Unset, str] = UNSET
    data_primeira_habilitacao: Union[Unset, datetime.date] = UNSET
    data_validade: Union[Unset, datetime.date] = UNSET
    registro_nacional_estrangeiro: Union[Unset, str] = UNSET
    data_ultima_emissao: Union[Unset, datetime.date] = UNSET
    codigo_situacao: Union[Unset, CNHV1AnswerCodigoSituacao] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        categoria = self.categoria
        numero_registro = self.numero_registro
        data_primeira_habilitacao: Union[Unset, str] = UNSET
        if not isinstance(self.data_primeira_habilitacao, Unset):
            data_primeira_habilitacao = self.data_primeira_habilitacao.isoformat()

        data_validade: Union[Unset, str] = UNSET
        if not isinstance(self.data_validade, Unset):
            data_validade = self.data_validade.isoformat()

        registro_nacional_estrangeiro = self.registro_nacional_estrangeiro
        data_ultima_emissao: Union[Unset, str] = UNSET
        if not isinstance(self.data_ultima_emissao, Unset):
            data_ultima_emissao = self.data_ultima_emissao.isoformat()

        codigo_situacao: Union[Unset, str] = UNSET
        if not isinstance(self.codigo_situacao, Unset):
            codigo_situacao = self.codigo_situacao.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if categoria is not UNSET:
            field_dict["categoria"] = categoria
        if numero_registro is not UNSET:
            field_dict["numero_registro"] = numero_registro
        if data_primeira_habilitacao is not UNSET:
            field_dict["data_primeira_habilitacao"] = data_primeira_habilitacao
        if data_validade is not UNSET:
            field_dict["data_validade"] = data_validade
        if registro_nacional_estrangeiro is not UNSET:
            field_dict["registro_nacional_estrangeiro"] = registro_nacional_estrangeiro
        if data_ultima_emissao is not UNSET:
            field_dict["data_ultima_emissao"] = data_ultima_emissao
        if codigo_situacao is not UNSET:
            field_dict["codigo_situacao"] = codigo_situacao

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        categoria = d.pop("categoria", UNSET)

        numero_registro = d.pop("numero_registro", UNSET)

        _data_primeira_habilitacao = d.pop("data_primeira_habilitacao", UNSET)
        data_primeira_habilitacao: Union[Unset, datetime.date]
        if isinstance(_data_primeira_habilitacao, Unset):
            data_primeira_habilitacao = UNSET
        else:
            data_primeira_habilitacao = isoparse(_data_primeira_habilitacao).date()

        _data_validade = d.pop("data_validade", UNSET)
        data_validade: Union[Unset, datetime.date]
        if isinstance(_data_validade, Unset):
            data_validade = UNSET
        else:
            data_validade = isoparse(_data_validade).date()

        registro_nacional_estrangeiro = d.pop("registro_nacional_estrangeiro", UNSET)

        _data_ultima_emissao = d.pop("data_ultima_emissao", UNSET)
        data_ultima_emissao: Union[Unset, datetime.date]
        if isinstance(_data_ultima_emissao, Unset):
            data_ultima_emissao = UNSET
        else:
            data_ultima_emissao = isoparse(_data_ultima_emissao).date()

        _codigo_situacao = d.pop("codigo_situacao", UNSET)
        codigo_situacao: Union[Unset, CNHV1AnswerCodigoSituacao]
        if isinstance(_codigo_situacao, Unset):
            codigo_situacao = UNSET
        else:
            codigo_situacao = CNHV1AnswerCodigoSituacao(_codigo_situacao)

        cnhv1_answer = cls(
            categoria=categoria,
            numero_registro=numero_registro,
            data_primeira_habilitacao=data_primeira_habilitacao,
            data_validade=data_validade,
            registro_nacional_estrangeiro=registro_nacional_estrangeiro,
            data_ultima_emissao=data_ultima_emissao,
            codigo_situacao=codigo_situacao,
        )

        cnhv1_answer.additional_properties = d
        return cnhv1_answer

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
