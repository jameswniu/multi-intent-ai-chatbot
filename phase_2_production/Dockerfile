FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir fastapi uvicorn openai faiss-cpu sentence-transformers prometheus-client
EXPOSE 8000
CMD ["uvicorn", "services.router_service:app", "--host", "0.0.0.0", "--port", "8000"]
