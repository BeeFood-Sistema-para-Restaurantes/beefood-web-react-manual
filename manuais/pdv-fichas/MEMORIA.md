# MEMÓRIA — #45 PDV fichas de consumo

Status: ✅ 21/08/2026.

Flags: `impressaoFicha` (mestre), `impressaoFichaIndividual`, `impressaoFichaLista` (XOR na UI). Ligar o mestre sem modo força Individual.

Prova Individual: venda #846/#848 com Coxinha + Refrigerante Lata. HTML das fichas gerado com o mesmo layout de `usePDVImpressaoFichas.ts` (`gerarLinhasFichaIndividual` / `gerarLinhasFichaLista`) + CSS de `gerarHtmlParaImpressao`. Caminho do plano §8 (HTML visível) — o Chromium headless não segura o diálogo nativo `window.print()`.

Toast observado no receber: *Impressão via navegador — Servidor offline.*
