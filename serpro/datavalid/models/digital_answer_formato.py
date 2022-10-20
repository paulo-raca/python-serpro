from enum import Enum


class DigitalAnswerFormato(str, Enum):
    ISO = "ISO"
    JPG = "JPG"
    PNG = "PNG"
    WSQ = "WSQ"

    def __str__(self) -> str:
        return str(self.value)
