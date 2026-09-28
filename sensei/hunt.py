"""Módulo Caça-Bugs: Treino de Code Review Reverso e Leitura Crítica de Código."""
from sensei.colors import bold, cyan, green, red, yellow, dim, magenta
from sensei.journal import ensure_devlog_dir, ENTRY_TEMPLATE
from datetime import datetime
import re

HUNT_SCENARIOS = [
    {
        "id": 1,
        "title": "Limite de Laço (Off-by-One)",
        "scenario": "A função abaixo deveria somar todos os elementos do array, mas está gerando 'NaN' ao final da execução.",
        "code_lines": [
            "function somarValores(numeros: number[]): number {",
            "    let total = 0;",
            "    for (let i = 0; i <= numeros.length; i++) {",
            "        total += numeros[i];",
            "    }",
            "    return total;",
            "}"
        ],
        "bug_line": 3,
        "explanation": "Na linha 3, a condição 'i <= numeros.length' faz o laço acessar o índice após o final do array ('numeros[numeros.length]'), que vale 'undefined'. Somar número com undefined resulta em NaN.",
        "fix": "for (let i = 0; i < numeros.length; i++) {"
    },
    {
        "id": 2,
        "title": "Retorno do Array.prototype.push",
        "scenario": "O desenvolvedor queria retornar a lista com o novo item adicionado, mas a função retorna um número inteiro (ex: 4).",
        "code_lines": [
            "function adicionarItem(lista: string[], item: string): string[] {",
            "    const novaLista = lista.push(item);",
            "    return novaLista as any;",
            "}"
        ],
        "bug_line": 2,
        "explanation": "Na linha 2, o método '.push()' adiciona o elemento in-place e retorna o NOVO COMPRIMENTO (length) do array, não o array modificado.",
        "fix": "lista.push(item); return lista; // ou return [...lista, item];"
    },
    {
        "id": 3,
        "title": "Ordenação Numérica Padrão do JavaScript",
        "scenario": "Ao ordenar os pontos [100, 25, 5, 1], a lista é retornada como [1, 100, 25, 5].",
        "code_lines": [
            "function ordenarPontuacoes(pontos: number[]): number[] {",
            "    const copia = [...pontos];",
            "    copia.sort();",
            "    return copia;",
            "}"
        ],
        "bug_line": 3,
        "explanation": "Na linha 3, sem uma função comparadora, '.sort()' converte os elementos em strings e compara em ordem lexicográfica. '100' vem antes de '25' porque '1' vem antes de '2'.",
        "fix": "copia.sort((a, b) => a - b);"
    },
    {
        "id": 4,
        "title": "Comparação Inválida com NaN",
        "scenario": "A verificação abaixo nunca entra no bloco 'if', mesmo quando 'resultado' é comprovadamente NaN.",
        "code_lines": [
            "function validarCalculo(resultado: number): string {",
            "    if (resultado === NaN) {",
            "        return 'Erro: cálculo inválido';",
            "    }",
            "    return `Resultado: ${resultado}`;",
            "}"
        ],
        "bug_line": 2,
        "explanation": "Na linha 2, a comparação 'resultado === NaN' sempre retorna false. Na especificação IEEE 754, NaN é o único valor no JavaScript que NÃO é igual a si mesmo (NaN !== NaN).",
        "fix": "if (Number.isNaN(resultado)) {"
    },
    {
        "id": 5,
        "title": "Retorno Esquecido no Array.prototype.map",
        "scenario": "O array resultante da função abaixo sempre vem preenchido com '[undefined, undefined, undefined]'.",
        "code_lines": [
            "function dobrarNumeros(lista: number[]): number[] {",
            "    return lista.map(n => {",
            "        n * 2;",
            "    });",
            "}"
        ],
        "bug_line": 3,
        "explanation": "Na linha 3, ao usar chaves '{ ... }' na arrow function, o retorno implícito é desativado. Como não há a palavra 'return', a função retorna undefined para cada item.",
        "fix": "return n * 2; // ou lista.map(n => n * 2)"
    },
    {
        "id": 6,
        "title": "Mutação Acidental por Shallow Copy",
        "scenario": "Ao atualizar a configuração de um usuário clonado, o objeto do usuário original também tem suas preferências alteradas.",
        "code_lines": [
            "function atualizarTema(usuarioOriginal: any, novoTema: string) {",
            "    const usuarioClonado = { ...usuarioOriginal };",
            "    usuarioClonado.config.tema = novoTema;",
            "    return usuarioClonado;",
            "}"
        ],
        "bug_line": 3,
        "explanation": "Na linha 3, o operador spread '{ ...obj }' só cria uma cópia rasa. O objeto interno 'config' continua apontando para a mesma referência na memória do objeto original.",
        "fix": "const usuarioClonado = structuredClone(usuarioOriginal);"
    },
    {
        "id": 7,
        "title": "Armadilha do Array.prototype.forEach Assíncrono",
        "scenario": "A função abaixo retorna uma lista vazia antes que as requisições assíncronas terminem de executar.",
        "code_lines": [
            "async function carregarTodos(ids: number[], fetchFn: any): Promise<any[]> {",
            "    const dados: any[] = [];",
            "    ids.forEach(async (id) => {",
            "        const item = await fetchFn(id);",
            "        dados.push(item);",
            "    });",
            "    return dados;",
            "}"
        ],
        "bug_line": 3,
        "explanation": "Na linha 3, '.forEach()' não espera Promises. Ele dispara as funções assíncronas e passa direto para o 'return dados', que ainda está vazio.",
        "fix": "return Promise.all(ids.map(id => fetchFn(id))); // ou for (const id of ids)"
    },
    {
        "id": 8,
        "title": "Coerção Acidental de Concatenação no Operador +",
        "scenario": "Ao ler uma idade digitada no formulário (ex: '25') e somar 1, o resultado final é '251' em vez de 26.",
        "code_lines": [
            "function incrementarIdade(idadeString: string): number {",
            "    const proximaIdade = idadeString + 1;",
            "    return proximaIdade as any;",
            "}"
        ],
        "bug_line": 2,
        "explanation": "Na linha 2, quando um dos operandos de '+' é uma string, o JavaScript realiza concatenação de texto em vez de soma aritmética ('25' + 1 = '251').",
        "fix": "const proximaIdade = Number(idadeString) + 1;"
    }
]


