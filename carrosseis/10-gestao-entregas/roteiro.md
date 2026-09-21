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
| No app a pílula tem **três** estados — ONLINE, PAUSA, OFFLINE — e **quem toca nela é o entregador**; no painel são **quatro** grupos, porque *Em rota* aparece quando a loja despacha | Deixa de existir o telefonema "você tá na rua?": a informação é dele, e chega sozinha | 4 |
| A pílula **avisa e não bloqueia**: a loja consegue despachar para quem está em pausa ou offline, e as entregas que já estão na lista dele continuam dele | Sem promessa de bloqueio, que o sistema não faz | 4 (o que não se diz) |
| A posição do entregador vem do celular dele; a lista mostra **há quanto tempo** a última posição chegou, a **distância** até a loja e a **bateria** | Fica na imagem do 4, na linha de cada pessoa, sem virar título | 4 |
| O aplicativo **BeeFood Entregador** está no Google Play e na App Store, e a lista dele é só as entregas daquele entregador, ordenadas da mais perto para a mais longe | O motoboy não liga para a loja para saber o endereço seguinte | 5 |
| No app, a rota montada pela loja chega com a letra, o contador de entregas e o botão **INICIAR ROTA**; cada parada mostra o pedido, a previsão e quanto **cobrar** na porta | A ordem que a loja montou chega no celular como ela foi montada | 5 |
| Quatro avisos de WhatsApp: **Nova entrega**, **Entrega cancelada** e **Relatório diário** vão para o entregador; **Entregador próximo** vai para o cliente, a partir de 2 km | Dois telefonemas que deixam de existir: o da loja para o motoboy e o do cliente para a loja | 6 |
| Todos nascem ligados e com texto pronto; o do cliente tem **três variações** sorteadas a cada envio | Não há nada para escrever no primeiro dia | 6 |
| O relatório **Operação de Entrega** quebra a entrega em quatro etapas e mostra **onde o tempo é investido**, separando loja e rua | A conversa "o motoboy é devagar" costuma terminar na cozinha | 7 |
| O relatório **Entregador (Taxa / KM)** fecha quanto pagar, em **três modos** — taxa do cliente, valor gravado no pedido, KM rodado do cadastro —, com a opção de **pagar o KM de ida e volta**, e a diária somada por cima | Fechamento de motoboy é discussão semanal, e ela acaba com a lista na mão | 8 |
| Sai em **Imprimir Cupom**, Imprimir A4 e Excel, um por entregador | O comprovante mais barato de encerrar discussão | 8 |
| A Gestão de Entregas **está incluso no módulo Entrega**, junto do Painel para Entregadores, e fica em **Delivery → Entregas** | Quem já paga o módulo já tem isto — não há o que contratar, há o que abrir | 9 (CTA) |

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
| 1b | Capa, versão alternativa | idem | o **mesmo** `.notebook`, no mesmo tamanho, com o `.celular` do `app-rota.png` na frente — em `capa-alternativa/` |
| 2 | Explica o recurso | Uma tela só: o mapa diz onde, a lista diz quem leva | `painel-inteiro.png` em `.navegador` sangrando |
| 3 | Roteirização automática | O sistema junta os pedidos e escolhe quem sai; despachar continua sendo seu | `roteirizacao.png` (desenho): os três passos do agrupamento |
| 4 | Situação do entregador | Online, em pausa ou offline: quem marca é o entregador, no app dele | `situacao-entregador.png` (desenho): o app dele e o painel da loja juntos |
| 5 | BeeFood Entregador | A rota montada no painel aparece no celular de quem vai levar | `app-rota.png` (desenho) |
| 6 | Avisos no WhatsApp | Quatro avisos prontos: três para o entregador, um para quem está esperando | `zap-avisos.png` (desenho) |
| 7 | Relatório de Operação de Entrega | Quanto do tempo é cozinha e quanto é rua | `relatorio-operacao.png` (desenho) num `.notebook` |
| 8 | Relatório do Entregador | Três modos de pagar, e o fechamento por pessoa | `relatorio-entregador.png` (desenho) num `.notebook` |
| 9 | CTA | Já está no ar, em Delivery → Entregas: monte a primeira rota hoje | `mapa-rotas.png` num `.notebook` — a mesma arte da capa, fechando a peça |

