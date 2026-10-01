# Modo escrita: containerizar + manifests

> **Origem**: exportada da plataforma anterior (pasta Drive "skills-Adapta/inativas"), status legado "inativa/backup". Importada para o repo em 2026-10-01 para consolidação; ainda sem validação de descoberta/execução neste agente.


# Ambiente Docker e Kubernetes

## Objetivo
Containerizar uma aplicação Python/Flask e criar manifests Kubernetes para deploy em cluster local (Kind) ou produção.

## Pré-requisitos
- Docker 20.10+
- Docker Compose v2+
- kubectl
- kind (para testes locais)
- Git

## Fase 1: Análise do Projeto

### 1.1 Stack e Execução
- Identificar linguagem, framework, servidor WSGI
- Determinar porta de escuta
- Verificar healthcheck/endpoint de status

### 1.2 Docker Compose
- Ler `docker-compose.yml`
- Mapear imagem da aplicação
- Listar dependências externas (banco, cache, etc.)

### 1.3 Variáveis de Ambiente
- Separar sensíveis (credenciais) das não-sensíveis (config)
- Documentar cada variável

## Fase 2: Dockerfile

### 2.1 Estrutura
```dockerfile
FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y --no-install-recommends build-essential libpq-dev
RUN groupadd --system appuser && useradd --system --create-home --gid appuser appuser
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src ./src
RUN chown -R appuser:appuser /app
USER appuser
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=3 CMD curl --fail http://localhost:8000/ || exit 1
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120", "src.main:app"]
```

### 2.2 Requisitos
- Imagem base slim
- Usuário não-root
- Healthcheck
- Servidor WSGI (Gunicorn)
- Variáveis de otimização

## Fase 3: Docker Compose

### 3.1 Serviços
- **app**: imagem da aplicação, porta 8000
- **postgres**: banco de dados, volume persistente
- **prometheus**: monitoramento (opcional)

### 3.2 Configuração
- Rede dedicada
- Variáveis de ambiente via `.env`
- Volumes nomeados para persistência
- Healthchecks em todos os serviços
- `depends_on` com `condition: service_healthy`

### 3.3 Testes
```bash
docker compose build
docker compose up -d
docker compose ps
docker compose logs -f app
curl http://localhost:8000
docker compose down -v
```

## Fase 4: Kubernetes (Kind)

### 4.1 Manifests (arquivo único: encontros-tech.yaml)
- **Namespace**: isolamento lógico
- **ConfigMap**: variáveis não-sensíveis
- **Secret**: credenciais (base64)
- **PersistentVolumeClaim**: armazenamento
- **Services**: exposição (ClusterIP, LoadBalancer)
- **Deployments**: aplicação, banco, prometheus

### 4.2 Probes
- **Liveness**: GET / :8000, initialDelaySeconds=30, periodSeconds=10
- **Readiness**: GET / :8000, initialDelaySeconds=10, periodSeconds=5

### 4.3 Recursos
- App: requests (100m CPU, 128Mi mem), limits (500m, 512Mi)
- Postgres: requests (250m, 256Mi), limits (1000m, 1Gi)

## Fase 5: Testes com Kind

### 5.1 Setup
```bash
kind create cluster --name encontros-tech
docker build -t encontros-tech:latest -f src/Dockerfile src/
kind load docker-image encontros-tech:latest --name encontros-tech
kubectl apply -f k8s/encontros-tech.yaml
```

### 5.2 Validação
```bash
kubectl get pods -n encontros-tech -w
kubectl get svc -n encontros-tech
kubectl port-forward svc/app-service -n encontros-tech 8000:8000
curl http://localhost:8000
kubectl logs -f deploy/app -n encontros-tech
```

### 5.3 Cleanup
```bash
kubectl delete namespace encontros-tech
kind delete cluster --name encontros-tech
```

## Fase 6: Documentação

### 6.1 Arquivos
- `Dockerfile` (src/)
- `docker-compose.yml` (raiz)
- `.dockerignore` (raiz)
- `.env.docker` (raiz)
- `k8s/encontros-tech.yaml` (manifests consolidados)
- `test-k8s.sh` (script de testes)
- `KUBERNETES.md` (documentação)

### 6.2 Conteúdo
- Visão geral da arquitetura
- Explicação de cada componente
- Comandos kubectl úteis
- Troubleshooting
- Próximos passos (Ingress, HPA, Secrets Manager)

## Checklist de Implementação
- [ ] Analisar stack e dependências
- [ ] Criar Dockerfile com otimizações
- [ ] Configurar docker-compose.yml
- [ ] Testar com Docker Compose
- [ ] Criar manifests Kubernetes
- [ ] Testar com Kind
- [ ] Documentar arquitetura
- [ ] Validar probes e healthchecks
- [ ] Preparar para produção

## Próximos Passos
1. Push da imagem para registry
2. Deploy em cluster de produção (EKS, GKE, AKS)
3. Configurar Ingress + TLS
4. Implementar HPA (autoscaling)
5. Secrets Manager (Sealed Secrets / External Secrets)
6. Observabilidade (Prometheus + Grafana + Loki)
7. GitOps (ArgoCD / Flux)
