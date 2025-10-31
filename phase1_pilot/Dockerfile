# Dockerfile for Phase 1 Offline Chatbot
FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir fastapi uvicorn faiss-cpu sentence-transformers numpy

EXPOSE 8000
CMD ["uvicorn", "phase1_pilot.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
