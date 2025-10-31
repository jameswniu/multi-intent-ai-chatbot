
"""
KnowledgeAgent using FAISS vector database for offline retrieval.
"""

import faiss
from sentence_transformers import SentenceTransformer
from utils import load_docs

class KnowledgeAgent:
    def __init__(self, docs_path="phase1_pilot/data/user_guide_sample.txt"):
        self.docs = load_docs(docs_path)
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        embeddings = self.model.encode(self.docs, convert_to_numpy=True)
        dim = embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)

    def _search(self, query: str, top_k: int = 2):
        query_vec = self.model.encode([query], convert_to_numpy=True)
        D, I = self.index.search(query_vec, top_k)
        return [self.docs[i] for i in I[0]]

    def answer(self, query: str) -> str:
        top_docs = self._search(query)
        context = "\n\n".join(top_docs)
        return f"Here’s what I found based on documentation:\n\n{context}"
