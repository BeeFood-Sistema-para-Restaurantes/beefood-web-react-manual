# O que o acompanhamento do cliente faz de verdade — lido no código

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `gestao-entregas-rastreio-cliente.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

**A fonte não é um clone.** O rastreio mora no **cardápio digital**, que é um projeto Nuxt 2
próprio, em repositório separado — e não é nem o `beefood-web-react` nem o backend
`beetech-server-node-2.0` (este continua inacessível nesta VM: as quatro combinações de token do
Bitbucket falham com *"You may not have access to this repository"*, como já registrado na seção 8
da `MEMORIA-GERAL.md`).

O que deu para ler é o **código publicado**: `https://menu.beefood.com.br/beefood3` serve o bundle
do Nuxt, e ele tem todas as frases, todos os intervalos e toda a lógica de tela. Como achar de
novo, em quatro passos:

```bash
# 1. a página traz os chunks de entrada
curl -s https://menu.beefood.com.br/beefood3 | grep -o '/_nuxt/[^"]*\.js'

# 2. o chunk grande tem o mapa de rotas e o mapa de hashes de chunk
#    (procurar por "rastreio" devolve a rota e os componentes)
#    rota: { path: "/:cardapioID/rastreio/:token?", name: "cardapioID-rastreio-token" }
#    componentes: RastreioIconeLoja, RastreioIconeMoto, RastreioMapaRastreio,
#                 RastreioPainelAcompanhamento; layout _rastreio = LayoutRastreio

# 3. a rota carrega os chunks 16 e 166; o mapa de hashes traduz o número em arquivo
#    16 -> /_nuxt/1d9bfa7.modern.js   (PainelAcompanhamento + MapaRastreio)
#   166 -> /_nuxt/a42e4e0.modern.js   (a página, o ProgressoPedido e o módulo de frases)

# 4. a tela do pedido, que hospeda a linha "Acompanhar entrega", está no chunk 13
#    13 -> /_nuxt/4a13c5f.modern.js
```

Os hashes mudam a cada publicação; o caminho para redescobri-los não muda. Conferido em
23/09/2026.

## As peças

| Peça | Papel |
|---|---|
| Página `/:cardapioID/rastreio/:token?` (`PaginaRastreio`) | o que o link do WhatsApp abre. Só repassa o token ao painel, com `altura: 100vh` |
| `PainelAcompanhamento` | a tela inteira do acompanhamento: cabeçalho, mapa, folha de baixo, e **o relógio que consulta o servidor** |
| `MapaRastreio` | o mapa Leaflet, os três pinos e o traço pontilhado |
| `ProgressoPedido` | a barra de quatro etapas |
| módulo de frases (`ESTADOS`, `titulo`, `detalhe`, `podeMostrarMapa`, `intervalo`) | **todo** o texto que a tela escreve, e o ritmo de atualização |
| Detalhe do pedido em *Pedidos* | hospeda a linha *Acompanhar entrega*, o mapa de 200 px e a tela cheia em modal |

## Os cinco estados, e o texto de cada um

O servidor devolve um `estado`, e a tela **não** monta frase por conta própria:

```js
ESTADOS = { PREPARANDO, NA_FILA, A_CAMINHO, SEM_SINAL, ENTREGUE }
```

`titulo(rastreio)` — a frase grande:

| Entrada | Saída |
|---|---|
| ainda carregando | `Carregando…` |
| `expirado: true` | `Este link expirou` |
| `ENTREGUE` | `Pedido entregue às HH:MM` (a hora sai de `pedido.entregueEm`, posições 11 a 16 do texto); sem ela, `Pedido entregue` |
| `A_CAMINHO` | `{nome} está indo até você`; **sem nome**, `Seu pedido está a caminho` |
| `NA_FILA` | `{nome} saiu para entrega`; **sem nome**, `Seu pedido saiu para entrega` |
| `SEM_SINAL` | `Seu pedido está a caminho` |
| resto | `pedido.situacao === 'PRONTO'` → `Pedido pronto, aguardando o entregador`; senão `Seu pedido está sendo preparado` |

`detalhe(rastreio)` — a linha de baixo:

