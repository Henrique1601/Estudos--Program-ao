# Nível 13: TypeScript - Tipos Genéricos (Generics)

## Objetivo
Projetar estruturas de dados e funções reutilizáveis preservando a segurança de tipo do TypeScript.

## Requisitos
1. Implementar a classe `Fila<T>` (FIFO):
   - `enfileirar(item: T): void`
   - `desenfileirar(): T | undefined`
   - `tamanho(): number`
   - `primeiro(): T | undefined`
2. `trocarPrimeiroComUltimo<T>(lista: T[]): T[]`: Retorna um novo array com primeiro e último itens trocados de posição.

## Documentação oficial:
https://www.typescriptlang.org/docs/handbook/2/generics.html
