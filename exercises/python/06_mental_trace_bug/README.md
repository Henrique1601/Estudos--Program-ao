# Exercício 06: Bug Tracing (Armadilhas Reais do Runtime)

## Objetivo
Treinar depuração deliberada de dois dos erros mais comuns de iniciantes:
1. Argumentos padrão mutáveis em Python (`def fn(x, lista=[])`).
2. Erros de limite em laços de repetição (*Off-By-One*).

## Tarefa
1. Abra `exercise.py`.
2. Em `registrar_participante`: use a técnica idiomática de `participantes = None` e inicialize dentro da função.
3. Em `somar_fatias_janela`: ajuste o limite do `range` para que a última janela não seja ignorada.

## Documentação oficial:
https://docs.python.org/3/tutorial/controlflow.html#default-argument-values
