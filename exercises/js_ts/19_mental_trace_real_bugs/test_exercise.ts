import test from "node:test";
import assert from "node:assert";
import { ordenarNumeros, atualizarCidadeSemMutarOriginal, carregarTodos } from "./exercise.ts";

test("ordenarNumeros ordena numericamente", () => {
    assert.deepStrictEqual(ordenarNumeros([10, 2, 5, 1, 20]), [1, 2, 5, 10, 20]);
});

test("atualizarCidadeSemMutarOriginal preserva original", () => {
    const original = { nome: "Ana", endereco: { cidade: "SP", pais: "BR" } };
    const atualizado = atualizarCidadeSemMutarOriginal(original, "RJ");
    assert.strictEqual(atualizado.endereco.cidade, "RJ");
    assert.strictEqual(original.endereco.cidade, "SP");
});

test("carregarTodos aguarda resolucoes", async () => {
    const busca = async (id: number) => `item_${id}`;
    const res = await carregarTodos([1, 2], busca);
    assert.deepStrictEqual(res, ["item_1", "item_2"]);
});
