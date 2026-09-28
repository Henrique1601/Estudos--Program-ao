// Nível 14: Promises e Temporizadores Nativos

export function esperar(ms: number): Promise<void> {
    // ESCREVA SEU CÓDIGO AQUI
    return Promise.resolve();
}

export function promessaComTimeout<T>(promessa: Promise<T>, timeoutMs: number): Promise<T> {
    // ESCREVA SEU CÓDIGO AQUI (Dica: Promise.race)
    return promessa;
}
