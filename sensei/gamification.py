"""Motor de Gamificação RPG, Skill Tree e Streaks Offline do Code Sensei."""
import os
import subprocess
from datetime import datetime, date, timedelta
from pathlib import Path
from sensei.colors import bold, cyan, green, yellow, red, dim, magenta
from sensei import runner
from sensei import journal

BRANCHES = [
    {
        "name": "RAMO I: FUNDAMENTOS & LÓGICA ESTRITA",
        "description": "Controle de fluxo, coerção de tipos, laços e closures.",
        "boss": "boss_01_cli_task_manager",
        "boss_title": "BOSS 1: Gerenciador de Tarefas em Memória",
        "katas": [
            ("01_primitives_coercion", "Coerção & Formatação"),
            ("02_conditionals_branching", "Condicionais & Branches"),
            ("03_loops_accumulators", "Loops & Acumuladores"),
            ("04_array_basics", "Arrays & Extremos sem Math"),
            ("05_functions_closures", "Closures & Memoização")
        ]
    },
    {
        "name": "RAMO II: MODELAGEM & ESTRUTURAS DE DADOS",
        "description": "Objetos, tipagem estrita com TypeScript e coleções funcionais.",
        "boss": "boss_02_csv_financial_analyzer",
        "boss_title": "BOSS 2: Analisador Financeiro de CSV",
        "katas": [
            ("06_objects_destructuring", "Projeção & Spread Seguro"),
            ("07_ts_basic_interfaces", "TypeScript Interfaces"),
            ("08_ts_unions_narrowing", "Unions & Narrowing"),
            ("09_array_methods_map_filter", "Map, Filter & Pureza"),
            ("10_array_methods_reduce", "Reduce & Histogramas")
        ]
    },
    {
        "name": "RAMO III: CONTROLE AVANÇADO & ASSINCRONISMO",
        "description": "Sets/Maps O(1), erros customizados, Generics e Promises.",
        "boss": "boss_03_resilient_api_crawler",
        "boss_title": "BOSS 3: Crawler Resiliente com Retries",
        "katas": [
            ("11_sets_and_maps", "Sets & Maps O(1)"),
            ("12_error_handling_custom", "Erros Customizados & JSON"),
            ("13_ts_generics", "Fila FIFO & Generics"),
            ("14_async_promises_basics", "Promises & Timeouts"),
            ("15_async_await_flow", "Async/Await Sequencial")
        ]
    },
    {
        "name": "RAMO IV: ARQUITETURA, EVENTOS & ALGORITMOS DE ELITE",
        "description": "Concorrência controlada, Streams/I/O, Debugging Reverso e LRU.",
        "boss": "boss_04_in_memory_kv_store",
        "boss_title": "BOSS FINAL: Mini Banco KV com Cache LRU",
        "katas": [
            ("16_async_concurrency_limit", "Pool de Concorrência"),
            ("17_node_path_fs", "Arquivos Atômicos com FS"),
            ("18_node_events_streams", "Eventos & Streams"),
            ("19_mental_trace_real_bugs", "Caça aos Bugs Reais"),
            ("20_lru_cache_algorithm", "Cache LRU O(1)")
        ]
    }
]

RANKS = [
    {
        "name": "Faixa Branca (Iniciante)",
        "color": "white",
        "min_katas": 0,
        "min_bosses": 0,
        "symbol": "🥋 [BRANCA]",
        "desc": "Iniciando a jornada da Notional Machine. Dominando sintaxe e controle de fluxo."
    },
    {
        "name": "Faixa Amarela (Praticante)",
        "color": "yellow",
        "min_katas": 5,
        "min_bosses": 1,
        "symbol": "🥋 [AMARELA]",
        "desc": "Fundamentos consolidados. Capaz de criar mini-aplicações em memória."
    },
    {
        "name": "Faixa Laranja (Ascendente)",
        "color": "yellow",
        "min_katas": 10,
        "min_bosses": 2,
        "symbol": "🥋 [LARANJA]",
        "desc": "Modelagem de dados e tipagem estrita com TypeScript afiadas."
    },
    {
        "name": "Faixa Verde (Arquiteto)",
        "color": "green",
        "min_katas": 15,
        "min_bosses": 3,
        "symbol": "🥋 [VERDE]",
        "desc": "Mestre do assincronismo, Generics e controle de exceções."
    },
    {
        "name": "Faixa Marrom (Graduado)",
        "color": "magenta",
        "min_katas": 20,
        "min_bosses": 3,
        "symbol": "🥋 [MARROM]",
        "desc": "Todos os 20 katas dominados. Pronto para o Chefão Final."
    },
    {
        "name": "Faixa Preta (Code Sensei)",
        "color": "cyan",
        "min_katas": 20,
        "min_bosses": 4,
        "symbol": "🥋 [PRETA - MESTRE]",
        "desc": "Maestria completa: 20 katas, 4 Bosses e mentalidade anti-IA consolidada!"
    }
]


