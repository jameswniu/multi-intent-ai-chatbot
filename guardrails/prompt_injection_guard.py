"""
Detects and blocks malicious or manipulative input prompts.
Protects the chatbot from instruction override or injection attempts.
"""

def detect_prompt_injection(prompt: str) -> bool:
    blacklist = [
        "ignore previous instructions",
        "system override",
        "disable filters",
        "bypass safety",
        "reveal hidden data",
        "execute code",
        "drop table",
    ]
    return any(term in prompt.lower() for term in blacklist)
