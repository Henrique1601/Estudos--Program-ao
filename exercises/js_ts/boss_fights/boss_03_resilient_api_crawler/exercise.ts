// Boss Fight 3 (Marco Nível 15): Crawler Assíncrono com Resiliência
// Promises, Timeouts com Promise.race, Retentativas e Concorrência Serial.

export interface RespostaCrawler<T> {
    sucessos: { id: string; dados: T }[];
    falhas: { id: string; erro: string }[];
}

/**
 * Executa uma requisição assíncrona aplicando:
 * 1. Timeout máximo de 'timeoutMs'.
 * 2. Até 'maxRetentativas' tentativas em caso de erro.
 * Executa para cada item da lista em série para evitar throttling.
 */
export async function rastrearComResiliencia<T>(
    itens: { id: string; requisicao: () => Promise<T> }[],
    timeoutMs: number,
    maxRetentativas: number
): Promise<RespostaCrawler<T>> {
    // ESCREVA SEU CÓDIGO AQUI
    return { sucessos: [], falhas: [] };
}