## Decisões de arte

### O que a pasta guarda de sondagem, e por quê

Nenhum carrossel anterior guarda saída de sonda, e esta guarda três arquivos
porque eles sustentam as duas decisões mais contestáveis da peça:

| Arquivo | Que decisão ele prova |
|---|---|
| `sonda-painel.png` e `sonda-painel.json` | o painel **como foi encontrado**: `0 em rota`, `0 disponíveis`, `4 offline`, despacho desligado e nenhum motoboy no mapa. É o que justifica o `cena.json` |
| `sonda/operacao-1.png` e `sonda/entregador-0.png` | os dois relatórios **como a sandbox os entrega**: *Poucos pedidos — mínimo 20* nos cartões de etapa e 162 de 195 entregas como *Sem entregador*. É o que justifica desenhar os dois relatórios em vez de capturá-los |

As outras oito tiras de rolagem saíram: `sondar-relatorios.py` as refaz, e
3 MB de print que ninguém vai abrir não é acervo, é andaime.

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

O achado sobrevive à revisão mesmo tendo perdido o uso: das duas janelas, a do
despacho saiu da peça (era tela de configuração) e a de entregadores virou
**referência de desenho**, não imagem de slide. O `z-index` continua no script
porque é ele que deixa a lista de entregadores fotografável — e é dessa foto que
o desenho do slide 4 copia layout, paleta e hierarquia.

### As janelas são fotografadas inteiras e recortadas depois

Medir a caixa no DOM não serviu: `[role="dialog"]` casa com mais de um elemento
da página, porque a janela da tela inteira fica montada mesmo fechada. O
caminho foi fotografar a tela inteira com `--medir`, achar a caixa da janela pelo
branco (`medir-janela.py` — o véu escurece a página e a janela é a única coisa
branca) e guardar o corte em pixel de arquivo no próprio script. É a mesma regra
da #7: **coordenada medida no arquivo, nunca estimada na miniatura**.

### Por que os dois relatórios são desenhados, e não capturados

A primeira versão da peça capturou os dois, e a captura foi o pior par de
imagens do conjunto. A causa não é técnica: é que **o relatório do sandbox não
tem o que afirmar**.

No de operação, as médias só saem com vinte pedidos no período, então dois
cartões de etapa dizem *Poucos pedidos — mínimo 20*, que é o aviso normal de
volume baixo e no slide lê como falha. O que sobrava de afirmação era uma barra
de *87% na loja* contra *13% na rua* — número verdadeiro de uma loja de teste
com quatro entregas, e leitura de operação nenhuma.

No de acerto é pior: 162 das 195 entregas do período estão como *Sem
entregador*, porque ninguém se identifica no painel de uma loja de teste. A
tabela por pessoa, que é o assunto do slide, era uma coluna de traços. O recorte
fugiu dela e foi parar no **cabeçalho** — os três modos de cálculo e a caixa do
ida e volta —, ou seja, na tela de ajuste. Era o defeito que o dono nomeou, e é
o que a skill passou a proibir.

Desenhar resolve as duas coisas de uma vez, e sem inventar produto: a
**estrutura** dos dois relatórios está inteira nos manuais, seção por seção, e é
ela que o desenho reproduz na ordem em que ela aparece na tela. O que é de
exemplo é o **número**.

Três regras seguraram a honestidade, e valem para qualquer relatório desenhado:

