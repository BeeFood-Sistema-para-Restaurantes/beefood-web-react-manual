# MCP: a sua IA trabalhando dentro do BeeFood

- **Gênero:** novidade
- **Fonte:** [MCP: converse com o seu restaurante usando IA 🤖](https://beefood.app/novidades/mcp-inteligencia-artificial)
  — 13/10/2026, áreas Aplicativos e Sistema, aplicativo BeeFood App. Mais a
  **documentação do servidor**, que é onde está a metade que o release não
  conta (ver *O que a documentação mudou na peça*).
- **Manual:** não existe em `manuais/`. Os passo a passo publicados são os da
  própria folha de *Aplicativos → MCP* (Manual do MCP, Como conectar ao ChatGPT,
  Como conectar ao Claude), e eles são **conteúdo de configuração** — a peça os
  cita no CTA e não copia nada deles.
- **Nome de venda × nome do release:** o release batiza **MCP: converse com o
  seu restaurante usando IA**; o menu e o cartão da grade escrevem **MCP**, e é
  por *MCP* que o leitor vai procurar. A peça vende **MCP**, e a parte "converse
  com o seu restaurante" não virou nome: virou o título do slide 2, que é onde
  ela explica em vez de batizar.
- **Formato:** 1080 × 1350 (4:5)
- **Slides:** 6

## O que a documentação mudou na peça

Esta peça foi entregue uma vez e **devolvida inteira**. O pedido de refação tem
quatro linhas, e três delas dizem a mesma coisa:

> - slide 1 → deve ser o mesmo layout de aplicativos → mcp
> - slide 1 → anunciar lançamento "MCP da BeeFood chegou", "Conecte sua IA
>   preferida no BeeFood"
> - refaça dos outros layouts. estude a documentação, veja o que ele faz →
>   edita cardapio, traz relatorios, e muito mais
> - de forma geral nenhum slide ficou bom

A primeira versão vendia um recurso que **responde pergunta**. Capa com o
faturamento, slide 3 com o faturamento conferido, slide 4 com os canais de
venda, slide 5 com a contagem do cardápio: quatro telas escuras de conversa,
quatro respostas de consulta, e o leitor passando por elas sem ver nada novo
depois da segunda.

A documentação do servidor diz outra coisa. O `listar_endpoints` devolve **61
operações, e 29 delas alteram dado** — 24 só no catálogo. A descrição que o
próprio `execute_beefood_request` publica é de uma ferramenta que escreve:

> *Writes (POST, PUT, PATCH, DELETE) are not idempotent: describe the change
> and get explicit confirmation first; never retry a failed write
> automatically. A 403 means a missing scope.*

E a tela de autorização tem **duas colunas**, LEITURA e **ESCRITA**, com as
doze caixas das seis áreas já marcadas. Vender só a leitura era vender menos da
metade do que foi entregue.

A peça refeita tem duas provas, uma por direção: um número que fecha com o
painel (slide 3) e um produto que a IA criou, fotografado no painel (slide 4).

## O acervo, antes de escrever

Doze peças entregues, e **nenhuma** toca este assunto. Não há, em
`carrosseis/*/imagens-puras/`, uma só tela de integração, de API ou de
ferramenta externa: as doze anteriores vendem módulo de dentro do sistema, e
esta vende uma **porta para fora** dele.

**A capa é anúncio de chegada, e o molde veio do dono.** A #12 também anunciou
chegada, e a regra da skill manda não repetir o molde da peça anterior. Ela cede
aqui por dois motivos: quem escreveu a manchete foi quem vende o produto, e o
fato é mesmo uma estreia — até esta semana não havia como uma IA falar com o
sistema. Placar depois desta peça: afirmação do fato 5, **anúncio de chegada
3**, pergunta 2, nome + canal 1, nome + dois-pontos 1, nome + para quem 1;
ordem direta e antes × agora continuam em 0. **A #14 não abre assim.**

Os dois moldes zerados foram escritos e caíram, e vale registrar por quê:

- **ordem direta** daria *"Pergunte ao ChatGPT quanto a sua loja vendeu"*, e
  ela só se paga quando o recurso tem **um objeto**. Este lê relatório e edita
  cardápio, e a capa escolheria um dos dois — é a mesma conta do "concisão corta
  palavra, nunca eixo" da #12, pelo outro lado;
- **antes × agora** pediria um "antes" em que consultar o resultado era
  difícil. Quem consulta resultado hoje é o nosso próprio **Desempenho**, e a
  primeira metade do título falaria mal de um módulo que a BeeFood vende e
  continua vendendo. É literalmente o erro que a #12 evitou com o cashback.

## O fato, o ângulo, e o que o slide diz

| Fato (release + painel + servidor) | Ângulo | O que vira slide |
|---|---|---|
| Com o **MCP** você conecta a sua conta ao **ChatGPT**, **Claude**, **Lovable**, **Cursor** e outras ferramentas compatíveis | Estreia: o sistema do restaurante passou a ser alcançável por uma IA | Capa |
| A folha de *Aplicativos → MCP* abre com um **arco de cinco quadrados** e o título centrado | O layout é a assinatura do recurso: quem já entrou lá reconhece a peça antes de ler o título | Capa (arte) |
| O MCP é um **padrão** de conexão entre IA e sistema | Uma frase, e acabou: quem lê não precisa saber o que é um protocolo para entender o que ganhou | 2 (corpo) |
| A IA passa a acessar o restaurante **com a autorização da sua conta** | É a resposta de "então qualquer um mexe na minha loja?", e é o único dos três passos do release que muda o que o leitor passa a ter | 2 (corpo e cena) |
| Dá para **perguntar como foram as vendas** sem abrir o painel | Prova de leitura: o valor total e o ticket médio que a IA respondeu são os que o Desempenho fecha | 3 |
| **29 das 61 rotas alteram dado**, e 24 delas são de catálogo | Prova de escrita: a IA cadastrou um produto, e ele está no Cardápio do painel | 4 |
| A tela de autorização lista **seis áreas**, com LEITURA e ESCRITA por área | É o "e muito mais" e o "então ela mexe em tudo?" na mesma imagem | 5 |
| "O acesso … pode ser revogado a qualquer momento no menu de API" | A pergunta cara é "e se eu me arrepender?", e quem responde é o texto do produto | 5 (pé) |
| No mesmo painel existem **manuais passo a passo** para conectar ao ChatGPT e ao Claude | Tira o medo de não saber fazer, e cabe numa linha do subtítulo do CTA | 6 (CTA) |
| O recurso mora em **Aplicativos → MCP** | CTA: o que se pede não é a conexão, é a **primeira pergunta** | 6 (CTA) |

**Ficou de fora, de propósito:**

- **os três passos de conexão** (copiar o link, colar na configuração de
  conectores, autorizar). É o miolo do release e é **trabalho**: slide que
  ensina a ligar o recurso é manual, e o CTA que termina em tarefa é a fatura
  antes da venda. Sobrou a parte que muda o que o leitor tem — a autorização da
  conta — e o resto virou uma linha no subtítulo do CTA;
- **o campo *Link do MCP*, o botão de copiar e a lista de manuais.** São a
  folha de configuração do recurso, e configuração não é imagem de carrossel.
  Nem capturada, nem desenhada;
- **a quebra por canal de venda** (sete canais, de `MANUAL` a `KEETA`). Era o
  slide 4 da primeira versão, e saiu por dois motivos: é mais uma resposta de
  consulta num carrossel que já tinha três, e ela não fecha com o relatório de
  *Origem* do painel (ver *o painel reparte de outro jeito*);
- **a contagem do cardápio** (399 produtos, 35 setores, 70 com venda). Mesmo
  problema, e pior: era o terceiro cartão escuro seguido dizendo "a IA sabe
  responder";
- **as seis ferramentas do servidor** (`search_beefood_api`,
  `listar_endpoints`, `detalhe_endpoint`, `execute_beefood_request`,
  `query_docs_filesystem_beefood_api`, `submit_feedback`). É arquitetura, e o
  leitor compra resultado;
- **as duas áreas "em breve"** (Entregadores e Estoque), que a tela de
  autorização mostra apagadas. Saíram do recorte do slide 5 por aritmética de
  layout, e o que elas acrescentavam era promessa;
- **a API aberta**, que saiu no mesmo dia
  ([`api-aberta-liberada`](https://beefood.app/novidades/api-aberta-liberada),
  seq 121). É release irmão e peça própria: uma fala com quem programa, a outra
  com quem pergunta.

## Slide a slide

| # | Arquivo | Título | Imagem |
|---|---|---|---|
| 1 | `01-capa.html` | O **MCP** da BeeFood chegou | o arco da folha do MCP — **captura**, cinco recortes, remontados nas posições do `mcp-panel.css` |
| 2 | `02-como-funciona.html` | Você conversa com a sua IA, e ela faz o trabalho dentro do seu BeeFood | cena de convergência com quatro dos cinco quadrados — **captura** |
| 3 | `03-relatorios.html` | **Relatórios**: pergunte o faturamento e confira no painel | bloco da conversa **desenhado** + `rec-desempenho.png` — **captura** |
| 4 | `04-cardapio.html` | **Cardápio**: peça a mudança e ela aparece no painel | conversa **desenhada** + `rec-cardapio.png` — **captura**, com o anel medido no DOM |
| 5 | `05-permissoes.html` | **Permissões**: você marca o que ela lê e o que ela altera | `rec-permissoes.png` — **captura** da tela de autorização |
| 6 | `06-cta.html` | Faça **hoje** a primeira pergunta ao seu BeeFood | `rec-cartao-mcp.png` — **captura**, recorte |

Lidos em fila, os seis títulos montam a frase do recurso: ele chegou, você
conversa e ele trabalha, ele lê o seu relatório, ele edita o seu cardápio, você
decide até onde, e dá para começar hoje. O slide 2 é a exceção estrutural da
regra do nome — ele explica o recurso que a capa acabou de nomear, e por isso é
o único título sem nome antes dos dois-pontos.

**Quatro das seis imagens são captura**, e as duas desenhadas são as duas
conversas. É o inverso da primeira versão, em que cinco das seis eram desenho.

## Decisões de arte

### A capa é a folha do MCP, e não uma releitura dela

O pedido foi literal: *"deve ser o mesmo layout de aplicativos → MCP"*. E o
layout de lá não é escolha de estilo — é a assinatura do recurso. Quem já abriu
aquela folha reconhece o arco de cinco quadrados antes de ler o título, e quem
nunca abriu vai reconhecer a folha quando chegar nela.

A ordem dos elementos é a da tela: arco, pílula, título grande centrado, linha
de apoio e a lista de tiques. O que muda é o que cada um diz:

| Na folha do painel | Na capa |
|---|---|
| pílula *MCP + Inteligência Artificial* | pílula **Novidade** |
| *Conecte o seu BeeFood a sua IA favorita* | **O MCP da BeeFood chegou** |
| quatro benefícios, todos de consulta ("Consulte os dados da sua loja", "Analise vendas e desempenho", "Crie análises e relatórios personalizados", "Conecte sua operação a ferramentas de IA") | quatro áreas que o servidor alcança de verdade, **duas delas de escrita** |
| botão arco-íris *Copiar link para conectar* | nada: copiar link é trabalho, e trabalho não vai na capa |

As **posições do arco são as do `mcp-panel.css`**, lidas no
`@keyframes mcp-panel-arc`: `translateY` e `rotate` crescendo para fora, sem
mudar de tamanho. O que muda é a opacidade das pontas — no painel ela cai a 0,4,
e aqui para em 0,55, porque a arte é vista reduzida no feed e a 0,4 as duas
pontas somem.

**Quem fica no centro é a BeeFood.** As cinco peças passam pelo centro a cada
quinze segundos, então qualquer uma seria um quadro honesto da mesma animação —
e numa peça nossa a que importa no meio é a nossa.

Duas medidas que custaram uma rodada:

- **o quadrado tem 148 px, e não 160.** As pontas ficam a 356 px do centro, e o
  giro de 16° estica a quina para 447 — contra os 452 de meia largura útil. Com
  160 a quina sangrava pela borda;
- **o recorte precisa de `border-radius: 22.2%` e `overflow: hidden`.** Sem
  isso, o que entra na arte é o retângulo do print: as quinas trazem o fundo
  quase preto da folha, que é **mais escuro** que o da capa, e cada logotipo
  ganha um quadrado escuro em volta. 22,2% é o `rounded-2xl` do painel (16 px
  num quadrado de 72), em porcentagem para acompanhar o tamanho da peça.

### As duas provas, e por que elas vêm na mesma ordem

Os slides 3 e 4 são a espinha da peça, e são irmãos de propósito: **pedido em
cima, painel embaixo**. Invertido, cada um vira "o painel mostra isto, e a IA
repetiu", que é uma frase sobre o painel.

Eles também são diferentes onde precisam ser, porque quatro cartões escuros
iguais foi exatamente o que derrubou a primeira versão:

| | Slide 3 | Slide 4 |
|---|---|---|
| o que prova | que a IA **lê** o seu dado | que a IA **altera** o seu dado |
| a conversa | só o fio, o conector e dois números — sem pergunta e sem caixa de escrever | pergunta do lojista e resposta em prosa |
| o painel | dois cartões de número | uma fileira de cardápio, com anel vermelho |
| o rótulo | *O que a IA respondeu* | *O que foi pedido na conversa* |

A prova de escrita **foi feita, não desenhada**. O `consultar-mcp.py
--escrever` pede ao conector, por `POST /v1/catalog/products`, que crie a
*Limonada Suíça 500ml* por R$ 12,90 no setor Bebidas; o `capturar-telas.py
cardapio` fotografa o setor na tela que o lojista abre todo dia; e o `--apagar`
devolve o cardápio ao que era. A sandbox fica como foi encontrada, e o
[`cena.json`](cena.json) registra o caminho inteiro.

É bebida porque o setor Bebidas é curto — o produto novo aparece sem rolagem —
e porque bebida não tem complemento, então criar e apagar não deixa grupo de
opção órfão.

### O slide 5 era desenho, e virou captura

A primeira versão desta página era uma **grade desenhada** com as seis áreas,
cartão por cartão, mais duas apagadas de "em breve". Ela caiu quando a tabela de
verdade foi capturada: desenho que copia uma tela existente é a versão pior
dela.

A captura **não sai do painel**: essa folha só existe dentro do fluxo de
autorização, entre o login e o clique em PERMITIR. Por isso quem a fotografa é o
`consultar-mcp.py --retrato`, no meio do caminho, e não o `capturar-telas.py`.

Três decisões de recorte:

1. **fora o cabeçalho**, que nomeia o cliente registrado ("BeeFood Carrossel
   (sandbox)"). Nome de script nosso numa peça de venda é ruído, e o que o
   lojista veria ali é o nome da ferramenta de IA dele;
2. **fora as duas linhas de "em breve"** (Entregadores e Estoque). Com oito
   linhas a tabela só cabia a 700 px de largura, e a letra dela chegava ao feed
   com 22 px; com seis ela ocupa os 904 e a letra dobra. O que as duas
   acrescentavam era promessa, e promessa não é o assunto da página;
3. **a linha do pé é citação**, elidida com reticências. A frase inteira — *"O
   acesso é aos dados reais da sua loja e pode ser revogado a qualquer momento
   no menu de API"* — ocupa duas linhas de 30 px e encosta nos pontinhos do
   rodapé. O que foi cortado é o que o slide já disse ("aos dados reais da sua
   loja") e o que o slide 6 vai dizer (o "onde"). Sobrou a única parte que o
   leitor não sabia: que dá para desfazer.

E a grade desenhada não foi jogada fora inteira — o que sobrou dela é a lista
de tiques da **capa**, que é onde quatro pares de palavras debaixo de um título
grande funcionam.

### Os quadrados são captura, e não desenho de marca

A cena do slide 2 usa os cinco `.mcp-arc-item` da própria folha do MCP —
Lovable, Claude, ChatGPT, Cursor e BeeFood —, cada um com o fundo que o painel
lhe dá. Nenhum logotipo foi baixado de lugar nenhum.

A folha desenha esses quadrados num **arco animado**, e item que anda não se
fotografa. O painel já tem o estado parado pronto, na regra
`@media (prefers-reduced-motion: reduce)` do `mcp-panel.css` — e
`emulate_media(reduced_motion="reduce")` **sozinho não o alcança**: o
`position: absolute` vem de uma classe utilitária do Tailwind com a mesma
especificidade da regra de dentro da media query, e quem desempata é a ordem
das folhas. O sintoma é silencioso e caro: os cinco quadrados saem empilhados
na mesma coordenada, as cinco medidas do `bounding_box` vêm iguais, e os cinco
recortes viram cinco cópias do quadrado da BeeFood. A captura repete a
declaração do próprio painel com `!important`, e o que aparece é o layout que o
produto desenha para quem pede menos movimento.

Dentro do disco branco os cinco viram um conjunto. Soltos, o quadrado
azul-escuro do Lovable e o quase branco do ChatGPT lado a lado leem como dois
tratamentos diferentes.

### O ícone do cartão também é um carrossel, e a captura escolhe a estação

Uma correção de uma nota antiga deste arquivo, que dizia que *"o ícone do cartão
MCP é o mesmo do Lovable"* e que o painel dava aquela marca ao cartão. **Não
dá.** O `McpIconCarousel` roda os cinco logotipos dentro do quadrado do cartão,
um a cada três segundos (`mcp-app-arc`, 15 s para 5 logos). O print anterior
pegou um quadro, e o quadro que a animação parada mostra é o **primeiro da
lista** — o Lovable.

A captura passou a escolher a quinta estação, a da BeeFood, com duas linhas de
CSS que mexem só na opacidade (`ICONE_BEEFOOD`). Continua sendo captura e
continua sendo um quadro real da animação: é o mesmo critério do arco da capa.
O leitor que chegar em *Aplicativos → MCP* vai ver o quadrado girando, e a
BeeFood é uma das cinco faces que ele mostra.

### A cena desce reta, e o visto quer dizer "autorizado"

É a gramática da capa de dark kitchen (`.origem` / `.fio` / `.selo-ok`), com
duas diferenças:

- **os fios descem retos**, e não em curva. Curva serve para juntar três linhas
  num ponto; aqui embaixo há uma coisa só e ela é **larga** — quatro linhas
  entrando numa barra pedem reta, e curva vira enfeite;
- **o visto não é "deu certo", é "autorizado"**. É o que a frase do corpo
  promete, desenhado no lugar onde acontece.

Uma medida que custou uma rodada: o fio tem **170 px para 54 de selo**. A
primeira versão tinha 76, e sobravam 11 px de tracejado de cada lado do selo —
quatro bolinhas penduradas no nome não desenham caminho nenhum.

### O painel reparte de outro jeito, e foi por isso que o slide de canais saiu

O painel tem *Desempenho → Vendas → Origem*, que parece ser o par de uma
pergunta sobre canais. Não é: ele agrupa por **tipo de atendimento** (Delivery,
Mesas, PDV, Cardápio Digital, iFood, 99Food, Keeta), e a API agrupa por **canal
de venda**, onde balcão, mesa e PDV caem todos em `MANUAL`. As duas contas somam
o mesmo total e repartem diferente — a própria tela dá Delivery com
R$ 7.431,87 na lista e R$ 10.330,37 no pódio logo abaixo, porque nem ela usa um
corte só.

Enquanto a quebra por canal era um slide, isso obrigava a peça a não fotografar
aquela tela e a não emprestar o nome dela. Com o slide fora, o problema sumiu
junto — e fica registrado aqui, porque a próxima peça que quiser falar de canal
de venda vai esbarrar nele de novo.

### Um jogo de números, e ele foi defendido em código

A loja de demonstração **recebe pedido enquanto a peça é feita**, e isso decide
se a peça tem um jogo de números ou dois. Por isso a conferência não é do olho:
o [`capturar-telas.py`](capturar-telas.py) lê o `conversas.json`, compara com o
que acabou de fotografar e **estoura** se os dois divergirem.

```
painel: R$ 14.283,52 | R$ 53,70    conversa: R$ 14.283,52 | R$ 53,70
--> painel e conversa fecham no mesmo número
```

Esse guarda pegou um defeito que o olho não pegaria. O painel dizia
R$ 14.283,52 e a conversa R$ 12.083,98, e não era pedido novo: **o "hoje" da
máquina não é o da loja**. O Cloud Agent roda em UTC, e depois das 21h de
Brasília `date.today()` já virou o dia seguinte — a janela de 30 dias andava 24
horas, perdia o primeiro dia e a diferença lia como erro de leitura da IA. O
`consultar-mcp.py` passou a calcular o dia em UTC−3.

A mesma conferência vale para a escrita: o `cardapio()` **estoura** se o produto
que o `conversas.json` diz que foi criado não estiver na tela.

### Três recortes, e por que cada um fecha onde fecha

Medidos no DOM pela própria captura ([`medidas.json`](medidas.json)), nunca
estimados na miniatura.

- **`rec-desempenho.png`** começa na linha *Últimos 30 dias* — e não no seletor
  acima dela, onde moram as datas, porque data na arte faz o post nascer velho.
  Fecha no **pé do número**, com folga de 4 px: a linha seguinte do painel é
  *+141,1% vs período anterior*, que é verdade da loja de demonstração e, numa
  peça de venda, lê como crescimento prometido pelo produto. É a lição da #9,
  que cortou o *R$ 0,00 de receita gerada* pelo mesmo motivo, do outro lado.
- **`rec-cardapio.png`** fecha **dentro** do cartão vizinho, 170 px depois do
  nosso. Com os dois cartões inteiros o quadro tinha 970 px de tela dentro de
  904 de slide, e o nome do produto ficava com 13 px de altura numa arte de
  1080; cortado ao meio o vizinho ainda diz o que precisa dizer — que o produto
  novo entrou numa lista com outros — e o que sobra aparece 1,3× maior. De
  quebra sai a barra de botões da direita (*Editar em Lote*, *Importar*), que é
  tela de trabalho e não prova nenhuma. O anel vermelho vem do `medidas.json`
  (x 1,5 / y 40,9 / 72,3 de largura / 57,9 de altura).
- **`rec-cartao-mcp.png`** é o cartão do MCP na grade de Aplicativos, com a
  borda arco-íris, e entra a 904 px — 1,33× o arquivo puro, que ainda sai limpo.
  Não dá para capturar maior: a grade reflui com zoom e o cartão sai **mais
  estreito**, não mais largo (1,5× dá 340 CSS px de largura, 2× dá 293). A
  chamada do cartão aparece cortada em *"a sua I…"* porque é assim que o painel
  a corta — é print, e print mostra o que está na tela.

**O Desempenho não é uma página do painel: é um `iframe`** servido por
`relatorios.beefood.com.br`. Procurar o rótulo no documento de fora não acha
nada — nem `VALOR TOTAL`, nem `Valor total`, nem uma sondagem do DOM inteiro —,
e a busca **sai vazia em vez de dar erro**, que é o pior jeito possível de
descobrir isso. `frame_locator("iframe")` resolve, e a caixa que ele mede já
vem em coordenada da página, que é o que o `clip` do print espera.

**E o nome do setor se filtra por igualdade exata.** `text=Bebidas` casa
primeiro com *iFood Vínculo Bebidas*, que tem um produto só e nenhum deles é o
nosso — e o print sai de uma tela que **parece** a certa. `exact=True` resolve.

### O CTA não repete a arte da capa

É a segunda vez na série em que isso acontece, e a skill permite as duas coisas
— a repetição é aprovada, não obrigatória.

Fechar com o arco seria fechar com a imagem que o leitor viu cinco telas atrás,
e num carrossel a última página é a que fica. O que entra no lugar serve melhor
ao que o slide pede: o último slide manda abrir *Aplicativos → MCP*, e o cartão
fotografado mostra exatamente o que o leitor vai ver quando chegar lá.

Ele é o limite da regra de "nada de tela de configuração", e fica do lado de
dentro: o que aparece não é campo, interruptor nem lista de parâmetros, é a
**porta** — um cartão de navegação com o nome do recurso. A folha que está atrás
dele, essa sim, não entrou em nenhum slide.

Ele também fecha o círculo do fio arco-íris que abre as telas de conversa dos
slides 3 e 4: aquele fio desenhado e esta borda fotografada são a mesma
assinatura.

### O verbo do CTA é "pergunte", e não "conecte"

O molde da série está lá — chapéu *Já está no ar*, imperativo com **hoje**,
primeiro passo no subtítulo e a pílula apontando para o módulo. O que mudou foi
o verbo, pelo mesmo motivo da #12.

Esta peça só tem um ato do lado do leitor, e ele é trabalho: copiar um link e
colar na configuração de conectores. Diferente da #12, aqui **não há uma decisão
de cadastro para pedir no lugar** — não se escolhe recompensa, não se define
régua. Então o que o título pede é o resultado:

> Faça **hoje** a primeira pergunta ao seu BeeFood

Quem quer fazer a pergunta conecta sozinho. O passo concreto vai no subtítulo,
junto com a única informação que tira o medo de não saber fazer: os dois passo
a passo que a própria folha do MCP traz, do ChatGPT e do Claude. **Lovable e
Cursor aparecem no slide 2 e não aqui**, porque para eles não há manual
publicado, e CTA não promete material que não existe.

### Nenhum dado de cliente em imagem nenhuma

Não há o que borrar nesta peça, e isso é consequência do assunto. Tudo que
entrou é agregado — resumo de vendas, contagem de cardápio, tabela de
permissões, um produto criado por nós. O `token` de sessão do `iframe` do
Desempenho viaja na URL do quadro, e não aparece em pixel nenhum.

Uma consulta precisou de cuidado: `/v1/store/reviews` devolve **telefone de
quem avaliou**. Por isso o `consultar-mcp.py` guarda dela só o `total`, e nunca
o corpo. O repositório é público.

O `access_token` do OAuth fica em `/tmp/beefood-mcp-token.json`, **fora do
repositório**. As credenciais da conta sandbox seguem versionadas, pela regra da
casa: o ambiente é descartável.
