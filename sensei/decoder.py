"""Decodificador de Erros do Terminal: Traduz mensagens crípticas em modelos mentais."""
import re
from sensei.colors import bold, cyan, green, yellow, red, dim, magenta

ERROR_CATALOG = [
    {
        "pattern": r"Cannot read propert(?:ies|y) of (undefined|null) \(reading '(.+?)'\)",
        "name": "TypeError: Cannot read properties of undefined/null",
        "example": "TypeError: Cannot read properties of undefined (reading 'map')",
        "explanation": "Você tentou acessar uma propriedade ou método (como '.{prop}') em uma variável que vale estritamente 'undefined' ou 'null'. O JavaScript não permite navegar dentro de valores nulos.",
        "root_cause": "Geralmente ocorre quando: 1) Uma função assíncrona não terminou e retornou antes da hora; 2) Um objeto aninhado não possui aquela chave; 3) Uma busca com .find() não achou nada.",
        "debug_checklist": [
            "Coloque um 'console.log(\"DEBUG:\", minhaVariavel)' exatamente na linha anterior.",
            "Use o operador Optional Chaining se a propriedade for opcional: 'objeto?.{prop}'.",
            "Verifique se você não esqueceu de usar 'await' na chamada que gera esse dado."
        ]
    },
    {
        "pattern": r"(.+?) is not a function",
        "name": "TypeError: X is not a function",
        "example": "TypeError: usuario.obterDados is not a function",
        "explanation": "Você colocou parênteses '()' para chamar algo como função, mas o valor real guardado nessa variável não é uma função (é undefined, um objeto, ou uma string).",
        "root_cause": "1) Erro de digitação no nome do método; 2) Importação com destructuring incorreta ('import { foo }' em vez de 'import foo'); 3) A variável foi sobrescrita por outro valor.",
        "debug_checklist": [
            "Imprima 'console.log(typeof {prop})'. Se imprimir 'undefined' ou 'object', você não tem uma função.",
            "Cheque a exportação no arquivo de origem: export default vs export nomeado."
        ]
    },
    {
        "pattern": r"(.+?) is not defined",
        "name": "ReferenceError: X is not defined",
        "example": "ReferenceError: total is not defined",
        "explanation": "O JavaScript procurou por essa variável no escopo atual e em todos os escopos pais até o escopo global, mas não encontrou nenhuma declaração com esse nome.",
        "root_cause": "1) Nome de variável digitado com erro ortográfico (typo); 2) A variável foi declarada dentro de um bloco 'if' ou 'for' com 'let/const' e você tentou usá-la fora; 3) Esqueceu de importar o módulo.",
        "debug_checklist": [
            "Verifique se o nome bate com exatidão (JavaScript é case-sensitive: 'Total' != 'total').",
            "Verifique as chaves '{ }' onde a variável foi criada. Variáveis criadas com let/const morrem ao sair do bloco."
        ]
    },
    {
        "pattern": r"Maximum call stack size exceeded",
        "name": "RangeError: Maximum call stack size exceeded",
        "example": "RangeError: Maximum call stack size exceeded",
        "explanation": "A pilha de chamadas de funções (Call Stack) transbordou. O JavaScript possui um limite de chamadas aninhadas (cerca de 10.000).",
        "root_cause": "Uma função recursiva está chamando a si mesma infinitamente sem uma 'condição de parada' (caso base), ou dois métodos chamam um ao outro em loop infinito.",
        "debug_checklist": [
            "Procure por chamadas recursivas no seu código.",
            "Verifique se o caso base ('if (n <= 1) return ...') está sendo atingido com a entrada recebida."
        ]
    },
    {
        "pattern": r"Unexpected token (.+)",
        "name": "SyntaxError: Unexpected token",
        "example": "SyntaxError: Unexpected token '}'",
        "explanation": "O interpretador do JavaScript encontrou um caractere onde as regras da gramática da linguagem não permitiam.",
        "root_cause": "1) Chave '{', parêntese '(' ou colchete '[' aberto que nunca foi fechado; 2) Vírgula sobrando ou faltando; 3) Tentou fazer JSON.parse() em uma string que não é um JSON válido.",
        "debug_checklist": [
            "Olhe para a linha IMEDIATAMENTE ANTERIOR à linha apontada pelo erro.",
            "Se estiver usando JSON.parse(), imprima a string antes para ver se não veio HTML ou texto vazio."
        ]
    },
    {
        "pattern": r"UnhandledPromiseRejection|Unhandled promise rejection",
        "name": "UnhandledPromiseRejection (Promessa Rejeitada)",
        "example": "UnhandledPromiseRejection: This error originated either by throwing...",
        "explanation": "Uma função assíncrona falhou (lançou um erro ou rejeitou uma Promise) e você não colocou um bloco de captura para tratar a falha.",
        "root_cause": "Falta de 'try / catch' ao redor de um comando com 'await', ou falta de '.catch()' em uma Promise.",
        "debug_checklist": [
            "Envolva o bloco assíncrono em um 'try { await ... } catch (erro) { console.error(erro); }'.",
            "Nunca deixe uma chamada de rede ou banco de dados sem tratamento de falha."
        ]
    },
    {
        "pattern": r"Assignment to constant variable",
        "name": "TypeError: Assignment to constant variable",
        "example": "TypeError: Assignment to constant variable.",
        "explanation": "Você declarou uma variável com 'const' e tentou reatribuir um novo valor a ela usando o operador '='.",
        "root_cause": "Tentar reatribuir variável constante (ex: 'const total = 0; total = 10;').",
        "debug_checklist": [
            "Se o valor precisa mudar com o tempo, declare usando 'let' em vez de 'const'.",
            "Lembre-se: 'const arr = []' permite arr.push(1), mas proíbe 'arr = [1]'."
        ]
    }
]


