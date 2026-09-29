"""CLI principal do Code Sensei."""
import sys
import argparse
from sensei.colors import bold, green, red, yellow, cyan, dim, magenta
from sensei import socratic
from sensei import runner
from sensei import journal
from sensei import hints
from sensei import tracer
from sensei import hunt
from sensei import decoder
from sensei import inspector
from sensei import anki



def show_banner():
    track = runner.get_current_track()
    track_name = "JavaScript / TypeScript / Node.js" if track == "js_ts" else "Python"
    banner = f"""
{bold(cyan("=========================================================="))}
{bold(yellow("           🥋 CODE SENSEI: SEU MENTOR ANTI-IA 🥋           "))}
{bold(cyan("=========================================================="))}
{dim("  Aprenda a programar de verdade com modelo mental e sem atalhos")}
  Trilha atual: {bold(green(track_name))}
"""
    print(banner)


def show_stats():
    show_banner()
    passed, failed = runner.check_progress()
    total = len(passed) + len(failed)
    entries = journal.list_entries()
    bosses = runner.get_boss_fights()
    bosses_passed = [b for b in bosses if runner.run_exercise_test(b)[0]]

    print(bold("📊 RESUMO DE PROGRESSO:\n"))
    print(f"- Exercícios Concluídos : {green(str(len(passed)))} / {total}")
    print(f"- Exercícios Pendentes  : {yellow(str(len(failed)))} / {total}")
    print(f"- Boss Fights Vencidos  : {magenta(str(len(bosses_passed)))} / {len(bosses)}")
    print(f"- Lições no DevLog      : {cyan(str(len(entries)))}")

    if total > 0:
        pct = (len(passed) / total) * 100
        bar_len = 24
        filled = int(bar_len * (len(passed) / total))
        bar = green("█" * filled) + dim("░" * (bar_len - filled))
        print(f"\nProgresso Katas: [{bar}] {pct:.1f}%")

    if failed:
        print(f"\nPróximo foco: {bold(yellow(failed[0].name))}")
        print(dim("Execute 'python main.py watch' para começar a resolver!"))
    else:
        print(f"\n{bold(green('Todos os katas finalizados! Pratique os Boss Fights com python main.py boss.'))}")


def run_boss_checks():
    bosses = runner.get_boss_fights()
    if not bosses:
        print(yellow("Nenhum Boss Fight disponível nesta trilha."))
        return

    print("\n" + bold(magenta("=== 👹 BOSS FIGHTS (MARCOS DE PROJETO) 👹 ===")))
    print(dim("Mini-projetos aplicados que testam arquitetura e raciocínio real.\n"))

    for boss in bosses:
        ok, output = runner.run_exercise_test(boss)
        if ok:
            print(f" {green('✔ DERROTADO')} {bold(boss.name)}")
        else:
            print(f" {red('✖ VIVO')}      {bold(boss.name)}")
            print("\n" + runner.format_failure_message(boss, output))
            break


def switch_track_interactive():
    print("\n" + bold(cyan("=== SELECIONE A TRILHA DE ESTUDOS ===")))
    print(f" 1. {bold('JavaScript / TypeScript / Node.js')} (20 Níveis + 4 Boss Fights)")
    print(f" 2. {bold('Python')} (6 Níveis)")
    op = input(bold("\nEscolha a trilha (1 ou 2) > ")).strip()
    if op == "1":
        runner.set_current_track("js_ts")
        print(green("✔ Trilha alterada para JavaScript / TypeScript / Node.js!"))
    elif op == "2":
        runner.set_current_track("python")
        print(green("✔ Trilha alterada para Python!"))
    else:
        print(yellow("Opção cancelada."))


