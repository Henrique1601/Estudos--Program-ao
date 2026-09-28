# Nível 12: Tratamento de Erros e Exceções Customizadas

## Objetivo
Construir hierarquia de erros com classes e isolar falhas de parsing/runtime de forma previsível.

## Requisitos
1. Criar classe `ValidacaoError extends Error` com propriedade `campo: string`.
2. `validarUsuario(dados)`: Lança `ValidacaoError` se nome tiver menos de 3 letras ou idade < 0.
3. `parseJsonSeguro<T>(texto: string, fallback: T)`: Retorna JSON.parse ou fallback caso lance SyntaxError.

## Documentação oficial:
https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Global_Objects/Error
