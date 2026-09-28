import test from "node:test";
import assert from "node:assert";
import { LRUCache } from "./exercise.ts";

test("LRUCache armazena e recupera valores", () => {
    const lru = new LRUCache<string, number>(2);
    lru.put("a", 1);
    lru.put("b", 2);

    assert.strictEqual(lru.get("a"), 1);
    assert.strictEqual(lru.get("b"), 2);
});

test("LRUCache descarta chave menos recentemente usada ao estourar capacidade", () => {
    const lru = new LRUCache<string, number>(2);
    lru.put("a", 1);
    lru.put("b", 2);

    // Acessa 'a', tornando 'b' o menos recentemente usado
    lru.get("a");

    // Adiciona 'c', deve descartar 'b'
    lru.put("c", 3);

    assert.strictEqual(lru.get("a"), 1);
    assert.strictEqual(lru.get("b"), undefined); // descartado!
    assert.strictEqual(lru.get("c"), 3);
});

test("LRUCache valida capacidade minima", () => {
    assert.throws(() => new LRUCache(0), RangeError);
});
