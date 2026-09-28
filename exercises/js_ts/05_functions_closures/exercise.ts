// Nível 05: Funções, Escopo e Closures

export function criarContador(inicial = 0) {
    // ESCREVA SEU CÓDIGO AQUI
    return {
        incrementar: () => 0,
        obter: () => 0,
        resetar: () => {},
    };
}

export function memoizar<T, R>(fn: (arg: T) => R): (arg: T) => R {
    // ESCREVA SEU CÓDIGO AQUI
    return fn;
}
