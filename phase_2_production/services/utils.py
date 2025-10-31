"""
Shared utility functions.
"""

def sanitize_input(text: str) -> str:
    return text.strip()

def load_docs(path: str):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().split("\n\n")
    except FileNotFoundError:
        return ["No documentation found."]
