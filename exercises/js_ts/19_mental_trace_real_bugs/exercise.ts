// Nível 19: Bug Hunting Real (Sort, Shallow Copy, Async forEach)

export function ordenarNumeros(numeros: number[]): number[] {
    // CORRIJA O BUG:
    return [...numeros].sort();
}

export interface PerfilUsuario {
    nome: string;
    endereco: { cidade: string; pais: string };
}

export function atualizarCidadeSemMutarOriginal(
    usuario: PerfilUsuario,
    novaCidade: string
): PerfilUsuario {
    // CORRIJA O BUG:
    const copia = { ...usuario };
    copia.endereco.cidade = novaCidade;
    return copia;
}

export async function carregarTodos(
    ids: number[],
    buscadorAsync: (id: number) => Promise<string>
): Promise<string[]> {
    const resultados: string[] = [];
    // CORRIJA O BUG:
    ids.forEach(async (id) => {
        const item = await buscadorAsync(id);
        resultados.push(item);
    });
    return resultados;
}
