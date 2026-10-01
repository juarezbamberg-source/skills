# Template PRD — Product Requirements Document

Filha da skill #Geração de PRD, TRD e ADR. Carregar SOMENTE quando o pedido exige gerar o PRD (foco em produto). A entrevista e as regras globais de qualidade já estão no playbook pai — não repetir.

## Estrutura fixa (6 seções, nesta ordem)

1. **Contexto** — por que existe, quem é afetado, dor resolvida. Nada implícito.
2. **Objetivos** — resultados, não funcionalidades (2 a 4 objetivos).
3. **Requisitos funcionais** — lista RF1..RFn, comportamentos do sistema.
4. **Critérios de aceite** — formato Dado/Quando/Então (Gherkin). Mensagens de erro EXATAS e verificáveis. Sem adjetivos ("rápido", "fácil").
5. **Escopo** — in-scope e out-of-scope explícitos. Out-of-scope protege o projeto contra crescimento infinito.
6. **Fases** — decomposição em marcos.

Ao final, incluir a tabela "Decisões registradas" (Decisão | Escolha | Justificativa).

## Regras de critérios de aceite
- Para cada REQ com restrição, escrever o cenário positivo E o negativo.
- Restrições de tipo: usar ALLOWLIST ("aceitar apenas X, Y, Z; qualquer outro é recusado"). Denylist fica incompleta.
- Mensagens de erro transcritas literalmente, verificáveis por teste.

## Checklist antes de entregar
- [ ] Contexto sem suposição implícita.
- [ ] Objetivos mensuráveis.
- [ ] Todo RF tem critério de aceite com cenário positivo e negativo.
- [ ] Out-of-scope listado.
- [ ] Decisões registradas com justificativa.
- [ ] Nenhum valor inventado: itens não confirmados marcados "[A CONFIRMAR]".