def decode_error(raw_text: str) -> dict | None:
    for entry in ERROR_CATALOG:
        match = re.search(entry["pattern"], raw_text, re.IGNORECASE)
        if match:
            prop = match.group(2) if len(match.groups()) > 1 else (match.group(1) if match.groups() else "")
            return {
                "name": entry["name"],
                "explanation": entry["explanation"].replace("{prop}", prop),
                "root_cause": entry["root_cause"],
                "debug_checklist": [item.replace("{prop}", prop) for item in entry["debug_checklist"]],
                "prop": prop
            }
    return None


def show_decoded_result(info: dict):
    print("\n" + bold(cyan("==========================================================")))
    print(bold(green(f"  🔍 ERRO IDENTIFICADO: {info['name']}")))
    print(bold(cyan("==========================================================")))

    print("\n" + bold(yellow("1. O que o computador tentou fazer:")))
    print(dim(info["explanation"]))

    print("\n" + bold(yellow("2. Causas raízes mais frequentes:")))
    print(dim(info["root_cause"]))

    print("\n" + bold(yellow("3. Checklist de Investigação Ativa:")))
    for step in info["debug_checklist"]:
        print(f" {green('•')} {step}")


def start_decoder_session():
    print("\n" + bold(magenta("==========================================================")))
    print(bold(magenta("    🛠️ DECODIFICADOR DE ERROS: TRADUTOR DO RUNTIME 🛠️     ")))
    print(bold(magenta("==========================================================")))
    print(dim("Cole a mensagem de erro do seu terminal ou consulte os 7 erros mais comuns.\n"))

    print(f" {bold(cyan('1.'))} 📋 Colar mensagem de erro do terminal")
    print(f" {bold(cyan('2.'))} 📚 Ver catálogo dos erros mais comuns de JavaScript/Node\n")

    opcao = input(bold("Escolha uma opção > ")).strip()

    if opcao == "1":
        print("\n" + yellow("Cole a linha de erro completa (ex: TypeError: Cannot read properties of undefined...):"))
        raw = input(bold("> ")).strip()
        if not raw:
            print(red("Nenhum texto informado."))
            return

        resultado = decode_error(raw)
        if resultado:
            show_decoded_result(resultado)
        else:
            print("\n" + yellow("Padrão exato não encontrado no catálogo automático."))
            print(dim("Dica: procure se o erro começa com 'TypeError', 'ReferenceError' ou 'SyntaxError'."))
            print(dim("Tente identificar a primeira linha do stack trace onde aparece o nome do seu arquivo."))

    elif opcao == "2":
        print("\n" + bold(cyan("=== CATÁLOGO DE ERROS FREQUENTES ===")))
        for idx, item in enumerate(ERROR_CATALOG, 1):
            print(f" {cyan(str(idx))}. {bold(item['name'])}")
            print(f"    {dim(item['example'])}")

        escolha = input(bold("\nDigite o número para ver a explicação (ou ENTER para voltar) > ")).strip()
        if escolha.isdigit() and 1 <= int(escolha) <= len(ERROR_CATALOG):
            item = ERROR_CATALOG[int(escolha) - 1]
            info = {
                "name": item["name"],
                "explanation": item["explanation"].replace("{prop}", "x"),
                "root_cause": item["root_cause"],
                "debug_checklist": [i.replace("{prop}", "x") for i in item["debug_checklist"]]
            }
            show_decoded_result(info)
