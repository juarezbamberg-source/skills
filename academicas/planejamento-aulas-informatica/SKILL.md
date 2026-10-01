---
name: planejamento-aulas-informatica
description: This skill should be used when the user asks to "planejar aula", "gerar plano de aula", "criar exercícios", "roteiro de slides", "análise de lacunas", "guia noob" para curso técnico em informática (Senac) — ou citar UC5/UC6/UC7/UC8 de redes. Gera planejamento, exercícios contextualizados, roteiro de slides, análise de lacunas e guia noob com vídeos. As competências oficiais das UCs (indicadores, conhecimentos, habilidades) ficam em references/ (progressive disclosure); o fluxo pedagógico está neste corpo.
version: 0.2.0
---

> **Origem**: skill da plataforma Adapta ONE + 4 skills filhas de competências oficiais (UC5–UC8), importadas em 2026-10-01. As filhas viraram references. Usada no planejamento da UC5 (SENACRS Gravataí, 2026). Ainda sem validação de descoberta/execução neste agente (v0.x).

# SKILL: Planejamento de Aulas — Curso Técnico em Informática (3h/aula)

## OBJETIVO
Gerar planejamento de aulas, exercícios práticos, roteiros de slides, análise de lacunas e guia noob (versão simplificada com vídeos) para qualquer disciplina do curso técnico em informática, seguindo padrão pedagógico consistente e adaptável.

## FUNCIONALIDADES PRINCIPAIS
1. **Planejamento de aula** (Word/PDF) — objetivo, conteúdo teórico, metodologia, sequência didática, slides sugeridos, prática em sala, materiais, referências
2. **Exercícios práticos** — contextualizados em TI, com exemplos similares, resolução passo a passo e exercícios extras sem resposta
3. **Análise de lacunas** — identificar conteúdos faltantes, sugerir inserções no local adequado, citar fontes e vídeos
4. **Roteiro de slides** — títulos, tópicos principais, sugestão de fala do professor
5. **Guia Noob (documento de apoio ao aluno)** — versão simplificada e didática do conteúdo completo, com linguagem acessível para iniciantes, analogias do cotidiano, passo a passo visual e links de vídeos do YouTube para complementar o entendimento de cada tópico

## FLUXO DE USO

### Passo 1 — Coleta de informações
Ao receber o pedido, confirmar (máx. 3 questões via askQuestions se faltar):
- Disciplina/bloco e tema das aulas
- Carga horária (dias × horas-aula por dia)
- Quais entregáveis gerar (planejamento, slides, exercícios, lacunas, guia noob — seleção múltipla)

Se o usuário já forneceu esses dados na mensagem, NÃO perguntar de novo — executar diretamente.

### Passo 2 — Pesquisa de fontes
- Buscar na web fontes fidedignas: normas ABNT (NBR 5410, 5419), NRs (NR-10), documentos acadêmicos, IEEE, ANSI/TIA, ITU
- Priorizar fontes oficiais (.gov.br, ABNT, instituições de ensino)
- Citar TODAS as referências com link URL
- Buscar 1-2 vídeos do YouTube pertinentes quando útil

### Passo 3 — Geração de entregáveis
Gerar na ordem solicitada, um artefato por vez:
- Planejamento → usar documentGenerate
- Slides → usar presentation com textMode: "preserve"
- Exercícios → integrar ao planejamento ou gerar como documento separado
- Lacunas → usar documentUpdate para revisar o documento já gerado
- Guia Noob → usar documentGenerate (documento separado, voltado para o aluno)

## REGRAS DE CONSISTÊNCIA

### Estrutura do Planejamento (por aula/dia)
Cada dia de aula deve conter:
1. **Objetivo da aula** — capacidades que o aluno deverá demonstrar ao final
2. **Conteúdo teórico** — detalhado, com analogias do cotidiano; aproximadamente 40% do tempo
3. **Metodologia** — exposição dialogada + prática orientada ("aprender fazendo")
4. **Sequência didática** — tabela com tempo | atividade | descrição
5. **Slides sugeridos** — título do slide + tópicos principais + breve sugestão de fala
6. **Prática em sala** — estações ou atividades com tempo definido, materiais e procedimento detalhado; aproximadamente 60% do tempo
7. **Materiais necessários** — tabela com item, quantidade (para 20 alunos) e observação
8. **Referências** — lista numerada com link URL das fontes

