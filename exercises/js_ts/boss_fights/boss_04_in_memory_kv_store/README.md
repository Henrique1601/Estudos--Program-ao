# 👹 Boss Fight 4: Mini Banco Chave-Valor com LRU e Eventos (Chefão Final - Nível 20)

## Desafio
Construir uma solução integrada de engenharia de software unindo:
- Generics `<V>`.
- Cache LRU em O(1) com descarte inteligente de chaves menos usadas.
- Emissão de eventos assíncronos via `EventEmitter`.
- Persistência e restauração atômica de arquivos com `node:fs/promises`.

## Requisitos
1. Herde de `EventEmitter`.
2. `definir(chave, valor)`: Insere no cache. Se chave já existe, remove antes para atualizar ordem. Se exceder capacidade, remove a mais antiga e dispara `this.emit("despejo", chaveRemovida)`. Em seguida, dispara `this.emit("gravado", chave)`.
3. `obter(chave)`: Se existir, atualiza ordem de recenticidade e retorna. Senão `undefined`.
4. `salvarEmDisco()`: Converte `[...this.cache.entries()]` em objeto ou array e grava no arquivo JSON com `fs.writeFile`.
5. `carregarDoDisco()`: Lê o arquivo JSON e repopula o cache com `this.definir`.
