# skills

Skills do meu agente pessoal (leao, rodando sobre GLM). Cada skill nasce de um **fluxo executado de verdade** — primeiro resolvo a tarefa com o agente, depois empacoto o que funcionou. Skill escrita de cabeça não entra aqui.

## Skills

| Skill | Versão | O que faz | Origem |
|---|---|---|---|
| [`exercicio-devops-cloud-ia/`](exercicio-devops-cloud-ia/) | 1.1.0 | Método completo para transformar enunciado/padrão em repo sustentável: spec primeiro, policy as code, CI/CD com gate humano, auditoria. Inclui playbook de ambiente (kind no Windows + túnel cloudflared + auth por token). | Exercício Metacortex (MBA DevOps) + Desafio 03 |
| [`padrao-manifests-metacortex/`](padrao-manifests-metacortex/) | 1.0.0 | Gera e confere manifests Kubernetes no padrão da casa. Script para regras mecânicas, instrução para o que exige ler o projeto, mapeamento Trivy para não reimplementar. | Desafio 03, Ticket 01 |
| [`triagem-cluster-metacortex/`](triagem-cluster-metacortex/) | 1.0.0 | Método único de triagem de incidentes Kubernetes: sintoma → camadas fixas → cruzamento de fontes → veredito de 4 linhas. Só leitura. | Desafio 03, Ticket 02 |

## Skills legadas (importadas da plataforma anterior)

Exportadas da pasta Drive "skills-Adapta/inativas" e consolidadas aqui em 2026-10-01. Estão em **v0.1.0** — status legado "inativa/backup", ainda sem validação de descoberta/execução neste agente. A origem está marcada no topo de cada SKILL.md; conforme forem usadas e validadas em fluxos reais, ganham versão 1.x e saem desta lista.

| Skill | Tema |
|---|---|
| [`adorote-devote/`](adorote-devote/) | Framework CARE para adoração ao Santíssimo Sacramento |
| [`ambiente-docker-kubernetes/`](ambiente-docker-kubernetes/) | Containerização Docker + deploy Kubernetes |
| [`analise-remediacao-incidentes/`](analise-remediacao-incidentes/) | Triagem, diagnóstico, remediação e post-mortem de incidentes |
| [`auditoria-dockerfiles/`](auditoria-dockerfiles/) | Auditoria comparativa de Dockerfiles |
| [`gerar-terraform/`](gerar-terraform/) | Estrutura modular e reutilizável de Terraform |
| [`pregacao-framework-care/`](pregacao-framework-care/) | Pregações estruturadas no framework C-A-R-E |
| [`tcc-ava-ia/`](tcc-ava-ia/) | Estrutura e validação de TCC de AVA inteligente com IA |

## Estrutura de cada skill

```
<skill>/
├── SKILL.md          # corpo: método, curadoria, permissões, origem
├── scripts/          # regras mecânicas (código determinístico)
├── references/       # consultado sob demanda (mapeamentos, playbooks, casos reais)
└── examples/         # artefatos funcionais prontos para copiar
```

## Controle de versão

- Cada SKILL.md tem `version:` no frontmatter — **patch** para correção de texto, **minor** para nova fase/reference, **major** para mudança de método.
- Mudanças de método entram por commit com a lição que motivou (o "porquê" fica no histórico).
- A origem de cada skill fica registrada na própria skill (seção "Origem") — skill sem fluxo executado por trás não é skill, é palpite.

## Uso

As skills são lidas pelo agente (leao) via `find_installed_skills` → `read_file`. Para instalar em outro agente compatível (Claude Code, picoclaw), copiar a pasta da skill para `skills/<nome>/`.

## Agente e modelos

- **Agente**: leao (assistente pessoal, sandbox arm64 Linux)
- **Modelo**: GLM (via Z.ai)
