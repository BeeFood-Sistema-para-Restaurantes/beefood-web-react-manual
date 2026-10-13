# MCP: a loja dentro da IA

- **Gênero:** novidade
- **Fonte:** [MCP: converse com o seu restaurante usando IA 🤖](https://beefood.app/novidades/mcp-inteligencia-artificial)
  — 13/10/2026, áreas Aplicativos e Sistema, aplicativo BeeFood App.
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

## O acervo, antes de escrever

Doze peças entregues, e **nenhuma** toca este assunto. Não há, em
`carrosseis/*/imagens-puras/`, uma só tela de integração, de API ou de
ferramenta externa: as doze anteriores vendem módulo de dentro do sistema, e
esta vende uma **porta para fora** dele. Nenhuma imagem foi reaproveitada, e
nenhuma técnica de captura serviu direto — esta é a primeira peça da série em
que a prova não estava em tela nenhuma antes de alguém ir buscá-la.

**A capa não repete a forma da anterior.** A #12 usou *anúncio de chegada*.
Aqui o molde é **afirmação do fato**, que é o mais gasto do acervo (cinco usos
em doze peças) e ainda assim o certo: a notícia é grande por si — o sistema do
restaurante passou a ser alcançável por uma IA —, e não precisa de nenhuma
armação para ser interessante. Placar depois desta peça: afirmação do fato
**6**, pergunta 2, anúncio de chegada 2, nome + canal 1, nome + dois-pontos 1,
nome + para quem 1; ordem direta e antes × agora continuam em 0.

Os dois moldes zerados foram escritos e caíram, e vale registrar por quê:

- **ordem direta** daria *"Pergunte ao ChatGPT quanto a sua loja vendeu"*, e
  ela só se paga quando o recurso tem **um objeto**. Este responde sobre
  vendas, pedidos **e** cardápio, e a capa escolheria um dos três — é a mesma
  conta do "concisão corta palavra, nunca eixo" da #12, pelo outro lado;
- **antes × agora** pediria um "antes" em que consultar o resultado era
  difícil. Quem consulta resultado hoje é o nosso próprio **Desempenho**, e a
  primeira metade do título falaria mal de um módulo que a BeeFood vende e
  continua vendendo. É literalmente o erro que a #12 evitou com o cashback.

## O fato, o ângulo, e o que o slide diz

| Fato (release + painel + servidor) | Ângulo | O que vira slide |
|---|---|---|
| Com o **MCP** você conecta a sua conta ao **ChatGPT**, **Claude**, **Lovable**, **Cursor** e outras ferramentas compatíveis | O sistema do restaurante passa a ser alcançável por uma IA. A capa afirma o fato e o subtítulo diz o que se pergunta | Capa |
| Passa a **conversar com os seus dados direto do chat da IA** | A resposta não sai de uma tela nossa: ela chega onde o leitor já está digitando | Capa (arte) e 2 |
| O MCP é um **padrão** de conexão entre IA e sistema | Uma frase, e acabou: quem lê não precisa saber o que é um protocolo para entender o que ganhou | 2 (corpo) |
| A IA passa a acessar o restaurante **com a autorização da sua conta** | É a resposta de "então qualquer um lê a minha loja?", e é o único dos três passos do release que muda o que o leitor passa a ter | 2 (corpo e cena) |
| Dá para **perguntar como foram as vendas** sem abrir o painel | Prova: o valor total e o ticket médio que a IA respondeu são os que o Desempenho fecha | 3 |
| Dá para **acompanhar pedidos** | A mesma pergunta se abre em recorte — sete canais de venda, cada um com pedidos e valor, fechando no total do slide 3 | 4 |
| Dá para **consultar o cardápio** | O conector enxerga o cadastro, e não só o dinheiro: produto, setor e o que girou no período | 5 |
| No mesmo painel existem **manuais passo a passo** para conectar ao ChatGPT e ao Claude | Tira o medo de não saber fazer, e cabe numa linha do subtítulo do CTA | 6 (CTA) |
| O recurso mora em **Aplicativos → MCP** | CTA: o que se pede não é a conexão, é a **primeira pergunta** | 6 (CTA) |

Nove linhas de fato para seis lugares.

**Ficou de fora, de propósito:**

- **os três passos de conexão** (copiar o link, colar na configuração de
  conectores, autorizar). É o miolo do release e é **trabalho**: slide que
  ensina a ligar o recurso é manual, e o CTA que termina em tarefa é a fatura
  antes da venda. Sobrou a parte que muda o que o leitor tem — a autorização da
  conta — e o resto virou uma linha no subtítulo do CTA;
- **o campo *Link do MCP*, o botão de copiar e a lista de manuais.** São a
  folha de configuração do recurso, e configuração não é imagem de carrossel.
  Nem capturada, nem desenhada;
- **os 61 endpoints em cinco grupos** (Catálogo 33, Restaurante 15, Pedidos 6,
  Relatórios 5, Clientes 2). É o número mais impressionante que o servidor
  devolve e não diz nada a quem vende comida: ninguém compra sistema por
  quantidade de endpoint. O que ele vira na peça são os quatro assuntos do
  cartão do slide 2 — vendas, pedidos, cardápio e relatórios;
- **as seis ferramentas do servidor** (`search_beefood_api`,
  `listar_endpoints`, `detalhe_endpoint`, `execute_beefood_request`,
  `query_docs_filesystem_beefood_api`, `submit_feedback`). Mesma conta: é
  arquitetura, e o leitor compra resultado;
- **a API aberta**, que saiu no mesmo dia
  ([`api-aberta-liberada`](https://beefood.app/novidades/api-aberta-liberada),
  seq 121). É release irmão e peça própria: uma fala com quem programa, a outra
  com quem pergunta. Misturar as duas entregaria um carrossel que não sabe com
  quem está falando;
- **o relatório *Desempenho → Vendas → Origem***, que parece o par do slide 4 e
  não é. Está explicado em *o painel reparte de outro jeito*, abaixo.

## Slide a slide

| # | Arquivo | Título | Imagem |
|---|---|---|---|
| 1 | `01-capa.html` | O **MCP** põe a sua loja dentro da sua IA | conversa **desenhada** (`.tela-ia`), com o resumo dos 30 dias |
| 2 | `02-como-funciona.html` | Você pergunta na sua IA, e a resposta vem do seu BeeFood | cena de convergência com os cinco quadrados da folha do MCP — **captura**, cinco recortes |
| 3 | `03-confere-com-o-painel.html` | **Desempenho**: a IA responde o mesmo que o painel mostra | bloco da conversa **desenhado** + `rec-desempenho.png` — **captura**, recorte |
| 4 | `04-canais-de-venda.html` | **Canais de venda**: quanto cada um trouxe no período | conversa **desenhada**, com os sete canais e o total |
| 5 | `05-cardapio.html` | **Cardápio**: quantos produtos e quais setores você tem | conversa **desenhada**, com a resposta em prosa |
| 6 | `06-cta.html` | Faça **hoje** a primeira pergunta ao seu BeeFood | `rec-cartao-mcp.png` — **captura**, recorte |

Lidos em fila, os seis títulos montam a lista do que o recurso passou a fazer:
responder sobre desempenho, repartir por canal de venda e falar do cardápio. O
slide 2 é a exceção estrutural da regra do nome — ele explica o recurso que a
capa acabou de nomear, e por isso é o único título sem nome antes dos
dois-pontos.

## Decisões de arte

### A tela desenhada, e por que ela é a prova

Esta é a primeira peça da série em que **a maior parte das imagens é desenho**,
e isso precisa de uma defesa, porque a regra da casa é o contrário.

O resultado do MCP **não mora em tela nenhuma da BeeFood**. Ele acontece dentro
do ChatGPT, do Claude, do Lovable ou do Cursor — que não rodam neste ambiente e
não são nossos para fotografar. Na escada de imagem da skill, isso é o degrau
2: *tela de resultado desenhada pela peça*, que existe justamente para o caso
em que o degrau de cima não existe.

O que o desenho **não** faz é imitar nenhum daqueles quatro aplicativos. Copiar
a interface de um deles diria "é no ChatGPT", e o recurso é de todos; e
desenhar marca de terceiro é afirmar coisa que não é nossa. A paleta da
`.tela-ia` é a do **painel do MCP** (`mcp-panel.css`): fundo quase preto,
cartão grafite, texto branco, apoio cinza-azulado e o fio arco-íris que o
painel usa na borda do botão e do campo do link. Quem conhece a folha de
*Aplicativos → MCP* reconhece a cena, e ela fecha no slide 6, onde a mesma
assinatura aparece **fotografada**, na borda do cartão da grade.

E o desenho não inventa o que importa:

| O que é desenho | O que é medido |
|---|---|
| o cartão, o fio, a bolha da pergunta, a caixa de escrever | o nome do conector (`beefood-api`), que é o que o servidor anuncia no `initialize` |
| a frase de resposta, em volta dos números | **todos os números**, que são o que o servidor respondeu para a conta sandbox |
| as perguntas | os rótulos de canal (`Manual`, `Cardápio Digital`, `Externo`, `iFood`, `99Food`, `Totem`, `Keeta`), que vêm do agrupamento por `salesChannel` |

Os números estão em [`conversas.json`](conversas.json), e quem os buscou é o
[`consultar-mcp.py`](consultar-mcp.py) — que faz o OAuth inteiro (registro
dinâmico, autorização no navegador com a conta de teste, PKCE) e conversa com
`https://docs.beefood.app/mcp` pelo protocolo, como qualquer IA conversaria.
Não é uma chamada de API por dentro: é o mesmo caminho que o recurso oferece ao
cliente.

### Os cinco quadrados são captura, e não desenho de marca

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

### A cena desce reta, e o visto quer dizer "autorizado"

É a gramática da capa de dark kitchen (`.origem` / `.fio` / `.selo-ok`), com
duas diferenças:

- **os fios descem retos**, e não em curva. Curva serve para juntar três linhas
  num ponto; aqui embaixo há uma coisa só e ela é **larga** — quatro linhas
  entrando numa barra pedem reta, e curva vira enfeite;
- **o visto não é "deu certo", é "autorizado"**. É o que a frase do corpo
  promete, desenhado no lugar onde acontece.

Uma medida que custou uma rodada: o fio tem **140 px para 54 de selo**. A
primeira versão tinha 76, e sobravam 11 px de tracejado de cada lado do selo —
quatro bolinhas penduradas no nome não desenham caminho nenhum.

### O painel reparte de outro jeito, e por isso o slide 4 não empresta o nome dele

O painel tem *Desempenho → Vendas → Origem*, que parece ser o par da pergunta
do slide 4. Não é: ele agrupa por **tipo de atendimento** (Delivery, Mesas,
PDV, Cardápio Digital, iFood, 99Food, Keeta), e a API agrupa por **canal de
venda**, onde balcão, mesa e PDV caem todos em `MANUAL`. As duas contas somam o
mesmo total e repartem diferente — a própria tela dá Delivery com R$ 7.431,87
na lista e R$ 10.330,37 no pódio logo abaixo, porque nem ela usa um corte só.

Isso decidiu três coisas:

1. **a captura daquela tela saiu da peça.** Pôr a lista do chat ao lado dela
   seria oferecer ao leitor duas contas que não fecham entre si, e a peça
   inteira se apoia em fechar;
2. **o título do slide 4 não diz "Vendas por Origem".** Emprestar o nome do
   relatório mandaria o leitor conferir numa tela que diz outra coisa. O
   vermelho pega *Canais de venda*, que é o nome do **corte**, e não de uma tela
   — nesta peça não há tela para o leitor procurar no menu;
3. **a prova ficou onde ela fecha:** valor total e ticket médio, que são iguais
   nos dois lugares, no slide 3.

`Manual` fica na tabela como o servidor devolveu. Traduzir o rótulo para
"balcão" dentro da resposta seria reescrevê-la, e ele é vocabulário do produto
— o painel chama de *Delivery Manual* o pedido que a equipe lança no sistema.
Quem explica isso é a legenda do post.

### Um jogo de números, e ele foi defendido em código

A loja de demonstração **recebe pedido enquanto a peça é feita**. Entre uma
rodada e a seguinte o total subiu de R$ 13.473,52 para 13.518,52, depois
13.563,52 e depois 13.698,52, em poucos minutos. Isso não é detalhe de
execução: é o que decide se a peça tem **um** jogo de números ou dois, e a
única captura de dado dela existe justamente para dizer que o número da
conversa é o do painel.

Por isso a conferência não é do olho. O
[`capturar-telas.py`](capturar-telas.py) lê o `conversas.json`, compara com o
que acabou de fotografar e **estoura** se os dois divergirem:

```
painel: R$ 13.698,52 | R$ 54,14    conversa: R$ 13.698,52 | R$ 54,14
--> painel e conversa fecham no mesmo número
```

E os dois fecham porque a janela perguntada ao MCP (`2026-09-13` a
`2026-10-13`) é a que a tela abre sozinha: *Últimos 30 dias (31 dias)*. A
sequência correta é rodar o `consultar-mcp.py` e o `capturar-telas.py
desempenho` em seguida, no mesmo minuto.

As somas também fecham entre si: os sete canais somam 253 pedidos e
R$ 13.698,52, que é o resumo do slide 3. O `consultar-mcp.py` verifica isso e
grava o resultado em `asSomasFecham`.

### Dois recortes, e por que cada um fecha onde fecha

Medidos no DOM pela própria captura ([`medidas.json`](medidas.json)), nunca
estimados na miniatura.

- **`rec-desempenho.png`** começa na linha *Últimos 30 dias* — e não no seletor
  acima dela, onde moram as datas, porque data na arte faz o post nascer velho.
  Fecha no **pé do número**, com folga de 4 px: a linha seguinte do painel é
  *+131,3% vs período anterior*, que é verdade da loja de demonstração e, numa
  peça de venda, lê como crescimento prometido pelo produto. É a lição da #9,
  que cortou o *R$ 0,00 de receita gerada* pelo mesmo motivo, do outro lado.
  Encostar no pé do número foi o que deixou a linha verde inteira de fora: 16 px
  de sobra traziam a metade de cima dela, e linha cortada ao meio lê como erro
  de render. À direita o quadro fecha no **cartão**, e não no rótulo: ancorado
  no texto ele saía com 693 px e cortava o cartão do ticket ao meio.
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

### O CTA não repete a arte da capa

É a primeira vez na série em que isso acontece, e a skill permite as duas
coisas — a repetição é aprovada, não obrigatória.

A capa e mais três slides já somam quatro cartões escuros de conversa; um
quinto fecharia a peça com a imagem mais vista dela. O que entra no lugar serve
melhor ao que o slide pede: o último slide manda abrir *Aplicativos → MCP*, e
o cartão fotografado mostra exatamente o que o leitor vai ver quando chegar lá.

Ele é o limite da regra de "nada de tela de configuração", e fica do lado de
dentro: o que aparece não é campo, interruptor nem lista de parâmetros, é a
**porta** — um cartão de navegação com o nome do recurso. A folha que está atrás
dele, essa sim, não entrou em nenhum slide.

### O ícone do cartão MCP é o mesmo do Lovable, e isso é do painel

Quem olhar o slide 6 ao lado do slide 2 vai achar que a arte trocou os
logotipos: o quadrado do cartão *MCP* é, pixel por pixel, a marca que o slide 2
usa para o **Lovable**. Não é engano da peça — é o ícone que o painel dá hoje ao
cartão, e o recorte é captura pura da folha de *Aplicativos*.

Não se conserta na arte. Trocar o ícone do cartão seria desenhar por cima de uma
captura, e aí ela deixa de ser prova; o leitor que chegar em *Aplicativos → MCP*
precisa encontrar o quadrado que viu no post. Se o painel trocar o ícone, a
captura se refaz. Fica anotado aqui e na nota de publicação para o revisor não
"corrigir" o que está certo.

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

### A capa perdeu o aparelho, e o slide 5 perdeu a promessa de preço

Duas correções que vieram da revisão, e as duas valem para a próxima peça.

A arte da capa é prova de **leitura** — a graça dela é que dá para ler os três
números. Por isso ela entra margem a margem, sem moldura de celular: com o
aparelho em volta, a mesma lista chegaria ao feed com metade da altura de
letra. É a regra 1a da skill, aplicada antes de alguém reclamar.

E o título do slide 5 prometia *"produto, setor e preço"*. A API devolve o
preço de cada produto, então a frase era verdadeira — mas a resposta daquele
cartão fala de **quantidade**, e título que promete um dado que a imagem ao
lado não mostra é exatamente o furo que esta peça inteira existe para não ter.
O chapéu caiu junto: *"E não é só venda"* brigava com a própria resposta, que
termina em *"70 deles tiveram venda"*.

### Nenhum dado de cliente em imagem nenhuma

Não há o que borrar nesta peça, e isso é consequência do assunto. Tudo que
entrou é agregado — resumo, canais, contagem de cardápio — e nenhuma consulta
pediu nome, telefone ou endereço de quem compra. O `token` de sessão do
`iframe` do Desempenho viaja na URL do quadro, e não aparece em pixel nenhum.

O `access_token` do OAuth fica em `/tmp/beefood-mcp-token.json`, **fora do
repositório**. As credenciais da conta sandbox seguem versionadas, pela regra da
casa: o ambiente é descartável.
