---
name: exercicio-devops-cloud-ia
description: This skill should be used when the user asks to "executar um exercício DevOps", "fazer exercício da pós em engenharia cloud com IA", "criar repositório e executar o exercício", "transformar um padrão/política/documento em repositório", "montar pipeline CI/CD para exercício acadêmico", "validar manifests Kubernetes contra um padrão", "aplicar o método Metacortex", ou falar em "exercício prático do MBA de DevOps". NÃO usar para containerizar/auditar Dockerfiles de produção real (usar tecnicas/containers-docker-kubernetes) nem para gerar Terraform (usar tecnicas/gerar-terraform). Guia a execução completa de um exercício de infra/repo: ler o enunciado como especificação de sistema, checklist primeiro, policy as code, teste negativo, validação local, CI/CD por PR com gate humano, auditoria e documentação viva. Também quando precisar "conectar o agente ao meu cluster local", "subir kind no Windows com Docker Desktop", "criar túnel cloudflared para o agente acessar o cluster", "passar kubeconfig/token para o agente com segurança", ou "carregar imagens no nó do kind sem Docker Hub".
version: 1.1.0
---

# Exercício DevOps/Cloud/IA — método completo (do padrão ao repo sustentável)

Metodologia validada no exercício **"Padrão de Manifests da Metacortex"** (MBA Engenharia DevOps): transformar um documento de padrão/regras/enunciado em um repositório com CI/CD, conformidade provada por pipeline e fluxo por PR. O guia é um **receita de fim a fim** — funciona para exercícios de Kubernetes, Cloud (AWS/Azure/GCP), IaC, IA/MLOps ou qualquer disciplina que entregue artefatos versionados com regras revisáveis.

## Fase 0 — Antes de tocar em código

### 0.1 Ler o enunciado como especificação de sistema

Todo documento de padrão contém a arquitetura da solução escondida. Exemplos reais: uma página de regras que diz *"a varredura com Trivy roda no pipeline"* já descreve o CI; um rótulo `managed-by: platform` já descreve o GitOps. **Extrair essas pistas** antes de projetar:

- Grifar cada regra/menção a ferramenta, fluxo, nível (obrigatório/recomendado/proibido) e exceção.
- Traduzir o texto em **requisitos de sistema**: o que o repositório precisa ter para provar cada regra.
- Identificar os **níveis** que o documento usa — eles viram o contrato da validação (ver Fase 1).

### 0.2 Fazer checklist primeiro, YAML depois

Antes de escrever qualquer artefato, produzir uma tabela `regra → como atendo → nível`. Ela é o mapa do exercício: cada artefato posterior referencia uma linha dela. Sem checklist, o exercício vira improviso.

### 0.3 Listar dúvidas antes de prosseguir

Quando o enunciado tiver ambiguidades (app-alvo, formato YAML/Helm/Kustomize, escopo do CI, nome do repo), consolidadar em poucas perguntas objetivas e só então planejar. Um erro aqui custa caro depois.

## Fase 1 — Policy as code (o coração do exercício)

### 1.1 As regras viram código

Criar um script que reproduza a semântica do documento:

- Regra **obrigatória** violada → **FALHA** → exit 1 (barra o pipeline).
- Regra **proibida** violada → **FALHA** (não existe exceção).
- Regra **recomendada** não atendida → **AVISO** (exige justificativa no PR, não barra).

Modelo de saída por arquivo: `✓ arquivo` (ok), `⚠ arquivo` (avisos), `✗ arquivo` (falhas), com resumo final `N arquivo(s) · X falha(s) · Y aviso(s)`.

### 1.2 Incluir as regras que a ferramenta genérica não conhece

A ferramenta (kubeconform, terraform validate, etc.) valida **forma**; o script valida **intenção da casa**: nomenclatura, rótulos obrigatórios, seletor × template, ausência de segredo, securityContext, probes em portas reais, réplicas por ambiente. Exemplo funcional: `examples/validar-regras-casa.py`.

### 1.3 Escrever o teste negativo primeiro

Um validador que nunca provou que **barra** não é gate, é sugestão. Criar uma fixture que viole o padrão (nome errado, sem rótulos, `:latest`, senha em texto puro, seletor descasado) e afirmar que o script retorna exit 1 em cada regra. Adotar sempre o padrão: **base válida + uma violação por teste**.

## Fase 2 — Estrutura do repositório

Padrão de árvore (ajustar à disciplina):

```
<repo>/
├── .github/
│   ├── dependabot.yml            # updates semanais das actions
│   └── workflows/
│       ├── validar.yml           # REUTILIZÁVEL: testes + regras da casa + schema + varredura
│       ├── validar-manifests.yml # CI de PR (chama validar.yml)
│       └── deploy.yml            # CD: validar → dev → stg → prod (gate em prod)
├── scripts/                      # policy as code (regras da casa)
├── tests/                        # testes do validador (camada 0 do CI)
├── docs/
│   ├── RUNBOOK.md                # procedimento de plantão (o runbook do padrão)
│   ├── DECISOES.md               # ADRs — contexto → decisão → consequência
│   └── RELATORIO-EXERCICIO.md    # metodologia, provas, lições (para o MBA)
├── manifests/ (ou infra/)        # os artefatos por ambiente (YAML puro, sem template)
└── LICENSE
```

