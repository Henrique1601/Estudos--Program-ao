// Nível 18: Node.js Core - EventEmitter e Pub/Sub
import { EventEmitter } from "node:events";

export class CentralAlertas extends EventEmitter {
    private total = 0;

    emitirAlerta(nivel: "info" | "aviso" | "critico", mensagem: string): void {
        // ESCREVA SEU CÓDIGO AQUI
    }

    obterTotalDisparos(): number {
        return this.total;
    }
}
