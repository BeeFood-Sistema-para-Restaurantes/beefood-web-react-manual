# texto-documentation.ia.md — Entendendo a numeração dos pedidos

## PROMPT (copiar e colar)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `numeracao-pedidos.md`
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

Em **Caixa**, crie um novo item de menu por último chamado **Entendendo a numeração dos pedidos**.

Leia APENAS os arquivos abaixo (não varra o resto do projeto):

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/numeracao-pedidos/numeracao-pedidos.md`
2. Imagens (nesta ordem), em `beefood-web-react-manual/manuais/numeracao-pedidos/imagens-tratadas/`:
   `05-venda-detalhe.png`, `04-delivery.png`, `06-cupom.png`, `02-historico-virada.png`,
   `01-parametros-pdv.png`, `03-historico-mesa.png`

NÃO leia outros arquivos (`fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

- Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa".
- pt-BR, didático. É um manual **conceitual**: o leitor quer entender por que existem dois
  números, não executar um cadastro. Não transforme as seções em passo a passo.
- Manter as tabelas comparativas — elas são o coração do texto, em especial a que mostra o
  pedido indo de 60 para 1 enquanto a venda vai de 930 para 931.
- Manter os dois quadros de destaque: o da tela do PDV (que mostra o número da **venda**, não o
  do pedido) e o do **reset opcional** do número da venda, que ainda não existe.
- Não publicar nada do `fluxo-codigo.md`.

## Estrutura da página (na ordem do `.md`)

1. Os dois números
2. Como o sistema escreve os dois
3. O número da venda nunca reinicia
4. O número do pedido é a contagem do caixa
5. Por que vale fechar o caixa todo dia
6. Quem recebe número de pedido (Ligando no PDV / Mesa e comanda)
7. Resumo
8. Perguntas frequentes
9. Manuais relacionados

## Anexo — legendas das imagens (na ordem em que aparecem no texto)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|-------|----------------------------------|------|---------|
| 1 | `05-venda-detalhe.png` | com setas | Detalhe da venda: **Venda Nº 931** e **Pedido Nº 1** na mesma venda |
| 2 | `04-delivery.png` | com setas | Cards do Delivery no formato `#pedido (venda)` |
| 3 | `06-cupom.png` | com setas | Cupom do cliente com **Pedido #1 (931)** em destaque |
| 4 | `02-historico-virada.png` | com setas | A virada do contador: pedido volta a 1 e a venda segue para 931 |
| 5 | `01-parametros-pdv.png` | com setas | Configuração → Parâmetros, card PDV, switch **Número de Pedido no PDV** |
| 6 | `03-historico-mesa.png` | com setas | Cinco vendas de mesa sem número de pedido, entre os pedidos 5 e 6 |

## Observações de conteúdo

- A imagem **`02-historico-virada.png`** é a central do manual. Ela precisa aparecer grande o
  suficiente para o leitor comparar as linhas `1 (931)` e `60 (930)`.
- A ordem `pedido (venda)` é o que o leitor tem de sair sabendo. Repetida de propósito em várias
  seções — não enxugar.
- Na imagem 6, o ponto não é só que a mesa não tem número: é que a contagem do pedido vai de
  **5** para **6** atravessando as cinco mesas, ou seja, **mesa não gasta número**. Manter essa
  explicação junto da tabela.
- As imagens 2, 4 e 6 têm regiões borradas de propósito (telefone, endereço e nomes de clientes).
  Não substituir nem tentar "limpar".
- Não publicar nomes de campo da API (`numeroPreVenda`, `numeroPedido`, `pdvNumeroPedido`),
  números de caixa, endpoints nem nomes de arquivo do código.
