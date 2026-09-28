import test from "node:test";
import assert from "node:assert";
import { contarFrequencia, agruparPor } from "./exercise.ts";

test("contarFrequencia cria histograma", () => {
    assert.deepStrictEqual(contarFrequencia(["a", "b", "a", "c", "b", "a"]), {
        a: 3,
        b: 2,
        c: 1
    });
});

test("agruparPor agrupa elementos", () => {
    const palavras = ["sol", "lua", "marte"];
    assert.deepStrictEqual(agruparPor(palavras, p => p.length), {
        3: ["sol", "lua"],
        5: ["marte"]
    });
});
