# Exercício 03: Laços e Acumuladores

## Objetivo
Treinar a simulação mental de iterações em listas e manipulação de variáveis acumuladoras.

## Requisitos
1. `somar_impares(numeros)`:
   - Itera por cada número. Se `n % 2 != 0`, acumula na soma.
2. `encontrar_maior(numeros)`:
   - Se `len(numeros) == 0`, deve lançar: `raise ValueError("Lista vazia")`.
   - Inicialize a variável de maior valor com o primeiro elemento da lista (`numeros[0]`), nunca com zero (pois a lista pode ter só números negativos).
   - Itere pelo restante e atualize se encontrar valor maior. Proibido usar `max()`.

## Documentação oficial:
https://docs.python.org/3/tutorial/controlflow.html#for-statements