def interactive_menu():
    while True:
        show_banner()
        print(bold("Escolha uma ação:\n"))
        print(f" {bold(cyan('1.'))} 🦆 {bold('Pato Socrático')} - Debugar um erro que está te travando")
        print(f" {bold(cyan('2.'))} 🥋 {bold('Katas Runner')} - Verificar os exercícios")
        print(f" {bold(cyan('3.'))} 👁️ {bold('Modo Watch')} - Monitorar exercícios em tempo real (com Auto-Commit)")
        print(f" {bold(cyan('4.'))} 🧠 {bold('Blind Trace')} - Treinar compilador mental (prever output sem rodar)")
        print(f" {bold(cyan('5.'))} 🔍 {bold('Caça-Bugs')} - Code review reverso (achar o bug lendo o código)")
        print(f" {bold(cyan('6.'))} 👹 {bold('Boss Fights')} - Mini-projetos marcos de arquitetura")
        print(f" {bold(cyan('7.'))} 🛠️ {bold('Decodificador')} - Traduzir erro críptico do terminal")
        print(f" {bold(cyan('8.'))} 🔬 {bold('Inspetor de Memória')} - Visualizar loops, call stack e ponteiros")
        print(f" {bold(cyan('9.'))} 📇 {bold('Exportar Anki')} - Gerar baralho de flashcards (.csv)")
        print(f" {bold(cyan('10.'))} 💡 {bold('Pedir Dica')} - Dicas em 3 níveis sem código pronto")
        print(f" {bold(cyan('11.'))} 📝 {bold('Novo DevLog')} - Registrar um erro e o que aprendeu")
        print(f" {bold(cyan('12.'))} 📚 {bold('Ver DevLogs')} - Listar seus aprendizados salvos")
        print(f" {bold(cyan('0.'))} 📊 {bold('Estatísticas')} - Ver seu progresso")
        print(f" {bold(cyan('T.'))} 🔄 {bold('Trocar Trilha')} - Alternar entre JS/TS/Node e Python")
        print(f" {bold(cyan('Q.'))} ❌ {dim('Sair')}\n")

        choice = input(bold("Opção > ")).strip()

        if choice == "1":
            socratic.start_session()
        elif choice == "2":
            runner.run_checks(stop_on_first=True)
        elif choice == "3":
            runner.watch_mode()
        elif choice == "4":
            tracer.start_trace_session()
        elif choice == "5":
            hunt.start_hunt_session()
        elif choice == "6":
            run_boss_checks()
        elif choice == "7" or choice.lower() in ("e", "erro", "error"):
            decoder.start_decoder_session()
        elif choice == "8" or choice.lower() in ("i", "inspect", "memoria"):
            inspector.start_inspector_session()
        elif choice == "9" or choice.lower() in ("a", "anki", "flashcards"):
            anki.start_anki_export()
        elif choice == "10":
            ex_name = input(bold("Nome do exercício (ou ENTER para atual pendente): ")).strip()
            if not ex_name:
                _, failed = runner.check_progress()
                ex_name = failed[0].name if failed else "01_primitives_coercion"
            lvl_str = input(bold("Nível da dica (1=Pergunta, 2=Pseudocódigo, 3=Doc): ")).strip()
            lvl = int(lvl_str) if lvl_str.isdigit() else 1
            print(hints.get_hint(ex_name, lvl))
        elif choice == "11":
            journal.create_entry_interactive()
        elif choice == "12":
            journal.show_summary()
        elif choice == "0":
            show_stats()
        elif choice.lower() in ("t", "trocar", "track"):
            switch_track_interactive()
        elif choice.lower() in ("q", "sair", "exit"):
            print(dim("\nAté a próxima sessão de código! Continue praticando."))
            break
        else:
            print(red("\nOpção inválida."))

        input(dim("\nPressione ENTER para voltar ao menu..."))


def main():
    parser = argparse.ArgumentParser(
        description="Code Sensei: Mentor pessoal para aprender a programar sem IA."
    )
    parser.add_argument(
        "--track",
        choices=["js_ts", "python"],
        help="Define a trilha ativa de estudos (js_ts ou python)"
    )
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("duck", help="Inicia sessão do Pato Socrático para debugar")
    subparsers.add_parser("train", help="Executa verificação dos Katas")
    subparsers.add_parser("watch", help="Modo observador em tempo real dos exercícios com Git Auto-commit")
    subparsers.add_parser("trace", help="Modo Blind Trace (flashcards mentais de código)")
    subparsers.add_parser("hunt", help="Modo Caça-Bugs (Code Review Reverso)")
    subparsers.add_parser("boss", help="Verifica e executa os Boss Fights")
    subparsers.add_parser("inspect", help="Visualizador de memória RAM e call stack")
    subparsers.add_parser("anki", help="Exporta baralho Anki com 20 modelos mentais")
    subparsers.add_parser("log", help="Cria nova entrada no DevLog")
    subparsers.add_parser("logs", help="Lista entradas do DevLog")
    subparsers.add_parser("stats", help="Exibe estatísticas de progresso")

    err_parser = subparsers.add_parser("error", help="Decodifica erro críptico do terminal")
    err_parser.add_argument("message", nargs="*", default=[], help="Texto do erro para decodificar")

    hint_parser = subparsers.add_parser("hint", help="Obtém dica progressiva (1=Pergunta, 2=Estrutura, 3=Doc)")
    hint_parser.add_argument("exercise", nargs="?", default="", help="Nome do exercício")
    hint_parser.add_argument("level", nargs="?", type=int, default=1, help="Nível da dica (1, 2 ou 3)")

    args = parser.parse_args()

    if args.track:
        runner.set_current_track(args.track)
        print(green(f"✔ Trilha ativa configurada para: {args.track}"))

    if not args.command:
        interactive_menu()
    elif args.command == "duck":
        socratic.start_session()
    elif args.command == "train":
        runner.run_checks(stop_on_first=True)
    elif args.command == "watch":
        runner.watch_mode()
    elif args.command == "trace":
        tracer.start_trace_session()
    elif args.command == "hunt":
        hunt.start_hunt_session()
    elif args.command == "boss":
        run_boss_checks()
    elif args.command == "error":
        if args.message:
            msg = " ".join(args.message)
            res = decoder.decode_error(msg)
            if res:
                decoder.show_decoded_result(res)
            else:
                print(yellow("Padrão não reconhecido automaticamente. Abrindo decodificador interativo..."))
                decoder.start_decoder_session()
        else:
            decoder.start_decoder_session()
    elif args.command == "inspect":
        inspector.start_inspector_session()
    elif args.command == "anki":
        anki.start_anki_export()
    elif args.command == "hint":
        ex_name = args.exercise
        if not ex_name:
            _, failed = runner.check_progress()
            ex_name = failed[0].name if failed else "01_primitives_coercion"
        print(hints.get_hint(ex_name, args.level))
    elif args.command == "log":
        journal.create_entry_interactive()
    elif args.command == "logs":
        journal.show_summary()
    elif args.command == "stats":
        show_stats()


if __name__ == "__main__":
    main()
