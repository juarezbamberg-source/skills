# Playbook de ambiente — cluster local Windows + ponte para o agente

Casos reais que geraram este playbook (Desafio 03, 2026-09-30): cluster kind na máquina
Windows do usuário acessado pelo agente (sandbox Linux) via túnel; imagens carregadas no
nó quando o Docker Hub não é alcançável de dentro do kind; token de SA entregue por
arquivo anexo. Cada armadilha abaixo foi um erro real que custou iterações.

## 1. Subir o cluster local (Windows + Docker Desktop, sem WSL distro)

O kind roda dentro do Docker Desktop — o usuário NÃO precisa de distro WSL (não usar
`wsl -e bash ...`: dá `execvpe(bash) failed` quando não há distro registrada).

```powershell
winget install Kubernetes.kind        # se ainda não tiver
kind create cluster --name metacortex # nome do cluster usado nos comandos seguintes
kind get kubeconfig --name metacortex # exibe o kubeconfig (server https://127.0.0.1:<porta>)
```

Armadilhas:
- **Não** assumir WSL distro; se `wsl -l -v` listar algo, tudo bem, mas o fluxo funciona só com Docker Desktop.
- O `server:` do kubeconfig é `127.0.0.1:<porta efêmera>` — a porta muda a cada `kind create`.

## 2. Ponte agente → cluster via cloudflared (quick tunnel)

O `127.0.0.1` do kubeconfig só existe na máquina do usuário. Para o agente (sandbox)
alcançar a API server, o usuário sobe um túnel quick do Cloudflare (sem conta):

```powershell
winget install Cloudflare.cloudflared
cloudflared tunnel --url https://127.0.0.1:<porta> --no-tls-verify
```

Regras duras (todas testadas a erro):
- **`https://` + `--no-tls-verify` é a ÚNICA combinação que funciona** para API server do kind:
  - `http://` puro → o API server responde `400 Client sent an HTTP request to an HTTPS server`;
  - `https://` sem `--no-tls-verify` → cloudflared recusa o certificado self-signed do kind
    (`x509: certificate signed by unknown authority`) e o túnel dá 502;
- Usar **`127.0.0.1` explícito**, nunca `localhost` (no Windows pode resolver `::1`/IPv6 e o kind escuta IPv4);
- Cada execução gera **URL nova** (`https://<palavras>.trycloudflare.com`) — atualizar o kubeconfig a cada reinício do túnel;
- O túnel morre se o usuário fechar o terminal (Ctrl+C) — é o "desligar" da ponte.

## 3. Autenticação através do túnel: SA + token, nunca client-cert

- **Client-cert NÃO atravessa o túnel**: o Cloudflare encerra/reabre o TLS e o certificado
  cliente se perde — a API passa a ver `system:anonymous` (403).
- Solução: ServiceAccount com token Bearer (header HTTP sobrevive ao proxy):

```powershell
kubectl create serviceaccount metavm-admin -n default
kubectl create clusterrolebinding metavm-admin --clusterrole=cluster-admin --serviceaccount=default:metavm-admin
kubectl create token metavm-admin --duration=24h   # token JWT (~944 chars)
```

- **Token colado no chat CORROMPE** (renderização come/trunca caracteres): no caso real
  chegou com 1 char a mais (945 vs 944) e o JWT inteiro invalidou. **Pedir sempre arquivo
  anexo** (`$tok | Out-File -Encoding ascii token.txt`) — arquivo chega byte a byte.
- Montar kubeconfig do agente: cluster com `insecure-skip-tls-verify: true` (o cert do kind
  é para 127.0.0.1, não para o domínio do túnel) + `user.token`. Sem CA data.
- Revogar no fim: `kubectl delete clusterrolebinding metavm-admin`.

## 4. Imagens no nó quando o kind não alcança o Docker Hub

Sintoma: pods em `ErrImagePull`/`ImagePullBackOff` com `EOF` em `auth.docker.io` — a rede
do Docker Desktop funciona (o `docker pull` na máquina baixa), mas o containerd DENTRO do
nó não. Fluxo que funcionou (o `kind load docker-image` buga com
`ctr: content digest ... not found`):

```powershell
docker pull --platform linux/amd64 <imagem:tag>          # se a tag for arm64-only, o pull amd64 falha — ver 4.1
docker save <imagem:tag> -o img.tar
cmd /c "docker exec -i metacortex-control-plane ctr --namespace=k8s.io images import - < img.tar"
del img.tar
```

- O `<` do PowerShell é reservado — o import tem que rodar via `cmd /c "..."`.
- `kind load` alternativo existe, mas falhou nos 3 testes com o mesmo erro de digest;
  o caminho `docker save` + `ctr import` via stdin funcionou sempre.

### 4.1 Tag arm64-only (kube-news:v1)

`fabricioveronez/kube-news:v1` só tem manifest arm64 — em cluster amd64 o pull falha com
`no matching manifest for linux/amd64`. Checar arquitetura antes (consulta ao registry ou
Docker Hub API) e usar tag multi-arch equivalente retaguada (`v1.0.0` → retag `v1`), com o
desvio documentado no ticket.

### 4.2 Achado de runtime: env × volumeMounts

`fabricioveronez/fake-shop:v26` exige `PROMETHEUS_MULTIPROC_DIR` apontando para diretório
EXISTENTE; `emptyDir` montado em `/tmp` não cria subdiretórios (`/tmp/metrics` não existe
→ gunicorn falha ao bootar → CrashLoopBackOff). Regra para manifests: env de caminho deve
apontar para o ponto de montagem em si (ou o app cria o dir no start).

## 5. Checklist da ponte (na ordem, com o que verificar)

1. `kind create cluster` → `kubectl get nodes` na máquina: `Ready`?
2. Túnel cloudflared com https + no-tls-verify → URL nova anotada?
3. SA + token 24h → token em ARQUIVO anexado ao chat (nunca colado)?
4. Kubeconfig do agente: server = URL do túnel + `insecure-skip-tls-verify: true` + token?
5. `kubectl get nodes` do agente: 200? (401 = token corrompido; 403 anonymous = cert não atravessou)
6. Imagens: pull na máquina + save/import no nó (seção 4)?
7. No fim: revogar o ClusterRoleBinding e fechar o túnel (Ctrl+C).

## 6. Entrega do repositório para a máquina local

Ao final do exercício, o usuário clona o repo para a pasta do projeto (exemplo real do
Desafio 03 — criar a pasta se não existir):

```powershell
cd "C:\Users\Juarez\Documents\00 Pos Graduação AIOPS\Desafios\SistemasMetacortex"
git clone https://github.com/juarezbamberg-source/Sistemas-Metacortex.git
```

Aviso: a pasta de destino deve estar VAZIA (ou ser nova) — `git clone` não aceita diretório
com conteúdo; se já houver material solto (ex.: clone antigo de projeto de apoio), mantenha
em subpasta própria. Rodar apps locais do repo a partir do clone (ex.: painel do Ticket 04:
`cd Sistemas-Metacortex\ticket-04-dashboard-do-cluster\painel-parque && npm install && npm start`).
