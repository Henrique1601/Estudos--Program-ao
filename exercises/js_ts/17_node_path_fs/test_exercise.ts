import test from "node:test";
import assert from "node:assert";
import fs from "node:fs/promises";
import path from "node:path";
import os from "node:os";
import { lerJsonSeguro, salvarJson } from "./exercise.ts";

test("lerJsonSeguro e salvarJson manipulam dados", async () => {
    const tmp = await fs.mkdtemp(path.join(os.tmpdir(), "fs-test-"));
    const arquivo = path.join(tmp, "subpasta", "dados.json");

    await salvarJson(arquivo, { ativo: true, versao: 1 });
    const lido = await lerJsonSeguro(arquivo, { ativo: false });
    assert.deepStrictEqual(lido, { ativo: true, versao: 1 });

    const inexistente = await lerJsonSeguro(path.join(tmp, "nada.json"), { padrao: true });
    assert.deepStrictEqual(inexistente, { padrao: true });

    await fs.rm(tmp, { recursive: true, force: true });
});
