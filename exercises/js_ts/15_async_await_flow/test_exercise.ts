import test from "node:test";
import assert from "node:assert";
import { executarEmSerie, tentarComRetry } from "./exercise.ts";

test("executarEmSerie executa sequencialmente", async () => {
    const rastro: string[] = [];
    const fn = async (n: number) => {
        rastro.push(`in_${n}`);
        await new Promise(r => setTimeout(r, 10));
        rastro.push(`out_${n}`);
        return n * 2;
    };

    const res = await executarEmSerie([1, 2], fn);
    assert.deepStrictEqual(res, [2, 4]);
    assert.deepStrictEqual(rastro, ["in_1", "out_1", "in_2", "out_2"]);
});

test("tentarComRetry tolera falhas parciais", async () => {
    let t = 0;
    const res = await tentarComRetry(async () => {
        t++;
        if (t < 2) throw new Error("Falha temporaria");
        return "Sucesso";
    }, 3);
    assert.strictEqual(res, "Sucesso");
    assert.strictEqual(t, 2);
});
