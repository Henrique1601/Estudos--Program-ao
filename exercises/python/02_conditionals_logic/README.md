# Exercício 02: Condicionais e Lógica Booleana

## Objetivo
Trabalhar com operadores de comparação (`==`, `!=`, `<`, `>`) e lógicos (`and`, `or`, `not`), evitando aninhamentos desnecessários (guard clauses).

## Requisitos
1. `eh_bissexto(ano)`:
   - Divisível por 4 e (não divisível por 100 ou divisível por 400).
2. `classificar_triangulo(a, b, c)`:
   - Condição de existência: cada lado deve ser maior que zero e menor que a soma dos outros dois (`a < b + c` e `b < a + c` e `c < a + b`).
   - Se falhar na existência, retorne `"invalido"`.
   - Se os 3 lados forem iguais: `"equilatero"`.
   - Se 2 lados forem iguais: `"isosceles"`.
   - Se os 3 forem diferentes: `"escaleno"`.

## Documentação oficial:
https://docs.python.org/3/tutorial/controlflow.html#if-statements
