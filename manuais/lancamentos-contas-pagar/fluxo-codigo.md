# fluxo-codigo.md — #66 Lançamentos: contas a pagar (uso interno, NÃO publicar)

## Tela

- Rota `/contas-pagar-receber` (`ContasPagarReceber.tsx`).
- Menu: **Financeiro → Lançamentos**.
- 3 abas (`tab=pagar|receber|todos`): cada uma monta um
  `LancamentosTab`. Período padrão: `startOfMonth` → `endOfMonth`
  (**Este mês**).
- `+ Novo (F1)` → dropdown **Despesa** / **Receita** abre
  `ModalLancamento` com `tipo: 'PAGAR' | 'RECEBER'`.

## APIs

- Lista: `GET /api/financeiro2/lancamentos/{empresaID}/{usuarioID}?dataInicio=&dataFim=&tipo=PAGAR`
  (`useLancamentos.ts`).
- Cache (formas, fornecedores, categorias, contas):
  `GET /api/financeiro2/lancamentos/dados/{empresaID}/{usuarioID}/1`
  (`useLancamentosCache.ts`).
- Criar / editar: `POST /api/financeiro2/lancamento`
  (`useLancamentoCRUD.ts`). Payload: `tipo: 'PAGAR'`, `parcelas`
  (número ou `null` se único), `valor` = valor da parcela quando
  parcelado, `financeiroPagamentoID` (forma do **topo**),
  `contaBancariaID` / `fornecedorID` / `pc2ID` opcionais.
- Quitar: `POST /api/financeiro2/lancamento/pagar`
  (`useLancamentoPagar.ts` + `ModalConfirmarPagamento.tsx`).
- Excluir: `DELETE /api/financeiro2/lancamento/{empresaID}/{usuarioID}/{financeiroContasID}`.

## Parcelado

- `ModalLancamento.tsx`: `tipoPagamento: 'unico' | 'parcelado'`.
- No parcelado o rótulo vira **Valor Parcela \*** e o texto
  `Será criado N parcelas de R$ …`.
- Backend cria N linhas; a 1ª vence no `dataVenc`; as seguintes
  avançam o mês. Filtro **Este mês** só devolve a parcela do mês.

## Formas

- Formas do modal = `useFormasRecebimentoFinanceiro` (Dinheiro,
  Boleto, Pix, Cartão) — **não** as formas de recebimento das
  vendas (`useFormasRecebimentoVendas`).
- IDs de venda (Débito, Crédito, Vale) não aparecem neste select.

## Não confundir

- Venda paga vira **RECEBER** sozinha — #67 /
  `ModalEditarLancamentoVenda`.
- Relatório **Pagamentos** (`/pagamentos`) agrega o que já foi
  quitado; não é aqui que se cria a despesa.
