# Caso real aplicado — exercício "Padrão de Manifests da Metacortex"

Registro de como o método desta skill foi aplicado em um exercício real de MBA (2026-09-29), para servir de exemplo concreto e calibrar expectativas. Repositório: `github.com/juarezbamberg-source/metacortex-manifest` (público, v1.0.0).

## O enunciado (o que havia de verdade)

Sem enunciado oficial além do documento "Padrão de Manifests da Metacortex" — um wiki interno de Plataforma com 4 blocos (Identidade/nomenclatura, Resiliência, Segurança, Vocabulário) e três níveis de regra (obrigatório/recomendado/proibido). Cada regra nasceu de incidente ou auditoria.

Decisões de escopo tomadas com o aluno: app-alvo `nyx-api` (citada pelo próprio padrão), **YAML puro**, 3 ambientes (dev/stg/prod), CI de validação + CD com gate, README com checklist. Repo público.

## O que foi entregue (linha do tempo)

1. **Checklist** regra → como atendo (20+ regras) antes de qualquer YAML.
2. **Manifests** YAML puro por ambiente: namespace, serviceaccount, configmap, secret (placeholder base64), deployment, service (+ pdb em prod) e kustomization de aplicação. Ambientes diferindo só no previsto: réplicas 1/1/2, RollingUpdate maxUnavailable 0 e PDB só em prod.
3. **Policy as code**: `validar-regras-casa.py` (FALHA/aviso, ~20 verificações) — camada que o kubeconform/trivy não cobre (kebab-case, namespace `<cliente>-<ambiente>`, 4 rótulos, seletor × template, `:latest`, segredo em texto puro, securityContext, probes, réplicas, selector de Service × PDB, targetPort órfão).
4. **Teste negativo**: fixture de propósito inválida barrada em todas as regras esperadas.
5. **CI 3 camadas** (depois 4, com pytest) em todo PR: regras da casa + kubeconform -strict + trivy config.
6. **CD**: workflow `deploy.yml` — validar → dev → stg → prod; environment prod com revisor obrigatório (gate manual); apply em cluster kind efêmero + **asserções pós-apply** (objetos aterrissados, réplicas, PDB, estrategia); concurrency serializando.
7. **Execução real**: 3 runs de deploy completos com gates aprovados pelo aluno (kind, checkout v7, setup-python v7 provados no pipeline inteiro).
8. **Auditoria (10 achados → G1–G5)**: main sem proteção (crítico), validador sem testes (crítico), porta de probe não validada, jobs sem timeout, validação duplicada, sem Dependabot, nenhum PR ainda, kubeconform defasado, sem LICENSE/topics, sem tag. Aplicado tudo **por PR #1** (dogfood) + branch protection na main + v1.0.0.
9. **Documentação**: README com checklist + entrega contínua + governança; `docs/RUNBOOK.md`, `docs/DECISOES.md` (8 ADRs), `docs/RELATORIO-EXERCICIO.md`.
10. **Apresentação**: deck de 13 slides em PDF + documentação completa em PDF (15 páginas).

## Erros reais que o pipeline pegou (lições valiosas)

- `trivy-action@0.28.0` → tag correta é `v0.36.0` (prefixo `v`). CI falhou em segundos — bom para a narrativa.
- `timeout-minutes` em job que **chama** workflow reutilizável → "workflow file issue" (property não suportada no caller). Mover o timeout para dentro do reutilizável.
- PR só de README: main com required status check + paths filter sem `README.md` → **PR BLOCKED para sempre** (o check nunca reporta). Incluir `README.md` no filtro.
- Merge de PR que toca `deploy.yml` → próximo deploy fica `pending` atrás do gate de prod aberto (concurrency). Aprovar o gate destrava a fila.

## Métricas do resultado

- 0 falhas / 0 avisos nas regras da casa (22 arquivos); kubeconform 19 válidos; trivy 0 HIGH/CRITICAL.
- 12 testes do validador (camada 0) verde.
- 6 runs de pipeline, 5 success + 1 failure (a de versão, corrigida e nunca repetida).
- 7 objetos aterrissados em cluster kind no prod real (2 réplicas + PDB + rollout).
- Fluxo completo exercido: PR #1 → CI → main protegida → CD → gate humano → prod.

## Checklist do deck de apresentação (13 slides)

Capa (dark) → o problema (o padrão) → a ideia central (policy as code) → metodologia 8 passos → o repositório (árvore) → o pipeline → as provas (números reais) → regra viva do documento (ex.: 1.4 seletor) → 8 ADRs → lições → auditoria (achados → G1–G5 → PR #1) → evolução (ArgoCD, External Secrets, OPA, preview) → fechamento (fluxo completo exercido).