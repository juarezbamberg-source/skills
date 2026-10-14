---
name: planejamento-aulas-informatica
description: "Use quando o usuário pedir para \"planejar aula\", \"plano de aula\", \"gerar exercícios práticos\", \"roteiro de slides\", \"análise de lacunas do conteúdo\", \"guia noob para alunos\", \"material didático para o técnico em informática\", ou mencionar UC5/UC6/UC7/UC8 de redes ou UC9/UC10 de desenvolvimento de sistemas (SENAC). Gera planejamento (DOCX/PDF), exercícios contextualizados em TI, roteiro de slides, análise de lacunas com fontes e guia noob com vídeos. Competências oficiais das UCs ficam em references/ (progressive disclosure: carregar só a UC em questão). NÃO usar para criar provas nem avaliar entregas."
version: 0.4.0
---

> **Origem**: skill da plataforma Adapta ONE + 4 skills filhas de competências oficiais (UC5–UC8), importadas em 2026-10-01 e adaptadas a esta plataforma em 2026-10-14. Usada no planejamento da UC5 (SENACRS Gravataí, 2026) e na produção do Bloco 7 (segurança).

# SKILL: Planejamento de Aulas — Curso Técnico em Informática (3h/aula)

## TÉCNICA: PROGRESSIVE DISCLOSURE

O corpo deste SKILL.md é o **núcleo** — regras estáveis que valem para toda UC. Os detalhes pesados (competências oficiais de cada UC) vivem em `references/` e **só são carregados quando necessários**:

1. A descrição do frontmatter e este arquivo entram no contexto na descoberta — nada mais.
2. Identificada a UC do pedido, chame `read_file` **apenas** em `skills/planejamento-aulas-informatica/references/ucN.md` (N = 5, 6, 7, 8, 9 ou 10). NUNCA carregue todas de uma vez.
3. Se o pedido cobrir mais de uma UC (ex.: projeto integrador UC5+UC8), carregue só as citadas.
4. Se o pedido não citar UC (tema solto de informática), NÃO carregue reference nenhuma — o núcleo basta.

Assim o contexto não infla e a skill escala para novas UCs: adicionar `references/ucN.md` é só criar o arquivo.

## OBJETIVO
Gerar planejamento de aulas, exercícios práticos, roteiros de slides, análise de lacunas e guia noob (versão simplificada com vídeos) para qualquer disciplina do curso técnico em informática, seguindo padrão pedagógico consistente e adaptável.

## FUNCIONALIDADES PRINCIPAIS
1. **Planejamento de aula** (DOCX/PDF) — objetivo, conteúdo teórico, metodologia, sequência didática, slides sugeridos, prática em sala, materiais, referências
2. **Exercícios práticos** — contextualizados em TI, com exemplos similares, resolução passo a passo e exercícios extras sem resposta
3. **Análise de lacunas** — identificar conteúdos faltantes, sugerir inserções no local adequado, citar fontes e vídeos
4. **Roteiro de slides** — títulos, tópicos principais, sugestão de fala do professor
5. **Guia Noob** (documento de apoio ao aluno) — versão simplificada e didática, linguagem acessível, analogias do cotidiano, passo a passo visual e links de vídeos do YouTube

## FLUXO DE USO

### Passo 1 — Coleta de informações
Confirmar (máx. 3 perguntas; no web use um único `Form` do openui):
- Disciplina/bloco e tema das aulas
- Carga horária (dias × horas-aula por dia)
- Quais entregáveis gerar (planejamento, slides, exercícios, lacunas, guia noob — múltipla escolha)

Se o usuário já forneceu esses dados na mensagem, NÃO pergunte de novo — execute direto.

### Passo 2 — Carregar a referência da UC (progressive disclosure)
Se houver UC citada (UC5–UC10): `read_file` em `references/ucN.md` e use seus indicadores/conhecimentos/habilidades/valores como fonte de requisitos. Indicadores → eixos de avaliação; conhecimentos → teoria; habilidades → práticas; atitudes/valores → avaliação formativa.

### Passo 3 — Pesquisa de fontes
- Buscar na web fontes fidedignas: normas ABNT (NBR 5410, 5419), NRs (NR-10), documentos acadêmicos, IEEE, ANSI/TIA, ITU
- Priorizar fontes oficiais (.gov.br, ABNT, instituições de ensino)
- Citar TODAS as referências com link URL
- Buscar 1-2 vídeos do YouTube pertinentes quando útil

### Passo 4 — Geração de entregáveis
Gerar na ordem solicitada, um artefato por vez. Ferramentas desta plataforma:
- **Planejamento** → DOCX (skill `docx` ou python-docx; padrão de cabeçalho SENACRS como nos roteiros do Bloco 7 da UC5)
- **Slides** → PPTX (skill `pptx`/pptxgenjs) ou HTML→PDF (skill `presentations`) para maior qualidade visual; máximo 25 slides por conjunto
- **Exercícios** → integrar ao planejamento ou gerar documento separado
- **Lacunas** → revisar o documento já gerado (ou entregar seção separada)
- **Guia Noob** → DOCX separado, voltado para o aluno
- Entregar tudo em `artifacts/` e exibir com `share_file`/`send_file`

## REGRAS DE CONSISTÊNCIA

### Estrutura do Planejamento (por aula/dia)
1. **Objetivo da aula** — capacidades que o aluno deverá demonstrar ao final
2. **Conteúdo teórico** — detalhado, com analogias do cotidiano; ~40% do tempo
3. **Metodologia** — exposição dialogada + prática orientada ("aprender fazendo")
4. **Sequência didática** — tabela tempo | atividade | descrição
5. **Slides sugeridos** — título + tópicos principais + breve sugestão de fala
6. **Prática em sala** — estações/atividades com tempo definido, materiais e procedimento; ~60% do tempo
7. **Materiais necessários** — tabela item | quantidade (para 20 alunos) | observação
8. **Referências** — lista numerada com link URL das fontes

