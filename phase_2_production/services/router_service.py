"""
Router microservice for Phase 2 production chatbot.
Performs LLM-assisted intent routing with environment variable credentials.
"""

import os
from fastapi import FastAPI, Query
from openai import OpenAI
from services.knowledge_service import KnowledgeService
from services.contract_service import ContractService
from services.feedback_service import FeedbackService
from services.utils import sanitize_input

app = FastAPI(title="Router Service – Phase 2")

def get_env_var(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise EnvironmentError(f"Missing required environment variable: {name}")
    return value

llm = OpenAI(api_key=get_env_var("OPENAI_API_KEY"))
knowledge = KnowledgeService()
contract = ContractService()
feedback = FeedbackService()

@app.post("/route")
def route_query(user_query: str = Query(...)):
    q = sanitize_input(user_query)
    completion = llm.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Classify query as 'knowledge' or 'contract'."},
            {"role": "user", "content": q},
        ]
    )
    intent = completion.choices[0].message.content.strip().lower()
    if "contract" in intent:
        response = contract.handle_contract(q)
    else:
        response = knowledge.handle_knowledge(q)
    feedback.log_interaction(q, intent, response)
    return {"intent": intent, "response": response}
