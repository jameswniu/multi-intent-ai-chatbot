"""
Ensures generated SQL is safe to execute.
"""

import re

def validate_sql(query: str) -> bool:
    dangerous = ["DROP", "DELETE", "ALTER", "UPDATE", ";"]
    if any(word.lower() in query.lower() for word in dangerous):
        raise ValueError("Unsafe SQL detected.")
    return True
