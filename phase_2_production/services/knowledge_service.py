"""
Vector DB + LLM Retriever microservice (RAG pattern).
"""

import os
import faiss
from sentence_transformers import SentenceTransformer
from openai import OpenAI
from services.utils import load_docs

class KnowledgeService:
    def __init__(self, docs_path="phase2_production/data/user_docs.txt"):
        self.docs = load_docs(docs_path)
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self._build_index()

    def _build_index(self):
        embeddings = self.model.encode(self.docs, convert_to_numpy=True)
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)

    def handle_knowledge(self, query: str) -> str:
        query_vec = self.model.encode([query], convert_to_numpy=True)
        _, I = self.index.search(query_vec, 3)
        context = "\n".join([self.docs[i] for i in I[0]])
        prompt = f"Answer the question using only this context:\n{context}\nQuestion: {query}"
        result = self.llm.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "system", "content": prompt}],
        )
        return result.choices[0].message.content.strip()
