from enum import Enum


class PFFacialCdvResultDocumento(str, Enum):
    CNH = "CNH"

    def __str__(self) -> str:
        return str(self.value)
