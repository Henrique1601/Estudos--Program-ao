import test from "node:test";
import assert from "node:assert";
import { Fila, trocarPrimeiroComUltimo } from "./exercise.ts";

test("Fila gerencia itens FIFO com tipagem estrita", () => {
    const fila = new Fila<string>();
    fila.enfileirar("primeiro");
    fila.enfileirar("segundo");

    assert.strictEqual(fila.tamanho(), 2);
    assert.strictEqual(fila.primeiro(), "primeiro");
    assert.strictEqual(fila.desenfileirar(), "primeiro");
    assert.strictEqual(fila.desenfileirar(), "segundo");
    assert.strictEqual(fila.desenfileirar(), undefined);
});

test("trocarPrimeiroComUltimo troca pontas", () => {
    assert.deepStrictEqual(trocarPrimeiroComUltimo([1, 2, 3, 4]), [4, 2, 3, 1]);
    assert.deepStrictEqual(trocarPrimeiroComUltimo(["a"]), ["a"]);
});
