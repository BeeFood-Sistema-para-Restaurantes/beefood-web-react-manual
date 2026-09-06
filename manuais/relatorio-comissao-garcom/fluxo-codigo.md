# Fluxo de código — #84 Relatório de comissão do garçom

Documento interno: **não publicar**.

## Relatório

Iframe em `/desempenho` → `https://relatorios.beefood.com.br`. Aba
`presencial-pedidos-mobile` (`Reports.tsx`). Componente
`RelatorioPedidosMobile.tsx`.

API: `GET /api/relatorio2/relatorioMobileComissao/{empresaID}/{start}/{end}/{horaIni}/{horaFim}`.

Padrão: `selectedTipos = { RECEBIDO }`. Datas padrão: últimos 30 dias — por isso o
manual manda filtrar Hoje. Query `relatorio` + `dataInicio`/`dataFim` só vale se
`relatorio` vier na URL (esconde o menu).

KPIs: Venda Total, Pedidos, Itens, Comissão Total, % Mobile.

Tabela Comissão por Garçom: clique abre detalhe (timeline / Itens Vendidos). Grade:
Nº, Data, Garçom, Descrição, Qtd, Situação, Mesa, Mobile, Login, Venda, Comissão R$,
Comissão %.

Permissão reports-hub: `presencial-pedidos-mobile` → `pedidosMobileComissao`.

## Caixa — Resumo Presencial

`CaixaResumoPresencialPanel.tsx`. API
`/api/caixa2/caixaDetalhes/relatorioTaxaServicoComissao/{empresa}/{filial}/{usuario}/{caixaID}?garcom=&taxaServico=&pagoTaxa=&pagoGarcom=`.

Checkbox **somente Mobile** mapeia `garcom` (1/0). No sandbox 06/09/2026, com
`garcom=0` a seção `garcom[]` **não** devolveu Ana/Bruno (só uma venda antiga do
principal sem comissão). A seção `taxaServico[]` devolveu as duas. O fechamento
item a item é o relatório de Desempenho — o manual diz isso.

Seção Taxa de Serviço: `getConfigValue('gerente') === true`.
