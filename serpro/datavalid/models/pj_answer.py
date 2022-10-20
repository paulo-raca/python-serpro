import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.codigo_descricao_answer import CodigoDescricaoAnswer
from ..models.endereco_answer import EnderecoAnswer
from ..models.pj_answer_porte import PJAnswerPorte
from ..models.situacao_cadastral_answer import SituacaoCadastralAnswer
from ..models.telefone_answer import TelefoneAnswer
from ..types import UNSET, Unset

T = TypeVar("T", bound="PJAnswer")


@attr.s(auto_attribs=True)
class PJAnswer:
    """
    Attributes:
        endereco (Union[Unset, EnderecoAnswer]):
        porte (Union[Unset, PJAnswerPorte]): 00 - não informado, 01 - microempresa, 03 - empresa pequeno porte, 05 -
            empresa grande porte
        telefone (Union[Unset, TelefoneAnswer]):
        razao_social (Union[Unset, str]):
        nome_fantasia (Union[Unset, str]):
        data_abertura (Union[Unset, datetime.date]):
        cnae_principal (Union[Unset, CodigoDescricaoAnswer]):
        natureza_juridica (Union[Unset, CodigoDescricaoAnswer]):
        situacao_cadastral (Union[Unset, SituacaoCadastralAnswer]):
        situacao_especial (Union[Unset, str]):
        nome_orgao (Union[Unset, str]):
        ente_federativo (Union[Unset, str]):
        correio_eletronico (Union[Unset, str]):
        capital_social (Union[Unset, float]):
    """

    endereco: Union[Unset, EnderecoAnswer] = UNSET
    porte: Union[Unset, PJAnswerPorte] = UNSET
    telefone: Union[Unset, TelefoneAnswer] = UNSET
    razao_social: Union[Unset, str] = UNSET
    nome_fantasia: Union[Unset, str] = UNSET
    data_abertura: Union[Unset, datetime.date] = UNSET
    cnae_principal: Union[Unset, CodigoDescricaoAnswer] = UNSET
    natureza_juridica: Union[Unset, CodigoDescricaoAnswer] = UNSET
    situacao_cadastral: Union[Unset, SituacaoCadastralAnswer] = UNSET
    situacao_especial: Union[Unset, str] = UNSET
    nome_orgao: Union[Unset, str] = UNSET
    ente_federativo: Union[Unset, str] = UNSET
    correio_eletronico: Union[Unset, str] = UNSET
    capital_social: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        endereco: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.endereco, Unset):
            endereco = self.endereco.to_dict()

        porte: Union[Unset, str] = UNSET
        if not isinstance(self.porte, Unset):
            porte = self.porte.value

        telefone: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.telefone, Unset):
            telefone = self.telefone.to_dict()

        razao_social = self.razao_social
        nome_fantasia = self.nome_fantasia
        data_abertura: Union[Unset, str] = UNSET
        if not isinstance(self.data_abertura, Unset):
            data_abertura = self.data_abertura.isoformat()

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
        nome_orgao = self.nome_orgao
        ente_federativo = self.ente_federativo
        correio_eletronico = self.correio_eletronico
        capital_social = self.capital_social

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if endereco is not UNSET:
            field_dict["endereco"] = endereco
        if porte is not UNSET:
            field_dict["porte"] = porte
        if telefone is not UNSET:
            field_dict["telefone"] = telefone
        if razao_social is not UNSET:
            field_dict["razao_social"] = razao_social
        if nome_fantasia is not UNSET:
            field_dict["nome_fantasia"] = nome_fantasia
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
        if nome_orgao is not UNSET:
            field_dict["nome_orgao"] = nome_orgao
        if ente_federativo is not UNSET:
            field_dict["ente_federativo"] = ente_federativo
        if correio_eletronico is not UNSET:
            field_dict["correio_eletronico"] = correio_eletronico
        if capital_social is not UNSET:
            field_dict["capital_social"] = capital_social

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _endereco = d.pop("endereco", UNSET)
        endereco: Union[Unset, EnderecoAnswer]
        if isinstance(_endereco, Unset):
            endereco = UNSET
        else:
            endereco = EnderecoAnswer.from_dict(_endereco)

        _porte = d.pop("porte", UNSET)
        porte: Union[Unset, PJAnswerPorte]
        if isinstance(_porte, Unset):
            porte = UNSET
        else:
            porte = PJAnswerPorte(_porte)

        _telefone = d.pop("telefone", UNSET)
        telefone: Union[Unset, TelefoneAnswer]
        if isinstance(_telefone, Unset):
            telefone = UNSET
        else:
            telefone = TelefoneAnswer.from_dict(_telefone)

        razao_social = d.pop("razao_social", UNSET)

        nome_fantasia = d.pop("nome_fantasia", UNSET)

        _data_abertura = d.pop("data_abertura", UNSET)
        data_abertura: Union[Unset, datetime.date]
        if isinstance(_data_abertura, Unset):
            data_abertura = UNSET
        else:
            data_abertura = isoparse(_data_abertura).date()

        _cnae_principal = d.pop("cnae_principal", UNSET)
        cnae_principal: Union[Unset, CodigoDescricaoAnswer]
        if isinstance(_cnae_principal, Unset):
            cnae_principal = UNSET
        else:
            cnae_principal = CodigoDescricaoAnswer.from_dict(_cnae_principal)

        _natureza_juridica = d.pop("natureza_juridica", UNSET)
        natureza_juridica: Union[Unset, CodigoDescricaoAnswer]
        if isinstance(_natureza_juridica, Unset):
            natureza_juridica = UNSET
        else:
            natureza_juridica = CodigoDescricaoAnswer.from_dict(_natureza_juridica)

        _situacao_cadastral = d.pop("situacao_cadastral", UNSET)
        situacao_cadastral: Union[Unset, SituacaoCadastralAnswer]
        if isinstance(_situacao_cadastral, Unset):
            situacao_cadastral = UNSET
        else:
            situacao_cadastral = SituacaoCadastralAnswer.from_dict(_situacao_cadastral)

        situacao_especial = d.pop("situacao_especial", UNSET)

        nome_orgao = d.pop("nome_orgao", UNSET)

        ente_federativo = d.pop("ente_federativo", UNSET)

        correio_eletronico = d.pop("correio_eletronico", UNSET)

        capital_social = d.pop("capital_social", UNSET)

        pj_answer = cls(
            endereco=endereco,
            porte=porte,
            telefone=telefone,
            razao_social=razao_social,
            nome_fantasia=nome_fantasia,
            data_abertura=data_abertura,
            cnae_principal=cnae_principal,
            natureza_juridica=natureza_juridica,
            situacao_cadastral=situacao_cadastral,
            situacao_especial=situacao_especial,
            nome_orgao=nome_orgao,
            ente_federativo=ente_federativo,
            correio_eletronico=correio_eletronico,
            capital_social=capital_social,
        )

        pj_answer.additional_properties = d
        return pj_answer

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
