import test from "node:test";
import assert from "node:assert";
import { gerarRecibo, type ItemVenda } from "./exercise.ts";

test("gerarRecibo calcula totais e descontos", () => {
    const itens: ItemVenda[] = [
        { id: "1", nome: "Teclado", precoUnitario: 100, quantidade: 2 }, // 200
        { id: "2", nome: "Mouse", precoUnitario: 50, quantidade: 1 },    // 50
    ];

    const recibo = gerarRecibo(itens, 10); // 10% de desconto
    assert.strictEqual(recibo.totalBruto, 250);
    assert.strictEqual(recibo.desconto, 25);
    assert.strictEqual(recibo.totalLiquido, 225);
});
