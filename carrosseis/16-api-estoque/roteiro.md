# Carrossel 16 — Estoque pela IA e pela API

- **Gênero:** novidade
- **Fonte:** [Estoque na API Aberta e no MCP 📦](https://beefood.app/novidades/api-estoque-mcp),
  26/10/2026, áreas Aplicativos e Estoque — e a **documentação**, que é de onde
  saiu o que o release resume
- **Peça irmã, e molde desta:** [`13-mcp-conexao-ia`](../13-mcp-conexao-ia/) —
  mesmo leitor, mesma gramática, mesma capa (ver *Esta peça foi devolvida*)
- **Manual:** não existe. O passo a passo do recurso é o portal de
  desenvolvedores e as duas folhas de *Aplicativos*
- **Medição:** `consultar-estoque.py` → `chamadas.json`. Todo número desta
  peça foi medido hoje contra a loja sandbox *BeeFood3 - Manual* (empresa
  38311), **pelas duas portas**
- **Formato:** 1080 × 1350 (4:5)
- **Slides:** 6

## Esta peça foi devolvida, e a devolução tem três linhas

> - slide 1 → idem ao outro carrossel que já fizemos, mostrando MCP → título
>   precisa melhorar
> - de forma geral, todos os outros slides deveriam ser parecidos com o
>   carrossel que já fizemos sobre MCP
> - por que erramos tanto? o novidades não é técnico e sim informativo

A primeira versão desta peça tinha seis páginas e **quatro formas de
desenvolvedor**: a capa abria com a conversa desenhada, o slide 3 mostrava o
corpo de `GET /v1/stock/items` com `supplyId` e `stockSituation: "low"`, e o
slide 4 era uma tabela de nomes de operação — `add`, `subtract`, `new`,
`stockControl`, `stockMinimumQuantity` — com a tradução de cada um ao lado. Era
a página de referência da documentação copiada para dentro de um post.

A #13 estava no repositório o tempo todo, pronta, com o mesmo leitor e a mesma
gramática. O erro não foi de falta de material. Foi de **duas regras aplicadas
fora do lugar**, e as duas estão escritas na memória da skill:

### 1. "A documentação é a fonte" vale para o ESCOPO, não para o vocabulário

A regra da 39ª rodada diz que em peça de integração o release é a manchete e a
documentação é a fonte. Ela foi escrita para resolver um problema de **escopo**:
o release conta metade do que foi entregue, e quem só lê o release vende menos
do que existe. É isso, e só isso.

Aplicada ao **vocabulário**, ela vira outra coisa — e foi o que aconteceu aqui.
A documentação fala em rota, parâmetro, operação e código de erro, porque o
leitor dela é quem integra. Quem rola o feed tem um restaurante. A regra
continua valendo: a medição desta peça segue sendo contra a API, pelas duas
portas, e é o que garante que cada número da arte é verdade. **O que a
documentação não decide é como a arte fala.**

A frase do dono fecha a conta: *o novidades não é técnico e sim informativo*. É
a página que o lojista lê para saber o que ganhou, não o changelog.

### 2. "Forma antes do conteúdo" é remédio, e não objetivo

A memória registra, desde a #13, que peça de integração tende a virar quatro
blocos escuros iguais, e que o que separa um slide do outro é a forma. A
primeira versão leu isso como **meta**: variou a forma cinco vezes em seis
páginas — conversa, cena, código, lista, captura, captura — e marcou como
acerto o fato de nenhuma página repetir a anterior.

Variedade não é o objetivo; **monotonia é o defeito**. A #13 tem duas páginas de
miolo com a MESMA forma (slides 3 e 4: conversa em cima, print do painel
embaixo) e não é monótona, porque o que muda dentro da forma é o que ela prova —
uma lê, a outra altera. Forma repetida com conteúdo diferente lê como argumento;
forma variada só para variar lê como catálogo de componentes.

### E a terceira, que é a de onde o molde veio

A #16 copiou as formas da **#14**, e não da #13, por um motivo bobo: a #14 é a
irmã mais recente, e as duas tratam de integração. Mas irmandade de peça não se
mede por assunto, e sim por **leitor**:

| Peça | Assunto | Quem lê |
|---|---|---|
| #13 MCP | integração | o **lojista** — ele conecta, ele pergunta |
| #14 API Aberta | integração | o **integrador** — ele escreve o código |
| **#16 Estoque** | integração | o **lojista**, como a #13 |

A `.requisicao` e a `.eventos` da #14 existem porque lá o leitor lê JSON. Aqui
ele não lê, e nenhuma das duas formas voltou nesta versão.

## O que mudou da primeira versão para esta

| | Antes | Agora |
|---|---|---|
| capa | conversa desenhada, título *"API de Estoque: a sua IA responde o que está acabando"* | **o arco de cinco quadrados da #13**, título *"Agora a sua IA cuida do Estoque"* |
| slide 3 | cartão de código: `GET /v1/stock/items?stockSituation=low` e o JSON da resposta | **prova pareada**: a pergunta na conversa, e a aba *Insumos* do painel embaixo |
| slide 4 | tabela de operações (`add`, `subtract`, `new`) com tradução | **prova pareada**: o pedido na conversa, e a linha do produto no painel, com o saldo novo |
| slide 5 | dois prints sem rótulo | os mesmos dois prints, **com o nome da tela de cada um** |
| slide 6 | *"Ligue o Estoque hoje"* | *"Pergunte hoje o que está acabando"* |
| palavra "API" | na capa, no título | só no caminho de menu do CTA, que é como o painel escreve |

As duas provas pareadas **custaram duas capturas novas de painel** — e é por
isso que elas não existiam antes. Fazer prova de verdade é mais caro que
desenhar o fato: foi preciso achar, na loja de exemplo, um insumo abaixo do
mínimo que aparecesse com as pílulas de contagem ao lado, e um produto com nome
**único** para a escrita poder ser fotografada sozinha na tela.

## Nome de venda × nome do release

O release se chama *Estoque na API Aberta e no MCP*, que é um título de
changelog: ele nomeia os dois lugares onde a coisa apareceu. A primeira frase do
texto diz *"a BeeFood lançou a **API de Estoque**"*.

A peça não usa nenhum dos dois. Usa **Estoque**, que é o nome da linha nova nas
duas folhas de *Aplicativos*, o nome do módulo no menu e a palavra que o lojista
já usa. "API de Estoque" é como o desenvolvedor chama, e foi o nome que a
primeira versão pôs na capa — nome de venda inventado do lado errado do balcão.

## A terceira peça da família, e o que a separa das outras duas

| Peça | O que ela vende | Quem é o sujeito |
|---|---|---|
| #13 MCP | a **porta**: uma IA conectada ao sistema | a ferramenta de IA |
| #14 API Aberta | a **porta**: o sistema do parceiro falando com o nosso | o sistema do parceiro |
| **#16 Estoque** | o que passou a existir **atrás** das duas portas | o estoque da loja |

As duas primeiras venderam encanamento. Esta é a primeira que vende **o que
corre pelo cano**: as portas já estavam abertas e não mudaram, o que mudou foi o
que dá para alcançar por elas. Por isso a peça não repete *como conectar* — isso
é assunto da #13 e da #14, as duas publicadas — e gasta as seis páginas no que o
Estoque faz.

E há uma herança concreta, medida: a #14 fotografou a folha de permissões da API
Aberta e **fechou o quadro em Avaliações**, de propósito, porque as duas linhas
seguintes estavam apagadas, com a etiqueta *Em breve*. Eram **Entregadores e
Estoque**. A #13 descartou as mesmas duas linhas pelo mesmo motivo. Uma delas
saiu do em breve hoje — e é por isso que nesta peça o recorte é o contrário: ele
existe **para** mostrar a linha que as outras duas tiveram de esconder.

## O que veio de cada fonte

| Do release | Da documentação e das chamadas |
|---|---|
| que dá para consultar saldos, registrar movimentações, cadastrar insumos e ver o histórico | que são **11 rotas**, **5 delas de escrita**, em dois escopos: `stock:read` e `stock:write` |
| "produtos, complementos e insumos em uma única lista" | que a lista é **uma rota só** (`GET /v1/stock/items`), e que a loja de exemplo tem **362** itens nela: 267 insumos, 64 produtos e 31 complementos |
| "quais insumos estão abaixo do mínimo?" | que essa pergunta é **um filtro** (`stockSituation=low`), e que entre os insumos da loja ela devolve **1** de 11 com controle ligado |
| "entradas, saídas e correção do saldo após a contagem" | que as três operações se chamam `add`, `subtract` e `new`, e que **`remove` e `set` não existem** — a `new` grava o saldo informado, e é por isso que a demonstração desta peça é reversível |
| "para vários itens de uma vez" | que o lote responde **uma linha por item**, e que a que falha não desfaz as outras |
| "períodos de até 6 meses" | que o limite é do **servidor**: `400 'fromDate'..'toDate' must span at most 6 months` |
| "ative as permissões de Estoque na credencial" | que a folha já mostra a linha **Estoque**, descrita como *Insumos, categorias, itens e movimentações* |

**Nada disso virou vocabulário de arte.** Os nomes de rota, de operação e de
escopo ficam neste roteiro, no `chamadas.json` e — o que interessa ao leitor —
na legenda, que é por onde o suporte responde. Na arte, `stockSituation=low` se
chama *"o que está abaixo do mínimo"*, e `operation: add` se chama *"dá entrada
no estoque"*.

## Fato → ângulo → o que o slide diz

| Fato (medido) | Ângulo | Slide |
|---|---|---|
| A IA passou a alcançar o Estoque, pelas mesmas ferramentas da #13 (ChatGPT, Claude, Lovable, Cursor) | O módulo já existia; o que chegou foi poder cuidar dele conversando | Capa |
| As mesmas 11 rotas atendem o MCP e a API Aberta, no mesmo escopo | A notícia é dupla e as duas metades têm donos diferentes: a IA é do lojista, o sistema é do fornecedor dele. Ninguém precisa escolher | 2 |
| `stockSituation=low` devolve 1 insumo, de 11 com controle ligado — e o painel mostra o mesmo 1 na pílula *Baixo* | Prova de leitura: a resposta da conversa é a tela que ele abre todo dia | 3 |
| `operation: add` de 20 unidades muda o saldo do produto de 47 para 67, e a tela de *Produtos* passa a mostrar 67 | Prova de escrita: mandar lançar a compra funciona, e funciona no painel dele | 4 |
| A linha **Estoque** está nas duas folhas de permissão, com *Consultar* e *Alterar* separados | Entregar o estoque a um robô assusta mais que entregar o cardápio: é dinheiro parado. O que desarma é a chave estar do lado de cá | 5 |
| Está em *Aplicativos → MCP* e em *Aplicativos → API Aberta*, nas duas | CTA: não há tela nova para aprender; é uma chave a mais numa folha que já existe | 6 (CTA) |

## Slide a slide

| # | Arquivo | Título | Imagem |
|---|---|---|---|
| 1 | `01-capa.html` | Agora a sua IA cuida do **Estoque** | o arco de cinco quadrados da folha do MCP — **captura**, a mesma da #13 |
| 2 | `02-duas-portas.html` | Você **pergunta**, ou o seu sistema pede sozinho | cena de convergência com as duas portas — **desenho** |
| 3 | `03-uma-lista.html` | **Estoque**: pergunte o que está acabando e confira no painel | conversa **desenhada** + `rec-insumo-baixo.png` — **captura** |
| 4 | `04-movimentacao.html` | **Entrada**: mande lançar a compra e o saldo muda no painel | conversa **desenhada** + `rec-produto-entrada.png` — **captura**, com o anel medido no DOM |
| 5 | `05-permissao.html` | **Permissões**: você escolhe se ela só consulta ou também altera | `rec-estoque-api.png` + `rec-autorizacao.png` — **captura** |
| 6 | `06-cta.html` | Pergunte **hoje** o que está acabando | `rec-cartoes.png` — **captura** dos dois cartões de *Aplicativos* |

Lidos em fila, os seis títulos montam a frase do recurso: agora a sua IA cuida
do estoque, você pergunta ou o seu sistema pede, ela diz o que está acabando e o
painel confirma, ela lança a compra e o painel confirma, você escolhe até onde
ela vai, e dá para perguntar hoje. O slide 2 é a exceção da regra do nome — ele
explica o que a capa acabou de nomear, como o slide 2 da #13.

**Cinco das seis páginas trazem captura**, e a única inteiramente desenhada é a
cena do slide 2 — que desenha um caminho, não uma tela. As conversas dos slides
3 e 4 são desenho porque não há o que fotografar: a resposta acontece dentro do
ChatGPT, do Claude, do Lovable ou do Cursor, que não rodam aqui e não são nossos
para capturar. É a mesma conta da #13, e o inverso da primeira versão desta
peça, em que cinco das seis eram desenho.

### A forma, agora

| # | Forma | Na #13 |
|---|---|---|
| 1 | arco de cinco quadrados, pílula, título, tiques | **igual** |
| 2 | cena de convergência: origens, fios, selos e barra escura | **igual** |
| 3 | conversa desenhada + print do painel, com rótulo em cada metade | **igual** |
| 4 | conversa desenhada + print do painel, com anel vermelho | **igual** |
| 5 | print da tela de permissão | **igual** |
| 6 | capa escura, caminho em pílula e o cartão de *Aplicativos* | **igual** |

Seis de seis. Isso é o pedido do dono cumprido ao pé da letra, e não é
preguiça: as duas peças vendem a mesma coisa para a mesma pessoa, e quem viu a
#13 reconhece esta antes de ler o título.

O que impede a monotonia é o que muda **dentro** de cada forma, como na #13:

| | Slide 3 | Slide 4 |
|---|---|---|
| o que prova | que a IA **lê** o seu estoque | que a IA **altera** o seu estoque |
| a conversa | pergunta do lojista e resposta em tabela de dois números | pedido do lojista e resposta em uma frase |
| o painel | a aba *Insumos* com as pílulas de contagem | a aba *Produtos*, filtrada, com anel vermelho no saldo |
| o rótulo | *O que a IA respondeu* | *O que foi pedido na conversa* |

## A capa

### A forma é a da #13, e foi pedida com todas as letras

> *slide 1 → idem ao outro carrossel que já fizemos, mostrando MCP*

Arco de cinco quadrados, pílula *Novidade*, título grande centrado, linha de
apoio e a lista de quatro tiques — que é a ordem da própria folha
*Aplicativos → MCP* no painel. As medidas são as da #13, e elas custaram uma
rodada lá: peça de **148 px** e passo de **178** põem as pontas a 356 px do
centro, e o giro de 16° estica a quina para 447 contra os 452 de meia largura
útil; com 160 a quina sangra.

Os cinco quadrados são os **mesmos arquivos** da #13 —
`imagens-puras/logo-*.png` —, que são recortes dos `.mcp-arc-item` da folha, com
o fundo que o painel dá a cada um. Nenhum logotipo foi baixado de lugar nenhum,
e capturar de novo daria pixel idêntico.

Os quatro tiques são o bloco de benefícios da folha, reescritos para este
recurso: os três primeiros são exatamente o que os slides 3 e 4 provam, e o
quarto nomeia as ferramentas.

### O título, e o molde

> **Agora a sua IA cuida do Estoque**
> Pergunte o que está acabando e mande lançar a compra, ali na conversa — ou
> deixe o seu próprio sistema fazer sozinho.

O molde é **afirmação do fato**. Placar depois desta peça: afirmação do fato 6,
anúncio de chegada 3, nome + dois-pontos 2, pergunta 2, nome + canal 1, nome +
para quem 1, ordem direta 1; antes × agora continua em 0. A #15 abriu em ordem
direta, então a regra de não repetir o molde da anterior está cumprida.

Três moldes foram escritos e caíram:

- **nome + dois-pontos**, que era o da primeira versão: *"API de Estoque: a sua
  IA responde o que está acabando"*. Caiu junto com a palavra API — o molde
  começa pelo nome, e aqui o nome que o leitor usa é só *Estoque*, que sozinho
  não abre uma capa porque o módulo já existe;
- **anúncio de chegada** daria *"Chegou a API de Estoque"*, e o molde só se paga
  quando um módulo inteiro chega. Aqui o módulo de Estoque já estava no painel;
  o que chegou foi o acesso a ele de fora. "Chegou o Estoque" seria falso para
  quem já usa;
- **antes × agora** tem, pela primeira vez na série, um "antes" documentado que
  não é produto nosso no lado perdedor: o *Em breve* que a #13 e a #14
  fotografaram. Caiu por outro motivo — esse "antes" é **nosso**, não do leitor.
  Quem rola o feed nunca abriu a folha de permissões para ver a linha apagada.

A palavra **Agora** faz o trabalho que o "antes × agora" faria, sem gastar meia
linha explicando uma tela que o leitor não viu. E o verbo é **cuidar**, não
*consultar* nem *integrar*: cuidar do estoque é o que o lojista faz, e é o que
ele passou a poder fazer conversando.

## As duas provas, e por que elas são o coração desta versão

Os slides 3 e 4 são irmãos de propósito, e a ordem é a da #13: **o que foi dito
na conversa em cima, o painel embaixo**. Invertido, cada um vira "o painel
mostra isto, e a IA repetiu", que é uma frase sobre o painel.

### A leitura (slide 3)

A IA responde que o TOMATE está com 1,5 KG para um mínimo de 2 KG, e que é o
único entre os 11 insumos com controle de estoque. Embaixo, a aba *Insumos* de
*Meu Estoque*: as pílulas **Regular 10 · Baixo 1 · Crítico 0 · Controla estoque
11** e a linha do tomate, com mínimo 2 e estoque atual 1.5.

**As pílulas são parte da prova.** Sem elas, uma tabela de uma linha só diria
que existe um tomate baixo — não que ele é o único. É a pílula *Baixo 1* que
transforma a captura na confirmação da frase.

**O número da frase mudou de 18 para 11, e isso é correção de fato.** A primeira
versão dizia "os outros 18 continuam regulares", somando insumo, produto e
complemento. O número era verdade e teria **desmentido a imagem logo abaixo
dele**, porque a pílula da aba *Insumos* conta só insumo. O
`consultar-estoque.py` passou a medir também a versão `type=supply`, e ela está
em `chamadas.json`, em `abaixoDoMinimo.sóInsumos`.

### A escrita (slide 4)

O lojista manda dar entrada de 20 unidades, a IA confirma que o saldo passou a
67, e a aba *Produtos* mostra 67 com anel vermelho.

**A escrita foi feita, não desenhada.** O `consultar-estoque.py --entrada` pede
ao conector, pela rota de verdade, a entrada de 20 unidades; o
`capturar-telas.py --so entrada` fotografa a linha; e o `--restaurar 47` devolve
o saldo. Está em `chamadas.json`, em *escrita*, com 47 → 67 → 47 e
`oSaldoVoltou: true`.

**O item não é o do release, e o motivo é de captura.** O release diz
"refrigerante", e a Coca Cola 350ml está cadastrada **duas vezes** na loja de
exemplo, as duas com controle ligado: a busca devolve duas linhas idênticas e a
captura deixa de provar qual delas mudou. O TOMATE do slide 3 seria melhor para
a história, mas são três insumos com esse nome, e a busca devolve cinco linhas.
Dos oito produtos com controle, **só dois têm nome único**, e o Sprite é um
deles.

A regra que ficou: **o item da prova de escrita tem de poder ser achado sozinho
na tela em que vai ser fotografado.** O `capturar-telas.py` estoura se a busca
devolver qualquer número de linhas diferente de 1.

**A captura do slide 4 não tem as pílulas, e a do slide 3 tem.** Com a tela
filtrada por busca, as pílulas passam a contar só a linha achada e todas dizem
1 — um *Regular 1* na página seguinte a um *Regular 10* lê como contradição.
Onde a pílula não prova nada, ela sai.

**Os rótulos nomeiam a aba** (*em Estoque → Insumos*, *em Estoque → Produtos*).
Sem isso, as duas contagens diferentes em páginas seguidas leem como erro.

### Por que não é a tela de Movimentações

Ela seria a prova mais direta da escrita: a entrada de 20 aparece lá com saldo
anterior e delta. Mas a tabela tem uma coluna **Data**, e data na arte faz o
post nascer velho — a peça pode esperar na fila de publicação. A tela de
*Produtos* prova o mesmo fato sem carimbar o dia.

## O que ficou de fora, e por quê

- **o JSON de qualquer rota.** É o defeito que foi devolvido. O corpo das
  respostas continua medido e vive no `chamadas.json`;
- **os nomes das operações.** `add`, `subtract` e `new` são o que o integrador
  escreve; o lojista diz "dá entrada", "dá baixa" e "corrige a contagem". Os
  três verbos estão na arte, os três nomes estão aqui;
- **a contagem de rotas.** Onze é um número que o leitor não tem como julgar —
  ele não sabe se é muito ou pouco. O cartão escuro do slide 2 trocou "11
  rotas" pela fórmula da #13: *Lê e altera: saldo, entrada, baixa e contagem*;
- **o histórico de movimentações.** Um dos quatro pontos do release, medido (566
  movimentações na janela de seis meses). Virou uma linha na legenda — ver *Por
  que não é a tela de Movimentações*;
- **o limite de seis meses**, medido de propósito pedindo 200 dias e guardando
  o `400`. É um limite, e limite antes do CTA é a fatura antes da venda;
- **o lote de vários itens**, que era metade do slide 4 antigo. Quem recebe nota
  com trinta itens é o sistema do fornecedor, não o lojista — e o slide 4 agora
  prova uma coisa só, que é a que o leitor vai fazer. Fica na legenda;
- **o cadastro de insumo por categoria.** Quarto ponto do release e o mais fraco
  para quem lê: já dá para fazer no painel, e o ganho pela API só existe para
  quem está migrando de sistema;
- **os filtros da consulta.** A rota aceita treze parâmetros, de `sectorId` a
  `stockQuantityOperator`. O slide 3 mostra **um**, e mostra como pergunta;
- **o `userId` de quem moveu**, que vem em toda movimentação. O repositório é
  público e o campo não acrescenta nada ao argumento;
- **a comparação com os outros grupos.** O Estoque ser o segundo maior da API é
  um fato bonito e é **interno**;
- **o nome do cliente.** Nenhuma arte desta peça mostra nome, telefone ou
  e-mail: o que aparece é tela de estoque e de permissão.

## Decisões de arte

### O slide 2 é cena, e por que não é o `.fluxo-api` da #14

Por desenho: o `.fluxo-api` é **entradas → núcleo → saídas**, e é a saída que
justifica os dois lados. O Estoque não tem webhook: nada sai sozinho. Montar o
lado direito com qualquer coisa seria preencher uma forma que o fato não tem.

Por sentido: aqui as duas coisas de cima não são dois sistemas quaisquer — são
**as duas portas**, e o que o slide afirma é que elas chegam no mesmo lugar.
Isso é convergência, e é a cena que a #13 usa. A regra do fio é a de lá: para
linha que cai numa barra larga, o fio desce **reto**; curva só quando o destino
é um ponto.

O corpo amarra na #13 de propósito — *"a sua IA já lia os seus relatórios e
mexia no cardápio"* é exatamente o que aquela peça vendeu. Quem viu as duas
entende que isto é uma área nova numa coisa que ele já conhece.

### Dois recortes no slide 5, um de cada folha, e agora com rótulo

O slide afirma que a chave existe nas duas portas, então mostra as duas: a linha
**Estoque** do formulário de credencial (*Aplicativos → API Aberta*, com
*Consultar* e *Alterar*) e a linha **Estoque** da tabela de autorização do MCP
(com LEITURA e ESCRITA marcadas).

A segunda só existe **dentro do fluxo de autorização** — não há rota no painel
que abra aquela tela —, então ela é capturada no meio do caminho, pelo
`--retrato` do `consultar-estoque.py`. É a técnica que a #13 inventou, e aqui
ela fotografa exatamente a linha que a #13 e a #14 tiveram de deixar de fora.

Cada faixa ganhou o **nome da sua tela** nesta versão. Print sem rótulo é print
que o leitor adivinha de onde veio, e duas faixas sem rótulo leem como uma só,
partida no meio. É a regra da #13, cujo print de permissões também tem rótulo.

**As duas larguras são diferentes, e isso é cálculo.** O que o olho compara é o
tamanho da letra, que sai de `largura exibida ÷ largura capturada em px de CSS`:
o cartão da credencial tem 605 px de CSS e a tabela tem 444. Nos dois a 840, o
primeiro chegava a 1,39× e o segundo a 1,89×. A 904 e 720 as escalas ficam em
1,49× e 1,62×, que o olho lê como iguais.

### A janela da captura decide a escala final

A tabela de *Meu Estoque* acompanha a largura da janela, então a janela é
escolhida por aba e está escrita no `capturar-telas.py`:

| Aba | Colunas | Janela | Tabela | Escala a 904 px |
|---|---|---|---|---|
| Insumos | 9 | 1120 | 870 px de CSS | 1,04× |
| Produtos | 11 | 1140 | 901 px de CSS | 1,00× |

Aos 1440 de sempre, a tabela de Insumos chega a 1190 px e **encolhe** para 0,76×
dentro da faixa de 904 — letra de 11 px numa arte de 1080. O script estoura se a
tabela pedir mais largura do que a janela tem.

### O CTA fotografa os dois cartões

A #14 fechou com o cartão da API Aberta na grade de *Aplicativos*, pela razão
que a #13 deixou escrita: a última página é a que fica, e ela tem de mostrar o
que o leitor vai procurar. Aqui são **dois** cartões, porque são duas portas, e
é a última chance de a peça não deixar metade da notícia para trás.

**O imperativo pede o resultado, não o trabalho.** A primeira versão dizia
*"Ligue o Estoque hoje"*, e ligar a chave é tarefa — trabalho no último slide é
a fatura antes da venda, que é a lição da #12. A #13 fechou com *"faça hoje a
primeira pergunta"*, e aqui a pergunta tem assunto: o que está acabando. Quem
quiser fazer a pergunta liga a chave sozinho, e o subtítulo diz que é uma chave
só.

### O jogo de números

Quatro, e todos vêm de fora de nós:

| Número | De onde |
|---|---|
| **11** insumos com controle, **1** abaixo do mínimo | `GET /v1/stock/items?type=supply`, com e sem `stockSituation=low` |
| **47 → 67** no Sprite Original 350ml | `PATCH /v1/stock/items`, feito e desfeito |
| **11** rotas, **5** de escrita | `listar_endpoints` do servidor de documentação — só no roteiro |
| **362** itens: 267 insumos, 64 produtos, 31 complementos | `GET /v1/stock/items` por tipo — só no roteiro |

Nenhum número de resultado comercial aparece: não há tela que mostre quanto o
controle de estoque economizou, e prometer isso seria prometer relatório.

**O número pequeno é o número certo.** Um item abaixo do mínimo é uma resposta
magra, e a tentação era mexer no saldo de dois ou três insumos para a lista
ficar mais cheia. Isso seria inventar o fato que a arte existe para provar — e a
resposta curta diz, de graça, uma coisa que uma lista longa não diria: que a
pergunta serve justamente para **não** ter que olhar os outros dez.

## O sandbox voltou como estava

A única escrita desta peça é a entrada de 20 unidades no Sprite Original 350ml,
desfeita no mesmo arranque e conferida por leitura. Nenhuma permissão foi
alterada: a linha **Estoque** já estava ligada na credencial quando a folha foi
aberta, e a tela de autorização do MCP já vinha com as caixas marcadas.

**Demonstração reversível precisa de duas saídas**, e essa lição é da primeira
rodada: a leitura que vem logo depois do `PATCH` é idêntica à que veio antes
dele, e a API devolve `429` para requisição idêntica em menos de quatro
segundos. O script quebrou **entre** a entrada e o desfazer, e o saldo ficou
alto. A correção foi dupla — uma pausa de cinco segundos antes de cada leitura
(o limite é publicado em `docs.beefood.app/docs/limites`, então respeitar é o
certo, não contorno) e um `--restaurar` que devolve o saldo sozinho.

A credencial de produção fica em `/tmp/beefood-api-cred.json` e **não** entra no
repositório. Os recortes começam abaixo dela, já na imagem **pura**, porque a
pura também é versionada.
