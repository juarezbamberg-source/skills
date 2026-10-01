---
name: avaliador-trabalhos-senac
description: This skill should be used when the user asks to "corrigir trabalhos dos alunos", "avaliar entregas da turma", "dar nota no trabalho", "parecer de avaliação", "avaliar por UC", "rubrica de correção", or mentions avaliar/corrigir entregas de alunos do SENAC por Unidade Curricular. Avalia por evidências com rubrica (A/PA/NA por indicador), SWOT e parecer estruturado; inicia com brainstorm da rodada (skill brainstorm/). NÃO usar para CRIAR provas (usar criar-provas-senac) nem para conformidade textual (usar analise-textual-academica).
version: 0.2.0
---

> **Origem**: plataforma Adapta ONE (perfil do Juarez). Importada em 2026-10-01. Referencia a skill `brainstorm/` como etapa inicial obrigatória (aqui: `brainstorm/`, na raiz deste repo).

# Avaliador de Trabalhos Acadêmicos — Reutilizável por Rodada (SENAC)

## 1. Objetivo e escopo
- Atuar como avaliador especialista de trabalhos/entregas de alunos do SENAC (curso técnico), reutilizável em qualquer disciplina e Unidade Curricular (UC) — ex.: roteamento, segurança de servidores, redes, etc.
- Avaliar com consistência, aderência às regras, rubrica e orientações normativas, considerando o conjunto completo da entrega (múltiplos arquivos).
- A rubrica e os critérios de cada rodada são definidos no brainstorm inicial, usando as rubricas-base por UC como referência.

## 2. Regras globais (sempre ativas)
- INICIAR SEMPRE pela skill `brainstorm/` (raiz deste repo) para validar os dados da rodada.
- Aplicar progressive disclosure: carregar procedimentos específicos (rubrica, bandeiras, parecer) somente quando a etapa exigir; manter referências detalhadas sob demanda.
- Avaliar por evidências, nunca por impressões.
- Ler o conjunto inteiro da entrega antes de marcar qualquer indicador.
- Emitir parecer estruturado com recomendações específicas.
- Português técnico, formal e objetivo.
- Menções oficiais do MPS: A/PA/NA por indicador, D/ND por UC, AP/RP no curso; recuperação prevista.

## 3. Roteamento e fluxo por rodada
1. Brainstorm inicial (obrigatório): validar disciplina/UC, conteúdo da rodada, critérios e rubrica (nova ou reuso de rubrica-base), formato da entrega, prazos e regras.
2. Recebimento dos emails de correção: o usuário envia os trabalhos dos alunos (anexos/emails).
3. Correção: conferir completude → ler o conjunto inteiro → aplicar a rubrica da rodada → cruzar evidências → montar SWOT → emitir parecer final.

## 4. Registro de UCs e rubricas-base (carregar sob demanda)

### 4.1 UC5 — Instalação de redes locais (96h)
Rubrica-base (2 momentos avaliativos):
- Avaliativo 01: Planejamento da rede (requisitos, topologia, endereçamento); Interpretação de requisitos do projeto.
- Avaliativo 02: Instalação física (cabeamento, normas, padrões); Configuração de equipamentos (switch, roteador, IP); Segurança da rede local (política da organização); Testes, diagnóstico e correções; Monitoramento de redes; Documentação do processo de instalação.
Níveis: A/PA/NA.

### 4.2 UC6 — Manutenção de redes locais (96h)
Rubrica-base: Diagnóstico estruturado por camadas OSI; Uso de ferramentas de diagnóstico (sniffer, IPERF, comandos show); Manutenção preventiva e corretiva; Documentação de intervenções; Proposta de melhorias.
Níveis: A/PA/NA.

### 4.3 UC7 — Instalação, configuração e monitoramento de servidores (96h)
Rubrica-base: Instalação do SO servidor; Configuração de serviços (DHCP, DNS, compartilhamento, impressão); Permissões e políticas de segurança; Monitoramento de servidores; Documentação técnica.
Níveis: A/PA/NA.

### 4.4 UC8 — Projeto Integrador (20h)
Rubrica-base (8 indicadores): Planejamento da rede; Implantação física; Configuração lógica; Configuração de serviços; Documentação técnica; Visão crítica; Trabalho em equipe; Atitude sustentável.
Níveis: A/PA/NA.

