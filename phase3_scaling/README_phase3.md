# Phase 3 - Scaling & Orchestration

Phase 3 builds on the LLM-enabled chatbot architecture to deliver enterprise-grade scalability, reliability, and automation.

### Core Additions
- Kubernetes orchestration (GKE/EKS/AKS)
- Helm-based deployment templates
- Prometheus + Grafana for observability
- Alerting via Prometheus Rules
- GitOps with Argo CD

### Runbook Summary
1. Apply Helm deployment:
   ```bash
   helm upgrade --install chatbot ./helm -n chatbot
   ```
2. Verify Prometheus metrics:
   ```bash
   kubectl port-forward svc/prometheus-server 9090:9090
   ```
3. Monitor Grafana dashboard:
   ```bash
   kubectl port-forward svc/grafana 3000:3000
   ```
4. Manage via GitOps:
   - Argo CD auto-syncs latest repo changes to live clusters.

### Alerts Configured
- High Latency > 2s
- CPU Usage > 85%
- Pod Restarts > 3

### Scaling Goals
- SLA Uptime: ≥ 99.95%
- Node Utilization: ≥ 80%
- Pod Auto-scaling: 2–10 replicas
