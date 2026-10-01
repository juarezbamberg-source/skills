---
name: gerar-terraform
description: This skill should be used when the user asks to "criar infraestrutura como código", "montar o Terraform do projeto", "gerar main.tf/providers.tf", "provisionar EKS/RDS/S3/VPC", "padronizar estrutura Terraform entre projetos", or mentions IaC em Terraform para qualquer cloud (AWS, GCP, Azure). Gera estrutura modular reutilizável (providers, variables, main, outputs, locals, tfvars.example, modules). NÃO usar para manifests Kubernetes (usar padrao-manifests-metacortex) nem para exercício acadêmico completo com CI/CD (usar exercicio-devops-cloud-ia).
version: 0.1.0
---

> **Origem**: exportada da plataforma anterior (pasta Drive "skills-Adapta/inativas"), status legado "inativa/backup". Importada para o repo em 2026-10-01 para consolidação; ainda sem validação de descoberta/execução neste agente.


# Gerar Arquivos Terraform

## Propósito
Gerar uma estrutura modular, reutilizável e bem documentada de arquivos Terraform que possa ser adaptada para diferentes tipos de infraestrutura (EKS, RDS, S3, CloudFront, etc.) em qualquer cloud provider (AWS, GCP, Azure).

## Quando Usar
- Provisionar infraestrutura como código (IaC) em novos projetos
- Padronizar a estrutura Terraform entre múltiplos projetos
- Criar templates reutilizáveis com boas práticas
- Documentar infraestrutura de forma reproduzível

## Fluxo de Execução

### 1. Coleta de Informações (Básico)
Pergunte ao usuário:
- **Tipo de infraestrutura**: EKS, RDS, S3, VPC, multi-serviço, ou outro?
- **Cloud provider**: AWS, GCP, Azure?
- **Nome do projeto**: para nomear recursos e variáveis
- **Ambiente**: dev, staging, production?

### 2. Estrutura de Diretórios Gerada
```
terraform/
├── providers.tf          # Provider, versões, default_tags
├── variables.tf          # Variáveis com validação e defaults
├── main.tf               # Recursos principais
├── outputs.tf            # Saídas (IDs, endpoints, comandos)
├── locals.tf             # Valores comuns (tags, AZs, CIDRs)
├── terraform.tfvars.example  # Exemplo de valores
└── modules/              # (Opcional) Módulos reutilizáveis
    ├── network/
    ├── compute/
    └── database/
```

### 3. Padrões Aplicados em Cada Arquivo

#### **providers.tf**
- Definir versão mínima do Terraform (>= 1.0)
- Provider com versão mínima (>= 5.0 para AWS)
- default_tags para aplicar tags globais
- Comentários explicativos

#### **variables.tf**
- Todas as variáveis com `description`, `type`, `default`
- Validação com `validation` blocks
- Variáveis sensíveis marcadas com `sensitive = true`
- Agrupadas por responsabilidade (rede, compute, banco)

#### **main.tf**
- Locals para valores comuns (tags, AZs, CIDRs)
- Recursos agrupados por seção com comentários
- Dependências explícitas com `depends_on`
- Nomes descritivos: `tipo_nome_propósito` (ex: `aws_instance_web`)

#### **outputs.tf**
- Outputs essenciais (IDs, endpoints, comandos)
- Descrição clara de cada output
- Sensitive outputs marcados quando apropriado

#### **locals.tf** (se necessário)
- `common_tags`: tags aplicadas globalmente
- `azs`: zonas de disponibilidade
- `cidr_blocks`: blocos de rede
- Valores reutilizados em múltiplos recursos

### 4. Boas Práticas Incluídas

✅ **Modularidade**: Separação clara de responsabilidades  
✅ **Reutilização**: Locals para valores comuns  
✅ **Validação**: Validation blocks em variáveis críticas  
✅ **Documentação**: Comentários explicativos em cada seção  
✅ **Tags**: Aplicadas em todos os recursos via locals  
✅ **Defaults sensatos**: Valores padrão realistas  
✅ **Segurança**: Variáveis sensíveis marcadas  
✅ **Escalabilidade**: Estrutura preparada para crescimento  

### 5. Customização Avançada (Sob Demanda)

Se o usuário solicitar:
- **Módulos**: Criar estrutura de módulos reutilizáveis
- **Backend remoto**: Adicionar configuração de S3 + DynamoDB
- **Workspaces**: Estrutura para dev/staging/prod
- **Políticas IAM customizadas**: Além das gerenciadas
- **Networking avançado**: VPC peering, Transit Gateway, etc.
- **Monitoramento**: CloudWatch, SNS, alertas

### 6. Saída Esperada

Gerar arquivos `.tf` prontos para:
```bash
terraform init
terraform plan
terraform apply
```

Com comentários guia em cada seção para o usuário adaptar.

## Exemplo de Uso

**Usuário**: "Preciso de Terraform para um cluster EKS com RDS"

**Skill**:
1. Coleta: EKS + RDS, AWS, projeto "meu-app", staging
2. Gera: providers.tf, variables.tf, main.tf, outputs.tf
3. Estrutura: VPC, subnets, EKS, RDS, IAM, security groups
4. Customização: Pergunta se quer backend remoto, workspaces, etc.

## Limitações e Melhorias Futuras

❌ **Não faz**: Executar `terraform apply` (apenas gera código)  
❌ **Não faz**: Gerenciar state remoto automaticamente  
❌ **Não faz**: Validar credenciais do cloud provider  

✅ **Futuro**: Integração com CI/CD (GitHub Actions, GitLab CI)  
✅ **Futuro**: Geração de testes Terraform (terratest)  
✅ **Futuro**: Documentação automática (terraform-docs)  
✅ **Futuro**: Análise de custo (infracost)
