# Dark kitchen: várias marcas num painel só

- **Gênero:** função do sistema (a primeira peça deste gênero, ver
  `MEMORIA-CARROSSEIS.md`, seção *o segundo gênero*)
- **Pauta:** [`beefood.com.br/sistema-dark-kitchen`](https://beefood.com.br/sistema-dark-kitchen/)
  — lida com `pauta.py --pagina`
- **Manuais lidos:** nenhum cobre multicardápio (é o buraco que o
  `CHECKLIST-MANUAIS.md` registra como **Multilojas**, prioridade 3).
  Emprestam vocabulário: [`vinculo-marketplace`](../../manuais/vinculo-marketplace/vinculo-marketplace.md),
  [`ficha-tecnica`](../../manuais/ficha-tecnica/ficha-tecnica.md) e
  [`formas-recebimento`](../../manuais/formas-recebimento/formas-recebimento.md)
- **Formato:** 4:5 (1080×1350), 7 slides
- **Imagens:** 6 telas **desenhadas** (`telas/*.html` → `desenhar-telas.py`).
  Nenhuma captura: o sandbox é uma loja só, e o assunto da peça é uma operação
  com três marcas

## Por que esta peça é desenhada, e o que isso obriga

O sandbox (BeeFood3) tem um cardápio. A peça fala de três. Sem o terceiro degrau
da ancoragem — **manual > tela capturada > tela desenhada** — sobrariam dois
caminhos, e os dois são piores: recortar a ilustração da página de vendas (que é
marketing, e a regra do manual vale igual para o site: referência, não acervo) ou
não fazer a peça.

Desenhar obriga a três coisas, e elas estão cumpridas aqui:

| Obrigação | Como esta peça cumpre |
|---|---|
| rótulo é o do sistema | `Aguardando`, `Preparo`, `Pronto/Entrega`, `Entregue` (painel de Delivery); `Por Cardápio`, `Valor Total de Vendas`, `Ticket Médio` (painel inicial); `Em Espera`, `Em Preparo`, `Colunas`, `Setores` (KDS). Lidos do print real que a página usa e das capturas dos manuais |
| número é exemplo, e é um jogo só | R$ 38.740,00 em 719 pedidos, repartidos entre as três marcas. As somas fecham (19.420 + 12.860 + 6.460 = 38.740; 38.740 ÷ 719 = 53,88) porque painel com soma errada derruba a peça inteira. O `R$ 298.921,66` da arte do site ficou fora: na nossa arte, número daquele tamanho vira promessa de resultado |
| o exemplo não estreia nada | as marcas (Hamburgueria, Pizzaria, Marmitaria) são as da própria arte do site; os produtos (One Burger, Batata Frita Grande, Coca-Cola 350ml) são os do sandbox dos manuais; o endereço é o do sandbox |

## O fato, inteiro

A página vende um segmento, e o que sustenta a peça são as **afirmações
funcionais** dela — a empresa descrevendo o próprio produto. Separadas do claim
institucional, que não entra na arte (`+100 mil negócios impactados`, `melhor
avaliação no Google`, `melhor suporte do Brasil`):

1. **uma operação, várias marcas.** Cada marca tem cardápio, canais de venda e
   relatórios próprios; a estrutura física e o sistema são um só. Sem outro
   login, sem outro sistema.
2. **os pedidos chegam num painel.** Marketplaces (iFood, 99Food, Keeta,
   Aiqfome, Rappi, Delivery Much, UaiRango), cardápio próprio e WhatsApp.
3. **filtro de marca.** Liga para ver uma; desliga para ver a operação inteira.
4. **o mesmo produto em vários cardápios**, com preço, promoção e
   disponibilidade próprios em cada um.
5. **a cozinha recebe organizada** por marca e por setor, no Monitor KDS.
6. **o estoque pode ser compartilhado** entre as marcas, com baixa pela ficha
   técnica.
7. **resultado por marca e consolidado**, do faturamento ao ticket médio.
8. **link multilojas:** todas as marcas numa página, e o cliente escolhe.

Fora da peça: fiscal por marca e logística ficaram de fora por espaço — sete
slides é o que o assunto pede, e os dois exigiriam tela própria para provar.

## O ângulo, e de onde ele sai

O ângulo é o **custo de operar marca por marca**, e ele sai do que a própria
página afirma do produto, não de cena inventada sobre a rotina de ninguém:
"gerenciar várias marcas sem abrir outro sistema, sem fazer novo login, sem
perder tempo alternando entre telas".

Nenhum slide afirma que o leitor tem três marcas, que ele perde pedido ou que ele
usa planilha. Todos afirmam o que o sistema faz — é o teste *quem poderia
desmentir isto?* aplicado slide por slide.

## Fato → ângulo → o que o slide diz

| Fato (da página, funcional) | Ângulo | O que o slide diz |
|---|---|---|
| cada marca com cardápio, canais e relatórios próprios, numa operação centralizada | o nome do recurso é o próprio arranjo: várias marcas, um painel | capa: "Várias marcas num painel **só**" |
| sem abrir outro sistema, sem novo login | o que é por marca e o que é compartilhado | slide 2: "Cada marca tem o seu **cardápio**" |
| pedidos de marketplaces, cardápio próprio e WhatsApp num painel; filtro por marca | a tela é a prova, e ela mostra canal e marca em cada pedido | slide 3: "Os pedidos chegam todos na mesma **tela**" |
| o mesmo produto em vários cardápios, com preço e disponibilidade próprios | cadastrar uma vez e escolher onde aparece | slide 4: "Um produto, um preço por **marca**" |
| organização automática por marca e por setor no KDS | a cozinha é uma; o pedido precisa dizer de qual marca é | slide 5: "A cozinha vê de qual marca é o **pedido**" |
| link multilojas reunindo os cardápios numa página | do lado do cliente, três marcas viram um endereço | slide 6: "Todas as marcas num link **só**" |
| a operação inteira num sistema (KDS, estoque, financeiro, fiscal) | o pedido para quem está escolhendo sistema | slide 7: "Coloque as suas marcas num painel **só**" |

## Os slides

| # | Arquivo | Ideia única | Imagem |
|---|---------|-------------|--------|
| 1 | `01-capa.html` | várias marcas, um painel — e o nome das três na mesma tela | `vendas-por-cardapio` em recorte, sem moldura |
| 2 | `02-como-funciona.html` | o que é por marca, o que é compartilhado | — (o slide 3 é a prova) |
| 3 | `03-pedidos.html` | canais diferentes, marcas diferentes, uma tela | `pedidos-tres-marcas` em janela de navegador |
| 4 | `04-produto.html` | um cadastro, preço por cardápio | `produto-em-cardapios` em recorte |
| 5 | `05-cozinha.html` | o KDS diz a marca e o setor de cada pedido | `kds-marcas` em tablet |
| 6 | `06-link.html` | o cliente escolhe a marca num link só | `link-multilojas` em celular, sangrando pela base |
| 7 | `07-cta.html` | o pedido, com o endereço da página | `painel-inicio` em notebook |

A capa **nomeia** o recurso, o slide 2 **explica** e o slide 3 **mostra** — a
ordem é regra da skill, e vale nos dois gêneros. A diferença do gênero está na
pílula (`Dark Kitchen`, não `Novidade`), no vocabulário (nenhum "agora", nenhum
"acabou de sair": multicardápio não é novidade) e no CTA, que aponta a página do
site porque quem lê pode não ter painel nenhum.

## Decisões de arte

**A capa não leva mockup.** A tela da capa é um recorte do painel, sem moldura de
aparelho, porque o que ela tem de provar são **os três nomes de marca no mesmo
cartão** — e nome de marca dentro de notebook em 620 px de largura não se lê. O
notebook (mockup novo no acervo) foi para o slide 7, onde a tela é atmosfera e
não prova.

**Um mockup por slide, e nenhum repetido:** recorte (1), navegador (3), recorte
(4), tablet (5), celular sangrando (6), notebook (7). O tablet no KDS não é
enfeite: é onde o monitor de cozinha fica.

**Três cores, sempre as mesmas:** Hamburgueria em vermelho, Pizzaria em azul,
Marmitaria em verde. Elas repetem nos pontinhos do painel, nas etiquetas do
pedido, nos chips do cardápio e na legenda do gráfico. Cor trocada no meio da
peça faz o leitor procurar uma quarta marca.

**Emoji:** só nos chips das marcas dentro das telas desenhadas (🍔 🍕 🍱), porque
o cardápio real tem foto ali e o desenho precisa de algo no lugar. Nos títulos
dos slides, nenhum.
