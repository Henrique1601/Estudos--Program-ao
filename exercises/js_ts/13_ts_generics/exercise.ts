// Nível 13: TypeScript - Tipos Genéricos (Generics)

export class Fila<T> {
    private itens: T[] = [];

    enfileirar(item: T): void {
        // ESCREVA SEU CÓDIGO AQUI
    }

    desenfileirar(): T | undefined {
        // ESCREVA SEU CÓDIGO AQUI
        return undefined;
    }

    tamanho(): number {
        return this.itens.length;
    }

    primeiro(): T | undefined {
        return this.itens[0];
    }
}

export function trocarPrimeiroComUltimo<T>(lista: T[]): T[] {
    // ESCREVA SEU CÓDIGO AQUI
    return [...lista];
}
