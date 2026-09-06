# fluxo-codigo.md — #83 Pedidos pelo chat (uso interno, NÃO publicar)

## Onde liga

- Painel BeeBot: `https://bot.beefood.com.br` (redirect `bot2.beefood.com.br`).
- Login: `POST https://app.beetechapi.be/datasnap/rest/tusuario/validaBeebot`
  e `POST https://app3.beetechapi.be/api/tusuario/validaBeeFood`.
- Switch: `button#beeBotBeeChatPedido` (`role=switch`). Campo
  `beeBotBeeChatPedido` no retorno de `POST /api/whatsapp2/validaBeeBot`.
- Flag extra: `beeBotBeeChatPedido_BeeFoodHabilitado` (plano/loja).
- No web React, o badge **Pedidos Chat** (`WhatsAppConexaoCard.tsx`) só aparece
  no card conectado/conectando. Tooltip: *Retira pedidos direto pela conversa*.
- Abrir o painel pelo BeeFood: `WhatsAppConexaoContent` →
  `https://bot.beefood.com.br/login/?embeded=1&user={beecripto}&token={bearer}`
  (`useBeeCripto`: texto `{empresaID}_{filialID}_{usuarioID}`).

## Motor do pedido

- `POST https://chat.beetechapi.be/api/rest/tchatfluxo/validaFluxo`
- Auth básica `beetech:1q2w3e4r` (mesmo padrão das outras APIs internas).
- Body:

```json
{
  "filialID": 3408,
  "telefone": "11959572150",
  "clienteID": null,
  "mensagem": "fazer pedido",
  "clienteNome": "Testes pedido",
  "latitude": "",
  "longitude": ""
}
```

- Estado é por **telefone + filial**. `continuarMsg: "Continuar"` = o bot manda
  a próxima fala sozinho (ex.: depois da retirada, endereço da loja → observação).
- Resposta: `resposta1`, `resposta2`, `opcoes[]` (`titulo` + `origem`), `alerta`.
- Textos vêm da tabela `chatFluxo` (fixa por filial). Variáveis:
  `CLIENTE_NOME`, `SETORES_LISTA`, `BUSCA_*`, `PRODUTO_*`, `PEDIDO_RESUMO`,
  `MEU_ENTREGA_*`, `MEU_FORMA_PAGAMENTO`, `ENDERECO`, etc.
- Ações Nv1: 1 iniciar pedido, 2 entrega/retirada, 3 observação, 4 pagamento
  + resumo, 5 atendente, 6 cancelar. Nv2 = subetapa (produto achado, grupo,
  quantidade, CEP, localização…).

## Prova neste ambiente

Filial **3408** / empresa **3271**. Cardápio com 11 setores. Pedido de teste:
Junior Burger R$ 20 (ponto + Coca) / retirada na Rua Caramuru, 108 / Dinheiro.
Sandbox BeeFood3 é empresa **38311** / filial **39202** — o interruptor foi
fotografado **nessa** conta; o diálogo veio da 3408.

## Não documentar no manual do usuário

API, IDs de fluxo, `continuarMsg`, o texto invertido do cancelar (32910).
