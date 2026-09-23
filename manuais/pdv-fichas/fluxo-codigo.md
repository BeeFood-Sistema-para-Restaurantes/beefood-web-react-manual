# fluxo-codigo.md — PDV fichas (#45)

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `pdv-fichas.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

`src/hooks/usePDVImpressaoFichas.ts`. Dispara em `PDV.tsx` **antes** de `pvdImprimirVendaSempre`.

Se `checkPrinterConnection()` falha → `gerarHtmlParaImpressao` + `imprimirViaIframe`.

Individual: um `window.print()` por item. Lista: um bloco com título `ITENS:`.
