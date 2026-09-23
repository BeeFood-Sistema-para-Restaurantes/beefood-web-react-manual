# Rastreio da entrega, pelo cliente

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

| # | Tipo | Ideia única | Imagem |
|---|---|---|---|
| 1 | Capa | A mensagem de sempre agora abre um mapa ao vivo no celular de quem pediu | `cel-a-caminho.png` num `.celular` sangrando pela base — **captura** |
| 2 | Explica o recurso | O link entra sozinho no aviso que a loja já mandava | `zap-rastreio.png` — **desenho** da conversa, com o bloco *Acompanhe a entrega* |
| 3 | O mapa ao vivo | O nome de quem está levando e a distância até a porta | `recorte-a-caminho.png` + `recorte-cartao.png` — **captura**, dois recortes |
| 4 | A barra de etapas | Onde o pedido está em cada momento, sem ninguém perguntar | `recorte-preparo.png`, `recorte-fila.png`, `recorte-entregue.png` — **captura**, três recortes |
| 5 | O pino da loja | A logo do restaurante no meio do mapa, e nenhuma marca nossa | `recorte-mapa.png` — **captura**, recorte fechado |
| 6 | No computador | A mesma página e o mesmo link, em duas colunas | `pc-a-caminho.png` num `.notebook` — **captura** |
| 7 | CTA | Já está no ar, e não há nada para ligar: despache a próxima rota | `cel-a-caminho.png` no mesmo `.celular` da capa — a peça abre e fecha na mesma cena |

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

### O celular da capa e o do CTA são o mesmo

A skill aprova **uma** repetição de prova dentro de uma peça, e é esta: o CTA
manda abrir justamente o que a capa mostrou, e a peça abre e fecha na mesma
cena. Foi o que a #10 fez com o notebook do mapa, por decisão do dono.

Aqui vale ainda melhor, porque a imagem **é** o assunto do pedido: o último
slide diz "despache a próxima rota" e mostra o que chega do outro lado quando
ela sai.

### A capa: antes × agora, o molde que faltava

Placar dos moldes nas dez peças: pergunta 2, afirmação do fato 5, anúncio de
chegada 1, nome + canal 1, nome + dois-pontos 1 — **antes × agora 0**.

Ele é o molde certo aqui, e não só por rodízio: o recurso **é** um antes e um
agora da mesma mensagem. A loja não passou a mandar nada novo; o aviso que já
saía ganhou um bloco no fim.

> **A mesma mensagem, agora com rastreio da entrega**

O par de perguntas passa: **qual é o nome?** Rastreio da entrega. **O que aquilo
faz?** Abre um mapa ao vivo no celular de quem pediu, e o subtítulo diz isso.
**Onde acontece?** No aviso de saiu para entrega, no WhatsApp.

E a capa não afirma nada sobre o leitor. A primeira versão do título era
*"Antes, o telefone. Agora, o rastreio da entrega"* — boa frase, e ela afirma
que os clientes dele ligam. Quem poderia desmentir? Ele. O antes virou o da
**mensagem**, que é do produto.
