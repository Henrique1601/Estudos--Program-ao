import test from "node:test";
import assert from "node:assert";
import { CentralAlertas } from "./exercise.ts";

test("CentralAlertas dispara niveis e evento qualquer", () => {
    const central = new CentralAlertas();
    const avisos: string[] = [];
    const todos: string[] = [];

    central.on("aviso", msg => avisos.push(msg));
    central.on("qualquer", msg => todos.push(msg));

    central.emitirAlerta("info", "Deploy ok");
    central.emitirAlerta("aviso", "CPU 80%");

    assert.deepStrictEqual(avisos, ["CPU 80%"]);
    assert.deepStrictEqual(todos, ["Deploy ok", "CPU 80%"]);
    assert.strictEqual(central.obterTotalDisparos(), 2);
});
