# fluxo-codigo.md — Integração Uber Direct (uso interno / técnico)

> Documento técnico de apoio. **Não** é o manual do usuário. Mapeia onde a integração vive no
> código, as rotas do servidor e o modelo de dados. Base: `beefood-web-react` (git pull 04/08/2026)
> e `beefood3-server-entregas/docs/uber-direct`.

## 1. Onde fica no BeeFood (front — `beefood-web-react`)

- **Card do app:** `src/data/appCategories.ts` → seção **Entregas**
  `{ id: 'uber-direct', name: 'Uber Direct', description: 'Solicite entregadores', isNew: true }`.
  O card está **ativo** (não é mais `disabled: 'Em breve!'`).
- **Abertura do modal:** `src/pages/Aplicativos.tsx` → ao clicar no card `uber-direct`,
  `setUberDirectModalOpen(true)` renderiza `<UberDirectModal />`. Também na versão mobile
  (`src/components/mobile/aplicativos/MobileAplicativosPage.tsx`).
- **Modal de credencial:** `src/components/aplicativos/UberDirectModal.tsx`.
  Campos exibidos (todos obrigatórios):
  - **ID do usuário** → `customer_id`
  - **ID de cliente do desenvolvedor** → `client_id`
  - **Client Secret** → `client_secret` (campo com olho de mostrar/ocultar)
  - **Chave de autenticação** → `webhook_signing_key` (campo com olho de mostrar/ocultar)
  - **Integração ativa** (switch) → `ativo` (1/0)
  - Salvar com botão **SALVAR** ou tecla **F2**; fechar com **ESC**.
  - Botão **AJUDA** abre `https://ajuda3.beefood.com.br/integracao-uber-direct` (destino deste manual).
- **Hook de credencial:** `src/hooks/useUberDirectCredencial.ts` (`fetchConfig`/`saveConfig`).
- **Service de entrega:** `src/services/entrega/uberdirect.ts` (`buscarCotacao`, `solicitarPedido`,
  `cancelar`). Fluxo de despacho usa cotação → solicitação, nunca `solicitar` direto.
- **Flag de credencial ativa:** `entregaUberDirectAtiva` em `src/hooks/useCredenciaisEntrega.ts`,
  `src/utils/entregaCache.ts` e `src/services/entrega/types.ts`.
- **Ícone:** `src/assets/apps/uberdirect.png`.

## 2. Rotas do servidor (`beefood3-server-entregas`, prefixo `/api/uberDirect`)

| Método | Rota | Uso |
|--------|------|-----|
| GET | `/api/entregas/credencialAtiva/{empresaID}/{filialID}/{usuarioID}/{cripto?}` | Retorna `entregaUberDirectAtiva` |
| GET | `/api/uberDirect/credencial/{empresaID}/{filialID}/{usuarioID}` | Consulta a credencial (usado pelo `fetchConfig`) |
| POST | `/api/uberDirect/credencial` | Insere/atualiza a credencial (usado pelo `saveConfig`) |
| POST | `/api/uberDirect/testarConexao/{empresaID}/{filialID}/{usuarioID}` | Testa OAuth com a Uber |
| POST | `/api/uberDirect/resetCache` | Invalida cache (Basic Auth, server-to-server) |
| POST | `/api/uberDirect/cotacao/{empresaID}/{filialID}/{usuarioID}/{preVendaID}` | Cotação da entrega |
| POST | `/api/uberDirect/pedido` | Cria a entrega (a partir da cotação) |
| POST | `/api/uberDirect/pedidoCancelar/{empresaID}/{filialID}/{usuarioID}/{preVendaID}` | Cancela a entrega |
| POST | `/api/uberDirect/webhook` | Recebe `event.delivery_status` (assinatura HMAC) |

Auth do front/apps: **Bearer JWT** (exige `empresaID` e `usuarioID` batendo com o token).

## 3. Comunicação com a Uber

- OAuth: `POST https://auth.uber.com/oauth/v2/token`, grant `client_credentials`, scope `eats.deliveries`.
- API base: `https://api.uber.com/v1/`.
  - Cotação: `POST customers/{customer_id}/delivery_quotes`
  - Criar entrega: `POST customers/{customer_id}/deliveries`
  - Cancelar: `POST customers/{customer_id}/deliveries/{delivery_id}/cancel`
- `access_token` é cacheado em `uber_direct_credencial` com `expires_at`; renovado sob demanda
  (margem de 5 min). Não há rota específica de token.

## 4. Webhook e autenticação

- Endpoint: `https://entregas.beefoodapi.be/api/uberDirect/webhook`, evento **event.delivery_status**.
- Autenticidade validada por **HMAC SHA-256** usando a **`webhook_signing_key`** — por isso o passo 8
  do manual pede copiar a "Chave de autenticação" do webhook e colá-la no BeeFood.
- Cada evento é gravado em `uber_direct_webhook` **antes** de qualquer validação (auditoria).
- Move o pedido no kanban: `ENTREGA` (a caminho) e `ENTREGUE` (concluído).

## 5. Modelo de dados (server)

- **`uber_direct_credencial`** (1 por filial): `empresaID`, `filialID`, `customer_id`,
  `client_id`, `client_secret`, `access_token`/`expires_at` (cache), `webhook_signing_key`
  (obrigatória p/ HMAC), `sandbox`, `ativo`.
- **`uber_direct_pedido`** (1 por entrega): ids do pedido BeeFood + ids de marketplaces,
  `delivery_id`, `quote_id`, `tracking_url`, `status_uber`, `fee` (em reais), `currency`,
  `cancelado`, `recebido`, `finalizado`.
- **`uber_direct_webhook`**: auditoria (`delivery_id`, `customer_id`, `kind`, `jsonPayload`).

## 6. Credencial considerada ativa

Precisa de: linha com `ativo = 1` no cache, `customer_id` preenchido e `client_id` + `client_secret`
preenchidos. Faltando algo: `{ resultado: false, mensagem: "Credencial Uber Direct inativa ou incompleta..." }`.

## 7. Modelo de negócio

Modelo A: **cada filial tem a própria conta Uber + Uber Direct + cartão**. A Uber cobra as corridas
direto no cartão da loja; o BeeFood apenas solicita, acompanha e cancela. Não há cobrança
centralizada por parceiro.

## 8. Origem do manual

- Importado de `C:\projetos\beefood3-server-entregas\docs\uber-direct`.
- Texto: `onboarding-uber-direct-preview.md` (plain markdown), usado **verbatim** como
  `integracao-uber-direct.md` (só caminhos `imagens/` → `imagens-tratadas/`).
- Docs de API da fonte (`README.md`, `api-conta/credencial/entrega/webhook.md`,
  `schema-add-marketplace-ids.sql`) consolidadas aqui.

## 9. Imagens

27 imagens (`uber-direct-01`..`27`). Já vinham prontas (com destaques) — apenas copiadas para
`imagens-puras/` (backup) e `imagens-tratadas/` (fonte única do manual). Ordem = 01→27.
