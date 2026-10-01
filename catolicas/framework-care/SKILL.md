---
name: framework-care
description: This skill should be used when the user asks to "gerar pregação", "homilia para o domingo", "preparar adoração ao Santíssimo Sacramento", "adoro-te devote", "meditações para adoração", "pregação com as leituras do dia", or mentions framework C-A-R-E para conteúdo católico (Contexto, Análise/Arquitetura, Reflexão/Roteiro, Encerramento/Execução). Três aplicações: pregação (leituras do dia), adoração (meditações + músicas, 45-50 min) e homilia (10 min, 900-1.100 palavras). O framework comum está neste corpo; os roteiros específicos ficam em references/ (progressive disclosure). NÃO usar para brainstorm de ideias gerais (usar brainstorm/) — este framework é específico de conteúdo católico falado/cantado.
version: 0.3.0
---

> **Origem**: fusão de duas skills legadas da plataforma anterior (pregacao-framework-care + adorote-devote, pasta Drive "skills-Adapta/inativas"), consolidadas em 2026-10-01. O framework C-A-R-E é comum às duas; o que muda é a aplicação — cada roteiro completo vive em `references/`. Ainda sem validação de descoberta/execução neste agente (v0.x).

# Framework C-A-R-E para conteúdo católico

Framework para estruturar conteúdo católico falado/cantado: **C**ontexto, **A** (Análise ou Arquitetura, conforme a aplicação), **R** (Reflexão ou Roteiro), **E** (Encerramento ou Execução).

## Qual aplicação usar?

| Se o pedido for… | Use o reference | Estrutura |
|---|---|---|
| Pregação a partir das leituras do dia | [`references/pregacao.md`](references/pregacao.md) | Contexto → Análise → Reflexão → Encerramento |
| Adoração ao Santíssimo Sacramento (radiofônica ou presencial) | [`references/adoracao.md`](references/adoracao.md) | Contexto → Arquitetura (progressão espiritual) → Roteiro → Execução |
| Homilia (pregação oral de exatamente 10 min, 900–1.100 palavras) | [`references/homilia.md`](references/homilia.md) | Contexto → Análise → Reflexão → Encerramento |

## Núcleo comum do framework

- **C — Contexto**: estabelecer o cenário espiritual, integrar as leituras/tema, conectar com a realidade do ouvinte. Tom introdutório e envolvente.
- **A — Análise/Arquitetura**: aprofundar o significado (pregação) ou definir a progressão espiritual em etapas (adoração). Sempre com base textual (leituras, passagens bíblicas).
- **R — Reflexão/Roteiro**: provocar o ouvinte com questões e desafios práticos (pregação) ou roteirizar cada meditação com elementos obrigatórios (adoração).
- **E — Encerramento/Execução**: convite à transformação/ação (pregação) ou estrutura técnica da transmissão com tempos e transições (adoração).

## Regras de ouro (valem para as duas aplicações)

1. **Linguagem poética mas acessível** — profundidade sem rebuscamento.
2. **Base textual sempre citada** — leitura bíblica integrada organicamente, nunca decorativa.
3. **Tempos respeitados** — pregação 8–10 min de leitura; meditação 4–5 min; os detalhes de timing estão nos references.
4. **Tom escolhido pelo usuário** — Inspirador, Reflexivo, Desafiador, Consolador, Exortativo, Contemplativo, Empático, Redentor, ou customizado.
5. **Pausas são conteúdo** — silêncio e respiração fazem parte do roteiro, não são vazio.

## Entrada esperada

- Leituras: Evangelho do dia, Primeira Leitura, Salmo, Leitura Livre (referência digitada).
- Tom: lista acima ou descrição customizada.
- Para adoração: duração total (padrão 45–50 min, 6 meditações + 6 músicas).
