# 🥋 Code Sensei: Seu Mentor Pessoal de Programação Anti-IA

> **Aprenda a programar de verdade criando modelos mentais sólidos, sem atalhos de inteligência artificial ou ilusão de fluência.**

O **Code Sensei** é uma ferramenta de terminal leve, rápida e offline projetada para quem quer aprender a programar construindo autonomia e disciplina técnica.

---

## 🎯 Por que aprender sem IA?
Estudos mostram que o autocompletion e a geração indiscriminada de código criam a **"ilusão de fluência"**: você lê o código gerado, acha que entendeu, mas seu cérebro não construiu os caminhos neurais para depurar, rastrear variáveis ou sintetizar lógica do zero.

O Code Sensei atua como seu treinador rigoroso:
1. **Zero código mastigado**: ele nunca cospe a solução pronta.
2. **Depuração ativa**: força você a inspecionar estado real com prints/debugger.
3. **Metacognição**: registra o que você presumiu errado vs como o runtime realmente funciona.

---

## 🥋 Trilhas Disponíveis

O Code Sensei possui suporte nativo a testes rápidos em duas trilhas completas:
1. **JavaScript / TypeScript / Node.js** (Padrão - usa Node.js 24 com `node --test` e type-stripping nativo de TypeScript, sem necessidade de compilação ou dependências externas).
2. **Python** (Usa runner nativo com `unittest`).

Você pode alternar entre as trilhas a qualquer momento pelo menu interativo (`Opção 7`) ou via linha de comando:
```bash
python main.py --track js_ts
python main.py --track python
```

---

## 🚀 Como Usar

### 1. Menu Interativo Principal
Basta rodar o comando abaixo no terminal da pasta do projeto:
```bash
python main.py
```
Isso abrirá um menu interativo com todas as opções numeradas.

---

### 2. Comandos Diretos no Terminal

#### 🦆 Pato Socrático (`python main.py duck`)
Travou em um bug? Em vez de jogar o erro no ChatGPT, inicie uma sessão com o Pato Socrático. Ele conduzirá você por 5 etapas de raciocínio investigativo:
1. Delimitar a discrepância (Entrada vs Saída esperada vs Real).
2. Isolar a linha exata onde o estado divergiu.
3. Inspecionar variáveis e tipos reais antes da linha.
4. Traduzir o objetivo em português claro.
5. Formular uma hipótese e um teste de 1 linha.
*(Ao final, você pode salvar a análise diretamente no seu diário).*

#### 👁️ Modo Watch dos Exercícios (`python main.py watch`)
Monitora os exercícios em tempo real:
- Deixe o terminal aberto com `python main.py watch`.
- Abra o arquivo indicado (ex: `exercises/js_ts/01_js_primitives_coercion/exercise.ts`) no seu editor favorito (com sugestões de IA desligadas!).
- Escreva a solução e salve o arquivo (`Ctrl+S`).
- O Sensei retesta instantaneamente e avisa se passou ou mostra onde falhou, junto com a documentação oficial.

#### 🥋 Verificador de Katas (`python main.py train`)
Executa uma passada nos exercícios para verificar o status atual e o próximo exercício bloqueado.

#### 📝 Diário Metacognitivo DevLog (`python main.py log` e `python main.py logs`)
Quando resolver um bug difícil, registre seu aprendizado:
- `python main.py log`: formulário guiado para registrar a falsa premissa vs a causa real.
- `python main.py logs`: lista todo o seu histórico de aprendizados salvos na pasta `devlog/`.

#### 📊 Estatísticas (`python main.py stats`)
Mostra seu progresso geral de katas concluídos e total de lições registradas.

---

## 📂 Estrutura de Exercícios

### Trilha JavaScript / TypeScript / Node.js (`exercises/js_ts/`)
- `01_primitives_coercion`: Valores falsy, coerção de tipos e formatação de moeda.
- `02_conditionals_branching`: Classificação de notas, anos bissextos e cálculo de descontos.
- `03_loops_accumulators`: Acumuladores de pares, contagem de caracteres e fatorial manual.
- `04_array_basics`: Busca de extremos (min/max) e divisão de arrays em fatias (chunking).
- `05_functions_closures`: Estado encapsulado com closures e memoização funcional.
- `06_objects_destructuring`: Seleção de chaves (Pick) e merge seguro com spread.
- `07_ts_basic_interfaces`: Modelagem de e-commerce e recibos com interfaces estritas.
- `08_ts_unions_narrowing`: Unions discriminadas e inferência de tipos polimórficos.
- `09_array_methods_map_filter`: Transformações funcionais e descarte de falsy values.
- `10_array_methods_reduce`: Agrupamento de dados e histogramas com reduce.
- `11_sets_and_maps`: Interseção O(1) com Set e tabelas de busca com Map.
- `12_error_handling_custom`: Classes de erro customizadas e parsing seguro de JSON.
- `13_ts_generics`: Estrutura de dados Fila (FIFO) e tipos genéricos reutilizáveis.
- `14_async_promises_basics`: Envelopamento de temporizadores e Promise.race com timeout.
- `15_async_await_flow`: Execução assíncrona sequencial e retentativas automáticas (retries).
- `16_async_concurrency_limit`: Controle de concorrência com pool de workers assíncronos.
- `17_node_path_fs`: Manipulação atômica de JSON com `node:fs/promises` e `node:path`.
- `18_node_events_streams`: Arquitetura orientada a eventos com `EventEmitter`.
- `19_mental_trace_real_bugs`: Caça aos 3 bugs clássicos (`.sort()`, shallow copy, async forEach).
- `20_lru_cache_algorithm`: Implementação de Cache LRU (Least Recently Used) com Map em O(1).

### Trilha Python (`exercises/python/`)
- `01_variables_types`: Tipos, tuplas e conversão numérica.
- `02_conditionals_logic`: Ano bissexto, classificação geométrica e guard clauses.
- `03_loops_accumulators`: Laços manuais e acumuladores.
- `04_functions_pure`: Funções puras e remoção de duplicados preservando ordem.
- `05_data_structures_maps`: Dicionários e contagem de frequência.
- `06_mental_trace_bug`: Armadilhas de runtime (default mutável `[]` e off-by-one).

---

## 📂 Estrutura de Arquivos

```text
charming-shannon/
├── exercises/                     # Exercícios práticos progressivos
│   ├── 01_variables_types/       # Variáveis, tipos e operações
│   ├── 02_conditionals_logic/    # Lógica booleana e guard clauses
│   ├── 03_loops_accumulators/    # Laços e acumuladores manuais
│   ├── 04_functions_pure/        # Funções puras e mutabilidade
│   ├── 05_data_structures_maps/  # Dicionários e agrupamentos
│   └── 06_mental_trace_bug/      # Caça a bugs reais (default mutável, off-by-one)
├── sensei/                        # Motor do mentor
│   ├── cli.py                    # Menu e comandos CLI
│   ├── socratic.py               # Sessão do Pato Socrático
│   ├── runner.py                 # Validador de testes e observador de arquivos
│   ├── journal.py                # Diário DevLog metacognitivo
│   └── colors.py                 # Formatação de terminal
├── devlog/                        # Seus aprendizados salvos em Markdown
└── main.py                        # Ponto de entrada do sistema
```

---

## 💡 Dica de Ouro para o Aprendizado
No seu editor de código (VS Code, Cursor, etc.):
- **Desative extensões de Copilot/autocompletion por IA**.
- Use o terminal integrado lado a lado com seu código.
- Consulte a documentação oficial indicada nos links de cada exercício.
