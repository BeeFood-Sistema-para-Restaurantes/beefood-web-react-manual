# fluxo-codigo.md — #67 Lançamentos: contas a receber (uso interno, NÃO publicar)

## Tela

- Mesma rota `/contas-pagar-receber`, aba `tab=receber` e
  `tab=todos` (`ContasPagarReceber.tsx` + `LancamentosTab`).
- Receita extra: `+ Novo → Receita` → `ModalLancamento`
  `tipo: 'RECEBER'`.
- Venda: lápis da linha com `preVendaID` abre
  `ModalEditarLancamentoVenda` (não o `ModalLancamento`).

## APIs

- Lista receber: `GET /api/financeiro2/lancamentos/{empresaID}/{usuarioID}?…&tipo=RECEBER`.
- Lista todos: o mesmo GET **sem** `tipo`.
- Receita extra: `POST /api/financeiro2/lancamento` com
  `tipo: 'RECEBER'`. Categoria fixa no UI (**Outras Receitas**);
  `pc2ID` vai nulo / padrão do backend.
- Detalhe da venda: `GET /api/financeiro2/lancamento/vendaPagamento/{empresaID}/{usuarioID}/{preVendaID}/{preVendaPagamentoID}`
  (`useLancamentoVendaPagamento.ts`).
- Salvar detalhe da venda: `POST /api/financeiro2/lancamento/vendaPagamento`
  (taxa %, taxa valor, conta, documento, datas, `recebido`).

## Como a venda vira receber

- Pagamento no PDV (`ModalPagamentos`) grava o pagamento da
  `preVenda`. O backend cria o lançamento RECEBER com
  `preVendaID` + `preVendaPagamentoID`.
- Valor da linha = `valorLiquido` (taxa #65). Categoria
  **Receita de Pedidos**. Status **Recebido** se a venda já foi
  paga.
- Prova #915 (30/08/2026): original 14,00; taxa Visa 2,19%;
  líquido 13,69; D+0.

## Receita extra

- `ModalLancamento.tsx` linhas ~784–798: se `tipo === 'RECEBER'`,
  o campo Categoria é um bloco desabilitado **Outras Receitas**
  (tooltip: “Em breve teremos novas categorias de receita”).
- Switch **Recebido** no cadastro = já quita (data, encargos,
  desconto, valor recebido). Sem o switch, a linha nasce
  Pendente e o cifrão chama `ModalConfirmarPagamento`.

## Aba Todos

- Mesmo `LancamentosTab` sem filtro de `tipo`. Busca é
  client-side / query de descrição na lista do período.
- Filtro **Este mês** esconde parcela 2/2 do #66.

## Não confundir

- Formas da receita extra = topo de Formas Pagamento.
  Formas da venda = bloco de baixo (#65).
- Relatório **Recebimentos** (`/recebimentos`) agrega; não cria
  linha.
- Não pagar de novo uma venda que já está Recebido.
