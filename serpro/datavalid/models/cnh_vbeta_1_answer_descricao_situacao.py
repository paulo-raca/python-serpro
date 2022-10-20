from enum import Enum


class CNHVbeta1AnswerDescricaoSituacao(str, Enum):
    EM_EMISSÃO = "em emissão"
    EMITIDA = "emitida"
    CONFIRMADA = "confirmada"
    CANCELADA = "cancelada"

    def __str__(self) -> str:
        return str(self.value)
