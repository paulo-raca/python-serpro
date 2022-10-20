from enum import Enum


class PFImagemVbeta1AnswerSexo(str, Enum):
    F = "F"
    M = "M"

    def __str__(self) -> str:
        return str(self.value)
