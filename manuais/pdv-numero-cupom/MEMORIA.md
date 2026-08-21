# MEMÓRIA — #44 PDV número e cupom

Status: ✅ 21/08/2026.

Flags: `pdvNumeroPedido`, `pvdImprimirVendaSempre` (typo histórico na flag).

Prova: PDV Coxinha + Refri = R$ 14,00 → Receber → **Venda #848** + toast **Impressão via navegador / Servidor offline. Usando impressão do navegador.**

Sem BeeImpressão: `checkPrinterConnection()` falha → `gerarHtmlParaImpressao` + `imprimirViaIframe` → `window.print()`. O preview HTML 80 mm foi gerado com o mesmo CSS de `impressao-service.ts` (caminho 5 do plano, registrado aqui).

Fichas ligadas no mesmo sandbox — o toast de impressão via navegador vale para os dois. No texto do #44 pedimos desligar fichas para não misturar.
