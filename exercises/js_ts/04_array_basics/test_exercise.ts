import test from "node:test";
import assert from "node:assert";
import { encontrarExtremos, dividirEmFatias } from "./exercise.ts";

test("encontrarExtremos acha menor e maior", () => {
    assert.deepStrictEqual(encontrarExtremos([10, -5, 20, 3]), { min: -5, max: 20 });
    assert.deepStrictEqual(encontrarExtremos([42]), { min: 42, max: 42 });
    assert.throws(() => encontrarExtremos([]), /Array vazio/);
});

test("dividirEmFatias divide array em lotes", () => {
    const arr = [1, 2, 3, 4, 5, 6, 7];
    assert.deepStrictEqual(dividirEmFatias(arr, 3), [[1, 2, 3], [4, 5, 6], [7]]);
    assert.throws(() => dividirEmFatias(arr, 0), RangeError);
});
