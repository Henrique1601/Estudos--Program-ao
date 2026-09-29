# 🥋 Code Sensei: Seu Mentor Pessoal de Programação Anti-IA

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node.js](https://img.shields.io/badge/Node.js-24%2B-green.svg)](https://nodejs.org/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://python.org/)
[![Obsidian Brain](https://img.shields.io/badge/Obsidian-Vault-purple.svg)](brain/INDEX.md)

> **Aprenda a programar de verdade criando modelos mentais sólidos, sem atalhos de inteligência artificial ou ilusão de fluência.**

O **Code Sensei** é um ecossistema offline de terminal projetado para quem quer construir autonomia técnica real através de **prática deliberada**, **TDD progressivo** e **metacognição**.

---

## 🎯 Por que aprender sem IA?
Estudos empíricos em Educação em Computação mostram que o autocompletion indiscriminado cria a chamada **"ilusão de fluência"**: você lê o código gerado pela IA e acha que aprendeu, mas seu cérebro não constrói o modelo mental (*Notional Machine*) necessário para sintetizar ou depurar lógica a partir do zero.

O Code Sensei atua como seu treinador pessoal:
1. **Zero código mastigado**: ele nunca cospe a solução pronta.
2. **Anti-Cheat Linter**: bloqueia o uso de métodos mágicos quando o objetivo é treinar lógica manual.
3. **Depuração Socrática**: conduz você com perguntas investigativas baseadas em fatos.
4. **Compilador Mental (Blind Trace)**: treina a simulação mental do runtime antes de executar.
5. **Git Auto-Commit**: salva e commita cada nível vencido automaticamente no seu histórico.
6. **Segundo Cérebro Obsidian**: base de conhecimento completa em `brain/` com Wikilinks e mapas de competência.

---

## 🚀 Como Usar

### 1. Menu Interativo Principal
Execute no terminal:
```bash
python main.py
```
Isso abrirá o menu interativo com todas as ferramentas disponíveis.

---

### 2. Comandos Diretos no Terminal

| Comando | O que faz |
| :--- | :--- |
| `python main.py watch` | **Modo Observador Ativo**: monitora o código, retesta ao salvar e faz Git Auto-Commit ao passar. |
| `python main.py tree` | **Skill Tree RPG**: árvore de habilidades em 4 ramos, graduação por faixas (Branca à Preta) e streaks offline. |
| `python main.py stats` | **Estatísticas & Perfil RPG**: mostra nível, XP acumulado, dias seguidos e progresso dos katas/chefões. |
| `python main.py hunt` | **Caça-Bugs**: treino de Code Review Reverso (encontrar a linha do bug lendo o código). |
| `python main.py error [msg]` | **Decodificador de Erros**: traduz mensagens crípticas do runtime em explicações humanas e checklists de debug. |
| `python main.py inspect` | **Visualizador de Memória**: simula no terminal a evolução de variáveis em loops, recursão e ponteiros. |
| `python main.py anki` | **Exportador Anki**: gera baralho `flashcards/code_sensei_anki.csv` com 20 modelos mentais fundamentais. |
| `python main.py hint [ex] [1..3]` | **Dicas Progressivas**: Nível 1 (Pergunta), Nível 2 (Pseudocódigo), Nível 3 (Doc da API). |
| `python main.py trace` | **Blind Trace**: flashcards mentais no terminal para prever o output antes de rodar. |
| `python main.py boss` | **Boss Fights**: avalia e executa os mini-projetos práticos de marco. |
| `python main.py duck` | **Pato Socrático**: sessão de 5 etapas para debugar problemas difíceis. |
| `python main.py train` | **Katas Runner**: executa a suíte e para no primeiro exercício pendente. |
| `python main.py log` | **Novo DevLog**: formulário guiado para registrar a falsa premissa vs a causa real do bug. |
| `python main.py logs` | **Ver DevLogs**: lista seus aprendizados e modelos mentais salvos. |
| `python main.py --track js_ts` | Ativa a trilha **JavaScript / TypeScript / Node.js**. |
| `python main.py --track python` | Ativa a trilha **Python**. |



---

## 📂 Suíte de 20 Katas Progressivos (`exercises/js_ts/`)

1. `01_primitives_coercion`: Valores falsy, coerção de tipos e formatação de moeda BRL.
2. `02_conditionals_branching`: Classificação de notas, anos bissextos e cálculo de descontos.
3. `03_loops_accumulators`: Acumuladores de pares, contagem de caracteres e fatorial manual.
4. `04_array_basics`: Busca de extremos (min/max sem Math.max) e fatiamento em lotes (chunking).
5. `05_functions_closures`: Estado encapsulado com closures e memoização funcional.
6. `06_objects_destructuring`: Projeção de chaves (Pick) e merge seguro com spread.
7. `07_ts_basic_interfaces`: Modelagem de e-commerce e recibos com interfaces estritas.
8. `08_ts_unions_narrowing`: Unions discriminadas e inferência de tipos polimórficos.
9. `09_array_methods_map_filter`: Transformações funcionais puras e descarte de falsy values.
10. `10_array_methods_reduce`: Agrupamento de dados e histogramas com reduce.
11. `11_sets_and_maps`: Interseção O(1) com Set e tabelas de busca com Map.
12. `12_error_handling_custom`: Classes de erro customizadas e parsing seguro de JSON.
13. `13_ts_generics`: Estrutura de dados Fila (FIFO) e tipos genéricos reutilizáveis.
14. `14_async_promises_basics`: Envelopamento de temporizadores e Promise.race com timeout.
15. `15_async_await_flow`: Execução assíncrona sequencial e retentativas automáticas (retries).
16. `16_async_concurrency_limit`: Controle de concorrência com pool de workers assíncronos.
17. `17_node_path_fs`: Manipulação atômica de JSON com `node:fs/promises` e `node:path`.
18. `18_node_events_streams`: Arquitetura orientada a eventos com `EventEmitter`.
19. `19_mental_trace_real_bugs`: Caça aos 3 bugs clássicos (`.sort()` numérico, shallow copy, async forEach).
20. `20_lru_cache_algorithm`: Implementação de Cache LRU (Least Recently Used) com Map em O(1).

---

## 👹 Boss Fights (Marcos Práticos de Projeto)

A cada 5 níveis, você encara um mini-projeto de arquitetura:
- **Boss 1 (Nível 5)**: `boss_01_cli_task_manager` — Gerenciador de Tarefas em Memória com buscas e filtros.
- **Boss 2 (Nível 10)**: `boss_02_csv_financial_analyzer` — Analisador analítico de extratos bancários em CSV.
- **Boss 3 (Nível 15)**: `boss_03_resilient_api_crawler` — Crawler serial assíncrono com retries e timeouts.
- **Boss 4 (Nível 20 - Chefão Final)**: `boss_04_in_memory_kv_store` — Mini Banco Chave-Valor em disco com Cache LRU e Eventos.

---

## 🧠 Segundo Cérebro Obsidian (`brain/`)

O repositório inclui um cofre Obsidian pronto para uso:
- [INDEX.md](brain/INDEX.md): Ponto de entrada central (Map of Content).
- [Sistema-de-Faixas-e-Skill-Tree.md](brain/Sistema-de-Faixas-e-Skill-Tree.md): Árvore de habilidades RPG e streaks Git.
- [Como-Estudar-Sem-IA.md](brain/Como-Estudar-Sem-IA.md): A neurociência do aprendizado e a ilusão de fluência.
- [Mapa-de-Niveis.md](brain/Mapa-de-Niveis.md): Guia detalhado de todos os 20 níveis e competências.
- [Boss-Fights-Guia.md](brain/Boss-Fights-Guia.md): Requisitos arquiteturais dos 4 projetos práticos.
- [Metodologia-Pato-Socratico.md](brain/Metodologia-Pato-Socratico.md): O algoritmo de 5 etapas para debugar.
- [Arquitetura-Code-Sensei.md](brain/Arquitetura-Code-Sensei.md): Engenharia interna do runner e linter.
- [Guia-do-DevLog.md](brain/Guia-do-DevLog.md): Como capturar discrepâncias de modelos mentais.
- [Decodificador-de-Erros.md](brain/Decodificador-de-Erros.md): Guia de anatomia de erros do runtime e checklist de debug.

---

## 🤖 Agente Especialista (`code-sensei-mentor`)

O projeto inclui a especificação do subagente em [agents/code-sensei-mentor.md](agents/code-sensei-mentor.md), focado exclusivamente em:
- Conduzir tutorias socráticas.
- Criar novos desafios personalizados.
- Diagnosticar modelos mentais defeituosos sem nunca entregar código pronto.

---

## 📄 Licença
Distribuído sob a licença **MIT**. Veja [LICENSE](LICENSE) para mais detalhes.
