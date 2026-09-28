// Nível 06: Objetos e Desestruturação

export function selecionarPropriedades<T extends object, K extends keyof T>(
    obj: T,
    chaves: K[]
): Pick<T, K> {
    // ESCREVA SEU CÓDIGO AQUI
    return {} as Pick<T, K>;
}

export function mesclarConfiguracoes<T extends object, U extends object>(
    padrao: T,
    sobrescrita: U
): T & U {
    // ESCREVA SEU CÓDIGO AQUI
    return { ...padrao, ...sobrescrita };
}
