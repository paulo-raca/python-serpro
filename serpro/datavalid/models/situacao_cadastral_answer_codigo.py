from enum import IntEnum


class SituacaoCadastralAnswerCodigo(IntEnum):
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_8 = 8

    def __str__(self) -> str:
        return str(self.value)
