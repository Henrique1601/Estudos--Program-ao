"""DevLog Metacognitivo: diário para registrar gaps de modelo mental e bugs difíceis."""
from datetime import datetime
from pathlib import Path
import re
from sensei.colors import bold, green, cyan, yellow, dim, badge

DEVLOG_DIR = Path("devlog")

ENTRY_TEMPLATE = """# DevLog: {title}
Data: {date}
Tags: {tags}

---

### 1. Sintoma Observado (O que deu errado?)
{symptom}

### 2. Comportamento Esperado vs Real
- **Esperava**: {expected}
- **Ocorreu**: {actual}

### 3. Modelo Mental Incorreto (O que eu assumi errado sobre a linguagem/runtime?)
{mental_gap}

### 4. Causa Raiz Real
{root_cause}

### 5. Regra Pessoal de Prevenção (Como nunca mais cair nisso?)
{prevention}
"""


def ensure_devlog_dir() -> Path:
    DEVLOG_DIR.mkdir(parents=True, exist_ok=True)
    return DEVLOG_DIR


def create_entry_interactive() -> Path:
    ensure_devlog_dir()
    print("\n" + bold(cyan("=== NOVO REGISTRO NO DEVLOG METACOGNITIVO ===")))
    print(dim("Treine seu cérebro registrando o que você assumiu errado.\n"))

    title = input(bold("Título do problema / bug: ")).strip()
    if not title:
        title = "Bug sem título"

    tags_input = input(bold("Tags (ex: python, loops, arrays, tipos) [separadas por vírgula]: ")).strip()
    tags = [t.strip() for t in tags_input.split(",") if t.strip()] or ["geral"]

    print("\n" + yellow("1. Qual foi o sintoma visível? (mensagem de erro, saída esquisita, loop infinito)"))
    symptom = input("> ").strip() or "Não especificado"

    print("\n" + yellow("2. O que você esperava que o código fizesse?"))
    expected = input("> ").strip() or "Não especificado"

    print("\n" + yellow("3. O que realmente aconteceu?"))
    actual = input("> ").strip() or "Não especificado"

    print("\n" + yellow("4. MODELO MENTAL: O que você acreditava que a linguagem/função fazia que NÃO era verdade?"))
    print(dim("   Ex: 'Achei que list.append() retornava a nova lista', 'Achei que dict preservava tipagem'"))
    mental_gap = input("> ").strip() or "Não analisado"

    print("\n" + yellow("5. Qual foi a causa raiz real quando você descobriu?"))
    root_cause = input("> ").strip() or "Não analisada"

    print("\n" + yellow("6. Como você vai prevenir isso no futuro? (teste unitário, print de tipo, asserção)"))
    prevention = input("> ").strip() or "Atenção redobrada"

    now = datetime.now()
    safe_title = re.sub(r"[^\w\-_]", "_", title.lower())[:30]
    filename = f"{now.strftime('%Y-%m-%d')}_{safe_title}.md"
    file_path = DEVLOG_DIR / filename

    content = ENTRY_TEMPLATE.format(
        title=title,
        date=now.strftime("%Y-%m-%d %H:%M:%S"),
        tags=", ".join(tags),
        symptom=symptom,
        expected=expected,
        actual=actual,
        mental_gap=mental_gap,
        root_cause=root_cause,
        prevention=prevention,
    )

    file_path.write_text(content, encoding="utf-8")
    print("\n" + green(f"✔ DevLog salvo com sucesso em: {file_path}"))
    return file_path


def list_entries() -> list[Path]:
    if not DEVLOG_DIR.exists():
        return []
    return sorted(DEVLOG_DIR.glob("*.md"), reverse=True)


def show_summary():
    entries = list_entries()
    print("\n" + bold(cyan("=== DEVLOGS REGISTRADOS ===")))
    if not entries:
        print(dim("Nenhum registro ainda. Use 'python main.py log' para registrar aprendizados."))
        return

    print(f"Total de lições registradas: {bold(str(len(entries)))}\n")
    for idx, path in enumerate(entries, 1):
        content = path.read_text(encoding="utf-8", errors="ignore")
        lines = content.splitlines()
        first_line = lines[0].replace("# DevLog: ", "").strip() if lines else path.stem
        date_line = [l for l in lines if l.startswith("Data: ")]
        date_str = date_line[0].replace("Data: ", "").strip() if date_line else "Data desconhecida"
        print(f" {cyan(str(idx).rjust(2))}. {bold(first_line)} {dim(f'({date_str})')}")
        print(f"     {dim(str(path))}")