### Linguagem
- Português técnico, formal e didático; público: alunos de curso técnico em informática
- Analogias do cotidiano para conceitos abstratos (ex.: pressão da água = tensão)
- Explicar termos técnicos na primeira menção; sem jargão excessivo

### Proporção teoria/prática (3h/aula)
- ~40% teoria (~1h), ~60% prática (~2h)
- Práticas com materiais acessíveis em sala; estações de 25-30 min cada
- Incluir checklist de avaliação ou relatório como instrumento

### Slides
- Máximo 25 slides por conjunto; pt-br; tom educational; com slide de título
- Quando houver identidade visual do material da UC (ex.: PPTXs do Bloco 7 da UC5), seguir o mesmo padrão (navy + acento, rodapé "UC5 · Redes de Computadores")

### Exercícios
- Contextualizados em TI (servidores, switches, racks, data centers, cabos, PoE, UPS)
- Exemplo similar resolvido antes de cada exercício; resolução passo a passo (para o professor)
- 2 exercícios extras sem resposta para resolução em sala
- Fórmulas com delimitadores `$$`

### Guia Noob
- Linguagem simples e amigável (conversar com um iniciante)
- Cada conceito: definição simples + analogia do cotidiano + exemplo prático em TI
- 1-2 vídeos do YouTube por tópico principal
- Boxes "Dicas do professor" e "Cuidado!" (segurança/erros comuns)
- Caixas de destaque, tabelas simples; estruturado por aula/dia na mesma sequência do planejamento
- Glossário final de termos técnicos
- Meta: aluno com zero conhecimento prévio entende o conteúdo

### Análise de Lacunas
- Comparar conteúdo enviado vs. referências pesquisadas
- Para cada lacuna: identificar, sugerir inserção, citar fontes e vídeos
- Integrar ao documento gerado ou entregar como seção própria

## PARÂMETROS ADAPTÁVEIS
- Número de dias/aulas e carga horária por aula: conforme input (padrão: 3h/aula)
- Disciplina: qualquer do curso técnico em informática
- Entregáveis: selecionáveis a cada uso
- Nome do professor: Juarez Bamberg

## OBSERVAÇÕES PEDAGÓGICAS
- Sempre incluir avaliação formativa (checklist, observação) e somativa (relatório, prova)
- Sugerir recursos complementares: simuladores (PhET), vídeos técnicos, visitas
- Ao final do planejamento, incluir observações gerais e sugestões de avaliação
- Apontar lacunas no conteúdo recebido e sugerir complementações

## EXEMPLO DE APLICAÇÃO
Usuário: "Conteúdo do bloco de Redes de Computadores, 2 aulas de 3h, gerar planejamento e slides."
1. Dados fornecidos — não perguntar.
2. Se citada a UC: carregar só `references/ucN.md`.
3. Pesquisar metodologias e fontes (ABNT/NRs).
4. Gerar planejamento DOCX com estrutura completa.
5. Gerar slides (até 25, pt-br, educational) e entregar em `artifacts/`.

## References — competências oficiais (carregar só a UC em questão)

- [`references/uc5.md`](references/uc5.md) — UC5 Instalação de Redes Locais (96h): indicadores, conhecimentos, habilidades, atitudes
- [`references/uc6.md`](references/uc6.md) — UC6 Manutenção de Redes Locais (96h)
- [`references/uc7.md`](references/uc7.md) — UC7 Servidores de Redes Locais (96h)
- [`references/uc8.md`](references/uc8.md) — UC8 Projeto Integrador (20h): fases e temas geradores
- [`references/uc9.md`](references/uc9.md) — UC9 Desenvolver Algoritmos (108h): indicadores, conhecimentos, habilidades, atitudes — qualificação Assistente de Desenvolvimento de Aplicativos Computacionais
- [`references/uc10.md`](references/uc10.md) — UC10 Desenvolver Banco de Dados (72h): indicadores, modelagem, SQL, segurança do BD (pré-requisito: UC9)

## Permissões que a skill pede

- **Pesquisa na web** (normas ABNT/NBR, NRs, fontes acadêmicas, vídeos) para embasar conteúdo.
- **Geração de documentos** (planejamento DOCX/PDF, slides, exercícios, guia noob) em `artifacts/`.
- **Não pede**: acesso a sistemas da instituição, dados de alunos, envio de e-mail.

## Critério de prontidão

O planejamento está pronto para gerar quando estão definidos: disciplina/tema, carga horária (dias × horas-aula) e quais entregáveis o usuário quer. Dados já fornecidos não se reperguntam.

## Saída esperada

Planejamento em DOCX/PDF (objetivo, conteúdo, metodologia, sequência didática, materiais, referências) + os entregáveis escolhidos, com fontes/vídeos citados, todos em `artifacts/`.

## Histórico

- 0.4.0 (2026-10-14): UC9 (Desenvolver Algoritmos, 108h) e UC10 (Desenvolver Banco de Dados, 72h) adicionadas em references/ — competências e indicadores extraídos do Plano de Curso Técnico em Informática (MPS); descrição e regras de disclosure atualizadas (uc5–uc10).
- 0.3.0 (2026-10-14): adaptada à plataforma leao — tools do Adapta ONE substituídas (documentGenerate→docx/python-docx, presentation→pptx/presentations, askQuestions→Form openui), saída em artifacts/ via share_file; técnica de progressive disclosure documentada explicitamente na seção própria; references/uc5–uc8 preservadas.
- 0.2.0 (2026-10-01): estado original — ver seção Origem.
