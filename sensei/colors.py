"""Terminal styling and colors using standard ANSI escape codes."""
import sys
import os

# Enable ANSI escape sequences and UTF-8 encoding on Windows
if os.name == "nt":
    os.system("")
    try:
        if sys.stdout and hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        if sys.stderr and hasattr(sys.stderr, "reconfigure"):
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

class Style:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"

    # Colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # Backgrounds
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"


def bold(text: str) -> str:
    return f"{Style.BOLD}{text}{Style.RESET}"

def dim(text: str) -> str:
    return f"{Style.DIM}{text}{Style.RESET}"

def green(text: str) -> str:
    return f"{Style.GREEN}{text}{Style.RESET}"

def red(text: str) -> str:
    return f"{Style.RED}{text}{Style.RESET}"

def yellow(text: str) -> str:
    return f"{Style.YELLOW}{text}{Style.RESET}"

def cyan(text: str) -> str:
    return f"{Style.CYAN}{text}{Style.RESET}"

def magenta(text: str) -> str:
    return f"{Style.MAGENTA}{text}{Style.RESET}"

def blue(text: str) -> str:
    return f"{Style.BLUE}{text}{Style.RESET}"

def badge(label: str, color_fn) -> str:
    return f"[{color_fn(label)}]"
