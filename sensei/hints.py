"""Sistema de Dicas Progressivas em 3 níveis (Anti-IA)."""
from sensei.colors import bold, cyan, yellow, green, dim, red

HINTS_DB = {
    "01_primitives_coercion": {
        1: "Pense em quais valores no JavaScript são convertidos para `false` quando você aplica o operador de negação dupla `Boolean(v)` ou `!v`.",
        2: "Para somarSeguro: Verifique se `a == null || b == null`. Depois `const numA = Number(a)`. Se `Number.isNaN(numA)`, dispare `new TypeError(...)`.",
        3: "Para formatarMoeda: Divida os centavos por 100 com `Math.floor`. Pegue o resto com `% 100` e use `.toString().padStart(2, '0')`."
    },
    "02_conditionals_branching": {
        1: "Prefira retornar cedo (Guard Clauses) em vez de aninhar múltiplos blocos `if/else`.",
        2: "No ano bissexto: `(ano % 4 === 0 && ano % 100 !== 0) || (ano % 400 === 0)`. Valide limites primeiro.",
        3: "No desconto: use `switch(cupom)` ou mapeamento simples `{ DESC10: 0.10, DESC20: 0.20 }`. Multiplique `valor * (1 - taxa)`."
    },
    "03_loops_accumulators": {
        1: "Ao buscar o fatorial ou somar pares, inicialize uma variável acumuladora antes do laço.",
        2: "Para contarVogais: crie uma string `'aeiou'` e itere sobre cada caractere de `texto.toLowerCase()`. Se `vogais.includes(letra)`, incremente.",
        3: "Para fatorial de n: se n < 0 lance RangeError. Use um loop `let res = 1; for(let i = 2; i <= n; i++) res *= i; return res;`."
    },
    "04_array_basics": {
        1: "Proibido Math.min e Math.max. Como você descobre o menor número de uma fila de pessoas olhando uma a uma?",
        2: "Inicialize `let min = numeros[0]; let max = numeros[0];`. Itere do índice 1 em diante. Se `num < min` atualize `min`. Se `num > max` atualize `max`.",
        3: "Para fatiar em lotes (chunking): use um laço `for (let i = 0; i < itens.length; i += tamanhoFatia)` e aplique `itens.slice(i, i + tamanhoFatia)`."
    },
    "05_functions_closures": {
        1: "Uma closure é uma função que 'lembra' do ambiente léxico onde foi criada, mesmo depois que a função externa terminou.",
        2: "Para o contador: declare `let valor = inicial;` dentro de `criarContador`. As funções internas leem e alteram esse mesmo `valor`.",
        3: "Para memoizar: crie `const cache = new Map();`. Na função retornada: `if (cache.has(arg)) return cache.get(arg)!; const res = fn(arg); cache.set(arg, res); return res;`."
    },
    "06_objects_destructuring": {
        1: "Como você cria um novo objeto pegando apenas certas chaves de um objeto existente sem mutar o original?",
        2: "Para selecionar: crie `const res = {} as Pick<T, K>;`. Itere com `for (const chave of chaves) { if (chave in obj) res[chave] = obj[chave]; }`.",
        3: "Para mesclar: utilize a sintaxe de desestruturação com spread `{ ...padrao, ...sobrescrita }`."
    },
    "07_ts_basic_interfaces": {
        1: "Tipagem estrita impede erros de cálculo de ponto flutuante antes mesmo de rodar o código.",
        2: "Itere sobre os itens somando `item.precoUnitario * item.quantidade`. Calcule o desconto multiplicando pela porcentagem dividida por 100.",
        3: "Retorne o objeto no formato exato da interface: `{ totalBruto, desconto: valorDesconto, totalLiquido: totalBruto - valorDesconto }`."
    },
    "08_ts_unions_narrowing": {
        1: "O TypeScript permite refinar o tipo de uma variável usando propriedades literais distintas (Discriminated Unions).",
        2: "Faça `switch (forma.tipo)`. No case 'circulo', a propriedade `forma.raio` estará disponível sem erros de compilação.",
        3: "Para o círculo: use `Math.PI * Math.pow(forma.raio, 2)`. Para arredondar 2 casas: `Math.round(area * 100) / 100`."
    },
    "09_array_methods_map_filter": {
        1: "Métodos funcionais não devem alterar o array original recebido como parâmetro.",
        2: "Encadeie métodos: `estudantes.filter(e => e.nota >= notaCorte).map(e => e.nome.toUpperCase())`.",
        3: "Para removerFalsy: aplique `itens.filter((item): item is T => Boolean(item))` para satisfazer o sistema de tipos."
    },
    "10_array_methods_reduce": {
        1: "O método `reduce` reduz uma coleção a um único valor acumulado (que pode ser um número, array ou objeto).",
        2: "Passe o acumulador inicial como `{}` no segundo argumento do reduce. Para cada item, incremente `acc[item] = (acc[item] || 0) + 1`.",
        3: "No agrupamento: `const chave = seletorChave(item); if (!acc[chave]) acc[chave] = []; acc[chave].push(item); return acc;`."
    },
    "11_sets_and_maps": {
        1: "A busca em um `Set` ou `Map` tem complexidade de tempo O(1), enquanto `array.includes` é O(n).",
        2: "Para interseção: crie `const conjuntoB = new Set(b);`. Filtre `a` verificando `conjuntoB.has(item)`. Use `[...new Set(resultado)]` para remover repetidos.",
        3: "Para tabela de preços: use `new Map(itens)`. Acesse com `tabela.get(chave)` e verifique existência com `tabela.has(chave)`."
    },
    "12_error_handling_custom": {
        1: "Herde de `Error` usando `class MinhaExcecao extends Error` e chame `super(mensagem)` no construtor.",
        2: "Não esqueça de atribuir `this.name = 'ValidacaoError'` no construtor para que o nome da exceção fique correto.",
        3: "Para JSON seguro: envolva `JSON.parse(texto)` em um bloco `try / catch`. No catch retorne o fallback."
    },
    "13_ts_generics": {
        1: "Generics funcionam como 'parâmetros de tipos' para que a mesma estrutura funcione para strings, números ou objetos.",
        2: "Na classe `Fila<T>`: use um array privado `private itens: T[] = []`. Enfileirar usa `.push()` e desenfileirar usa `.shift()`.",
        3: "Para trocar pontas: se `lista.length <= 1` retorne a cópia. Caso contrário, crie `[...lista]` e faça destructuring swap `[copia[0], copia[ult]] = [copia[ult], copia[0]]`."
    },
    "14_async_promises_basics": {
        1: "Uma Promise representa um valor que pode estar disponível agora, no futuro ou nunca.",
        2: "Para esperar: `return new Promise(resolve => setTimeout(resolve, ms));`.",
        3: "Para timeout: crie uma promessa de temporizador que rejeita após `timeoutMs`. Use `Promise.race([promessa, temporizadorRejeita])`."
    },
    "15_async_await_flow": {
        1: "Nunca use `array.forEach` com funções assíncronas se você precisa aguardar a conclusão delas.",
        2: "Use um laço `for (const item of itens)` padrão e aguarde com `await tarefaAsync(item)` a cada volta.",
        3: "Para o retry: laço `for (let i = 1; i <= max; i++)` com `try { return await fn(); } catch(err) { if (i === max) throw err; }`."
    },
    "16_async_concurrency_limit": {
        1: "Se você tem 100 requisições, rodá-las todas de uma vez derruba o servidor. Rodar em série é muito lento. Limitar concorrência é o meio termo.",
        2: "Crie um índice de leitura e um número de workers simultâneos igual ao limite. Cada worker pega o próximo item livre da fila enquanto houver.",
        3: "Estrutura: Guarde os resultados em um array do mesmo tamanho `const resultados = new Array(itens.length)`. Use `Promise.all(workers)`."
    },
    "17_node_path_fs": {
        1: "Em Node.js moderno, prefira sempre o módulo com promises: `import fs from 'node:fs/promises';`.",
        2: "Para lerJsonSeguro: leia com `fs.readFile(caminho, 'utf-8')` e faça `JSON.parse`. Se estourar erro, retorne o fallback.",
        3: "Para salvarJson: use `path.dirname(caminho)` e garanta a pasta com `fs.mkdir(dir, { recursive: true })`. Depois salve com `JSON.stringify(dados, null, 2)`."
    },
    "18_node_events_streams": {
        1: "O padrão Observer do Node é implementado pela classe `EventEmitter` do módulo nativo `node:events`.",
        2: "Herde de `EventEmitter`. No método `emitirAlerta`, incremente seu contador e chame `this.emit(nivel, mensagem)` e `this.emit('qualquer', mensagem)`.",
        3: "Crie métodos getters para expor métricas internas sem expor variáveis privadas."
    },
    "19_mental_trace_real_bugs": {
        1: "Em JavaScript, `[10, 2, 5].sort()` vira `[10, 2, 5]` porque os números viram strings! '10' começa com '1' e vem antes de '2'.",
        2: "Bug 1: Passe sempre a função comparadora `(a, b) => a - b`. Bug 2: Use `structuredClone(usuario)` ou spread aninhado para cópia profunda.",
        3: "Bug 3: Substitua `forEach(async ...)` por `Promise.all(ids.map(id => buscadorAsync(id)))`."
    },
    "20_lru_cache_algorithm": {
        1: "O objeto `Map` em JavaScript mantém a ORDEM de inserção das chaves! Se você deletar e reinserir uma chave, ela vai pro fim da fila.",
        2: "No `get(chave)`: se não existe, retorne undefined. Se existe, leia o valor, delete com `this.cache.delete(chave)` e reinsira com `this.cache.set(chave, valor)`. Retorne o valor.",
        3: "No `put(chave, valor)`: se já existe, delete. Se estourou capacidade, pegue a primeira chave com `this.cache.keys().next().value` e delete. Depois faça `this.cache.set(chave, valor)`."
    }
}


def get_hint(exercise_name: str, level: int = 1) -> str:
    # Normaliza o nome do exercicio
    clean_name = exercise_name.lower().strip()
    match_key = None
    for k in HINTS_DB:
        if k in clean_name or clean_name in k:
            match_key = k
            break

    if not match_key:
        return yellow(f"Nenhuma dica cadastrada para o exercício '{exercise_name}'. Leia o README.md na pasta do exercício.")

    hints_for_ex = HINTS_DB[match_key]
    level = max(1, min(3, level))
    hint_text = hints_for_ex.get(level, hints_for_ex.get(1))

    level_names = {
        1: ("Dica Nível 1: Provocação Conceitual", cyan),
        2: ("Dica Nível 2: Estrutura / Pseudocódigo", yellow),
        3: ("Dica Nível 3: Pistas da API / Standard Library", green)
    }
    title, color_fn = level_names[level]

    return f"\n{bold(color_fn(title))}\n{hint_text}\n"
