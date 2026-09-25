# fluxo-codigo.md — PDV número e cupom (#44)

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `pdv-numero-cupom.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

| Tela | Flag | Uso |
|------|------|-----|
| Número de Pedido no PDV | `pdvNumeroPedido` | título *Venda #N* em Conferir e Dividir / cupom |
| Imprimir Venda Sempre | `pvdImprimirVendaSempre` | `usePDV` / `PDV.tsx` chama `imprimirCupom` ao finalizar |

Cupom: `usePDVImpressao.ts` (`gerarLinhasFallback` se o servidor falha) → `gerarHtmlParaImpressao` → `imprimirViaIframe`.
