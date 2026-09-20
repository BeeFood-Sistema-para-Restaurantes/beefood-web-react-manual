# Painel para Entregadores

- **Gênero:** novidade
- **Fonte:** [Painel para Entregadores](https://beefood.app/novidades/painel-para-entregadores)
- **Manual:** [Painel para Entregadores](https://ajuda.beefood.com.br/manual-painel-entregador)
  — na pasta, [`manuais/painel-entregador/`](../../manuais/painel-entregador/painel-entregador.md)
- **Formato:** 1080 × 1350 (4:5)
- **Slides:** 7

## O acervo, antes de escrever

As sete peças anteriores são de **cardápio, totem, tablet e dark kitchen**: o lado
do cliente pedindo. Nenhuma fala de **entrega**, e nenhuma tem uma captura de
Delivery, de KDS ou de cartão de pedido. Então não há prova para reusar — é a
primeira peça deste módulo.

Das capas, porém, há o que desencostar: sete entregues e **só uma diz o nome do
recurso**. As outras seis são pergunta ou cena, e a desta peça saiu cena também,
e voltou. Aqui o molde é o **anúncio de chegada**, que ainda não tinha sido
usado, e cabe porque o recurso é batizado — "Painel para Entregadores" é o nome
no release, no menu e no suporte.

O que se aproveitou do acervo foi **método**, não imagem:

- a injeção de dados na resposta da API, do carrossel do totem (cupons) e do
  tablet (frota), que aqui virou o `cena.json`;
- o recorte por caixa medida no DOM, do tablet, que aqui mede o último cartão
  para o clip não cortar a coluna pela metade.

## O fato, o ângulo, e o que o slide diz

O manual desta funcionalidade foi lido no código-fonte, então os fatos abaixo são
mais duros que o release.

| Fato (release / manual) | Ângulo | O que vira slide |
|---|---|---|
| O recurso se chama **Painel para Entregadores**, é o nome do release e do menu | Em novidade a capa anuncia: o nome no título, o que ele faz no subtítulo | Capa |
| "O entregador chega e pergunta para a cozinha se o pedido dele já saiu. A cozinha para o que está fazendo para responder." | A cena é do release e é boa: o custo não é o pedido, é a **interrupção** | 2 (abre o slide) |
| Colunas **Em preparo** e **Pronto**, número em fonte grande, legível de longe | Tela de parede é um gênero de tela: ela é lida **em pé, de longe** | 2 |
| Cada cartão traz origem (iFood, 99Food, Keeta, Cardápio Digital) e tempo decorrido | O entregador de marketplace procura o número **do app dele**, não o do caixa | 3 |
| Pedido fora do prazo ganha alerta, com o mesmo critério da tela de Delivery | O atraso aparece **sem ninguém conferir relógio** | 4 |
| Atualiza sozinha (WebSocket + `refetch` de 30 s) e é **somente leitura** | As duas coisas são a mesma promessa: **ninguém opera a tela** | 5 |
| Abre em janela separada, para arrastar até a TV; F11; tema claro ou escuro | O pedido de instalação é pequeno, e o tema resolve o lugar onde a TV está | 6 |
| Está em *Aplicativos → Entrega*, incluso no módulo Entrega, junto da Gestão de Entregas | Já está lá, sem contratar nada | 7 (CTA) |

**Ficou de fora, de propósito:** o detalhe do pedido (a janela mostra nome e
endereço do cliente, e este repositório é público); a busca por pedido/cliente; o
recorte de 6 horas; e o layout de duas colunas internas acima de 1500 px. São
fatos verdadeiros e nenhum deles é motivo para ligar o painel.

## Slide a slide

| # | Tipo | Ideia única | Imagem |
|---|---|---|---|
| 1 | Capa | Chegou o Painel para Entregadores, e ele mostra o que está em preparo e o que já ficou pronto | `painel-claro.png` numa TV de parede |
| 2 | Como funciona | Duas colunas e o número grande, para ler de longe e em pé | `colunas.png` |
| 3 | O cartão | O cartão diz de que canal veio e há quanto tempo está lá | `cartoes-origens.png` |
| 4 | Alerta | O que passou do prazo fica vermelho sozinho | `coluna-preparo.png` |
| 5 | Sem operação | O cartão muda de coluna sozinho, e nada na tela é clicável para mudar pedido | `andou-antes.png` + `andou-depois.png` |
| 6 | Onde ligar | Janela separada para arrastar até a TV, clara ou escura conforme o lugar | `tema-claro.png` + `tema-escuro.png` |
| 7 | CTA | Já está no módulo Entrega, e o manual tem o passo a passo | `novidades-celular.png` |

## Decisões de arte

### A cena das capturas é montada, e o `cena.json` diz o que foi montado

O painel de verdade da sandbox, capturado agora, mostra **sete cartões vermelhos**:
os pedidos foram criados há mais de duas horas e estão todos "Atrasado • 1h38min".
É a tela honesta de uma loja de teste parada — e é a pior peça de venda possível,
porque quem olha entende que o sistema atrasa tudo.

Então a captura intercepta a resposta de `venda2/delivery` e reescreve **duas
coisas**: a situação de um pedido de Cardápio Digital (de aguardando para em
preparo, porque o release cita esse canal) e os relógios de etapa. **Os pedidos
são reais** — inclusive as origens de iFood, 99Food e Keeta, que o dono estampou
no banco para o manual do #120. Nada é escrito no servidor, e `--cru` mostra a
tela como ela está.

Um atraso ficou de pé, no cartão mais antigo: o slide 4 precisa dele, e um painel
sem nenhum alerta não é um painel de turno real.

### O carimbo de hora é o de São Paulo, vestido de UTC

O servidor devolve `...Z`, mas o front lê com `parseLocalDateTime`, que **ignora o
sufixo**. Medido no navegador da captura: `2026-09-19T22:40:00.000Z` volta como
7 min atrás se lido como UTC e como 173 min **no futuro** se lido como local — e
tempo negativo o painel mostra como "há 0min". A primeira rodada de capturas saiu
com os sete cartões marcando zero minuto por causa disso.

E o alerta de atraso é **outra conta**: ele não olha a hora da etapa, olha a do
pedido. Sem reescrever `dataHoraPedido` junto, os cartões continuavam vermelhos
com tempos de etapa curtinhos — que é um estado que não existe.

Um resíduo ficou, de propósito: o `Atrasado • 14min` do slide 4 aparece como
`15min` no slide 2. O carimbo é recalculado a cada resposta, então o tempo de
etapa sai exato ("há 61min" em toda captura) e o atraso, que é uma subtração
com o prazo da loja, cai de um lado ou do outro do arredondamento conforme os
segundos. Travar o carimbo de uma vez consertaria o minuto e estragaria o
resto: ao longo da execução o relógio real anda, e os cartões passariam a
marcar 61, 63, 65. O que precisa concordar entre os slides é a **cena** —
mesmos pedidos, mesmas colunas, mesmos contadores —, e ela concorda.

### Menos pixels de largura, para caber mais texto

A TV do restaurante é larga, e acima de 1500 px cada etapa ganha **duas colunas
internas** — o painel real aproveita melhor a tela grande. Capturado assim, porém,
o cartão estreita e `2740 - Coleta 6118` sai cortado no meio da palavra, o que num
slide não lê como "tela larga", lê como bug. A captura é em 1280 × 720: coluna
única, número inteiro, e 16/9 exato para entrar na moldura de TV sem o
`object-fit: cover` comer uma faixa.

### A capa precisou de uma televisão, e o acervo só tinha monitor

O `.monitor` existe desde o dark kitchen, e o comentário dele avisa que o queixo
embaixo da tela é justamente **o que separa monitor de televisão de parede**. Este
produto é uma tela de parede: desenhá-lo com pescoço e pé colocava um monitor de
escritório na área de retirada.

Daí o `.monitor--parede`: some o pé, e a caixa passa a ter o que uma TV tem e uma
moldura de imagem não tem.

A **primeira versão voltou** — *"não é só uma imagem, precisa ter um mockup"* — e
ela era exatamente isto: um fio de moldura de 13 px em volta do print, sem massa,
sem volume e sem contexto. O que consertou foram quatro coisas, e nenhuma delas é
a espessura sozinha:

- **a borda de baixo é o dobro das outras três** (4,2% contra 2,2%). É a
  assimetria de qualquer televisão, e nenhuma moldura de imagem tem;
- **volume:** fio de luz no topo da moldura, sombra no pé, e cinza bem mais claro
  que o do monitor de mesa — em capa escura, moldura escura some no fundo;
- **o LED** no meio da faixa de baixo, e um reflexo diagonal fraco sobre o vidro,
  que é o que diz "aqui tem vidro" sem lavar o print;
- **a luz na parede:** uma `.luz` branca e quente atrás do aparelho. É a camada
  que faz mais diferença — sem ela a TV flutua no preto; com ela há uma parede
  atrás, e a tela está claramente acesa.

E a tela que entra na moldura é a **clara**, não a escura, apesar de a capa ser
escura: tela acesa e branca sobre fundo escuro é o que lê como televisão ligada.
A escura fica no slide 6, onde ela tem função — mostrar que o tema acompanha a luz
do lugar.

### O slide 5 mostra o mesmo pedido duas vezes

Dois cartões diferentes lado a lado provariam que existem duas colunas, que é o
slide 2. O que prova "anda sozinho" é o **mesmo** `#1133 · 2740 - Coleta 6118`
fotografado duas vezes, "Em preparo há 4min" e depois "Pronto há 1min" — mesma
moldura, mesmo número, fundo creme virando verde. A captura roda a cena duas
vezes para conseguir o par.
