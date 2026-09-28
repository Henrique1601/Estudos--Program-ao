# Nível 08: TypeScript - Unions Discriminadas e Type Narrowing

## Objetivo
Garantir segurança estrita em tipos polimórficos sem conversões manuais (`as any`).

## Requisitos
1. `calcularArea(forma: Forma)`: Circulo (PI * r^2 arredondado com 2 casas), Retângulo (largura * altura), Quadrado (lado * lado).
2. `extrairDados<T>(resposta: RespostaAPI<T>, fallback: T)`: Retorna dados se status === "sucesso", senão fallback.

## Documentação oficial:
https://www.typescriptlang.org/docs/handbook/2/narrowing.html
