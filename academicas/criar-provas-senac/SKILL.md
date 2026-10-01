---
name: criar-provas-senac
description: This skill should be used when the user asks to "criar prova", "montar avaliação", "fazer prova para a turma", "gerar versões de prova por grupo", "prova prática com rubrica", "gabarito do professor", or mentions criar avaliações para o SENAC (técnico, qualquer disciplina). Cria provas com brainstorm inicial (skill brainstorm/), versões por grupo, gabarito separado, rubrica e ficha de assinatura; entrega por e-mail. NÃO usar para corrigir/avaliar trabalhos já entregues (usar avaliador-trabalhos-senac) nem para planejar aulas (usar planejamento-aulas-informatica).
version: 0.2.0
---

> **Origem**: plataforma Adapta ONE (perfil do Juarez). Importada em 2026-10-01. Referencia a skill `brainstorm/` como etapa inicial obrigatória (aqui: `brainstorm/`, na raiz deste repo).

# provas_SENAC — Criação de Provas para o SENAC

## 1. Objetivo e escopo
- Criar provas/avaliações para alunos do SENAC (curso técnico), reutilizável em qualquer disciplina.
- Manter a metodologia validada: brainstorm inicial, versões por grupo, gabarito do professor, rubrica, ficha de assinatura e entrega por e-mail.

## 2. Regras globais (sempre ativas)
- INICIAR SEMPRE pela skill `brainstorm/` (raiz deste repo) para validar os dados iniciais.
- Aplicar progressive disclosure: carregar procedimentos específicos somente quando a etapa exigir; manter referências detalhadas sob demanda.
- Skill pai chama skill filha: `brainstorm/` é obrigatória no início; outras filhas (#Avaliador UC8, #Análise Textual, #Planejamento de Aulas) somente se o contexto da prova exigir.
- ENTREGÁVEIS: a prova deve ser documentada e entregue POR E-MAIL e DENTRO DO PRAZO COMBINADO EM SALA DE AULA.
- Nunca incluir gabarito na versão do aluno.
- Nomes de arquivos claros: prova_V1, prova_V2... (alunos) e prova_V1_prof, prova_V2_prof... (professor).

## 3. Roteamento e critérios de decisão
- Prova individual → versão única + gabarito.
- Prova em dupla/grupo → N versões (uma por grupo), mesma estrutura com cenários/endereçamentos diferentes + gabarito por versão + ficha de assinatura por grupo.
- Prova prática (simulador/ferramenta) → roteiro passo a passo, ambiente as-is, diagnóstico por camadas, questões de fundamentação, checklist e rubrica de 100 pts.
- Prova teórica → questões objetivas/dissertativas + gabarito + rubrica.

## 4. Procedimentos (carregar sob demanda)

### 4.1 Brainstorm inicial (obrigatório)
- Chamar a skill `brainstorm/` e validar: turma, UC, disciplina, conteúdo didático, nº de alunos, formação de grupos, formato da prova, ferramenta e prazo de entrega.
- Não avançar enquanto houver lacuna fundamental.

### 4.2 Estrutura padrão da prova
- Cabeçalho com identificação (aluno, turma, data, nota).
- Instruções gerais acolhedoras e didáticas.
- Contexto/cenário (ticket, caso ou problema).
- Topologia/plano de dados em tabelas.
- Configuração as-is (blocos de código).
- Metodologia de execução em etapas.
- Questões de fundamentação (5).
- Checklist de entrega.
- Matriz de avaliação (100 pts).
- Seção de entrega: e-mail + prazo combinado em sala de aula.

### 4.3 Versões e gabarito
- Gerar N versões para alunos e N gabaritos para o professor.
- Gabarito: causa raiz/respostas, trilha de diagnóstico, saídas reais, correção, validação, rubrica analítica e variações para reaplicação. Incluir aviso de confidencialidade docente.

### 4.4 Rubrica e ficha de assinatura
- Documento de rubrica por grupo: matriz de 100 pts + ficha de acompanhamento com tarefas em ordem lógica, colunas de assinatura/data por aluno, status (C/EA/P/NE) e observações do professor.

### 4.5 Ferramentas
- Documentos Word/PDF → ferramenta de geração de documentos.
- Planilhas (rubrica, ficha, controle) → ferramenta de planilhas.
- Arquivos binários de simulador (ex.: .pka) não são gerados pela IA — orientar o professor a montá-los.

## 5. Regras de comportamento
- Ser generoso e didático (alunos iniciantes).
- Não inventar dados; marcar incertezas.
- Confirmar dados essenciais via brainstorm antes de gerar os documentos finais.
