# Nível 01: Primitivos e Coerção de Tipos

## Objetivo
Dominar a diferença entre valores falsy/truthy no JavaScript e manipular conversões explícitas com segurança sem recorrer a `any`.

## Requisitos
1. `ehFalsy(valor)`: Retorna true se for false, 0, -0, 0n, "", null, undefined ou NaN.
2. `somarSeguro(a, b)`: Rejeita null e undefined com TypeError. Converte para Number e rejeita NaN com TypeError.
3. `formatarMoeda(centavos)`: Formata centavos em string BRL: `R$ 15,50`.

## Documentação oficial:
https://developer.mozilla.org/pt-BR/docs/Glossary/Type_coercion
