---
title: Decodificador de Erros do Terminal & Guia de Debugging
date: 2026-09-29
tags:
  - mental-models
  - debugging
  - v8-runtime
  - nodejs
  - javascript
aliases:
  - Decodificador de Erros
  - Guia de Erros
---

# 🛠️ Decodificador de Erros do Terminal

> [!important] Princípio Fundamental
> Um erro de terminal **não é uma bronca do computador**. É um **relatório científico exato** emitido pelo motor de execução (V8/Node.js ou CPython) avisando o exato momento em que uma premissa sua colidiu com a realidade da memória física da máquina.

Aprender a ler stack traces linha por linha sem entrar em pânico e sem colar no chat de IA é o divisor de águas entre um digitador de código e um engenheiro de software real.

---

## 🧭 Como Ler um Stack Trace (Anatomia do Erro)

Quando o Node.js cospe um erro no terminal, ele fornece 3 informações essenciais:

```text
TypeError: Cannot read properties of undefined (reading 'map')   <-- [1] TIPO E CAUSA
    at processarItens (c:\projeto\servico.js:42:15)            <-- [2] ARQUIVO E LINHA EXATA
    at ModuleJob.run (node:internal/modules/esm/module_job:234)  <-- [3] CÓDIGO INTERNO DO NODE
```

1. **Tipo & Mensagem:** Diz qual regra da máquina foi violada (`TypeError`, `ReferenceError`, `SyntaxError`, `RangeError`).
2. **Ponto de Origem no seu Código:** A primeira linha do rastreio que aponta para um arquivo **seu** (ignore as linhas internas que começam com `node:internal/...`).
3. **Pilha de Execução (Call Stack):** O caminho inverso das funções que estavam abertas na memória quando o desastre aconteceu.

---

## 🔬 Catálogo dos Erros Mais Frequentes no JavaScript/Node

### 1. `TypeError: Cannot read properties of undefined / null (reading 'x')`
- **O que a máquina tentou fazer:** Você tentou acessar uma propriedade ou método (ex: `usuario.nome` ou `itens.map()`), mas a variável à esquerda do ponto vale `undefined` ou `null`.
- **Causas Frequentes:**
  1. Uma requisição assíncrona não terminou e o código rodou antes da Promise resolver (faltou `await`).
  2. Um método de busca (`arr.find(...)`) não encontrou o item e retornou `undefined`.
  3. O backend enviou uma estrutura de dados com uma chave ligeiramente diferente.
- **Como Inspecionar Ativamente:**
  ```javascript
  // Coloque o log na linha imediatamente anterior
  console.log("DEBUG estado de itens:", itens, typeof itens);
  const nomes = itens.map(i => i.nome);
  ```

---

### 2. `TypeError: X is not a function`
- **O que a máquina tentou fazer:** Você colocou parênteses `()` ao lado de um identificador esperando executá-lo, mas o valor contido naquela variável é uma string, um objeto, um número ou `undefined`.
- **Causas Frequentes:**
  1. Importação incorreta: fez `import { somar } from './utils'` quando o arquivo exportava `export default somar` (ou vice-versa).
  2. Erro de digitação no nome do método nativo (ex: `arr.pushBack()` em vez de `arr.push()`).
  3. A variável que guardava a função foi sobrescrita por outro valor ao longo da execução.
- **Checklist:**
  - Imprima `console.log(typeof minhaFuncao)`. Se sair `'undefined'`, a importação falhou.

---

### 3. `ReferenceError: X is not defined`
- **O que a máquina tentou fazer:** O interpretador tentou buscar uma variável no escopo atual e subiu na cadeia de escopos até o escopo global sem encontrar nenhuma declaração com esse nome.
- **Causas Frequentes:**
  1. Erro de digitação no nome (JavaScript diferencia maiúsculas de minúsculas com rigor: `Total` ≠ `total`).
  2. A variável foi declarada dentro de um bloco `if` ou `for` com `let` ou `const` e você tentou acessá-la do lado de fora (escopo de bloco).
  3. Faltou importar a biblioteca ou variável de outro arquivo.

---

### 4. `RangeError: Maximum call stack size exceeded`
- **O que a máquina tentou fazer:** A pilha de chamadas (Call Stack) do motor V8 estourou o limite físico permitido de memória (~10.000 chamadas abertas simultaneamente).
- **Causas Frequentes:**
  1. Função recursiva sem **caso base** (a condição `if` que interrompe a auto-chamada).
  2. O argumento passado na recursão não está convergindo para o caso base (ex: chamou `f(n)` em vez de `f(n - 1)`).
  3. Duas funções se chamando mutuamente em ciclo infinito (ping-pong).
- **Consulte também:** [[Metodologia-Pato-Socratico]] para desenhar a árvore de recursão no papel antes de codificar.

---

### 5. `SyntaxError: Unexpected token X`
- **O que a máquina tentou fazer:** O compilador/parser não conseguiu transformar seu arquivo de texto em uma Árvore Sintática Abstrata (AST) porque você quebrou as regras gramaticais da linguagem.
- **Causas Frequentes:**
  1. Parêntese `(`, chave `{` ou colchete `[` aberto e nunca fechado.
  2. Vírgula sobrando ou faltando em declarações de objetos ou listas de parâmetros.
  3. Executar `JSON.parse(resposta)` quando a resposta da API é um HTML de erro `<html>...` e não um JSON válido.
- **Dica de Ouro:** O erro quase sempre está na linha **imediatamente acima** da apontada pelo compilador.

---

### 6. `UnhandledPromiseRejection`
- **O que a máquina tentou fazer:** Uma Promise falhou (foi rejeitada ou lançou uma exceção), mas não havia nenhum bloco `try/catch` (para `async/await`) ou `.catch()` (para Promises encadeadas) escutando a rejeição.
- **Regra do Sensei:** Toda operação de I/O (rede, disco, banco de dados) **vai falhar** em algum momento. Trate com `try/catch`:
  ```javascript
  try {
    const dados = await buscarServidor();
  } catch (erro) {
    console.error("Falha ao buscar servidor:", erro.message);
  }
  ```

---

### 7. `TypeError: Assignment to constant variable`
- **O que a máquina tentou fazer:** Você usou o operador `=` para atribuir um novo endereço de memória a uma variável que foi travada com a palavra-chave `const`.
- **Diferença Crucial:**
  ```javascript
  const lista = [1, 2];
  lista.push(3);       // PERMITIDO! O ponteiro não mudou, apenas o conteúdo interno.
  lista = [1, 2, 3];   // ERRO! Tentativa de reatribuir o ponteiro da constante.
  ```

---

## ⚡ Como Usar as Novas Ferramentas no Terminal

- **Decodificador Interativo:**
  ```bash
  python main.py error
  ```
  Permite colar a linha de erro do terminal ou navegar pelas explicações detalhadas.

- **Decodificador Direto:**
  ```bash
  python main.py error "TypeError: Cannot read properties of undefined (reading 'split')"
  ```

- **Visualizador de Memória e Call Stack:**
  ```bash
  python main.py inspect
  ```
  Veja simulações passo a passo da evolução de variáveis em loops e pilhas de chamada.

- **Exportador Anki:**
  ```bash
  python main.py anki
  ```
  Gera `flashcards/code_sensei_anki.csv` com 20 cartões prontos para você revisar no celular.

---

## 🔗 Links Relacionados
- [[INDEX]]: Hub Central do Cérebro
- [[Metodologia-Pato-Socratico]]: Passo a passo para debugar
- [[Como-Estudar-Sem-IA]]: Treinando modelos mentais sólidos
