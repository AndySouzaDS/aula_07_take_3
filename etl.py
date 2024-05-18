# a funcao csv, poderia ser colocada dentro da funcao, mas como sera usada outras vezes será colocada fora.
import csv

caminho_arquivo = 'vendas.csv'


def ler_csv(nome_do_arquivo_csv: str) -> list[dict]:
    """Funcao que le um arquivo em csv e retorna uma lista de dicionarios.

    Args:
        nome_do_arquivo_csv (str): lista de vendas

    Returns:
        list[dict]: dicionario com informacoes das vendas
    """
    lista = []
    with open(nome_do_arquivo_csv, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista


vendas_itens: list[dict]

vendas_itens = ler_csv(caminho_arquivo)
print(vendas_itens)
