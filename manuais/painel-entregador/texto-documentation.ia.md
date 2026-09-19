# texto-documentation.ia.md — Painel para Entregadores (#120)

## PROMPT (copiar e colar)

Em **Entrega**, crie um novo item de menu por último chamado **Painel para Entregadores**.

Leia APENAS os arquivos abaixo (não varra o resto do projeto):

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/painel-entregador/painel-entregador.md`
2. Imagens (nesta ordem):
   - `beefood-web-react-manual/manuais/painel-entregador/imagens-tratadas/01-painel-completo.png`
   - `beefood-web-react-manual/manuais/painel-entregador/imagens-tratadas/02-abrir-pela-tela-delivery.png`
   - `beefood-web-react-manual/manuais/painel-entregador/imagens-tratadas/03-abrir-por-aplicativos.png`
   - `beefood-web-react-manual/manuais/painel-entregador/imagens-tratadas/04-detalhe-do-pedido.png`

NÃO leia outros arquivos (`fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `capturar.py`,
`smoketeste.py`, `pedido_*.py`, `exp_*.py`, `marketplace-db.js`, `molde-pedido.json`,
`imagens-puras/`).

- Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa".
- pt-BR, didático; destacar os obrigatórios; não publicar o rodapé de referências internas.
- Palavras que o leitor vai buscar e que devem sobreviver na página: *painel do
  entregador*, *tela para TV*, *pedido pronto*, *pedido em preparo*, *o meu já saiu*,
  *acompanhamento de entregadores*, *painel de retirada*, *iFood*, *99Food*, *Keeta*,
  *Aiqfome*.

## Estrutura da página (na ordem do `.md`)

1. Título e para que serve — a mentalidade: informação na parede em vez de conversa no
   balcão.
2. Pré-requisitos — permissão de **Gestão de Entregas**, recurso em liberação, computador
   ligado na TV.
3. **1. O que a tela mostra** — as duas colunas, a busca, o cartão, a janela de 6 horas e a
   atualização automática.
4. **2. Abrir pela tela Delivery** — menu dos três pontinhos.
5. **3. Abrir por Aplicativos** — card na categoria Entrega e o botão ABRIR PAINEL (F2).
6. **4. Ver os detalhes de um pedido** — a janela de leitura.
7. Dicas.
8. Onde isto não serve — Delivery e Gestão de Entregas são as telas de operação.

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|---|---|---|---|
| 1 | `01-painel-completo.png` | com setas (7) | O painel aberto: busca, as colunas Em preparo e Pronto, o logo do canal, o número da plataforma, o tempo da etapa e o aviso de atraso |
| 2 | `02-abrir-pela-tela-delivery.png` | com moldura e seta (1) | O menu de ações do Delivery, com o item Painel Entregador |
| 3 | `03-abrir-por-aplicativos.png` | com setas (2) | A janela de apresentação em Aplicativos e o botão ABRIR PAINEL (F2) |
| 4 | `04-detalhe-do-pedido.png` | com setas (4) | O detalhe do pedido aberto pelo cartão: etapa e canal, cliente, itens e total |

## Observações de conteúdo

- O manual **não ensina a criar pedido** e **não ensina a operar** — é tela de leitura.
  Toda ação continua no Delivery e na Gestão de Entregas.
- Na imagem 4 o nome do cliente aparece **desfocado**, e o texto do manual explica o
  motivo. Manter o desfoque: as capturas são de produção e o repositório é público.
- O recurso está **em liberação** (lista de empresas no código). O aviso do
  pré-requisito deve ir para a página.
