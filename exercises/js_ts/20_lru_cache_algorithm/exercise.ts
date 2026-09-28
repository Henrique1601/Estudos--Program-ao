// Nível 20: Algoritmo Avançado - Cache LRU (Least Recently Used)

export class LRUCache<K, V> {
    private cache = new Map<K, V>();

    constructor(private capacidade: number) {
        if (capacidade <= 0) {
            throw new RangeError("Capacidade deve ser maior que zero");
        }
    }

    get(chave: K): V | undefined {
        // ESCREVA SEU CÓDIGO AQUI
        return undefined;
    }

    put(chave: K, valor: V): void {
        // ESCREVA SEU CÓDIGO AQUI
    }

    tamanho(): number {
        return this.cache.size;
    }
}