- **um jogo só de números, com as somas fechando.** As conferências estão nos
  comentários de `telas/relatorio-operacao.html` e `telas/relatorio-entregador.html`,
  linha por linha: 128 entregas × R$ 8,00 = R$ 1.024,00 de taxas; 148,6 km ×
  R$ 1,50 = R$ 222,90 de ida; as 13 barras do gráfico por hora somam 128; 18 + 9
  + 20 min das etapas dão os 47 min do total; o Total Geral de R$ 1.612,20 é a
  soma das quatro linhas mais as quatro diárias. O 128, o R$ 1.024,00 e o
  R$ 413,00 são **os mesmos nos dois slides**;
- **a copy não cita nenhum número da imagem.** Quanto da entrega é cozinha e
  quanto é rua é a leitura de cada loja; escrito no slide, o exemplo viraria
  promessa de resultado nosso;
- **a legenda do post diz, uma vez, que o dado é de exemplo** — e na arte não
  vai carimbo nenhum.

Os dois entram em `.notebook`, na proporção 16/10 exata da tela dele, para que o
`object-fit: cover` não coma faixa nenhuma do relatório. Relatório se lê
sentado, e a moldura deitada conta isso.

### O que é desenho, e por quê

Cinco das nove imagens da peça são **tela desenhada**, e são três motivos
diferentes:

| Imagem | Por que desenhada | De onde saiu o desenho |
|---|---|---|
| `app-rota.png` | o app é Android/iOS e não roda no Cloud Agent | `manuais/app-entregador-rota/imagens-puras/03-rota-na-lista.png` e `manuais/app-entregador-entregas-do-dia/imagens-puras/01-lista.png` (prints de produção) |
| `situacao-entregador.png` | o app e o painel precisavam ficar na **mesma** imagem: é o encontro dos dois que prova o fato | `manuais/gestao-entregas/material-recebido/app-entregador/02-disponibilidade/prints/02-pilula-pausa.png`, mais `imagens-puras/lista-entregadores.png`, que é captura de produção desta peça |
| `zap-avisos.png` | não há número conectado na sandbox | o **texto de fábrica** dos avisos, com os marcadores substituídos |
| `roteirizacao.png` | o fato é uma **regra**, e a janela da regra é tela de configuração — então a imagem é o efeito dela | `imagens-puras/lista-rotas.png` (captura de produção) e as seções 4 e 5 do manual do despacho automático |
| `relatorio-operacao.png` e `relatorio-entregador.png` | o sandbox não tem volume (acima) | a estrutura dos dois manuais de relatório, seção por seção |

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

### A segunda revisão, que refez quatro imagens

A primeira entrega foi reprovada por uma coisa só, e ela vale mais que as quatro
correções que gerou: **quatro dos nove slides mostravam tela de configuração**.
O slide 3 era a janela das sete regras do despacho, o 8 era o cabeçalho de modos
de cálculo do relatório, o 9 era a janela que ensina os dois cadastros, e o 7
era um recorte de duas linhas de um relatório sem volume. Formulário, campo,
interruptor. Nas palavras do dono: *"nossos carrosséis ficam só com imagem de
configuração de campos e printscreen das telas"*.

A causa não era descuido de execução: era a **ordem da skill**. O passo 3 da
`SKILL.md` ordenava a imagem por facilidade de captura, com desenho no último
degrau, como pobreza — e a tela mais fácil de capturar é sempre o formulário,
que abre com um clique e fica pronto sem dado nenhum dentro. A skill foi
corrigida primeiro, e só depois os slides: a ordem agora é **resultado
capturado > resultado desenhado**, e tela de configuração não entra em nenhuma
das duas.

O que mudou em cada um:

| Slide | Era | É |
|---|---|---|
| 3 | a janela das sete regras | o **efeito** da regra: três pedidos soltos → a rota fechada ainda *Sem entregador*, em *Montando* → a mesma rota com o Rafael Lima e o avião do despacho ao lado |
| 4 | "antes de ligar, olhe a bateria" — e o dono disse que não fechava | quem **declara** a disponibilidade: o app do Paulo Henrique em PAUSA ao lado do painel com ele dentro de *Em pausa (1)* |
| 7 | dois cartões recortados de um relatório sem volume | o relatório **inteiro**, desenhado, num notebook |
| 8 | o cabeçalho com os modos de cálculo | o **fechamento**: a linha de cada pessoa, a diária e o total a pagar |
| 9 | a janela que ensina os dois cadastros | o **resultado** dos dois cadastros: o app aberto, pílula verde, lista ainda vazia |

