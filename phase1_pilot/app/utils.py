
"""
Utility functions for embeddings, similarity, and logging.
"""

import datetime
import numpy as np

def log_event(event_type: str, detail: str):
    ts = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {event_type}: {detail}")

def sanitize_input(text: str) -> str:
    return text.strip()

def embed_text(text: str) -> np.ndarray:
    vec = np.zeros(300)
    for w in text.lower().split():
        vec[hash(w) % 300] += 1
    norm = np.linalg.norm(vec)
    return vec / norm if norm > 0 else vec

def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    return float(np.dot(a, b) / denom) if denom != 0 else 0.0

def load_docs(path: str):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read().split("\n\n")
    except FileNotFoundError:
        return ["Documentation file not found."]
