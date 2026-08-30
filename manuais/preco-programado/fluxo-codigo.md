# fluxo-codigo.md — #69 Preço Programado (uso interno, NÃO publicar)

- Página: `src/pages/PrecoProgramado.tsx` — rota `/preco-programado`.
- Permissão de menu: **`rodizio`** (não tem chave própria).
- Lista: `CardapioTabelasPrecoTab` com `isRodizio=true` +
  `isProgramado=true` → GET `?preco=1` e `filtroProduto='semProduto'`.
- Modal: `ModalTabelaPreco` `isRodizio` + `isProgramado` → `ocultar`
  **fixo 1** (Alterar Preço), `produtoIDRodizio=null`, canais iguais
  ao Exibir/Ocultar (delivery / presencial / beeshop).
- Rodízio de verdade (`/rodizio`) usa `?rodizio=1` + produto vinculado
  e **só** canal Presencial. Não misturar.
- Produtos: `TabelaPrecoProdutosTab` com `isAlterarPreco` — colunas
  Desc. % / Desc. R$ / Valor Final. Botão **Desconto (N)** só com
  seleção. Modal **Aplicar Desconto**: `valor` | `porcentagem` +
  `updateMultipleDescontos`.
- Conta do exemplo: 18,90 × 0,80 = **15,12**.
- Cardápio Vue: card mostra `valorFinal | valorUnt | -N%`.
- IDs sandbox: empresa 38311, usuário 88711, filial 39202.
  Tabela do manual: **Happy hour milk-shake (manual)** + Milk Shake
  de Morango 20%. Intacta: **Preço 24/08 13:35** (50% burgers).
