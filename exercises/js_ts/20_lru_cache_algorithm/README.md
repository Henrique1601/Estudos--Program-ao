# Nível 20: Algoritmo Avançado - Cache LRU (Least Recently Used)

## Objetivo
Implementar uma estrutura de dados fundamental em engenharia de software de alta performance: o cache LRU com operações em O(1).

## Requisitos
Implementar `LRUCache<K, V>(capacidade: number)`:
1. `get(chave: K): V | undefined`:
   - Se existir, retorna o valor e atualiza a chave como a MAIS RECENTEMENTE usada.
   - Se não existir, retorna undefined.
2. `put(chave: K, valor: V): void`:
   - Insere ou atualiza o valor.
   - Marca a chave como mais recentemente usada.
   - Se ultrapassar a capacidade máxima, descarta a chave MENOS recentemente usada (eviction).
3. `tamanho(): number`:
   - Retorna o número de itens armazenados no momento.

## Documentação oficial:
https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Map
