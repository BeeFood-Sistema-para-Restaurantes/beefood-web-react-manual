# MEMORIA.md — #132 Código de barras no cupom para marcar o pedido como Pronto

## O pedido do dono

> *"novo manual, faça git pull nos fontes e crie o novo manual simples de como configurar e
> usar"* — 03/11/2026, acompanhado do guia interno de teste *"Como testar (só navegador) —
> código de barras → PRONTO"*.

O guia de teste é **insumo, não produto**. Ele descreve o recurso em duas linhas — o cupom do
Delivery ganha um EAN-13 com o `preVendaID`, e bipar esse código na tela Delivery move o
pedido de AGUARDANDO ou PREPARO para PRONTO — e traz a tabela que separa a flag nova da
antiga. O que o dono pediu é o manual **simples de configurar e usar**, então o guia virou
roteiro de verificação, e os cenários A–F dele viraram a tabela de problemas e o FAQ.

## O que entrou e o que ficou fora

**Entrou:** onde a caixinha mora, marcar e salvar, de onde o cupom sai, o cupom sem e com o
código (e o pé dele de perto), a fila antes e o pedido depois da leitura, os dois avisos de
bipe que não move nada, e a tabela que separa as duas caixinhas de código de barras.

**Ficou fora, de propósito:** o módulo de impressão do Windows (`BeeFood3_Impressao.exe`,
que o dono tirou do escopo e aparece só como uma linha na tabela de problemas), o fluxo do app
do entregador — que tem manual próprio — e todo o resto da aba *Texto Padrão*. Regra 0:
imagem só entra se o leitor sair dela fazendo algo diferente, e as outras opções do layout não
são deste manual.

## A descoberta que deu forma ao manual

**A flag nova não é a flag antiga com outro nome.** As duas caixinhas ficam encostadas na
mesma aba, e a diferença está no código, não no rótulo: `beeEntregaCodigoBarras` exige
`tipoPedido === 'DELIVERY'`, endereço e plano de entregas; `beeCodigoBarrasPronto` exige
apenas `venda.tipo === 'DELIVERY'`, isto é, o **módulo** Delivery. Quem só trabalha com
retirada no balcão nunca tinha visto código de barras no cupom.

Isso virou a espinha do manual: a imagem do cupom é a de um pedido de **retirada**, porque
nela o código de barras só pode ter vindo da flag nova. O par de medições que sustenta a
afirmação está no `fluxo-codigo.md`.

As outras três que o código entregou e a tela não diz:

- **Ligar as duas não imprime dois códigos.** O bloco está sob um `||`, e entra uma vez. Sem
  essa frase, o lojista desliga uma por medo.
- **O leitor da tela Delivery está sempre ligado**, nas duas chamadas de
  `useLeitorCodigoBarras` (`ativo = true`), e não tem configuração nenhuma. A única
  configuração do recurso é a caixinha do cupom.
- **O leitor ignora a leitura** quando o foco está em `INPUT`/`TEXTAREA`/`SELECT` ou quando
  existe `[role="dialog"]` na página, e zera o buffer quando passam mais de 50 ms entre dois
  dígitos. É isso, e não um defeito, que explica *"bipei e nada aconteceu"* e
  *"digitei à mão e não funcionou"*.

## O cenário

A fila do sandbox abria vazia, e a janela do Delivery olha a hora de **criação** do pedido —
então não dava para reaproveitar nada. O `capturar.py` semeia dois pedidos pela rota da
própria tela (`POST /api/venda2/salvar`), um de **retirada** e um de **entrega**, os dois já
nascendo em `PREPARO`, e cancela no fim.

Três detalhes que custaram tempo e ficam registrados:

1. **`tipoPedido: "RETIRADA"` volta da API como `BALCAO`.** O `cmd_capturar` procura
   `BALCAO` primeiro justamente por isso.
2. **A listagem do Delivery não devolve as observações.** A sentinela de texto nas observações
   não serve de filtro ali, então o `semear` anota os `preVendaID` em `/tmp` e o `limpar`
   exige os três: id anotado, nome fictício do cenário e `origem = Manual`.
3. **A observação sai impressa no cupom.** A primeira rodada semeou com `[SMOKE-BARRAS]` no
   `obsx` e o cupom da foto saiu com `Obs: [SMOKE-BARRAS] retirada 03/11 20:59`. Os pedidos
   foram cancelados e refeitos com observação vazia. Quando o cupom é uma das imagens, o
   marcador do cenário não pode ser texto que o cupom imprime.

O cancelamento de pedido do Delivery **não é** uma rota própria: é
`POST /datasnap/rest/venda2/atualizaSituacaoDelivery` com `situacaoDelivery: "CANCELADO"`. O
mesmo caminho serve para devolver o pedido a `PREPARO`, o que virou o comando `rebobinar` —
útil porque a imagem 05 teve de ser refeita.

