# 👹 Boss Fight 3: Crawler Assíncrono com Resiliência (Marco Nível 15)

## Desafio
Construir um pipeline assíncrono que processa requisições em série, protege contra travamentos infinitos com timeouts estritos (`Promise.race`) e retenta chamadas com falha temporária.

## Requisitos
1. Para cada item da lista (em série, com `for...of`):
2. Envolva a execução em um mecanismo de timeout: se `requisicao()` demorar mais que `timeoutMs`, rejeite com erro.
3. Se falhar, execute até `maxRetentativas` tentativas.
4. Se obtiver sucesso, adicione em `sucessos: { id, dados }`.
5. Se todas as tentativas falharem ou der timeout, adicione em `falhas: { id, erro }` sem interromper os próximos itens.
