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
| Campo novo **Destaque na impressão** no cadastro de produto e de complemento | a bebida esquecida na sacola é a dor que todo mundo já teve | "Cansou de bebida esquecida na sacola? 🥤" | 1 |
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
[`roteiro-e-copy.md`](../../.cursor/skills/carrossel-novidades/references/roteiro-e-copy.md).

Emoji em quatro dos oito slides, um em cada: 🥤 na capa, 🖨️ no papel, 👇
apontando o mockup e 🛵 na rua. Os slides de custo, de lote, de limite e o CTA
ficam sem — e é o vazio deles que faz os quatro funcionarem.

## Slides

| # | Arquivo | Tipo | Ideia única | Imagem |
|---|---------|------|-------------|--------|
| 1 | `01-capa.html` | capa com imagem | A bebida esquecida na sacola tem fim | cupom real recortado em **uma** linha destacada — `manuais/destaque-impressao/imagens-puras/05-cupom-pedido.png` |
| 2 | `02-custo.html` | texto | Você já sabe como termina quando o item fica para trás | — |
| 3 | `03-no-papel.html` | antes × depois | O contraste é o que faz a linha ser vista | cupom desenhado em CSS (o "antes" não existe como captura) |
| 4 | `04-onde-ligar.html` | mockup de computador | Um interruptor abaixo de Descrição | `imagens-puras/03-modal-janela.png` em `.sangria--janela`, com `.realce` no campo |
| 5 | `05-em-lote.html` | passos | Editar em Lote marca o setor inteiro | — |
| 6 | `06-na-rua.html` | mockup de celular (ilustração) | O app do entregador pede confirmação | tela desenhada em `.tela-app`, com `.selo-ilustracao` |
| 7 | `07-limite.html` | texto | Marcar tudo anula o efeito | — |
| 8 | `08-cta.html` | mockup de celular + CTA | Toda novidade fica registrada, com manual | `imagens-puras/04-novidades-celular.png` em sangria |

Cinco dos oito slides têm imagem, e a capa é um deles.

## Decisões de roteiro

**A capa mostra o resultado, e mostra UM destaque.** O cupom real do manual #99
tem três linhas em fundo preto (Coca Cola, Sem Maionese Verde, Molho verde). A
capa com as três ficava bonita e dizia o contrário do slide 7 — "não saia
marcando tudo" depois de uma foto com tudo marcado. O recorte fecha em
`600 / 390`, que é o fim exato da linha da bebida (a faixa preta vai de y 341 a
439 e tem duas linhas de 49 px), então sobra só ela. O corte é declarado no
`aspect-ratio` do slide, sem gerar arquivo novo: duas cópias do mesmo cupom
seriam duas verdades para manter.

Com o recorte deitado, a sangria pela base cortava justo a faixa preta. O papel
passou a ser tratado como **objeto na bancada**: 620 px, inteiro dentro do slide,
inclinado −3°, cantos de baixo quase retos porque o arredondamento comia a ponta
da faixa. A sangria continua valendo para mockup de aparelho (slides 4, 6 e 8).

**O "antes" é desenho, o "depois" é captura.** O slide 3 compara os dois cupons
em `.cupom` (CSS) porque o cupom sem destaque não existe em `imagens-puras/`:
seria preciso desmarcar o produto, imprimir, remarcar. Bobina térmica em
monoespaçada é claramente desenho, então não engana — e o cupom real já apareceu
na capa, em tamanho grande.

**O mockup de computador sangra pela direita.** O recorte do modal tem 605 px
lógicos e é exibido a 1120 px (1,85×): o rótulo *Destaque na impressão* sai com
27 px na arte, legível no feed. O painel inteiro na mesma janela sairia a 0,8×.
O `.realce` foi posicionado por medida do arquivo (o interruptor verde está em
y 0,70–0,77), não no olho — as duas primeiras tentativas circularam a linha
*"Exibido nos aplicativos…"*, que é a de cima.

**O app do Entregador entrou como ilustração, com selo.** Na primeira versão esse
slide ficou fora, e o carrossel perdia a ponta mais convincente da novidade: o
item destacado chega até a rua. O emulador Android não sobe no Cloud Agent
(`MEMORIA-GERAL.md`, seção 6), então a tela é desenhada em `.tela-app`, mostrando
só o que a novidade afirma — item em evidência no pedido e confirmação na entrega
— com `.selo-ilustracao` no slide.

> **Pendente com o dono:** print real do app do Entregador na tela do pedido com
> item destacado e na confirmação de entrega. Quando chegar, substitui a
> ilustração do slide 6 e o selo sai.

**Sem rodapé no slide 4.** A janela em sangria cobre a base inteira do slide, e
os pontos desenhados por cima dela pareciam sujeira. O "4 de 8" do topo resolve.

## Capturas

```bash
# página pública e lista de produtos (sem clique)
python .cursor/skills/carrossel-novidades/scripts/capturar.py destaque-impressao \
    --url https://beefood.app/novidades --nome 01-pagina-novidades --publico
python .cursor/skills/carrossel-novidades/scripts/capturar.py destaque-impressao \
    --rota /cardapio --nome 02-cardapio-produtos

# telas que exigem clique
python carrosseis/destaque-impressao/capturar-telas.py
```

De `imagens-puras/`, os slides usam `03-modal-janela.png` e
`04-novidades-celular.png`. As outras ficam como **fonte**: o
`03-modal-produto.png` é de onde os recortes saem, o `03-modal-recorte.png` é a
faixa fechada do interruptor (sobrou depois que a janela em sangria passou a dar
conta da legibilidade) e as duas primeiras são contexto da rodada de captura.
Mesmo princípio dos manuais — a pura é backup, não é a arte.

Produto do exemplo: **Coca Cola 350ml** do setor **Bebidas** (BeeFood3 - Manual).
O sandbox tem dois produtos com esse nome — o script clica pelo cartão do setor,
não pelo nome solto.

## Render

```bash
python .cursor/skills/carrossel-novidades/scripts/renderizar.py \
    carrosseis/destaque-impressao --contato
```

## Legenda para publicar

> Cansou de bebida esquecida na sacola? 🥤
>
> Você sabe como essa história termina: o cliente liga com a sacola já aberta na
> mesa, alguém tem que sair de novo no meio do pico, e a nota cai sem ninguém
> descobrir onde foi que falhou.
>
> E não é falta de atenção. No cupom, toda linha tem o mesmo peso — a bebida
> simplesmente desaparece dentro do combo.
>
> Agora dá para avisar no papel. Abra o produto em **Cardápio → Produtos**, ligue
> o **Destaque na impressão** (ele fica ali, abaixo de Descrição) e aquela linha
> passa a sair com fundo preto e letra branca: no Cupom Pedido, na ficha da
> cozinha, no salão e no delivery. 🖨️
>
> Tem muita bebida? Filtre o setor e resolva o grupo todo pelo **Editar em Lote**.
>
> Seu entregador também vê: o item salta no pedido dele e, na hora de entregar,
> o app pergunta se aquilo foi junto. 🛵
>
> Um cuidado só — não saia marcando tudo. O destaque vive de contraste, então
> comece pelo que já ficou para trás alguma vez: bebida, molho, brinde e os
> pedidos de retirada, do tipo "sem maionese".
>
> O passo a passo está no manual **Destaque na impressão**, dentro do sistema.
>
> #beefood #restaurante #delivery #gestaoderestaurante #pdv
