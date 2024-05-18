# Calcular Média de Valores em uma Lista

from typing import List


def calcular_media(valores: List[float]) -> float:
    return sum(valores) / len(valores)


notas = [7.5, 9.75, 10, 9.25, 2.5]
print(calcular_media(notas))
