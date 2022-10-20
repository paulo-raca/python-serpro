from enum import Enum


class DigitalOldAnswerFormato(str, Enum):
    JPG = "JPG"
    PNG = "PNG"
    WSQ = "WSQ"

    def __str__(self) -> str:
        return str(self.value)