def start_hunt_session():
    print("\n" + bold(magenta("==========================================================")))
    print(bold(magenta("    🔍 CAÇA-BUGS: TREINO DE CODE REVIEW REVERSO 🔍     ")))
    print(bold(magenta("==========================================================")))
    print(dim("Leia o código com atenção como um revisor de código sênior.\nIdentifique a linha que contém o defeito lógico.\n"))

    acertos = 0

    for item in HUNT_SCENARIOS:
        print("\n" + bold(cyan(f"--- Caso #{item['id']}: {item['title']} ---")))
        print(bold("Cenário Observado:"))
        print(yellow(item["scenario"]) + "\n")

        print(dim("Código para revisão:"))
        for idx, line in enumerate(item["code_lines"], 1):
            print(f" {dim(str(idx).rjust(2))} | {line}")

        ans = input(bold("\nQual o número da linha com o bug? (ou 'pular') > ")).strip()
        if ans.lower() in ("p", "pular", "skip"):
            print(dim("Caso pulado."))
            continue

        if ans.isdigit() and int(ans) == item["bug_line"]:
            print("\n" + bold(green(f"✔ TIRO CERTEIRO! Linha {item['bug_line']} identificada com sucesso!")))
            acertos += 1
        else:
            print("\n" + bold(red(f"✖ NÃO FOI ESSA! A linha com defeito é a linha {item['bug_line']}.")))

        print("\n" + bold("🧠 Causa Raiz do Modelo Mental:"))
        print(dim(item["explanation"]))

        print("\n" + bold("💡 Correção de 1 linha recomendada:"))
        print(green(item["fix"]))

        salvar = input("\nDeseja salvar essa análise no seu DevLog? (s/N) > ").strip().lower()
        if salvar in ("s", "sim", "y", "yes"):
            agora = datetime.now()
            safe_title = f"caca_bugs_{item['id']}_{re.sub(r'[^\\w\\-_]', '_', item['title'].lower())[:25]}"
            arquivo = ensure_devlog_dir() / f"{agora.strftime('%Y-%m-%d')}_{safe_title}.md"

            conteudo = ENTRY_TEMPLATE.format(
                title=f"Caça-Bugs: {item['title']}",
                date=agora.strftime("%Y-%m-%d %H:%M:%S"),
                tags="caca-bugs, code-review, modelo-mental",
                symptom=item["scenario"],
                expected="Funcionamento sem efeitos colaterais",
                actual="Bug identificado na linha " + str(item["bug_line"]),
                mental_gap=item["explanation"],
                root_cause=f"Linha {item['bug_line']}: {item['code_lines'][item['bug_line']-1]}",
                prevention=f"Aplicar padrão correto: {item['fix']}"
            )
            arquivo.write_text(conteudo, encoding="utf-8")
            print(green(f"✔ Salvo no DevLog: {arquivo}"))

        input(dim("\nPressione ENTER para o próximo caso..."))

    print("\n" + bold(cyan("=== RESUMO DA SESSÃO DE CAÇA-BUGS ===")))
    print(f"Linhas corretas identificadas: {bold(green(str(acertos)))} / {len(HUNT_SCENARIOS)}")
    if acertos == len(HUNT_SCENARIOS):
        print(bold(green("🏆 Olho de águia! Você identificou todos os bugs de runtime!")))
    else:
        print(yellow("💡 Dica: continue praticando leitura de código para fortalecer sua intuição."))
