# Architecture Overview

The system follows a modular design that separates intent detection, knowledge retrieval, and secure data access. This keeps it easy to scale and maintain while fitting into standard enterprise analytics environments.

### Core Components

| Layer | Component | Purpose |
|-------|------------|----------|
| Interface | Chat or agent UI | Collects and displays user interactions |
| Logic | Intent Classifier and Router | Decides which backend should answer the question |
| Knowledge Service | Vector database and LLM retriever | Handles "how-to" or documentation queries |
| Contract Service | SQL API layer | Fetches account or contract data securely |
| Feedback Service | RLHF feedback pipeline | Learns from user feedback to improve accuracy |
| Observability | Prometheus, Grafana, OpenTelemetry | Tracks performance, uptime, and cost |

### Data Flow
1. A user sends a query through the chat interface.  
2. The Intent Classifier detects whether it is a product or contract question.  
3. The Router directs it to the right backend.  
4. The system composes a response and sends it back.  
5. Each interaction is logged and reviewed for improvement.

### Security and Governance
- Role-based access control (RBAC)  
- Data masking and PII filtering  
- Encrypted communication between services  
- Complete audit logs and drift monitoring
