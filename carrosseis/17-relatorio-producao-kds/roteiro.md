# Carrossel 17 — Relatório de Produção (KDS)

- **Novidade:** [Relatório de Produção (KDS)](https://beefood.app/novidades/relatorio-producao-kds), 27/10/2026
- **Área:** KDS · item de menu **Desempenho → Produção (KDS)**
- **Gênero:** novidade (quem lê já é cliente e já tem KDS na cozinha)
- **Manual:** não existe. `ls manuais/ | grep -iE "kds|producao|cozinha|desempenho"`
  volta vazio, e as três pastas mais próximas que o `pauta.py` sugeriu
  (`relatorio-comissao-garcom`, `relatorio-operacao-entrega`,
  `relatorio-taxa-servico`) são de outros relatórios. **O fato veio da tela**,
  que é o que a `SKILL.md` manda quando não há manual.
- **Formato:** 4:5, 7 slides

## A conta que esta peça teve de fazer antes de tudo: capturar ou desenhar

O dono mandou a conta de uma loja de **produção** para ver as telas. Elas estão
cheias: 5.074 itens em trinta dias, mapa de calor pintado, ranking de pratos
inteiro. É a tentação de fotografar tudo e acabar em uma hora. Três coisas
derrubaram a captura, e vale deixar as três escritas porque a próxima peça de
relatório vai cair na mesma encruzilhada.

**1. O relatório é de um cliente, e ele tem nome.** O que aparece na tela não é
"dado de exemplo com cara de real": é a cozinha de um restaurante que existe,
com o cardápio dele (`ONE BURGER (COMBO)`, `Combo Casal Match Perfeito`,
`COMBO FANTA HALLOWEEN`), o volume dele e a hora em que ele trava. O chip com o
nome da loja fica na moldura do painel e sai no recorte; o cardápio, não — ele
está **dentro** do relatório, e é o que identifica a marca. Este repositório é
público e a peça vai para o Instagram. Cobrir o nome não resolveria: a lista de
pratos é a assinatura.

**2. A loja que a gente pode publicar está zerada.** A sandbox é a única cozinha
cujo dado é nosso, e ali a Produção (KDS) devolve `0 itens produzidos`,
`Cobertura —` e *"não é possível dividir o tempo entre espera e preparo"*. É,
palavra por palavra, o caso que a memória já tinha: **relatório sem volume se
desenha inteiro**.

**3. Nem a loja de produção exercita o relatório inteiro.** Ela marca *pronto*
sem marcar *iniciado* em 4.637 dos 4.670 itens medidos, então as colunas
**Espera** e **Preparo** saem com traço na tela toda; nenhum produto dela tem
estação de produção vinculada, então a visão por estação vem vazia; e o
retrabalho do período é zero. Uma peça feita daquelas capturas venderia um
relatório que responde "não medido" — e o que ele faz de melhor é justamente
medir.

E tem a trava que fecha a decisão: **um jogo de números por carrossel**. Se um
slide fosse desenhado (porque a coluna está vazia) e outro capturado, a peça
publicaria duas leituras diferentes da mesma cozinha. Ou tudo captura, ou tudo
desenho.

**Ficou desenho**, com as telas de produção servindo de planta: estrutura,
ordem das seções, rótulo por rótulo, paleta e comportamento. Nenhum pixel delas
entra na arte.

## O que veio de cada fonte

| Fonte | O que ela deu |
|---|---|
| release de 27/10 | o nome do recurso, o caminho de menu, as sete abas e o que cada uma mostra, mais os *Detalhes em janela* |
| as telas de produção | a **estrutura**: nome e ordem das seções, rótulo de cada coluna, o que a tela escreve quando falta dado, o desenho da janela de detalhe e da linha do tempo |
| a sandbox | a prova de que não havia o que capturar |
| acervo | a #10, que já tinha desenhado dois relatórios inteiros, e de onde saiu a forma do `telas/*.html` |

**Rótulos que a arte copia da tela, porque rótulo inventado é produto
inventado:** *Tempo total médio*, *Espera média*, *Preparo médio*, *Itens
produzidos*, *Retrabalho*, *Cobertura*, *Onde o tempo é investido*,
*Curva do dia*, *Mapa de calor dia da semana × hora*, *vs loja*,
*Agendado × imediato*, *Pontualidade do agendado*, *Linha do tempo*, *Etapas*,
*Os mais lentos*, *lançamento → preparo*, *preparo → pronto*, *Lançado*,
*Preparo*, *Pronto*, *Entregue*.

**O texto de ajuda do mapa de calor saiu palavra por palavra, inclusive o
tropeço.** A tela escreve *"é aqui que decisão de escala se apoia"*, sem o
artigo, e o slide 4 escreve igual. Não é erro de digitação nosso: é o texto que
está no ar, e consertá-lo na arte faria a imagem divergir da tela que o leitor
vai abrir. Se o produto arrumar a frase, a arte acompanha.

## Nome de venda × nome do release

O release se chama **Relatório de Produção (KDS)** e o item de menu é
**Produção (KDS)**. Os dois são o mesmo, e aqui não há divergência a resolver
como houve na #11: quem compra procura no menu pela palavra *Produção*, debaixo
de *Desempenho*. A capa leva **relatório de Produção do KDS** — "KDS" fica
porque é o aparelho que o leitor tem na cozinha e é ele que situa de que
produção se fala.

## Fato → ângulo → o que o slide diz

| # | Fato (da tela e do release) | Ângulo | O que o slide diz |
|---|---|---|---|
| 1 | Entrou em *Desempenho → Produção (KDS)* um relatório de tempo de cozinha, com sete visões | A cozinha é a única parte da casa que ninguém cronometra: o dono sabe quanto vendeu e quanto gastou, e não sabe quanto demorou | Chegou o relatório de **Produção** do KDS |
| 2 | Cada item carrega três marcos — lançado, preparo iniciado e pronto —, e o relatório parte o tempo em espera e preparo | "Demorou" é uma palavra só para duas coisas diferentes: prato parado na fila e prato sendo feito. O conserto de cada uma é outro | A espera na fila e o preparo vêm separados |
| 3 | A aba *Itens* ordena os pratos por tempo e traz a coluna *vs loja*, a diferença para a média da casa | O dono já desconfia de um prato; o que falta é o nome dele e o tamanho da diferença | **Itens**: quanto cada prato passa da média da sua loja |
| 4 | A aba *Tempo* tem mapa de calor dia da semana × hora, quebra por dia da semana e evolução diária | Escala de cozinha se monta no palpite de quem está lá dentro | **Tempo**: o dia e a hora em que a cozinha aperta |
| 5 | A aba *Canal* separa agendado de imediato e mede a pontualidade do agendado contra a hora prometida | Pedido marcado para as 20h fica pronto às 20h, e isso entra na média como se fosse demora | **Canal**: o agendado não pesa na média de quem pediu agora |
| 6 | Clicar em cartão, linha ou barra abre uma janela com o recorte, os mais lentos e a linha do tempo em mm:ss, levando os filtros do topo | Média é afirmação sobre o negócio de alguém, e quem recebe uma afirmação quer conferir | **Detalhes em janela**: cada pedido que entrou na conta |
| 7 | Está no ar em *Desempenho → Produção (KDS)*, com exportação em Excel | — | Abra a Produção do KDS hoje |

## Slide a slide

| Arquivo | Tipo | Ideia única | Imagem |
|---|---|---|---|
| `01-capa.html` | capa | chegou o relatório de produção da cozinha | `telas/resumo.html` dentro de um `.notebook` em sangria |
| `02-duas-metades.html` | explicação | o tempo se parte em fila e preparo | `telas/linha-do-tempo.html`, a janela de um item |
| `03-itens.html` | prova | o prato que está acima da média | `telas/itens.html`, o ranking com *vs loja* |
| `04-mapa-de-calor.html` | prova | em que dia e hora a fila cresce | `telas/mapa-de-calor.html` |
| `05-agendado.html` | prova | agendado e imediato contados à parte | `telas/agendado.html`, os dois blocos |
| `06-janela.html` | prova | a média abre e mostra os pedidos | `telas/janela.html`, a janela com *Os mais lentos* |
| `07-cta.html` | CTA | abra hoje | a arte da capa, no mesmo lugar e tamanho |

## A copy, depois de três revisões

O dono pediu revisão com subagente **antes** de montar slide, e o pedido tem
razão de ser: texto escrito junto com a arte fica refém da arte, e aí o que
entra na página é a frase que coube, não a frase certa. Foram três passagens —
naturalidade, auditoria contra as regras da skill, e leitura em voz alta.

O que elas mudaram, e por quê:

1. **Saiu todo número de exemplo da copy.** Caíram os "20 minutos" do título 2,
   a "sexta às 20h e quarta às 20h" do corpo 4 e os "últimos 30 dias" do CTA.
   Número de exemplo vive na arte, onde a legenda avisa o que ele é; escrito na
   copy ele vira promessa de resultado nosso.
2. **Saiu a metáfora.** O corpo 2 dizia "prato na chapa" onde a tela escreve
   **Preparo** — e metade das cozinhas que vão ler isto não têm chapa.
3. **Gente voltou a ser sujeito** nos corpos 3, 5 e 6, no lugar da interface.
4. **"Ao cliente" virou "quem pediu".** Quem lê é o dono da loja: para ele, do
   outro lado do pedido tem uma pessoa, não uma categoria.
5. **O subtítulo da capa ganhou verbo principal** e um paralelismo que fechou:
   *"entre cair no KDS e ficar pronto"*.
6. **O título 4 virou o nome da aba.** Era "Mapa de calor:", que é o nome do
   gráfico; virou "Tempo:", que é a palavra que o leitor vai achar no
   relatório. O mapa de calor continua sendo a imagem do slide.
7. **"Média da casa" e "média da sua loja" viraram uma coisa só** — a da tela,
   que escreve `vs loja`.
8. **Os chapéus 2 e 6 deixaram de ter a mesma fôrma.**
9. **O corpo 2 passou a dizer "São sete abas"**, porque sem isso os slides 3, 4
   e 5 chegam como três telas soltas em vez de três cortes do mesmo relatório.

Onde as revisões brigaram, ganhou a casa: a primeira pediu para abandonar o
molde *"Nome: o que ele te dá"* em quatro títulos seguidos, por monotonia. Esse
molde é regra daqui, veio de correção do dono, e fica. A monotonia foi resolvida
onde dava — diferenciando os chapéus — e não desmontando o molde.

### Texto final

| # | Chapéu / pílula | Título | Corpo |
|---|---|---|---|
| 1 | `Novidade` | Chegou o relatório de **Produção** do KDS | *(subtítulo)* Você vê quanto tempo cada prato levou entre cair no KDS e ficar pronto. |
| 2 | `SETE ABAS, UM TEMPO SÓ` | A espera na fila e o preparo **vêm separados** | Cada item carrega três horários do KDS: lançado, preparo e pronto. O tempo total vale para todos; a divisão entre espera e preparo, para os que a cozinha marcou ao começar. |
| 3 | `O PRATO QUE SEGURA A FILA` | **Itens**: quanto cada prato passa da média da sua loja | Os pratos saem do mais demorado ao mais rápido. O que segura a fila sai dali com nome e com o tamanho da diferença. |
| 4 | `QUANDO A FILA CRESCE` | **Tempo**: o dia e a hora em que a cozinha aperta | No mapa de calor o dia da semana cruza com a hora, e cada cruzamento traz o tempo médio dali. O aperto da sua cozinha ganha dia e hora, e é com eles que você monta a escala da semana seguinte. |
| 5 | `AGENDADO NÃO É ATRASO` | **Canal**: o agendado não pesa na média de quem pediu agora | O agendado fica parado de propósito até perto da hora marcada, e essa espera não entra na média do pedido imediato. Ao lado, você vê quantos agendados ficaram prontos antes da hora combinada. |
| 6 | `ATRÁS DO NÚMERO` | **Detalhes em janela**: cada pedido que entrou na conta | Clique no cartão, na linha ou na barra e veja os pedidos que formaram aquele número, um a um, com a espera e o preparo de cada um. A janela leva junto os filtros do topo. |
| 7 | `Já está no ar` · `Desempenho → Produção (KDS)` | Abra a **Produção do KDS** hoje | *(subtítulo)* Comece pelo Resumo e escolha o período no topo. A lista inteira sai em Excel. Tudo que entra de novo está em **beefood.app/novidades**. |

### A quarta correção, que veio da arte e não de subagente

Os corpos dos slides 2, 3 e 6 encolheram depois da primeira renderização: o
texto encostava na imagem, e quem cede é o texto. É a mesma aritmética que a
#16 escreveu no slide 5 — a página tem por volta de 600 px para imagem, e o que
não serve à afirmação só diminui o que serve. O "São sete abas" do fim do corpo
2 não foi cortado: subiu para o chapéu, onde custa zero.

E uma mudança que não é de altura, é de verdade. O corpo 2 dizia *"todo item
que passa pelo KDS marca três horários"*, e isso não é verdade em cozinha
nenhuma: o marco do meio só existe se a equipe tocar em **iniciar** no monitor.
A loja de produção que serviu de planta marcou pronto sem marcar iniciado em
4.637 dos 4.670 itens medidos, e o relatório inteiro dela sai com traço nas
colunas Espera e Preparo. Quem abrisse o relatório depois de ler a promessa
encontraria traço. A frase que ficou é a da própria tela — *"O tempo total vale
para todos; a divisão entre espera e preparo vale para 33"* — e ela não
enfraquece a venda: diz ao dono o único gesto que dobra o relatório dele.

## A capa

**Molde: anúncio de chegada.** Placar antes desta peça — afirmação do fato 6,
anúncio de chegada 3, nome + dois-pontos 2, pergunta 2, nome + canal 1,
nome + para quem 1, ordem direta 1, antes × agora 0.

A condição do molde é a que está escrita desde a #8: ele pede **recurso
batizado, com nome próprio que vira item de menu**, e pede que o que chegou
seja uma coisa inteira, não uma capacidade que mudou. Aqui as duas fecham —
nasceu uma linha nova no menu do Desempenho, com sete abas dentro.

Os concorrentes caíram assim:

- **afirmação do fato** é a forma da #16, que é a capa imediatamente anterior.
  A regra do quarto vício é sobre o perfil, não sobre a peça: duas capas
  seguidas no mesmo molde leem como fórmula;
- **antes × agora** continua zerado e continuou. O "antes" daqui seria *"você
  sabia quanto vendeu, não quanto demorou"*, e "quanto vendeu" é o relatório de
  Vendas, que a casa vende e continua vendendo. É exatamente a armadilha que
  derrubou o molde na #12: **nunca ponha um produto do catálogo no lado
  perdedor**;
- **ordem direta** precisa de um objeto só, e este relatório tem sete abas;
- **nome + dois-pontos** foi a forma da #14 e, mais do que isso, é a forma dos
  títulos de dentro desta peça. Repetida na capa, ela apagaria a diferença
  entre a capa e o miolo.

O vermelho caiu em **Produção**, uma palavra — e aqui ele cumpre a função da #8
à #10: é a palavra que o leitor vai procurar no menu depois.

## O jogo de números

Um só na peça inteira, e as somas fecham. A loja do exemplo é uma
hamburgueria de trinta dias:

```
espera 9,8 min + preparo 4,4 min            = 14,2 min de tempo total
9,8 / 14,2 = 69%   e   4,4 / 14,2 = 31%     → a barra "onde o tempo é investido"
2.490 itens produzidos / 30 dias            = 83 por dia
2.490 medidos de 2.700 itens                = 92% de cobertura, 210 sem marco
38 itens de retrabalho / 2.490              = 1,5% do produzido
1.620 imediatos + 870 agendados             = 2.490
(1.620x12,4 + 870x17,6) / 2.490             = 14,2 min, o total do cabeçalho
(1.620x7,9  + 870x13,3) / 2.490             =  9,8 min, a espera do cabeçalho
imediato  7,9 + 4,5 = 12,4   agendado 13,3 + 4,3 = 17,6
870 / 2.490                                 = 34,9% de agendados
701 + 44 + 67                               = 812 agendados já prontos
701/812 = 86,3%   44/812 = 5,4%   67/812 = 8,3%   → soma 100%
398 + 1.394 + 548 + 124 + 26                = 2.490 na distribuição dos tempos
cada linha do ranking: espera + preparo     = total, e total - 14,2 = "vs loja"
a linha do tempo do slide 2: 12:35 + 11:11  = 23:46, e os relógios batem
38 itens de retrabalho x 4,4 min de preparo = 167 min perdidos
as 13 barras da Curva do dia somam                   2.490
e a média delas, pesada pelas barras,       = 14,2 min, o total do cabeçalho
```

A **copy não repete nenhum destes números**. Eles são estrutura: quanto a
cozinha de cada loja demora é leitura dela, e escrito na copy o exemplo vira
promessa de resultado nosso. A legenda avisa uma vez que o dado é de exemplo, e
a arte não leva carimbo.

## Decisões de arte

- **Sem data de carimbo na arte, mas com a data que é dado.** A regra da casa
  tem uma exceção escrita só para print de verdade, e tela desenhada não é
  print — então o seletor de período diz *Últimos 30 dias*, sem as datas que a
  tela de verdade imprime ao lado, e o cabeçalho da janela diz a mesma coisa.
  Já os relógios da linha do tempo e a coluna *Lançado* de *Os mais lentos*
  ficam: ali a data **é a medição**, e sem ela o slide 2 não tem o que provar.
  A separação que ficou valendo é essa — data que carimba quando a peça foi
  feita sai; data que é o dado medido fica, e sem o ano, que é a parte que
  envelhece à vista.
- **A medida do desenho sai do mockup.** `1440x900` é 16/10, a proporção exata
  do `.notebook__tela`; fora dela o `object-fit: cover` come uma faixa do
  relatório. As telas que entram como `.recorte` nascem na largura em que vão
  aparecer.
- **O mapa de calor sai recortado nas horas de serviço (16h às 23h).** A tela
  de verdade pinta as 24, e as oito colunas de madrugada ficariam cinzas no
  slide — e cada coluna a mais rouba largura da célula, que é onde mora o
  número que o título promete. O recorte acaba onde a afirmação do slide acaba.
- **Nenhum chip de loja, nenhum nome de marca.** A tela desenhada identifica o
  recorte como a tela de verdade faz, com `Loja 142` e o período.
- **Os pratos do exemplo são genéricos de hamburgueria** — *Burger Duplo
  Cheddar*, *Onion Rings*, *Combo da Família*. Nenhum deles é do cardápio da
  loja que serviu de planta.

## O que ficou de fora, e por quê

- **A aba Retrabalho não virou slide.** Ela é uma das sete, e a ideia é boa
  (o prato que voltou para a chapa custa duas vezes). Perdeu para os *Detalhes
  em janela* porque a peça inteira se apoia em **confiar no número**, e a janela
  é o que torna o número conferível. O retrabalho continua na peça: ele é um dos
  seis cartões do Resumo, que está na capa, e a legenda o nomeia.
- **A aba Setor também não.** A tela separa *setor do cardápio* de *estação do
  KDS* e explica por que os dois não fecham entre si — é uma distinção
  excelente e é distinção de quem já abriu o relatório, não de quem está
  decidindo se abre.
- **A aba Dados virou meia linha no CTA.** Lista completa com paginação e
  Excel é entrega, não argumento.
- **Oito slides.** O corte foi por aritmética de leitura: quem rola o feed para
  no quinto, e oito slides empurrariam a janela de detalhe para a sétima
  posição.

## O sandbox e a conta de produção

Nada foi alterado em lugar nenhum: as duas contas foram só lidas. A conta de
produção **não** está neste repositório — ela vive em variável de ambiente, e o
estado de sessão dela ficou em `/tmp`, fora da árvore do git. Nenhum print dela
entrou em `imagens-puras/`.
