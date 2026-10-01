---
name: pregacao-framework-care
description: This skill should be used when the user asks to "pregação com framework c-a-r-e" — skill importada da plataforma anterior (legado, sem fluxo executado anexado). Gera pregações estruturadas no framework C-A-R-E a partir de leituras e tom
version: 0.1.0
---

> **Origem**: exportada da plataforma anterior (pasta Drive "skills-Adapta/inativas"), status legado "inativa/backup". Importada para o repo em 2026-10-01 para consolidação; ainda sem validação de descoberta/execução neste agente.


# Framework C-A-R-E para Pregações

## Objetivo
Estruturar pregações completas e coerentes usando o framework C-A-R-E (Contexto, Análise, Reflexão, Encerramento) a partir das leituras diárias e tom definido pelo usuário.

## Entrada Esperada

### Leituras Diárias (Dropdown)
Apresentar como **caixa suspensa** com opções predefinidas de leituras comuns:
- Evangelho do dia (Mateus, Marcos, Lucas, João)
- Primeira Leitura (Antigo Testamento)
- Salmo Responsorial
- Segunda Leitura (Novo Testamento)
- Leitura Livre (usuário digita a referência)

O usuário seleciona na dropdown. Se escolher "Leitura Livre", abre campo de texto para inserir a referência bíblica.

### Tom da Pregação (Dropdown + Customização)
Apresentar como **lista suspensa** com opções predefinidas:
- Inspirador
- Reflexivo
- Desafiador
- Consolador
- Exortativo
- Contemplativo
- Empático
- Redentor
- **Customizado** (ao selecionar, abre campo de texto para o usuário descrever o tom próprio)

Se o usuário selecionar "Customizado", permitir que digite uma descrição (ex: "esperançoso e prático", "profundo e acessível").

## Estrutura C-A-R-E

### C — Contexto (2-3 parágrafos)
- Apresentar as leituras de forma integrada
- Estabelecer o cenário espiritual/bíblico
- Conectar com a realidade atual do ouvinte
- Tom: introdutório, envolvente
- O tempo de leitura deve ser entre 8 e no máximo 10 minutos

### A — Análise (3-4 parágrafos)
- Aprofundar o significado das leituras
- Explorar palavras-chave, símbolos, ensinamentos
- Conectar os textos entre si
- Aplicar hermenêutica básica (contexto histórico, autoria, propósito)
- Tom: educativo, reflexivo

### R — Reflexão (2-3 parágrafos)
- Questões provocativas para o ouvinte
- Desafios práticos derivados da mensagem
- Convite à transformação pessoal
- Aplicação concreta à vida cotidiana
- Tom: pessoal, desafiador (ou consolador, conforme tom escolhido)

### E — Encerramento (1-2 parágrafos)
- Síntese da mensagem central
- Chamado à ação ou à contemplação
- Bênção ou oração de encerramento
- Tom: inspirador, esperançoso, conclusivo

## Adaptação ao Tom

**Inspirador**: ênfase em possibilidades, esperança, transformação positiva
**Reflexivo**: convite à meditação profunda, questionamento interno, silêncio contemplativo
**Desafiador**: confrontação com verdades incômodas, chamado à coragem, ruptura com conformismo
**Consolador**: ênfase em conforto, presença divina, alívio do sofrimento
**Exortativo**: urgência, chamado à ação, mobilização para mudança
**Contemplativo**: foco na beleza divina, mistério, adoração silenciosa
**Empático**: conexão emocional, validação de sentimentos, acolhimento
**Redentor**: esperança na transformação, libertação, novo começo

Se tom customizado, manter a essência do tom predefinido mais próximo + elementos do tom descrito.

## Processo de Geração

1. Receber as 3 leituras via dropdown (ou texto livre se selecionado)
2. Receber tom via dropdown (predefinido ou customizado)
3. Gerar cada seção C-A-R-E respeitando:
   - Extensão apropriada (parágrafos conforme especificado)
   - Tom consistente ao longo
   - Fluxo lógico entre seções
   - Linguagem acessível mas profunda
4. Apresentar pregação completa, formatada e pronta para uso

## Qualidade

- Pregação deve ser coerente, fluida e pronta para ser lida/pregada
- Evitar clichês religiosos vazios
- Integrar as 3 leituras de forma orgânica (não isolada)
- Respeitar a teologia cristã católica (se aplicável ao contexto)
- Permitir ajustes: usuário pode pedir revisões de tom, extensão ou seções específicas