O slide 4 é o que mais ganhou, e não foi só a imagem. A versão antiga gastava o
título com uma exceção de suporte (bateria abaixo de 15%); a nova diz o fato que
muda o dia de quem opera — a disponibilidade é declarada pelo entregador, e o
painel lê. A bateria continua na imagem, na linha de cada pessoa, que é o
tamanho que ela tem.

E uma coisa **não** entrou no slide 4, de propósito: a promessa de que quem está
offline não recebe rota. O manual é explícito no contrário — *a pílula avisa, não
tranca* —, e a loja consegue despachar para quem está em pausa ou offline. A
versão anterior do roteiro afirmava que o painel "recusa dar rota a quem não
está", e aquilo era invenção.

### A terceira revisão, que reescreveu sete títulos

A imagem tinha sido consertada e o texto, não. O dono leu slide por slide e
devolveu seis linhas; cinco delas são de redação e a sexta é de arte. Vale
transcrever, porque a peça é o caso que mudou a skill pela segunda vez:

| Slide | O retorno | O que estava errado |
|---|---|---|
| 3 | *"'Roteirização automática de pedidos' — por que não usamos isso?"* | o título tinha só o ângulo ("No pico, a rota já chega montada"), e o nome do recurso estava em nenhum lugar do tipo grande |
| 4 | *"quem marca é ele, ele quem?"* | pronome no título, com o antecedente no chapéu |
| 5 | *"abre no celular dele quem? que frase estranha"* | o mesmo pronome, e uma construção que ninguém fala |
| 7 | *"Relatórios… deveria ser esse o título vendedor"* | o título vendia o ângulo e escondia que aquilo é um relatório com nome |
| 8 | *"também igual 7"* | idem |
| 9 | *"a copy ficou estranha… como estamos chegando num texto tão tosco assim?"* | artigo cortado e `de que` comido: "Lista vazia com a pílula verde é sinal que deu certo" |

A causa é uma, e ela estava na skill: **nomear era regra da capa, e os slides de
dentro ficaram livres para ser espertos.** Nove peças passaram assim. As três
regras novas do passo 2 da `SKILL.md` saíram daqui — *nome, dois-pontos, o que
ele te dá*, *pronome no título é sempre erro* e *frase de manchete de jornal não
é frase de carrossel* —, e com elas os títulos ficaram:

| # | Era | É |
|---|---|---|
| 3 | No pico, a rota já chega montada | **Roteirização automática**: a rota já chega montada |
| 4 | Online, em pausa ou offline — quem marca é ele | Online, em pausa ou offline: **quem marca é o entregador** |
| 5 | A rota que você montou abre no celular dele | **BeeFood Entregador**: a rota no celular do entregador |
| 6 | Dois telefonemas a menos em cada entrega | **Avisos no WhatsApp**: dois telefonemas a menos |
| 7 | Quanto da entrega é cozinha, e quanto é rua | **Relatório de Operação de Entrega**: quanto é cozinha, quanto é rua |
| 8 | Escolha como pagar, e o relatório fecha a conta | **Relatório do Entregador**: quanto pagar a cada um |
| 9 | Dois cadastros, e o entregador já entra no mapa | O entregador entra no mapa com **dois cadastros que você já tem** |

O 6 não tinha sido reclamado e entrou na leva de propósito: o defeito era o
mesmo — "Avisos no WhatsApp" existia só no chapéu — e consertar cinco de seis
deixaria a fila de títulos sem ritmo.

