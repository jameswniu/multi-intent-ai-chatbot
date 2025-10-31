
"""
Routes queries between KnowledgeAgent and ContractAgent.
Now includes prompt-injection and PII guardrails.
"""

from intent_classifier import IntentClassifier
from chains import KnowledgeAgent
from contract_agent import ContractAgent
from utils import sanitize_input
from guardrails.prompt_injection_guard import detect_prompt_injection
from guardrails.pii_filter import remove_pii


class QueryRouter:
    def __init__(self):
        self.classifier = IntentClassifier()
        self.knowledge_agent = KnowledgeAgent()
        self.contract_agent = ContractAgent()

    def handle_query(self, query: str):
        clean = sanitize_input(query)

        # Guardrail 1: Prompt injection detection (input side)
        if detect_prompt_injection(clean):
            return "unsafe", (
                "Your request appears unsafe or may contain restricted instructions. "
                "Please rephrase and try again."
            )

        # Classify intent
        intent, confidence = self.classifier.classify(clean)

        # Low confidence fallback
        if intent == "unknown" or confidence < 0.4:
            response = (
                "I'm not confident I understand this question. "
                "Could you rephrase it or provide more context?"
            )
        elif intent == "contract":
            response = self.contract_agent.answer(clean)
        else:
            response = self.knowledge_agent.answer(clean)

        # Guardrail 2: Remove PII before returning (output side)
        safe_response = remove_pii(response)
        return intent, safe_response
