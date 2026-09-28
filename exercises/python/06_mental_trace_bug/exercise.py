# Exercício 06: Bug Tracing (Armadilhas Reais do Runtime)
# Documentação oficial: https://docs.python.org/3/tutorial/controlflow.html#default-argument-values

# ATENÇÃO: Esta função tem um bug clássico de modelo mental em Python.
# O argumento default mutável faz com que chamadas sucessivas compartilhem o mesmo estado!
def registrar_participante(nome: str, participantes: list = []) -> list:
    """
    Adiciona um participante à lista e retorna a lista atualizada.
    Se nenhuma lista for fornecida, deve iniciar uma NOVA lista vazia isolada.
    """
    participantes.append(nome)
    return participantes


def somar_fatias_janela(valores: list[int], tamanho_janela: int) -> list[int]:
    """
    Calcula a soma de janelas deslizantes de tamanho 'tamanho_janela'.
    Exemplo: valores=[1, 2, 3, 4], tamanho=2 -> [3, 5, 7]
    (1+2=3, 2+3=5, 3+4=7)

    BUG ATUAL: a iteração está errada no limite superior e perdendo a última fatia!
    """
    resultado = []
    # DICA: preste atenção no limite do range (off-by-one error)
    for i in range(len(valores) - tamanho_janela):
        janela = valores[i : i + tamanho_janela]
        resultado.append(sum(janela))
    return resultado
