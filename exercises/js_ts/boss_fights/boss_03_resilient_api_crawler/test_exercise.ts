import test from "node:test";
import assert from "node:assert";
import { rastrearComResiliencia } from "./exercise.ts";

test("rastrearComResiliencia coleta sucessos e recupera de erros parciais", async () => {
    let falhasItem2 = 0;

    const itens = [
        {
            id: "req-1",
            requisicao: async () => "Resultado 1",
        },
        {
            id: "req-2",
            requisicao: async () => {
                falhasItem2++;
                if (falhasItem2 < 2) throw new Error("Queda momentanea");
                return "Resultado 2";
            },
        },
        {
            id: "req-3",
            requisicao: async () => {
                // Timeout intencional
                await new Promise((r) => setTimeout(r, 60));
                return "Lento demais";
            },
        },
    ];

    const resultado = await rastrearComResiliencia(itens, 30, 2);

    assert.strictEqual(resultado.sucessos.length, 2);
    assert.strictEqual(resultado.sucessos[0].id, "req-1");
    assert.strictEqual(resultado.sucessos[1].id, "req-2");
    assert.strictEqual(resultado.falhas.length, 1);
    assert.strictEqual(resultado.falhas[0].id, "req-3");
});
