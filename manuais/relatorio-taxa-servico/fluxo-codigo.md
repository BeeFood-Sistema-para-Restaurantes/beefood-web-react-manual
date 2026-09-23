# Fluxo de código — #85 Relatório de taxa de serviço

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `relatorio-taxa-servico.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

Documento interno: **não publicar**.

## Relatório

Aba `presencial-taxa-servico`. Componente `RelatorioTaxaServico.tsx`. API
`GET /api/relatorio2/relatorioTaxaServico/{empresa}/{start}/{end}/{horaIni}/{horaFim}`.

Agrupa **por venda**, não por item. Tipo: `%` se `taxaServicoValor > 0`, `R$ (Fixo)` se
`taxaServicoValorDinheiro > 0`.

KPIs: Total Taxa Serviço, Total Pago, Taxa Média, % Média, Faturamento Total.

Padrão RECEBIDO. Clique no garçom → timeline / Análise por Venda.

Permissão: `presencial-taxa-servico` → `taxaServico`.

## Sem taxa no produto

`ModalEditarProduto` → Opções avançadas → `#semTaxaServico`.
`pedidoBuilder` exclui `produto.semTaxaServico === true` da base da taxa. Comissão do
item **não** olha esse flag.

## Caixa

Mesmo endpoint do #84. Seção Taxa: só `gerente === true`. Checkbox
`pagoTaxaFilter` → `pagoTaxa`.
