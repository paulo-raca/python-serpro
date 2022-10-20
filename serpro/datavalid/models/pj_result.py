from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.codigo_descricao_result import CodigoDescricaoResult
from ..models.endereco_result import EnderecoResult
from ..models.situacao_cadastral_result import SituacaoCadastralResult
from ..models.telefone_result import TelefoneResult
from ..types import UNSET, Unset

T = TypeVar("T", bound="PJResult")


@attr.s(auto_attribs=True)
class PJResult:
    """
    Attributes:
        porte (Union[Unset, bool]):
        telefone (Union[Unset, TelefoneResult]):
        endereco (Union[Unset, EnderecoResult]):
        cnpj_disponivel (Union[Unset, bool]): Indicates whether the CNPJ exists on the official government basis
        razao_social (Union[Unset, bool]):
        razao_social_similaridade (Union[Unset, float]):
        nome_fantasia (Union[Unset, bool]):
        nome_fantasia_similaridade (Union[Unset, float]):
        data_abertura (Union[Unset, bool]):
        cnae_principal (Union[Unset, CodigoDescricaoResult]):
        natureza_juridica (Union[Unset, CodigoDescricaoResult]):
        situacao_cadastral (Union[Unset, SituacaoCadastralResult]):
        situacao_especial (Union[Unset, bool]):
        situacao_especial_similaridade (Union[Unset, float]):
        nome_orgao (Union[Unset, bool]):
        nome_orgao_similaridade (Union[Unset, float]):
        ente_federativo (Union[Unset, bool]):
        ente_federativo_similaridade (Union[Unset, float]):
        correio_eletronico (Union[Unset, bool]):
        correio_eletronico_similaridade (Union[Unset, float]):
        capital_social (Union[Unset, bool]):
    """

    porte: Union[Unset, bool] = UNSET
    telefone: Union[Unset, TelefoneResult] = UNSET
    endereco: Union[Unset, EnderecoResult] = UNSET
    cnpj_disponivel: Union[Unset, bool] = UNSET
    razao_social: Union[Unset, bool] = UNSET
    razao_social_similaridade: Union[Unset, float] = UNSET
    nome_fantasia: Union[Unset, bool] = UNSET
    nome_fantasia_similaridade: Union[Unset, float] = UNSET
    data_abertura: Union[Unset, bool] = UNSET
    cnae_principal: Union[Unset, CodigoDescricaoResult] = UNSET
    natureza_juridica: Union[Unset, CodigoDescricaoResult] = UNSET
    situacao_cadastral: Union[Unset, SituacaoCadastralResult] = UNSET
    situacao_especial: Union[Unset, bool] = UNSET
    situacao_especial_similaridade: Union[Unset, float] = UNSET
    nome_orgao: Union[Unset, bool] = UNSET
    nome_orgao_similaridade: Union[Unset, float] = UNSET
    ente_federativo: Union[Unset, bool] = UNSET
    ente_federativo_similaridade: Union[Unset, float] = UNSET
    correio_eletronico: Union[Unset, bool] = UNSET
    correio_eletronico_similaridade: Union[Unset, float] = UNSET
    capital_social: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        porte = self.porte
        telefone: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.telefone, Unset):
            telefone = self.telefone.to_dict()

        endereco: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.endereco, Unset):
            endereco = self.endereco.to_dict()

        cnpj_disponivel = self.cnpj_disponivel
        razao_social = self.razao_social
        razao_social_similaridade = self.razao_social_similaridade
        nome_fantasia = self.nome_fantasia
        nome_fantasia_similaridade = self.nome_fantasia_similaridade
        data_abertura = self.data_abertura
        cnae_principal: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cnae_principal, Unset):
            cnae_principal = self.cnae_principal.to_dict()

        natureza_juridica: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.natureza_juridica, Unset):
            natureza_juridica = self.natureza_juridica.to_dict()

        situacao_cadastral: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.situacao_cadastral, Unset):
            situacao_cadastral = self.situacao_cadastral.to_dict()

        situacao_especial = self.situacao_especial
        situacao_especial_similaridade = self.situacao_especial_similaridade
        nome_orgao = self.nome_orgao
        nome_orgao_similaridade = self.nome_orgao_similaridade
        ente_federativo = self.ente_federativo
        ente_federativo_similaridade = self.ente_federativo_similaridade
        correio_eletronico = self.correio_eletronico
        correio_eletronico_similaridade = self.correio_eletronico_similaridade
        capital_social = self.capital_social

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if porte is not UNSET:
            field_dict["porte"] = porte
        if telefone is not UNSET:
            field_dict["telefone"] = telefone
        if endereco is not UNSET:
            field_dict["endereco"] = endereco
        if cnpj_disponivel is not UNSET:
            field_dict["cnpj_disponivel"] = cnpj_disponivel
        if razao_social is not UNSET:
            field_dict["razao_social"] = razao_social
        if razao_social_similaridade is not UNSET:
            field_dict["razao_social_similaridade"] = razao_social_similaridade
        if nome_fantasia is not UNSET:
            field_dict["nome_fantasia"] = nome_fantasia
        if nome_fantasia_similaridade is not UNSET:
            field_dict["nome_fantasia_similaridade"] = nome_fantasia_similaridade
        if data_abertura is not UNSET:
            field_dict["data_abertura"] = data_abertura
        if cnae_principal is not UNSET:
            field_dict["cnae_principal"] = cnae_principal
        if natureza_juridica is not UNSET:
            field_dict["natureza_juridica"] = natureza_juridica
        if situacao_cadastral is not UNSET:
            field_dict["situacao_cadastral"] = situacao_cadastral
        if situacao_especial is not UNSET:
            field_dict["situacao_especial"] = situacao_especial
        if situacao_especial_similaridade is not UNSET:
            field_dict["situacao_especial_similaridade"] = situacao_especial_similaridade
        if nome_orgao is not UNSET:
            field_dict["nome_orgao"] = nome_orgao
        if nome_orgao_similaridade is not UNSET:
            field_dict["nome_orgao_similaridade"] = nome_orgao_similaridade
        if ente_federativo is not UNSET:
            field_dict["ente_federativo"] = ente_federativo
        if ente_federativo_similaridade is not UNSET:
            field_dict["ente_federativo_similaridade"] = ente_federativo_similaridade
        if correio_eletronico is not UNSET:
            field_dict["correio_eletronico"] = correio_eletronico
        if correio_eletronico_similaridade is not UNSET:
            field_dict["correio_eletronico_similaridade"] = correio_eletronico_similaridade
        if capital_social is not UNSET:
            field_dict["capital_social"] = capital_social

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        porte = d.pop("porte", UNSET)

        _telefone = d.pop("telefone", UNSET)
        telefone: Union[Unset, TelefoneResult]
        if isinstance(_telefone, Unset):
            telefone = UNSET
        else:
            telefone = TelefoneResult.from_dict(_telefone)

        _endereco = d.pop("endereco", UNSET)
        endereco: Union[Unset, EnderecoResult]
        if isinstance(_endereco, Unset):
            endereco = UNSET
        else:
            endereco = EnderecoResult.from_dict(_endereco)

        cnpj_disponivel = d.pop("cnpj_disponivel", UNSET)

        razao_social = d.pop("razao_social", UNSET)

        razao_social_similaridade = d.pop("razao_social_similaridade", UNSET)

        nome_fantasia = d.pop("nome_fantasia", UNSET)

        nome_fantasia_similaridade = d.pop("nome_fantasia_similaridade", UNSET)

        data_abertura = d.pop("data_abertura", UNSET)

        _cnae_principal = d.pop("cnae_principal", UNSET)
        cnae_principal: Union[Unset, CodigoDescricaoResult]
        if isinstance(_cnae_principal, Unset):
            cnae_principal = UNSET
        else:
            cnae_principal = CodigoDescricaoResult.from_dict(_cnae_principal)

        _natureza_juridica = d.pop("natureza_juridica", UNSET)
        natureza_juridica: Union[Unset, CodigoDescricaoResult]
        if isinstance(_natureza_juridica, Unset):
            natureza_juridica = UNSET
        else:
            natureza_juridica = CodigoDescricaoResult.from_dict(_natureza_juridica)

        _situacao_cadastral = d.pop("situacao_cadastral", UNSET)
        situacao_cadastral: Union[Unset, SituacaoCadastralResult]
        if isinstance(_situacao_cadastral, Unset):
            situacao_cadastral = UNSET
        else:
            situacao_cadastral = SituacaoCadastralResult.from_dict(_situacao_cadastral)

        situacao_especial = d.pop("situacao_especial", UNSET)

        situacao_especial_similaridade = d.pop("situacao_especial_similaridade", UNSET)

        nome_orgao = d.pop("nome_orgao", UNSET)

        nome_orgao_similaridade = d.pop("nome_orgao_similaridade", UNSET)

        ente_federativo = d.pop("ente_federativo", UNSET)

        ente_federativo_similaridade = d.pop("ente_federativo_similaridade", UNSET)

        correio_eletronico = d.pop("correio_eletronico", UNSET)

        correio_eletronico_similaridade = d.pop("correio_eletronico_similaridade", UNSET)

        capital_social = d.pop("capital_social", UNSET)

        pj_result = cls(
            porte=porte,
            telefone=telefone,
            endereco=endereco,
            cnpj_disponivel=cnpj_disponivel,
            razao_social=razao_social,
            razao_social_similaridade=razao_social_similaridade,
            nome_fantasia=nome_fantasia,
            nome_fantasia_similaridade=nome_fantasia_similaridade,
            data_abertura=data_abertura,
            cnae_principal=cnae_principal,
            natureza_juridica=natureza_juridica,
            situacao_cadastral=situacao_cadastral,
            situacao_especial=situacao_especial,
            situacao_especial_similaridade=situacao_especial_similaridade,
            nome_orgao=nome_orgao,
            nome_orgao_similaridade=nome_orgao_similaridade,
            ente_federativo=ente_federativo,
            ente_federativo_similaridade=ente_federativo_similaridade,
            correio_eletronico=correio_eletronico,
            correio_eletronico_similaridade=correio_eletronico_similaridade,
            capital_social=capital_social,
        )

        pj_result.additional_properties = d
        return pj_result

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
