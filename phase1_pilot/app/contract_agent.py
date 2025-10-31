"""
ContractAgent with rule + keyword mapping SQL generator.
No LLM used - fully local and deterministic.
"""

import sqlite3
from guardrails.sql_validator import validate_sql

COLUMN_MAP = {
    "price": "price",
    "cost": "price",
    "expiry": "expiry_date",
    "renewal": "expiry_date",
    "module": "module",
    "customer": "customer_id",
    "contract": "customer_id"
}

class ContractAgent:
    def __init__(self, db_path="phase1_pilot/data/mock_contracts.db"):
        self.db_path = db_path

    def _construct_sql(self, query: str) -> str:
        words = query.lower().split()
        selected_cols = [COLUMN_MAP[w] for w in words if w in COLUMN_MAP]

        if not selected_cols:
            selected_cols = ["customer_id", "module", "expiry_date", "price"]

        sql = f"SELECT {', '.join(set(selected_cols))} FROM contracts LIMIT 10;"
        validate_sql(sql)
        return sql

    def answer(self, query: str) -> str:
        sql = self._construct_sql(query)
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()

        if not rows:
            return "No matching records found."

        header = [desc[0] for desc in cur.description]
        result_text = [dict(zip(header, row)) for row in rows]
        return f"Query: {sql}\n\nResults:\n{result_text}"
