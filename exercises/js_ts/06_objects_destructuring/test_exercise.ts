import test from "node:test";
import assert from "node:assert";
import { selecionarPropriedades, mesclarConfiguracoes } from "./exercise.ts";

test("selecionarPropriedades extrai chaves", () => {
    const usuario = { id: 1, nome: "Leo", email: "leo@teste.com", senhaHash: "123" };
    const publico = selecionarPropriedades(usuario, ["id", "nome"]);
    assert.deepStrictEqual(publico, { id: 1, nome: "Leo" });
});

test("mesclarConfiguracoes une objetos", () => {
    const padrao = { tema: "claro", porta: 3000 };
    const custom = { tema: "escuro" };
    assert.deepStrictEqual(mesclarConfiguracoes(padrao, custom), { tema: "escuro", porta: 3000 });
});
