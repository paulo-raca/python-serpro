from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.cnhv1_result import CNHV1Result
from ..models.documento_result import DocumentoResult
from ..models.endereco_result import EnderecoResult
from ..models.face_result import FaceResult
from ..models.filiacao_result import FiliacaoResult
from ..types import UNSET, Unset

T = TypeVar("T", bound="PFFaceV1Result")


@attr.s(auto_attribs=True)
class PFFaceV1Result:
    """
    Attributes:
        nome (Union[Unset, bool]):
        sexo (Union[Unset, bool]):
        nacionalidade (Union[Unset, bool]):
        filiacao (Union[Unset, FiliacaoResult]):
        endereco (Union[Unset, EnderecoResult]):
        cnh (Union[Unset, CNHV1Result]):
        documento (Union[Unset, DocumentoResult]):
        cpf_disponivel (Union[Unset, bool]): Indicates whether the CPF exists on the official government basis
        nome_similaridade (Union[Unset, float]):
        data_nascimento (Union[Unset, bool]):
        situacao_cpf (Union[Unset, bool]):
        biometria_face (Union[Unset, FaceResult]):
    """

    nome: Union[Unset, bool] = UNSET
    sexo: Union[Unset, bool] = UNSET
    nacionalidade: Union[Unset, bool] = UNSET
    filiacao: Union[Unset, FiliacaoResult] = UNSET
    endereco: Union[Unset, EnderecoResult] = UNSET
    cnh: Union[Unset, CNHV1Result] = UNSET
    documento: Union[Unset, DocumentoResult] = UNSET
    cpf_disponivel: Union[Unset, bool] = UNSET
    nome_similaridade: Union[Unset, float] = UNSET
    data_nascimento: Union[Unset, bool] = UNSET
    situacao_cpf: Union[Unset, bool] = UNSET
    biometria_face: Union[Unset, FaceResult] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nome = self.nome
        sexo = self.sexo
        nacionalidade = self.nacionalidade
        filiacao: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filiacao, Unset):
            filiacao = self.filiacao.to_dict()

        endereco: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.endereco, Unset):
            endereco = self.endereco.to_dict()

        cnh: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cnh, Unset):
            cnh = self.cnh.to_dict()

        documento: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.documento, Unset):
            documento = self.documento.to_dict()

        cpf_disponivel = self.cpf_disponivel
        nome_similaridade = self.nome_similaridade
        data_nascimento = self.data_nascimento
        situacao_cpf = self.situacao_cpf
        biometria_face: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.biometria_face, Unset):
            biometria_face = self.biometria_face.to_dict()

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
        if endereco is not UNSET:
            field_dict["endereco"] = endereco
        if cnh is not UNSET:
            field_dict["cnh"] = cnh
        if documento is not UNSET:
            field_dict["documento"] = documento
        if cpf_disponivel is not UNSET:
            field_dict["cpf_disponivel"] = cpf_disponivel
        if nome_similaridade is not UNSET:
            field_dict["nome_similaridade"] = nome_similaridade
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

        sexo = d.pop("sexo", UNSET)

        nacionalidade = d.pop("nacionalidade", UNSET)

        _filiacao = d.pop("filiacao", UNSET)
        filiacao: Union[Unset, FiliacaoResult]
        if isinstance(_filiacao, Unset):
            filiacao = UNSET
        else:
            filiacao = FiliacaoResult.from_dict(_filiacao)

        _endereco = d.pop("endereco", UNSET)
        endereco: Union[Unset, EnderecoResult]
        if isinstance(_endereco, Unset):
            endereco = UNSET
        else:
            endereco = EnderecoResult.from_dict(_endereco)

        _cnh = d.pop("cnh", UNSET)
        cnh: Union[Unset, CNHV1Result]
        if isinstance(_cnh, Unset):
            cnh = UNSET
        else:
            cnh = CNHV1Result.from_dict(_cnh)

        _documento = d.pop("documento", UNSET)
        documento: Union[Unset, DocumentoResult]
        if isinstance(_documento, Unset):
            documento = UNSET
        else:
            documento = DocumentoResult.from_dict(_documento)

        cpf_disponivel = d.pop("cpf_disponivel", UNSET)

        nome_similaridade = d.pop("nome_similaridade", UNSET)

        data_nascimento = d.pop("data_nascimento", UNSET)

        situacao_cpf = d.pop("situacao_cpf", UNSET)

        _biometria_face = d.pop("biometria_face", UNSET)
        biometria_face: Union[Unset, FaceResult]
        if isinstance(_biometria_face, Unset):
            biometria_face = UNSET
        else:
            biometria_face = FaceResult.from_dict(_biometria_face)

        pf_face_v1_result = cls(
            nome=nome,
            sexo=sexo,
            nacionalidade=nacionalidade,
            filiacao=filiacao,
            endereco=endereco,
            cnh=cnh,
            documento=documento,
            cpf_disponivel=cpf_disponivel,
            nome_similaridade=nome_similaridade,
            data_nascimento=data_nascimento,
            situacao_cpf=situacao_cpf,
            biometria_face=biometria_face,
        )

        pf_face_v1_result.additional_properties = d
        return pf_face_v1_result

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
