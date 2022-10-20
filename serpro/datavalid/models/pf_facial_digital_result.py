from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.cnh_result import CNHResult
from ..models.digitais_result import DigitaisResult
from ..models.documento_result import DocumentoResult
from ..models.endereco_result import EnderecoResult
from ..models.face_result import FaceResult
from ..models.filiacao_result import FiliacaoResult
from ..types import UNSET, Unset

T = TypeVar("T", bound="PFFacialDigitalResult")


@attr.s(auto_attribs=True)
class PFFacialDigitalResult:
    """
    Attributes:
        cpf_disponivel (Union[Unset, bool]): Indicates whether the CPF exists on the official government basis
        nome (Union[Unset, bool]):
        nome_similaridade (Union[Unset, float]):
        data_nascimento (Union[Unset, bool]):
        situacao_cpf (Union[Unset, bool]):
        sexo (Union[Unset, bool]):
        nacionalidade (Union[Unset, bool]):
        cnh_disponivel (Union[Unset, bool]):
        cnh (Union[Unset, CNHResult]):
        filiacao (Union[Unset, FiliacaoResult]):
        documento (Union[Unset, DocumentoResult]):
        endereco (Union[Unset, EnderecoResult]):
        biometria_face (Union[Unset, FaceResult]):
        biometria_digital (Union[Unset, DigitaisResult]):
    """

    cpf_disponivel: Union[Unset, bool] = UNSET
    nome: Union[Unset, bool] = UNSET
    nome_similaridade: Union[Unset, float] = UNSET
    data_nascimento: Union[Unset, bool] = UNSET
    situacao_cpf: Union[Unset, bool] = UNSET
    sexo: Union[Unset, bool] = UNSET
    nacionalidade: Union[Unset, bool] = UNSET
    cnh_disponivel: Union[Unset, bool] = UNSET
    cnh: Union[Unset, CNHResult] = UNSET
    filiacao: Union[Unset, FiliacaoResult] = UNSET
    documento: Union[Unset, DocumentoResult] = UNSET
    endereco: Union[Unset, EnderecoResult] = UNSET
    biometria_face: Union[Unset, FaceResult] = UNSET
    biometria_digital: Union[Unset, DigitaisResult] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cpf_disponivel = self.cpf_disponivel
        nome = self.nome
        nome_similaridade = self.nome_similaridade
        data_nascimento = self.data_nascimento
        situacao_cpf = self.situacao_cpf
        sexo = self.sexo
        nacionalidade = self.nacionalidade
        cnh_disponivel = self.cnh_disponivel
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

        biometria_digital: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.biometria_digital, Unset):
            biometria_digital = self.biometria_digital.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cpf_disponivel is not UNSET:
            field_dict["cpf_disponivel"] = cpf_disponivel
        if nome is not UNSET:
            field_dict["nome"] = nome
        if nome_similaridade is not UNSET:
            field_dict["nome_similaridade"] = nome_similaridade
        if data_nascimento is not UNSET:
            field_dict["data_nascimento"] = data_nascimento
        if situacao_cpf is not UNSET:
            field_dict["situacao_cpf"] = situacao_cpf
        if sexo is not UNSET:
            field_dict["sexo"] = sexo
        if nacionalidade is not UNSET:
            field_dict["nacionalidade"] = nacionalidade
        if cnh_disponivel is not UNSET:
            field_dict["cnh_disponivel"] = cnh_disponivel
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
        if biometria_digital is not UNSET:
            field_dict["biometria_digital"] = biometria_digital

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cpf_disponivel = d.pop("cpf_disponivel", UNSET)

        nome = d.pop("nome", UNSET)

        nome_similaridade = d.pop("nome_similaridade", UNSET)

        data_nascimento = d.pop("data_nascimento", UNSET)

        situacao_cpf = d.pop("situacao_cpf", UNSET)

        sexo = d.pop("sexo", UNSET)

        nacionalidade = d.pop("nacionalidade", UNSET)

        cnh_disponivel = d.pop("cnh_disponivel", UNSET)

        _cnh = d.pop("cnh", UNSET)
        cnh: Union[Unset, CNHResult]
        if isinstance(_cnh, Unset):
            cnh = UNSET
        else:
            cnh = CNHResult.from_dict(_cnh)

        _filiacao = d.pop("filiacao", UNSET)
        filiacao: Union[Unset, FiliacaoResult]
        if isinstance(_filiacao, Unset):
            filiacao = UNSET
        else:
            filiacao = FiliacaoResult.from_dict(_filiacao)

        _documento = d.pop("documento", UNSET)
        documento: Union[Unset, DocumentoResult]
        if isinstance(_documento, Unset):
            documento = UNSET
        else:
            documento = DocumentoResult.from_dict(_documento)

        _endereco = d.pop("endereco", UNSET)
        endereco: Union[Unset, EnderecoResult]
        if isinstance(_endereco, Unset):
            endereco = UNSET
        else:
            endereco = EnderecoResult.from_dict(_endereco)

        _biometria_face = d.pop("biometria_face", UNSET)
        biometria_face: Union[Unset, FaceResult]
        if isinstance(_biometria_face, Unset):
            biometria_face = UNSET
        else:
            biometria_face = FaceResult.from_dict(_biometria_face)

        _biometria_digital = d.pop("biometria_digital", UNSET)
        biometria_digital: Union[Unset, DigitaisResult]
        if isinstance(_biometria_digital, Unset):
            biometria_digital = UNSET
        else:
            biometria_digital = DigitaisResult.from_dict(_biometria_digital)

        pf_facial_digital_result = cls(
            cpf_disponivel=cpf_disponivel,
            nome=nome,
            nome_similaridade=nome_similaridade,
            data_nascimento=data_nascimento,
            situacao_cpf=situacao_cpf,
            sexo=sexo,
            nacionalidade=nacionalidade,
            cnh_disponivel=cnh_disponivel,
            cnh=cnh,
            filiacao=filiacao,
            documento=documento,
            endereco=endereco,
            biometria_face=biometria_face,
            biometria_digital=biometria_digital,
        )

        pf_facial_digital_result.additional_properties = d
        return pf_facial_digital_result

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
