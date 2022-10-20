from enum import Enum


class PJAnswerPorte(str, Enum):
    VALUE_0 = "00"
    VALUE_1 = "01"
    VALUE_2 = "03"
    VALUE_3 = "05"

    def __str__(self) -> str:
        return str(self.value)
