# fluxo-codigo.md — PDV número e cupom (#44)

| Tela | Flag | Uso |
|------|------|-----|
| Número de Pedido no PDV | `pdvNumeroPedido` | título *Venda #N* em Conferir e Dividir / cupom |
| Imprimir Venda Sempre | `pvdImprimirVendaSempre` | `usePDV` / `PDV.tsx` chama `imprimirCupom` ao finalizar |

Cupom: `usePDVImpressao.ts` (`gerarLinhasFallback` se o servidor falha) → `gerarHtmlParaImpressao` → `imprimirViaIframe`.
