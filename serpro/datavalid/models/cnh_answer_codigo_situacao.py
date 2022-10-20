from enum import Enum


class CNHAnswerCodigoSituacao(str, Enum):
    VALUE_0 = "2"
    VALUE_1 = "3"
    A = "A"

    def __str__(self) -> str:
        return str(self.value)
