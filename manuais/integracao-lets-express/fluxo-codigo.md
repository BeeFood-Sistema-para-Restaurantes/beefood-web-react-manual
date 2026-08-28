# fluxo-codigo.md — #59 Let's Express (uso interno, NÃO publicar)

- Card **Aplicativos → Entrega → Lets Express** (`app.id === 'lets-express'`).
  Modal: `LetsExpressModal` + `LetsExpressConfigForm`.
- Config GET `/api/empresa2/letsexpress/:empresaID/:usuarioID`
  POST `/api/empresa2/letsexpress`
  Campos: `api_key`, `empresa_id`, `forma_pagamento`, `retorno`,
  `manual` / `auto_preparo` / `auto_entrega`, `agenda_minutos`, `origens`.
- Formas (`FORMAS_PAGAMENTO_LETS`): D B C T V F X P H R.
- Origens: mesma lista `ORIGENS_AGILIZONE` (iFood, 99Food, Keeta, AIQFome,
  Rappi, DeliveryMuch, UaiRango, CARDAPIO_MANUAL).
- Despacho: `ModalAlterarMotorista` → `onLetsExpressClick` →
  `ModalLetsExpressConfig` → `letsExpressService.solicitar`
  POST `/api/entrega2/le/pedido`.
- Cancelar: `cancelarEntrega` →
  POST `/api/entrega2/le/pedidoCancelar/:empresaID/:filialID/:usuarioID/:preVendaID`.
- ID terceirizado `ENTREGA_TERCEIRIZADA_IDS.LETS_EXPRESS = -2`.
  `deliveredBy === 'LETS_EXPRESS'` → "Entregue por Lets Express".
- **Sem cotação** no web (`SERVICOS_COM_COTACAO` não inclui LE).
- Help do modal ainda aponta para o artigo antigo do ajuda.beefood.
- Mobile: `MobileLetsExpressPage` — **não** documentar (manuais são desktop).
