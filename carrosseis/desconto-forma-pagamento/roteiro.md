# Desconto ou acréscimo por forma de pagamento

- **Novidade:** [17/08/2026](https://beefood.app/novidades/desconto-acrescimo-forma-pagamento)
  — áreas Pagamento, Cardápio Digital e Sistema
- **Manuais lidos:** [`cardapio-digital-desconto-formas`](../../manuais/cardapio-digital-desconto-formas/cardapio-digital-desconto-formas.md)
  e [`formas-recebimento`](../../manuais/formas-recebimento/formas-recebimento.md)
- **Formato:** 4:5 (1080×1350), 7 slides
- **Imagens:** 5 capturas próprias, todas de tela real

## A terceira versão: a capa nomeia o recurso

A segunda versão acertou a imagem e o fato, e voltou pelo **texto** de três
slides. O diagnóstico está em *o sétimo vício: a manchete-conceito* na
`MEMORIA-CARROSSEIS.md`; aqui ficam as trocas:

| Devolvido | O que esta versão diz | Por quê |
|---|---|---|
| capa: "Cada forma de pagamento com o seu **preço**" | "Acréscimo e desconto por **forma** de pagamento" | a capa nomeia o recurso. A anterior tinha os três eixos e não dizia o nome de nada — conceito, e o dono leu como fuga da funcionalidade |
| slide 2: "O pedido tinha um preço **só**" | "O ajuste entra sozinho no **total**" | o slide 2 explica o recurso. A anterior contava o antes do sistema, e história ali gasta o lugar de quem ainda não entendeu o que a capa anunciou |
| CTA: "Comece pela forma que mais **entra**" | "Ligue o primeiro **ajuste** hoje" | o pedido é a ação, com a palavra do recurso. "Mais entra" é metáfora e não diz o que fazer |
| slide 5: "A forma que cai na hora pode sair mais **barata**" | "Desconto numa, acréscimo na **outra**" | mesmo vício do CTA, não apontado na revisão. O título agora é a captura em palavras |

As quatro são o mesmo erro: metáfora onde existia a palavra do recurso
(desconto, acréscimo, ajuste). Ordem dos três primeiros slides, que agora é
regra da skill: a capa **nomeia**, o slide 2 **explica**, o slide 3 **mostra**.

## A segunda versão, e o que derrubou a primeira

A primeira versão desta peça voltou inteira, por três motivos que a memória da
skill autorizava e agora proíbe (ver *a 19ª rodada devolveu a peça inteira* na
`MEMORIA-CARROSSEIS.md`). Registrado aqui porque é o que explica cada escolha
abaixo:

| Falha | O que esta versão faz |
|---|---|
| a capa dizia "Dê 5% de desconto no Pix" — um dos exemplos do release, promovido a manchete, com o acréscimo e o ajuste em R$ de fora | a capa diz o fato com os três eixos, e a **imagem** também: uma lista de formas com desconto numa, acréscimo na outra, em R$ e em % |
| cinco das seis imagens eram recorte de print de manual, o que trouxe o aviso de cashback e o de cupom para a capa e **dois jogos de número** para a peça | as cinco imagens são captura feita para este carrossel, com **um** exemplo montado no sandbox |
| o slide 2 afirmava a rotina do leitor ("Você já faz isso no balcão. No caixa você propõe na hora") | o slide 2 fala do sistema: a taxa da forma já estava cadastrada, o preço do cliente é que não acompanhava |

## O fato, inteiro

Três eixos, e nenhum pode sair da peça — cada um muda **quem** se interessa:

1. **desconto ou acréscimo.** Quem quer repassar a taxa do crédito não tem
   interesse num post sobre desconto.
2. **em % ou em R$.** Valor fixo é a régua de quem tem ticket baixo.
3. **no cardápio, no totem, no caixa e no chat.** Quem não tem delivery para de
   ler se a capa falar só de cardápio digital.

O ajuste incide sobre o **subtotal dos produtos** e aparece para o cliente no
fechamento, ao escolher a forma. Configura-se em três lugares:
`Cadastros → Formas de Recebimento` (vendas do BeeFood),
`Cardápio Digital → Formas Recebimento` (pedidos do cliente) e
`Cardápio Digital → Pagamento Online` (Pix e cartão online).

## O ângulo, e de onde ele sai

O ângulo é o custo que o recurso resolve, e ele está no manual
`formas-recebimento` — não em cenário nenhum inventado:

> "**Taxa** e **Dias para Recebimento** são o seu contrato com a adquirente, **não
> o preço do cliente**."

E, na mesma página: "o **Tipo** decide se existe aba de taxas — Dinheiro, Fiado e
PIX Online não têm". Ou seja: o sistema já sabia que receber custa diferente em
cada forma, e guardava a taxa e o prazo de cada uma. O que não existia era um
caminho dessa diferença até o total do pedido. É isso que mudou, e é isso que a
peça conta.

## Fato → ângulo → o que o slide diz

| Fato (novidade ou manual) | Ângulo | O que o slide diz |
|---|---|---|
| Cada forma pode ter desconto **ou** acréscimo, em % **ou** em R$ | o nome do recurso é a notícia | "Acréscimo e desconto por **forma** de pagamento" |
| O ajuste é automático e incide sobre o subtotal; o cliente vê ao escolher a forma | o dono marca uma vez e não faz conta nenhuma | "O ajuste entra sozinho no **total**" |
| O ajuste incide sobre o subtotal e aparece no fechamento, com o nome da forma | a prova é a tela | "Mesmo pedido, **dois** totais" |
| Cinco opções no **Ajuste no pagamento**: sem ajuste, desconto e acréscimo, em % e em R$ | valor fixo e porcentagem servem a pedidos de tamanhos diferentes | "Escolha **reais** ou porcentagem" |
| Cada forma tem o seu ajuste, e "sem ajuste" é uma das cinco opções | o ajuste é por forma, e vai nos dois sentidos na mesma lista | "Desconto numa, acréscimo na **outra**" |
| Vale no Cardápio Digital, no Totem, na tela de pagamento do BeeFood e no BeeBot | não é recurso de delivery | "Vale no totem, no caixa e no **chat**" |
| Já está no ar, nas três telas de configuração | um pedido só, e é uma ação | "Ligue o primeiro **ajuste** hoje" |

Nenhuma frase afirma o que o leitor faz, tem ou sente. O teste aplicado em cada
linha: **quem poderia desmentir isto?** Tudo acima está na tela, na novidade ou
no manual.

## Os slides

| # | Arquivo | Ideia única | Imagem |
|---|---------|-------------|--------|
| 1 | `01-capa.html` | **nomeia:** acréscimo e desconto por forma de pagamento | `formas-lista.png` no celular, em sangria |
| 2 | `02-como-funciona.html` | **explica:** o ajuste é automático e cai no total | — |
| 3 | `03-dois-totais.html` | **mostra:** o mesmo subtotal fecha em dois totais | `total-dinheiro.png` + `total-credito.png` |
| 4 | `04-regua.html` | o ajuste pode ser fixo ou proporcional | `painel-ajuste.png` em janela de navegador |
| 5 | `05-forma-por-forma.html` | os dois sentidos convivem na mesma lista | `painel-lista.png` em recorte, sem realce |
| 6 | `06-onde-vale.html` | vale nos quatro canais, não só no delivery | — |
| 7 | `07-cta.html` | ligar o primeiro ajuste | `novidades-celular.png` no celular |

Cinco dos sete slides têm imagem. As aberturas não se repetem: nome do recurso,
mecanismo, prova em tela, ordem direta, par de exemplos, enumeração de canais e
pedido.

## O exemplo numérico, e por que é um só

Um jogo de números na peça inteira, e é o da própria novidade:

| Forma | Ajuste | No pedido de R$ 39,55 |
|---|---|---|
| PIX Online | 5% de desconto | − R$ 1,98 |
| Dinheiro | R$ 3,00 de desconto | − R$ 3,00 → **R$ 36,55** |
| Cartão de Crédito | 2% de acréscimo | + R$ 0,79 → **R$ 40,34** |

O pedido é Combo One Burger + batata frita + Coca Cola, em retirada, sem cupom e
sem cashback. O `capturar-telas.py` cadastra esse exemplo no sandbox antes de
fotografar e **devolve** a configuração que encontrou — ela é a que os manuais
versionam.

A versão anterior misturava dois jogos (5% nas telas do cardápio, −1,00%/+3,00%/
+R$ 5,00 nas do caixa) porque cada print vinha de um manual com outra
configuração. Lido de fora, pareciam duas versões do recurso.

## Capturas

Todas próprias, em `imagens-puras/`, nenhuma editada:

| Arquivo | O que é | Como saiu |
|---|---|---|
| `formas-lista.png` | gaveta de formas do cliente, com os três selos | cardápio público no celular, barra de cupom fechada |
| `total-dinheiro.png` | cartão `Resumo de valores` com o desconto | print do **elemento**, não da página |
| `total-credito.png` | o mesmo cartão com o acréscimo | idem |
| `painel-ajuste.png` | campo `Ajuste no pagamento` com as cinco opções | painel 1440×900, DPR 2 |
| `painel-lista.png` | lista de formas com o selo de cada uma | idem |
| `novidades-celular.png` | o cartão desta novidade | `<time>` escondido: data não entra em arte |

Print de manual **não** entrou na arte. Os dois manuais foram lidos para saber
quais campos existem, que valores são reais e qual tela prova o quê — e é o que
tornou a captura barata.

## Decisões de arte

- **A capa é a gaveta de formas, e não um total com desconto.** Um total mostra
  um sentido do ajuste; a gaveta mostra o par (selo verde de desconto, selo
  vermelho de acréscimo) e as duas unidades (R$ 3,00 e 2%) na mesma imagem.
- **O slide 3 empilha as duas imagens** em vez de pô-las lado a lado: os cartões
  de valores são deitados (2,6/1), e empilhados cada um sai 1,7x maior — o
  `R$ 36,55` e o `R$ 40,34` precisam ser legíveis no feed.
- **Slide 4 e 5 vão retos**, e centralizados: a imagem está sozinha na faixa nos
  dois. São também os dois slides em que o leitor lê rótulo de interface, e a
  face que recua no 3D come contraste justo ali. A janela de navegador fica só
  no 4; no 5 o recorte vai sem moldura, porque duas barras de navegador
  seguidas viram moldura repetida.
- **Sem `.realce` no slide 5.** O anel diz "olhe aqui", e ali o assunto são as
  três linhas juntas — desconto em R$, nenhum ajuste e acréscimo em %. Um anel
  num selo só contaria a metade que a primeira versão contou.
- **Onde a captura termina é decisão do slide, não do arquivo.** As duas telas de
  painel vão inteiras em `imagens-puras/` e o slide corta por CSS: 514 px de 540
  no slide 4 (logo depois da borda do menu, antes do rótulo `DISPONIBILIDADE`) e
  520 px de 556 no slide 5 (depois do terceiro cartão, antes da faixa do
  quarto). Rótulo cortado no meio lê como falha de render.
- **A capa usa `titulo--medio`, e é o nome do recurso que pede.** Em 92 px,
  "Acréscimo e desconto por forma de pagamento" quebra em quatro linhas e não
  sobra slide para a imagem; em 68 px ela fecha em duas, e o aparelho volta para
  620 px de largura em 560 px de altura — nessa medida o selo de acréscimo do
  crédito ainda entra e o subtítulo cabe em duas linhas.
- **Nenhum emoji em título:** todos têm palavra em vermelho, e grifo em cima de
  grifo cancela os dois. O único emoji da peça é o 💳 da própria novidade, e ele
  vai no **rótulo do cartão** do slide 6 — o chapéu é vermelho inteiro, e emoji
  ao lado de vermelho é a mesma colisão.
