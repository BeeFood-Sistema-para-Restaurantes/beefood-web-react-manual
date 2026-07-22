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
| `POST /api/99Entrega/pedido` | Place Order — criar entrega (`estimateId` obrigatório; `external_order_id` = `preVendaID_timestamp`) |
| `GET /api/99Entrega/pedidoDetalhes/...` | Get Order Details (99 por `order_id`) |
| `POST /api/99Entrega/pedidoCancelar/...` | Cancelar (99 por `order_id`) |
| `POST /api/99Entrega/webhook` | Status da 99 — sem JWT, global; HMAC no header `X-Webhook-Signature` |

---

## 3. Modelo de dados — `entregas.*`

**`nn_entrega_credencial`** (1 por filial, OAuth + CRUD):
`empresaID`, `filialID`, `client_id`, `client_secret`, `webhook_secret`, `access_token`, `expires_at`,
`ativo` (default 1), timestamps.

**`nn_entrega_pedido`** (Place Order):
`empresaID`, `filialID`, `preVendaID`, `numeroPreVenda`, `clienteID`, `order_id`, `external_order_id`,
`estimate_id`, `status_nn`, `jsonRequest`, `jsonResponse`, `cancelado`, `recebido`, `finalizado`, timestamps.

**`nn_entrega_webhook`** (auditoria):
`empresaID`, `event`, `event_id` (UNIQUE), `order_id`, `external_order_id`, `jsonPayload`, `created_at`.

---

## Referências internas (origem)

- `beefood3-server-entregas/docs/nn-entregas/onboarding-99-entrega.md` — manual de origem
- `beefood3-server-entregas/docs/nn-entregas/api-cotacao.md`
- `beefood3-server-entregas/docs/nn-entregas/schema.sql`
- Postman: `beefood3-nn-entregas.postman_collection.json`
