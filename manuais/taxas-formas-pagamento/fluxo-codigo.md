# fluxo-codigo.md — #65 Taxas das formas de recebimento (uso interno, NÃO publicar)

## Duas telas

1. **Financeiro → Formas Pagamento** (`/formas-pagamento`, `FormasPagamento.tsx`)
   - Topo: formas financeiras (Boleto, Cartão, Dinheiro, Pix) —
     contas a pagar/receber (`useFormasRecebimentoFinanceiro`).
   - Final: **Formas de Recebimento das Vendas**
     (`useFormasRecebimentoVendas` →
     `GET /api/financeiro2/formasPagamento/{empresaID}/{usuarioID}`).
   - Clique na linha → `ModalEditarFormaRecebimento` (taxas + bandeiras).
   - Colunas: `diasRecebimento`, `desconto` (taxa %), `descontoFixo`.
2. **Cadastros → Formas de Recebimento** (`/formas-recebimento`) —
   cadastro completo (ativo, TEF, desconto/acréscimo do **PDV**). Não é
   a taxa da operadora.

## Gravação da taxa

- GET ` /api/empresa2/formaRecebimento/config/{empresaID}/{usuarioID}/{formaPagamentoID}`
- POST `/api/empresa2/formaRecebimento/config`
  ```json
  {
    "formaPagamentoID": 381235,
    "empresaID": 38311,
    "usuarioID": 88711,
    "formaPagamentoConfig": [{
      "formaPagamentoConfigID": 12238,
      "parcela": 1,
      "desconto": 2.5,
      "descontoFixo": 0,
      "diasRecebimento": 0
    }],
    "formaPagamentoBandeiraConfig": []
  }
  ```
- Hook: `useFormaRecebimentoConfig.ts`. Depois do POST chama
  `setDataAtualizacaoFP()`.
- Modal: **SALVAR E SAIR (F2)** — não é auto-save. Taxa % e desconto
  fixo são exclusivos no UI (`atualizarConfigGeral`).
- IDs sandbox (BeeFood3): Débito `381235`, Crédito `381236`, Vale
  Refeição `381239`.

## Pagamento da venda

- Modal `ModalPagamentos.tsx` / `useModalPagamentosLogic.ts`.
- POST do pagamento **não envia** taxa; o backend preenche
  `taxa`, `taxaValor`, `valorLiquido`, `dataRecebimento`,
  `dataRecebimentoPrevista` (`Pagamento` em `useVendaPagamentos.ts`).
- Detalhe (lupa): bloco **Configuração de taxa** só renderiza se algum
  desses campos vier preenchido (linhas 1570–1614 de
  `ModalPagamentos.tsx`).
- Bandeira opcional: `ccbandeiraID`. Sem bandeira → config geral.

## Relatório faturado × realizado

- Rota `/desempenho` embute iframe
  `https://relatorios.beefood.com.br/relatorios?...&embedded=1`.
- Menu interno: **Vendas → Recebimento** (não existe item "Financeiro"
  dentro do iframe). Abas **Resumo** e **Dados**.
- API: `GET https://report.beetechapi.be/api/relatorio2/resumoPagamentos/{empresaID}`
  (além de `resumoVendaTicketMedio` no Resumo geral).
- Colunas Resumo: Qtd Faturado, Qtd Realizado, Valor Pago, Valor
  Realizado. Dados: Valor, V. Realizado, Taxa, Data Venda, Vencimento,
  Receb. Previsto, Recebimento.
- Prova ao vivo (30/08/2026): PIX Manual #878 — Valor 63,90 / realizado
  63,26 / taxa −1% / datas D+0. Débito #892 e #893 — vencimento no
  mesmo dia da venda (D+0); taxa ainda não copiada para o registro
  nessas duas vendas de cartão.

## Outro relatório

- `Financeiro → Recebimentos` (`/recebimentos`): abas Categorias / Tipo
  / Datas; filtro **Previsto e Realizado**. Agrega lançamentos, não a
  grade faturado×realizado por forma da venda.

## Não confundir

- Desconto/acréscimo do **cardápio digital** (#64) e o badge do botão
  no PDV (Dinheiro −1%, Crédito +3%) alteram o **total da venda**.
- Taxa da operadora altera o **líquido** e as **datas** de recebimento.
