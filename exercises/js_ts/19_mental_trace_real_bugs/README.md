# Nível 19: Bug Hunting Real (Sort, Shallow Copy, Async forEach)

## Objetivo
Identificar e corrigir as 3 armadilhas de modelo mental mais comuns do ecossistema JS/TS.

## Requisitos
1. `ordenarNumeros`: Consertar ordenação de números (não lexicográfica).
2. `atualizarCidadeSemMutarOriginal`: Impedir mutação de objeto original aninhado com cópia profunda.
3. `carregarTodos`: Substituir o forEach assíncrono que retorna antes das promessas terminarem.

## Documentação oficial:
https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Array/sort
