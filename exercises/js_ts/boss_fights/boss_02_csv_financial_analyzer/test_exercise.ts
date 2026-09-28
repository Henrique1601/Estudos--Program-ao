import test from "node:test";
import assert from "node:assert";
import { analisarExtratoCsv } from "./exercise.ts";

test("analisarExtratoCsv processa linhas e calcula metricas", () => {
    const csv = `data,descricao,categoria,valor,tipo
2026-09-01,Salario,trabalho,5000,receita
2026-09-02,Mercado,alimentacao,400,despesa
2026-09-03,Aluguel,moradia,1500,despesa
2026-09-04,Restaurante,alimentacao,150,despesa
2026-09-05,Freelance,trabalho,800,receita`;

    const resumo = analisarExtratoCsv(csv);

    assert.strictEqual(resumo.totalReceitas, 5800);
    assert.strictEqual(resumo.totalDespesas, 2050);
    assert.strictEqual(resumo.saldoFinal, 3750);
    assert.strictEqual(resumo.maiorDespesaCategoria, "moradia"); // 1500 > 550
    assert.deepStrictEqual(resumo.contagemPorCategoria, {
        trabalho: 2,
        alimentacao: 2,
        moradia: 1,
    });
});
