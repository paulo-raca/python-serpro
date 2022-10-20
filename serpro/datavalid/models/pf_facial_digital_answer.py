import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.cnh_answer import CNHAnswer
from ..models.digital_answer import DigitalAnswer
from ..models.documento_answer import DocumentoAnswer
from ..models.endereco_answer import EnderecoAnswer
from ..models.face_answer import FaceAnswer
from ..models.filiacao_answer import FiliacaoAnswer
from ..models.pf_facial_digital_answer_nacionalidade import PFFacialDigitalAnswerNacionalidade
from ..models.pf_facial_digital_answer_sexo import PFFacialDigitalAnswerSexo
from ..models.pf_facial_digital_answer_situacao_cpf import PFFacialDigitalAnswerSituacaoCpf
from ..types import UNSET, Unset

T = TypeVar("T", bound="PFFacialDigitalAnswer")


@attr.s(auto_attribs=True)
class PFFacialDigitalAnswer:
    """
    Attributes:
        nome (Union[Unset, str]):
        data_nascimento (Union[Unset, datetime.date]):
        situacao_cpf (Union[Unset, PFFacialDigitalAnswerSituacaoCpf]): regular, suspensa, titular falecido, pendente de
            regularização, cancelada por multiplicidade, nula, cancelada de oficio
        sexo (Union[Unset, PFFacialDigitalAnswerSexo]): F - female, M - male
        nacionalidade (Union[Unset, PFFacialDigitalAnswerNacionalidade]): 1 - brazilian, 2 - naturalized brazilian, 3 -
            foreigner, 4 - brazilian born abroad
        cnh (Union[Unset, CNHAnswer]):
        filiacao (Union[Unset, FiliacaoAnswer]):
        documento (Union[Unset, DocumentoAnswer]):
        endereco (Union[Unset, EnderecoAnswer]):
        biometria_face (Union[Unset, FaceAnswer]):
        digitais (Union[Unset, List[DigitalAnswer]]):
    """

    nome: Union[Unset, str] = UNSET
    data_nascimento: Union[Unset, datetime.date] = UNSET
    situacao_cpf: Union[Unset, PFFacialDigitalAnswerSituacaoCpf] = UNSET
    sexo: Union[Unset, PFFacialDigitalAnswerSexo] = UNSET
    nacionalidade: Union[Unset, PFFacialDigitalAnswerNacionalidade] = UNSET
    cnh: Union[Unset, CNHAnswer] = UNSET
    filiacao: Union[Unset, FiliacaoAnswer] = UNSET
    documento: Union[Unset, DocumentoAnswer] = UNSET
    endereco: Union[Unset, EnderecoAnswer] = UNSET
    biometria_face: Union[Unset, FaceAnswer] = UNSET
    digitais: Union[Unset, List[DigitalAnswer]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nome = self.nome
        data_nascimento: Union[Unset, str] = UNSET
        if not isinstance(self.data_nascimento, Unset):
            data_nascimento = self.data_nascimento.isoformat()

        situacao_cpf: Union[Unset, str] = UNSET
        if not isinstance(self.situacao_cpf, Unset):
            situacao_cpf = self.situacao_cpf.value

        sexo: Union[Unset, str] = UNSET
        if not isinstance(self.sexo, Unset):
            sexo = self.sexo.value

        nacionalidade: Union[Unset, int] = UNSET
        if not isinstance(self.nacionalidade, Unset):
            nacionalidade = self.nacionalidade.value

        cnh: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cnh, Unset):
            cnh = self.cnh.to_dict()

        filiacao: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filiacao, Unset):
            filiacao = self.filiacao.to_dict()

        documento: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.documento, Unset):
            documento = self.documento.to_dict()

        endereco: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.endereco, Unset):
            endereco = self.endereco.to_dict()

        biometria_face: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.biometria_face, Unset):
            biometria_face = self.biometria_face.to_dict()

        digitais: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.digitais, Unset):
            digitais = []
            for digitais_item_data in self.digitais:
                digitais_item = digitais_item_data.to_dict()

                digitais.append(digitais_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nome is not UNSET:
            field_dict["nome"] = nome
        if data_nascimento is not UNSET:
            field_dict["data_nascimento"] = data_nascimento
        if situacao_cpf is not UNSET:
            field_dict["situacao_cpf"] = situacao_cpf
        if sexo is not UNSET:
            field_dict["sexo"] = sexo
        if nacionalidade is not UNSET:
            field_dict["nacionalidade"] = nacionalidade
        if cnh is not UNSET:
            field_dict["cnh"] = cnh
        if filiacao is not UNSET:
            field_dict["filiacao"] = filiacao
        if documento is not UNSET:
            field_dict["documento"] = documento
        if endereco is not UNSET:
            field_dict["endereco"] = endereco
        if biometria_face is not UNSET:
            field_dict["biometria_face"] = biometria_face
        if digitais is not UNSET:
            field_dict["digitais"] = digitais

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        nome = d.pop("nome", UNSET)

        _data_nascimento = d.pop("data_nascimento", UNSET)
        data_nascimento: Union[Unset, datetime.date]
        if isinstance(_data_nascimento, Unset):
            data_nascimento = UNSET
        else:
            data_nascimento = isoparse(_data_nascimento).date()

        _situacao_cpf = d.pop("situacao_cpf", UNSET)
        situacao_cpf: Union[Unset, PFFacialDigitalAnswerSituacaoCpf]
        if isinstance(_situacao_cpf, Unset):
            situacao_cpf = UNSET
        else:
            situacao_cpf = PFFacialDigitalAnswerSituacaoCpf(_situacao_cpf)

        _sexo = d.pop("sexo", UNSET)
        sexo: Union[Unset, PFFacialDigitalAnswerSexo]
        if isinstance(_sexo, Unset):
            sexo = UNSET
        else:
            sexo = PFFacialDigitalAnswerSexo(_sexo)

        _nacionalidade = d.pop("nacionalidade", UNSET)
        nacionalidade: Union[Unset, PFFacialDigitalAnswerNacionalidade]
        if isinstance(_nacionalidade, Unset):
            nacionalidade = UNSET
        else:
            nacionalidade = PFFacialDigitalAnswerNacionalidade(_nacionalidade)

        _cnh = d.pop("cnh", UNSET)
        cnh: Union[Unset, CNHAnswer]
        if isinstance(_cnh, Unset):
            cnh = UNSET
        else:
            cnh = CNHAnswer.from_dict(_cnh)

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

        _biometria_face = d.pop("biometria_face", UNSET)
        biometria_face: Union[Unset, FaceAnswer]
        if isinstance(_biometria_face, Unset):
            biometria_face = UNSET
        else:
            biometria_face = FaceAnswer.from_dict(_biometria_face)

        digitais = []
        _digitais = d.pop("digitais", UNSET)
        for digitais_item_data in _digitais or []:
            digitais_item = DigitalAnswer.from_dict(digitais_item_data)

            digitais.append(digitais_item)

        pf_facial_digital_answer = cls(
            nome=nome,
            data_nascimento=data_nascimento,
            situacao_cpf=situacao_cpf,
            sexo=sexo,
            nacionalidade=nacionalidade,
            cnh=cnh,
            filiacao=filiacao,
            documento=documento,
            endereco=endereco,
            biometria_face=biometria_face,
            digitais=digitais,
        )

        pf_facial_digital_answer.additional_properties = d
        return pf_facial_digital_answer

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
