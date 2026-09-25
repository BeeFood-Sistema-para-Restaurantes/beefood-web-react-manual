# texto-documentation.ia.md — Fiado (operar no dia a dia)

## PROMPT (copiar e colar)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `fiado.md`
  e das imagens listados neste prompt.
- **Não publique**, em nenhuma seção: rota ou URL de API (`/api/...`); nome de campo,
  de arquivo, de componente, de tabela ou de coluna; bloco de código, JSON ou
  `campo=true`; nem as palavras *backend*, *endpoint*, *payload*, *array*, *bundle*.
  Se a frase só faz sentido para quem programa, ela não entra. Única exceção: a URL
  completa de webhook que o lojista copia para o painel do parceiro.
- Se você leu **qualquer outro arquivo** desta pasta — `fluxo-codigo.md`,
  `MEMORIA.md`, `annotate.py`, `capturar.py` —, **descarte o que leu**: são anotações
  internas de quem produziu o manual.
- Em 23/09/2026 uma página publicada saiu com a rota da API do cupom e dois nomes de
  campo do cashback, porque esta regra não estava aqui em cima.

Em **Financeiro** (ou junto aos manuais de operação), crie um item de menu chamado **"Fiado — Operar no dia a dia"**.

Leia APENAS os arquivos abaixo (não varra o resto do projeto):

1. Conteúdo (use na íntegra): `beefood-web-react-manual/manuais/fiado/fiado.md`
2. Imagens (nesta ordem):
   - `beefood-web-react-manual/manuais/fiado/imagens-tratadas/13-forma-recebimento-fiado.png`
   - `beefood-web-react-manual/manuais/fiado/imagens-tratadas/12-pdv-formas-pagamento.png`
   - `beefood-web-react-manual/manuais/fiado/imagens-tratadas/01-menu-fiado.png`
   - `beefood-web-react-manual/manuais/fiado/imagens-tratadas/02-visao-geral-kpis.png`
   - `beefood-web-react-manual/manuais/fiado/imagens-tratadas/03-visao-geral-grafico.png`
   - `beefood-web-react-manual/manuais/fiado/imagens-tratadas/04-visao-geral-tabela.png`
   - `beefood-web-react-manual/manuais/fiado/imagens-tratadas/05-controle-filtros-acoes.png`
   - `beefood-web-react-manual/manuais/fiado/imagens-tratadas/06-controle-lista-clientes.png`
   - `beefood-web-react-manual/manuais/fiado/imagens-tratadas/08-extrato-cliente.png`
   - `beefood-web-react-manual/manuais/fiado/imagens-tratadas/09-modal-pagamento.png`
   - `beefood-web-react-manual/manuais/fiado/imagens-tratadas/10-modal-divida.png`
   - `beefood-web-react-manual/manuais/fiado/imagens-tratadas/11-extrato-detalhado.png`
   - `beefood-web-react-manual/manuais/fiado/imagens-tratadas/07-vendas-sem-pagamento.png`

NÃO leia outros arquivos (fluxo-codigo.md, MEMORIA*.md, annotate.py, imagens-puras/).

- Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa".
- pt-BR, didático; números normais 1, 2, 3 nas setas.
- Destaque: cliente obrigatório no PDV; caixa aberto para pagamento; migração na aba Vendas sem Pagamento.
- Não publique o rodapé "Referências internas".

## Anexo — legendas

| Ordem | Arquivo | Tipo | Legenda |
|-------|---------|------|---------|
| 1 | 13-forma-recebimento-fiado.png | setas | Forma Fiado ativa |
| 2 | 12-pdv-formas-pagamento.png | setas | PDV — escolher Fiado |
| 3 | 01-menu-fiado.png | setas | Menu Fiado |
| 4 | 02-visao-geral-kpis.png | setas | KPIs |
| 5 | 03-visao-geral-grafico.png | setas | Gráfico e período |
| 6 | 04-visao-geral-tabela.png | contexto | Tabela de operações |
| 7 | 05-controle-filtros-acoes.png | setas | Filtros e ações |
| 8 | 06-controle-lista-clientes.png | setas | Lista (dados borrados) |
| 9 | 08-extrato-cliente.png | setas | Extrato lateral |
| 10 | 09-modal-pagamento.png | setas | Registrar pagamento |
| 11 | 10-modal-divida.png | setas | Registrar dívida |
| 12 | 11-extrato-detalhado.png | setas | Extrato por produto |
| 13 | 07-vendas-sem-pagamento.png | setas | Migração Conta Corrente |
