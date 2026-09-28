import test from "node:test";
import assert from "node:assert";
import { ValidacaoError, validarUsuario, parseJsonSeguro } from "./exercise.ts";

test("validarUsuario lanca ValidacaoError com campo correto", () => {
    assert.throws(
        () => validarUsuario({ nome: "Al", idade: 25 }),
        (err: any) => err instanceof ValidacaoError && err.campo === "nome"
    );
    assert.throws(
        () => validarUsuario({ nome: "Alice", idade: -1 }),
        (err: any) => err instanceof ValidacaoError && err.campo === "idade"
    );
    assert.doesNotThrow(() => validarUsuario({ nome: "Alice", idade: 25 }));
});

test("parseJsonSeguro recupera com fallback", () => {
    assert.deepStrictEqual(parseJsonSeguro('{"ok": true}', { ok: false }), { ok: true });
    assert.deepStrictEqual(parseJsonSeguro("invalido", { ok: false }), { ok: false });
});
