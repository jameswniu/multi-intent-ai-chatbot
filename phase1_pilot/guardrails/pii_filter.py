"""
Removes personally identifiable information (PII) from text responses.
Prevents data leakage during chatbot output or logging.
"""

import re

def remove_pii(text: str) -> str:
    patterns = [
        (r"\b\d{3}-\d{2}-\d{4}\b", "[SSN]"),           # Social Security Number
        (r"\b[\w.%+-]+@[\w.-]+\.\w+\b", "[EMAIL]"),    # Email address
        (r"\b\d{10}\b", "[PHONE]"),                      # 10-digit phone number
        (r"\b\d{4} \d{4} \d{4} \d{4}\b", "[CARD]"),   # Credit card pattern
    ]
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text)
    return text
