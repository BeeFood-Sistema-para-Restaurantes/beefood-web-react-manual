# texto-documentation.ia.md — Delivery pagamento automático (#43)

---

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `delivery-pagamento-auto.md`
  e das imagens listados neste prompt.
- **Não publique**, em nenhuma seção: rota ou URL de API (`/api/...`); nome de campo,
  de arquivo, de componente, de tabela ou de coluna; bloco de código, JSON ou
  `campo=true`; nem as palavras *backend*, *endpoint*, *payload*, *array*, *bundle*.
  Se a frase só faz sentido para quem programa, ela não entra. Única exceção: a URL
  completa de webhook que o lojista copia para o painel do parceiro.
- Se você leu **qualquer outro arquivo** desta pasta — `fluxo-codigo.md`,
  `MEMORIA.md`, `annotate.py`, `capturar.py` —, **descarte o que leu**: são anotações
  internas de quem produziu o manual.
- Em 23/09/2026 uma página publicada saiu com a rota da API do cupom e dois nomes de
  campo do cashback, porque esta regra não estava aqui em cima.

Manual **"Pagamento automático no Delivery"** em Configuração.

Fonte: `manuais/delivery-pagamento-auto/delivery-pagamento-auto.md` (use na íntegra).

Imagens, nesta ordem:

- `imagens-tratadas/02-pagamento-auto-ligado.png`
- `imagens-tratadas/03-kanban.png`
- `imagens-tratadas/05-coxinha-no-pedido.png`
- `imagens-tratadas/06-intencao-dinheiro.png`
- `imagens-tratadas/07-pedido-no-preparo.png`
- `imagens-tratadas/08-detalhe-preparo.png`
- `imagens-tratadas/09-pedido-pronto.png`
- `imagens-tratadas/10-depois-entregue.png`

Não leia MEMORIA, fluxo-codigo, annotate nem imagens-puras.

Destaque: sem intenção o Entregue **não** cobra; o automático só roda no clique
**PEDIDO ENTREGUE**; a prova é **Dinheiro — Pago** na venda 850 e o filtro Sem
pagamento caindo de 2 para 1. Números `1`, `2`, `3`.
