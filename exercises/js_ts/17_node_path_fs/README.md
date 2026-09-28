# Nível 17: Node.js Core - File System e Arquivos JSON

## Objetivo
Utilizar `node:fs/promises` e `node:path` para manipulação segura e atômica de arquivos.

## Requisitos
1. `lerJsonSeguro<T>(caminho, fallback)`: Lê arquivo do disco ou retorna fallback sem lançar exceção.
2. `salvarJson(caminho, dados)`: Salva objeto como JSON formatado (`JSON.stringify(dados, null, 2)`). Garante diretório pai.

## Documentação oficial:
https://nodejs.org/docs/latest/api/fs.html#fspromisesreadfilepath-options
