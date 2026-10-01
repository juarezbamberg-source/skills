---
name: analise-textual-academica
description: This skill should be used when the user asks to "analisar texto do trabalho", "conformidade textual", "verificar formato do documento acadêmico", "checar regras de escrita da entrega", or mentions validar conformidade textual de trabalhos acadêmicos (PDF/DOCX) contra regras definidas. Classifica cada item como em compliance/não em compliance/não verificado, com detecção de tipo de arquivo (não avalia slides). NÃO usar para dar nota/conteúdo (usar avaliador-trabalhos-senac) nem para estrutura de TCC (usar tcc-ava-ia).
version: 0.2.0
---

> **Origem**: plataforma Adapta ONE (perfil do Juarez). Importada em 2026-10-01. Referencia a skill `brainstorm/` como etapa inicial obrigatória (aqui: `brainstorm/`, na raiz deste repo).

# Análise Textual de Entregas Acadêmicas

## Objetivo
Validar trabalhos acadêmicos contra as regras de análise textual do documento de referência "Regras e métodos adicionais". Classificar cada item como **em compliance**, **não em compliance** ou **não verificado**, com justificativa curta e observações.

## Entrada
- Arquivo anexado (PDF/DOCX) OU texto colado pelo usuário.
- Se o material não permitir verificar um critério (ex.: margens, numeração de páginas em texto colado), marcar como "não verificado" e sinalizar explicitamente. Nunca assumir conformidade sem evidência.

## Regras de detecção de tipo de arquivo

### Tipo 1 — PDF de apresentação (slides)
- **Como identificar:** PDF cujo conteúdo apresenta textos curtos, tópicos em bullets, imagens grandes, layouts de slide (título no topo + conteúdo resumido), sem parágrafos acadêmicos estruturados. Semelhante a um PowerPoint exportado.
- **Ação:** NÃO avaliar. Retornar apenas uma mensagem curta: "Não avaliado — o arquivo enviado é uma apresentação (slides), não um documento acadêmico estruturado. Para avaliação completa, enviar como documento textual (PDF com parágrafos, introdução, desenvolvimento, conclusão e referências)."
- **Não gerar tabelas de verificação, rubrica ou nota.**

### Tipo 2 — PDF de documento textual (acadêmico)
- **Como identificar:** PDF com parágrafos estruturados, seções numeradas, introdução, desenvolvimento em prosa, conclusão e referências. Texto explicativo e aprofundado sobre o assunto.
- **Ação:** Avaliar normalmente com todos os blocos de verificação abaixo.

### Tipo 3 — DOCX ou texto colado
- **Ação:** Avaliar normalmente. Itens de formatação que não puderem ser verificados (margens, fonte, espaçamento) marcar como "não verificado".

## Regras de formatação por tipo de arquivo

### Para PDFs (Tipo 2 — documento textual):
- **NÃO avaliar nem constar na saída** os itens do Bloco 3 (Formatação: fonte, espaçamento, margens, alinhamento, recuo, numeração de páginas). Estes itens não são verificáveis de forma confiável em PDFs extraídos.
- O Bloco 3 deve ser inteiramente omitido da saída quando o arquivo for PDF.
- A rubrica de "Formatação e normas" (20%) deve avaliar apenas o que for verificável: nome do arquivo, entrega em PDF, presença e numeração de figuras/tabelas, e normas de apresentação. Itens não verificáveis não penalizam a nota.

### Para DOCX ou texto colado:
- Avaliar o Bloco 3 normalmente, marcando "não verificado" os itens que não puderem ser confirmados.

## Blocos de verificação

### 1. Identificação
- Capa padrão com ordem fixa (de cima para baixo): logo → instituição → curso → disciplina → título → subtítulo (se houver) → identificação do aluno → turma → professor → data.
- Identificação completa na capa: nome completo, matrícula, turma, turno, disciplina, professor, data de entrega.
- Folha de rosto: opcional/recomendada (título + natureza do trabalho + dados do aluno).
- Cabeçalho nas páginas internas: nome do aluno e disciplina no canto superior.

### 2. Estrutura
- Ordem obrigatória: Capa → Sumário → Introdução → Desenvolvimento (seções numeradas) → Conclusão → Referências → Anexos (se houver).
- Numeração de seções ABNT: 1, 1.1, 1.1.1 (máximo 3 níveis).
- Sumário automático com títulos e numeração de páginas.
- Introdução: tema, problema/objetivo e organização do trabalho.
- Desenvolvimento: cada seção responde a um aspecto do tema, parágrafos coesos, dados/argumentos.
- Conclusão: retoma o objetivo, apresenta resultados, sugere desdobramentos.
- Referências: todas as fontes citadas, ordem alfabética, padrão ABNT.

### 3. Formatação (apenas para DOCX ou texto colado — omitir para PDFs)
- Fonte: Times New Roman ou Arial, tamanho 12 no corpo do texto.
- Espaçamento 1,5 entre linhas; simples em citações longas e referências.
- Margens: superior e esquerda 3 cm; inferior e direita 2 cm.
- Alinhamento justificado; títulos alinhados à esquerda.
- Recuo de 1,25 cm na primeira linha dos parágrafos.
- Títulos: negrito, caixa alta para seções primárias, tamanho 12 ou 14.
- Numeração de páginas a partir da folha de rosto, canto superior direito; capa sem número.
- Citações diretas com mais de 3 linhas: recuo de 4 cm, fonte 10, espaçamento simples.

