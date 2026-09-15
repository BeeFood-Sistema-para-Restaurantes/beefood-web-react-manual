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
| Campo novo **Destaque na impressão** no cadastro de produto e de complemento | toda loja já tem uma gambiarra caseira para não esquecer a bebida | "Toda loja tem uma gambiarra para não esquecer a bebida" | 1 |
| A linha do item marcado sai com fundo escuro e letra clara | no cupom todas as linhas têm o mesmo peso, e a bebida some dentro do combo | "Um esquecido custa duas viagens" + o custo em cena (cliente liga, alguém sai de novo, a nota cai) | 2 |
| Efeito no **Cupom Pedido** e na ficha da cozinha, no presencial e no delivery | é marca-texto impresso | "A linha que importa para de se esconder" | 3 |
| O campo fica logo abaixo de **Descrição**, em produto e em complemento | é um interruptor, não um projeto | "É um interruptor no cadastro do item" | 4 |
| **Editar em Lote** com o setor filtrado marca vários itens | quem tem cardápio grande não vai abrir item por item | "Marque a geladeira inteira de uma vez" | 5 |
| No app do Entregador o item aparece em evidência e a entrega pede confirmação | o cuidado não para no balcão | "O entregador confirma antes de ir embora" | 6 |
| Usar com critério: marcar tudo anula o efeito | destaque funciona por contraste | "Se tudo é destaque, nada é" | 7 |
| A novidade tem manual publicado no mesmo dia | — | "Todo recurso novo vira manual no mesmo dia" | 8 |

Números: nenhum. A novidade não traz métrica, e o custo do item esquecido está
descrito em cena ("alguém sai de novo, no meio do pico") justamente para não
inventar percentual.

## Slides

| # | Arquivo | Tipo | Ideia única | Imagem |
|---|---------|------|-------------|--------|
| 1 | `01-capa.html` | capa com imagem | Toda loja tem uma gambiarra para não esquecer a bebida | cupom real em sangria, inclinado — `manuais/destaque-impressao/imagens-puras/05-cupom-pedido.png` |
| 2 | `02-custo.html` | texto | Um item esquecido custa uma segunda viagem | — |
| 3 | `03-no-papel.html` | antes × depois | O contraste é o que faz a linha ser vista | cupom desenhado em CSS (o "antes" não existe como captura) |
| 4 | `04-onde-ligar.html` | mockup de computador | Um interruptor abaixo de Descrição | `imagens-puras/03-modal-janela.png` em `.sangria--janela`, com `.realce` no campo |
| 5 | `05-em-lote.html` | passos | Editar em Lote marca o setor inteiro | — |
| 6 | `06-na-rua.html` | mockup de celular (ilustração) | O app do entregador pede confirmação | tela desenhada em `.tela-app`, com `.selo-ilustracao` |
| 7 | `07-limite.html` | texto | Marcar tudo anula o efeito | — |
| 8 | `08-cta.html` | mockup de celular + CTA | A novidade já tem manual | `imagens-puras/04-novidades-celular.png` em sangria |

Cinco dos oito slides têm imagem, e a capa é um deles.

## Decisões de roteiro

**A capa mostra o resultado, não um ícone.** O cupom real do manual #99 entra em
sangria pela base, com a inclinação de −3° que faz o papel parecer objeto na
bancada. As duas barras preta sobre branco são o contraste que para o dedo — é a
própria novidade funcionando, sem precisar de legenda.

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

> Toda loja tem uma gambiarra para não esquecer a bebida: canetinha vermelha na
> lata, durex colorido na comanda, grito na cozinha.
>
> O problema nunca foi falta de atenção. É que no cupom todas as linhas têm o
> mesmo peso — e a bebida é justo a que some no meio do combo. Aí o pedido volta,
> alguém sai de novo no meio do pico e a nota cai sem ninguém saber onde falhou.
>
> Agora o papel avisa sozinho. Ligue **Destaque na impressão** no cadastro do
> item, logo abaixo de Descrição, e aquela linha passa a sair com fundo escuro e
> letra clara no Cupom Pedido e na ficha da cozinha, no salão e no delivery. Para
> a geladeira inteira de uma vez, filtre o setor e use o **Editar em Lote**.
>
> Um cuidado só: o recurso trabalha por contraste. Marque o que já ficou para
> trás alguma vez — bebida, molho, brinde, "sem maionese". Se tudo é destaque,
> nada é.
>
> Passo a passo completo no manual **Destaque na impressão**, dentro do sistema.
>
> #beefood #restaurante #delivery #gestaoderestaurante #pdv