Princípios de estrutura:
- **YAML puro** em vez de Helm/Kustomize quando o aprendizado for o objetivo: cada objeto visível, sem camada que esconda o resultado. A repetição controlada entre ambientes é aceita (e didática).
- **Ambientes diferem só no que o padrão prevê** — documentar a pequena tabela "regra × dev × stg × prod".
- **`tests/` dentro do repo** (não ad-hoc): o validador também é código e precisa de teste.

## Fase 3 — Validação local antes do push

Rodar as MESMAS camadas do CI na máquina antes de commitar. Se o sandbox não tiver as ferramentas, baixar as binárias oficiais (kubeconform, trivy, etc.) em `tmp/bin` (não instalar global com sudo).

Ordem das camadas (do mais barato para o mais caro):
1. **Camada 0** — `pytest tests/` (testa o validador).
2. **Camada 1** — script das regras da casa (`python scripts/validar-*.py artefacts/`).
3. **Camada 2** — schema/forma (ex.: `kubeconform -strict -summary`).
4. **Camada 3** — varredura de segurança/misconfig (ex.: `trivy config --exit-code 1 --severity HIGH,CRITICAL`).

Resultado esperado: lint local 100% verde e o **teste negativo barrando** — isso antecipa o CI e evita rodadas de correção no GitHub.

## Fase 4 — CI e CD

### 4.1 Workflow reutilizável (uma fonte de verdade)

Centralizar a validação em um workflow reutilizável (`validar.yml`) chamado pelo CI de PR **e** pelo CD. Assim CI e deploy validam a mesma coisa — sem drift. Modelo: `examples/workflow-validar-reutilizavel.yml` + `examples/workflow-ci-pr.yml`.

### 4.2 O que o workflow de deploy deve ter

- `validar` (workflow reutilizável) → `deploy-dev` → `deploy-stg` → `deploy-prod`.
- **Promoção por commit**: o mesmo SHA validado flui pelos ambientes; nunca re-gerar artefato no caminho.
- **Gate de produção**: environment `prod` com **revisor obrigatório** (GitHub Environments) — produção pausa até aprovação humana na UI.
- **Prova de deploy**: em vez de só `kubectl apply`, executar **asserções pós-apply** (objetos existem, réplicas certas, recurso de prod só existe em prod). Modelo: `examples/workflow-deploy.yml`.
- **Concorrência** (`concurrency: deploy-nyx`) para serializar deploys — dois pushes não deployam em paralelo.
- **Permissão mínima**: `permissions: contents: read`.
- **timeout-minutes: 10** em cada job (evita runner queimado).
- **Imagem/registry fictício**: documentar que `ImagePullBackOff` é esperado quando o registry não existe — a prova é a aterrissagem dos objetos no API server, não a saúde do pod.

### 4.3 Armadilhas conhecidas (lições reais)

- **Tag de action**: usar `@vX.Y.Z` (com o `v`), não `@X.Y.Z` — o CI falha com "Unable to resolve action".
- **Job caller de workflow reutilizável NÃO aceita `timeout-minutes`** — o GitHub barra com "workflow file issue"; o timeout vai dentro do workflow reutilizável.
- **Paths filter do CI**: se a main tem *required status check* e o PR só toca arquivos fora do filtro (ex.: `README.md`), o PR fica `BLOCKED` para sempre — o check nunca reporta. Incluir `README.md` (e docs) no filtro do pull_request.
- **Merge de PR que toca `deploy.yml` enfileira atrás do gate de prod aberto** (concurrency) — o deploy seguinte fica `pending` até o gate anterior ser decidido. Avise o usuário: aprovar destrava a fila.

## Fase 5 — Proteção, governança e automação

Depois do fluxo funcionar, proteger o repo (é o que o MBA valoriza: o sistema que se governa):

- **Branch protection na main**: PR obrigatório + status check exigido (nome exato do check do CI) + `strict: true` + `enforce_admins: true` + sem force push. Configurar via API para não depender da UI:
  ```bash
  gh api -X PUT "repos/<owner>/<repo>/branches/main/protection" --input - <<'EOF'
  {
    "required_status_checks": {"strict": true, "contexts": ["<nome do check>"]},
    "enforce_admins": true,
    "required_pull_request_reviews": null,
    "restrictions": null,
    "allow_force_pushes": false,
    "allow_deletions": false
  }
  EOF
  ```
