# Nível 16: Concorrência Assíncrona Controlada (Worker Pool)

## Objetivo
Evitar sobrecarregar APIs ou recursos do sistema executando no máximo `concorrenciaMaxima` tarefas em paralelo.

## Requisitos
1. `executarComLimite<T, R>(itens: T[], limite: number, tarefa: (item: T) => Promise<R>): Promise<R[]>`:
   - Se houver 10 itens e limite 2: roda no máximo 2 simultâneos por vez.
   - Retorna os resultados na ordem original dos itens de entrada.

## Documentação oficial:
https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Promise/all
