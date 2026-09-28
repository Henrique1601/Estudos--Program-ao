// Boss Fight 4 (Chefão Final - Marco Nível 20): Mini Banco Chave-Valor com LRU e Eventos
// Une: Classes, Generics, Cache LRU O(1), EventEmitter e Persistência File System.

import { EventEmitter } from "node:events";
import fs from "node:fs/promises";
import path from "node:path";

export class BancoChaveValor<V> extends EventEmitter {
    private cache = new Map<string, V>();

    constructor(
        private capacidadeCache: number,
        private caminhoArquivoPersistencia?: string
    ) {
        super();
        if (capacidadeCache <= 0) throw new RangeError("Capacidade deve ser > 0");
    }

    definir(chave: string, valor: V): void {
        // ESCREVA SEU CÓDIGO AQUI
        // 1. Atualizar cache LRU
        // 2. Descartar mais antigo se estourar capacidade (emitir evento 'despejo')
        // 3. Emitir evento 'gravado'
    }

    obter(chave: string): V | undefined {
        // ESCREVA SEU CÓDIGO AQUI
        // Retornar valor e atualizar ordem LRU
        return undefined;
    }

    async salvarEmDisco(): Promise<void> {
        // ESCREVA SEU CÓDIGO AQUI
        // Salvar todos os itens do cache no arquivo JSON formatado
    }

    async carregarDoDisco(): Promise<void> {
        // ESCREVA SEU CÓDIGO AQUI
        // Carregar itens do arquivo JSON para o cache LRU
    }

    tamanho(): number {
        return this.cache.size;
    }
}
