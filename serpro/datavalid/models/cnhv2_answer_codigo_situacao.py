from enum import Enum


class CNHV2AnswerCodigoSituacao(str, Enum):
    VALUE_0 = "0"
    VALUE_1 = "1"
    VALUE_2 = "2"
    VALUE_3 = "3"
    VALUE_4 = "4"
    VALUE_5 = "5"
    VALUE_6 = "6"
    A = "A"
    B = "B"
    Z = "Z"

    def __str__(self) -> str:
        return str(self.value)
