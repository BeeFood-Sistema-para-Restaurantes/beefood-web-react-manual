# fluxo-codigo.md — PDV fichas (#45)

`src/hooks/usePDVImpressaoFichas.ts`. Dispara em `PDV.tsx` **antes** de `pvdImprimirVendaSempre`.

Se `checkPrinterConnection()` falha → `gerarHtmlParaImpressao` + `imprimirViaIframe`.

Individual: um `window.print()` por item. Lista: um bloco com título `ITENS:`.