| Estado | Saída |
|---|---|
| `NA_FILA` | com `fila.posicao` e `fila.total`: `total <= 1` devolve **nada**, senão `Você é a {posicao}ª de {total} paradas desta viagem.` Sem objeto `fila`: `Há outra entrega antes da sua.` |
| `A_CAMINHO` | `distanciaMetros` abaixo de 1000 → `A {arredondado a 10 m} m de você, em linha reta.`; a partir de 1000 → `A {km com uma decimal e vírgula} km de você, em linha reta.` |
| `SEM_SINAL` | `Localização indisponível no momento.` |
| `PREPARANDO` | `Avisaremos assim que sair para entrega.` |
| `ENTREGUE` e expirado | nada |

Daí saem duas afirmações do manual que **não** são suposição: a distância é arredondada de dez em
dez metros (`10 * Math.round(m / 10)`), e o nome que aparece é o que o servidor mandou em
`entregador.nome` — a tela não corta nem formata nada, então "Funcionário 1" sai inteiro.

`textoAtualizacao`, no cartão do entregador:

| `entregador.atualizadoHaSegundos` | Texto |
|---|---|
| ausente | `Posição em tempo real` |
| menos de 60 | `Posição atualizada agora` |
| 60 ou mais | `Posição de {minutos} min atrás` |

E quando o token não é reconhecido, o cabeçalho troca de conteúdo: `Esse pedido não tem rastreio` +
`O link pode ter expirado, ou esta entrega não está sendo acompanhada.`

## As duas rotas de leitura

```
GET https://cardapio-digital.beetechapi.be/api/rest/tempresaDelivery/rastreio/{token}
GET https://cardapio-digital.beetechapi.be/api/rest/tempresaDelivery/rastreioPedido/{empresaID}/{filialID}/{preVendaID}
```

A primeira é a do link do WhatsApp. A segunda é a **segunda porta**: a tela do pedido a chama em
`iniciarAcompanhamento()` e recebe o `token` de volta no corpo — é por isso que o cliente acompanha
sem nunca ter visto a mensagem.

As duas respondem `{"encontrado": false}` quando o token não vale. Medido em 23/09/2026:

```
$ curl -s .../rastreio/aaaaaaaaaaaaaaaaaaaaaa
{"encontrado":false}        HTTP 404
```

**E o token do pedido deste manual já responde a mesma coisa.** O link da captura
(`.../rastreio/7Kq2XbVn4pHs9dTmRcJw1e`, 22 caracteres) foi sondado no fim da tarde do mesmo dia da
entrega e devolveu `encontrado: false`. Vale a distinção para o FAQ: **link vencido não cai
necessariamente em *"Este link expirou"***. Esse texto exige que o servidor ainda conheça o token e
responda `expirado: true`; quando ele já não conhece, o cliente vê *"Esse pedido não tem rastreio"*.

## O relógio: quem manda no ritmo é o servidor

```js
intervalo(r) = r.proximaLeituraSegundos == null ? null : 1000 * Math.max(5, r.proximaLeituraSegundos)
```

Três consequências:

1. **A tela não tem intervalo fixo.** O servidor diz quando voltar; o front só impõe um **piso de
   5 segundos**. Por isso o manual fala em "dez ou vinte segundos" (o ritmo observado) sem cravar
   um número como se fosse constante do produto.
2. **`proximaLeituraSegundos` ausente para o relógio.** É assim que o acompanhamento se encerra
   sozinho depois da baixa, sem ninguém chamar `clearTimeout`.
3. **Aba escondida não consulta.** `visibilitychange` cancela o `setTimeout` quando
   `document.hidden`, e chama `atualizar()` na hora em que a aba volta.

## O mapa

