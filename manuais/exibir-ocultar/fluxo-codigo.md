# fluxo-codigo.md — #68 Exibir / Ocultar (uso interno, NÃO publicar)

- Página: `src/pages/ExibirOcultar.tsx` — rota `/exibir-ocultar`.
- Permissão: `exibirOcultar` (sidebar `AppSidebar.tsx`).
- Lista: `CardapioTabelasPrecoTab` com `isRodizio=false`.
- Modal: `ModalTabelaPreco` com `isRodizio=false` → `ocultar` **fixo 0**
  (Ocultar Item). Canais: `delivery`, `presencial`, `beeshop`.
- Segunda aba: `TodosProdutosTabelasTab` — GET produtos **por tabela**
  (rota sem `cardapioID` dá 401).
- Lista GET: `/api/cardapio2/tabelasPreco/{empresa}/{usuario}` (sem query).
- Detalhe/grava: POST `/api/cardapio2/tabelaPreco`.
- Produtos: `useTabelaPrecoProdutos` —
  `/api/cardapio2/tabelaPreco/produtos/{empresa}/{usuario}/{cardapioID}`.
- Ao ir para aba Produtos sem `cardapioID`, `handleTabChange` chama
  `handleSave(true, false)` (auto título + não fecha).
- Dia marcado + hora vazia → front preenche 00:00–23:59
  (`updateDia` em `ModalTabelaPreco.tsx`).
- Badge da lista: `ocultar===1` → “Altera Preço”; senão “Oculta”.
- Cardápio Vue (`menu.beefood.com.br`): produto some da grade quando a
  tabela está ativa no canal `beeshop`. Cache até ~5 min.
- IDs sandbox: empresa 38311, usuário 88711, filial 39202.
  Tabela do manual: **Ocultar Brownie (manual)** + produto Brownie.
