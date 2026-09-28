import test from "node:test";
import assert from "node:assert";
import { criarContador, memoizar } from "./exercise.ts";

test("criarContador gerencia estado fechado", () => {
    const c1 = criarContador(10);
    assert.strictEqual(c1.obter(), 10);
    assert.strictEqual(c1.incrementar(), 11);
    assert.strictEqual(c1.incrementar(), 12);
    c1.resetar();
    assert.strictEqual(c1.obter(), 10);
});

test("memoizar evita execucoes redundantes", () => {
    let execucoes = 0;
    const dobro = memoizar((n: number) => {
        execucoes++;
        return n * 2;
    });

    assert.strictEqual(dobro(5), 10);
    assert.strictEqual(dobro(5), 10);
    assert.strictEqual(execucoes, 1);
    assert.strictEqual(dobro(6), 12);
    assert.strictEqual(execucoes, 2);
});
