# Nível 15: Fluxo Async/Await e Retries Resilientes

## Objetivo
Dominar a diferença entre execução sequencial e paralela e implementar resiliência com retentativas automáticas.

## Requisitos
1. `executarEmSerie<T, R>(itens, tarefaAsync)`: Executa tarefas assíncronas uma a uma em ordem. Proibido usar Promise.all ou forEach.
2. `tentarComRetry<T>(tarefaAsync, maxTentativas)`: Tenta executar até `maxTentativas` em caso de erro. Lança a última exceção capturada.

## Documentação oficial:
https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Statements/async_function
