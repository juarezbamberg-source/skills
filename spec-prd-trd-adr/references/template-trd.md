# Template TRD (Technical Requirements Document)

Use quando o pedido focar na SOLUÇÃO: arquitetura, contratos, modelo de dados e testes.

## 1. Requisitos não-funcionais QUANTIFICADOS
- Tempo de resposta (ms + volume máximo).
- Disponibilidade (%).
- Segurança: senhas com bcrypt/argon2/PBKDF2 (nunca MD5/SHA1/texto puro).

## 2. Arquitetura e contratos
- Endpoints: método, caminho, autenticação/permissão.
- Formato REST/JSON.

## 3. Modelo de dados
- Tabelas com colunas, PK/FK.
- UNIQUE para regras de não-duplicidade (ex.: UNIQUE (recurso_id, data, hora)).
- CHECK para limites de valor (ex.: CHECK (limite <= 100)).

## 4. Stack
- Apenas decisões VERIFICADAS (repositório real, documento do projeto-base) ou marcadas como suposição a confirmar.
- Nunca inventar dependência ou ferramenta.

## Checklist de qualidade
- [ ] NFRs com números (ms, %, volume).
- [ ] Endpoints com método, caminho e permissão.
- [ ] Modelo de dados com PK/FK e UNIQUE/CHECK onde aplicável.
- [ ] Stack verificada ou marcada "[A CONFIRMAR]".
- [ ] Consistência com o PRD: cada regra de negócio vira restrição técnica.
