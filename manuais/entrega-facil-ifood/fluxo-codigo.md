# fluxo-codigo.md — #59 Entrega Fácil iFood (uso interno, NÃO publicar)

- Card **Aplicativos → Entrega → Entrega Fácil iFood** (`app.id === 'ifood-entrega-facil'`).
  Modal `EntregaFacilIFoodModal`: só orientação + link do artigo antigo. **Não grava**.
- Marketplace iFood: `IFoodModal` + `IFoodConfigModal` (Merchant ID, `SALVAR (F2)`).
  Flag de uso: `credenciais.entregaIfoodAtiva` em
  `GET /api/entregas/credencialAtiva/{empresa}/{filial}/{usuario}/1`.
- Permissão RBAC: `ifoodEntregaFacil` (`usePermissions`).
- ID interno do serviço: `ENTREGA_TERCEIRIZADA_IDS.IFOOD_ENTREGA_FACIL = -5`.
- Entrada no Delivery: `ModalAlterarMotorista` → `onIfoodEntregaFacilClick`
  (`Delivery.tsx`, `VendaDetalhes.tsx`). Só **1** pedido por vez.
- Modal operacional: `ModalIfoodEntregaFacil`.
  - Endereço incompleto (CEP/rua/bairro/número) → editar +
    `PUT /datasnap/rest/cliente2/atualizarEndereco` +
    **SALVAR E BUSCAR COTAÇÃO (F2)**.
  - Cotação: `GET /api/rest/entrega/disponibilidadeEntrega/{filial}/{corrId}/{lat}/{lng}`
    (`ifoodEntregaFacilService.buscarCotacao`). Exige lat/lng.
  - Pedido **com** `correlationId` (iFood): step `confirmacao` direto,
    botão **CONFIRMAR** → `POST /api/rest/entrega/solicitarMotorista`.
  - Pedido **sem** `correlationId`: step `pagamento`
    (`Pedido pago` / `Pagamento na entrega` + `paymentMethods`) →
    **CONTINUAR** + **CONFIRMAR** → `POST /api/rest/entrega/criarPedido`
    (`pago`, `method`, `brand`).
  - **Não existe** no web o checkbox *Incluir frete ao valor do pedido* do Windows.
- Cancelar: `cancelar()` no service existe
  (`POST /api/rest/entrega/solicitarMotorista{correlationId}`), mas
  `VendaDetalhes` **não** expõe lixeira para esse serviço
  (`deliveredBy` iFood Entrega Fácil cai no caso de motoboy `-5`, não na lista
  AGILIZONE/99/UBER). Cancelamento prático = Gestor do iFood.
- WhatsApp: BeeBot manda o link `meupedido.ifood.com.br/...` ao sair para entrega
  (comportamento do artigo; não recapturado neste ambiente).
- Pré-cotação paralela: `useCotacoesEntregaParalelas` inclui iFood quando há
  coordenadas e o serviço está ativo.
- Mobile: `MobileEntregaFacilIFoodPage` / `MobileModalAlterarMotorista` —
  **não documentar** (manuais são do painel desktop).
