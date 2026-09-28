"""CLI principal do Code Sensei."""
import sys
import argparse
from sensei.colors import bold, green, red, yellow, cyan, dim, magenta
from sensei import socratic
from sensei import runner
from sensei import journal


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

    print(bold("📊 RESUMO DE PROGRESSO:\n"))
    print(f"- Exercícios Concluídos : {green(str(len(passed)))} / {total}")
    print(f"- Exercícios Pendentes  : {yellow(str(len(failed)))} / {total}")
    print(f"- Lições no DevLog      : {magenta(str(len(entries)))}")

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
        print(f"\n{bold(green('Todos os katas finalizados! Adicione novos ou pratique debug.'))}")


def switch_track_interactive():
    print("\n" + bold(cyan("=== SELECIONE A TRILHA DE ESTUDOS ===")))
    print(f" 1. {bold('JavaScript / TypeScript / Node.js')}")
    print(f" 2. {bold('Python')}")
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
        print(f" {bold(cyan('3.'))} 👁️ {bold('Modo Watch')} - Monitorar exercícios em tempo real enquanto digita")
        print(f" {bold(cyan('4.'))} 📝 {bold('Novo DevLog')} - Registrar um erro e o que aprendeu")
        print(f" {bold(cyan('5.'))} 📚 {bold('Ver DevLogs')} - Listar seus aprendizados salvos")
        print(f" {bold(cyan('6.'))} 📊 {bold('Estatísticas')} - Ver seu progresso")
        print(f" {bold(cyan('7.'))} 🔄 {bold('Trocar Trilha')} - Alternar entre JS/TS/Node e Python")
        print(f" {bold(cyan('0.'))} ❌ {dim('Sair')}\n")

        choice = input(bold("Opção > ")).strip()

        if choice == "1":
            socratic.start_session()
        elif choice == "2":
            runner.run_checks(stop_on_first=True)
        elif choice == "3":
            runner.watch_mode()
        elif choice == "4":
            journal.create_entry_interactive()
        elif choice == "5":
            journal.show_summary()
        elif choice == "6":
            show_stats()
        elif choice == "7":
            switch_track_interactive()
        elif choice in ("0", "sair", "exit", "q"):
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
    subparsers.add_parser("watch", help="Modo observador em tempo real dos exercícios")
    subparsers.add_parser("log", help="Cria nova entrada no DevLog")
    subparsers.add_parser("logs", help="Lista entradas do DevLog")
    subparsers.add_parser("stats", help="Exibe estatísticas de progresso")

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
    elif args.command == "log":
        journal.create_entry_interactive()
    elif args.command == "logs":
        journal.show_summary()
    elif args.command == "stats":
        show_stats()


if __name__ == "__main__":
    main()
