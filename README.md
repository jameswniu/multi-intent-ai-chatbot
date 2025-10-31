# Multi-Intent AI Chatbot Assistant

### Overview
This project shows how to design and build an AI-powered support chatbot that helps customer service teams answer product and contract questions quickly and accurately.

The system is built in two stages:
1. **Phase 1:** A working MVP that proves the concept and gathers feedback.
2. **Phase 2:** A production-grade version that scales securely with monitoring, automation, and continuous learning.

---

## Phase 1: MVP Implementation

### Architecture Flow
```mermaid
flowchart TD
    A[User / Agent Chat UI] --> B[Intent Classifier]
    B --> C{Router}
    C -->|How-to Query| D[Knowledge QA Chain<br/>(Docs + Embeddings + LLM)]
    C -->|Contract Query| E[SQL Chain<br/>(Mock or Read-Only DB)]
    D --> F[Response Composer]
    E --> F
    F --> G[Chat Response to User]

    subgraph Monitoring
        H[Logs & Metrics]
        I[LangSmith / Grafana]
    end
    F --> H
```

```
Chat UI -> Intent Classifier -> Router
    ├─ Knowledge QA Chain (FAISS + LLM)
    └─ SQL Chain (Mock or Read-Only DB)
-> Response Composer -> User
```

### What's Inside
- Simple FastAPI or Streamlit interface for chat
- LangChain `RetrievalQA` for document search and `SQLDatabaseChain` for contract lookup
- Basic intent router using zero-shot or few-shot classification
- Docker environment for easy setup and reproducibility

### Evaluation
| Category | Metric | Target | Method |
|-----------|---------|---------|--------|
| Intent Accuracy | ≥ 80% | 50 labeled queries | Manual evaluation |
| SQL Validity | ≥ 90% | Syntax and dry-run validation | SQL parser |
| Answer Relevance | ≥ 0.8 cosine similarity | Embedding similarity | Cosine metric |
| Latency | < 3 seconds average | Logged request times | Timing logs |

### Guardrails
- Read-only database schema
- SQL parser and injection filter
- PII scrubber for sensitive data
- Confidence threshold fallback if unsure

### Monitoring and Observability
- LangSmith or local Grafana dashboard
- Structured logs with metadata
- Alerts for latency or error spikes

### CI/CD and A/B Testing
- GitHub Actions for build, test, and deploy
- A/B testing for model or retriever variants
- Metrics tracked for side-by-side comparison

### RLHF Feedback Loop
- Collect simple thumbs-up/down feedback on responses
- Use results to refine prompts and routing logic
- Continuous updates based on real interactions

---

## Phase 2: Production Scaling

### Architecture Flow
```mermaid
flowchart TD
    A[User / Agent Chat UI] --> B[API Gateway]
    B --> C[Router Service]
    C -->|Knowledge Request| D[Knowledge Service<br/>(Vector DB + LLM Retriever)]
    C -->|Contract Request| E[Contract Service<br/>(Cloud SQL via API)]
    C -->|Feedback| F[Feedback Service<br/>(RLHF Pipeline)]
    D --> G[Response Composer]
    E --> G
    F --> H[Model Feedback Store]
    G --> I[Analytics Dashboard]
    I --> J[User Response]

    subgraph Observability
        K[Prometheus / Grafana / OpenTelemetry]
    end
    C --> K
    D --> K
    E --> K
    F --> K
```

```
Chat UI -> API Gateway -> Router Service
    ├─ Knowledge Service (Vector DB + LLM Retriever)
    ├─ Contract Service (API to Cloud SQL Replica)
    └─ Feedback Service (RLHF Pipeline)
-> Monitoring -> Analytics Dashboard
```

### What's Inside
- Modular FastAPI microservices
- Fine-tuned MiniLM intent classifier with LLM fallback
- Template-based NL2SQL generator for safety and consistency
- Automatic document embedding refresh pipeline
- Kubernetes or ECS deployment with auto-scaling and health checks

### Evaluation
| Category | Metric | Target | Tool |
|-----------|---------|---------|------|
| Intent F1 | ≥ 0.95 | Scikit-learn | Classification report |
| SQL Semantic Accuracy | ≥ 95% | Read-only replica testing | SQL validator |
| Answer Quality | BLEU ≥ 0.85 / ROUGE-L ≥ 0.9 | Automated evaluation | NLP metrics |
| Latency P95 | < 2 seconds | Prometheus | API timing |
| Cost per Query | <$0.05 | Cloud cost dashboard | Billing logs |
| Uptime | ≥ 99.9% | Synthetic monitors | Health checks |

### Guardrails
- Role-based access control (RBAC)
- Query rate limits and validation
- Output sanitization for hallucinations
- Schema drift detection and alerting

### Monitoring and Observability
- Prometheus and Grafana metrics
- OpenTelemetry traces for APIs
- ELK or CloudWatch logs
- LangSmith or Weights & Biases for model tracing

### CI/CD (Updates and Bug Fixes)
1. Multi-branch Git flow (main and dev)
2. GitHub Actions pipeline for Docker builds, testing, and scans
3. Helm deployment to Kubernetes staging
4. Manual approval before production rollout
5. Canary release with auto rollback on failed checks

### RLHF Continuous Learning
- Feedback service stores ratings and conversation context
- Regular retraining of intent and reward models
- Weekly evaluation and auto-weight updates via CI/CD

---

### Repository Structure
```
ai-chatbot/
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
Developed by **James W. Niu**
Questions: **jameswnarch@gmail.com**

---

### License
MIT License
