# skills

Skills do meu agente pessoal (leao, rodando sobre GLM). Cada skill nasce de um **fluxo executado de verdade** — primeiro resolve a tarefa com o agente, depois empacota o que funcionou. Skill escrita de cabeça não entra aqui (as legadas ficam em v0.x até serem validadas).

![Skills](https://img.shields.io/badge/skills-8-8a2be2) ![Validadas](https://img.shields.io/badge/validadas-3-4c1) ![Legadas](https://img.shields.io/badge/legadas_v0.x-5-f9a825)

## Organização (por finalidade)

```
skills/
├── exercicio-devops-cloud-ia/    # metodologia completa de exercícios (raiz: transversal)
├── padrao-manifests-metacortex/  # manifests K8s da casa (raiz: validada em fluxo real)
├── triagem-cluster-metacortex/   # triagem de cluster K8s (raiz: validada em fluxo real)
├── tecnicas/                     # infraestrutura e operação
│   ├── containers-docker-kubernetes/   # Docker + K8s: escrita e auditoria (fusão 2026-10-01)
│   ├── analise-remediacao-incidentes/  # incidentes de produção gerais + post-mortem
│   └── gerar-terraform/                # estrutura modular de Terraform
├── catolicas/                    # conteúdo católico
│   └── framework-care/                 # pregação + adoração (fusão 2026-10-01)
└── academicas/                   # trabalho acadêmico
    └── tcc-ava-ia/                     # TCC de plataforma AVA com IA
```

## Skills validadas (raiz — fluxo executado comprovado)

| Skill | Versão | O que faz | Origem |
|---|---|---|---|
| [`exercicio-devops-cloud-ia/`](exercicio-devops-cloud-ia/) | 1.1.0 | Método completo para transformar enunciado/padrão em repo sustentável: spec primeiro, policy as code, CI/CD com gate humano, auditoria. Inclui playbook de ambiente (kind no Windows + túnel cloudflared + auth por token). | Exercício Metacortex (MBA DevOps) + Desafio 03 |
| [`padrao-manifests-metacortex/`](padrao-manifests-metacortex/) | 1.0.0 | Gera e confere manifests Kubernetes no padrão da casa. Script para regras mecânicas, instrução para o que exige ler o projeto, mapeamento Trivy para não reimplementar. | Desafio 03, Ticket 01 |
| [`triagem-cluster-metacortex/`](triagem-cluster-metacortex/) | 1.0.0 | Método único de triagem de incidentes Kubernetes: sintoma → camadas fixas → cruzamento de fontes → veredito de 4 linhas. Só leitura. | Desafio 03, Ticket 02 |

## tecnicas/ — infraestrutura e operação

| Skill | Versão | O que faz | Status |
|---|---|---|---|
| [`containers-docker-kubernetes/`](tecnicas/containers-docker-kubernetes/) | 0.2.0 | Dois modos: escrita (containerizar app + manifests K8s lendo o projeto) e auditoria (revisar/comparar Dockerfiles com notas e tabela comparativa). | Legado, fundida de 2 skills; pendente de validação |
| [`analise-remediacao-incidentes/`](tecnicas/analise-remediacao-incidentes/) | 0.2.0 | Incidentes de produção em geral: triagem → diagnóstico (cadeia causal) → remediação em 2 fases (parar o sangramento / correção definitiva) → validação → post-mortem. | Legado; pendente de validação |
| [`gerar-terraform/`](tecnicas/gerar-terraform/) | 0.1.0 | Estrutura modular e reutilizável de Terraform (providers, variables, modules) para qualquer cloud. | Legado; pendente de validação |

## catolicas/ — conteúdo católico

| Skill | Versão | O que faz | Status |
|---|---|---|---|
| [`framework-care/`](catolicas/framework-care/) | 0.2.0 | Framework C-A-R-E com duas aplicações: pregação (a partir das leituras do dia) e adoração ao Santíssimo Sacramento (meditações + músicas). Corpo tem o núcleo; roteiros completos em `references/`. | Legado, fundida de 2 skills; pendente de validação |

## academicas/ — trabalho acadêmico

| Skill | Versão | O que faz | Status |
|---|---|---|---|
| [`tcc-ava-ia/`](academicas/tcc-ava-ia/) | 0.1.0 | Estrutura e validação de TCC de plataforma AVA inteligente (RAG, visão computacional, análise comportamental): checklists por capítulo, metodologia, métricas. | Legado; pendente de validação |

## Progressive disclosure (regra do repo)

Skills grandes **não** colocam tudo no corpo do SKILL.md. O corpo tem: gatilhos (description), o essencial do método e a rota para os arquivos de detalhe. O detalhe vive em `references/` (consultado sob demanda) e artefatos prontos em `examples/`. **Ao fundir skills, o corpo fundido fica enxuto e os corpos originais viram references** — nunca concatenar tudo no corpo.

## Estrutura de cada skill

```
<skill>/
├── SKILL.md          # corpo: gatilhos, método essencial, rota para references
├── scripts/          # regras mecânicas (código determinístico)
├── references/       # consultado sob demanda (roteiros, playbooks, casos reais)
└── examples/         # artefatos funcionais prontos para copiar
```

## Controle de versão

- Cada SKILL.md tem `version:` no frontmatter — **patch** para correção de texto, **minor** para nova fase/reference, **major** para mudança de método.
- Mudanças de método entram por commit com a lição que motivou (o "porquê" fica no histórico).
- A origem de cada skill fica registrada na própria skill (seção "Origem") — skill sem fluxo executado por trás não é skill, é palpite.
- **Legadas (v0.x)**: promovidas a 1.x somente após fluxo executado validado neste agente.

## Roteamento entre skills (descrições cruzadas)

As descrições delimitam território para o agente não carregar a skill errada:
- **triagem-cluster-metacortex** × **analise-remediacao-incidentes**: triagem K8s só-leitura ≠ incidente geral com remediação/post-mortem — cada descrição aponta a outra no "NÃO usar para".
- **padrao-manifests-metacortex** × **containers-docker-kubernetes**: padrão da casa (escrita/conferência de manifests) ≠ containerização genérica — a de manifests prevalece para manifests da casa.

## Uso

As skills são lidas pelo agente (leao) via `find_installed_skills` → `read_file`. Para instalar em outro agente compatível (Claude Code, picoclaw), copiar a pasta da skill para `skills/<nome>/`.

## Agente e modelos

- **Agente**: leao (assistente pessoal, sandbox arm64 Linux)
- **Modelo**: GLM (via Z.ai)
