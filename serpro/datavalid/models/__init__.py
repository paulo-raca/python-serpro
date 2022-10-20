""" Contains all the data models used in inputs/outputs """

from .arquivo_answer import ArquivoAnswer
from .arquivo_answer_formato import ArquivoAnswerFormato
from .cnh_answer import CNHAnswer
from .cnh_answer_codigo_situacao import CNHAnswerCodigoSituacao
from .cnh_biometry_vbeta_1_answer import CNHBiometryVbeta1Answer
from .cnh_biometry_vbeta_1_result import CNHBiometryVbeta1Result
from .cnh_cdv_result import CNHCdvResult
from .cnh_result import CNHResult
from .cnh_vbeta_1_answer import CNHVbeta1Answer
from .cnh_vbeta_1_answer_codigo_situacao import CNHVbeta1AnswerCodigoSituacao
from .cnh_vbeta_1_answer_descricao_situacao import CNHVbeta1AnswerDescricaoSituacao
from .cnh_vbeta_1_result import CNHVbeta1Result
from .cnhv1_answer import CNHV1Answer
from .cnhv1_answer_codigo_situacao import CNHV1AnswerCodigoSituacao
from .cnhv1_result import CNHV1Result
from .cnhv2_answer import CNHV2Answer
from .cnhv2_answer_codigo_situacao import CNHV2AnswerCodigoSituacao
from .codigo_descricao_answer import CodigoDescricaoAnswer
from .codigo_descricao_result import CodigoDescricaoResult
from .digitais_result import DigitaisResult
from .digital_answer import DigitalAnswer
from .digital_answer_formato import DigitalAnswerFormato
from .digital_answer_posicao import DigitalAnswerPosicao
from .digital_old_answer import DigitalOldAnswer
from .digital_old_answer_formato import DigitalOldAnswerFormato
from .digital_old_answer_posicao import DigitalOldAnswerPosicao
from .digital_result import DigitalResult
from .digital_result_posicao import DigitalResultPosicao
from .digital_result_probabilidade import DigitalResultProbabilidade
from .documento_answer import DocumentoAnswer
from .documento_answer_tipo import DocumentoAnswerTipo
from .documento_answer_uf_expedidor import DocumentoAnswerUfExpedidor
from .documento_result import DocumentoResult
from .documento_vbeta_1_result import DocumentoVbeta1Result
from .endereco_answer import EnderecoAnswer
from .endereco_answer_uf import EnderecoAnswerUf
from .endereco_result import EnderecoResult
from .face_answer import FaceAnswer
from .face_answer_formato import FaceAnswerFormato
from .face_result import FaceResult
from .face_result_probabilidade import FaceResultProbabilidade
from .filiacao_answer import FiliacaoAnswer
from .filiacao_result import FiliacaoResult
from .gateway_negate import GatewayNegate
from .integration import Integration
from .pf_basica_answer import PFBasicaAnswer
from .pf_basica_answer_nacionalidade import PFBasicaAnswerNacionalidade
from .pf_basica_answer_sexo import PFBasicaAnswerSexo
from .pf_basica_answer_situacao_cpf import PFBasicaAnswerSituacaoCpf
from .pf_basica_input import PFBasicaInput
from .pf_basica_result import PFBasicaResult
from .pf_digitais_v1_answer import PFDigitaisV1Answer
from .pf_digitais_v1_answer_nacionalidade import PFDigitaisV1AnswerNacionalidade
from .pf_digitais_v1_answer_sexo import PFDigitaisV1AnswerSexo
from .pf_digitais_v1_answer_situacao_cpf import PFDigitaisV1AnswerSituacaoCpf
from .pf_digitais_v1_input import PFDigitaisV1Input
from .pf_digitais_v1_result import PFDigitaisV1Result
from .pf_digitais_v2_answer import PFDigitaisV2Answer
from .pf_digitais_v2_answer_nacionalidade import PFDigitaisV2AnswerNacionalidade
from .pf_digitais_v2_answer_sexo import PFDigitaisV2AnswerSexo
from .pf_digitais_v2_answer_situacao_cpf import PFDigitaisV2AnswerSituacaoCpf
from .pf_digitais_v2_input import PFDigitaisV2Input
from .pf_digitais_v2_result import PFDigitaisV2Result
from .pf_digitais_vbeta_1_answer import PFDigitaisVbeta1Answer
from .pf_digitais_vbeta_1_answer_nacionalidade import PFDigitaisVbeta1AnswerNacionalidade
from .pf_digitais_vbeta_1_answer_sexo import PFDigitaisVbeta1AnswerSexo
from .pf_digitais_vbeta_1_answer_situacao_cpf import PFDigitaisVbeta1AnswerSituacaoCpf
from .pf_digitais_vbeta_1_input import PFDigitaisVbeta1Input
from .pf_digitais_vbeta_1_result import PFDigitaisVbeta1Result
from .pf_digital_answer import PFDigitalAnswer
from .pf_digital_answer_nacionalidade import PFDigitalAnswerNacionalidade
from .pf_digital_answer_sexo import PFDigitalAnswerSexo
from .pf_digital_answer_situacao_cpf import PFDigitalAnswerSituacaoCpf
from .pf_digital_input import PFDigitalInput
from .pf_digital_result import PFDigitalResult
from .pf_face_v1_answer import PFFaceV1Answer
from .pf_face_v1_answer_nacionalidade import PFFaceV1AnswerNacionalidade
from .pf_face_v1_answer_sexo import PFFaceV1AnswerSexo
from .pf_face_v1_answer_situacao_cpf import PFFaceV1AnswerSituacaoCpf
from .pf_face_v1_input import PFFaceV1Input
from .pf_face_v1_result import PFFaceV1Result
from .pf_face_v2_answer import PFFaceV2Answer
from .pf_face_v2_answer_nacionalidade import PFFaceV2AnswerNacionalidade
from .pf_face_v2_answer_sexo import PFFaceV2AnswerSexo
from .pf_face_v2_answer_situacao_cpf import PFFaceV2AnswerSituacaoCpf
from .pf_face_v2_input import PFFaceV2Input
from .pf_face_v2_result import PFFaceV2Result
from .pf_face_vbeta_1_answer import PFFaceVbeta1Answer
from .pf_face_vbeta_1_answer_nacionalidade import PFFaceVbeta1AnswerNacionalidade
from .pf_face_vbeta_1_answer_sexo import PFFaceVbeta1AnswerSexo
from .pf_face_vbeta_1_answer_situacao_cpf import PFFaceVbeta1AnswerSituacaoCpf
from .pf_face_vbeta_1_input import PFFaceVbeta1Input
from .pf_face_vbeta_1_result import PFFaceVbeta1Result
from .pf_facial_answer import PFFacialAnswer
from .pf_facial_answer_nacionalidade import PFFacialAnswerNacionalidade
from .pf_facial_answer_sexo import PFFacialAnswerSexo
from .pf_facial_answer_situacao_cpf import PFFacialAnswerSituacaoCpf
from .pf_facial_cdv_answer import PFFacialCdvAnswer
from .pf_facial_cdv_input import PFFacialCdvInput
from .pf_facial_cdv_result import PFFacialCdvResult
from .pf_facial_cdv_result_documento import PFFacialCdvResultDocumento
from .pf_facial_digital_answer import PFFacialDigitalAnswer
from .pf_facial_digital_answer_nacionalidade import PFFacialDigitalAnswerNacionalidade
from .pf_facial_digital_answer_sexo import PFFacialDigitalAnswerSexo
from .pf_facial_digital_answer_situacao_cpf import PFFacialDigitalAnswerSituacaoCpf
from .pf_facial_digital_input import PFFacialDigitalInput
from .pf_facial_digital_result import PFFacialDigitalResult
from .pf_facial_input import PFFacialInput
from .pf_facial_result import PFFacialResult
from .pf_imagem_v1_answer import PFImagemV1Answer
from .pf_imagem_v1_answer_nacionalidade import PFImagemV1AnswerNacionalidade
from .pf_imagem_v1_answer_sexo import PFImagemV1AnswerSexo
from .pf_imagem_v1_answer_situacao_cpf import PFImagemV1AnswerSituacaoCpf
from .pf_imagem_v1_input import PFImagemV1Input
from .pf_imagem_v1_result import PFImagemV1Result
from .pf_imagem_v2_answer import PFImagemV2Answer
from .pf_imagem_v2_answer_nacionalidade import PFImagemV2AnswerNacionalidade
from .pf_imagem_v2_answer_sexo import PFImagemV2AnswerSexo
from .pf_imagem_v2_answer_situacao_cpf import PFImagemV2AnswerSituacaoCpf
from .pf_imagem_v2_input import PFImagemV2Input
from .pf_imagem_v2_result import PFImagemV2Result
from .pf_imagem_vbeta_1_answer import PFImagemVbeta1Answer
from .pf_imagem_vbeta_1_answer_nacionalidade import PFImagemVbeta1AnswerNacionalidade
from .pf_imagem_vbeta_1_answer_sexo import PFImagemVbeta1AnswerSexo
from .pf_imagem_vbeta_1_answer_situacao_cpf import PFImagemVbeta1AnswerSituacaoCpf
from .pf_imagem_vbeta_1_input import PFImagemVbeta1Input
from .pf_imagem_vbeta_1_result import PFImagemVbeta1Result
from .pf_key import PFKey
from .pf_vbeta_1_answer import PFVbeta1Answer
from .pf_vbeta_1_answer_nacionalidade import PFVbeta1AnswerNacionalidade
from .pf_vbeta_1_answer_sexo import PFVbeta1AnswerSexo
from .pf_vbeta_1_answer_situacao_cpf import PFVbeta1AnswerSituacaoCpf
from .pf_vbeta_1_input import PFVbeta1Input
from .pf_vbeta_1_result import PFVbeta1Result
from .pfv1_answer import PFV1Answer
from .pfv1_answer_nacionalidade import PFV1AnswerNacionalidade
from .pfv1_answer_sexo import PFV1AnswerSexo
from .pfv1_answer_situacao_cpf import PFV1AnswerSituacaoCpf
from .pfv1_input import PFV1Input
from .pfv1_result import PFV1Result
from .pfv2_answer import PFV2Answer
from .pfv2_answer_nacionalidade import PFV2AnswerNacionalidade
from .pfv2_answer_sexo import PFV2AnswerSexo
from .pfv2_answer_situacao_cpf import PFV2AnswerSituacaoCpf
from .pfv2_input import PFV2Input
from .pfv2_result import PFV2Result
from .pj_answer import PJAnswer
from .pj_answer_porte import PJAnswerPorte
from .pj_input import PJInput
from .pj_key import PJKey
from .pj_result import PJResult
from .situacao_cadastral_answer import SituacaoCadastralAnswer
from .situacao_cadastral_answer_codigo import SituacaoCadastralAnswerCodigo
from .situacao_cadastral_result import SituacaoCadastralResult
from .telefone_answer import TelefoneAnswer
from .telefone_result import TelefoneResult
from .violation import Violation

