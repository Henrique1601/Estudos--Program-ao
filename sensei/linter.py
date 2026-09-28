"""Anti-Cheat Linter: Análise estática para impedir atalhos mágicos nos katas."""
import re
from pathlib import Path
from sensei.colors import bold, red, yellow, dim

FORBIDDEN_RULES = {
    "04_array_basics": [
        (r"Math\.(min|max)\b", "Uso proibido de Math.min ou Math.max! Implemente a busca de extremos manualmente com laços para exercitar o raciocínio algorítmico.")
    ],
    "03_loops_accumulators": [
        (r"\.reduce\b", "Uso de .reduce() bloqueado neste nível! Use laços for ou while tradicionais para treinar mutação de estado e acumuladores.")
    ],
    "11_sets_and_maps": [
        (r"\.indexOf\b|\.includes\b", "Aviso de performance: use a busca em O(1) do Set (.has()) em vez de varrer arrays com .includes() ou .indexOf().")
    ]
}


def check_anti_cheat(exercise_dir: Path) -> tuple[bool, str]:
    """
    Verifica se o arquivo de exercício do aluno viola alguma restrição pedagógica.
    Retorna (True, "") se estiver limpo, ou (False, "motivo") se violou.
    """
    code_file = None
    for ext in [".ts", ".js", ".py"]:
        candidate = exercise_dir / f"exercise{ext}"
        if candidate.exists():
            code_file = candidate
            break

    if not code_file:
        return True, ""

    exercise_name = exercise_dir.name
    rules = []
    for pattern_key, rule_list in FORBIDDEN_RULES.items():
        if pattern_key in exercise_name:
            rules.extend(rule_list)

    if not rules:
        return True, ""

    try:
        content = code_file.read_text(encoding="utf-8")
    except Exception:
        return True, ""

    # Remove comentários para não acusar falsos positivos
    clean_code = re.sub(r"//.*", "", content)
    clean_code = re.sub(r"/\*[\s\S]*?\*/", "", clean_code)
    clean_code = re.sub(r"#.*", "", clean_code)

    for pattern, message in rules:
        if re.search(pattern, clean_code):
            error_msg = [
                bold(red("⚠️ BLOQUEIO DO ANTI-CHEAT LINTER ⚠️")),
                dim(f"Arquivo analisado: {code_file}"),
                yellow(f"\nMotivo: {message}"),
                dim("\nRemova o atalho proibido e escreva a lógica na mão para que o teste seja liberado.")
            ]
            return False, "\n".join(error_msg)

    return True, ""
