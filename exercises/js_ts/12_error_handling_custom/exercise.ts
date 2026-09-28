// Nível 12: Tratamento de Erros e Exceções Customizadas

export class ValidacaoError extends Error {
    constructor(public campo: string, mensagem: string) {
        super(mensagem);
        this.name = "ValidacaoError";
    }
}

export function validarUsuario(dados: { nome: string; idade: number }): void {
    // ESCREVA SEU CÓDIGO AQUI
}

export function parseJsonSeguro<T>(texto: string, fallback: T): T {
    // ESCREVA SEU CÓDIGO AQUI
    return fallback;
}
