import test from "node:test";
import assert from "node:assert";
import fs from "node:fs/promises";
import path from "node:path";
import os from "node:os";
import { BancoChaveValor } from "./exercise.ts";

test("BancoChaveValor armazena e emite eventos com LRU", () => {
    const db = new BancoChaveValor<number>(2);
    const eventos: string[] = [];

    db.on("gravado", (chave) => eventos.push(`set:${chave}`));
    db.on("despejo", (chave) => eventos.push(`evict:${chave}`));

    db.definir("a", 1);
    db.definir("b", 2);
    db.obter("a"); // a vira mais recente, b vira mais antigo
    db.definir("c", 3); // deve despejar b

    assert.strictEqual(db.obter("a"), 1);
    assert.strictEqual(db.obter("b"), undefined); // despejado
    assert.strictEqual(db.obter("c"), 3);

    assert.ok(eventos.includes("set:a"));
    assert.ok(eventos.includes("evict:b"));
});

test("BancoChaveValor salva e recupera do disco", async () => {
    const tmp = await fs.mkdtemp(path.join(os.tmpdir(), "kv-test-"));
    const arquivo = path.join(tmp, "banco.json");

    const db1 = new BancoChaveValor<string>(5, arquivo);
    db1.definir("usuario_1", "Alice");
    db1.definir("usuario_2", "Bob");
    await db1.salvarEmDisco();

    const db2 = new BancoChaveValor<string>(5, arquivo);
    await db2.carregarDoDisco();

    assert.strictEqual(db2.obter("usuario_1"), "Alice");
    assert.strictEqual(db2.obter("usuario_2"), "Bob");

    await fs.rm(tmp, { recursive: true, force: true });
});
