// Nível 17: Node.js Core - File System e Arquivos JSON
import fs from "node:fs/promises";
import path from "node:path";

export async function lerJsonSeguro<T>(caminho: string, fallback: T): Promise<T> {
    // ESCREVA SEU CÓDIGO AQUI
    return fallback;
}

export async function salvarJson(caminho: string, dados: unknown): Promise<void> {
    // ESCREVA SEU CÓDIGO AQUI
}
