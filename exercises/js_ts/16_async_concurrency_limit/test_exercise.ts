import test from "node:test";
import assert from "node:assert";
import { executarComLimite } from "./exercise.ts";

test("executarComLimite limita tarefas ativas", async () => {
    let ativas = 0;
    let maxAtivas = 0;

    const fn = async (n: number) => {
        ativas++;
        maxAtivas = Math.max(maxAtivas, ativas);
        await new Promise(r => setTimeout(r, 20));
        ativas--;
        return n * 10;
    };

    const res = await executarComLimite([1, 2, 3, 4, 5], 2, fn);
    assert.deepStrictEqual(res, [10, 20, 30, 40, 50]);
    assert.ok(maxAtivas <= 2, `Executou ${maxAtivas} concorrentes (limite era 2)`);
});
