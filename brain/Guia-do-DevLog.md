---
title: Guia do DevLog Metacognitivo
date: 2026-09-28
tags:
  - devlog
  - metacognicao
  - aprendizado
  - modelo-mental
aliases:
  - Guia do DevLog
  - Diário de Bordo
---

# 📝 Guia do DevLog Metacognitivo

A **Metacognição** é o ato de pensar sobre o seu próprio processo de pensamento. Na programação, ela é o fator que separa quem estuda por 6 meses sem sair do lugar de quem ganha autonomia real em poucas semanas.

---

## O Conceito: "Mental Model Diff" (Diferença de Modelo Mental)

Quando você passa 30 minutos travado em um bug e finalmente descobre a solução, seu impulso natural é comemorar e esquecer o assunto. **Não faça isso.**

Esse momento é o ápice do aprendizado. Um erro demorado significa que a sua **teoria sobre como a linguagem funciona** estava em conflito com a **realidade do runtime**.

> [!tip] A Pergunta Chave
> *"Qual premissa incorreta sobre a linguagem eu assumi como verdadeira antes de descobrir o erro?"*

### Exemplos Reais de Lacunas Mentais:
- **Suposição Falsa:** *"Achei que `array.sort()` ordenava números do menor para o maior por padrão."*
  - **Realidade do JS:** Ele converte números para string e compara a ordem lexicográfica (`[10, 2]` vira `[10, 2]`).
- **Suposição Falsa:** *"Achei que `{ ...objeto }` criava uma cópia independente de todas as propriedades."*
  - **Realidade do JS:** O operador spread só faz cópia rasa (*shallow copy*). Propriedades aninhadas continuam apontando para a mesma referência.
- **Suposição Falsa:** *"Achei que `array.forEach(async () => ...)` esperava todas as promessas terminarem."*
  - **Realidade do JS:** O `forEach` ignora o retorno da Promise e continua imediatamente.

---

## Como Registrar um DevLog

No terminal:
```bash
python main.py log
```
O Code Sensei fará as 6 perguntas do protocolo:
1. **Título do problema.**
2. **Tags** (ex: `javascript, loops, async`).
3. **Sintoma observado.**
4. **Comportamento esperado vs real.**
5. **Modelo mental incorreto** (a premissa falsa).
6. **Regra pessoal de prevenção** (o que você vai checar da próxima vez).

O arquivo será salvo na pasta `devlog/` em Markdown formatado.

Para listar seu histórico a qualquer momento:
```bash
python main.py logs
```

---

## 🔗 Navegação
- Conheça a técnica de depuração em [[Metodologia-Pato-Socratico]].
- Voltar ao início: [[INDEX]].
