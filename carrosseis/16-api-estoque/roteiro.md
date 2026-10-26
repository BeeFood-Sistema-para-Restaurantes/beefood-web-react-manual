# Carrossel 16 — API de Estoque

- **Gênero:** novidade
- **Fonte:** [Estoque na API Aberta e no MCP 📦](https://beefood.app/novidades/api-estoque-mcp),
  26/10/2026, áreas Aplicativos e Estoque — e a **documentação**, que é a fonte
  de verdade desta peça
- **Manual:** não existe. O passo a passo do recurso é o portal de
  desenvolvedores e as duas folhas de *Aplicativos*
- **Medição:** `consultar-estoque.py` → `chamadas.json`. Toda rota, todo número
  e todo corpo de resposta desta peça foram medidos hoje, contra a loja sandbox
  *BeeFood3 - Manual* (empresa 38311), **pelas duas portas**
- **Formato:** 1080 × 1350 (4:5)
- **Slides:** 6

## Nome de venda × nome do release

O release se chama *Estoque na API Aberta e no MCP*, que é um título de
changelog: ele nomeia os dois lugares onde a coisa apareceu. A primeira frase do
texto diz o nome do produto — *"a BeeFood lançou a **API de Estoque**"* —, e é
esse que a peça usa. O painel reforça: nas duas folhas de *Aplicativos* a linha
nova se chama **Estoque**, e é essa palavra que o lojista vai procurar.

É o mesmo caso da #11, com o sinal trocado: lá o release tinha o nome técnico e
a peça achou o nome de venda; aqui o release tem o nome **composto** e a peça
fica com o curto.

## A terceira peça da família, e o que a separa das outras duas

| Peça | O que ela vende | Quem é o sujeito |
|---|---|---|
| #13 MCP | a **porta**: uma IA conectada ao sistema | a ferramenta de IA |
| #14 API Aberta | a **porta**: o sistema do parceiro falando com o nosso | o sistema do parceiro |
| **#16 API de Estoque** | o que passou a existir **atrás** das duas portas | o estoque da loja |

As duas primeiras venderam encanamento. Esta é a primeira que vende **o que
corre pelo cano**, e a diferença não é retórica: as portas já estavam abertas e
não mudaram, o que mudou foi o que dá para alcançar por elas. Por isso a peça
não repete *como conectar* — isso é assunto da #13 e da #14, as duas publicadas
—, e gasta as seis páginas no que o Estoque faz.

E há uma herança concreta, medida: a #14 fotografou a folha de permissões da
API Aberta e **fechou o quadro em Avaliações**, de propósito, porque as duas
linhas seguintes estavam apagadas, com a etiqueta *Em breve*. Eram
**Entregadores e Estoque**. A #13 descartou as mesmas duas linhas pelo mesmo
motivo, e escreveu no script o porquê. Uma delas saiu do em breve hoje — e é
por isso que nesta peça o recorte é o contrário: ele existe **para** mostrar a
linha que as outras duas tiveram de esconder.

## Em peça de integração, o release é a manchete e a documentação é a fonte

A regra da 39ª rodada, agora pela terceira vez. O que veio de cada fonte:

| Do release | Da documentação e das chamadas |
|---|---|
| que dá para consultar saldos, registrar movimentações, cadastrar insumos e ver o histórico | que são **11 rotas**, **5 delas de escrita**, em dois escopos: `stock:read` e `stock:write` |
| "produtos, complementos e insumos em uma única lista" | que a lista é **uma rota só** (`GET /v1/stock/items`), e que a loja de exemplo tem **362** itens nela: 267 insumos, 64 produtos e 31 complementos |
| "quais insumos estão abaixo do mínimo?" | que essa pergunta é **um filtro** (`stockSituation=low`), e que na loja de exemplo ela devolve **1** item |
| "entradas, saídas e correção do saldo após a contagem" | que as três operações se chamam `add`, `subtract` e `new`, e que **`remove` e `set` não existem** |
| "para vários itens de uma vez" | que o lote responde **uma linha por item**, na ordem do corpo, e que **cada linha é independente: a que falha não desfaz as outras** |
| "períodos de até 6 meses" | que o limite é do **servidor**, e devolve `400 'fromDate'..'toDate' must span at most 6 months` — pedido de propósito e gravado |
| "ative as permissões de Estoque na credencial" | que a folha já mostra a linha **Estoque**, descrita como *Insumos, categorias, itens e movimentações*, e que *Entregadores* é a única que continua *Em breve* |

**O release não diz, e a medição disse:** o grupo Estoque é o **segundo maior**
da API, atrás só do Catálogo. Hoje são 67 rotas de negócio em seis grupos, e 11
delas são de estoque — mais que Pedidos (6), Clientes (2) e Relatórios (5).

## Fato → ângulo → o que o slide diz

| Fato (medido) | Ângulo | Slide |
|---|---|---|
| Uma pergunta em português — *quais insumos estão abaixo do mínimo?* — vira `GET /v1/stock/items?stockSituation=low`, e a loja de exemplo responde: 1 de 19 itens controlados | O dono não quer consultar estoque; ele quer saber **o que vai faltar**. A diferença entre abrir o painel e perguntar é quem faz o trabalho de procurar | Capa |
| As mesmas 11 rotas atendem o MCP e a API Aberta; o escopo é o mesmo (`stock:read`, `stock:write`) | A notícia é dupla e as duas metades têm donos diferentes: a IA é do lojista, o sistema é do fornecedor dele. Ninguém precisa escolher | 2 |
| `GET /v1/stock/items` devolve insumo, produto e complemento **na mesma lista**, com saldo, mínimo e situação | Em sistema de restaurante, insumo e produto quase sempre moram em telas separadas. Uma lista só é o que permite perguntar "o que está acabando" sem dizer de que tipo | 3 |
| `PATCH /v1/stock/items` leva `add`, `subtract` e `new` e aceita várias linhas; cada linha responde `success` por conta própria | Integração de estoque é onde dá erro: a nota chega com trinta itens e um deles não existe mais. Aqui os outros vinte e nove entram | 4 |
| A linha **Estoque** está nas duas folhas de permissão, com *Consultar* e *Alterar* separados | Entregar o estoque a um robô assusta mais que entregar o cardápio: é dinheiro parado. O que desarma é a chave estar do lado de cá | 5 |
| Está em *Aplicativos → MCP* e em *Aplicativos → API Aberta*, nas duas | CTA: não há tela nova para aprender; é uma chave a mais numa folha que já existe | 6 (CTA) |

## Slide a slide

| # | Arquivo | Título | Imagem |
|---|---|---|---|
| 1 | `01-capa.html` | **API de Estoque**: a sua IA responde o que está acabando | `.tela-ia` — **desenho**, com a pergunta e a resposta medidas |
| 2 | `02-duas-portas.html` | Pela sua **IA** ou pelo seu **sistema**: o mesmo estoque | cena de convergência — **desenho** |
| 3 | `03-uma-lista.html` | Insumo, produto e complemento na **mesma lista** | `.requisicao` — **desenho**, com a chamada e a resposta reais |
| 4 | `04-movimentacao.html` | Entrada, saída e contagem — **várias de uma vez** | `.eventos` — **desenho**, as três operações publicadas |
| 5 | `05-permissao.html` | O Estoque é uma chave que **você** liga | `rec-estoque-api.png` + `rec-autorizacao.png` — **captura** |
| 6 | `06-cta.html` | Ligue o Estoque **hoje** | `rec-cartoes.png` — **captura** dos dois cartões de *Aplicativos* |

Lidos em fila, os seis títulos montam o recurso: a IA responde o que está
acabando, as duas portas servem o mesmo estoque, a consulta traz tudo numa
lista, a escrita move vários de uma vez, a permissão é sua, e dá para ligar
hoje. O slide 2 é a exceção da regra do nome — ele explica o que a capa acabou
de nomear.

### A forma antes do conteúdo

A armadilha desta família é conhecida e está escrita na memória: peça de
integração vira quatro blocos escuros iguais, que foi o que derrubou a primeira
versão da #13. O que separa um slide do outro é a **forma**, e aqui ela muda
cinco vezes em seis páginas:

| # | Forma |
|---|---|
| 1 | **conversa** (`.tela-ia`) |
| 2 | **cena** (origem, fio e cartão de destino) |
| 3 | **código** (`.requisicao`, com corpo) |
| 4 | **lista** (`.eventos`, duas colunas) |
| 5 | **captura** |
| 6 | **captura** |

Os dois últimos são captura seguida de captura, e isso é de propósito: depois
de quatro desenhos, as duas páginas que fecham a peça são as duas únicas que o
leitor pode conferir no próprio painel dele. A peça abre no que a IA responde e
fecha no que ele vai clicar.

## A capa

### O molde é *nome + dois-pontos*, e a primeira metade da notícia ganha a página

Placar antes desta peça: afirmação do fato 5, anúncio de chegada 3, pergunta 2,
nome + dois-pontos 2, nome + canal 1, nome + para quem 1, ordem direta 1; antes
× agora continua em 0.

A #15 abriu em **ordem direta** e a capa não repete a forma da anterior, então
esse estava fora de saída. Dos outros, dois foram escritos e caíram:

- **anúncio de chegada** daria *"Chegou a API de Estoque"*, e o molde só se paga
  quando a notícia é que um módulo inteiro chegou — foi assim na #8 e na #12.
  Aqui o módulo de Estoque **já existia** no painel há tempo; o que chegou foi o
  acesso a ele de fora. "Chegou o Estoque" seria falso para quem já usa;
- **antes × agora** tem, pela primeira vez na série, um "antes" documentado e
  que não é produto nosso no lado perdedor: o *Em breve* que a #13 e a #14
  fotografaram. Caiu por outro motivo — esse "antes" é **nosso**, não do leitor.
  Quem lê o feed nunca abriu a folha de permissões para ver a linha apagada, e
  uma capa que começa explicando o que estava escrito numa tela que ele não viu
  gasta a primeira metade da linha com a nossa fila de desenvolvimento.

Sobrou **nome + dois-pontos** (placar 2 → 3). É o molde da #14, e não o da peça
anterior — a regra é sobre a capa que veio antes, e entre as duas há a #15
inteira. Fica:

> **API de Estoque**: a sua IA responde o que está acabando
> E o seu sistema dá entrada e baixa sozinho.

O vermelho pega **API de Estoque** inteiro, porque é o nome; e o sujeito da
segunda metade é **a sua IA**, que é o lado da notícia que pertence a quem lê.

### Por que a capa mostra só uma das duas portas

A notícia tem duas metades e a capa mostra uma. Foi decisão, não falta de
espaço.

As duas metades têm **donos diferentes**: a porta da IA é do lojista — ele
conecta, ele pergunta, ele lê a resposta — e a porta da API é do **fornecedor**
dele, que é quem vai escrever o código. Quem rola o feed do Instagram é o
primeiro. Uma capa que vendesse as duas de uma vez ou viraria diagrama (e
diagrama é o que a #14 já pôs na capa dela), ou viraria título com dois sujeitos.

O que a segunda metade ganha em troca é melhor que meia capa: o subtítulo, que é
lido por quem parou, e o **slide 2 inteiro**.

### A conversa desenhada, e o que dentro dela é medido

Não há como capturar: o resultado acontece dentro do ChatGPT, do Claude, do
Lovable ou do Cursor, que não rodam aqui e não são nossos para fotografar. É o
degrau 2 da escada, e a `.tela-ia` existe para isto desde a #13.

O que a peça escreve é a **forma** da frase. O que está dentro dela é medido, e
saiu do `chamadas.json`:

| Na tela | De onde veio |
|---|---|
| a pergunta | é a do próprio release, palavra por palavra |
| `TOMATE`, `1,5 KG`, mínimo `2 KG` | `GET /v1/stock/items?stockSituation=low` — o único item que a loja devolveu |
| "os outros 18 continuam regulares" | 19 itens com controle ligado menos o 1 abaixo do mínimo |
| a etiqueta `beefood-api` | é o nome que o servidor anuncia no `initialize` |

**O número pequeno é o número certo.** Um item abaixo do mínimo é uma resposta
magra para uma capa, e a tentação era mexer no saldo de dois ou três insumos da
sandbox para a lista ficar mais cheia. Isso seria inventar o fato que a arte
existe para provar — e a resposta curta diz, de graça, uma coisa que uma lista
longa não diria: que a pergunta serve justamente para **não** ter que olhar os
outros dezoito.

## A escrita foi feita, não desenhada

É a lição da #13, e nesta peça ela sai mais barata do que em qualquer outra: o
exemplo que o próprio release dá — *"dê entrada de 20 unidades de
refrigerante"* — é **reversível**, porque a operação `new` grava o saldo
informado no lugar do atual.

O `consultar-estoque.py --escrever` faz o caminho inteiro **pelo MCP**, que é a
porta que a capa vende:

```
saldo antes ............ 23
PATCH /v1/stock/items    [{"type":"product","productId":…,"operation":"add","stockQuantity":20}]
resposta ............... [{"productId":…,"success":true,"stockQuantity":43}]
saldo depois ........... 43
desfeito com `new` 23 .. saldo final 23
```

Está gravado em `chamadas.json`, em *escrita*, com a confirmação de que o saldo
voltou. O que sobra na loja são duas linhas no histórico de movimentações — que
é exatamente o que a rota de histórico existe para registrar, e é sandbox.

**A primeira rodada deixou o saldo errado, e isso virou regra do script.** A
leitura que vem logo depois do `PATCH` é idêntica à que veio antes dele, e a API
devolve `429` para requisição repetida em menos de quatro segundos. O script
quebrou **entre** a entrada e o desfazer, e o saldo ficou em 43. A correção foi
dupla: uma pausa de cinco segundos antes de cada leitura (o limite é publicado
em `docs.beefood.app/docs/limites`, então respeitar é o certo, não contorno) e
um `--restaurar` que devolve o saldo sozinho. Demonstração reversível precisa de
**duas** saídas: a que desfaz no caminho feliz e a que desfaz depois do erro.

## O que ficou de fora, e por quê

- **o histórico de movimentações.** É um dos quatro pontos do release, a rota
  existe e foi medida (555 movimentações na janela de seis meses, com saldo
  anterior e delta por linha). Caiu por **forma**: ele seria uma lista, e o
  slide 4 já é a lista. Um sétimo slide com a mesma forma do quarto é o defeito
  que a memória chama de quatro blocos escuros iguais. O fato virou uma linha no
  corpo do slide 4 e um parágrafo na legenda;
- **o limite de seis meses**, que foi medido de propósito pedindo 200 dias e
  guardando o `400`. É um limite, e limite antes do CTA é a fatura antes da
  venda. Vai na legenda, que é por onde o suporte responde;
- **o cadastro de insumo por categoria, com unidade e custo.** É o quarto ponto
  do release e o mais fraco para quem lê: cadastrar insumo já dá para fazer no
  painel, e o ganho de fazer pela API só existe para quem está migrando de
  sistema. Uma linha na legenda. Vale dizer que a loja de exemplo tem **uma**
  categoria cadastrada — mais um número que seria magro na arte;
- **os filtros da consulta.** A rota aceita treze parâmetros, de `sectorId` a
  `stockQuantityOperator`. É o que faz a integração ser boa e é vocabulário de
  quem programa. O slide 3 mostra **um** filtro, que é o da pergunta da capa;
- **o `userId` de quem moveu**, que vem em toda movimentação. O repositório é
  público e o campo não acrescenta nada ao argumento;
- **a comparação com os outros grupos.** O Estoque ser o segundo maior da API é
  um fato bonito e é **interno**: o leitor não tem como saber que 11 rotas é
  muito ou pouco. Fica no roteiro e na nota de produção;
- **o nome da loja de exemplo.** Nenhuma arte desta peça mostra a loja: o que
  aparece é resposta de API, e o `tradeName` não entra em nenhum corpo mostrado.

## Decisões de arte

### O slide 2 é cena, e por que não é o `.fluxo-api`

A tentação era reusar a peça da capa da #14: dois lados olhando para um núcleo.
Ela não serve aqui, por desenho e por sentido.

Por desenho: o `.fluxo-api` é **entradas → núcleo → saídas**, e é a saída que
justifica os dois lados. O Estoque não tem webhook: nada sai sozinho. Montar o
lado direito com qualquer coisa seria preencher uma forma que o fato não tem.

Por sentido: aqui as duas coisas da esquerda não são dois sistemas quaisquer —
são **as duas portas**, e o que o slide afirma é que elas chegam no mesmo lugar.
Isso é convergência, e para convergência a prateleira já tem a cena de
`.origem` + `.fio`, com o destino numa barra larga. A regra da #13 vale: para
duas linhas caindo numa barra que atravessa o slide, o fio desce **reto**.

### Dois recortes no slide 5, um de cada folha

O slide afirma que a chave existe nas duas portas, então ele mostra as duas: a
linha **Estoque** do formulário de credencial (*Aplicativos → API Aberta*, com
*Consultar* e *Alterar*) e a linha **Estoque** da tabela de autorização do MCP
(com LEITURA e ESCRITA marcadas).

A segunda só existe **dentro do fluxo de autorização** — não há rota no painel
que abra aquela tela —, então ela é capturada no meio do caminho, pelo
`--retrato` do `consultar-estoque.py`. É a técnica que a #13 inventou, e aqui
ela é usada para fotografar exatamente a linha que a #13 teve de deixar de fora.

Os dois recortes são **faixa contínua** da tela de origem, nunca montagem: o da
autorização começa no cabeçalho (`PERMISSÃO | LEITURA | ESCRITA`), porque sem
ele os dois tiques não têm nome.

### O CTA fotografa os dois cartões

A #14 fechou com o cartão da API Aberta na grade de *Aplicativos*, pela razão
que a #13 deixou escrita: a última página é a que fica, e ela tem de mostrar o
que o leitor vai procurar. Aqui são **dois** cartões, porque são duas portas, e
é a última chance de a peça não deixar metade da notícia para trás.

### O jogo de números

Quatro, e todos vêm de fora de nós:

| Número | De onde |
|---|---|
| **11** rotas, **5** de escrita | `listar_endpoints` do servidor de documentação |
| **362** itens — 267 insumos, 64 produtos, 31 complementos | `GET /v1/stock/items`, por tipo |
| **1** abaixo do mínimo, de **19** controlados | `GET /v1/stock/items?stockSituation=low` |
| **20** unidades de entrada, 23 → 43 → 23 | `PATCH /v1/stock/items`, feito e desfeito |

Nenhum número de resultado comercial aparece: não há tela que mostre quanto o
controle de estoque economizou, e prometer isso seria prometer relatório.

## O sandbox voltou como estava

A única escrita desta peça é a entrada de 20 unidades, desfeita no mesmo
arranque e conferida por leitura. Nenhuma permissão foi alterada: a linha
**Estoque** já estava ligada na credencial quando a folha foi aberta, e a tela
de autorização do MCP já vinha com as caixas marcadas. A credencial de produção
fica em `/tmp` e **não** entra no repositório.
