// Nível 08: TypeScript - Unions Discriminadas e Type Narrowing

export type Forma =
    | { tipo: "circulo"; raio: number }
    | { tipo: "retangulo"; largura: number; altura: number }
    | { tipo: "quadrado"; lado: number };

export function calcularArea(forma: Forma): number {
    // ESCREVA SEU CÓDIGO AQUI
    return 0;
}

export type RespostaAPI<T> =
    | { status: "sucesso"; dados: T }
    | { status: "erro"; mensagem: string };

export function extrairDados<T>(resposta: RespostaAPI<T>, fallback: T): T {
    // ESCREVA SEU CÓDIGO AQUI
    return fallback;
}