__all__ = (
    "ArquivoAnswer",
    "ArquivoAnswerFormato",
    "CNHAnswer",
    "CNHAnswerCodigoSituacao",
    "CNHBiometryVbeta1Answer",
    "CNHBiometryVbeta1Result",
    "CNHCdvResult",
    "CNHResult",
    "CNHV1Answer",
    "CNHV1AnswerCodigoSituacao",
    "CNHV1Result",
    "CNHV2Answer",
    "CNHV2AnswerCodigoSituacao",
    "CNHVbeta1Answer",
    "CNHVbeta1AnswerCodigoSituacao",
    "CNHVbeta1AnswerDescricaoSituacao",
    "CNHVbeta1Result",
    "CodigoDescricaoAnswer",
    "CodigoDescricaoResult",
    "DigitaisResult",
    "DigitalAnswer",
    "DigitalAnswerFormato",
    "DigitalAnswerPosicao",
    "DigitalOldAnswer",
    "DigitalOldAnswerFormato",
    "DigitalOldAnswerPosicao",
    "DigitalResult",
    "DigitalResultPosicao",
    "DigitalResultProbabilidade",
    "DocumentoAnswer",
    "DocumentoAnswerTipo",
    "DocumentoAnswerUfExpedidor",
    "DocumentoResult",
    "DocumentoVbeta1Result",
    "EnderecoAnswer",
    "EnderecoAnswerUf",
    "EnderecoResult",
    "FaceAnswer",
    "FaceAnswerFormato",
    "FaceResult",
    "FaceResultProbabilidade",
    "FiliacaoAnswer",
    "FiliacaoResult",
    "GatewayNegate",
    "Integration",
    "PFBasicaAnswer",
    "PFBasicaAnswerNacionalidade",
    "PFBasicaAnswerSexo",
    "PFBasicaAnswerSituacaoCpf",
    "PFBasicaInput",
    "PFBasicaResult",
    "PFDigitaisV1Answer",
    "PFDigitaisV1AnswerNacionalidade",
    "PFDigitaisV1AnswerSexo",
    "PFDigitaisV1AnswerSituacaoCpf",
    "PFDigitaisV1Input",
    "PFDigitaisV1Result",
    "PFDigitaisV2Answer",
    "PFDigitaisV2AnswerNacionalidade",
    "PFDigitaisV2AnswerSexo",
    "PFDigitaisV2AnswerSituacaoCpf",
    "PFDigitaisV2Input",
    "PFDigitaisV2Result",
    "PFDigitaisVbeta1Answer",
    "PFDigitaisVbeta1AnswerNacionalidade",
    "PFDigitaisVbeta1AnswerSexo",
    "PFDigitaisVbeta1AnswerSituacaoCpf",
    "PFDigitaisVbeta1Input",
    "PFDigitaisVbeta1Result",
    "PFDigitalAnswer",
    "PFDigitalAnswerNacionalidade",
    "PFDigitalAnswerSexo",
    "PFDigitalAnswerSituacaoCpf",
    "PFDigitalInput",
    "PFDigitalResult",
    "PFFaceV1Answer",
    "PFFaceV1AnswerNacionalidade",
    "PFFaceV1AnswerSexo",
    "PFFaceV1AnswerSituacaoCpf",
    "PFFaceV1Input",
    "PFFaceV1Result",
    "PFFaceV2Answer",
    "PFFaceV2AnswerNacionalidade",
    "PFFaceV2AnswerSexo",
    "PFFaceV2AnswerSituacaoCpf",
    "PFFaceV2Input",
    "PFFaceV2Result",
    "PFFaceVbeta1Answer",
    "PFFaceVbeta1AnswerNacionalidade",
    "PFFaceVbeta1AnswerSexo",
    "PFFaceVbeta1AnswerSituacaoCpf",
    "PFFaceVbeta1Input",
    "PFFaceVbeta1Result",
    "PFFacialAnswer",
    "PFFacialAnswerNacionalidade",
    "PFFacialAnswerSexo",
    "PFFacialAnswerSituacaoCpf",
    "PFFacialCdvAnswer",
    "PFFacialCdvInput",
    "PFFacialCdvResult",
    "PFFacialCdvResultDocumento",
    "PFFacialDigitalAnswer",
    "PFFacialDigitalAnswerNacionalidade",
    "PFFacialDigitalAnswerSexo",
    "PFFacialDigitalAnswerSituacaoCpf",
    "PFFacialDigitalInput",
    "PFFacialDigitalResult",
    "PFFacialInput",
    "PFFacialResult",
    "PFImagemV1Answer",
    "PFImagemV1AnswerNacionalidade",
    "PFImagemV1AnswerSexo",
    "PFImagemV1AnswerSituacaoCpf",
    "PFImagemV1Input",
    "PFImagemV1Result",
    "PFImagemV2Answer",
    "PFImagemV2AnswerNacionalidade",
    "PFImagemV2AnswerSexo",
    "PFImagemV2AnswerSituacaoCpf",
    "PFImagemV2Input",
    "PFImagemV2Result",
    "PFImagemVbeta1Answer",
    "PFImagemVbeta1AnswerNacionalidade",
    "PFImagemVbeta1AnswerSexo",
    "PFImagemVbeta1AnswerSituacaoCpf",
    "PFImagemVbeta1Input",
    "PFImagemVbeta1Result",
    "PFKey",
    "PFV1Answer",
    "PFV1AnswerNacionalidade",
    "PFV1AnswerSexo",
    "PFV1AnswerSituacaoCpf",
    "PFV1Input",
    "PFV1Result",
    "PFV2Answer",
    "PFV2AnswerNacionalidade",
    "PFV2AnswerSexo",
    "PFV2AnswerSituacaoCpf",
    "PFV2Input",
    "PFV2Result",
    "PFVbeta1Answer",
    "PFVbeta1AnswerNacionalidade",
    "PFVbeta1AnswerSexo",
    "PFVbeta1AnswerSituacaoCpf",
    "PFVbeta1Input",
    "PFVbeta1Result",
    "PJAnswer",
    "PJAnswerPorte",
    "PJInput",
    "PJKey",
    "PJResult",
    "SituacaoCadastralAnswer",
    "SituacaoCadastralAnswerCodigo",
    "SituacaoCadastralResult",
    "TelefoneAnswer",
    "TelefoneResult",
    "Violation",
)
