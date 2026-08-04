# fluxo-codigo.md — Integração Uber Direct (uso interno, NÃO publicar)

> Atualizado em 04/08/2026 com as docs de API do `beefood3-server-entregas` (`docs/uber-direct`).
> Modelo A: **cada filial tem a própria conta na Uber + cartão**. O BeeFood só solicita, acompanha e cancela.

## 1. Onde fica no app (BeeFood front)

- Menu **Aplicativos** (`src/pages/Aplicativos.tsx`) → seção **Entrega** → card **Uber Direct**
  (`src/data/appCategories.ts`, id `uber-direct`, ícone `src/assets/apps/uberdirect.png`).
- **Estado no `git pull` de 04/08/2026:** card ainda marcado `disabled: true, badge: 'Em breve!'` em
  `appCategories.ts` (liberação depende de release/flag). O backend do fluxo já existe.
- Flag de credencial ativa: `entregaUberDirectAtiva` em `src/hooks/useCredenciaisEntrega.ts`
  (`GET /api/entregas/credencialAtiva/{empresaID}/{filialID}/{usuarioID}/1`).

## 2. O que o usuário cola no BeeFood

Do painel Uber Direct em **Desenvolvedor → Chaves de API** (passo 9) + **Chave de autenticação do
webhook** (passo 8 — novidade desta versão):

| Campo (banco) | Origem no Uber Direct |
|---------------|-----------------------|
| `customer_id` | **ID do usuário** |
| `client_id` | **ID de cliente do desenvolvedor** |
| `client_secret` | **Client Secret** (usar "Mostrar" antes de copiar) |
| `webhook_signing_key` | **Chave de autenticação do webhook** (3 pontinhos → Editar → Copiar) — **obrigatória** p/ validar o HMAC |

## 3. Webhook

- Endpoint cadastrado no painel Uber: **`https://entregas.beefoodapi.be/api/uberDirect/webhook`**, evento **event.delivery_status**.
- Rota no servidor: `POST /api/uberDirect/webhook` — sem JWT/Basic; autenticidade por **HMAC SHA-256**
  usando a `webhook_signing_key`. Move o pedido no kanban (`ENTREGA`/`ENTREGUE`).
- Toda ocorrência é auditada em `entregas.uber_direct_webhook` (gravada antes de validar).

## 4. Rotas do servidor (`beefood3-server-entregas`, prefixo `/api/uberDirect`)

| Método | Rota | Auth | Uso |
|--------|------|------|-----|
| GET | `/api/entregas/credencialAtiva/{empresaID}/{filialID}/{usuarioID}/{cripto?}` | Bearer JWT | flag ativa |
| GET | `/api/uberDirect/credencial/{empresaID}/{filialID}/{usuarioID}` | Bearer JWT | ler credencial |
| POST | `/api/uberDirect/credencial` | Bearer JWT | inserir/atualizar credencial |
| POST | `/api/uberDirect/testarConexao/{empresaID}/{filialID}/{usuarioID}` | Bearer JWT | testar OAuth |
| POST | `/api/uberDirect/resetCache` | Basic Auth (`beetech:...`) | invalidar cache |
| POST | `/api/uberDirect/cotacao/{empresaID}/{filialID}/{usuarioID}/{preVendaID}` | Bearer JWT | cotação |
| POST | `/api/uberDirect/pedido` | Bearer JWT | criar entrega |
| POST | `/api/uberDirect/pedidoCancelar/{empresaID}/{filialID}/{usuarioID}/{preVendaID}` | Bearer JWT | cancelar |
| POST | `/api/uberDirect/webhook` | HMAC | status → kanban |

Docs detalhadas no fonte: `api-credencial.md`, `api-conta.md`, `api-entrega.md`, `api-webhook.md`, `README.md`, `schema-add-marketplace-ids.sql`.

## 5. Comunicação com a Uber

- Auth: `POST https://auth.uber.com/oauth/v2/token`, grant `client_credentials`, scope `eats.deliveries`.
- API base: `https://api.uber.com/v1/`. Endpoints: `delivery_quotes`, `deliveries`, `deliveries/{id}/cancel`.
- `access_token` + `expires_at` ficam em `uber_direct_credencial`; renovação sob demanda (margem de 5 min).
- `fee` da Uber vem em **centavos** → gravado em reais (÷100). `sandbox=1` usa entregador-robô (test_specifications).

## 6. Modelo de dados (servidor)

- `entregas.uber_direct_credencial` — 1 linha por filial: `empresaID/filialID`, `customer_id`,
  `client_id/client_secret`, `access_token/expires_at`, **`webhook_signing_key`**, `sandbox`, `ativo`.
- `entregas.uber_direct_pedido` — 1 linha por entrega: ids BeeFood + ids de marketplaces
  (`nnID`, `keetaId`, `aiqfomeId`, etc.), `delivery_id`, `quote_id`, `tracking_url`, `status_uber`,
  `fee`, `cancelado`, `recebido`, `finalizado`.
- `entregas.uber_direct_webhook` — auditoria de eventos.
- Logs em `beetech.procInsert_log2` (módulo `Delivery`).

## 7. Origem do conteúdo (manual)

- Importado de `C:\projetos\beefood3-server-entregas\docs\uber-direct` (atualizado 04/08/2026).
- Dois textos prontos: `onboarding-uber-direct.md` (MDX Steps/Callout) e
  `onboarding-uber-direct-preview.md` (plain markdown). Para o repo usei o **preview (plain markdown)**,
  por casar com o padrão dos demais manuais; ajustei só os caminhos `imagens/` → `imagens-tratadas/`.
  Nenhum texto reinterpretado.
- **Mudança nesta versão:** passou a ter **10 passos** (novo passo 8 = copiar a Chave de autenticação do
  webhook) e o conjunto de imagens virou **`01`..`21`** (não há mais `00`).

## 8. Imagens

21 imagens (`uber-direct-01`..`21`). Já vinham prontas (com destaques) — apenas copiadas para
`imagens-puras/` (backup) e `imagens-tratadas/` (fonte única do manual). Ordem = 01→21.
