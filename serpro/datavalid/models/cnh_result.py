from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CNHResult")


@attr.s(auto_attribs=True)
class CNHResult:
    """
    Attributes:
        nome (Union[Unset, bool]):
        nome_similaridade (Union[Unset, float]):
        numero_registro (Union[Unset, bool]):
        categoria (Union[Unset, bool]):
        codigo_situacao (Union[Unset, bool]):
        registro_nacional_estrangeiro (Union[Unset, bool]):
        data_ultima_emissao (Union[Unset, bool]):
        data_primeira_habilitacao (Union[Unset, bool]):
        data_validade (Union[Unset, bool]):
        possui_impedimento (Union[Unset, bool]):
        observacoes (Union[Unset, bool]):
        observacoes_similaridade (Union[Unset, float]):
    """

    nome: Union[Unset, bool] = UNSET
    nome_similaridade: Union[Unset, float] = UNSET
    numero_registro: Union[Unset, bool] = UNSET
    categoria: Union[Unset, bool] = UNSET
    codigo_situacao: Union[Unset, bool] = UNSET
    registro_nacional_estrangeiro: Union[Unset, bool] = UNSET
    data_ultima_emissao: Union[Unset, bool] = UNSET
    data_primeira_habilitacao: Union[Unset, bool] = UNSET
    data_validade: Union[Unset, bool] = UNSET
    possui_impedimento: Union[Unset, bool] = UNSET
    observacoes: Union[Unset, bool] = UNSET
    observacoes_similaridade: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nome = self.nome
        nome_similaridade = self.nome_similaridade
        numero_registro = self.numero_registro
        categoria = self.categoria
        codigo_situacao = self.codigo_situacao
        registro_nacional_estrangeiro = self.registro_nacional_estrangeiro
        data_ultima_emissao = self.data_ultima_emissao
        data_primeira_habilitacao = self.data_primeira_habilitacao
        data_validade = self.data_validade
        possui_impedimento = self.possui_impedimento
        observacoes = self.observacoes
        observacoes_similaridade = self.observacoes_similaridade

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nome is not UNSET:
            field_dict["nome"] = nome
        if nome_similaridade is not UNSET:
            field_dict["nome_similaridade"] = nome_similaridade
        if numero_registro is not UNSET:
            field_dict["numero_registro"] = numero_registro
        if categoria is not UNSET:
            field_dict["categoria"] = categoria
        if codigo_situacao is not UNSET:
            field_dict["codigo_situacao"] = codigo_situacao
        if registro_nacional_estrangeiro is not UNSET:
            field_dict["registro_nacional_estrangeiro"] = registro_nacional_estrangeiro
        if data_ultima_emissao is not UNSET:
            field_dict["data_ultima_emissao"] = data_ultima_emissao
        if data_primeira_habilitacao is not UNSET:
            field_dict["data_primeira_habilitacao"] = data_primeira_habilitacao
        if data_validade is not UNSET:
            field_dict["data_validade"] = data_validade
        if possui_impedimento is not UNSET:
            field_dict["possui_impedimento"] = possui_impedimento
        if observacoes is not UNSET:
            field_dict["observacoes"] = observacoes
        if observacoes_similaridade is not UNSET:
            field_dict["observacoes_similaridade"] = observacoes_similaridade

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        nome = d.pop("nome", UNSET)

        nome_similaridade = d.pop("nome_similaridade", UNSET)

        numero_registro = d.pop("numero_registro", UNSET)

        categoria = d.pop("categoria", UNSET)

        codigo_situacao = d.pop("codigo_situacao", UNSET)

        registro_nacional_estrangeiro = d.pop("registro_nacional_estrangeiro", UNSET)

        data_ultima_emissao = d.pop("data_ultima_emissao", UNSET)

        data_primeira_habilitacao = d.pop("data_primeira_habilitacao", UNSET)

        data_validade = d.pop("data_validade", UNSET)

        possui_impedimento = d.pop("possui_impedimento", UNSET)

        observacoes = d.pop("observacoes", UNSET)

        observacoes_similaridade = d.pop("observacoes_similaridade", UNSET)

        cnh_result = cls(
            nome=nome,
            nome_similaridade=nome_similaridade,
            numero_registro=numero_registro,
            categoria=categoria,
            codigo_situacao=codigo_situacao,
            registro_nacional_estrangeiro=registro_nacional_estrangeiro,
            data_ultima_emissao=data_ultima_emissao,
            data_primeira_habilitacao=data_primeira_habilitacao,
            data_validade=data_validade,
            possui_impedimento=possui_impedimento,
            observacoes=observacoes,
            observacoes_similaridade=observacoes_similaridade,
        )

        cnh_result.additional_properties = d
        return cnh_result

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
