# texto-documentation.ia.md — O pedido do totem no painel

## PROMPT (copiar e colar)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `totem-venda-no-painel.md`
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

Em **Histórico de Vendas**, adicione um item de menu por último chamado **O
pedido do totem no painel**.

Leia APENAS os arquivos abaixo:

    10|1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/totem-venda-no-painel/totem-venda-no-painel.md`
2. Imagens (nesta ordem):
   - `beefood-web-react-manual/manuais/totem-venda-no-painel/imagens-tratadas/02-totem-dinheiro.png`
   - `beefood-web-react-manual/manuais/totem-venda-no-painel/imagens-tratadas/04-painel-delivery-pedido-totem.png`
   - `beefood-web-react-manual/manuais/totem-venda-no-painel/imagens-tratadas/05-painel-pedido-detalhe.png`
   - `beefood-web-react-manual/manuais/totem-venda-no-painel/imagens-tratadas/06-painel-historico-filtro-origem.png`
   - `beefood-web-react-manual/manuais/totem-venda-no-painel/imagens-tratadas/07-painel-historico-lista-totem.png`
   - `beefood-web-react-manual/manuais/totem-venda-no-painel/imagens-tratadas/08-painel-desempenho-origem.png`
   - `beefood-web-react-manual/manuais/totem-venda-no-painel/imagens-tratadas/09-painel-desempenho-autoatendimento.png`
    20|
NÃO leia `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`.

- Apresentação IGUAL ao menu "Abrir Caixa".
- pt-BR, didático. Publicar as imagens na ordem acima (a numeração dos arquivos
  tem lacunas de propósito — duas capturas desta série são publicadas no manual de
  configuração do totem).
- Destacar: pedido do totem pago em **Dinheiro nasce sem pagamento** e espera o
  caixa; o mesmo pedido aparece como **AutoAtendimento** no card da venda e como
  **Totem** nos filtros (e **Autoatendimento** no Desempenho); o **desconto da
    30|  forma de pagamento** entra como desconto da venda.
- Manter a seção **"O que não se pode esquecer no fim do dia"**.
- **SEO**: manter as palavras de busca do lojista nos títulos e na FAQ (*venda do
  totem*, *pedido do totem no painel*, *origem AutoAtendimento*, *filtrar vendas
  por origem*, *ticket médio do totem*, *totem pago em dinheiro*). Não trocar por
  sinônimos genéricos nem resumir a FAQ.
- Não publicar o rodapé interno.

## Estrutura da página

    40|1. Antes de começar
2. O que acontece quando o cliente confirma
3. No Delivery: o pedido do totem no quadro
4. O card do pedido: origem, itens e o que fazer
5. Histórico de Vendas: filtrar pela origem Totem
6. Desempenho: quanto o totem vendeu
7. O que não se pode esquecer no fim do dia
8. Problemas comuns
9. Perguntas frequentes
10. Manuais relacionados
    50|
## Anexo — legendas

| Ordem | Arquivo | Tipo | Legenda |
|-------|---------|------|---------|
| 1 | `02-totem-dinheiro.png` | com setas | O aviso do totem antes de confirmar o pagamento em dinheiro |
| 2 | `04-painel-delivery-pedido-totem.png` | com setas | O quadro do Delivery filtrado pelo chip Totem |
| 3 | `05-painel-pedido-detalhe.png` | com setas | O card da venda, com a origem AutoAtendimento |
| 4 | `06-painel-historico-filtro-origem.png` | com setas | O filtro de origem do Histórico de Vendas |
| 5 | `07-painel-historico-lista-totem.png` | com setas | A lista do Histórico só com as vendas do totem |
    60|| 6 | `08-painel-desempenho-origem.png` | com setas | Desempenho → Vendas → Origem, com o chip Autoatendimento |
| 7 | `09-painel-desempenho-autoatendimento.png` | com setas | O faturamento e o ticket médio do autoatendimento |

A imagem 1 é tela do **aparelho** (1080×1920, retrato) — publicar sem
redimensionar.
