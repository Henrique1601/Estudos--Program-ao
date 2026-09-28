import test from "node:test";
import assert from "node:assert";
import { intersecao, criarTabelaPrecos } from "./exercise.ts";

test("intersecao acha elementos em comum sem repeticao", () => {
    const a = [1, 2, 2, 3, 4];
    const b = [2, 4, 4, 6];
    assert.deepStrictEqual(intersecao(a, b), [2, 4]);
});

test("criarTabelaPrecos retorna Map funcional", () => {
    const tabela = criarTabelaPrecos([["cafe", 5.0], ["cha", 4.0]]);
    assert.strictEqual(tabela.get("cafe"), 5.0);
    assert.strictEqual(tabela.has("leite"), false);
});
