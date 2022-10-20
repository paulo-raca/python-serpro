from enum import Enum


class PFDigitalAnswerSexo(str, Enum):
    F = "F"
    M = "M"

    def __str__(self) -> str:
        return str(self.value)
