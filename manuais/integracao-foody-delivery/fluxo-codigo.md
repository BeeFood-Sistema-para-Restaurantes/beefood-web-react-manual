# fluxo-codigo.md — #61 Foody Delivery (uso interno, NÃO publicar)

- Card **Aplicativos → Entrega → Foody Delivery** (`app.id === 'foody-delivery'`).
  Modal desktop: `FoodyDeliveryModal`. Mobile: `MobileFoodyDeliveryPage` (não documentar).
- Config: `GET /api/empresa2/foodydelivery/{empresaID}/{usuarioID}` e
  `POST /api/empresa2/foodydelivery`. Hook `useFoodyDelivery`.
- Campos: `token`, `token_wh`, `manual` / `auto_preparo` / `auto_entrega` (um de cada vez),
  `origens` (`null` = todas; CSV dos códigos de `ORIGENS_AGILIZONE`).
- Códigos de origem: `IFOOD`, `99FOOD`, `KEETA`, `AIQFOME`, `RAPPI`, `DELIVERYMUCH`,
  `UAIRANGO`, `CARDAPIO_MANUAL`.
- Despacho: `POST /api/entrega2/fd/pedido` (`foodyDeliveryService.solicitar`).
  Cancelar: `POST /api/entrega2/fd/pedidoCancelar`.
- ID terceirizado: `ENTREGA_TERCEIRIZADA_IDS.FOODY_DELIVERY = -1`.
  `deliveredBy = 'FOODY_DELIVERY'`. Flag ativa: `entregaFoodyDeliveryAtivo`
  em `GET /api/entregas/credencialAtiva/...`.
- Webhook cadastrado **na Foody** (não no BeeFood):
  `https://app.beetechapi.be/api/entrega/fd/webhook`
  (o artigo antigo citava a URL datasnap; o print oficial já usa `/api/entrega/fd/webhook`).
- AJUDA do modal ainda aponta para o artigo antigo do ajuda.beefood.
- Botão **Adicionar Entregador** / lixeira: `VendaDetalhes` + `ModalAlterarMotorista`.
  Clique em Foody chama `onMotoristaSelect(-1)` → `solicitarEntrega` na hora
  (não tem tela de cotação).
