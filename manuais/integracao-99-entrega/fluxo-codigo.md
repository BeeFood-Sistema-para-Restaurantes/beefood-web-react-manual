# fluxo-codigo.md — Integração 99 Entrega (referência técnica)

> Uso interno. **Não publicar** no manual do usuário. Mapeia as APIs e o modelo de dados por trás da
> integração 99 Entrega, com base nos docs originais em `beefood3-server-entregas/docs/nn-entregas`.

Serviço: **beefood3-server-entregas** · Integração: **99 Entrega**
Base das rotas: `{server-entregas}/api/99Entrega`

---

## Autenticação

```
Authorization: Bearer {jwt}
```

- `usuarioID` é **opcional** (rota ou body). Quando enviado com JWT, deve coincidir com o token.
- O token OAuth da 99 é obtido/renovado sob demanda (`nnEntregaRetornaToken`), sem rota prévia.
- URL da 99 é **única** (sandbox = produção), fixa no código
  (`src/services/axiosNnEntrega.js`: `https://entrega.99app.com/entrega-openplatform`).

---

## 1. Cotação — `POST /api/99Entrega/cotacao/{empresaID}/{filialID}/{preVendaID}/{usuarioID}`

Solicita a **estimativa** (valor, distância e tempo). Não cria a corrida — apenas cota. O `estimateId`
retornado é usado depois em `POST /api/99Entrega/pedido`. Endereço e cliente são obtidos no banco pelo
`preVendaID` (o body **não** envia endereço; body opcional só p/ log: `{ "usuario": "João Silva" }`).

Sucesso → `{ resultado: true, cotacao: { estimativa_valor, estimativa_minutos, estimativa_km, estimateId, partida, desejado }, data: {…} }`

| Campo | Descrição |
|-------|-----------|
| `estimativa_valor` | Valor em reais (`fee` da 99 vem em centavos → `/100`) |
| `estimativa_minutos` | Tempo estimado (`delivery_duration`) |
| `estimativa_km` | Distância em km (`delivery_distance` em metros / 1000) |
| `estimateId` | Id da estimativa na 99 — **guardar** para criar o pedido |
| `partida` / `desejado` | Coordenadas de retirada e entrega (`lat`/`lng`) |
| `data.expires_time` | Expiração da estimativa (epoch, s) — após isso é preciso recotar |

Erro → HTTP 200 com `{ resultado: false, mensagem }`. Mensagens: `Credencial 99 Entrega inativa ou
incompleta para esta filial`, `Pedido não encontrado`, `Pedido não é do tipo DELIVERY`, `Endereço de
retirada/entrega incompleto (...)`, `Falha ao obter cotação da 99 Entrega`.

**Validações antes de chamar a 99:** credencial da filial ativa e completa; pedido existe e é DELIVERY;
endereços de retirada e entrega com rua, bairro, cidade, estado e CEP.

---

## 2. Outras rotas

| Rota | Uso |
|------|-----|
| `POST /api/99Entrega/credencial` | CRUD credencial (por filial) |
| `POST /api/99Entrega/pedido` | Place Order — criar entrega (`estimateId` obrigatório) |
| `GET /api/99Entrega/pedidoDetalhes/...` | Get Order Details (99 por `order_id`) |
| `POST /api/99Entrega/pedidoCancelar/...` | Cancelar (99 por `order_id`) |
| `POST /api/99Entrega/webhook` | Status da 99 — sem JWT, global; HMAC no header `X-Webhook-Signature` |

Webhook a cadastrar no painel da 99: `https://entregas.beetechapi.be/api/99Entrega/webhook`.

---

## 3. Modelo de dados — `entregas.*`

> Tabelas renomeadas de `nn_entregas_*` → **`nn_entrega_*`** (`schema-rename-tabelas.sql`).

**`nn_entrega_credencial`** (1 por filial, OAuth + CRUD):
`empresaID`, `filialID`, `client_id`, `client_secret`, `webhook_secret`, `access_token`, `expires_at`,
`ativo` (default 1), timestamps.
- Coluna `base_url` **removida** (`schema-drop-base_url.sql`) — URL da 99 é única e fixa no código.

**`nn_entrega_pedido`** (Place Order):
`empresaID`, `filialID`, `preVendaID`, `numeroPreVenda`, `clienteID`, IDs de marketplace
(`correlationId`, `nnID`, `keetaId`, `muchDeliveryCode`, `aiqfomeId`, `uaiRangoID`, `rappiOrderID`),
`order_id`, `estimate_id`, `status_nn`, `jsonRequest`, `jsonResponse`, `cancelado`, `recebido`,
`finalizado`, timestamps.
- IDs de marketplace **adicionados** (`schema-add-marketplace-ids.sql`) — sincronizam status com o
  marketplace de origem do pedido.
- Colunas **removidas**: `external_order_id` (`schema-drop-external_order_id.sql`; sempre igual ao
  `preVendaID`) e `fee`/`currency` (`schema-drop-fee-currency.sql`; nunca preenchidas — só existem no
  retorno da cotação em memória).

**`nn_entrega_webhook`** (auditoria):
`empresaID`, `event`, `event_id` (UNIQUE), `order_id`, `external_order_id` (mantida p/ payload cru da 99),
`jsonPayload`, `created_at`.

---

## Referências internas (origem)

- `beefood3-server-entregas/docs/nn-entregas/onboarding-99-entrega.md` — manual de origem
- `beefood3-server-entregas/docs/nn-entregas/api-cotacao.md`
- `beefood3-server-entregas/docs/nn-entregas/schema.sql` e `schema-*.sql` (rename/drops/marketplace-ids)
- Postman: `beefood3-nn-entregas.postman_collection.json`
