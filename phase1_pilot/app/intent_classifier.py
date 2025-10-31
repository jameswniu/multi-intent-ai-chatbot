
"""
IntentClassifier identifies the intent behind a user's query.
Uses simple keyword-based scoring to decide between 'knowledge', 'contract', or 'unknown'.
"""

from typing import Tuple

class IntentClassifier:
    def __init__(self):
        self.contract_keywords = ["contract", "price", "expiry", "renewal", "billing"]
        self.knowledge_keywords = ["how", "guide", "use", "setup", "instructions", "help"]

    def classify(self, query: str) -> Tuple[str, float]:
        q = query.lower()
        contract_score = sum(1 for k in self.contract_keywords if k in q)
        knowledge_score = sum(1 for k in self.knowledge_keywords if k in q)

        total = contract_score + knowledge_score
        confidence = total / (len(self.contract_keywords) + len(self.knowledge_keywords))

        if contract_score > knowledge_score:
            intent = "contract"
        elif knowledge_score > contract_score:
            intent = "knowledge"
        else:
            intent = "unknown"
            confidence = 0.3

        return intent, confidence