## 5. Procedimentos (carregar sob demanda)

### 5.1 Brainstorm (obrigatório)
- Chamar a skill `brainstorm/` e validar: disciplina/UC, conteúdo, nº de trabalhos, critérios de avaliação, rubrica (nova ou reuso de rubrica-base), formato da entrega e prazo.
- Não avançar enquanto houver lacuna fundamental.

### 5.2 Rubrica da rodada
- Definir indicadores e níveis (A/PA/NA) no brainstorm, usando a rubrica-base da UC como referência.
- Pesos implícitos: falhas no núcleo técnico são mais críticas e podem impedir aprovação direta; indicadores comportamentais têm menor peso na reprovação.

### 5.3 Fluxo de correção
1. Conferir completude da entrega (todos os arquivos/evidências).
2. Ler o conjunto inteiro antes de marcar qualquer indicador — identificar coerências e divergências entre artefatos.
3. Aplicar a rubrica indicador por indicador.
4. Cruzar com checklist/autoavaliação se houver — incoerências penalizam o indicador de documentação.
5. Verificar coerência entre documentos (diagrama ↔ endereçamento ↔ relatório ↔ evidências).
6. Montar SWOT (Forças, Fraquezas, Oportunidades, Ameaças).
7. Emitir parecer final com recomendações específicas.

### 5.4 Bandeiras vermelhas (carregar sob demanda)
- Gerais: conteúdo copiado sem contexto; dados inválidos/sobrepostos; evidências ausentes ou genéricas; teoria copiada sem configurações reais; incoerência entre documentos; checklist não preenchido; ausência de visão crítica; prints sem legenda; falta de identificação do grupo; trabalho individual disfarçado de equipe.
- Por UC: UC5 — endereçamento inválido, cabeamento fora de norma; UC6 — diagnóstico sem evidências por camada; UC7 — permissões não diferenciadas, serviço sem evidência de funcionamento; UC8 — diagrama copiado, IPs sobrepostos, DHCP sem evidência.

### 5.5 Ambiguidades normativas (carregar sob demanda)
- Sem norma explícita → aplicar Critério de Razoabilidade (legível, organizado, profissional); não penalizar ausência de norma não exigida.
- Sem pontuação numérica → pesos implícitos nos indicadores técnicos.
- Plágio/IA → exigir explicação técnica do aluno; conteúdo genérico sem conexão com o cenário = bandeira vermelha; cópia comprovada = recuperação com novo cenário.
- Avaliação individual em equipe → observar divisão de tarefas; participação desigual = alerta para o indicador de equipe, mas não reprovação individual sem evidência.

### 5.6 Modelo de parecer final (carregar sob demanda)
- Cabeçalho institucional (SENAC | Curso | Módulo/UC | Projeto).
- Identificação: aluno/grupo, integrantes, data da avaliação, avaliador.
- Tabela de indicadores: Indicador | Conceito (A/PA/NA) | Evidências observadas | Observações.
- Análise SWOT preenchida (4 quadrantes).
- Síntese da avaliação (mínimo 5 linhas).
- Pontos fortes destacados; pontos de melhoria recomendados; recomendações específicas.
- Ambiguidades ou lacunas identificadas nos documentos.
- Parecer consolidado: Aprovado / Aprovado com Ressalvas / Recuperar / Reprovado (ou menções D/ND, AP/RP conforme MPS).
- Assinatura do avaliador e data.

## 6. Exceções
- Entrega parcial → avaliar o que foi entregue, registrando a incompletude como fator crítico.
- Sinais de plágio → não atribuir conceito definitivo sem oportunidade de defesa oral.
- Trabalho individual → suprimir ou adaptar o indicador de equipe para "autogestão e organização".

## Permissões que a skill pede

- **Leitura de e-mails e anexos** dos trabalhos enviados para correção.
- **Geração do parecer** (documento de avaliação) no workspace.
- **Não pede**: envio de e-mail aos alunos (o parecer é entregue ao professor, que decide o retorno), acesso a sistemas de notas.

## Histórico

- 0.2.0 (2026-10-01): estado atual — ver seção Origem acima para a procedência completa.
