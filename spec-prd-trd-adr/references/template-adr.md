# Template ADR — Architecture Decision Record

Filha da skill #Geração de PRD, TRD e ADR. Carregar SOMENTE quando houver uma decisão de arquitetura a registrar (stack, containerização, orquestração, banco). A entrevista e as regras globais de qualidade já estão no playbook pai — não repetir.

## Template obrigatório (frontmatter YAML)
---
adr_number: "NNN"
status: aceito
created: YYYY-MM-DD
supersedes: ""
superseded_by: ""
---

# ADR NNN: Título da decisão em uma linha

## Contexto
Problema, restrições e forças em jogo.

## Alternativas Consideradas
Cada opção com prós e contras (mínimo 2).

## Decisão
Escolha clara, com a razão que pesou mais.

## Consequências
Positivas / Negativas / Neutras (trade-offs aceitos).

## Regras
- Um ADR por decisão de arquitetura.
- Registrar apenas o verificado; o que não puder ser confirmado vira "[A CONFIRMAR]", nunca valor inventado.
- Incluir "Fontes:" ao final quando houver repositório/documento de referência.

## Checklist antes de entregar
- [ ] Frontmatter YAML completo (número, status, data).
- [ ] Alternativas com prós e contras (mínimo 2).
- [ ] Decisão clara com a razão que pesou mais.
- [ ] Consequências positivas E negativas.
- [ ] Supersedes/superseded_by preenchidos quando aplicável.
- [ ] Fontes citadas quando existirem.
