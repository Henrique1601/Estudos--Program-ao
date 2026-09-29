"""Visualizador de Memória e Call Stack no Terminal: Torna o estado invisível visível."""
import time
from sensei.colors import bold, cyan, green, yellow, red, dim, magenta

def simular_loop_acumulador():
    print("\n" + bold(cyan("=== SIMULAÇÃO 1: LAÇO ACUMULADOR (LOOP ACCUMULATOR) ===")))
    print(dim("Código analisado:"))
    codigo = """const numeros = [10, 25, 5];
let total = 0;
for (let i = 0; i < numeros.length; i++) {
    total += numeros[i];
}"""
    print(yellow(codigo) + "\n")
    print(bold("Evolução da Memória RAM ciclo a ciclo:"))
    print("+" + "-"*8 + "+" + "-"*10 + "+" + "-"*16 + "+" + "-"*14 + "+" + "-"*15 + "+")
    print(f"| {bold('Passo')}  | {bold('Índice i')} | {bold('Elemento atual')} | {bold('total (antes)')} | {bold('total (depois)')} |")
    print("+" + "-"*8 + "+" + "-"*10 + "+" + "-"*16 + "+" + "-"*14 + "+" + "-"*15 + "+")

    numeros = [10, 25, 5]
    total = 0
    for passo, (i, elem) in enumerate(enumerate(numeros), 1):
        total_antes = total
        total += elem
        time.sleep(0.3)
        print(f"| {str(passo).center(8)} | {str(i).center(10)} | {str(elem).center(16)} | {str(total_antes).center(14)} | {bold(green(str(total))).center(23)} |")

    print("+" + "-"*8 + "+" + "-"*10 + "+" + "-"*16 + "+" + "-"*14 + "+" + "-"*15 + "+")
    print(bold(green(f"\nValor final de 'total' na memória: {total}")))
    print(dim("Lição: a variável 'total' é sobrescrita a cada volta, mantendo apenas o estado acumulado mais recente."))


def simular_call_stack_recursiva():
    print("\n" + bold(cyan("=== SIMULAÇÃO 2: CALL STACK RECURSIVA (PILHA DE CHAMADAS) ===")))
    print(dim("Código analisado:"))
    codigo = """function fatorial(n) {
    if (n <= 1) return 1;
    return n * fatorial(n - 1);
}
fatorial(3);"""
    print(yellow(codigo) + "\n")

    print(bold("Fase 1: Empilhamento (Stack Growing) -> cada chamada aguarda o retorno da próxima:"))
    stack = []
    chamadas = [3, 2, 1]
    for n in chamadas:
        stack.append(f"fatorial({n})")
        print(f"  ⬇ [PUSH] Empilhando: {bold(cyan(stack[-1]))} | Pilha atual: {dim(' -> '.join(stack))}")
        time.sleep(0.3)

    print("\n" + bold("Fase 2: Caso base atingido (n=1 retorna 1). Desempilhamento (Unwinding):"))
    valores = {1: 1, 2: 2, 3: 6}
    while stack:
        topo = stack.pop()
        n = int(topo.replace("fatorial(", "").replace(")", ""))
        val = valores[n]
        print(f"  ⬆ [POP]  Resolvido: {bold(green(topo))} = {bold(yellow(str(val)))} | Pilha restante: {dim(' -> '.join(stack) if stack else '[Vazia]')}")
        time.sleep(0.3)

    print(bold(green("\nResultado final retornado para o escopo global: 6")))
    print(dim("Lição: se você esquecer o 'if (n <= 1) return 1', o empilhamento nunca para e causa 'Maximum call stack size exceeded'."))


def simular_referencia_vs_copia():
    print("\n" + bold(cyan("=== SIMULAÇÃO 3: PONTEIROS DE MEMÓRIA (REFERÊNCIA VS CÓPIA) ===")))
    print(dim("Código analisado:"))
    codigo = """const original = [1, 2];
const atribuicao = original;           // Copia o ponteiro (mesmo endereço)
const copiaReal  = [...original];       // Cria nova região na memória (Clone)

atribuicao.push(99);"""
    print(yellow(codigo) + "\n")

    print(bold("Mapa da Memória (Heap vs Stack):"))
    print(f"  Endereço #0x100: [1, 2]")
    print(f"  • variável 'original'   aponta para -> {cyan('#0x100')}")
    print(f"  • variável 'atribuicao' aponta para -> {cyan('#0x100')} (mesmo ponteiro!)")
    print(f"  • variável 'copiaReal'  aponta para -> {green('#0x200')} (nova região isolada)")

    print("\n" + bold(yellow("Após executar: atribuicao.push(99)")))
    print(f"  Endereço #0x100 modificado: [1, 2, 99]")
    print(f"  • original:   {red('[1, 2, 99]')} (foi mutado sem você chamar original.push!)")
    print(f"  • atribuicao: {red('[1, 2, 99]')}")
    print(f"  • copiaReal:  {green('[1, 2]')}      (permaneceu protegido e intacto)")


def start_inspector_session():
    while True:
        print("\n" + bold(magenta("==========================================================")))
        print(bold(magenta("   👁️ VISUALIZADOR DE MEMÓRIA: MODELOS MENTAIS REAIS 👁️   ")))
        print(bold(magenta("==========================================================")))
        print(dim("Escolha um mecanismo de execução para visualizar passo a passo no terminal:\n"))

        print(f" {bold(cyan('1.'))} 🔄 Laço Acumulador (Tabela de evolução de variáveis)")
        print(f" {bold(cyan('2.'))} 🥞 Call Stack Recursiva (Empilhamento e desempilhamento)")
        print(f" {bold(cyan('3.'))} 🎯 Ponteiros de Memória (Referência vs Cópia independente)")
        print(f" {bold(cyan('0.'))} ⬅️ Voltar ao menu principal\n")

        escolha = input(bold("Escolha uma simulação > ")).strip()

        if escolha == "1":
            simular_loop_acumulador()
        elif escolha == "2":
            simular_call_stack_recursiva()
        elif escolha == "3":
            simular_referencia_vs_copia()
        elif escolha in ("0", "voltar", "sair"):
            break
        else:
            print(red("Opção inválida."))

        input(dim("\nPressione ENTER para continuar..."))
