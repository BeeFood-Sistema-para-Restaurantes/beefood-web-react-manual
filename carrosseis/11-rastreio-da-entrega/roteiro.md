# Acompanhamento em tempo real, pelo cliente

- **Nome de venda × nome do release:** a peça vende **acompanhamento em tempo
  real**. O release se chama *"rastreio da entrega pelo cliente"*, que é o nome
  escrito do lado de quem construiu; os dois são o mesmo recurso, e o segundo
  fica registrado aqui e no `copy-instagram.txt` porque é por ele que quem leu a
  publicação vai perguntar. O caso está na skill, em *o décimo vício*.
- **Gênero:** novidade
- **Fonte:** [Gestão de Entregas: rastreio da entrega pelo
  cliente](https://beefood.app/novidades/gestao-entregas-rastreio-pelo-cliente)
  — 23/09/2026, áreas Delivery e Cardápio Digital. O fato duro está no
  [manual](../../manuais/gestao-entregas-rastreio-cliente/gestao-entregas-rastreio-cliente.md)
  e no [estudo de
  código](../../manuais/gestao-entregas-rastreio-cliente/fluxo-codigo.md), que leu
  a tela no bundle publicado do cardápio digital.
- **Manuais vizinhos que entram como fonte:**
  [avisos de WhatsApp](../../manuais/gestao-entregas-avisos-whatsapp/gestao-entregas-avisos-whatsapp.md)
  (a mensagem que carrega o link),
  [despachar a rota](../../manuais/gestao-entregas-despachar/gestao-entregas-despachar.md)
  (o clique que manda o link) e
  [liberar o entregador](../../manuais/gestao-entregas-liberar-entregador/gestao-entregas-liberar-entregador.md)
  (o cadastro de onde sai o nome que aparece na tela).
- **Formato:** 1080 × 1350 (4:5)
- **Slides:** 7

## O acervo, antes de escrever

A peça irmã é a **#10, Gestão de Entregas** — mesma família, publicada logo
antes. Ela vende o **painel**: o mapa das rotas, o despacho, o app do entregador
e os dois relatórios. O leitor dela sai sabendo o que a **loja** passa a fazer.

Esta peça vende o outro lado do mesmo despacho: **o que chega no celular de quem
pediu**. Nenhuma tela é a mesma, e nenhum argumento se repete.

A fronteira entre as duas tem um ponto de encosto, e ele foi tratado de
propósito:

| Onde encosta | #10 | #11 |
|---|---|---|
| WhatsApp | slide 6, *Avisos no WhatsApp: dois telefonemas a menos* — os **quatro** avisos de fábrica, três para o entregador e um para quem espera | slide 2, e o assunto é **um bloco dentro de um** deles: o link que o sistema anexa ao aviso de saída |
| Mapa | o mapa **da loja**, com rotas, paradas numeradas e motoboys — operado sentado, num notebook | o mapa **de quem pediu**, com três pinos e uma moto — aberto em pé, no celular |

O que se reusou do acervo foi **método**, em dois pontos:

- a **interceptação da resposta da API** (do totem, do tablet, da #8 e da #10):
  aqui ela devolve um rastreio montado e quem desenha a tela é o cardápio digital
  de produção, com o mapa Leaflet de verdade, o pino da logo, a moto pulsando e
  a barra de etapas;
- a **conversa de WhatsApp desenhada** (da #10): não há número conectado na
  sandbox, e o texto das mensagens é o de fábrica, com os marcadores trocados
  pelos dados da cena.

O que **não** se reusou: nenhuma imagem, e nenhum print do manual. As sete
capturas do manual são de um pedido real feito em `menu.beefood.com.br/beefood3`
— loja de teste chamada *BeeFood3 - Manual*, com logotipo de placeholder. Elas
são referência de leitura da tela e não entram na arte, como manda a skill.

**Erro documentado da #10 que esta peça herdou pronto:** *"nossos carrosséis
ficam só com imagem de configuração de campos"*. Aqui não havia esse risco pelo
lado bom — **este recurso não tem tela de configuração nenhuma**, porque não há
o que configurar. Todas as imagens são resultado.

## O fato, o ângulo, e o que o slide diz

| Fato (novidade + manual) | Ângulo | O que vira slide |
|---|---|---|
| Quando o pedido sai com um motoboy de GPS ligado, o cliente recebe no WhatsApp um link que abre um **mapa ao vivo** | A capa anuncia: o nome no título, o que ele faz no subtítulo | Capa |
| O link é **anexado ao aviso de *saiu para entrega* que a loja já mandava** — nenhum campo novo, nenhuma tela nova, nenhuma cobrança por mensagem | O melhor argumento do recurso é que ele não pede trabalho nenhum | 2 |
| O texto da mensagem continua sendo o da loja (WhatsApp → Notificações); o que o sistema acrescenta é o bloco **Acompanhe a entrega** e o endereço terminado num código de 22 caracteres | Quem reescreveu a mensagem não perde a versão dele | 2 |
| **Todo pedido de entrega em andamento** mostra o mesmo acompanhamento em *Pedidos*, dentro do Cardápio Digital | Quem apagou a conversa ou trocou de celular não fica sem | 2 (corpo) e 6 |
| A tela diz o **primeiro nome** do entregador (*"Diego está indo até você"*) e a **distância em linha reta**, arredondada de dez em dez metros | É a resposta pronta para *"quanto tempo falta?"*, e ela é verdadeira | 3 |
| A tela **se atualiza sozinha**: o servidor manda o intervalo e o front nunca consulta em menos de 5 segundos — a moto se mexe algumas vezes por minuto | Ninguém puxa, ninguém recarrega, e não existe botão de atualizar | 3 |
| O cartão do entregador diz **quando aquela posição foi capturada** (*Posição atualizada agora*, *Posição de 3 min atrás*) | Fica na imagem, na linha do cartão, sem virar título | 3 (imagem) |
| A barra tem **quatro etapas** — enviado, em preparo, pronto aguardando o entregador, saiu para entrega — e a atual pisca | Uma olhada responde "onde está", sem ninguém perguntar | 4 |
| O texto muda com a situação: *Seu pedido está sendo preparado*, *Você é a 2ª de 3 paradas desta viagem.*, *Pedido entregue às 20:12* | A reclamação "a moto está indo pro lado contrário" já vem respondida na tela | 4 |
| O pino da loja é a **logo da loja** (o mesmo arquivo do cardápio); se ela não carregar, entra um ícone genérico | Rastreio no mapa é o que as plataformas grandes ensinaram o país a esperar — aqui ele sai com a marca do restaurante | 5 |
| A página não leva marca da BeeFood: cabeçalho, pinos e folha são da loja | White label sem ninguém pedir | 5 |
| **É a mesma página e o mesmo link** no celular e no computador; no computador ela vira duas colunas, com o mapa à direita | Não há "versão para PC" para manter nem divulgar | 6 |
| **Não há nada para configurar**: o recurso é automático, e depende de coisas que já existem na operação | CTA: o primeiro passo é despachar a próxima rota | 7 (CTA) |

**Ficou de fora, de propósito:**

- **as quatro condições da seção *Antes de começar*** (app aberto com GPS, nome
  de gente no cadastro, endereço com coordenada, notificação ligada): são
  pré-requisito, e pré-requisito antes do CTA é a fatura antes da venda. Uma
  delas — o aplicativo aberto com GPS — aparece na legenda do post, que é onde
  quem publica responde a pergunta se ela vier;
- **o link expira duas horas depois da entrega**, o `noindex` e os 22 caracteres
  do código: é a parte de privacidade, e ela é boa — mas escrita no slide vira
  aviso de risco justamente onde o leitor está decidindo. Foi para a legenda;
- **"a tela não diz chega em 8 minutos"**: é a decisão de produto mais elegante
  do recurso e é, na forma, um **limite**. O que sobrou dela no slide 3 é a
  parte afirmativa — a distância é verdadeira;
- **o que acontece quando o sinal cai** (*Localização indisponível no
  momento.*): mesma razão. Está na tabela do manual, para quem atende;
- **o cartão de avaliação do pedido concluído**: é outro recurso, e puxá-lo aqui
  abriria um assunto que a peça não fecha.

## Slide a slide

| # | Arquivo | Título | Imagem |
|---|---|---|---|
| 1 | `01-capa.html` | Acompanhamento **em tempo real**, pelo seu cliente | `cel-a-caminho.png` num `.celular` sangrando pela base — **captura** |
| 2 | `02-o-link-vai-junto.html` | O link entra **sozinho** na mensagem que a sua loja já manda | `zap-rastreio.png` — **desenho** da conversa, com `.realce` no bloco que o sistema anexa |
| 3 | `03-mapa-ao-vivo.html` | **Mapa ao vivo**: quem está levando e quanto falta | `recorte-cabecalho.png` + `recorte-cartao.png` — **captura**, dois recortes |
| 4 | `04-barra-de-etapas.html` | **Barra de etapas**: onde o pedido está, sem ninguém perguntar | `recorte-preparo.png`, `recorte-fila.png`, `recorte-entregue.png` — **captura**, três recortes |
| 5 | `05-pino-da-loja.html` | **Pino da loja**: a sua logo no meio do mapa | `recorte-mapa.png` — **captura**, recorte fechado |
| 6 | `06-no-computador.html` | **Uma página só**: o mesmo endereço, em qualquer aparelho | `pc-a-caminho.png` num `.notebook` — **captura** |
| 7 | `07-cta.html` | Despache a próxima rota **hoje** | `cel-a-caminho.png` no mesmo `.celular` da capa — a peça abre e fecha na mesma cena |

Lidos em fila, os sete títulos montam a lista do que o módulo passou a fazer, e
nenhum deles tem pronome. O slide 2 é a exceção estrutural da regra do nome: ele
explica o recurso que a capa acabou de nomear, então o título ali é a explicação.

## Decisões de arte

### A tela do cliente é captura, e isso não era óbvio

Esta é a primeira peça em que a **tela do cliente** entra capturada. Nas
anteriores, resultado que mora fora do painel virava desenho: o app do
entregador é Android, o cupom sai na impressora, o relatório não tem volume.
Aqui o resultado mora numa **página pública do cardápio digital**, e ela aceita
a mesma interceptação que o totem e o tablet já usavam:

```python
ctx.route("**/tempresaDelivery/rastreio/**",
          lambda r: r.fulfill(status=200, content_type="application/json",
                              body=json.dumps(RASTREIO)))
pag.goto("https://menu.beefood.com.br/oneburger/rastreio/<token>")
```

Quem desenha é o cardápio de produção. O que sai da captura é o **Leaflet de
verdade** com a camada da ArcGIS, o pino da logo, a moto com o anel pulsando, o
traço pontilhado da distância e a barra de quatro etapas — nada disso é CSS
nosso. O formato da resposta saiu do
[`fluxo-codigo.md`](../../manuais/gestao-entregas-rastreio-cliente/fluxo-codigo.md),
lido no bundle publicado; formato adivinhado devolve tela em branco.

Isso muda o degrau da peça inteira: **seis das sete imagens são captura**, e a
única desenhada é a conversa de WhatsApp, pelo motivo de sempre (não há número
conectado na sandbox).

### O achado: o link do WhatsApp abre a tela SEM a cor da loja

O manual afirma, a partir do código, que o pino da loja e a moto saem na
`--v-corPrimariaEmp`, *"a cor primária do seu cardápio"*. Na captura pelo link
eles saem **verdes**, e não é defeito da captura — é o que todo cliente vê.

A causa está a um `getComputedStyle` de distância, e foi medida nas duas lojas:

| Onde | `--v-corPrimariaEmp` | `--v-corPrimariaEmp-base` |
|---|---|---|
| `/oneburger/` (layout padrão) | `#C52E1D`, **inline no `.v-application`** | `#c52e1d` |
| `/oneburger/rastreio/<token>` (layout `_rastreio`) | vazio | `#ef3f37`, o tema padrão |

O CSS do rastreio pede `var(--v-corPrimariaEmp, #4caf50)` — **sem** o sufixo
`-base` que o Vuetify escreve no `:root`. Quem preenche a variável sem sufixo é
o layout padrão do cardápio, num `style` inline; o layout do rastreio não a
preenche, então vale o fallback verde. As capturas vermelhas do manual são da
tela cheia aberta **de dentro do cardápio**, onde o tema já estava carregado.

Duas consequências para a peça, e as duas são de honestidade:

- **a arte mostra o verde**, porque é o que o link do WhatsApp abre. Injetar a
  cor da loja no navegador da captura seria fotografar um comportamento que o
  produto não tem nesse caminho;
- **o slide 5 afirma só a logo.** *"A sua marca no mapa"* vira *"o pino da loja é
  a sua logo"*, que é o que a captura prova. A cor ficou de fora.

### A cena, e o que nela é real

A loja é o **cardápio modelo da casa**, `menu.beefood.com.br/oneburger` (ONE
STAND HAMBURGUERIA) — o mesmo da #3. Não é loja de cliente, e é por isso que a
logo pode aparecer no pino: exemplo montado embaixo de marca de cliente leria
como promoção anunciada por ele.

| Item | Valor | De onde vem |
|---|---|---|
| Loja | ONE STAND HAMBURGUERIA, `-23.7345933, -46.6889459` | coordenada e logo reais do cardápio modelo |
| Destino | Rua Luis Reis Santos, 320 — Cidade Dutra, `-23.7285933, -46.6849459` | rua real, conferida no Nominatim, a 782 m da loja |
| Entregador | Diego, `-23.7318, -46.6871` (Rua Idalísio Soares Aranha Filho) | rua real entre a loja e o destino |
| Distância exibida | **420 m** | calculada da posição da moto até o destino, e arredondada pelo próprio front |
| Pedido | nº 42, interno 1188 | exemplo |
| Entrega concluída | 20:12 | exemplo |

**A distância não foi escolhida, foi medida.** `distanciaMetros` é o que o
servidor calcularia entre os dois pontos da cena, então o número do texto
concorda com o lugar dos pinos no mapa. É a regra do *um jogo de números, com as
somas fechando* aplicada a geografia: um pino a meio quarteirão do destino com
"A 1,2 km de você" escrito ao lado desmentiria a imagem.

O entregador se chama **Diego** de propósito: é o mesmo primeiro nome do
entregador da rota A da #10. As duas peças são do mesmo módulo, e quem vê as
duas encontra a mesma pessoa dos dois lados do despacho.

Nada é gravado em servidor nenhum. A única escrita é a resposta de
`GET .../tempresaDelivery/rastreio/{token}`, trocada dentro do Chromium da
captura. O `cena.json` registra linha por linha, e `--cru` mostra o que o
endereço responde hoje (`{"encontrado": false}`, HTTP 404 — o token é sorteado e
não existe).

### Por que a conversa de WhatsApp é desenhada

Mesmo motivo da #10: **não há número conectado na sandbox**, então a mensagem
não tem como ser fotografada. O texto não foi escrito à mão — o corpo do aviso é
o de fábrica de *Pedido saiu para entrega*, do
[manual dos avisos](../../manuais/gestao-entregas-avisos-whatsapp/gestao-entregas-avisos-whatsapp.md),
com os marcadores trocados pelos dados da cena; o bloco `🏍️ Acompanhe a
entrega` e a linha do endereço são o que o sistema acrescenta.

O desenho é **novo**, e não uma cópia do `zap-avisos.html` da #10: lá são duas
conversas lado a lado (entregador e cliente) com quatro avisos; aqui é **uma**
conversa, do lado de quem pediu, e o que precisa ser lido é o bloco do fim da
mensagem. É a regra do acervo — o que se reusa é a ideia da prova, não o
arquivo.

O código do link no desenho tem os 22 caracteres que o manual descreve, e é um
token sorteado que não existe no servidor.

### Recorte, e não aparelho, nos slides 3, 4 e 5

A capa e o CTA levam o celular inteiro; os três slides do meio levam **recorte**.
O critério é o da skill: aparelho quando a capa quer reconhecimento, recorte
quando o que precisa ser lido é o texto da tela. Nos slides 3 e 4 o assunto é
literalmente a frase que a tela escreve, e a moldura do celular comeria a
largura de que ela precisa.

O recorte do slide 5 é o contrário — ali não há texto, e o corte fecha em cima
dos três pinos para que a logo no pino tenha tamanho de leitura.

Todos os cortes são **medidos no arquivo** com Pillow, não estimados na
miniatura. É a regra herdada da #7 e da #10.

### A captura do computador foi refeita mais estreita

A primeira saiu em 1440 × 900. A página põe as informações numa coluna fixa e
dá o resto ao mapa, então em 1440 a coluna fica com 19% da tela — e reduzida
para os 936 px do `.notebook`, *Diego está indo até você* chegava ao slide com
10 px de letra. É o defeito que a #9 e a #8 já tinham documentado: **a largura
do viewport é decisão de arte**, e a conta é largura do recorte ÷ largura no
slide.

Refeita em **1152 × 720** — que é 16/10, a proporção da tela do `.notebook` —,
a coluna sobe para 29% e o nome do entregador continua legível depois da
redução. Nada mais mudou: é a mesma cena, a mesma resposta interceptada.

### O `.realce` do slide 2, e por que ele não está no arquivo

A captura do manual traz o bloco *Acompanhe a entrega* **marcado em amarelo**,
e copiar isso seria assar a anotação dentro da imagem — linguagem de manual, que
a skill proíbe na arte. O desenho saiu limpo, e quem dirige o olhar é o slide,
com o `.realce` posicionado em porcentagem sobre a figura.

### O celular da capa e o do CTA são o mesmo

A skill aprova **uma** repetição de prova dentro de uma peça, e é esta: o CTA
manda abrir justamente o que a capa mostrou, e a peça abre e fecha na mesma
cena. Foi o que a #10 fez com o notebook do mapa, por decisão do dono.

Aqui vale ainda melhor, porque a imagem **é** o assunto do pedido: o último
slide diz "despache a próxima rota" e mostra o que chega do outro lado quando
ela sai.

### A capa: três versões, e a terceira é a que anuncia o recurso

**Primeira:** *"Antes, o telefone. Agora, o rastreio da entrega"*. Caiu na
própria revisão, porque afirma que os clientes dele ligam — e quem pode
desmentir isso é ele.

**Segunda, a que foi entregue:** *"A mesma mensagem, agora com **rastreio da
entrega**"*, com o subtítulo *"No WhatsApp, quem pediu abre o mapa ao vivo"*. O
molde é antes × agora, que faltava no placar (pergunta 2, afirmação do fato 5,
anúncio de chegada 1, nome + canal 1, nome + dois-pontos 1 — antes × agora 0), e
o par de perguntas da skill passa inteiro: tem nome, tem o que faz, tem onde
acontece.

Voltou assim: *"a hero do slide 1 ainda não estamos conseguindo vender de forma
correta. 'Acompanhamento em tempo real pelo cliente' seria o correto."* São dois
defeitos, e os dois são de **sujeito**:

1. **o sujeito era o meio.** "A mesma mensagem" é o WhatsApp, e o WhatsApp é por
   onde o recurso chega, não o recurso. Título se lê da esquerda para a direita
   e a leitura do feed para no meio: quem leu a primeira metade foi informado de
   que **nada mudou**, e a novidade estava depois da vírgula. O molde antes ×
   agora carrega essa armadilha, porque o "antes" é sempre a coisa velha e ocupa
   a primeira metade da linha;
2. **o nome era o do release.** "Rastreio da entrega pelo cliente" é o título da
   publicação, escrito do lado de quem construiu. Quem compra compra
   *acompanhamento em tempo real*. Os dois são verdade, e é por isso que a troca
   não caiu em conferência nenhuma.

**Terceira, a publicada:**

> Acompanhamento **em tempo real**, pelo seu cliente
> O mapa da entrega chega pelo WhatsApp.

Molde novo na série: **nome + para quem**. O canal continua respondendo *onde
isso acontece?*, agora no subtítulo e como adjunto — que é o lugar dele quando
não é o nome do recurso (na #9 era: "Campanhas Inteligentes no WhatsApp").

O destaque mudou de lugar junto. Na #8, na #9 e na #10 o vermelho pegava o nome
inteiro, porque era a palavra que o leitor ia **procurar no menu** depois. Aqui
não há menu: o recurso é automático e não tem tela de configuração. Sem essa
função, o vermelho volta a marcar o que é notícia — *em tempo real*.

Três linhas curtas porque o nome tem 28 caracteres e em `titulo--medio` (68 px)
cabem cerca de 22 por linha. Quebrado em *Acompanhamento / em tempo real / pelo
seu cliente*, cada linha fecha inteira e o cartaz fica de pé.

As duas regras subiram para a skill, em *o décimo vício*.

### O segundo retorno: cinco slides explicavam a tela

A mesma leitura devolveu: *"tem slide que estamos explicando o funcionamento da
tela. não é um manual de usuário, e sim falando da novidade."*

Nenhum dos corpos acusados copiava a fonte, nenhum ensinava caminho de menu e
todos eram verdade conferida no manual. O que eles tinham era **sujeito de
interface** — "a tela escreve", "são quatro etapas", "o mapa ocupa a tela", "o
sistema anexa" —, e cada um descrevia a imagem que estava logo abaixo dele. O
slide tinha captura forte, a captura já dizia tudo, e a copy, sem assunto
próprio, legendou a prova. Legenda de captura é o formato de um manual.

A regra subiu para a skill como *o décimo primeiro vício*, e a revisão ganhou o
passo **1c**.

### O terceiro retorno: o conserto anterior esvaziou os slides

> *"O texto dos slides está sem sentido nenhum. Simplesmente falando frases
> estranhas sem sentido, tentando vender uma ideia que deveria ser simples —
> explicar a novidade."*

Certo, e a causa é a correção anterior. Ao tirar o sujeito de interface, tirei
o **fato** junto: os corpos ficaram só com a conclusão, e conclusão sem
premissa lê como frase de efeito.

A prova de que o defeito é de posição, e não de invenção: todas as frases
estranhas estão no manual, e no manual todas são complemento de um fato.

| O manual escreve | Ficou no slide |
|---|---|
| "É a mesma página, o mesmo link. **Não há 'versão para PC' para você manter nem divulgar**" | só a segunda frase, promovida a título |
| "Você não precisa configurar nada. Nenhum campo novo… **O link vai junto do aviso de saiu para entrega**" | só as ausências |
| "Carlos está indo até você / A 640 m de você, em linha reta" … "**O cliente que vê a moto se mexendo não pergunta**" | só a última frase |
| "Quando a entrega atrasa de verdade, **o cliente vê por quê**" | só "a demora ganha explicação" |

**A distinção que faltava:** como a tela se *comporta* é manual e sai; o que o
cliente *lê* ali é a novidade e fica. Tirar isso não conserta nada, esvazia o
slide.

As sete frases da terceira versão:

| Slide | Versão devolvida | Versão publicada |
|---|---|---|
| 2 corpo | "Não há campo novo para preencher, tela nova para aprender nem mensagem a mais na conta…" | "Na mensagem que avisa a saída, o sistema acrescenta o bloco **Acompanhe a entrega** e um endereço que vale só para aquele pedido…" |
| 3 título | "**Mapa ao vivo**: quem espera deixa de telefonar" | "**Mapa ao vivo**: quem está levando e quanto falta" |
| 3 corpo | "A ligação mais cara da noite é a de 'quanto tempo falta'…" | "Quem pediu lê o primeiro nome do entregador e quantos metros faltam até a porta, em linha reta…" |
| 4 corpo | "…a demora ganha explicação antes de virar reclamação" | "Quem pediu vê as quatro etapas se completarem, de **enviado** até **saiu para entrega**…" |
| 5 corpo | "Mapa de entrega é o que os aplicativos gigantes ensinaram o país a esperar…" | "O pino no meio do mapa carrega a logo do seu cardápio, e o nome da loja fica no alto da tela…" |
| 6 título | "**Uma página só**: nada de segunda versão para manter" | "**Uma página só**: o mesmo endereço, em qualquer aparelho" |
| 6 corpo | "…sem passar pelo seu telefone" | "…enquanto a entrega acontece, o acompanhamento também mora em **Pedidos**" |

Três correções de fato entraram junto, e as três valem registro:

- **a condição do slide 2 estava errada.** "Com o entregador em rota" não é a
  condição; o manual exige **posição enviada pelo celular dele nos últimos 15
  minutos**. Rota despachada não basta;
- **os títulos do 3 e do 6 eram corretos desde a primeira versão**, e fui eu que
  os quebrei lendo ganho como descrição. Voltaram, e voltaram a ser provados
  pela imagem;
- **a segunda porta do slide 6 ganhou a condição de volta**: ela vale enquanto a
  entrega está acontecendo, não para sempre.

E uma decisão de forma no slide 4: a frase da fila **não vai entre aspas**.
Citada ao pé da letra ela estoura a janela de seis palavras do conferidor contra
o manual; descrita ("ele lê em que lugar da viagem está") diz a mesma coisa sem
carregar parágrafo do manual. É a mesma decisão que os textos alternativos
tomaram na revisão anterior.

A pilha do slide 4 desceu de 820 para 740 px, com a margem de cima de 40 para
28: o corpo que devolve o fato ocupa cinco linhas em vez de três, e na largura
antiga o terceiro recorte batia nos pontos do rodapé. Encolher a imagem custa
menos que cortar informação.

Tudo isto subiu para a skill como *o décimo segundo vício*, e a tabela do
décimo primeiro foi corrigida de duas para **três** colunas — manual, retórica e
certo. Com duas colunas, o conserto vira "apague a descrição", e foi assim que
esta peça chegou ao terceiro retorno.

### O conferidor estava cego para o release

Ao reescrever a legenda, o `conferir-texto.py` rodado só com `--novidade` acusou
duas sequências do release que **três rodadas anteriores tinham aprovado**. A
causa é do script: `--fonte` **substituía** o feed em vez de somar, e esta peça
foi conferida com `--novidade` e quatro `--fonte` desde o começo. O `OK` saía,
e o release nunca tinha sido conferido.

O script foi corrigido na skill: as fontes se somam, e a linha de saída lista
todas — conferir essa lista é o jeito rápido de ver se faltou uma. A linha de
comando desta peça:

```bash
python .cursor/skills/carrossel/scripts/conferir-texto.py 11-rastreio-da-entrega \
  --novidade gestao-entregas-rastreio-pelo-cliente \
  --fonte manuais/gestao-entregas-rastreio-cliente \
  --fonte manuais/gestao-entregas-avisos-whatsapp \
  --fonte manuais/gestao-entregas-despachar \
  --fonte manuais/gestao-entregas-liberar-entregador
```

## O que a revisão mudou

**A capa perdeu uma linha de subtítulo** (isto foi na segunda versão do título,
e a medida continua valendo para a terceira). Na primeira renderização o subtítulo
quebrou em duas e o celular, em `top: 585px`, passou por cima da segunda — o
`z-index` do texto salvou a leitura e não salvou a arte. *"Quem pediu abre o
mapa ao vivo pelo WhatsApp"* virou *"No WhatsApp, quem pediu abre o mapa ao
vivo"*, que cabe em uma linha e diz a mesma coisa.

**O título do slide 2 desceu de tamanho.** Em `titulo--medio` ele ocupava três
linhas e empurrava a conversa de WhatsApp para uma largura em que o link não se
lia; em `titulo--pequeno` são duas linhas, e a figura subiu de 760 para 904 px,
que é a largura útil do slide.

**O `conferir-texto.py` pegou nove frases, e as nove eram do manual.** Duas em
slide (*"quando o entregador tem outra parada antes, a tela diz isso"* e *"o
link vai junto do aviso"*) e sete na legenda e nos textos alternativos. Vale
registrar o padrão: as frases que ele pega são as **mais bem escritas** do
rascunho, e é por isso que elas atravessam duas leituras sem levantar suspeita.

Uma decisão dentro dessa rodada: os textos alternativos descrevem uma tela, e
descrever uma tela é citar o que ela escreve. Onde a frase da tela é curta ela
ficou entre aspas (*"Pedido entregue às 20:12"*); onde ela é longa o suficiente
para o conferidor acusar, o texto alternativo **descreve em vez de citar** (a
linha da fila virou *"a linha que põe quem espera como a segunda de três
paradas da viagem"*). Acessibilidade não perde nada, e a peça não carrega
parágrafo do manual.

**Os 36 avisos de repetição entre carrosséis são um só.** Todos são a linha de
fechamento da série — *tudo que entra de novo está em beefood.app/novidades* —
mais a pílula de caminho. É convenção, e convenção repete de propósito.
