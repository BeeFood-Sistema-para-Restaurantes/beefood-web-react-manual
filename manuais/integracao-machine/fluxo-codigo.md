# fluxo-codigo.md — Integração Machine (referência técnica)

> Uso interno. **Não publicar** no manual do usuário. Mapeia as APIs e o modelo de dados por trás da
> integração Machine, com base nos docs originais em `beefood3-server-entregas/docs/machine`.

Serviço: **beefood3-server-entregas** · Integração: **Machine (Gaudium)**
Base das rotas: `{server-entregas}/api/machine`

---

## Autenticação

```
Authorization: Bearer {jwt}
```

- `empresaID` e `usuarioID` (no body ou na rota) devem coincidir com o token.
- Em **development** (`NODE_ENV` ausente ou ≠ `production`) o Bearer é opcional; em **production** é obrigatório.

---

## 1. Credencial — `entregas.machine_credencial` (1 por `filialID`)

Consultar:

```
GET /api/machine/credencial/{empresaID}/{filialID}/{usuarioID}
```

Inserir (sem `id`) / Atualizar (com `id`):

```
POST /api/machine/credencial
Content-Type: application/json
```

Campos principais:

| Campo | Tipo | Observação |
|-------|------|------------|
| `id` | int | PK (só no update) |
| `empresaID` | int | Empresa BeeFood |
| `filialID` | int | Filial (única por credencial; só no insert) |
| `usuarioID` | int | Usuário autenticado |
| `api_key` | string | Chave da central Machine |
| `client_id` | string | Usuário HTTP Basic da API Machine |
| `client_secret` | string | Senha HTTP Basic da API Machine |
| `empresa_id` | int | ID da loja na central (**≠** `empresaID` do BeeFood) |
| `ativo` | 0\|1 | `1` ativo; `0` desligado (não há DELETE — use `ativo: 0`) |
| `forma_pagamento` | string | String exata aceita pela central na abertura |
| `retorno` | 0\|1 | `1` = motoboy volta ao restaurante |
| `agenda_minutos` | int\|null | `0`/`null` = agora; `30` = agendar em X min |
| `manual` | 0\|1 | `1` = só manual |
| `auto_preparo` | 0\|1 | `1` = dispara no PREPARO |
| `auto_entrega` | 0\|1 | `1` = dispara no PRONTO/ENTREGA |
| `origens` | string\|null | `null` = todas; CSV: `"IFOOD,KEETA,CARDAPIO_MANUAL"` |

Códigos `origens`: `IFOOD`, `99FOOD`, `KEETA`, `AIQFOME`, `RAPPI`, `DELIVERYMUCH`, `UAIRANGO`, `CARDAPIO_MANUAL`.

> O cache de credenciais é invalidado automaticamente após salvar.

---

## 2. Abrir entrega — `POST /api/machine/pedido`

Abre corrida para uma pré-venda (`preVendaID`) do tipo `DELIVERY`. Só ocorre se a pré-venda ainda **não**
tiver integração (`deliveredBy is null`).

Body: `empresaID`, `filialID`, `preVendaID` (obrigatórios); `usuarioID` recomendado; `usuario`,
`numeroPreVenda`, `numeroPedido` (log).

Sucesso → `{ resultado: true, data: {...}, solicitacao: { id_mch } }`
(`id_mch` persiste em `machine_pedido.machine_solicitacao_id`).

Erros retornam **HTTP 200** com `{ resultado: false, mensagem }`. Mensagens comuns: credencial inativa/
incompleta, `forma_pagamento` não configurada, pedido não é DELIVERY, endereço incompleto, categoria Moto
indisponível, Machine não retornou ID da solicitação.

---

## 3. Cancelar entrega — `POST /api/machine/pedidoCancelar/{empresaID}/{filialID}/{usuarioID}/{preVendaID}`

Cancela a última solicitação Machine da pré-venda. Body opcional `{ "motivo_id": 6 }` (default `6`).

Sucesso → `{ resultado: true, mensagem }`; `machine_pedido.status_machine = 'C'` e integração local
desligada. Erros: HTTP 200 com `{ resultado: false, mensagem }`.

---

## 4. Webhook de status — `POST /api/machine/webhook/:empresaID`

A atualização pós-abertura (em rota / entregue / cancelado) **não** usa cron — chega por webhook.
Coluna adicionada para roteamento por empresa:

```sql
ALTER TABLE entregas.machine_webhook
    ADD COLUMN empresaID INT NULL AFTER id,
    ADD KEY idx_machine_webhook_empresa (empresaID);
```

---

## Outras rotas

| Rota | Uso |
|------|-----|
| `POST /api/machine/cotacao/...` | Estimativa (valor, tempo, distância) |
| `POST /api/machine/pedido` | Abrir corrida |
| `POST /api/machine/pedidoCancelar/...` | Cancelar |
| `POST /api/machine/webhook` | Status da central |
| `POST /api/machine/resetCache` | Basic Auth — server-to-server / manutenção |

---

## Referências internas (origem)

- `beefood3-server-entregas/docs/machine/README.md` — manual de origem
- `beefood3-server-entregas/docs/machine/api-credencial.md`
- `beefood3-server-entregas/docs/machine/api-pedido-cancelamento.md`
- `beefood3-server-entregas/docs/machine/schema-webhook-empresaID.sql`
- Postman: https://documenter.getpostman.com/view/30402848/2s9YkgDkKa
