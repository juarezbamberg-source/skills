---
name: containers-docker-kubernetes
description: This skill should be used when the user asks to "containerizar aplicação", "criar Dockerfile", "dockerizar", "auditar/revisar Dockerfile", "comparar Dockerfiles", "otimizar imagem Docker", "boilerplate Docker", "deploy genérico em Kubernetes", or mentions Docker/Compose/Kubernetes para uma app SEM padrão da casa. Dois modos: escrita (containerizar + manifests lendo o projeto) e auditoria (revisar Dockerfiles com notas e tabela comparativa); método de cada modo em references/. NÃO usar para triagem de incidente em cluster (usar tecnicas/analise-remediacao-incidentes para incidentes com remediação).
version: 0.2.0
---

> **Origem**: fusão de duas skills legadas da plataforma anterior (ambiente-docker-kubernetes + auditoria-dockerfiles, pasta Drive "skills-Adapta/inativas"), consolidadas em 2026-10-01. Ainda sem validação de descoberta/execução neste agente (v0.x).

# Containers: Docker + Kubernetes (escrita e auditoria)

## Qual modo usar?

| Se o pedido for… | Use o reference |
|---|---|
| Containerizar uma app (Dockerfile, Compose, manifests K8s) | [`references/escrita.md`](references/escrita.md) |
| Auditar/revisar/comparar Dockerfiles existentes | [`references/auditoria.md`](references/auditoria.md) |

## Essencial de escrita (resumo — detalhes no reference)

1. **Ler o projeto antes**: stack, porta de escuta, healthcheck existente, variáveis de ambiente (sensíveis × config), dependências externas.
2. **Dockerfile**: base slim, usuário não-root (`useradd --system -m`), `PYTHONDONTWRITEBYTECODE=1`/`PYTHONUNBUFFERED=1`, dependências antes do código (cache de camadas), `chown` final.
3. **Manifests K8s**: probes em endpoints que existem, credenciais por `secretKeyRef` (nunca texto puro), resources requests/limits.
4. **Validar antes de entregar**: build local + (se aplicável) kubeconform.

## Essencial de auditoria (resumo — detalhes no reference)

1. **Resumo executivo** com notas 0–10 e status de produção (Pronto/Parcialmente/Não).
2. **Por arquivo**: forças, fraquezas com gravidade (Crítica/Alta/Média/Baixa), oportunidades, ameaças.
3. **Tabela comparativa** obrigatória: multi-stage, usuário não-root, healthcheck **que existe na imagem base** (crítico!), build deps mínimas, instruções duplicadas, ENV multi-linha, secrets como ENV vazio, `HEALTHCHECK --retries`.
4. **Veredito** com justificativa técnica e boilerplate quando pedido.

## Permissões que a skill pede

- **Leitura do projeto** (arquivos locais ou clone público) para descobrir porta/healthcheck/env no modo escrita.
- **Leitura de Dockerfiles** enviados no modo auditoria.
- **Execução de validação local quando disponível** (docker build, kubeconform) — somente leitura dos artefatos.
- **Não pede**: push de imagens, deploy em cluster, ou qualquer escrita fora do workspace.

## Histórico

- 0.2.0 (2026-10-01): estado atual — ver seção Origem acima para a procedência completa.
