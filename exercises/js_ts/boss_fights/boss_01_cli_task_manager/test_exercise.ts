import test from "node:test";
import assert from "node:assert";
import { GerenciadorTarefas } from "./exercise.ts";

test("GerenciadorTarefas adiciona e incrementa IDs", () => {
    const app = new GerenciadorTarefas();
    const t1 = app.adicionar("Estudar JS", "alta");
    const t2 = app.adicionar("Tomar café", "baixa");

    assert.strictEqual(t1.id, 1);
    assert.strictEqual(t2.id, 2);
    assert.strictEqual(t1.concluida, false);
});

test("GerenciadorTarefas alterna conclusao", () => {
    const app = new GerenciadorTarefas();
    const t1 = app.adicionar("Dormir cedo");
    assert.strictEqual(app.alternarConclusao(t1.id), true);
    assert.strictEqual(app.listar()[0].concluida, true);
    assert.strictEqual(app.alternarConclusao(999), false);
});

test("GerenciadorTarefas filtra por pendentes e prioridade", () => {
    const app = new GerenciadorTarefas();
    const t1 = app.adicionar("Tarefa 1", "alta");
    const t2 = app.adicionar("Tarefa 2", "baixa");
    const t3 = app.adicionar("Tarefa 3", "alta");

    app.alternarConclusao(t1.id); // Concluída

    const pendentesAltas = app.listar({ apenasPendentes: true, prioridade: "alta" });
    assert.strictEqual(pendentesAltas.length, 1);
    assert.strictEqual(pendentesAltas[0].id, t3.id);
});

test("GerenciadorTarefas busca por termo sem case sensitivity", () => {
    const app = new GerenciadorTarefas();
    app.adicionar("Aprender TypeScript");
    app.adicionar("Comprar maçã");

    const encontrados = app.buscarPorTermo("type");
    assert.strictEqual(encontrados.length, 1);
    assert.strictEqual(encontrados[0].titulo, "Aprender TypeScript");
});
