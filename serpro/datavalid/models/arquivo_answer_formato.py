from enum import Enum


class ArquivoAnswerFormato(str, Enum):
    JPG = "JPG"
    PDF = "PDF"
    PNG = "PNG"

    def __str__(self) -> str:
        return str(self.value)
