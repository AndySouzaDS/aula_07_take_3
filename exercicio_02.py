## 2 - Filtrar Dados Acima de um Limite

from typing import List


def filtrar_acima_de(valores: List[float], limite: float) -> float:
    resultados = []
    for valor in valores:
        if valor > limite:
            resultados.append(valor)
    return resultados

lista = [10, 2, 19, 62]
print(filtrar_acima_de(lista, 2))