### Linguagem
- Português técnico, formal e didático
- Público-alvo: alunos de curso técnico em informática
- Analogias do cotidiano para conceitos abstratos (ex: pressão da água = tensão)
- Explicar termos técnicos na primeira menção
- Sem jargão excessivo

### Proporção teoria/prática (3h/aula)
- ~40% teoria (~1h), ~60% prática (~2h)
- Práticas com materiais acessíveis em sala de aula
- Tempo equilibrado entre estações/atividades (25-30 min cada)
- Incluir checklist de avaliação ou relatório como instrumento de avaliação

### Slides
- Usar textMode: "preserve" quando o usuário fornecer o conteúdo dos slides
- Máximo 25 slides por conjunto
- Idioma: pt-br
- Tom: educational
- Template: modern
- Sem table of contents
- Com slide de título

### Exercícios
- Contextualizados em TI (servidores, switches, racks, data centers, cabos, PoE, UPS)
- Incluir exemplo similar resolvido antes de cada exercício
- Resolução passo a passo (para o professor)
- Incluir 2 exercícios extras sem resposta para resolução em sala
- Fórmulas matemáticas com $$ delimitadores

### Guia Noob (Documento de Apoio ao Aluno)
- Linguagem simples, acessível e amigável (como conversar com um iniciante)
- Cada conceito explicado com: definição simples + analogia do cotidiano + exemplo prático em TI
- Para cada tópico principal, incluir 1-2 links de vídeos do YouTube que ajudem a entender
- Incluir "dicas do professor" (boxes com conselhos práticos)
- Incluir "cuidado!" (boxes com avisos de segurança ou erros comuns)
- Formato visual: usar caixas de destaque, ícones, tabelas simples
- Estruturar por aula/dia, seguindo a mesma sequência do planejamento
- Incluir glossário no final com os termos técnicos
- O objetivo é que um aluno com zero conhecimento prévio consiga entender o conteúdo

### Análise de Lacunas
- Comparar conteúdo enviado vs. referências pesquisadas
- Para cada lacuna: identificar, sugerir inserção, citar fontes e vídeos
- Usar documentUpdate para integrar as lacunas ao documento já gerado

## PARÂMETROS ADAPTÁVEIS
- Número de dias/aulas: conforme input do usuário
- Carga horária por aula: conforme input do usuário (padrão: 3h/aula)
- Disciplina: qualquer do curso técnico em informática
- Entregáveis: selecionáveis pelo usuário a cada uso

- Nome do professor: Juarez Bamberg

## OBSERVAÇÕES PEDAGÓGICAS
- Sempre incluir avaliação formativa (checklist, observação) e somativa (relatório, prova)
- Sugerir recursos complementares: simuladores (PhET), vídeos técnicos, visitas
- Ao final do planejamento, incluir seção de observações gerais e sugestões de avaliação
- Apontar lacunas no conteúdo recebido e sugerir complementações

## EXEMPLO DE APLICAÇÃO
Usuário envia: "Conteúdo do bloco de Redes de Computadores, 2 aulas de 3h, gerar planejamento e slides."
Fluxo:
1. Confirmar dados (já fornecidos — não perguntar)
2. Pesquisar metodologias e fontes sobre redes de computadores
3. Gerar planejamento em Word com estrutura completa
4. Gerar slides com textMode: preserve, máximo 25 slides, pt-br, educational

## References — competências oficiais (carregar só a UC em questão)

- [`references/uc5.md`](references/uc5.md) — UC5 Instalação de Redes Locais (96h): indicadores, conhecimentos, habilidades, atitudes
- [`references/uc6.md`](references/uc6.md) — UC6 Manutenção de Redes Locais (96h)
- [`references/uc7.md`](references/uc7.md) — UC7 Servidores de Redes Locais (96h)
- [`references/uc8.md`](references/uc8.md) — UC8 Projeto Integrador (20h): fases e temas geradores
