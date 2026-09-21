# Gestão de Entregas

- **Gênero:** novidade
- **Fonte:** não há release em `beefood.app/novidades` — o módulo está **em
  liberação**, e o fato vem dos **16 manuais** do grupo, que foram conferidos no
  código-fonte e na sandbox:
  [mapa e painel](../../manuais/gestao-entregas-mapa-painel/gestao-entregas-mapa-painel.md),
  [montar a rota](../../manuais/gestao-entregas-montar-rota/gestao-entregas-montar-rota.md),
  [despachar](../../manuais/gestao-entregas-despachar/gestao-entregas-despachar.md),
  [despacho automático](../../manuais/gestao-entregas-despacho-automatico/gestao-entregas-despacho-automatico.md),
  [fechar a entrega](../../manuais/gestao-entregas-fechar-entrega/gestao-entregas-fechar-entrega.md),
  [liberar o entregador](../../manuais/gestao-entregas-liberar-entregador/gestao-entregas-liberar-entregador.md),
  [ciclo completo](../../manuais/gestao-entregas-ciclo-completo/gestao-entregas-ciclo-completo.md),
  [avisos de WhatsApp](../../manuais/gestao-entregas-avisos-whatsapp/gestao-entregas-avisos-whatsapp.md),
  os seis do [app do entregador](../../manuais/app-entregador-entregas-do-dia/app-entregador-entregas-do-dia.md)
  e os dois relatórios
  ([operação](../../manuais/relatorio-operacao-entrega/relatorio-operacao-entrega.md),
  [taxa / KM](../../manuais/entregador-quanto-recebe/entregador-quanto-recebe.md)).
- **Formato:** 1080 × 1350 (4:5)
- **Slides:** 9

## O acervo, antes de escrever

A peça vizinha é a **#8, Painel para Entregadores** — mesmo módulo, e por isso a
primeira pergunta foi o que ela já vendeu. Ela vende **uma tela de parede na área
de retirada**, lida de longe pelo motoboy que chegou: o assunto dela é o pedido
(*já saiu da cozinha?*). Esta peça vende o outro lado do mesmo módulo, e o
assunto é a **viagem** (*quem leva, por onde, e quanto se paga por isso*). Os
dois manuais dizem essa fronteira com as mesmas palavras — na tela de Delivery
você mexe em **um pedido**; na Gestão de Entregas você organiza a **viagem**.

O que se reusou do acervo foi **método**, e em três pontos:

