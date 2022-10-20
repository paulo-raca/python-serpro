from enum import Enum


class FaceAnswerFormato(str, Enum):
    JPG = "JPG"
    PDF = "PDF"
    PNG = "PNG"

    def __str__(self) -> str:
        return str(self.value)
