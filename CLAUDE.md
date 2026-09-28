# CLAUDE.md - Code Sensei Context

## Project Overview
Code Sensei is an offline, terminal-based personal programming mentor designed for deliberate practice without relying on AI autocompletion. It features:
- Progressive TDD Katas (20 levels in JS/TS/Node.js, 6 in Python).
- 4 Boss Fights (integrated milestone projects).
- Socratic Rubber Duck interactive debugger.
- Blind Trace mental execution flashcards.
- 3-tier progressive hint system (`python main.py hint`).
- Static anti-cheat linter blocking shortcut methods.
- Git auto-commit on test passage in watch mode.
- Metacognitive DevLog system in Markdown.
- Complete Obsidian Knowledge Vault in `brain/`.

---

## Quick Reference Commands

### Running & Studying
```bash
python main.py                  # Open interactive menu
python main.py watch            # Active watch mode with Git Auto-Commit
python main.py train            # Run katas check (stops at first failing exercise)
python main.py hint [ex] [1..3] # Get Socratic hint (1=question, 2=pseudocode, 3=api doc)
python main.py trace            # Run Blind Trace mental compiler flashcards
python main.py hunt             # Run Caça-Bugs reverse code review challenges
python main.py boss             # Run and evaluate Boss Fights
python main.py duck             # Run Socratic Duck 5-stage debugging session
python main.py log              # Create DevLog entry
python main.py logs             # List DevLog entries
python main.py stats            # Show progress stats
python main.py --track js_ts    # Switch to JS/TS/Node track
python main.py --track python   # Switch to Python track
```

### Running Tests Directly
```bash
# In an exercise directory:
# For TypeScript (Node.js 24 native):
node --experimental-strip-types --test test_exercise.ts

# For Python:
python -m unittest test_exercise.py
```

---

## Architecture & Directory Layout

```text
charming-shannon/
├── .sensei_config.json        # Active track configuration
├── CLAUDE.md                  # Assistant project context
├── LICENSE                    # MIT License
├── README.md                  # Repository documentation and badges
├── main.py                    # Root entrypoint
├── sensei/                    # Core mentor engine
│   ├── cli.py                 # Menu and command-line parser
│   ├── colors.py              # ANSI styling and Windows UTF-8 stdout setup
│   ├── hints.py               # 3-tier progressive hint database
│   ├── journal.py             # DevLog manager
│   ├── linter.py              # Static anti-cheat analyzer
│   ├── runner.py              # Test discovery, execution & git auto-commit
│   ├── socratic.py            # Socratic duck interview engine
│   └── tracer.py              # Blind Trace mental compiler engine
├── exercises/                 # Progressive katas
│   ├── js_ts/                 # 20 Levels (01 to 20) in TypeScript
│   │   └── boss_fights/       # 4 Milestone Boss Projects
│   └── python/                # 6 Levels in Python
├── devlog/                    # User metacognitive reflections in Markdown
└── brain/                     # Obsidian Vault (MOC, levels, methodology)
```

---

## Technical Gotchas & Rules

1. **Zero External Dependencies**: The entire core engine runs purely on standard library (Python 3.10+ and Node.js 24+). Do NOT introduce external npm or pip dependencies for the core runner.
2. **Node.js 24 Type Stripping**: TypeScript files are executed directly via `node --experimental-strip-types --test test_exercise.ts`. No `tsconfig.json` or build step required.
3. **Windows Encoding**: Always ensure stdout is configured for UTF-8 with error replacement to prevent `charmap` codec errors with ANSI/emojis on Windows consoles.
4. **Anti-Cheat Linter**: When editing katas, the linter checks for prohibited shortcut functions (e.g. `Math.max` in Level 04, `.reduce` in Level 03).
5. **Anti-AI Policy**: When assisting the user, never provide complete copy-paste code solutions. Provide Socratic questions, pseudocode or links to official documentation.