def get_study_dates_from_git() -> set[date]:
    dates = set()
    try:
        proc = subprocess.run(
            ["git", "log", "--format=%cd", "--date=short"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if proc.returncode == 0:
            for line in proc.stdout.strip().splitlines():
                line = line.strip()
                if line:
                    try:
                        d = datetime.strptime(line, "%Y-%m-%d").date()
                        dates.add(d)
                    except ValueError:
                        pass
    except Exception:
        pass
    return dates


def get_study_dates_from_devlogs() -> set[date]:
    dates = set()
    devlog_dir = Path("devlog")
    if devlog_dir.exists():
        for file in devlog_dir.glob("*.md"):
            stem = file.stem
            # Verifica se o arquivo começa com YYYY-MM-DD
            if len(stem) >= 10:
                try:
                    d = datetime.strptime(stem[:10], "%Y-%m-%d").date()
                    dates.add(d)
                except ValueError:
                    pass
    return dates


def calculate_streaks() -> tuple[int, int, int]:
    all_dates = get_study_dates_from_git() | get_study_dates_from_devlogs()
    if not all_dates:
        # Se não houver histórico, conta hoje como ativo caso tenha rodado
        return (1, 1, 1)

    sorted_dates = sorted(all_dates)
    total_days = len(sorted_dates)

    # Streak atual
    today = date.today()
    yesterday = today - timedelta(days=1)

    current_streak = 0
    ref_date = today if today in all_dates else (yesterday if yesterday in all_dates else None)

    if ref_date:
        current_streak = 1
        curr = ref_date
        while True:
            prev = curr - timedelta(days=1)
            if prev in all_dates:
                current_streak += 1
                curr = prev
            else:
                break

    # Maior streak da história
    longest_streak = 1
    temp_streak = 1
    for i in range(1, len(sorted_dates)):
        if sorted_dates[i] - sorted_dates[i - 1] == timedelta(days=1):
            temp_streak += 1
            if temp_streak > longest_streak:
                longest_streak = temp_streak
        else:
            temp_streak = 1

    return current_streak, max(current_streak, longest_streak), total_days


def calculate_player_profile():
    passed_exercises, failed_exercises = runner.check_progress()
    passed_names = {p.name for p in passed_exercises}

    bosses = runner.get_boss_fights()
    bosses_passed = {b.name for b in bosses if runner.run_exercise_test(b)[0]}

    entries = journal.list_entries()
    katas_count = len(passed_names)
    bosses_count = len(bosses_passed)
    devlogs_count = len(entries)

    # Cálculo de XP
    xp = (katas_count * 50) + (bosses_count * 100) + (min(devlogs_count, 10) * 30)

    # Determinação da Faixa Marcial
    current_rank = RANKS[0]
    next_rank = RANKS[1]

    for i in range(len(RANKS) - 1, -1, -1):
        r = RANKS[i]
        if katas_count >= r["min_katas"] and bosses_count >= r["min_bosses"]:
            current_rank = r
            next_rank = RANKS[i + 1] if i + 1 < len(RANKS) else None
            break

    current_streak, longest_streak, total_days = calculate_streaks()

    return {
        "katas_done": katas_count,
        "katas_total": katas_count + len(failed_exercises),
        "passed_names": passed_names,
        "bosses_done": bosses_count,
        "bosses_total": len(bosses),
        "bosses_passed": bosses_passed,
        "devlogs_count": devlogs_count,
        "xp": xp,
        "rank": current_rank,
        "next_rank": next_rank,
        "current_streak": current_streak,
        "longest_streak": longest_streak,
        "total_days": total_days,
        "next_target": failed_exercises[0].name if failed_exercises else None
    }


def show_skill_tree():
    profile = calculate_player_profile()
    passed_names = profile["passed_names"]
    bosses_passed = profile["bosses_passed"]
    next_target = profile["next_target"]

    print("\n" + bold(magenta("==========================================================")))
    print(bold(magenta("     🌳 ÁRVORE DE HABILIDADES RPG DO CODE SENSEI 🌳       ")))
    print(bold(magenta("==========================================================")))

    # Banner do Jogador
    rank = profile["rank"]
    symbol = bold(cyan(rank["symbol"]) if rank["color"] == "cyan" else (green(rank["symbol"]) if rank["color"] == "green" else yellow(rank["symbol"])))
    print(f"\n Graduação Atual : {symbol} {bold(rank['name'])}")
    print(f" Filosofia        : {dim(rank['desc'])}")
    print(f" Pontos de XP     : {bold(green(str(profile['xp']) + ' XP'))}")
    print(f" Sequência Ativa  : {bold(yellow('🔥 ' + str(profile['current_streak']) + ' dias seguidos'))} (Recorde: {profile['longest_streak']} dias | {profile['total_days']} dias totais)\n")

    # Renderiza os 4 ramos
    print(bold("--- RAMOS DE CONHECIMENTO TÉCNICO ---"))

    for branch in BRANCHES:
        print("\n" + bold(cyan(branch["name"])))
        print(f" {dim(branch['description'])}")

        for code, label in branch["katas"]:
            if code in passed_names:
                badge = green("  [✔] ")
                title = green(label)
            elif code == next_target:
                badge = bold(yellow("  [⚡] "))
                title = bold(yellow(f"{label} <-- [ALVO ATUAL]"))
            else:
                badge = dim("  [🔒] ")
                title = dim(label)

            print(f"{badge}{bold(code)}: {title}")

        # Status do Boss do Ramo
        boss_key = branch["boss"]
        boss_label = branch["boss_title"]
        if boss_key in bosses_passed:
            print(f"{green('  🏆 [DERROTADO] ')}{bold(green(boss_label))}")
        else:
            print(f"{red('  👹 [A DESAFIAR] ')}{dim(boss_label)}")

    print("\n" + bold(cyan("==========================================================")))
    if profile["next_rank"]:
        req_k = profile["next_rank"]["min_katas"]
        req_b = profile["next_rank"]["min_bosses"]
        print(bold(yellow(f"Próxima Graduação: {profile['next_rank']['name']}")))
        print(dim(f"Requisitos: {req_k} Katas concluídos e {req_b} Bosses derrotados."))
    else:
        print(bold(green("🏆 Parabéns! Você atingiu o nível mais alto: FAIXA PRETA - CODE SENSEI!")))

    print(dim("Para avançar na árvore, execute: ") + bold(cyan("python main.py watch\n")))
