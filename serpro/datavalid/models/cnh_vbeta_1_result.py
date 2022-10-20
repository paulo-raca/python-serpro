from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CNHVbeta1Result")


@attr.s(auto_attribs=True)
class CNHVbeta1Result:
    """
    Attributes:
        nome (Union[Unset, bool]):
        categoria (Union[Unset, bool]):
        nome_similaridade (Union[Unset, float]):
        numero_registro (Union[Unset, bool]):
        data_primeira_habilitacao (Union[Unset, bool]):
        data_validade (Union[Unset, bool]):
        registro_nacional_estrangeiro (Union[Unset, bool]):
        data_ultima_emissao (Union[Unset, bool]):
        codigo_situacao (Union[Unset, bool]):
        descricao_situacao (Union[Unset, bool]):
    """

    nome: Union[Unset, bool] = UNSET
    categoria: Union[Unset, bool] = UNSET
    nome_similaridade: Union[Unset, float] = UNSET
    numero_registro: Union[Unset, bool] = UNSET
    data_primeira_habilitacao: Union[Unset, bool] = UNSET
    data_validade: Union[Unset, bool] = UNSET
    registro_nacional_estrangeiro: Union[Unset, bool] = UNSET
    data_ultima_emissao: Union[Unset, bool] = UNSET
    codigo_situacao: Union[Unset, bool] = UNSET
    descricao_situacao: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nome = self.nome
        categoria = self.categoria
        nome_similaridade = self.nome_similaridade
        numero_registro = self.numero_registro
        data_primeira_habilitacao = self.data_primeira_habilitacao
        data_validade = self.data_validade
        registro_nacional_estrangeiro = self.registro_nacional_estrangeiro
        data_ultima_emissao = self.data_ultima_emissao
        codigo_situacao = self.codigo_situacao
        descricao_situacao = self.descricao_situacao

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nome is not UNSET:
            field_dict["nome"] = nome
        if categoria is not UNSET:
            field_dict["categoria"] = categoria
        if nome_similaridade is not UNSET:
            field_dict["nome_similaridade"] = nome_similaridade
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
        if descricao_situacao is not UNSET:
            field_dict["descricao_situacao"] = descricao_situacao

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        nome = d.pop("nome", UNSET)

        categoria = d.pop("categoria", UNSET)

        nome_similaridade = d.pop("nome_similaridade", UNSET)

        numero_registro = d.pop("numero_registro", UNSET)

        data_primeira_habilitacao = d.pop("data_primeira_habilitacao", UNSET)

        data_validade = d.pop("data_validade", UNSET)

        registro_nacional_estrangeiro = d.pop("registro_nacional_estrangeiro", UNSET)

        data_ultima_emissao = d.pop("data_ultima_emissao", UNSET)

        codigo_situacao = d.pop("codigo_situacao", UNSET)

        descricao_situacao = d.pop("descricao_situacao", UNSET)

        cnh_vbeta_1_result = cls(
            nome=nome,
            categoria=categoria,
            nome_similaridade=nome_similaridade,
            numero_registro=numero_registro,
            data_primeira_habilitacao=data_primeira_habilitacao,
            data_validade=data_validade,
            registro_nacional_estrangeiro=registro_nacional_estrangeiro,
            data_ultima_emissao=data_ultima_emissao,
            codigo_situacao=codigo_situacao,
            descricao_situacao=descricao_situacao,
        )

        cnh_vbeta_1_result.additional_properties = d
        return cnh_vbeta_1_result

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
