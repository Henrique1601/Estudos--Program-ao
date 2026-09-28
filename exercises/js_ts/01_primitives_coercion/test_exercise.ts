import test from "node:test";
import assert from "node:assert";
import { ehFalsy, somarSeguro, formatarMoeda } from "./exercise.ts";

test("ehFalsy identifica valores falsy", () => {
    assert.strictEqual(ehFalsy(0), true);
    assert.strictEqual(ehFalsy(""), true);
    assert.strictEqual(ehFalsy(null), true);
    assert.strictEqual(ehFalsy(undefined), true);
    assert.strictEqual(ehFalsy(NaN), true);
    assert.strictEqual(ehFalsy(false), true);
    assert.strictEqual(ehFalsy("0"), false);
    assert.strictEqual(ehFalsy([]), false);
});

test("somarSeguro soma ou lanca TypeError", () => {
    assert.strictEqual(somarSeguro(10, 20), 30);
    assert.strictEqual(somarSeguro("15", "5"), 20);
    assert.throws(() => somarSeguro(null, 10), TypeError);
    assert.throws(() => somarSeguro("abc", 10), TypeError);
});

test("formatarMoeda formata centavos", () => {
    assert.strictEqual(formatarMoeda(1550), "R$ 15,50");
    assert.strictEqual(formatarMoeda(5), "R$ 0,05");
});