Nenhum ângulo foi perdido. Todos viraram a segunda metade do título, que é onde
eles sempre deviam estar, e o chapéu ficou livre para dizer **quando** a coisa
acontece: *na hora do pico*, *quem está na rua agora*, *em cada entrega*, *no
fim do dia*, *no dia do acerto*. Antes ele era nome de janela ("Despacho
automático") ou de item de menu ("Operação de entrega"), que a própria checagem
da skill já proibia — e que passou nove peças porque não havia para onde mover o
nome do recurso.

Os corpos foram atrás. Três começavam sem verbo principal — "Na ordem que a loja
definiu…", "Pela taxa cobrada na entrega…", "Quatro etapas medidas uma por
uma…" —, que é legenda de foto no lugar de parágrafo, e é isso que produz a
sensação de texto telegráfico mesmo quando cada palavra está certa.

### O CTA era sobre cadastro, e CTA de novidade vende

*"Refaça a copy inteira do último slide, não é sobre isso, venda a novidade."*

As duas versões anteriores eram sobre **trabalho**. A primeira mostrava a janela
do painel que ensina onde criar o funcionário e o usuário; a segunda trocou a
imagem e manteve o assunto — "dois cadastros que você já tem". Nenhuma vende o
módulo: as duas explicam a burocracia de ligá-lo. Fechar peça de novidade com
trabalho é perder a venda no último slide, depois de oito slides de argumento.

E o defeito era fácil de ver de fora, porque **a série inteira faz diferente**:

| Peça | CTA |
|---|---|
| #3 | *Já está no ar* · "Suba o seu primeiro vídeo hoje" |
| #4 | *Já está no ar* · "Ligue o primeiro ajuste hoje" |
| #8 (peça irmã, mesmo módulo) | *Já está no ar* · "Abra o painel e deixe ligado hoje" |
| #10 (era) | *Como começar* · "O entregador entra no mapa com dois cadastros" |

O molde da casa é chapéu **Já está no ar**, título no imperativo com **hoje**,
subtítulo com o primeiro passo mais a linha de fechamento da série, e a pílula
de caminho. Esta peça tinha abandonado os quatro.

Ficou: **"Monte a sua primeira rota hoje"**, com o caminho apontando para
`Delivery → Entregas` — o módulo que a peça vendeu — e não mais para
`Aplicativos → Entrega → BeeFood Entregador`, que é assunto de um slide do meio.

A linha de disponibilidade é **fato publicado**, não promessa nossa: a novidade
do Painel para Entregadores diz que ele *"está incluso no módulo Entrega, junto
da Gestão de Entregas"*. Por isso a frase é condicional — quem **tem** o módulo
Entrega já tem isto — em vez de "todo mundo já tem", que o módulo em liberação
não sustenta.

**A imagem caiu junto**, e pelo teste de imagem da revisão: a primeira era o
aplicativo **vazio**, com "Nenhuma entrega agora". Tela em que não acontece nada
é a pior arte possível para fechar uma venda — e ela só existia porque a copy
velha precisava dela ("lista vazia é sinal de que deu certo"). Trocado o texto,
a arte virou órfã na hora.

A segunda tentativa foi a **lista de rotas** cortada nas duas rotas. Ela prova o
título, e o dono resolveu por outro caminho: *"coloque a foto do mapa e o pc na
última com essa frase"*. Ficou o **mapa no notebook — o mesmo da capa**, no
mesmo lugar e no mesmo tamanho.

A decisão é melhor do que a minha, e o motivo é de forma: **a peça abre e fecha
na mesma cena.** A capa apresenta a tela e faz o leitor parar de rolar; o nono
slide devolve a mesma imagem inteira, agora com um imperativo em cima, para quem
já sabe ler cada coisa dali — a rota A tracejada, as paradas numeradas, o Diego
e o Marcos com nome no mapa. A lista de rotas provava o título de perto demais,
e fechar a peça num recorte é terminar olhando para um detalhe.

É a única vez em que **repetir a prova dentro da mesma peça** é a decisão certa,
e a condição é estreita: vale no CTA, porque o assunto dele é literalmente "abra
isto", e vale com a imagem da **capa**, que é a que o leitor reconhece. Repetir
a prova de um slide do meio seria só falta de arte.

Com isso `app-pronto.png` e `telas/app-pronto.html` **saíram da pasta**. Desenho
que nenhum slide usa não é acervo, é andaime — é o mesmo critério que tirou as
oito tiras de rolagem da sondagem. `lista-rotas.png` fica: ela continua sendo a
referência do desenho do slide 3.

### O notebook da capa alternativa não diminui

A sexta linha do retorno: *"slide 1 com celular + pc — o pc diminuiu pq? apenas
incluir o celular"*. A primeira versão reduziu o aparelho de 936 para 776 px
para abrir espaço lateral, e isso quebra o contrato da capa alternativa: as duas
versões precisam ser **trocáveis**, e aparelho de tamanho diferente muda o peso
do slide inteiro — deixa de ser a mesma capa com uma coisa a mais e vira outra
composição.

O notebook voltou aos 936 px, no mesmo lugar, e o celular entra **na frente**,
encostado na quina direita dele. Ele cobre o canto direito do mapa, e esse é o
preço certo: ali não passa rota desenhada, e a sobreposição é justamente o que
faz os dois aparelhos lerem como uma mesa em vez de dois recortes lado a lado.

### Duas coisas que só a releitura das imagens novas pegou

Desenhar seis telas cria um tipo de erro que a captura não tem: o desenho
**concorda com o texto que o acompanha**, porque as duas coisas saíram da mesma
cabeça na mesma hora. Duas passaram na primeira leitura:

- **o avião do despacho não era um avião.** O slide 3 fecha com *"Ela ganhou
  dono, e o avião de despachar apareceu"* — e o ícone desenhado era `&#10148;`,
  uma seta dentro de um círculo. A captura de produção
  (`imagens-puras/lista-rotas.png`) mostra um avião de papel, sem círculo, e o
  manual do despacho automático chama o botão de **Avião** na tabela dele.
  Virou um SVG de avião de papel, na cor e no tamanho da captura. Legenda que
  nomeia um ícone é uma afirmação sobre a tela, e vale o mesmo cuidado de
  qualquer outra;
- **a cobertura do relatório de operação não fechava.** O cartão dizia
  *"Com base em 96% dos pedidos · 2 entregas acima de 4 h ficaram fora"*, e 96%
  de 128 são 123 — que sai com **cinco** fora, não duas. O 96% tinha vindo da
  análise de prazos, que é outro recorte (123 pedidos com prazo prometido pelo
  canal) e coincidia no número. Ficou 98% e três entregas, que é a mesma conta
  dos dois lados. Dado de exemplo tem de aguentar a soma: quem lê relatório lê
  conferindo, e um número que não fecha estraga a confiança nos outros cinco.

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

### A capa tem duas versões

`capa-alternativa/slides/01-capa-pc-e-celular.html` traz o notebook **no mesmo
tamanho e no mesmo lugar** da capa principal, com o celular da rota na frente,
encostado na quina direita dele. O texto é **igual palavra por palavra**, para
as duas serem trocáveis sem reescrever nada, e a escolha é de quem publica:

- **só notebook** — o mapa fica limpo de ponta a ponta: as duas rotas
  tracejadas, as paradas numeradas e o nome dos motoboys ao lado do pino. É a
  capa que prova melhor a frase *numa tela só*;
- **notebook + celular** — a capa já diz "tem painel e tem aplicativo" sem
  gastar linha de texto, e o preço é o celular cobrir o canto direito do mapa.
  Vale quando o post vai para quem ainda não sabe que existe app do entregador.

É a mesma troca da #2, que tem `capa-alternativa/01-capa-so-totem.html` pelo
motivo inverso: lá a alternativa **tira** um aparelho para o outro respirar.
A pasta é separada porque o `renderizar.py` transforma em PNG todo `.html` de
`slides/`, e duas capas na mesma pasta virariam um carrossel de dez imagens com
dois slides "1 de 9". O `empacotar.py` põe a alternativa numa subpasta do zip.