- a **interceptação da resposta da API** (do totem, do tablet e da #8), que aqui
  virou o `cena.json` de nove pedidos, cinco entregadores e duas rotas;
- o **corte medido no arquivo**, e não estimado na miniatura (da #7 e da #9);
- a **promoção da melhor prova para a capa** (da #9): aqui a melhor imagem já
  nasceu sendo a capa, porque o mapa com rotas e motoboys é o que a peça tem de
  mais reconhecível.

O que **não** se reusou: nenhuma imagem. A #8 fotografa colunas de cartão de
pedido; esta fotografa mapa, lista de rota, janela de regras e relatório. Não há
um recorte em comum.

**Erro documentado da #8 que esta peça herdou pronto:** a sandbox parada gera
tela verdadeira e péssima. Lá eram sete cartões "Atrasado • 1h38min"; aqui é
pior — zero rota, zero motoboy no mapa e cinco entregadores com GPS de três
dias. A cena foi montada antes da primeira captura, e não depois de uma rodada
perdida.

## O fato, o ângulo, e o que o slide diz

| Fato (manual) | Ângulo | O que vira slide |
|---|---|---|
| O módulo se chama **Gestão de Entregas**, fica em **Delivery → Entregas** e é uma tela só, com mapa à esquerda e lista de rotas à direita | Em novidade a capa anuncia: o nome no título, o que ele faz no subtítulo | Capa |
| "Na tela de Delivery você mexe em **um** pedido; aqui você organiza a **viagem**" | É a fronteira do módulo, e é a frase que explica o recurso sem virar manual | 2 |
| Cada pedido aparece duas vezes: pino no mapa e cartão na lista. Os selos do topo (em preparação, prontos, em rota, entregues) contam e **filtram** | Uma olhada responde "quantos" e "onde" ao mesmo tempo | 2 |
| O **despacho automático** junta os pedidos em rota e escolhe o entregador, por sete regras: máximo por viagem, distância e tempo de agrupamento, quando liberar, raio da loja, posição do entregador e tolerância de GPS | Hora de pico não tem operador sobrando para montar rota a rota | 3 |
| "A rota **não sai sozinha**: despachar continua sendo um clique seu" — e a ordem das paradas é refeita pelo trajeto mais curto saindo da loja | O automático para antes do irreversível, e isso é a favor de quem opera | 3 |
| A posição do entregador vem do celular dele; a lista mostra **há quanto tempo** a última posição chegou, a **distância** até a loja e a **bateria** | Bateria na lista não é enfeite: abaixo de 15% o GPS para antes de a viagem acabar | 4 |
| Quatro situações — Disponível, Em rota, Em pausa, Offline — e **quem muda é o entregador, no app** | O painel mostra e recusa dar rota a quem não está; ninguém finge disponibilidade | 4 |
| O aplicativo **BeeFood Entregador** está no Google Play e na App Store, e a lista dele é só as entregas daquele entregador, ordenadas da mais perto para a mais longe | O motoboy não liga para a loja para saber o endereço seguinte | 5 |
| No app, a rota montada pela loja chega com a letra, o contador de entregas e o botão **INICIAR ROTA**; cada parada mostra o pedido, a previsão e quanto **cobrar** na porta | A ordem que a loja montou chega no celular como ela foi montada | 5 |
| Quatro avisos de WhatsApp: **Nova entrega**, **Entrega cancelada** e **Relatório diário** vão para o entregador; **Entregador próximo** vai para o cliente, a partir de 2 km | Dois telefonemas que deixam de existir: o da loja para o motoboy e o do cliente para a loja | 6 |
| Todos nascem ligados e com texto pronto; o do cliente tem **três variações** sorteadas a cada envio | Não há nada para escrever no primeiro dia | 6 |
| O relatório **Operação de Entrega** quebra a entrega em quatro etapas e mostra **onde o tempo é investido**, separando loja e rua | A conversa "o motoboy é devagar" costuma terminar na cozinha | 7 |
| O relatório **Entregador (Taxa / KM)** fecha quanto pagar, em quatro modos: taxa do cliente, valor gravado no pedido, KM rodado do cadastro, com ou sem ida e volta — mais a diária | Fechamento de motoboy é discussão semanal, e ela acaba com a lista na mão | 8 |
| Sai em **Imprimir Cupom**, Imprimir A4 e Excel, um por entregador | O comprovante mais barato de encerrar discussão | 8 |
| Está em **Delivery → Entregas**, e o app do entregador em **Aplicativos → Entrega** | Já está lá; o que falta é o cadastro do entregador e o app no celular dele | 9 (CTA) |

**Ficou de fora, de propósito:**

- **o código de barras e a cobrança dentro do app** (`app-entregador-codigo-barras`,
  `app-entregador-cobranca`): são fatos bons e são **operação do motoboy**, não
  motivo para o dono ligar o módulo. Nove slides já é o teto da peça;
- **a confirmação de entrega de marketplace pelo app** (`app-entregador-marketplace`):
  o mesmo, e ela pede explicar iFood e 99Food na arte;
- **as quatro camadas do mapa** (Claro, Ruas, Humanitário, Satélite) e a busca por
  pedido: microdetalhe de interface, que é material de manual;
- **"o painel precisa ficar aberto para o despacho automático rodar"**: é limite,
  e aviso de limite antes do CTA derruba a peça. Quem precisa dele abre o manual;
- **os números de acerto por pessoa** (a tabela *Resumo por Entregador*): ver
  *o recorte do relatório de acerto*, abaixo.

## Slide a slide

| # | Tipo | Ideia única | Imagem |
|---|---|---|---|
| 1 | Capa | Chegou a Gestão de Entregas: você organiza a viagem, não o pedido | `mapa-rotas.png` num `.notebook` |
| 2 | Explica o recurso | Uma tela só: o mapa diz onde, a lista diz quem leva | `painel-inteiro.png` em `.navegador` sangrando |
| 3 | Roteirização automática | O sistema junta os pedidos e escolhe quem sai; despachar continua sendo seu | `despacho-regras.png` |
| 4 | Tempo real | Onde cada motoboy está, de quando é a posição e quanta bateria sobra | `lista-entregadores.png` |
| 5 | App do entregador | A rota chega no celular dele, no Android e no iPhone | `app-rota.png` (desenho) + `app-lojas.png` |
| 6 | WhatsApp | Quatro avisos prontos: três para o entregador, um para quem está esperando | `zap-entregador.png` + `zap-cliente.png` (desenho) |
| 7 | Operação de Entrega | O relatório mostra quanto do tempo é cozinha e quanto é rua | `relatorio-operacao.png` |
| 8 | Acerto do entregador | Quatro modos de pagar, e o cupom de fechamento na mão dele | `relatorio-entregador.png` |
| 9 | CTA | Está em Delivery → Entregas, e o app em Aplicativos → Entrega | `app-lojas.png` recortado |

## Decisões de arte

### A cena das capturas é montada, e o `cena.json` diz o que

A sonda (`sondar.py`, e o `sonda-painel.json` ao lado) encontrou o painel assim:
quatro pedidos `PRONTO`, **zero rota**, **zero entregador com posição** — o GPS
mais novo tinha três dias e o mais velho oito. O mapa desenhava a loja e quatro
pinos cinzas. A peça inteira fala de rota, de despacho e de acompanhamento ao
vivo: não havia o que fotografar.

A cena repõe o que o tempo parado desfez, e o critério é o da #8 — **o que é
prova fica, muda-se o que o relógio estragou**:

- os **três pedidos reais** do seeder (1140, 1141, 1142) mantêm número, cliente,
  endereço, pagamento e **coordenada real**, e são as três paradas da rota A. Só
  a idade em minutos encurtou, porque o seeder rodou de manhã;
- **seis pedidos de exemplo** entram para a rota B, para a fila sem rota e para
  os selos do topo. Um pedido real (1143, Avenida Itavuvu 3040) **saiu**: ele
  fica a 10 km e, com ele na tela, o enquadramento abre tanto que as linhas das
  rotas desaparecem atrás dos pinos;
- **quatro entregadores** voltam a ter posição recente e bateria; o quinto
  continua "nunca usou o app", que é o estado real dele;
- **duas rotas** passam a existir — A na rua, B pronta para sair —, as duas com
  origem automática, e o despacho aparece ligado. Sem isso, a rota que o
  automático criou estaria na tela com o recurso que a criou desligado no selo.

Nada é escrito no servidor: as respostas de `GET /entrega2/gestao/painel`,
`/posicoes` e `/despacho/config` são reescritas no navegador da captura, e o PUT
das mesmas rotas segue para o servidor sem passar pelo script. `--cru` mostra a
tela como ela está hoje.

### O mapa lembra o quadro anterior, e é por isso que ele abria na cidade inteira

`gestaoEntregas.mapaZoom` e `gestaoEntregas.mapaCentro` moram no `localStorage`,
e com eles gravados o mapa **não enquadra os pinos**: abre no último quadro que
alguém deixou. Na sessão reaproveitada do `capturar.py` isso era Sorocaba
inteira. Apagadas as duas chaves num `init_script`, o `fitBounds` da cena volta
a valer — e um passo de zoom em cima disso é o que torna a linha tracejada da
rota visível: no zoom padrão, 500 m entre duas paradas viram 50 px e o traço
desaparece atrás dos pinos.

### O mapa passava por cima das janelas do painel

Duas capturas saíram com o recorte certo e o desenho errado: a janela do
despacho e a lista de entregadores apareciam **atrás do mapa**, com só a beirada
direita visível. Não é seletor errado — é empilhamento. `.leaflet-container` é
`position: relative` sem `z-index`, então não abre contexto próprio, e os painéis
de dentro dele (`z-index: 400`) disputam o desenho com a janela do Radix, que é
`z-index: 50`. Os quadrados do mapa e os pinos ganham.

Só aparece com o mapa **carregado**: no print do manual, em que os quadrados não
chegaram, a janela sai inteira — e foi essa diferença que apontou a causa. Um
`z-index: 0` no contêiner fecha o contexto e devolve a ordem, sem tocar em
conteúdo nenhum.

E a janela do despacho ainda pedia uma segunda correção: ela tem ~700 px de
altura e o teto é `90vh`. Nos 900 px do dispositivo `painel` ela abre **rolada**,
sem o título em cima e sem a tolerância de GPS embaixo — e recorte nenhum
devolve o que não foi desenhado. A captura dela é a única em 1440 × 1160.

### As janelas são fotografadas inteiras e recortadas depois

Medir a caixa no DOM não serviu: `[role="dialog"]` casa com mais de um elemento
da página, porque a janela da tela inteira fica montada mesmo fechada. O
caminho foi fotografar a tela inteira com `--medir`, achar a caixa da janela pelo
branco (`medir-janela.py` — o véu escurece a página e a janela é a única coisa
branca) e guardar o corte em pixel de arquivo no próprio script. É a mesma regra
da #7: **coordenada medida no arquivo, nunca estimada na miniatura**.

### O recorte do relatório de acerto

A sandbox tem dado de verdade nos dois relatórios, e eles são bons: 160 entregas
em 30 dias, R$ 1.058,45 de taxa, 22,6 min de duração média, 604,76 km rodados,
quatro diárias. O que ela **não** tem é operação disciplinada: 162 das 195
entregas do período estão como *Sem entregador*, porque ninguém se identifica no
painel de uma loja de teste.

Isso é verdade e é o contrário do que a peça promete. E não é caso de montar
cena — o critério é o da #9: **relógio e situação se montam; dinheiro pago e
volume, não**. Então quem decide é o recorte. O slide 8 afirma *"escolha como
pagar, e o relatório fecha a conta"*, e a tela para de afirmar isso na linha em
que a tabela começa: o corte fecha logo abaixo dos cinco cartões, com os quatro
modos de cálculo em cima e os botões de impressão ao lado. A tabela por pessoa
fica para o manual.

No relatório de operação a conta é parecida. Dois cartões de etapa dizem
*Poucos pedidos — mínimo 20*, que é o aviso normal de volume baixo e lê como
falha. O corte pega a faixa em que a tela afirma: *Saída até entrega 5,3 min*,
*Pedido até entrega 22,6 min* e a barra **Onde o tempo é investido**, com
*35,1 min na loja · 87%* contra *5,3 min na rua · 13%*. É, de longe, a coisa mais
forte dos dois relatórios — e é um número real da sandbox, não um exemplo.

### O que é desenho, e por quê

Três imagens desta peça são **tela desenhada**, e todas por um motivo só: o
aplicativo Android do entregador **não roda no Cloud Agent**.

| Imagem | O que é | De onde saiu o desenho |
|---|---|---|
| `app-rota.png` | a rota A na lista do aplicativo | `manuais/app-entregador-rota/imagens-puras/03-rota-na-lista.png` e `manuais/app-entregador-entregas-do-dia/imagens-puras/01-lista.png` (prints de produção) |
| `zap-entregador.png` | as três mensagens do entregador | o **texto de fábrica** dos avisos, com os marcadores substituídos |
| `zap-cliente.png` | as duas mensagens do cliente | idem |

O desenho copia layout, paleta e hierarquia do print de produção — barra escura
com o título em caixa alta, etiqueta laranja do número do pedido, previsão em
vermelho com o ícone de relógio, `Cobrar R$` em verde, círculo numerado da
sequência e a faixa vermelha à esquerda — e **troca os dados pelos da cena**, que
são os mesmos pedidos do painel: 1140 Ana Beatriz na Rua Padre Luiz, 1141 Carlos
Eduardo na Rua Dom Antônio Alvarenga, 1142 Fernanda na Rua Aparecida. É o que faz
o slide 5 concordar com a capa.

O texto das mensagens de WhatsApp **não foi escrito à mão**: é o de fábrica, que
está na seção 6 do manual dos avisos, com `**VENDA_NUMERO**`, `**CLIENTE_NOME**`
e companhia já trocados pelos dados da cena. O manual desenha as mesmas conversas
em HTML por não ter número conectado na sandbox; aqui elas foram redesenhadas no
vocabulário do carrossel, com os dados da cena — é a regra do acervo: **o que se
reusa é a ideia da prova, não o arquivo**.

E o print do manual não entra recortado em slide nenhum: ele é referência de
layout, como manda a skill.

### O que a revisão mudou

A folha de contato e a leitura em tamanho real pegaram quatro coisas, e nenhuma
delas aparece na miniatura:

- **a borda dos dois recortes de relatório estava torta.** O corte vinha de
  `1004 → 2816` e o painel branco do relatório vai de `962` a `2813`: sobrava
  uma faixa de 3 px do lado de fora à direita e faltavam 42 px à esquerda. No
  slide aquilo lia como cartão pela metade encostado na borda. A medida saiu da
  varredura do pixel branco puro na linha, e não de estimativa na miniatura;
- **os slides 7 e 8 tinham tarja morta entre a imagem e o rodapé.** Recorte de
  ~3/1 na largura do slide tem 320 px de altura numa faixa de 400, e
  `margin-top` acerta por acidente. Um `.empurra` de cada lado da `.figura`
  centraliza a imagem no vão, e a largura subiu para os 1004 px da sangria;
- **o título do slide 7 tinha três linhas**, a terceira com a palavra `rua`
  sozinha. Saiu *"O relatório diz"* — o chapéu já diz que é relatório — e o
  corpo passou a nomear o relatório, no lugar de um `ele` solto;
- **a frase do slide 3 era a do sistema, palavra por palavra.** Ver abaixo.

### A cópia que estava também na imagem

O `conferir-texto.py` ganhou `--fonte <caminho>` nesta peça, justamente porque
não há release para medir contra: as dezoito fontes são os manuais. Ele acusou
três frases, e a mais instrutiva é a do slide 3 — *"despachar continua sendo um
clique seu"*, que é o texto que o sistema escreve no alto da janela do despacho
**e que está na imagem daquele mesmo slide**. Era cópia do manual e era desenho
repetido: a única linha de copy do slide estava sendo gasta duas vezes.

A segunda versão (*"quem manda a rota para a rua continua sendo você"*) passou
no slide por inflexão e foi pega no texto alternativo, porque *"mandar a rota
para a rua"* é do manual. Ficou *"Nada sai da loja sem o seu clique"*.

Os avisos de repetição contra os outros carrosséis são todos a linha de
fechamento da série (*"Tudo que entra de novo está em beefood.app/novidades"*).
Ela repete de propósito: é convenção de CTA, e a frase mais comum possível é a
que funciona.

### A capa

O molde é novo na série: **nome, dois-pontos, e o fato**. As nove capas
anteriores já usaram pergunta (duas), afirmação do fato novo (cinco), anúncio de
chegada (uma) e nome + canal (uma). "Chegou a Gestão de Entregas" seria a oitava
repetição de um molde de duas peças atrás.

O par de perguntas da skill passa: **qual é o nome?** Gestão de Entregas.
**O que aquilo faz?** Organiza a viagem em vez do pedido — e o subtítulo diz
como: pedido virando rota, rota ganhando entregador, motoboy no mapa.
**Onde acontece?** No painel, em Delivery → Entregas; o módulo não é batizado
com canal nenhum, então não há terceiro eixo a carregar.

A imagem é o mapa, num `.notebook`: a Gestão de Entregas é operada **sentado**,
no computador do balcão, e é a cena que o aparelho deitado conta. O recorte do
mapa entra em 16/10, que é a tela do notebook — e o que ele mostra é exatamente
o pedido que abriu esta peça: mapa, duas rotas tracejadas com paradas numeradas
e os motoboys com nome.
