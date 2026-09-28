import test from "node:test";
import assert from "node:assert";
import { esperar, promessaComTimeout } from "./exercise.ts";

test("esperar aguarda intervalo", async () => {
    const t0 = Date.now();
    await esperar(30);
    assert.ok(Date.now() - t0 >= 25);
});

test("promessaComTimeout resolve a tempo", async () => {
    const rapida = esperar(10).then(() => "ok");
    const res = await promessaComTimeout(rapida, 50);
    assert.strictEqual(res, "ok");
});

test("promessaComTimeout estoura limite", async () => {
    const lenta = esperar(80).then(() => "tarde");
    await assert.rejects(
        () => promessaComTimeout(lenta, 20),
        /Tempo limite excedido/
    );
});