| Item | Regra |
|---|---|
| Biblioteca | Leaflet, com camada `Canvas/World_Light_Gray` da ArcGIS e atribuição *Esri, HERE, Garmin, OpenStreetMap* |
| `maxZoom` | 16 |
| Pino da loja | quadrado arredondado de 38 px com a `loja.logo`; `onerror` cai para o ícone genérico `IconeLoja` |
| Pino do destino | gota escura `#111827` |
| Pino do entregador | `IconeMoto` com um anel pulsando (animação CSS de 1,8 s) |
| Cor da loja e da moto | `var(--v-corPrimariaEmp)` — **a cor primária do seu cardápio** |
| Traço | `l-polyline` cinza, tracejado `6 8`, opacidade 0,55, ligando **entregador → destino** (ou **loja → destino**, sem entregador). Não é rota: é referência de distância |
| Enquadramento | `fitBounds` sobre os pinos existentes, refeito a cada mudança de pino e por `ResizeObserver` |
| Coordenada `0, 0` | tratada como **ausente** — é o que evita pino no Golfo da Guiné |
| `scrollWheelZoom` | desligado: a roda do mouse rola a página, não dá zoom |
| `dragging` | ligado só quando `interativo` (a tela cheia) ou no desktop. No celular, arrastar o mapa **pequeno** do pedido rola a página |

`podeMostrarMapa` = não expirado **e** (destino com coordenada **ou** loja com coordenada). Ou
seja: endereço sem geolocalização não mata o mapa — ele abre com a loja e a moto, e o que se perde
é o pino de destino e a distância (item 3 dos pré-requisitos do manual).

Quando não pode, o lugar do mapa recebe uma frase:

| Situação | Frase |
|---|---|
| token não encontrado | `Sem acompanhamento para este link.` |
| `expirado` | `Este link expirou.` |
| `ENTREGUE` | `Entrega concluída.` |
| resto | `O mapa aparece quando o pedido sair para entrega.` |

## A barra de progresso

Quatro etapas, com a situação numérica do ERP (`AGUARDANDO 1`, `PREPARO 2`, `PRONTO 2.5`,
`ENTREGA 3`, `ENTREGUE 4`, `CANCELADO 5`, `PIX 6`):

| Etapa | Rótulo (entrega) | Rótulo (retirada) |
|---|---|---|
| 1 | Pedido enviado para o restaurante | Pedido enviado para o restaurante |
| 2 | Pedido sendo preparado | Pedido sendo preparado |
| 3 | Pronto, aguardando o entregador | Pronto para retirada |
| 4 | Saiu para entrega | Aguardando você |

Cada etapa recebe duas classes por dois testes, e é isso que explica a leitura das barras nas
capturas:

```js
feita: situ > etapa.situ      // cheia
atual: situ === etapa.situ    // piscando (animação de opacidade, 1,4 s)
```