## A revisão pedida pelo dono

> *"volte para manuais/delivery-codigo-barras-pronto e melhore, falta: mostrar o impresso,
> mais imagens. resumir mais."* — 03/11/2026, depois de ler a primeira entrega.

As duas primeiras linhas eram a mesma coisa: **o impresso estava subdocumentado**. A primeira
entrega tinha uma única foto de cupom, e o controle com a flag desligada existia só como prova
interna, no `/tmp`. Quem lê não sabe como era o pé do cupom antes, nem de onde o cupom sai, nem
o que o leitor tem de mirar. A revisão respondeu com cinco imagens novas:

- o **par antes/depois** do mesmo pedido (`04` e `05`) — a captura de controle virou imagem;
- o **pé do cupom de perto** (`06`), por `clip` medido no `bounding_box()` do `<svg>`;
- o **botão de impressora** do painel do pedido (`03`), que é de onde o impresso sai na hora;
- os **dois avisos** de bipe que não move nada (`09` e `10`).

E *"resumir mais"* não briga com *"mais imagens"*: as duas telas de aviso **saíram da tabela de
problemas**, as legendas em tabela embaixo de cada imagem deram lugar ao `(N)` na frase que
antecede a imagem, e o FAQ perdeu as perguntas que eram a mesma pergunta duas vezes. Resultado:
o dobro das imagens, de 2264 para 1678 palavras.

## As capturas

Dez imagens, dezessete setas. Sete em 2160x1350; as três do impresso saem do próprio HTML de
impressão, em 630 de largura.

- O cupom é escrito num iframe oculto (`beefood-print-frame`) e seguido de `print()`, que
  travaria o Playwright. O gancho do #99 guarda o HTML e neutraliza o `print()`. O botão de
  impressora do painel de detalhe é o `svg.lucide-printer.h-5` — o `h-4 w-4 text-red-500` do
  alto da tela é o status do BeeImpressão, e clicar nele abre outra janela.
- O `full_page` do cupom herda a altura da viewport, então a viewport foi para 420x480 para a
  imagem não sair com um palmo de branco embaixo.
- O aviso de confirmação entra deslizando da direita. Esperar 2,5 s depois do Enter pegou o
  aviso cortado pela metade; o certo é esperar o texto aparecer (`get_by_text`) e **só então**
  deixar assentar.
- `annotate.py` ganhou `escala_etiqueta`, usado só nas imagens do cupom: num PNG de 630 px de
  largura, o círculo proporcional sairia menor que o texto ao lado.
- **A ordem de execução não é a ordem do manual.** O cupom "antes" (imagem `04`) só existe
  enquanto a caixinha está desligada, então o passo `antes` roda antes do passo `config`, que
  liga a flag. O `cmd_capturar` aborta se encontrar a flag já ligada no passo `antes` — refazer
  o par com a flag ligada daria duas imagens iguais e uma afirmação falsa no manual.
- **Aproximação é captura, não corte.** A imagem `06` é um segundo `screenshot` da mesma página,
  com `clip` calculado a partir do `bounding_box()` do `<svg>` do código. Recortar a pura depois
  quebraria a regra de não gravar nada nela. A margem de cima é de 85 px porque menos que isso
  corta a linha *Cobrar do Cliente* no meio da letra.
- **Ponta de seta em cima do alvo tapa o alvo.** A seta 2 da imagem `07` cobria o `0` do
  contador da coluna PRONTO, e a seta 1 da `08` cobria uma palavra do aviso. As duas passaram a
  parar logo abaixo do alvo.
- **Aviso de duas linhas não deixa lugar para a etiqueta.** Entre a tarja de *Pedido não
  encontrado* e o topo das colunas sobram 27 px, e o círculo tem 28. A etiqueta da imagem `10`
  foi para a esquerda, na faixa branca ao lado da tarja, em vez de ficar debaixo dela.
- **Cada aviso quer a fila recarregada.** Dois bipes seguidos empilham duas tarjas na tela, e
  duas tarjas não explicam nada. O `cap_aviso` recarrega `/delivery` antes de cada leitura.

## O estado do sandbox depois

O layout DELIVERY voltou para `beeEntregaCodigoBarras=True` e `beeCodigoBarrasPronto=False`,
que é como estava — os dois valores ficaram guardados em `/tmp/barras-pronto-estado.json`
antes da primeira escrita. Os seis pedidos criados nas três rodadas (`62986342`, `62986343`,
`62987841`, `62987842` e, na rodada da revisão, `63002108` e `63002110`) foram cancelados.
