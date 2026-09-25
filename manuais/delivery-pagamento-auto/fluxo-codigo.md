# fluxo-codigo.md — Delivery pagamento auto (#43)

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `delivery-pagamento-auto.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

Flag: `deliveryPagamentoAuto`.

Servidor: `beetech-server-node-2.0/src/models/delivery/alteraSituacaoDelivery.js` → `#processaPagamentoAutomatico`.

Condição do caminho 1: `valorPago === 0` && (`tipoPag > 0` || `tipoPagStr` não vazio) && situação `ENTREGUE`. `tipoPag` 1 = Dinheiro, 2 = Débito, 3 = Crédito, 4 = Carteira Digital; senão usa `tipoPagStr`.