Ou seja, **a etapa atual é a que pisca, não a última cheia**. Em *Saiu para entrega* (`situ` 3) as
três primeiras estão `feita` e a quarta está `atual` — três barras cheias e a quarta piscando, que
foi exatamente o que a captura mostrou e o que a primeira versão do manual leu errado ("a terceira
barra acendeu").

A seta para baixo ao lado do estado alterna `expandOrderStatus`, e a lista é filtrada por
`!!expandOrderStatus || 1 == e.current`: **fechada mostra só a etapa atual, aberta mostra todas as
já cumpridas**, cada uma com a sua hora (`statusList` monta `time` de `dataSitu3`,
`dataSituPronto`, `dataSitu2` e `dataSitu1`, e filtra por `situ >= situNumber`).

Outras três frases conferidas na mesma varredura, porque o manual as afirma:

```js
resumoItens = produtos.reduce((t, a) => t + (Number(a.qtd) || 0), 0)   // soma QUANTIDADE
            === 1 ? '1 item do pedido' : `${n} itens do pedido`
situ === 5  ? 'Pedido cancelado' (faixa #FFCDD2, mdi-close vermelho)
            : 'Pedido concluído' (faixa #E0E0E0, mdi-check-circle verde)
order.nota  ? 'Pedido avaliado' : 'Avalie seu pedido'
```

O contador de itens soma a **quantidade**, não o número de linhas — dois do mesmo lanche dão
*2 itens do pedido*. E o cartão de avaliação só aparece com `situacaoPedido === 'ENTREGUE'` ou em
pedido presencial.

E o cabeçalho do pedido troca de número conforme o estado: em andamento é
`Pedido nº{numeroPedido} ({numeroPreVenda})`; no cartão de avaliação do pedido concluído é
`Pedido nº{numeroPreVenda} | {data}`, **só o interno**.

## Onde o acompanhamento aparece dentro do pedido

```js
cabeRastreio = !isPresencial && emAndamento && order.tipoPedido === 'entrega'
```

Três portas fechadas de uma vez, e é o que sustenta as duas fronteiras da seção 2 do manual:

- **presencial não tem** (mesa, comanda, balcão);
- **retirada não tem** (`tipoPedido` precisa ser `entrega`);
- **pedido fora de andamento não tem** — `emAndamento` é `situ < ENTREGUE`, então depois da baixa a
  linha de acompanhamento **sai da tela do pedido**. O link do WhatsApp continua, porque ele fala
  com a rota de token, não com a tela.

O título da linha clicável:

```js
tituloCta = rastreio?.entregador?.nome ? titulo(rastreio) : 'Acompanhar entrega'
detalhe   = detalhe(rastreio) || 'Veja no mapa onde está seu pedido'
```

Ou seja, a mesma linha é *"Acompanhar entrega / Avisaremos assim que sair para entrega."* antes do
despacho e *"Carlos está indo até você / A 640 m de você, em linha reta."* depois — **não são dois
componentes**, é o mesmo, com o nome do entregador como chave.

### O que faz a tela do pedido se atualizar

Aqui está o achado mais útil do estudo. Antes deste recurso a tela do pedido só tinha o seu próprio
relógio de situação:

```
GET api/rest/tempresaDelivery/situacaoDelivery/{preVendaID}
```

Agora, **quando existe token**, ela abandona esse relógio e passa a usar a leitura do rastreio:
`aplicarRastreio()` emite `onChangeSituacao` com `situacao`, `dataHoraPedido`, `dataHoraAceito`,
`dataHoraPronto` e `dataHoraSaiuEntrega`. É por isso que o estado, a barra de etapas e o mapa mudam
no **mesmo** instante — é uma leitura só, não duas. Sem token, o comportamento antigo continua.

### A tela cheia, e o voltar do navegador

`abrirAcompanhamento()` não troca de página: abre um `v-dialog fullscreen` e **empurra histórico**
com `?orderID={preVendaID}&acompanhar={token}`. `fecharAcompanhamento()` chama `history.back()`.

Por isso o voltar do navegador (e o botão físico do Android) fecha o mapa e devolve o cliente ao
pedido, em vez de tirá-lo do site — a promessa que o manual faz na seção 5. `aoVoltarNavegador` e
`sincronizarModalComUrl` mantêm modal e URL de acordo, inclusive quando o cliente abre a URL já com
`?acompanhar=`.

Um detalhe de economia: enquanto a tela cheia está aberta, a tela de trás **cancela** o próprio
relógio (`watch: modalAcompanhamento`), e a modal devolve cada leitura pelo evento `atualizado`
(`aproveitarLeituraDaModal`). Nunca há dois leitores ao mesmo tempo.

## Privacidade, no código

```js
head: { meta: [{ hid: 'robots', name: 'robots', content: 'noindex, nofollow' }] }
```

A página de rastreio pede para **não** ser indexada. Somado ao token de 22 caracteres, é o que
sustenta a frase do manual: o link é secreto por ser imprevisível, não por ter senha.

## O que ficou por confirmar (é do servidor, e não há clone)

Estas três regras vêm do briefing do dono, não do código lido. Nenhuma contradiz o que o front faz,
e o front tem o tratamento para todas elas — mas o número exato está no backend:

| Regra | Onde ela apareceria |
|---|---|
| o link só é anexado com **posição dos últimos 15 minutos** | quem monta a mensagem de *saiu para entrega* |
| o link **expira 2 horas depois da entrega** | quem responde `expirado: true` |
| o celular do entregador manda posição a cada **10 a 20 segundos** | o aplicativo do entregador + `proximaLeituraSegundos` |

O front trata as três sem saber os números: ele desenha o que `expirado`, `SEM_SINAL` e
`proximaLeituraSegundos` mandarem. Quando o backend voltar a clonar, o lugar de conferir é a rota
`tempresaDelivery/rastreio` e o montador da notificação de delivery.
