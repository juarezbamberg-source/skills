---
name: analise-remediacao-incidentes
description: This skill should be used when the user asks to "analisar incidente de produção", "post-mortem", "remediar incidente", "parar o sangramento", "análise de causa raiz com remediação", "corrigir incidente em produção", or mentions incidentes de produção EM GERAL (app, banco, infra) com direito a remediação em 2 fases (mitigação + correção definitiva) e post-mortem documentado. Framework completo: triagem → diagnóstico (cadeia causal) → remediação → validação → post-mortem. NÃO usar para triagem somente-leitura de cluster Kubernetes (usar triagem-cluster-metacortex) nem quando a correção for proibida pelo contexto (a triagem K8s nunca corrige).
version: 0.2.0
---

> **Origem**: exportada da plataforma anterior (pasta Drive "skills-Adapta/inativas"), status legado "inativa/backup". Importada para o repo em 2026-10-01 para consolidação; ainda sem validação de descoberta/execução neste agente.


# Análise e Remediação de Incidentes de Produção

## 1. TRIAGEM (Organizar Dados Brutos)

**Objetivo**: Estruturar fatos SEM diagnosticar ainda.

### Dados a Coletar:
- **Logs de aplicação**: Filtrar por ERROR, anotar timestamps, endpoints afetados, mensagens de erro
- **Métricas do sistema**: CPU, memória, conexões, latência (comparar com valores normais)
- **Status da infraestrutura**: Pods, réplicas, restarts, health checks
- **Histórico de mudanças**: Deploys recentes, alterações de configuração, atualizações

### Estrutura de Relatório:
1. **Resumo** (3 linhas): O quê, quando, taxa de impacto
2. **Padrões nos logs**: Agrupar por tipo de erro, frequência, endpoints afetados
3. **Anomalias nas métricas**: Comparar observado vs. normal, desvios percentuais
4. **Mudanças recentes**: Listar tudo que mudou nas últimas 24–48h
5. **Correlações**: Conectar padrões de logs com anomalias de métricas

---

## 2. DIAGNÓSTICO (Cadeia Causal Completa)

**Objetivo**: Identificar causa raiz com evidências.

### Método:
1. **Cadeia causal**: O que mudou → O que isso causou → Por que gerou o sintoma
2. **Evidências**: Citar dados específicos que sustentam cada etapa
3. **Hipóteses alternativas**: Listar 3–4 alternativas e descartar com evidências

### Checklist de Diagnóstico:
- [ ] Há descompasso entre demanda e capacidade? (ex: pool size vs. max_connections)
- [ ] Há padrão de falhas seletivo? (alguns endpoints falham, outros passam)
- [ ] Há cascata de degradação? (múltiplas métricas afetadas simultaneamente)
- [ ] O timing alinha com mudanças recentes?
- [ ] Há evidência de vazamento, contenção ou limite atingido?

---

## 3. REMEDIAÇÃO — FASE 1 (Parar o Sangramento)

**Objetivo**: Reduzir taxa de erro para <1% em 5–10 minutos.

### Ação 1.1 — Rollback/Redução Imediata:
- Reverter a mudança que causou o problema (ou reduzir demanda)
- Usar rollback de deploy ou ajuste de configuração
- Risco: Baixo (revertendo para estado que funcionava)
- Validação: Métricas normalizarem em 2–3 minutos

### Ação 1.2 — Monitoramento Contínuo:
- Ativar alertas em tempo real
- Acompanhar métricas críticas por 10 minutos
- Validação: Taxa de erro <1%, métricas no intervalo normal

---

## 4. REMEDIAÇÃO — FASE 2 (Correção Definitiva)

**Objetivo**: Permitir crescimento futuro sem recorrência.

### Ação 2.1 — Aumentar Capacidade:
- Identificar o limite atingido (ex: max_connections RDS)
- Calcular demanda futura com margem de segurança (+20%)
- Aumentar limite (ex: max_connections 100 → 300)
- Risco: Médio (pode exigir reboot)
- Validação: Confirmar novo limite, monitorar recursos

### Ação 2.2 — Aumentar Demanda Gradualmente:
- Aumentar em 3 fases (ex: pool size 10 → 25 → 40 → 50)
- Validar após cada fase (24–48h monitoramento)
- Risco: Baixo (aumento gradual detecta problemas cedo)
- Validação: Métricas <80% do novo limite, erro <0.1%

### Ação 2.3 — Adicionar Resiliência na Aplicação:
- Circuit breaker: timeout de conexão
- Retry logic: backoff exponencial (100ms, 200ms, 400ms)
- Risco: Baixo (melhora resiliência)
- Validação: Teste de saturação em staging

### Ação 2.4 — Alertas Permanentes:
- DatabaseConnections > 80% do max
- Pool exhausted errors > 5 em 5 min
- CPU > 85%
- Latência > 2x do normal
- Validação: Alerta testado, integração Slack confirmada

---

## 5. VALIDAÇÃO (Como Confirmar que Funcionou)

### Imediatamente após mitigação (5–10 min):
```
Taxa de erro: <1%
DatabaseConnections: 30–40 (ou 50–60 se aumentado)
CPU: 40–50% (normal)
Latência: 5–8ms (normal)
Health checks: 200 OK
```

### Após cada aumento de capacidade (24–48h):
```
DatabaseConnections: <80% do novo limite
Erro: <0.1%
Latência: normal
FreeableMemory: >1.5GB
Sem alertas disparados
```

---

## 6. POST-MORTEM (Documentação Final)

### Seções obrigatórias:
1. **Resumo** (3 linhas): O quê, quando, impacto
2. **Timeline**: Deploy → Início do incidente → Resolução (com timestamps)
3. **Causa raiz**: Cadeia causal completa
4. **Impacto**: Usuários afetados, duração, endpoints, SLA
5. **Ações tomadas**: Imediatas (mitigação) e definitivas (correção)
6. **Action items**: O que fazer para evitar recorrência
   - Validação de capacidade no CI/CD
   - Automação de alertas
   - Documentação de limites
   - Treinamento da equipe

---

## DICAS IMPORTANTES

- **Não diagnostique cedo**: Organize os dados primeiro, depois procure padrões
- **Sempre busque evidências**: Não assuma; cite dados específicos
- **Teste hipóteses alternativas**: Descartar alternativas fortalece o diagnóstico
- **Mitigação é rápida, correção é gradual**: Parar o sangramento é urgente; corrigir é cuidadoso
- **Valide cada passo**: Não assuma que funcionou; confirme com métricas
- **Documente tudo**: Post-mortem é aprendizado para a equipe
