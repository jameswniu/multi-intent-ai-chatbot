# AI Support Chatbot — Enterprise Design and Implementation

### Overview
This repository presents a two-phase architecture for an AI-powered support chatbot that assists customer service agents with:
- **Knowledge Retrieval** from product documentation.
- **Contract and Account Lookup** from structured SQL data sources.

The project demonstrates both a **Phase 1 Minimal Viable Product (MVP)** and a **Phase 2 Enterprise-Ready Architecture**, designed with observability, governance, and CI/CD integration.

---

## Phase 1: MVP Implementation

### Architecture Flow
```
Chat UI → Intent Classifier → Router  
    ├─ Knowledge QA Chain (FAISS + LLM)  
    └─ SQL Chain (Mock or Read-Only DB)  
→ Response Composer → User
```

### Core Components
- FastAPI or Streamlit interface for interaction
- LangChain `RetrievalQA` and `SQLDatabaseChain`
- Simple zero-shot or few-shot intent router
- Docker container for environment consistency

### Evaluation
| Category | Metric | Target | Method |
|-----------|---------|---------|--------|
| Intent Accuracy | ≥ 80% | 50 labeled queries |
| SQL Validity | ≥ 90% | Syntax and dry-run validation |
| Answer Relevance | ≥ 0.8 cosine similarity | Embedding similarity |
| Latency | < 3 seconds average | Request-duration logging |

### Guardrails
- Read-only schema access
- SQL parser and injection filter
- PII scrubber
- Confidence threshold fallback

### Monitoring and Observability
- LangSmith or local Grafana dashboard
- Structured JSON logs with metadata
- Alerts on latency > 3 seconds or error rate > 2%

### CI/CD and A/B Testing
- GitHub Actions for build, test, and deploy
- A/B variant routing for LLM and retriever configuration
- Metrics logging for experiment comparison

### RLHF Feedback Loop
- Collect thumbs-up/down feedback per response
- Weekly fine-tuning of classifier and prompt templates
- Store feedback for continuous improvement

---

## Phase 2: Production Scaling

### Architecture Flow
```
Chat UI → API Gateway → Router Service  
    ├─ Knowledge Service (Vector DB + LLM Retriever)  
    ├─ Contract Service (API to Cloud SQL Replica)  
    └─ Feedback Service (RLHF Pipeline)  
→ Monitoring → Analytics Dashboard
```

### Core Components
- FastAPI microservices
- Fine-tuned MiniLM intent classifier with LLM fallback
- Template-guarded NL2SQL generator
- Continuous document embedding refresh pipeline
- Kubernetes or ECS deployment with auto-scaling

### Evaluation
| Category | Metric | Target | Tool |
|-----------|---------|---------|------|
| Intent F1 | ≥ 0.95 | Scikit-learn |
| SQL Semantic Accuracy | ≥ 95% | Read-only replica test |
| Answer Quality | BLEU ≥ 0.85 / ROUGE-L ≥ 0.9 | Evaluation pipeline |
| Latency P95 | < 2 seconds | Prometheus |
| Cost per Query | <$0.05 | Cloud cost dashboard |
| Uptime | ≥ 99.9% | Synthetic monitors |

### Guardrails
- Role-based access control
- Query rate limits and validation
- Output sanitization
- Schema drift alerting

### Monitoring and Observability
- Prometheus and Grafana for metrics
- OpenTelemetry for API traces
- ELK or CloudWatch for logs
- LangSmith or Weights & Biases for model tracing

### CI/CD (Feature Updates and Bug Fixes)
1. Multi-branch Git flow (main, dev)
2. GitHub Actions for Docker build, unit tests, and scans
3. Helm deployment to Kubernetes staging
4. Manual approval gate before production release
5. Canary rollout and automatic rollback on failed health checks

### RLHF Continuous Learning
- Feedback service captures ratings and context
- Batch retraining of intent and reward models
- Weekly evaluation and automated weight updates

---

### Repository Structure
```
📦 ai-support-chatbot/
├── phase1_mvp/
│   ├── app/
│   ├── data/
│   ├── evals/
│   ├── Dockerfile
│   └── ci_cd.yaml
├── phase2_production/
│   ├── services/
│   ├── helm/
│   ├── observability/
│   ├── evals/
│   ├── Dockerfile
│   └── ci_cd_pipeline.yaml
├── guardrails/
│   ├── pii_filter.py
│   ├── prompt_injection_guard.py
│   └── sql_validator.py
└── docs/
    ├── 01_executive_summary.pdf
    ├── 02_architecture_overview.md
    ├── 03_phase1_phase2_roadmap.md
    └── 04_metrics_and_governance.md
```

---

### Contact
Developed by **[Your Name]**  
For questions: [your.email@example.com]

---

### License
MIT License