- **Dependabot** para actions (weekly) — a única falha de CI do exercício foi de versão de action; o Dependabot evita na fonte. Modelo: `examples/dependabot.yml`.
- **LICENSE** (MIT), **topics** (descobribilidade), **release/tag** (o padrão prega tag imutável — o repo pratica com `v1.0.0`).
- **Dogfood**: a PRIMEIRA mudança após proteger a main deve ser uma melhoria (auditoria), entrando por PR — prova que o fluxo funciona e fecha a história.

## Fase 6 — Auditoria do próprio ambiente

A verificação profunda é parte do exercício, não um extra. Auditar:
1. Proteção de branch (main sem proteção = push direto contorna tudo).
2. Testes do validador versionados (teste negativo ad-hoc é risco).
3. Regras que a ferramenta não valida (ex.: probe em porta que o container não expõe).
4. Higiene de CI (timeouts, duplicação, Dependabot, versões defasadas).
5. Documentação (runbook referenciado por anotação do artefato existe? ADRs? relatório?).
6. LICENSE/topics/release (repo público de portfólio).
7. Se o repo **nunca teve um PR**, o fluxo descrito no README é mentira até o primeiro PR.

Cada achado vira um group de melhoria (G1..Gn); aplicar tudo **por PR** com CI verde.

## Fase 7 — Documentação viva e entregáveis

- **README** com: badges (CI e CD), checklist de conformidade regra a regra, seção de entrega contínua (diagrama, gate, rollback), governança, "validar localmente".
- **docs/RUNBOOK.md** — o runbook que a anotação `*/*/runbook` do artefato promete (saúde, deploy, rollback, troubleshooting, segredos, escalação).
- **docs/DECISOES.md** — ADRs no formato contexto → decisão → consequência.
- **docs/RELATORIO-EXERCICIO.md** — método, provas (runs/IDs, asserções), lições.
- **Apresentação** (deck 13 slides: capa → problema → ideia central → método → repo → pipeline → provas → regra viva do documento → ADRs → lições → auditoria → evolução → fechamento) e **documentação em PDF** compilada (capa + README + runbook + ADRs + relatório).
- **QA honesto**: conferir conteúdo gerado por extração de texto (`pdftotext`) quando uma análise visual parecer estranha — análise de visão pode alucinar.

## Fase 2.5 — Ambiente do exercício: cluster local + ponte para o agente

Quando o exercício exigir cluster real e o agente rodar em sandbox (sem Docker/kind),
seguir o playbook testado em `references/playbook-ambiente-local-windows.md`. Resumo das
regras que não podem ser improvisadas:

- **Cluster**: kind dentro do Docker Desktop (Windows) — sem distro WSL; `kind create cluster --name <nome>`.
- **Ponte agente→cluster**: quick tunnel `cloudflared tunnel --url https://127.0.0.1:<porta> --no-tls-verify` — a ÚNICA combinação que funciona (http puro dá 400; https sem no-tls-verify dá 502 x509); URL nova a cada execução; `127.0.0.1` explícito, nunca `localhost`.
- **Auth pelo túnel**: client-cert NÃO atravessa (vira system:anonymous) — criar SA + token Bearer 24h e entregar o token por ARQUIVO anexo (colado no chat corrompe: caso real de 945 vs 944 chars); kubeconfig do agente com `insecure-skip-tls-verify: true`.
- **Imagens**: se o nó não alcança o Docker Hub (EOF no auth.docker.io), `docker pull` na máquina + `docker save` + `cmd /c "docker exec -i <nó> ctr --namespace=k8s.io images import - < tar"` (kind load buga com erro de digest); checar arquitetura da tag (arm64-only existe); env de caminho × volumeMounts precisa existir (emptyDir não cria subdiretório).
- **Fim da sessão**: revogar `kubectl delete clusterrolebinding <sa>` e fechar o túnel (Ctrl+C).
- **Entrega local**: usuário clona o repo do desafio para a pasta do projeto (pasta vazia/nova), com o caminho real do usuário no playbook.

## Recursos da skill

- **`references/aplicacao-real-metacortex.md`** — o caso real aplicado (linha do tempo do exercício Metacortex, erros que o pipeline pegou, métricas e checklist do deck) — ler para calibrar expectativas e colher exemplos.
- **`examples/validar-regras-casa.py`** — validador de policy as code funcional (base para a Camada 1).
- **`examples/workflow-validar-reutilizavel.yml`** — workflow reutilizável com camada 0 (pytest) + 3 camadas.
- **`examples/workflow-ci-pr.yml`** — CI de PR que chama o reutilizável (com paths includindo README).
- **`examples/workflow-deploy.yml`** — CD dev→stg→prod com gate, asserções e concorrência.
- **`examples/dependabot.yml`** — updates semanais de actions.

## Anti-padrões (não fazer)

- Subir tudo por push direto na main (o fluxo por PR é obrigatório — até para o assistente).
- Escrever YAML antes do checklist.
- Validador sem teste negativo versionado.
- Publicar repo sem LICENSE/topics/release.
- Configurar "3 camadas" no README quando o pipeline tem 4.
- Deixar o README descrever um fluxo que o repo não pratica.