from enum import Enum


class FaceResultProbabilidade(str, Enum):
    ALTÍSSIMA_PROBABILIDADE = "Altíssima probabilidade"
    ALTA_PROBABILIDADE = "Alta probabilidade"
    BAIXA_PROBABILIDADE = "Baixa probabilidade"
    BAIXÍSSIMA_PROBABILIDADE = "Baixíssima probabilidade"

    def __str__(self) -> str:
        return str(self.value)
