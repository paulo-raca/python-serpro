import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.cnh_biometry_vbeta_1_answer import CNHBiometryVbeta1Answer
from ..models.documento_answer import DocumentoAnswer
from ..models.endereco_answer import EnderecoAnswer
from ..models.filiacao_answer import FiliacaoAnswer
from ..models.pf_face_vbeta_1_answer_nacionalidade import PFFaceVbeta1AnswerNacionalidade
from ..models.pf_face_vbeta_1_answer_sexo import PFFaceVbeta1AnswerSexo
from ..models.pf_face_vbeta_1_answer_situacao_cpf import PFFaceVbeta1AnswerSituacaoCpf
from ..types import UNSET, Unset

T = TypeVar("T", bound="PFFaceVbeta1Answer")


@attr.s(auto_attribs=True)
class PFFaceVbeta1Answer:
    """
    Attributes:
        nome (Union[Unset, str]):
        sexo (Union[Unset, PFFaceVbeta1AnswerSexo]): F - female, M - male
        nacionalidade (Union[Unset, PFFaceVbeta1AnswerNacionalidade]): 1 - brazilian, 2 - naturalized brazilian, 3 -
            foreigner, 4 - brazilian born abroad
        filiacao (Union[Unset, FiliacaoAnswer]):
        documento (Union[Unset, DocumentoAnswer]):
        endereco (Union[Unset, EnderecoAnswer]):
        cnh (Union[Unset, CNHBiometryVbeta1Answer]):
        data_nascimento (Union[Unset, datetime.date]):
        situacao_cpf (Union[Unset, PFFaceVbeta1AnswerSituacaoCpf]): regular, suspensa, titular falecido, pendente de
            regularização, cancelada por multiplicidade, nula, cancelada de oficio
        biometria_face (Union[Unset, str]): Base64 encoded PDF or PNG formats only without line breaks
    """

    nome: Union[Unset, str] = UNSET
    sexo: Union[Unset, PFFaceVbeta1AnswerSexo] = UNSET
    nacionalidade: Union[Unset, PFFaceVbeta1AnswerNacionalidade] = UNSET
    filiacao: Union[Unset, FiliacaoAnswer] = UNSET
    documento: Union[Unset, DocumentoAnswer] = UNSET
    endereco: Union[Unset, EnderecoAnswer] = UNSET
    cnh: Union[Unset, CNHBiometryVbeta1Answer] = UNSET
    data_nascimento: Union[Unset, datetime.date] = UNSET
    situacao_cpf: Union[Unset, PFFaceVbeta1AnswerSituacaoCpf] = UNSET
    biometria_face: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nome = self.nome
        sexo: Union[Unset, str] = UNSET
        if not isinstance(self.sexo, Unset):
            sexo = self.sexo.value

        nacionalidade: Union[Unset, int] = UNSET
        if not isinstance(self.nacionalidade, Unset):
            nacionalidade = self.nacionalidade.value

        filiacao: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filiacao, Unset):
            filiacao = self.filiacao.to_dict()

        documento: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.documento, Unset):
            documento = self.documento.to_dict()

        endereco: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.endereco, Unset):
            endereco = self.endereco.to_dict()

        cnh: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cnh, Unset):
            cnh = self.cnh.to_dict()

        data_nascimento: Union[Unset, str] = UNSET
        if not isinstance(self.data_nascimento, Unset):
            data_nascimento = self.data_nascimento.isoformat()

        situacao_cpf: Union[Unset, str] = UNSET
        if not isinstance(self.situacao_cpf, Unset):
            situacao_cpf = self.situacao_cpf.value

        biometria_face = self.biometria_face

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nome is not UNSET:
            field_dict["nome"] = nome
        if sexo is not UNSET:
            field_dict["sexo"] = sexo
        if nacionalidade is not UNSET:
            field_dict["nacionalidade"] = nacionalidade
        if filiacao is not UNSET:
            field_dict["filiacao"] = filiacao
        if documento is not UNSET:
            field_dict["documento"] = documento
        if endereco is not UNSET:
            field_dict["endereco"] = endereco
        if cnh is not UNSET:
            field_dict["cnh"] = cnh
        if data_nascimento is not UNSET:
            field_dict["data_nascimento"] = data_nascimento
        if situacao_cpf is not UNSET:
            field_dict["situacao_cpf"] = situacao_cpf
        if biometria_face is not UNSET:
            field_dict["biometria_face"] = biometria_face

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        nome = d.pop("nome", UNSET)

        _sexo = d.pop("sexo", UNSET)
        sexo: Union[Unset, PFFaceVbeta1AnswerSexo]
        if isinstance(_sexo, Unset):
            sexo = UNSET
        else:
            sexo = PFFaceVbeta1AnswerSexo(_sexo)

        _nacionalidade = d.pop("nacionalidade", UNSET)
        nacionalidade: Union[Unset, PFFaceVbeta1AnswerNacionalidade]
        if isinstance(_nacionalidade, Unset):
            nacionalidade = UNSET
        else:
            nacionalidade = PFFaceVbeta1AnswerNacionalidade(_nacionalidade)

        _filiacao = d.pop("filiacao", UNSET)
        filiacao: Union[Unset, FiliacaoAnswer]
        if isinstance(_filiacao, Unset):
            filiacao = UNSET
        else:
            filiacao = FiliacaoAnswer.from_dict(_filiacao)

        _documento = d.pop("documento", UNSET)
        documento: Union[Unset, DocumentoAnswer]
        if isinstance(_documento, Unset):
            documento = UNSET
        else:
            documento = DocumentoAnswer.from_dict(_documento)

        _endereco = d.pop("endereco", UNSET)
        endereco: Union[Unset, EnderecoAnswer]
        if isinstance(_endereco, Unset):
            endereco = UNSET
        else:
            endereco = EnderecoAnswer.from_dict(_endereco)

        _cnh = d.pop("cnh", UNSET)
        cnh: Union[Unset, CNHBiometryVbeta1Answer]
        if isinstance(_cnh, Unset):
            cnh = UNSET
        else:
            cnh = CNHBiometryVbeta1Answer.from_dict(_cnh)

        _data_nascimento = d.pop("data_nascimento", UNSET)
        data_nascimento: Union[Unset, datetime.date]
        if isinstance(_data_nascimento, Unset):
            data_nascimento = UNSET
        else:
            data_nascimento = isoparse(_data_nascimento).date()

        _situacao_cpf = d.pop("situacao_cpf", UNSET)
        situacao_cpf: Union[Unset, PFFaceVbeta1AnswerSituacaoCpf]
        if isinstance(_situacao_cpf, Unset):
            situacao_cpf = UNSET
        else:
            situacao_cpf = PFFaceVbeta1AnswerSituacaoCpf(_situacao_cpf)

        biometria_face = d.pop("biometria_face", UNSET)

        pf_face_vbeta_1_answer = cls(
            nome=nome,
            sexo=sexo,
            nacionalidade=nacionalidade,
            filiacao=filiacao,
            documento=documento,
            endereco=endereco,
            cnh=cnh,
            data_nascimento=data_nascimento,
            situacao_cpf=situacao_cpf,
            biometria_face=biometria_face,
        )

        pf_face_vbeta_1_answer.additional_properties = d
        return pf_face_vbeta_1_answer

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
