# Exercício 05: Dicionários e Mapeamento de Dados

## Objetivo
Dominar dicionários (`dict`), verificação de chaves com `in` ou `.get()`, e construção de listas como valores de chaves.

## Requisitos
1. `contar_frequencia_palavras(texto)`:
   - Limpe pontuações (`.replace(".", "").replace(",", "")`, etc.).
   - Converta para minúsculo (`.lower()`).
   - Itere pelas palavras e incremente a contagem no dicionário.
2. `agrupar_por_tamanho(palavras)`:
   - Para cada palavra, descubra `tam = len(palavra)`.
   - Se `tam` ainda não está no dict, crie uma lista vazia `d[tam] = []`.
   - Dê `.append(palavra)`.

## Documentação oficial:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries
