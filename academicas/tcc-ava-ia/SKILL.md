---
name: tcc-ava-ia
description: This skill should be used when the user asks to "estruturar meu TCC", "analisar capítulo do TCC", "validar metodologia do TCC", "quais referências adicionar", "criar diagrama do TCC", "checklist do TCC", or mentions TCC de plataforma AVA inteligente com IA (RAG, visão computacional, análise comportamental, metacognição). Fornece checklists por capítulo, metodologia em 4 fases, métricas e validação técnica+pedagógica. NÃO usar para trabalhos comuns do SENAC (usar avaliador-trabalhos-senac) nem para análise de conformidade textual (usar analise-textual-academica).
version: 0.1.0
---

> **Origem**: exportada da plataforma anterior (pasta Drive "skills-Adapta/inativas"), status legado "inativa/backup". Importada para o repo em 2026-10-01 para consolidação; ainda sem validação de descoberta/execução neste agente.


# Skill: TCC - Plataforma AVA com Análise Comportamental e IA

## Contexto do Projeto
Você está desenvolvendo uma **Prova de Conceito (PoC)** de um Ambiente Virtual de Aprendizagem (AVA) apoiado por IA que monitora comportamento e foco de estudantes, gerando avaliações inteligentes e fornecendo analytics para professores.

## Três Pilares Principais

### 1. Módulo de Geração de Avaliações (IA Generativa)
- **Tecnologia**: RAG (Retrieval-Augmented Generation) com LLM
- **Cenário Restrito**: Perguntas baseadas apenas em documentos do professor
- **Cenário Expandido**: Perguntas enriquecidas com pesquisa na internet (ReAct)
- **Banco de Dados Vetorial**: Indexação de PDFs, slides, anotações
- **Validação**: Coerência e ausência de alucinações

### 2. Módulo de Monitoramento Comportamental (Visão Computacional)
- **Detecção de Foco**: Rastreamento de face landmarks + MediaPipe
- **Métrica focusScore**: % tempo com olhos abertos + face centrada
- **Detecção de Telefone**: YOLOv8 Nano em tempo real
- **Métrica phoneDetectedEvents**: Eventos quando smartphone é detectado
- **Saída**: Logs estruturados com timestamps

### 3. Dashboard Analytics (Backend + Frontend)
- **Para Alunos**: Relatório pessoal de foco, desempenho em avaliações, metacognição
- **Para Professores**: Engajamento da turma, material com mais dispersão, correlação foco vs desempenho
- **Nomenclaturas Consistentes**: focusScore, phoneDetectedEvents, studyDuration, correctAnswers

## Metodologia - 4 Fases

### Fase 1: Engenharia de Dados e IA Generativa
- Implementação do pipeline RAG
- Setup banco de dados vetorial
- Integração com LLM (especificar qual)
- Implementação do Cenário Expandido com ReAct

### Fase 2: Visão Computacional e Monitoramento
- Integração MediaPipe para detecção facial
- Implementação YOLOv8 Nano para detecção de objetos
- Cálculo de focusScore em tempo real
- Testes de precisão e revocação

### Fase 3: Desenvolvimento da Plataforma Web
- **Frontend**: Interface para alunos (estudo + avaliações + relatório de foco)
- **Backend**: API para processamento de documentos, geração de perguntas, armazenamento de dados
- **Database**: Estruturação de schemas (users, sessions, questions, focus_events, answers)

### Fase 4: Validação Técnica + Pedagógica
- **Validação Técnica**: Testes de coerência, alucinações, precisão de visão
- **Validação Pedagógica**: Testes A/B com alunos voluntários
- **Métrica de Sucesso**: Correlação positiva entre focusScore e acertos
- **Usabilidade**: Questionário SUS (System Usability Scale)

## Checklist de Estrutura TCC

### Introdução
- [ ] Contexto: IA em educação
- [ ] Problema: Dispersão de atenção em estudo autônomo
- [ ] Desafios: Falta de validação ativa, cegueira analítica do professor
- [ ] Benefícios: Metacognição + automação de avaliações
- [ ] Como vamos resolver: Descrição dos 3 módulos

### Referencial Teórico
- [ ] Sistemas de Tutoria Inteligente (ITS)
- [ ] RAG e mitigação de alucinações em LLMs
- [ ] Detecção de foco via eye-tracking e facial landmarks
- [ ] Análise comportamental em educação
- [ ] Metacognição e retenção de conhecimento
- [ ] Avaliações formativas automatizadas
- [ ] Visão Computacional: YOLO, detecção de objetos

### Proposta
- [ ] Descrição dos 3 módulos com detalhes técnicos
- [ ] Diagrama de arquitetura (C4 Model ou similar)
- [ ] Fluxo de dados end-to-end
- [ ] Escopo da PoC (n de alunos, duração, turmas)

### Metodologia
- [ ] Detalhamento das 4 fases
- [ ] Tecnologias específicas (LLM, banco vetorial, framework web, etc)
- [ ] Cronograma realista com marcos
- [ ] Requisitos funcionais e não-funcionais
- [ ] Plano de testes

### Avaliação
- [ ] Métricas técnicas (precisão, revocação, coerência)
- [ ] Plano de testes A/B
- [ ] Análise estatística (correlação foco vs desempenho)
- [ ] Questionário SUS
- [ ] Resultados esperados

### Considerações Éticas e Legais
- [ ] LGPD: Armazenamento e retenção de imagens de webcam
- [ ] Consentimento informado dos estudantes
- [ ] Privacidade dos dados comportamentais
- [ ] Direitos autorais dos materiais didáticos

## Pontos Críticos a Aprofundar

1. **Especificar Tecnologias**
   - Qual LLM? (GPT, Claude, Llama, etc)
   - Qual banco vetorial? (Pinecone, Weaviate, ChromaDB, etc)
   - Framework web? (FastAPI, Django, Next.js, etc)

2. **Definir Métricas com Precisão**
   - focusScore: Fórmula exata (ex: 0.8 * face_centrada + 0.2 * olhos_abertos)
   - phoneDetectedEvents: Limiar de confiança?
   - Correlação: Teste de Pearson? Spearman?

3. **Escopo Realista da PoC**
   - Quantos alunos voluntários?
   - Duração mínima de testes (semanas/meses)?
   - 1 turma ou múltiplas?

4. **Privacidade e Consentimento**
   - Como será armazenada a webcam? (cloud vs local?)
   - LGPD compliance: Anonimização dos dados
   - Opt-in/opt-out do monitoramento

## Documentação Técnica Necessária

- [ ] Diagrama de Arquitetura (C4 Model)
- [ ] Diagrama de Fluxo de Dados
- [ ] Esquema de Banco de Dados (ER Diagram)
- [ ] API Specification (OpenAPI/Swagger)
- [ ] Wireframes do Dashboard (Professor + Aluno)
- [ ] Documentação de Setup e Instalação

## Como Usar Esta Skill

**Quando precisar de:**
1. Estruturar um capítulo → Peça análise de coerência
2. Expandir seção do TCC → Peça sugestões embasadas
3. Criar diagramas técnicos → Peça geração de Mermaid
4. Revisar metodologia → Peça validação contra checklist
5. Gerar documentação → Peça templates estruturados

**Prompt de ativação:**
- "Analise meu [capítulo/seção] do TCC"
- "Quais referências devo adicionar em [seção]?"
- "Crie um diagrama de [componente técnico]"
- "Valide minha metodologia contra o checklist"
- "Me ajude a aprofundar [tópico específico]"
