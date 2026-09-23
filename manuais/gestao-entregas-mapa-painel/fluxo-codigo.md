# O que a tela faz de verdade — #105 Gestão de Entregas (mapa e painel)

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `gestao-entregas-mapa-painel.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

Lido em `beefood-web-react` e em `beetech-server-node-2.0/docs/gestao-entrega-2.0`, e
confirmado contra a API do sandbox. Serve para não escrever no manual coisa que a tela não
faz, e para explicar os números que o cliente vai ver.

## A tela e a rota

| | |
|---|---|
| Rota | `/gestao-entregas` |
| Porta | botão **Entregas** na barra da tela `/delivery` |
| Leitura | `GET /api/entrega2/gestao/painel/:empresaID/:filialID/:usuarioID` |
| Cliente da API | `src/lib/api/gestaoEntregas.ts` e `gestaoEntregasRota.ts` |
| Tipos | `src/types/gestaoEntregas.ts` |

## Uma leitura só monta a tela inteira

O `GET /painel` devolve tudo de uma vez: `loja`, `resumoPedidos`, `pedidos`, `entregadores`
e `rotas` (com as `paradas` dentro de cada rota). Não há chamada por pedido nem por
entregador — o que explica por que a tela inteira pisca junto quando atualiza, e por que o
"há N s" ao lado do Recarregar vale para todos os números da tela.

**O painel lê e também escreve.** O mesmo `GET` grava um `painel_heartbeat` (fire and
forget), que é como o servidor sabe que existe uma tela aberta. Isto tem uma consequência
que o manual precisa dizer: **o despacho automático depende da tela aberta**. O
`13-despacho-automatico.md` é explícito — o agrupamento roda no ciclo do painel, não num
cron.

> Para quem for montar cenário por script: chamar o `GET /painel` de fora **falsifica o
> heartbeat**. O `cenario.js` deste bloco passa `conferirPainel: false` ao seeder por isso.

## O que cada número da tela é

| Na tela | No `GET /painel` | Observação |
|---------|------------------|------------|
| selo *em preparação* | `resumoPedidos.emPreparo` | |
| selo *prontos* | `resumoPedidos.pronto` | |
| selo *em rota* | `resumoPedidos.emRota` | |
| selo *entregues* | `resumoPedidos.entregue` | do dia, não do período |
| "há 1h 22min" no cartão | `pedidos[].idadeMinutos` | minutos desde a confirmação |
| "151 m do restaurante" | `entregadores[].distanciaLojaMetros` | **linha reta**, calculada por Haversine |
| "há 2 min" do entregador | `entregadores[].posicaoIdadeMinutos` | idade da **última posição**, não do último toque |
| bateria | `entregadores[].bateria` | vem no ping de GPS |
| letra da rota | `rotas[].codigo` | `A`, `B`, … por filial e por dia |

### A janela de ±6 h

A lista de pedidos vem da `viewDeliveryFilaAguardandoEntrega`, que corta em **±6 horas**.
Pedido mais velho que isso **desaparece da tela sozinho**, sem cancelar nem entregar. Vale
para o manual como tranquilidade ("o lote de teste sai sozinho") e como aviso ("pedido
esquecido não fica acumulando na tela para sempre").

### `semLocalizacao`

O `resumoPedidos` traz `semLocalizacao`: quantos pedidos não têm coordenada. Eles aparecem
na **lista** e não no **mapa** — é a explicação de por que as duas contagens divergem, e é
o que o texto abaixo do mapa do relatório também diz com outras palavras.

## Situação do entregador: quem manda é o app

`entregadores[].status` é `OFFLINE`, `DISPONIVEL`, `PAUSA` ou `EM_ROTA`, e sai de
`entregador_status` no Aurora `beefood-entregas`. Quem escreve é:

- o **app**, pelo `POST /api/entrega2/gestao/presenca` (abre e fecha `entregador_sessao`);
- o **cron de timeout** (`10-timeout-presenca.md`), que derruba para `OFFLINE` quem parou
  de mandar sinal;
- a **própria rota**, que põe `EM_ROTA` ao despachar e devolve `DISPONIVEL` ao concluir.

**Não existe rota de API para o painel colocar alguém disponível.** Por isso o manual diz
que a mudança é sempre no aplicativo — não é escolha de redação, é o que a tela permite.

### `rotaIDAtual` e a rota fantasma

`entregador_status.rotaIDAtual` guarda a viagem em andamento. Quando ele aponta para uma
rota que já não existe, o entregador fica **ocupado para sempre**: o despacho automático o
ignora e o painel mostra vínculo com uma rota invisível. Não quebra nada e não aparece na
tela — só o dado direto denuncia. O `cenario.js limpar-fantasma` existe para isso, e vale
rodar antes de qualquer captura.

## Posição no mapa: o GPS não passa por este servidor

O ping de GPS do app vai para uma **Lambda de rastreamento**
(`06-lambda-rastreamento.md`), que escreve em `posicao` e atualiza `entregador_status`. O
painel só lê. Ou seja: o mapa pode mostrar entregador parado sem que nada esteja errado no
BeeFood — o que parou foi o celular.

O cron de distância (`08-cron-distancia-loja.md`) recalcula `distanciaLojaMetros`
periodicamente; o ping também já grava a distância do momento.

## Os selos são filtro de tela, não de dado

O clique no selo esconde a situação **no navegador**. Nada é salvo no servidor e nada muda
para os outros computadores do restaurante. A escolha da camada do mapa também é local.

## O que a tela **não** faz

- **Não** muda a situação de um pedido isolado (isso é a tela de Delivery).
- **Não** coloca entregador disponível nem em pausa.
- **Não** cria pedido.
- **Não** despacha sozinha: mesmo com o despacho automático ligado, a rota nasce parada e
  sair para a rua continua sendo um clique de alguém. O texto da própria janela do despacho
  diz isso.

## Cenário para as capturas

Montado com `manuais/gestao-entregas/scripts/cenario.js` (veja o cabeçalho do arquivo):

```bash
node cenario.js limpar-fantasma
node cenario.js semear --qtd 5 --offset 4
node cenario.js presenca --entregador 194115 --status DISPONIVEL
node cenario.js andar --entregador 194115 --para -23.5045,-47.4640 --passos 2
node cenario.js estado
```
