"""
RLHF feedback microservice.
Logs user queries, model responses, and feedback ratings for continuous learning.
"""

import json
from datetime import datetime

class FeedbackService:
    def __init__(self, log_path="phase2_production/logs/feedback_log.jsonl"):
        self.log_path = log_path

    def log_interaction(self, query, intent, response, rating=None):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "query": query,
            "intent": intent,
            "response": response,
            "rating": rating or "N/A"
        }
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
