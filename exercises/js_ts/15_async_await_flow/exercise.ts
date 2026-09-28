// Nível 15: Fluxo Async/Await e Retries Resilientes

export async function executarEmSerie<T, R>(
    itens: T[],
    tarefaAsync: (item: T) => Promise<R>
): Promise<R[]> {
    // ESCREVA SEU CÓDIGO AQUI
    return [];
}

export async function tentarComRetry<T>(
    tarefaAsync: () => Promise<T>,
    maxTentativas: number
): Promise<T> {
    // ESCREVA SEU CÓDIGO AQUI
    return tarefaAsync();
}
