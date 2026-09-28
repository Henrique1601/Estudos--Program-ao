import test from "node:test";
import assert from "node:assert";
import { calcularArea, extrairDados, type Forma, type RespostaAPI } from "./exercise.ts";

test("calcularArea calcula formas", () => {
    assert.strictEqual(calcularArea({ tipo: "circulo", raio: 3 }), 28.27);
    assert.strictEqual(calcularArea({ tipo: "retangulo", largura: 4, altura: 5 }), 20);
    assert.strictEqual(calcularArea({ tipo: "quadrado", lado: 6 }), 36);
});

test("extrairDados respeita união", () => {
    const ok: RespostaAPI<number[]> = { status: "sucesso", dados: [1, 2, 3] };
    assert.deepStrictEqual(extrairDados(ok, []), [1, 2, 3]);
});
