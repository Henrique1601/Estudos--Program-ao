# Nível 14: Promises e Temporizadores Nativos

## Objetivo
Compreender como envelopar operações assíncronas baseadas em callbacks em Promises nativas.

## Requisitos
1. `esperar(ms: number)`: Resolve após `ms` milissegundos.
2. `promessaComTimeout<T>(promessa: Promise<T>, timeoutMs: number)`: Se a promessa demorar mais que `timeoutMs`, rejeita com `new Error("Tempo limite excedido")`. Use `Promise.race`.

## Documentação oficial:
https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Promise/race
