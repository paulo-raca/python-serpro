from enum import Enum


class PFFacialAnswerSituacaoCpf(str, Enum):
    REGULAR = "regular"
    SUSPENSA = "suspensa"
    TITULAR_FALECIDO = "titular falecido"
    PENDENTE_DE_REGULARIZAÇÃO = "pendente de regularização"
    CANCELADA_POR_MULTIPLICIDADE = "cancelada por multiplicidade"
    NULA = "nula"
    CANCELADA_DE_OFICIO = "cancelada de oficio"

    def __str__(self) -> str:
        return str(self.value)
