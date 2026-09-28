import test from "node:test";
import assert from "node:assert";
import { classificarNota, ehAnoBissexto, calcularDesconto } from "./exercise.ts";

test("classificarNota avalia pontuacoes", () => {
    assert.strictEqual(classificarNota(95), "A");
    assert.strictEqual(classificarNota(82), "B");
    assert.strictEqual(classificarNota(70), "C");
    assert.strictEqual(classificarNota(61), "D");
    assert.strictEqual(classificarNota(40), "F");
    assert.throws(() => classificarNota(-5), RangeError);
    assert.throws(() => classificarNota(105), RangeError);
});

test("ehAnoBissexto valida anos", () => {
    assert.strictEqual(ehAnoBissexto(2024), true);
    assert.strictEqual(ehAnoBissexto(2023), false);
    assert.strictEqual(ehAnoBissexto(1900), false);
    assert.strictEqual(ehAnoBissexto(2000), true);
});

test("calcularDesconto aplica cupons corretamente", () => {
    assert.strictEqual(calcularDesconto(100, "DESC10"), 90);
    assert.strictEqual(calcularDesconto(200, "DESC20"), 160);
    assert.strictEqual(calcularDesconto(100, "INVALIDO"), 100);
});
