"""Módulo Pato Socrático: Depurador Metodológico Anti-IA."""
from sensei.colors import bold, green, cyan, yellow, dim, magenta, red
from sensei.journal import ensure_devlog_dir, ENTRY_TEMPLATE
from datetime import datetime
import re

STAGES = [
    {
        "num": 1,
        "title": "Delimitar a Discrepância",
        "intro": "Nunca tente consertar sem saber exatamente a distância entre o esperado e o observado.",
        "questions": [
            ("Qual é a entrada exata fornecida ao código?", "input_val"),
            ("Qual é a saída OU erro exato que aconteceu? (Cole a mensagem ou valor)", "actual"),
            ("Qual saída você esperava receber para essa mesma entrada?", "expected"),
        ]
    },
    {
        "num": 2,
        "title": "Isolamento da Linha de Divergência",
        "intro": "Um programa é uma linha do tempo. Em que momento exato o estado real divergiu da sua expectativa?",
        "questions": [
            ("Qual arquivo, função ou bloco de código você suspeita?", "location"),
            ("Você já colocou um print() ou usou debugger exatamente ANTES desse ponto? (Sim/Não e detalhes)", "inspected_before"),
        ]
    },
    {
        "num": 3,
        "title": "Inspeção do Estado Real (Fatos vs Suposições)",
        "intro": "IA falha em adivinhar estado. Você precisa ver o estado impresso com seus próprios olhos.",
        "questions": [
            ("Quais são as variáveis ativas nessa linha e quais os valores/tipos REAIS impressos no terminal?", "variables_state"),
            ("Algum valor é None/Null, vazio ou de tipo diferente do esperado (ex: string '10' em vez de int 10)?", "type_check"),
        ]
    },
    {
        "num": 4,
        "title": "Tradução Socrática em Linguagem Natural",
        "intro": "Se você não consegue explicar a linha em português simples, o computador também não vai entender.",
        "questions": [
            ("Explique em UMA frase simples o que essa instrução específica faz, como se explicasse para alguém de 10 anos:", "plain_explanation"),
            ("A documentação oficial dessa função/método exige algum argumento ou comportamento que você ignorou?", "doc_check"),
        ]
    },
    {
        "num": 5,
        "title": "Hipótese e Experimento Mínimo",
        "intro": "Formule uma causa e teste com o menor exemplo possível.",
        "questions": [
            ("Qual é a sua hipótese agora sobre por que o bug aconteceu?", "hypothesis"),
            ("Qual alteração de UMA linha você vai testar agora para validar essa hipótese?", "experiment"),
        ]
    }
]


def start_session():
    print("\n" + bold(magenta("====================================================")))
    print(bold(magenta("    🦆 PATO SOCRÁTICO: SESSÃO DE DEBUG ATIVO 🦆    ")))
    print(bold(magenta("====================================================")))
    print(dim("Regra: Sem atalhos de IA. Apenas perguntas lógicas e investigação manual.\n"))

    session_data = {}

    for stage in STAGES:
        print("\n" + bold(cyan(f"--- ETAPA {stage['num']}: {stage['title']} ---")))
        print(dim(stage["intro"]))
        for q_text, key in stage["questions"]:
            print("\n" + yellow(f"• {q_text}"))
            ans = input(bold("> ")).strip()
            session_data[key] = ans if ans else "Não informado"

    print("\n" + bold(green("✔ Investigação concluída!")))
    print("\n" + bold("Resumo do seu experimento:"))
    print(f"- {bold('Hipótese')}: {session_data.get('hypothesis')}")
    print(f"- {bold('Teste imediato')}: {session_data.get('experiment')}")
    print(dim("\nVá ao seu código agora, faça esse teste e observe o resultado no terminal."))

    save_opt = input("\n" + bold("Deseja salvar esta sessão no seu DevLog de aprendizado? (s/N): ")).strip().lower()
    if save_opt in ("s", "sim", "y", "yes"):
        title = input(bold("Título para o DevLog: ")).strip() or "Sessao de Debug Socratico"
        now = datetime.now()
        safe_title = re.sub(r"[^\w\-_]", "_", title.lower())[:30]
        file_path = ensure_devlog_dir() / f"{now.strftime('%Y-%m-%d')}_{safe_title}.md"

        content = ENTRY_TEMPLATE.format(
            title=title,
            date=now.strftime("%Y-%m-%d %H:%M:%S"),
            tags="debug-socratico, pato-borracha",
            symptom=f"Entrada: {session_data.get('input_val')}\nSaída/Erro: {session_data.get('actual')}",
            expected=session_data.get('expected'),
            actual=session_data.get('actual'),
            mental_gap=f"Explicação da linha: {session_data.get('plain_explanation')}\nDoc check: {session_data.get('doc_check')}",
            root_cause=f"Hipótese: {session_data.get('hypothesis')}\nLocal: {session_data.get('location')}\nEstado de variáveis: {session_data.get('variables_state')}",
            prevention=f"Experimento aplicado: {session_data.get('experiment')}",
        )
        file_path.write_text(content, encoding="utf-8")
        print(green(f"✔ Salvo em: {file_path}"))
