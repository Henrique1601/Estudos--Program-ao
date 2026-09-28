// Boss Fight 1 (Marco Nível 5): Gerenciador de Tarefas em Memória
// Requisitos reais de arquitetura sem auxílio de bibliotecas externas.

export interface Tarefa {
    id: number;
    titulo: string;
    concluida: boolean;
    prioridade: "baixa" | "media" | "alta";
}

export class GerenciadorTarefas {
    private tarefas: Tarefa[] = [];
    private proximoId = 1;

    adicionar(titulo: string, prioridade: "baixa" | "media" | "alta" = "media"): Tarefa {
        // ESCREVA SEU CÓDIGO AQUI
        const nova: Tarefa = { id: this.proximoId++, titulo, concluida: false, prioridade };
        this.tarefas.push(nova);
        return nova;
    }

    alternarConclusao(id: number): boolean {
        // ESCREVA SEU CÓDIGO AQUI
        return false;
    }

    listar(filtro?: { apenasPendentes?: boolean; prioridade?: "baixa" | "media" | "alta" }): Tarefa[] {
        // ESCREVA SEU CÓDIGO AQUI
        return [];
    }

    buscarPorTermo(termo: string): Tarefa[] {
        // ESCREVA SEU CÓDIGO AQUI
        return [];
    }
}
