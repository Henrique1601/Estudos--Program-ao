# Nível 02: Condicionais e Ramificações

## Objetivo
Estruturar tomadas de decisão lógicas com guard clauses, evitando múltiplos níveis de indentação.

## Requisitos
1. `classificarNota(nota: number)`:
   - Se nota < 0 ou nota > 100: lance RangeError("Nota fora do intervalo").
   - >= 90: "A"
   - >= 80: "B"
   - >= 70: "C"
   - >= 60: "D"
   - abaixo de 60: "F"
2. `ehAnoBissexto(ano: number)`:
   - Divisível por 4 e (não divisível por 100 ou divisível por 400).
3. `calcularDesconto(valor: number, cupom?: string)`:
   - Se cupom === "DESC10": 10% de desconto.
   - Se cupom === "DESC20": 20% de desconto.
   - Sem cupom ou cupom desconhecido: 0% de desconto. Retorna o valor final arredondado para 2 casas.

## Documentação oficial:
https://developer.mozilla.org/pt-BR/docs/Learn/JavaScript/Building_blocks/conditionals
