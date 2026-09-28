---
title: Mapa Completo dos 20 Níveis e Competências
date: 2026-09-28
tags:
  - curriculo
  - javascript
  - typescript
  - nodejs
  - roadmap
aliases:
  - Mapa de Níveis
  - Trilha JS TS
---

# 🗺️ Mapa Completo dos 20 Níveis e Competências

Esta trilha progressiva foi desenhada para construir as fundações da programação moderna em **JavaScript, TypeScript e Node.js 24**, eliminando lacunas de compreensão conceitual.

---

## 🟢 Fase 1: Primitivos e Controle de Fluxo (Níveis 1 ao 5)

| Nível | Módulo | Competência Central |
| :--- | :--- | :--- |
| **01** | `01_primitives_coercion` | Falsy values (`0`, `""`, `null`, `NaN`), coerção com `+` vs `Number()`. |
| **02** | `02_conditionals_branching` | Guard clauses, lógica booleana composta, ano bissexto. |
| **03** | `03_loops_accumulators` | Acumuladores manuais, simulação de mutação de estado. |
| **04** | `04_array_basics` | Algoritmos de busca min/max na mão (sem `Math.max`) e fatiamento (chunking). |
| **05** | `05_functions_closures` | Escopo léxico, variáveis encapsuladas em closures e memoização. |

> [!important] 👹 Marco da Fase 1: [[Boss-Fights-Guia#Boss 1 Gerenciador de Tarefas em Memória|Boss Fight 1 - Gerenciador de Tarefas]]
> Construir uma classe completa de gerenciamento de tarefas com filtros múltiplos e busca de texto.

---

## 🟡 Fase 2: Estruturação de Dados e Tipagem Forte (Níveis 6 ao 10)

| Nível | Módulo | Competência Central |
| :--- | :--- | :--- |
| **06** | `06_objects_destructuring` | Seleção de chaves (Pick manual) e merge seguro com spread. |
| **07** | `07_ts_basic_interfaces` | Modelagem de domínio e contratos estritos com TypeScript. |
| **08** | `08_ts_unions_narrowing` | Discriminated Unions e type guards sem uso de `any`. |
| **09** | `09_array_methods_map_filter` | Pipelines funcionais de transformação e descarte de dados. |
| **10** | `10_array_methods_reduce` | Histogramas e agrupamento dinâmico (`groupBy`) com acumuladores. |

> [!important] 👹 Marco da Fase 2: [[Boss-Fights-Guia#Boss 2 Analisador de Extrato Financeiro CSV|Boss Fight 2 - Analisador Financeiro CSV]]
> Processar arquivo de transações financeiras em texto puro e calcular métricas analíticas complexas com `reduce`.

---

## 🟠 Fase 3: Coleções O(1), Exceções e Generics (Níveis 11 ao 15)

| Nível | Módulo | Competência Central |
| :--- | :--- | :--- |
| **11** | `11_sets_and_maps` | Unicidade e buscas em tempo O(1) com `Set` e `Map`. |
| **12** | `12_error_handling_custom` | Classes de erro de domínio (`extends Error`) e isolamento de falhas. |
| **13** | `13_ts_generics` | Estrutura de dados Fila (FIFO) reutilizável com TypeScript Generics `<T>`. |
| **14** | `14_async_promises_basics` | Envelopamento de temporizadores e corrida com timeout (`Promise.race`). |
| **15** | `15_async_await_flow` | Execução em série sequencial estrita e retentativas automáticas (retries). |

> [!important] 👹 Marco da Fase 3: [[Boss-Fights-Guia#Boss 3 Crawler Assincrono Resiliente|Boss Fight 3 - Crawler Assíncrono com Resiliência]]
> Pipeline assíncrono que processa endpoints protegendo contra travamentos infinitos com timeout e retry.

---

## 🔴 Fase 4: Engenharia Avançada e Node.js Core (Níveis 16 ao 20)

| Nível | Módulo | Competência Central |
| :--- | :--- | :--- |
| **16** | `16_async_concurrency_limit` | Pool de concorrência limitada (Worker Pool pattern). |
| **17** | `17_node_path_fs` | Persistência assíncrona em arquivos JSON com `node:fs/promises` e `node:path`. |
| **18** | `18_node_events_streams` | Arquitetura orientada a eventos e mensageria local com `EventEmitter`. |
| **19** | `19_mental_trace_real_bugs` | Caça às armadilhas reais do JS (`.sort()` numérico, shallow copy e async forEach). |
| **20** | `20_lru_cache_algorithm` | Implementação completa de Cache LRU (Least Recently Used) em O(1). |

> [!important] 👹 Chefão Final: [[Boss-Fights-Guia#Boss 4 Mini Banco Chave-Valor com LRU e Eventos|Boss Fight 4 - Mini Banco Chave-Valor]]
> Construir um motor de banco de dados chave-valor unindo Cache LRU em memória, `EventEmitter` e persistência atômica em disco.

---

## 🔗 Navegação
- Conheça os mini-projetos práticos em [[Boss-Fights-Guia]].
- Entenda como rodar os testes em [[Arquitetura-Code-Sensei]].
- Voltar ao início: [[INDEX]].
