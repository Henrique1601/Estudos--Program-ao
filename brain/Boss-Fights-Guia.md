---
title: Guia dos Boss Fights (Marcos Práticos de Projeto)
date: 2026-09-28
tags:
  - boss-fights
  - projetos
  - arquitetura
  - marcos
aliases:
  - Boss Fights
  - Projetos Práticos
---

# 👹 Guia dos Boss Fights (Marcos Práticos de Projeto)

Katas isolados treinam a sintaxe e a memória de curto prazo. **Os Boss Fights treinam a arquitetura de software e a visão holística do sistema.**

A cada 5 níveis concluídos, você desbloqueia um Boss Fight. Eles ficam localizados na pasta `exercises/js_ts/boss_fights/`.

---

## Boss 1: Gerenciador de Tarefas em Memória
- **Marco:** Ao concluir o [[Mapa-de-Niveis#Fase 1 Primitivos e Controle de Fluxo Niveis 1 ao 5|Nível 05]].
- **Diretório:** `exercises/js_ts/boss_fights/boss_01_cli_task_manager/`
- **Conceitos avaliados:** Classes, métodos de instância, mutação controlada de arrays, buscas com `.filter()` e `.includes()`, e modelagem com interfaces TypeScript.
- **O que você constrói:** Uma classe `GerenciadorTarefas` que gera IDs automáticos, permite alternar conclusão com segurança e filtra por prioridade e termos parciais.

---

## Boss 2: Analisador de Extrato Financeiro CSV
- **Marco:** Ao concluir o [[Mapa-de-Niveis#Fase 2 Estruturacao de Dados e Tipagem Forte Niveis 6 ao 10|Nível 10]].
- **Diretório:** `exercises/js_ts/boss_fights/boss_02_csv_financial_analyzer/`
- **Conceitos avaliados:** Parsing de texto cru, desestruturação de arrays, conversão numérica rigorosa, agregação com `reduce`, e agrupamento em dicionários.
- **O que você constrói:** A função `analisarExtratoCsv(conteudoCsv)` que recebe uma string com dezenas de transações e gera um objeto consolidado com `totalReceitas`, `totalDespesas`, `saldoFinal`, `maiorDespesaCategoria` e `contagemPorCategoria`.

---

## Boss 3: Crawler Assíncrono com Resiliência
- **Marco:** Ao concluir o [[Mapa-de-Niveis#Fase 3 Colecoes O1 Excecoes e Generics Niveis 11 ao 15|Nível 15]].
- **Diretório:** `exercises/js_ts/boss_fights/boss_03_resilient_api_crawler/`
- **Conceitos avaliados:** `Promise`, `async`/`await`, temporizadores, corrida de promessas com `Promise.race`, laço serial `for...of` e retries automáticos.
- **O que você constrói:** A função `rastrearComResiliencia()` que faz requisições protegendo o sistema contra falhas temporárias e lentidões infinitas, separando os resultados finais em lotes de `sucessos` e `falhas`.

---

## Boss 4: Mini Banco Chave-Valor com LRU e Eventos (Chefão Final)
- **Marco:** Ao concluir o [[Mapa-de-Niveis#Fase 4 Engenharia Avancada e Nodejs Core Niveis 16 ao 20|Nível 20]].
- **Diretório:** `exercises/js_ts/boss_fights/boss_04_in_memory_kv_store/`
- **Conceitos avaliados:** `Map` em O(1), ordenação LRU, herança de `EventEmitter`, generics `<V>`, e I/O atômico com `node:fs/promises`.
- **O que você constrói:** O motor `BancoChaveValor<V>` que mantém um cache rápido em memória que descarta itens antigos automaticamente quando a capacidade atinge o limite, avisa o sistema disparando eventos e permite fazer dump e restore completo do disco em formato JSON.

---

## Como executar os testes dos Chefões

No terminal:
```bash
python main.py boss
```
O Code Sensei testará os 4 chefões na ordem e mostrará qual está vivo e qual já foi derrotado!

---

## 🔗 Navegação
- Voltar para o [[Mapa-de-Niveis]].
- Entenda a arquitetura em [[Arquitetura-Code-Sensei]].
- Voltar ao início: [[INDEX]].
