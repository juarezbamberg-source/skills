# skills

Skills do meu agente pessoal (leao, rodando sobre GLM). Cada skill nasce de um **fluxo executado de verdade** — primeiro resolve a tarefa com o agente, depois empacota o que funcionou. Skill escrita de cabeça não entra aqui (as legadas ficam em v0.x até serem validadas).

[![Validar skills](https://github.com/juarezbamberg-source/skills/actions/workflows/validar-skills.yml/badge.svg)](https://github.com/juarezbamberg-source/skills/actions/workflows/validar-skills.yml) ![Skills](https://img.shields.io/badge/skills-11-8a2be2) ![Validadas](https://img.shields.io/badge/validadas-1-4c1) ![Legadas](https://img.shields.io/badge/legadas_v0.x-10-f9a825)

## Organização (por finalidade)

```
skills/
├── brainstorm/                   # maturação de ideias (raiz: porta de entrada do arco de spec)
├── spec-prd-trd-adr/             # entrevista + PRD/TRD/ADR (raiz: transversal, usada no Desafio 03)
├── exercicio-devops-cloud-ia/    # metodologia completa de exercícios (raiz: transversal)
├── tecnicas/                     # infraestrutura e operação
│   ├── containers-docker-kubernetes/   # Docker + K8s: escrita e auditoria (fusão 2026-10-01)
│   ├── analise-remediacao-incidentes/  # incidentes de produção gerais + post-mortem
│   └── gerar-terraform/                # estrutura modular de Terraform
├── catolicas/                    # conteúdo católico
│   └── framework-care/                 # pregação + adoração + homilia (3 aplicações do C-A-R-E)
└── academicas/                   # trabalho acadêmico e docência
    ├── planejamento-aulas-informatica/ # aulas + UC5-8 (competências oficiais em references/)
    ├── criar-provas-senac/             # criação de provas SENAC
    ├── avaliador-trabalhos-senac/      # avaliação de trabalhos por UC
    ├── analise-textual-academica/      # validação de conformidade textual
    └── tcc-ava-ia/                     # TCC de plataforma AVA com IA
```

## Skills validadas (raiz — fluxo executado comprovado)

| Skill | Versão | O que faz | Origem |
|---|---|---|---|
| [`exercicio-devops-cloud-ia/`](exercicio-devops-cloud-ia/) | 1.1.0 | Método completo para transformar enunciado/padrão em repo sustentável: spec primeiro, policy as code, CI/CD com gate humano, auditoria. Inclui playbook de ambiente (kind no Windows + túnel cloudflared + auth por token). | Exercício Metacortex (MBA DevOps) + Desafio 03 |

## Raiz — transversais (spec e metodologia)

| Skill | Versão | O que faz | Status |
|---|---|---|---|
| [`brainstorm/`](brainstorm/) | 0.2.0 | Maturação colaborativa de ideias ANTES de especificar: entender → análise crítica → iterar → fechamento com decisões e pontos em aberto. Porta de entrada do arco de spec. | Adapta ONE (ativa); usada no Desafio 03 |
| [`spec-prd-trd-adr/`](spec-prd-trd-adr/) | 0.2.0 | Entrevista guiada (máx. 3 perguntas/rodada) e geração de PRD/TRD/ADR reutilizáveis. Playbook no corpo; templates fixos em `references/`. | Adapta ONE (ativa); base dos specs do Desafio 03 |

## tecnicas/ — infraestrutura e operação

| Skill | Versão | O que faz | Status |
|---|---|---|---|
| [`containers-docker-kubernetes/`](tecnicas/containers-docker-kubernetes/) | 0.2.0 | Dois modos: escrita (containerizar app + manifests K8s lendo o projeto) e auditoria (revisar/comparar Dockerfiles com notas e tabela comparativa). | Legado, fundida de 2 skills; pendente de validação |
| [`analise-remediacao-incidentes/`](tecnicas/analise-remediacao-incidentes/) | 0.2.0 | Incidentes de produção em geral: triagem → diagnóstico (cadeia causal) → remediação em 2 fases (parar o sangramento / correção definitiva) → validação → post-mortem. | Legado; pendente de validação |
| [`gerar-terraform/`](tecnicas/gerar-terraform/) | 0.1.0 | Estrutura modular e reutilizável de Terraform (providers, variables, modules) para qualquer cloud. | Legado; pendente de validação |

## catolicas/ — conteúdo católico

| Skill | Versão | O que faz | Status |
|---|---|---|---|
| [`framework-care/`](catolicas/framework-care/) | 0.3.0 | Framework C-A-R-E com três aplicações: pregação, adoração ao Santíssimo Sacramento e homilia (10 min). Corpo tem o núcleo; roteiros completos em `references/`. | Adapta ONE + fusões; pendente de validação |

## academicas/ — trabalho acadêmico e docência

| Skill | Versão | O que faz | Status |
|---|---|---|---|
| [`planejamento-aulas-informatica/`](academicas/planejamento-aulas-informatica/) | 0.2.0 | Planejamento de aulas, exercícios, slides, análise de lacunas e guia noob para técnico em informática. Competências oficiais UC5–UC8 em `references/`. | Adapta ONE + fusão; pendente de validação |
| [`criar-provas-senac/`](academicas/criar-provas-senac/) | 0.2.0 | Criação de provas SENAC: brainstorm inicial, versões por grupo, gabarito, rubrica, ficha de assinatura e entrega por e-mail. | Adapta ONE; pendente de validação |
| [`avaliador-trabalhos-senac/`](academicas/avaliador-trabalhos-senac/) | 0.2.0 | Avaliador de trabalhos por UC: brainstorm da rodada, rubrica-base, correção por evidências, SWOT e parecer. | Adapta ONE; pendente de validação |
| [`analise-textual-academica/`](academicas/analise-textual-academica/) | 0.2.0 | Validação de conformidade textual de entregas acadêmicas (com detecção de tipo de arquivo — não avalia slides). | Adapta ONE; pendente de validação |
| [`tcc-ava-ia/`](academicas/tcc-ava-ia/) | 0.1.0 | Estrutura e validação de TCC de plataforma AVA inteligente (RAG, visão computacional, análise comportamental). | Adapta ONE; pendente de validação |

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

## Validação contínua (CI)

A cada push/PR, o workflow `validar-skills.yml` verifica:
1. **Frontmatter** de todo SKILL.md: `name`, `description` (≥150 chars — gatilho de descoberta) e `version`.
2. **Permissões**: toda skill declara o que pede e o que **não** pede (seção "Permissões que a skill pede") — skills que agem no mundo (e-mail, infra, arquivos) são auditáveis.
3. **Histórico**: toda skill tem `## Histórico` no rodapé (registro de falhas e mudanças entra aí — a skill viva).
2. **Referências internas**: todo link `references/...` aponta para arquivo existente; skills irmãs citadas existem no repo.


**Método de manutenção** (aplicado via brainstorm 2026-10-01): skills geradoras têm critério de prontidão e saída esperada; M5 (idioma único nas descriptions) foi avaliado e **descartado** — o mix EN/PT funciona no roteamento atual e o custo de mexer em 14 arquivos não se justifica.

## Nota de escopo (2026-10-09)

As skills do desafio Metacortex (padrão de manifests e triagem de cluster) foram **removidas deste repo** — são entregas específicas do exercício e vivem no repo dele: [juarezbamberg-source/Sistemas-Metacortex](https://github.com/juarezbamberg-source/Sistemas-Metacortex) (ticket-01 e ticket-02). Este repo mantém apenas skills de uso geral e transversais.

## Uso

As skills são lidas pelo agente (leao) via `find_installed_skills` → `read_file`. Para instalar em outro agente compatível (Claude Code, picoclaw), copiar a pasta da skill para `skills/<nome>/`.

## Agente e modelos

- **Agente**: leao (assistente pessoal, sandbox arm64 Linux)
- **Modelo**: GLM (via Z.ai)