### 4. Normas de apresentação
- Entrega em PDF (e formato editável se solicitado).
- Nome do arquivo: SOBRENOME_Nome_Disciplina_Trabalho.pdf (ex.: SILVA_Joao_Redes_Trabalho.pdf).
- Limite de páginas: mínimo e máximo (conforme disciplina).
- Figuras e tabelas numeradas, título acima (tabelas) ou abaixo (figuras), com fonte de origem citada.
- Anexos/apêndices identificados com letras (Anexo A, Apêndice B) e listados no sumário.
- Revisão ortográfica obrigatória.

### 5. Rubrica de avaliação (pesos)
- Conteúdo e domínio do tema: 30% (profundidade, precisão técnica, uso de fontes).
- Estrutura e organização: 20% (presença/ordem das seções, coerência).
- Formatação e normas: 20% (para PDF: avaliar apenas nome do arquivo, formato, figuras/tabelas; para DOCX: avaliar todos os itens de formatação).
- Linguagem e ortografia: 15% (clareza, correção gramatical, vocabulário técnico).
- Apresentação visual: 10% (capa, figuras, tabelas, limpeza geral).
- Cumprimento de prazos: 5% — TRATAR COMO OBSERVAÇÃO, nunca como não conformidade. Informação de prazo raramente é verificável no material; registrar apenas observação quando o usuário fornecer a data de entrega.

## Regras de classificação
- **Em compliance**: evidência clara no material de que o item atende à regra.
- **Não em compliance**: evidência clara de descumprimento → justificar brevemente o motivo.
- **Não verificado**: impossível confirmar com o material fornecido → sinalizar explicitamente, sem penalizar o item.
- Ambiguidade ou falta de informação: sinalizar explicitamente na coluna de observações.

## Formato de saída
Para cada item: **Nome do item | Status | Justificativa curta | Observações**.
Ao final: resumo de contagem (X em compliance, Y não em compliance, Z não verificados) e, quando aplicável, nota estimada pela rubrica com os pesos.

### HTML para envio em e-mails
Toda a saída da avaliação deve ser em **HTML com estilos inline**, pronta para enviar diretamente no corpo de um e-mail (is_html: true). Regras:

- Usar HTML válido com **estilos inline em cada elemento** (style="..."). NÃO usar CSS externo, <style> blocks ou classes CSS — clientes de e-mail como Gmail e Outlook ignoram CSS em blocos <style>.
- Tabelas devem usar estrutura HTML completa: `<table style="border-collapse:collapse;width:100%;"><thead><tr><th style="border:1px solid #ddd;padding:8px;background:#f4f4f4;text-align:left;">...</th></tr></thead><tbody><tr><td style="border:1px solid #ddd;padding:8px;">...</td></tr></tbody></table>`.
- Títulos de seções: usar `<h2 style="color:#1a1a2e;margin:20px 0 10px 0;">` e `<h3 style="color:#16213e;margin:15px 0 8px 0;">`.
- Destaques e negrito: usar `<strong>` ou `<span style="font-weight:bold;">`.
- Listas: usar `<ul style="margin:10px 0;padding-left:20px;"><li style="margin:4px 0;">` ou `<ol>`.
- Parágrafos: `<p style="margin:8px 0;line-height:1.6;">`.
- Separadores entre seções de diferentes alunos: usar `<hr style="border:none;border-top:2px solid #e0e0e0;margin:30px 0;">`.
- Cores para status:
  - Em compliance: `<span style="color:#2e7d32;font-weight:bold;">Em compliance</span>`
  - Não em compliance: `<span style="color:#c62828;font-weight:bold;">Não em compliance</span>`
  - Não verificado: `<span style="color:#f57f17;font-weight:bold;">Não verificado</span>`
- Cabeçalho da avaliação: incluir no topo de cada avaliação uma tabela com nome do aluno, nome do arquivo e tema, usando `<table style="background:#f8f9fa;border-collapse:collapse;width:100%;margin-bottom:15px;">` com células `<td style="padding:8px;border:1px solid #ddd;">`.
- Quando houver múltiplos alunos, gerar uma seção HTML independente para cada um, separada por `<hr>`.
- NÃO usar sintaxe markdown (|, #, **). NÃO usar a ferramenta de tabelas visuais. Toda a saída deve ser HTML puro com estilos inline.
- O HTML deve renderizar corretamente em Gmail, Outlook e clientes modernos.

## Regras de conduta
- Não inventar informações; basear-se apenas no material fornecido e nas regras do documento de referência.
- Manter linguagem objetiva, consistente e uniforme em todas as avaliações.
- Se o documento de regras não cobrir um item, marcá-lo como "não verificado" com observação.

## Permissões que a skill pede

- **Leitura de arquivos enviados** (PDF/DOCX ou texto colado) — nada é gravado além do relatório de análise.
- **Não pede**: envio de e-mail, acesso a sistemas, ou qualquer escrita fora do relatório.

## Histórico

- 0.2.0 (2026-10-01): estado atual — ver seção Origem acima para a procedência completa.
