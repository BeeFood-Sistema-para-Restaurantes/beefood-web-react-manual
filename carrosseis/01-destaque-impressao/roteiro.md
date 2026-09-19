# Carrossel — Destaque na impressão

- **Novidade:** [Destaque na impressão: a bebida não fica mais para trás](https://beefood.app/novidades/destaque-impressao) — Novidade, 15/09/2026
- **Áreas:** Impressão, Cardápio, Aplicativos
- **Manual que aprofunda:** [`manuais/destaque-impressao/`](../../manuais/destaque-impressao/destaque-impressao.md) (#99)
- **Formato:** 4:5 (1080×1350) · 8 slides

## Fato → ângulo → o que o slide diz

O texto da novidade descreve o campo, a tela e o efeito, na ordem em que o
recurso foi construído. A publicação é escrita de novo a partir desse fato: nada
inventado, e nenhuma frase copiada.

| Fato (novidade + manual #99) | Ângulo | O que o slide diz | Slide |
|---|---|---|---|
| Campo novo **Destaque na impressão** no cadastro de produto e de complemento | a bebida esquecida na sacola é a dor que todo mundo já teve | "Cansou de esquecer a **bebida**?" | 1 |
| A linha do item marcado sai com fundo escuro e letra clara | no cupom toda linha tem o mesmo peso, e a bebida desaparece dentro do combo | "Você sabe como essa história termina" + o custo em cena (o cliente liga, alguém sai de novo, a nota cai) | 2 |
| Efeito no **Cupom Pedido** e na ficha da cozinha, no presencial e no delivery | é marca-texto impresso | "Olha o que muda no cupom 🖨️" | 3 |
| O campo fica logo abaixo de **Descrição**, em produto e em complemento | é um interruptor, não um projeto | "É só um interruptor 👇" | 4 |
| **Editar em Lote** com o setor filtrado marca vários itens | quem tem cardápio grande não vai abrir item por item | "Tem muita bebida? Marque tudo de uma vez" | 5 |
| No app do Entregador o item aparece em evidência e a entrega pede confirmação | o cuidado não para no balcão | "Seu entregador também vê 🛵" | 6 |
| Usar com critério: marcar tudo anula o efeito | destaque funciona por contraste | "Não saia marcando tudo" | 7 |
| A novidade tem manual publicado no mesmo dia | — | "Acompanhe tudo que entra no sistema" | 8 |

Números: nenhum. A novidade não traz métrica, e o custo do item esquecido está
descrito em cena ("alguém tem que sair de novo, no meio do pico") justamente para
não inventar percentual.

Registro: os títulos passaram por uma segunda reescrita. A primeira leva estava
correta e **travada** — "Um esquecido custa duas viagens", "A linha que importa
para de se esconder", "Todo recurso novo vira manual no mesmo dia". Oito
aforismos seguidos soam placa de museu. O antes-e-depois dos oito virou tabela em
[`roteiro-e-copy.md`](../../.cursor/skills/carrossel/references/roteiro-e-copy.md).

A capa levou uma terceira volta. "Cansou de bebida esquecida na sacola? 🥤" está
correta e tem seis palavras; "Cansou de esquecer a **bebida**?" tem cinco, diz o
mesmo, e o que sobra vai para a imagem. O emoji saiu quando "bebida" ficou
vermelha: vermelho e emoji na mesma linha são dois grifos brigando, e o vermelho
é o que manda o olho para a palavra que carrega o assunto.

O subtítulo voltou às duas linhas — "Sem canetinha na lata, sem grito na cozinha.
O cupom marca sozinho." Ele tinha sido encurtado para "Agora o cupom já sai com
ela marcada" só para abrir altura para a imagem; com o cupom centralizado, as
duas coisas couberam. O título corta até o osso, o subtítulo é onde a frase
respira.

Emoji em três dos oito slides, um em cada: 🖨️ no papel, 👇 apontando o mockup e
🛵 na rua. A capa, o custo, o lote, o limite e o CTA ficam sem — e é o vazio
deles que faz os três funcionarem.

## Slides

| # | Arquivo | Tipo | Ideia única | Imagem |
|---|---------|------|-------------|--------|
| 1 | `01-capa.html` | capa com imagem | A bebida esquecida na sacola tem fim | cupom real com **uma** linha destacada, centralizado em `.figura` e com a base serrilhada — `imagens-puras/01-cupom-bebida.png` |
| 2 | `02-custo.html` | texto | Você já sabe como termina quando o item fica para trás | — |
| 3 | `03-no-papel.html` | antes × depois | O contraste é o que faz a linha ser vista | cupom desenhado em CSS (o "antes" não existe como captura) |
| 4 | `04-onde-ligar.html` | mockup de computador | Um interruptor abaixo de Descrição | `imagens-puras/03-modal-janela.png` em `.sangria--janela`, com `.realce` no campo |
| 5 | `05-em-lote.html` | passos | Editar em Lote marca o setor inteiro | — |
| 6 | `06-na-rua.html` | mockup de celular 3D, com texto ao lado (**tela desenhada**) | O app do entregador pede confirmação | tela desenhada em `.tela-app`, em `.g3d` |
| 7 | `07-limite.html` | texto | Marcar tudo anula o efeito | — |
| 8 | `08-cta.html` | mockup de celular + CTA | Toda novidade fica registrada, com manual | `imagens-puras/04-novidades-celular.png` em sangria centralizada, 660 px |

Cinco dos oito slides têm imagem, e a capa é um deles.

## Decisões de roteiro

**A capa mostra o resultado, e mostra UM destaque — em impressão de verdade.**
O cupom do manual #99 sai com duas linhas em fundo preto, a Coca Cola e o "Sem
Maionese Verde", porque o manual precisava mostrar que complemento também
destaca. Na capa, duas faixas dividem a atenção e dizem o contrário do slide 7
("não saia marcando tudo" depois de uma foto com tudo marcado).

Recortar não resolvia: as duas faixas são **coladas** no cupom, uma acaba em
y 390 e a outra começa ali, então todo corte cai em cima de tinta. Tentei 390,
400, 472 e 590 — nenhum fecha sem parecer erro de render.

O que resolveu foi **gerar matéria-prima nova**: um pedido montado no sandbox com
o combo sem o complemento destacado, cuja impressão sai com a linha preta só na
bebida (pedido #43, `registrar_pedido` no `capturar-telas.py`). Continua sendo
impressão do sistema, não desenho. A impressão é feita num viewport de 340 px
para o papel ocupar a imagem inteira — em viewport largo a bobina fica
centralizada com margem branca dos dois lados, e aí o recorte da arte teria que
mexer no eixo X, que o `.recorte--topo` não faz.

O corte fecha em `680 / 554`: é a última janela que cabe, entre o traço duplo que
fecha o bloco de itens (y 535) e o "Subtotal" (y 557). `.rasgado` come os 13 px
finais e transforma o corte em papel destacado. O canto é de 5 px porque bobina
térmica não tem canto arredondado — os 24 px de fábrica do `.recorte` faziam o
papel parecer cartão.

**E o papel fica centralizado, grande e reto.** A versão anterior encostava o
cupom na direita e o inclinava em `.cena3d`/`.g3d`: virava objeto
fotografado na bancada, mas deixava a metade esquerda do slide vazia **e** saía
menor, porque a inclinação come altura. Centralizado em `.figura`, o mesmo
recorte foi a 728 px — o máximo que cabe entre o subtítulo e o "Arraste" — e
ainda sobrou espaço para o subtítulo voltar às duas linhas que ele tinha. O 3D foi para o slide 6, que é o único com conteúdo do lado
do mockup.

A faixa preta cai no terço de baixo do papel, porque antes dela há 454 px de
cabeçalho de cupom. Dá para subir cortando o topo também, mas aí o topo vira
outro corte para disfarçar; não compensa, e o olho vai na faixa de qualquer jeito
— é o único preto sobre a única forma branca do slide.

**O "antes" é desenho, o "depois" é captura.** O slide 3 compara os dois cupons
em `.cupom` (CSS) porque o cupom sem destaque não existe em `imagens-puras/`:
seria preciso desmarcar o produto, imprimir, remarcar. Bobina térmica em
monoespaçada é claramente desenho, então não engana — e o cupom real já apareceu
na capa, em tamanho grande.

**Um mockup 3D, e ele é o único que divide a faixa.** O celular do slide 6 é o
único em perspectiva, e para isso o corpo do texto desceu para uma coluna de
412 px ao lado dele — é o texto ao lado que dá licença para o aparelho sair do
centro e girar. Ali o texto da tela é grande e ninguém precisa ler rótulo de
interface, então o giro só ajuda.

**E ele gira para dentro** (`.g3d--na-direita`): a quina que afunda é a esquerda,
a que aponta para o texto. O primeiro render girava ao contrário — a face abria
para o texto, a quina de dentro vinha para frente e o aparelho parecia cair para
fora da arte, além de apertar o vão entre a coluna de texto e o mockup. Medido na
tinta do PNG, com a coluna de texto acabando em x 500: o vão mais estreito passou
de 51 para 71 px, e na altura do primeiro parágrafo, de 72 para 134 px.

No slide 4 o leitor tem que achar o interruptor: a face que recua come contraste
justo onde está a informação, e o mockup fica reto. No slide 8 o celular está
sozinho na faixa, então em vez de girar ele **centraliza e cresce** — de 586 para
660 px, com recuo igual dos dois lados. Encostado na direita, como estava, ele
deixava um vão à esquerda e mostrava a página de novidades menor.

**Celular que termina dentro do slide mostra a base da tela.** Com 462 px de
largura e `top: 300px`, o aparelho do slide 6 acaba em y 1335, dentro da arte. Aí
a barra "Confirmar entrega" precisou ir para a base da tela (`flex: 1` no corpo,
`margin-top: auto` no aviso) e a lista ganhou a quarta linha do pedido: no lugar
onde a tela sangrava pela base, esse terço final ficava fora do slide e o aviso
podia ficar no fluxo. Sem esse ajuste a tela fica com 300 px de branco embaixo e
parece render pela metade.

**O mockup de computador sangra pela direita.** O recorte do modal tem 605 px
lógicos e é exibido a 1120 px (1,85×): o rótulo *Destaque na impressão* sai com
27 px na arte, legível no feed. O painel inteiro na mesma janela sairia a 0,8×.
Aqui a sangria é assimétrica de propósito, e não por descuido: ela é 40 px mais
larga que o slide, e o que fica de fora tem de ser a direita, porque o campo e o
interruptor que o slide quer mostrar estão à esquerda da janela.
O `.realce` foi posicionado por medida do arquivo (o interruptor verde está em
y 0,70–0,77), não no olho — as duas primeiras tentativas circularam a linha
*"Exibido nos aplicativos…"*, que é a de cima.

**O app do Entregador entrou como tela desenhada.** Na primeira versão esse
slide ficou fora, e o carrossel perdia a ponta mais convincente da novidade: o
item destacado chega até a rua. O emulador Android não sobe no Cloud Agent
(`MEMORIA-GERAL.md`, seção 6), então a tela é desenhada em `.tela-app`, mostrando
só o que a novidade afirma — item em evidência no pedido e confirmação na
entrega.

O slide teve por três rodadas uma pílula "ILUSTRAÇÃO" no canto. Ela saiu da
skill inteira: numa peça de venda, avisar que a tela não é o produto é a única
frase que o leitor não esperava ler, e rouba o slide. O registro do que é
desenho é este roteiro.

> **Pendente com o dono:** print real do app do Entregador na tela do pedido com
> item destacado e na confirmação de entrega. Quando chegar, substitui o desenho
> do slide 6.

**Sem data na arte.** A capa trazia "15/09/2026" no canto superior direito e
agora traz "1 de 8", como os outros sete. O carrossel fica pronto antes de
entrar na fila de conteúdo, e arte datada anuncia novidade que parece velha. A
data do cupom continua no papel — aquela é do pedido #43, não do post.

**Sem rodapé nos slides 4 e 8.** A janela em sangria cobre a base inteira do
slide 4, e os pontos desenhados por cima dela pareciam sujeira; o "4 de 8" do topo
resolve. No 8, o celular centralizado passou a cobrir a base — e o
`beefood.app/novidades` já está no subtítulo, em negrito, que é onde ele é lido.

## Capturas

```bash
# página pública e lista de produtos (sem clique)
python .cursor/skills/carrossel/scripts/capturar.py destaque-impressao \
    --url https://beefood.app/novidades --nome 01-pagina-novidades --publico
python .cursor/skills/carrossel/scripts/capturar.py destaque-impressao \
    --rota /cardapio --nome 02-cardapio-produtos

# telas que exigem clique
python carrosseis/01-destaque-impressao/capturar-telas.py

# cupom da capa: 'venda' registra o pedido #43 (uma vez), 'cupom' reimprime
python carrosseis/01-destaque-impressao/capturar-telas.py venda
python carrosseis/01-destaque-impressao/capturar-telas.py cupom
```

De `imagens-puras/`, os slides usam `01-cupom-bebida.png`, `03-modal-janela.png`
e `04-novidades-celular.png`. As outras ficam como **fonte**: o
`03-modal-produto.png` é de onde os recortes saem, o `03-modal-recorte.png` é a
faixa fechada do interruptor (sobrou depois que a janela em sangria passou a dar
conta da legibilidade) e as duas primeiras são contexto da rodada de captura.
Mesmo princípio dos manuais — a pura é backup, não é a arte.

Produto do exemplo: **Coca Cola 350ml** do setor **Bebidas** (BeeFood3 - Manual).
O sandbox tem dois produtos com esse nome — o script clica pelo cartão do setor,
não pelo nome solto.

## Render e entrega

```bash
python .cursor/skills/carrossel/scripts/renderizar.py \
    carrosseis/01-destaque-impressao --contato
python .cursor/skills/carrossel/scripts/conferir-texto.py destaque-impressao
python .cursor/skills/carrossel/scripts/empacotar.py destaque-impressao
```

A legenda, o primeiro comentário e o texto alternativo de cada imagem estão em
[`copy-instagram.txt`](copy-instagram.txt). O que vai para quem publica é
`entrega/01-destaque-impressao.zip`: as oito imagens mais aquele `.txt`.
