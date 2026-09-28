"""Blind Trace: Modo Compilador Mental (Flashcards de Execução Mental no Terminal)."""
from sensei.colors import bold, cyan, green, red, yellow, dim, magenta

TRACES = [
    {
        "id": 1,
        "title": "Coerção de Tipos e Operadores",
        "snippet": """const a = 1 + "2";
const b = 1 - "2";
console.log(a, b);""",
        "question": "Qual é a saída impressa no console? (Exemplo de formato: 12 -1)",
        "expected": "12 -1",
        "explanation": "No operador '+', a presença de uma string força a concatenação ('1' + '2' = '12'). No operador '-', strings numéricas são convertidas para números (1 - 2 = -1)."
    },
    {
        "id": 2,
        "title": "Mutação de Array por Referência",
        "snippet": """const x = [1, 2, 3];
const y = x;
y.push(4);
console.log(x.length);""",
        "question": "Qual é o valor final impresso de x.length?",
        "expected": "4",
        "explanation": "Em JavaScript, arrays são tipos de referência. Atribuir 'y = x' NÃO copia o array, apenas copia o ponteiro para a mesma região da memória."
    },
    {
        "id": 3,
        "title": "Escopo Léxico e Closure com var vs let",
        "snippet": """const arr = [];
for (let i = 0; i < 3; i++) {
    arr.push(() => i);
}
console.log(arr[0]());""",
        "question": "Qual é a saída impressa ao chamar arr[0]()?",
        "expected": "0",
        "explanation": "Com 'let', cada iteração do laço for cria um novo binding léxico isolado na memória. Cada função fecha sobre seu próprio 'i'."
    },
    {
        "id": 4,
        "title": "Falsy Values e Operador Nullish Coalescing",
        "snippet": """const valor = 0;
const res1 = valor || 10;
const res2 = valor ?? 10;
console.log(res1, res2);""",
        "question": "Qual é a saída de res1 e res2? (Exemplo: 10 0)",
        "expected": "10 0",
        "explanation": "O operador '||' avalia qualquer valor falsy (e 0 é falsy, caindo no 10). Já o operador '??' só substitui se for estritamente null ou undefined."
    },
    {
        "id": 5,
        "title": "Ordem do Event Loop (Microtasks vs Macrotasks)",
        "snippet": """console.log("A");
setTimeout(() => console.log("B"), 0);
Promise.resolve().then(() => console.log("C"));
console.log("D");""",
        "question": "Qual é a ordem exata das 4 letras impressas? (Exemplo: A B C D)",
        "expected": "A D C B",
        "explanation": "1) Código síncrono roda primeiro (A, D). 2) Microtasks (fila de Promises) rodam imediatamente após a pilha síncrona (C). 3) Macrotasks (setTimeout) rodam na próxima volta do Event Loop (B)."
    }
]


def start_trace_session():
    print("\n" + bold(magenta("==========================================================")))
    print(bold(magenta("    🧠 BLIND TRACE: TREINO DE COMPILADOR MENTAL 🧠    ")))
    print(bold(magenta("==========================================================")))
    print(dim("Treine simulação mental de memória e estado sem rodar o código.\n"))

    acertos = 0

    for trace in TRACES:
        print("\n" + bold(cyan(f"--- Desafio #{trace['id']}: {trace['title']} ---")))
        print(dim("Analise o trecho de código abaixo mentalmente:\n"))
        print(bold(yellow(trace["snippet"])) + "\n")
        print(bold(trace["question"]))

        resposta = input(bold("\nSua previsão mental > ")).strip()

        # Normaliza comparacao (tira espacos duplos)
        resp_norm = " ".join(resposta.split()).lower()
        exp_norm = " ".join(trace["expected"].split()).lower()

        if resp_norm == exp_norm:
            print("\n" + green(f"✔ EXATO! Resposta: {trace['expected']}"))
            acertos += 1
        else:
            print("\n" + red(f"✖ DIVERGÊNCIA MENTAL! Você disse '{resposta}', o runtime faz '{trace['expected']}'."))

        print("\n" + bold("Modelo Mental Real:"))
        print(dim(trace["explanation"]))
        input(dim("\nPressione ENTER para o próximo..."))

    print("\n" + bold(cyan("=== RESULTADO DA SESSÃO ===")))
    print(f"Acertos: {bold(green(str(acertos)))} / {len(TRACES)}")
    if acertos == len(TRACES):
        print(bold(green("🎉 Incrível! Seu compilador mental de JavaScript está afiado!")))
    else:
        print(yellow("💡 Dica: registre os pontos onde sua previsão divergiu no seu DevLog com 'python main.py log'."))
