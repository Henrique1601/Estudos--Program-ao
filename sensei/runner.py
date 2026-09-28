"""Runner de Katas: avaliador progressivo com Anti-Cheat, Git Auto-commit e Suporte Multi-Track."""
import os
import sys
import subprocess
import time
import json
from pathlib import Path
from sensei.colors import bold, green, red, yellow, cyan, dim, magenta
from sensei import linter
from sensei import hints

CONFIG_FILE = Path(".sensei_config.json")
EXERCISES_ROOT = Path("exercises")


def get_current_track() -> str:
    if CONFIG_FILE.exists():
        try:
            data = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
            return data.get("current_track", "js_ts")
        except Exception:
            pass
    return "js_ts"


def set_current_track(track: str) -> None:
    data = {}
    if CONFIG_FILE.exists():
        try:
            data = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    data["current_track"] = track
    CONFIG_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")


def get_track_dir() -> Path:
    track = get_current_track()
    track_dir = EXERCISES_ROOT / track
    if track_dir.exists():
        return track_dir
    return EXERCISES_ROOT


def get_all_exercises(include_bosses: bool = False) -> list[Path]:
    track_dir = get_track_dir()
    if not track_dir.exists():
        return []

    exercises = []
    for p in track_dir.iterdir():
        if p.is_dir() and p.name != "boss_fights":
            if (p / "exercise.ts").exists() or (p / "exercise.js").exists() or (p / "exercise.py").exists():
                exercises.append(p)

    if include_bosses:
        boss_dir = track_dir / "boss_fights"
        if boss_dir.exists():
            for p in boss_dir.iterdir():
                if p.is_dir() and ((p / "exercise.ts").exists() or (p / "exercise.js").exists()):
                    exercises.append(p)

    return sorted(exercises, key=lambda p: p.name)


def get_boss_fights() -> list[Path]:
    track_dir = get_track_dir()
    boss_dir = track_dir / "boss_fights"
    if not boss_dir.exists():
        return []
    bosses = [
        p for p in boss_dir.iterdir()
        if p.is_dir() and ((p / "exercise.ts").exists() or (p / "exercise.js").exists())
    ]
    return sorted(bosses, key=lambda p: p.name)


def run_exercise_test(exercise_dir: Path) -> tuple[bool, str]:
    # 1. Checagem Anti-Cheat prévia
    linter_ok, linter_msg = linter.check_anti_cheat(exercise_dir)
    if not linter_ok:
        return False, linter_msg

    # 2. Execução dos Testes
    ts_test = exercise_dir / "test_exercise.ts"
    js_test = exercise_dir / "test_exercise.js"
    py_test = exercise_dir / "test_exercise.py"

    if ts_test.exists() or js_test.exists():
        test_file = ts_test if ts_test.exists() else js_test
        result = subprocess.run(
            ["node", "--experimental-strip-types", "--test", test_file.name],
            cwd=exercise_dir,
            capture_output=True,
            text=True
        )
        passed = (result.returncode == 0)
        output = result.stderr if result.stderr else result.stdout
        return passed, output

    elif py_test.exists():
        env = os.environ.copy()
        env["PYTHONPATH"] = str(exercise_dir.resolve()) + os.pathsep + env.get("PYTHONPATH", "")
        result = subprocess.run(
            [sys.executable, "-m", "unittest", py_test.name],
            cwd=exercise_dir,
            capture_output=True,
            text=True,
            env=env
        )
        passed = (result.returncode == 0)
        output = result.stderr if result.stderr else result.stdout
        return passed, output

    return False, f"Nenhum arquivo de teste encontrado em {exercise_dir}"


def format_failure_message(exercise_dir: Path, output: str) -> str:
    readme_path = exercise_dir / "README.md"
    doc_link = ""

    if readme_path.exists():
        content = readme_path.read_text(encoding="utf-8")
        lines = content.splitlines()
        for idx, line in enumerate(lines):
            if "Documentação oficial" in line or "Doc:" in line:
                if idx + 1 < len(lines) and lines[idx + 1].strip().startswith("http"):
                    doc_link = f"Documentação oficial: {lines[idx + 1].strip()}"
                elif "http" in line:
                    doc_link = line.strip()
                break
            elif line.strip().startswith("http"):
                doc_link = f"Documentação oficial: {line.strip()}"
                break

    clean_lines = []
    for line in output.splitlines():
        if any(keyword in line for keyword in ["✖", "FAIL", "AssertionError", "TypeError", "SyntaxError", "Error:", "assert.", "BLOQUEIO DO ANTI-CHEAT"]):
            clean_lines.append(line)
        elif "expected" in line.lower() or "actual" in line.lower():
            clean_lines.append(line)

    filtered_output = "\n".join(clean_lines[:10]) if clean_lines else output[:400]

    code_file = (
        exercise_dir / "exercise.ts" if (exercise_dir / "exercise.ts").exists()
        else (exercise_dir / "exercise.js" if (exercise_dir / "exercise.js").exists()
        else exercise_dir / "exercise.py")
    )

    msg = [
        bold(red(f"❌ Exercício com pendência: {exercise_dir.name}")),
        dim(f"Arquivo para editar: {code_file}"),
        "\n" + bold(yellow("Saída do Teste / Linter:")),
        filtered_output,
    ]
    if doc_link:
        msg.append("\n" + bold(cyan("📚 ") + doc_link))

    msg.append(dim(f"\nTravou? Digite 'python main.py hint {exercise_dir.name} 1' para uma dica socrática."))
    return "\n".join(msg)


