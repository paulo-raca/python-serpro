import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.cnh_answer_codigo_situacao import CNHAnswerCodigoSituacao
from ..types import UNSET, Unset

T = TypeVar("T", bound="CNHAnswer")


@attr.s(auto_attribs=True)
class CNHAnswer:
    """
    Attributes:
        numero_registro (Union[Unset, str]):
        categoria (Union[Unset, str]):
        codigo_situacao (Union[Unset, CNHAnswerCodigoSituacao]): 2 - in issue, 3 - issued, A - canceled
        data_ultima_emissao (Union[Unset, datetime.date]):
        data_validade (Union[Unset, datetime.date]):
        data_primeira_habilitacao (Union[Unset, datetime.date]):
        registro_nacional_estrangeiro (Union[Unset, str]):
        possui_impedimento (Union[Unset, bool]): When this field is sent to the service with the input parameter “true”
            it will return an information of “true” (if there is an impediment) or “false” (if there is no impediment) if
            the CNH of the CPF consulted has an impediment for registered driving in the Senatran database. If the input
            parameter is “false”, the value returned by the service will be “true” (if there is no impediment) or “false”
            (if there is an impediment). Note that depending on the input parameter sent to this field, the meaning of the
            return will be different as explained
        observacoes (Union[Unset, str]): To submit the validation of this field, the observation(s) must be informed
            separated by a semicolon (;), and when it is for a driver's license that does not have any observation the blank
            value must be entered (“”). Note that <em>null</em> is different from blank, and Datavalid treats them as
            distinct values. Examples: <code>“EAR;A”</code>, <code>“CETPP”</code>, <code>“”</code>.
    """

    numero_registro: Union[Unset, str] = UNSET
    categoria: Union[Unset, str] = UNSET
    codigo_situacao: Union[Unset, CNHAnswerCodigoSituacao] = UNSET
    data_ultima_emissao: Union[Unset, datetime.date] = UNSET
    data_validade: Union[Unset, datetime.date] = UNSET
    data_primeira_habilitacao: Union[Unset, datetime.date] = UNSET
    registro_nacional_estrangeiro: Union[Unset, str] = UNSET
    possui_impedimento: Union[Unset, bool] = UNSET
    observacoes: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        numero_registro = self.numero_registro
        categoria = self.categoria
        codigo_situacao: Union[Unset, str] = UNSET
        if not isinstance(self.codigo_situacao, Unset):
            codigo_situacao = self.codigo_situacao.value

        data_ultima_emissao: Union[Unset, str] = UNSET
        if not isinstance(self.data_ultima_emissao, Unset):
            data_ultima_emissao = self.data_ultima_emissao.isoformat()

        data_validade: Union[Unset, str] = UNSET
        if not isinstance(self.data_validade, Unset):
            data_validade = self.data_validade.isoformat()

        data_primeira_habilitacao: Union[Unset, str] = UNSET
        if not isinstance(self.data_primeira_habilitacao, Unset):
            data_primeira_habilitacao = self.data_primeira_habilitacao.isoformat()

        registro_nacional_estrangeiro = self.registro_nacional_estrangeiro
        possui_impedimento = self.possui_impedimento
        observacoes = self.observacoes

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if numero_registro is not UNSET:
            field_dict["numero_registro"] = numero_registro
        if categoria is not UNSET:
            field_dict["categoria"] = categoria
        if codigo_situacao is not UNSET:
            field_dict["codigo_situacao"] = codigo_situacao
        if data_ultima_emissao is not UNSET:
            field_dict["data_ultima_emissao"] = data_ultima_emissao
        if data_validade is not UNSET:
            field_dict["data_validade"] = data_validade
        if data_primeira_habilitacao is not UNSET:
            field_dict["data_primeira_habilitacao"] = data_primeira_habilitacao
        if registro_nacional_estrangeiro is not UNSET:
            field_dict["registro_nacional_estrangeiro"] = registro_nacional_estrangeiro
        if possui_impedimento is not UNSET:
            field_dict["possui_impedimento"] = possui_impedimento
        if observacoes is not UNSET:
            field_dict["observacoes"] = observacoes

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        numero_registro = d.pop("numero_registro", UNSET)

        categoria = d.pop("categoria", UNSET)

        _codigo_situacao = d.pop("codigo_situacao", UNSET)
        codigo_situacao: Union[Unset, CNHAnswerCodigoSituacao]
        if isinstance(_codigo_situacao, Unset):
            codigo_situacao = UNSET
        else:
            codigo_situacao = CNHAnswerCodigoSituacao(_codigo_situacao)

        _data_ultima_emissao = d.pop("data_ultima_emissao", UNSET)
        data_ultima_emissao: Union[Unset, datetime.date]
        if isinstance(_data_ultima_emissao, Unset):
            data_ultima_emissao = UNSET
        else:
            data_ultima_emissao = isoparse(_data_ultima_emissao).date()

        _data_validade = d.pop("data_validade", UNSET)
        data_validade: Union[Unset, datetime.date]
        if isinstance(_data_validade, Unset):
            data_validade = UNSET
        else:
            data_validade = isoparse(_data_validade).date()

        _data_primeira_habilitacao = d.pop("data_primeira_habilitacao", UNSET)
        data_primeira_habilitacao: Union[Unset, datetime.date]
        if isinstance(_data_primeira_habilitacao, Unset):
            data_primeira_habilitacao = UNSET
        else:
            data_primeira_habilitacao = isoparse(_data_primeira_habilitacao).date()

        registro_nacional_estrangeiro = d.pop("registro_nacional_estrangeiro", UNSET)

        possui_impedimento = d.pop("possui_impedimento", UNSET)

        observacoes = d.pop("observacoes", UNSET)

        cnh_answer = cls(
            numero_registro=numero_registro,
            categoria=categoria,
            codigo_situacao=codigo_situacao,
            data_ultima_emissao=data_ultima_emissao,
            data_validade=data_validade,
            data_primeira_habilitacao=data_primeira_habilitacao,
            registro_nacional_estrangeiro=registro_nacional_estrangeiro,
            possui_impedimento=possui_impedimento,
            observacoes=observacoes,
        )

        cnh_answer.additional_properties = d
        return cnh_answer

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
