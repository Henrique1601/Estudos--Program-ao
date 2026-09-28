import test from "node:test";
import assert from "node:assert";
import { obterNomesAprovados, removerFalsy } from "./exercise.ts";

test("obterNomesAprovados filtra e mapeia", () => {
    const lista = [
        { nome: "Ana", nota: 85 },
        { nome: "Beto", nota: 50 },
        { nome: "Carla", nota: 90 },
    ];
    assert.deepStrictEqual(obterNomesAprovados(lista, 80), ["ANA", "CARLA"]);
});

test("removerFalsy limpa valores falsos", () => {
    const entrada = [0, "oi", false, "mundo", null, undefined, 42];
    assert.deepStrictEqual(removerFalsy(entrada), ["oi", "mundo", 42]);
});
