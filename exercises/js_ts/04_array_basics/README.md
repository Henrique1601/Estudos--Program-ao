# Nível 04: Fundamentos de Arrays e Fatiamento

## Objetivo
Manipular vetores sem usar métodos mágicos prontas quando exigido, treinando algoritmos de busca.

## Requisitos
1. `encontrarExtremos(numeros: number[])`: Retorna `{ min: number, max: number }`. Lança Error("Array vazio") se vazio. Não use Math.min / Math.max!
2. `dividirEmFatias<T>(itens: T[], tamanhoFatia: number)`: Divide o array em chunks de tamanho especificado. Se tamanho <= 0 lance RangeError.

## Documentação oficial:
https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Array/slice
