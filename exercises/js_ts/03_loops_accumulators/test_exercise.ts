import test from "node:test";
import assert from "node:assert";
import { somarPares, contarVogais, fatorial } from "./exercise.ts";

test("somarPares soma apenas numeros pares", () => {
    assert.strictEqual(somarPares([1, 2, 3, 4, 5, 6]), 12);
    assert.strictEqual(somarPares([1, 3, 5]), 0);
    assert.strictEqual(somarPares([]), 0);
});

test("contarVogais conta vogais sem case sensitivity", () => {
    assert.strictEqual(contarVogais("JavaScript"), 3);
    assert.strictEqual(contarVogais("NODE JS"), 3);
    assert.strictEqual(contarVogais("xyz"), 0);
});

test("fatorial calcula fatorial ou lanca RangeError", () => {
    assert.strictEqual(fatorial(0), 1);
    assert.strictEqual(fatorial(5), 120);
    assert.throws(() => fatorial(-1), RangeError);
});
