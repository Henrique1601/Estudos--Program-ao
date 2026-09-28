# Exercício 04: Funções Puras e Manipulação de Sequências

## Objetivo
Entender o conceito de mutabilidade vs imutabilidade e evitar efeitos colaterais acidentais.

## Requisitos
1. `inverter_ordem_palavras(frase)`:
   - Divida a frase em palavras (`.split()`).
   - Inverta a ordem da lista (`[::-1]` ou manual).
   - Junte novamente com `" ".join(...)`.
2. `remover_duplicados(itens)`:
   - Não use `list(set(itens))` porque `set` perde a ordem original!
   - Crie uma nova lista e use um `set` auxiliar para busca rápida (`if x not in vistos:`).
   - A lista original de entrada NÃO pode ser modificada.

## Documentação oficial:
https://docs.python.org/3/tutorial/controlflow.html#defining-functions
