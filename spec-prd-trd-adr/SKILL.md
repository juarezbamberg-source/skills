---
name: spec-prd-trd-adr
description: This skill should be used when the user asks to "gerar PRD", "gerar TRD", "escrever ADR", "criar documento de requisitos", "especificar projeto/feature", "registrar decisão de arquitetura", ou fala em "spec-driven development", "PRD/TRD/ADR", "OpenSpec". Entrevista guiada (máx. 3 perguntas por rodada) e geração dos artefatos de spec reutilizáveis em qualquer domínio. O playbook (entrevista + roteamento + regras de qualidade) está neste corpo; as estruturas fixas de cada artefato ficam em references/ (progressive disclosure — carregar só o template necessário).
version: 0.2.0
---

> **Origem**: skill da plataforma Adapta ONE (playbook pai + 3 filhas: Template PRD, Template TRD, Template ADR). Importada e reorganizada em uma skill com references em 2026-10-01. Usada como base do arco de spec do Desafio 03 (PRDs/TRDs/ADRs dos Tickets 03 e 04 seguem este método).

# Geração de PRD, TRD e ADR — Playbook Pai (progressive disclosure)

## Objetivo
Entrevistar o usuário sobre um novo projeto ou feature e gerar os artefatos de Spec-Driven Development: PRD (Product Requirements Document), TRD (Technical Requirements Document) e ADR(s) (Architecture Decision Records). Reutilizável em qualquer domínio (software, infraestrutura, processos, serviços).

## Escopo
- USAR: projeto ou feature novo com requisitos a especificar; pedido explícito de PRD, TRD ou ADR; decisão de arquitetura a registrar.
- NÃO USAR: dúvida conceitual simples (responda direto), pedido de código, documentação de sistema legado sem decisões novas.

## Regras globais de qualidade (aplicar SEMPRE)
- Nada implícito: se não está escrito, não existe.
- Critérios verificáveis: números, não adjetivos ("rápido" → "responde em < 200 ms").
- Consistência entre artefatos: regra do PRD aparece como restrição técnica no TRD; decisão de arquitetura referenciada no ADR.
- Consistência interna: spec e dados de exemplo devem concordar.
- Lacuna declarada vale mais que suposição: sinalize "[A CONFIRMAR]", nunca invente valor.

## Fase 1 — Entrevista (iterativa)
1. Máximo 3 perguntas por rodada, começando pelas mais importantes. Nunca despeje todas de uma vez.
2. Tópicos na ordem: contexto do produto (o quê, para quem, dor, custo de não fazer) → usuários e papéis (quem cria/edita/exclui/consulta; login ou acesso público) → regras de negócio (validações, limites, allowlist, conflito/duplicidade) → escopo (in-scope e out-of-scope) → ambiente técnico (stack, projeto-base, deploy) → requisitos não-funcionais (desempenho, disponibilidade, segurança).
3. Quando o usuário não souber decidir, proponha a opção mais sensata COM justificativa e aguarde confirmação.
4. Nunca invente regra: se o usuário não mencionou, pergunte; se ainda faltar, marque "[A CONFIRMAR]".

## Roteamento — qual filha carregar
Decida pela intenção do pedido e carregue SOMENTE a(s) filha(s) necessária(s) — nunca todas:
- Foco em produto (o quê, público, regras de negócio, critérios de aceite) → carregar a filha Template PRD.
- Foco em solução (arquitetura, contratos, modelo de dados, testes) → carregar a filha Template TRD.
- Decisão de arquitetura a registrar (stack, banco, containerização, orquestração) → carregar a filha Template ADR.
- Pedido combinado (ex.: "PRD + TRD") → carregar as filhas correspondentes ao mesmo pedido.
- Dúvida conceitual ou pedido simples → responder só com este playbook, sem carregar filha.

## Prontidão
Contexto suficiente quando objetivo, público, escopo e restrições principais estão definidos (ou marcados como "[A CONFIRMAR]"). Encerre a entrevista quando novas perguntas não mudarem decisões relevantes.

## Formato de entrega
- Artefatos em markdown estruturado, prontos para copiar em arquivos.
- Se o usuário pedir Word/PDF, gere documento formatado.
- Encerre com próximos passos concretos (ex.: transformar critérios de aceite em spec OpenSpec com capabilities/requirements/scenarios).

## References (estruturas fixas — carregar só a necessária)

- [`references/template-prd.md`](references/template-prd.md) — 6 seções, critérios de aceite Gherkin, regras de allowlist e checklist.
- [`references/template-trd.md`](references/template-trd.md) — NFRs quantificados, arquitetura/contratos, modelo de dados, stack verificada.
- [`references/template-adr.md`](references/template-adr.md) — frontmatter YAML, contexto, alternativas (mín. 2), decisão, consequências, fontes.
