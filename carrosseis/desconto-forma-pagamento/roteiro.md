# Desconto ou acréscimo por forma de pagamento

- **Novidade:** [Desconto ou acréscimo por forma de pagamento](https://beefood.app/novidades/desconto-acrescimo-forma-pagamento) — 17/08/2026
- **Manual:** [`manuais/cardapio-digital-desconto-formas/`](../../manuais/cardapio-digital-desconto-formas/cardapio-digital-desconto-formas.md) (#64) e [`manuais/formas-recebimento/`](../../manuais/formas-recebimento/formas-recebimento.md) (#82)
- **Formato:** 4:5 (1080×1350), 7 slides
- **Pasta com nome curto:** o slug publicado tem quatro palavras;
  `conferir-texto.py` recebe `--novidade desconto-acrescimo-forma-pagamento`.

## Fato → ângulo → ideia de uso → o que o slide diz

O **fato**, sem adjetivo, lido na novidade e nos dois manuais:

- cada forma de recebimento passa a carregar um **ajuste automático**: desconto
  ou acréscimo, em % ou em R$ — cinco opções num campo só;
- o ajuste incide sobre o **subtotal dos produtos**;
- configura-se em três lugares: `Cadastros → Formas de Recebimento` (vendas do
  BeeFood), `Cardápio Digital → Formas Recebimento` (pedidos do cliente) e
  `Cardápio Digital → Pagamento Online` (Pix online e cartão online);
- aparece no cardápio digital (no fechamento, ao escolher a forma), no totem, na
  tela de pagamento do BeeFood e no pedido pelo chat do WhatsApp.

O **ângulo** é o custo que o dono já conhece e nunca conseguiu transferir para o
pedido de delivery: forma de pagamento não é neutra. No balcão ele negocia na
boca ("no Pix eu tiro 5%") e no cardápio digital não há ninguém para negociar.

| Fato | Ângulo | Ideia de uso | O que o slide diz |
|---|---|---|---|
| desconto automático por forma, em % ou R$ | o Pix custa menos que o cartão | dar o desconto no Pix e deixar o cliente se convencer sozinho | **1.** Dê 5% de desconto no **Pix** |
| o ajuste é do produto, não da conversa | no balcão ele já faz isso na boca | reconhecer que a prática existe e mostrar onde ela não alcança | **2.** Você já faz isso no **balcão** |
| o aviso aparece em cada forma, antes da escolha | ninguém precisa perguntar | pôr o desconto na tela e parar de pedir | **3.** Seu cliente vê o desconto e escolhe **sozinho** |
| desconto e acréscimo, calculados no subtotal | o cartão tem taxa; o Pix não | cobrar o custo de quem escolhe o caro, e só dele | **4.** O mesmo pedido, **dois** totais |
| cinco opções num campo: %, R$, desconto, acréscimo | R$ 3,00 fixos rendem mais em ticket baixo | escolher a régua pela margem, não pelo que o sistema oferece | **5.** Ajuste em **reais** ou em porcentagem |
| vale no PDV, mesa, comanda, delivery, totem e chat | o caixa também sofre com isso | ver o ajuste na tela de pagamento, na hora | **6.** No caixa o ajuste **já** vem na tela |
| onde ligar | — | um pedido só | **7.** Ligue o desconto do Pix **hoje** |

Nenhuma frase sobrevive igual à da novidade — o `conferir-texto.py` mede isso na
janela de seis palavras, e passa limpo.

## Slides

| # | Arquivo | Tipo | Imagem |
|---|---------|------|--------|
| 1 | `01-capa.html` | capa escura | celular: a sacola com o desconto do Pix e o total abatido |
| 2 | `02-balcao.html` | texto | — |
| 3 | `03-na-sacola.html` | recorte | a lista de formas, cada uma com o seu selo |
| 4 | `04-dois-totais.html` | par de recortes | o mesmo pedido de R$ 39,00, no Pix e no vale |
| 5 | `05-um-campo.html` | recorte | a lista de cinco opções, aberta no painel |
| 6 | `06-no-caixa.html` | recorte | os botões de forma de pagamento com o ajuste embaixo do nome |
| 7 | `07-cta.html` | capa escura | celular na página de novidades |

Cinco dos sete slides têm imagem, e todas são **captura de produção** — nenhuma
tela desenhada, nenhum número inventado. O que muda de slide para slide é o
recorte, não o arquivo.

### As aberturas

Sete imperativos em fila seriam template do mesmo jeito que sete "você pode".
A sequência alterna: ordem direta (1), reconhecimento (2), o ganho dito direto
(3), constatação com a prova na imagem (4), ordem direta (5), o lugar (6) e o
pedido final (7). As palavras em vermelho também não se repetem — Pix, balcão,
sozinho, dois, reais, já, hoje.

### O slide 2 elogia antes de cobrar

O furo só entra depois da premissa que o leitor aceita. "Você já faz isso no
balcão" é verdade e é elogio: negociar a forma de pagamento na boca do caixa é
gestão, não improviso. A falta aparece na frase seguinte, junto da consequência —
no cardápio digital não há quem negocie, e a taxa do cartão sai do lucro.

A versão que **não** ficou perguntava quanto o cartão custa por mês. É a fatura
na cara, no slide em que o leitor decide se arrasta.

## Imagens: de onde vem cada uma

Todas as capturas são prints de produção que os manuais #64 e #82 já versionam.
O `recortar.py` desta pasta lê esses arquivos e grava só o pedaço que cada slide
usa, com as coordenadas medidas no arquivo com Pillow e comentadas no script.
Não há imagem nova do sistema aqui — o que existe é recorte.

| Arquivo em `imagens-puras/` | Origem | Por que recortar |
|---|---|---|
| `sacola-formas.png` | #64 `07-cardapio-outras.png` | a lista inteira tem 844 px de altura; o slide mostra do "Pague online" até o dinheiro, e o selo de 11 px sobe para 25 px na arte |
| `total-pix.png`, `total-vale.png` | #64 `06-cardapio-pix.png` e `08-cardapio-vale.png` | o mesmo cartão de valores nos dois pedidos, cortado na mesma altura, para o leitor comparar o cartão e não duas fotos parecidas |
| `lista-ajuste.png` | #82 `04-ajuste-pagamento.png` | a lista aberta ocupa um oitavo da tela do painel; a tela inteira no slide fica com letra de 10 px |
| `caixa-formas.png` | #82 `08-pagamento-presencial.png` | três colunas de oito, escolhidas por serem as que têm ajuste: dinheiro (−1,00%), crédito (+3,00%) e vale alimentação (+R$ 5,00) |

A única captura feita para este carrossel é a do CTA (`novidades-celular.png`),
no `capturar-telas.py`: a página de novidades rolada até o **título** desta
publicação encostar no cabeçalho fixo, para a data de publicação ficar atrás
dele e não datar o post.

### Dois exemplos numéricos, e por que os dois ficam

Os slides do cardápio mostram **5%** e os do caixa mostram **−1,00%**, **+3,00%**
e **+R$ 5,00**. Não é descuido: são duas configurações diferentes do mesmo
sandbox, porque o ajuste do cardápio digital e o das vendas do BeeFood são
cadastrados em lugares distintos. Manter as duas é o que permite provar, com
captura, que o ajuste existe em porcentagem **e** em reais.

### A imagem prova o título?

- **1.** o título diz "5% no Pix" e a tela mostra `Pix Online — 5% de desconto`
  escolhido, com `Total R$ 37,05`;
- **3.** o título diz que o cliente vê antes de escolher, e o recorte é a lista
  de formas **antes** da escolha, cada uma com o seu selo;
- **4.** o título diz "dois totais", e são dois: `R$ 37,05` e `R$ 40,95`, do
  mesmo `R$ 39,00`;
- **5.** o título diz "em reais ou em porcentagem", e a lista aberta tem as
  quatro combinações mais o "sem ajuste";
- **6.** o título diz que o ajuste vem na tela do caixa, e ele está impresso
  embaixo do nome de cada forma.

## O que ficou de fora

A novidade lista o **Aplicativo Garçom** entre o que ainda não aplica o ajuste.
Peça de venda não anuncia o limite do recurso: quem precisa dessa linha abre o
manual, que está a um clique. Pelo mesmo motivo não entrou o "até 1 minuto" que
o cardápio leva para receber a mudança do painel.

Também ficou de fora a aba **Pagamento Online**, onde o Pix online tem desconto
próprio: é mais um lugar de cadastro, e o slide que ele ocuparia diria a mesma
coisa que o slide 5.

## Legenda

Em [`copy-instagram.txt`](copy-instagram.txt), com o primeiro comentário e o
texto alternativo de cada imagem.
