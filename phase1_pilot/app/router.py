"""
Routes queries between KnowledgeAgent and ContractAgent.
Handles confidence logic and safe fallback for 'unknown' intent.
"""

from intent_classifier import IntentClassifier
from chains import KnowledgeAgent
from contract_agent import ContractAgent
from utils import sanitize_input

class QueryRouter:
    def __init__(self):
        self.classifier = IntentClassifier()
        self.knowledge_agent = KnowledgeAgent()
        self.contract_agent = ContractAgent()

    def handle_query(self, query: str):
        clean = sanitize_input(query)
        intent, confidence = self.classifier.classify(clean)

        if intent == "unknown" or confidence < 0.4:
            return intent, (
                "I'm not confident I understand this question. "
                "Could you rephrase it or provide more context?"
            )

        if intent == "contract":
            answer = self.contract_agent.answer(clean)
        else:
            answer = self.knowledge_agent.answer(clean)

        return intent, answer
