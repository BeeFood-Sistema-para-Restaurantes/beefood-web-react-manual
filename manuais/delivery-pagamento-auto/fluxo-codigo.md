# fluxo-codigo.md — Delivery pagamento auto (#43)

Flag: `deliveryPagamentoAuto`.

Servidor: `beetech-server-node-2.0/src/models/delivery/alteraSituacaoDelivery.js` → `#processaPagamentoAutomatico`.

Condição do caminho 1: `valorPago === 0` && (`tipoPag > 0` || `tipoPagStr` não vazio) && situação `ENTREGUE`. `tipoPag` 1 = Dinheiro, 2 = Débito, 3 = Crédito, 4 = Carteira Digital; senão usa `tipoPagStr`.