def check_progress() -> tuple[list[Path], list[Path]]:
    exercises = get_all_exercises(include_bosses=False)
    passed = []
    failed = []

    for ex in exercises:
        ok, _ = run_exercise_test(ex)
        if ok:
            passed.append(ex)
        else:
            failed.append(ex)

    return passed, failed


def run_checks(stop_on_first: bool = True) -> bool:
    exercises = get_all_exercises(include_bosses=False)
    track = get_current_track()
    track_name = "JavaScript / TypeScript / Node.js" if track == "js_ts" else "Python"

    if not exercises:
        print(red(f"Nenhum exercício encontrado para a trilha '{track}'."))
        return False

    print("\n" + bold(cyan("=== CODE SENSEI: KATAS RUNNER ===")))
    print(bold(f"Trilha Ativa: {yellow(track_name)}"))
    print(dim("Treinamento sem IA: escreva à mão, rode os testes e aprenda com a doc.\n"))

    all_passed = True
    for ex in exercises:
        ok, output = run_exercise_test(ex)
        if ok:
            print(f" {green('✔ PASS')} {bold(ex.name)}")
        else:
            all_passed = False
            print(f" {red('✖ FAIL')} {bold(ex.name)}")
            if stop_on_first:
                print("\n" + format_failure_message(ex, output))
                print("\n" + yellow("Foco deliberado: resolva o exercício acima antes de avançar."))
                return False

    if all_passed:
        print("\n" + bold(green("🎉 PARABÉNS! Todos os 20 exercícios concluídos com sucesso!")))
        print(dim("Pronto para os Boss Fights? Execute 'python main.py boss'."))
    return all_passed


def auto_git_commit(exercise_dir: Path):
    try:
        # Adiciona o diretório do exercício resolvido
        subprocess.run(["git", "add", str(exercise_dir)], capture_output=True, text=True)
        commit_msg = f"feat(kata): resolve nivel {exercise_dir.name}"
        res = subprocess.run(["git", "commit", "-m", commit_msg], capture_output=True, text=True)
        if res.returncode == 0:
            print(bold(green(f"🚀 [Git Auto-Commit] Progresso salvo: '{commit_msg}'")))
    except Exception:
        pass


def watch_mode():
    exercises = get_all_exercises(include_bosses=False)
    track = get_current_track()
    track_name = "JavaScript / TypeScript / Node.js" if track == "js_ts" else "Python"

    if not exercises:
        print(red("Nenhum exercício para monitorar."))
        return

    print("\n" + bold(magenta("=== MODO OBSERVADOR ATIVO (WATCH MODE) ===")))
    print(bold(f"Trilha Ativa: {yellow(track_name)}"))
    print(dim("O Code Sensei está monitorando seus arquivos. Edite e salve para retestar na hora.\nPressione Ctrl+C para sair.\n"))

    last_mtimes = {}
    failing_exercises = set()

    # Identifica estado inicial de falhas
    for ex in exercises:
        ok, _ = run_exercise_test(ex)
        if not ok:
            failing_exercises.add(str(ex))

    def get_max_mtime(ex_dir: Path) -> float:
        mtimes = [p.stat().st_mtime for p in ex_dir.glob("*.*") if p.suffix in [".ts", ".js", ".py"]]
        return max(mtimes) if mtimes else 0

    run_checks(stop_on_first=True)

    try:
        while True:
            time.sleep(1.0)
            exercises = get_all_exercises(include_bosses=False)
            current_target = None
            for ex in exercises:
                ok, _ = run_exercise_test(ex)
                if not ok:
                    current_target = ex
                    break

            if not current_target:
                continue

            current_mtime = get_max_mtime(current_target)
            old_mtime = last_mtimes.get(str(current_target), 0)

            if current_mtime > old_mtime:
                last_mtimes[str(current_target)] = current_mtime
                print("\n" + dim(f"[{time.strftime('%H:%M:%S')}] Modificação detectada! Analisando com Anti-Cheat & Testes..."))

                ok, output = run_exercise_test(current_target)
                if ok:
                    print("\n" + bold(green(f"✔ PARABÉNS! {current_target.name} CONCLUÍDO COM SUCESSO!")))
                    if str(current_target) in failing_exercises:
                        failing_exercises.remove(str(current_target))
                        auto_git_commit(current_target)

                    run_checks(stop_on_first=True)
                else:
                    print("\n" + format_failure_message(current_target, output))

    except KeyboardInterrupt:
        print("\n" + dim("Modo observador finalizado."))
