# MEMÓRIA — #117 Uma entrega do começo ao fim

Pasta: `manuais/gestao-entregas-ciclo-completo/` · Numeração: **#117** ·
Aberta em 18/09/2026 na sandbox **BeeFood3 - Manual** (`empresaID 38311`, `filialID 39202`,
entregador `194115`).

**Estado: esqueleto.** Texto escrito e conferido contra os onze manuais que ele costura; **13
imagens pendentes**, e nenhuma delas capturável agora. É o último dos catorze manuais do bloco, e o
único que não dá para fechar de um lado só.

## Por que ele não está pronto, e por que isso não é atraso

O #117 mostra **o mesmo pedido** nas duas telas. Não é uma escolha de estilo: é o que o dono pediu
quando descreveu a terceira parte do manual como *"juntar as peças"*. E é justamente isso que torna o
manual impossível de montar por partes.

Eu capturo o painel. Eu **não capturo o aplicativo** — não há emulador Android nesta máquina, e iOS
está fora de qualquer hipótese. Então as duas metades vêm de lugares diferentes.

Se eu capturasse o painel hoje, com os pedidos 1057 a 1059, e o dono fotografasse o celular amanhã,
o manual mostraria a rota `A` com três números de um lado e três números diferentes do outro. Um
leitor atento percebe em dois segundos, e a partir daí não acredita em mais nada. Um manual de
"lado a lado" com números que não casam é pior do que manual sem imagem.

Daí a decisão: **esqueleto com texto final**, e as duas metades capturadas na mesma janela. Quando as
seis fotos do celular chegarem, eu rodo a janela de novo, capturo os sete do painel com os **mesmos
pedidos** e o manual fecha numa rodada.

## O storyboard — as 13 imagens, na ordem do texto

| # | Arquivo | Lado | Quem captura | Fase da janela |
|--:|---|---|---|--:|
| 1 | `01-fila-de-pedidos.png` | painel | eu | 1 |
| 2 | `02-rota-montada.png` | painel | eu | 2 |
| 3 | `03-rota-no-app.png` | app | dono | 2 |
| 4 | `04-confirmar-despacho.png` | painel | eu | 3 |
| 5 | `05-em-rota-no-app.png` | app | dono | 3 |
| 6 | `06-primeira-parada.png` | app | dono | 3 |
| 7 | `07-mapa-ao-vivo.png` | painel | eu | 4 |
| 8 | `08-cobranca-concluida.png` | app | dono | 5 |
| 9 | `09-uma-de-tres.png` | painel | eu | 5 |
| 10 | `10-lista-sem-a-rota.png` | app | dono | 6 |
| 11 | `11-rota-finalizada.png` | painel | eu | 6 |
| 12 | `12-relatorio-do-dia.png` | painel | eu | 7 |
| 13 | `13-historico-do-dia.png` | app | dono | 7 |

Sete minhas, seis dele. As seis dele estão pedidas em
[`capturas-app.md`](../gestao-entregas/pedidos/capturas-app.md), pasta **18**, com os nomes de
arquivo que o zip deve trazer:

| No pedido | Vira aqui |
|---|---|
| `18-ciclo-completo/prints/01-rota-recebida.png` | `03-rota-no-app.png` |
| `18-ciclo-completo/prints/02-em-rota.png` | `05-em-rota-no-app.png` |
| `18-ciclo-completo/prints/03-primeira-parada.png` | `06-primeira-parada.png` |
| `18-ciclo-completo/prints/04-cobranca-concluida.png` | `08-cobranca-concluida.png` |
| `18-ciclo-completo/prints/05-lista-sem-a-rota.png` | `10-lista-sem-a-rota.png` |
| `18-ciclo-completo/prints/06-historico-do-dia.png` | `13-historico-do-dia.png` |

## O recorte

Sete momentos, na ordem cronológica de um turno. Não foi a primeira ideia: o rascunho anterior
organizava por tela — "o painel faz isto, o aplicativo faz aquilo" —, e ficou sendo um índice dos
outros onze manuais, sem história nenhuma.

O que salvou o recorte foi a tabela de sete linhas que abre o manual, e em especial a primeira delas:
**no momento 1 o celular está vazio**. Essa linha é o manual inteiro em miniatura. Ela responde a
confusão número um da operação — o operador jura que mandou, o entregador jura que não chegou — e
justifica a existência de um manual que costura os outros em vez de repeti-los.

A regra que segurou o tamanho: **cada momento explica o que muda nas duas telas e aponta o manual do
detalhe.** Nenhuma tabela de "Nº / Onde / O que é" aqui; elas moram nos onze. Este é o fio.

## O que o texto afirma, e de onde vem cada afirmação

Nada aqui foi deduzido: as onze afirmações que sustentam o manual saíram de captura ou de leitura de
código nas rodadas anteriores.

| Afirmação | Onde foi medida |
|---|---|
| pedido só aparece no app com entregador atribuído | `FuncionarioIDMotoboy` — a coluna que o `smoke-app.js` escreve para montar a lista |
| a rota chega no celular **antes** do despacho | conferido pela API do app com a rota em `ASSOCIADA`, no caso `rota-viva` |
| o INICIAR ROTA do app tem o mesmo efeito do avião do painel | #113, `fluxo-codigo.md` |
| despachar avisa cliente, marketplace e impressora | `SituacaoDeliveryUpdater`, lido no estudo do backend |
| MELHOR ROTA reordena por distância e desfaz a ordem do operador | #113, `fluxo-codigo.md` |
| ler o código de barras é despachar | #114, `fluxo-codigo.md` |
| cobrar é finalizar | #116, `fluxo-codigo.md` |
| o aviso de proximidade depende de um SALVAR por loja | #110 — `raioProximidadeMetros` NULL em 56.633 das 56.639 filiais |
| finalizar rota confirma tudo, sem confirmação e sem volta | #108, medido na captura |
| a rota encerrada sai da tela, não do sistema | #108 |
| o despacho automático agrupa e associa, mas não despacha | #109, e o `painel_heartbeat` que a minha própria visita gravou |

## A janela, e o que ela precisa

O roteiro está em [`janela-117.md`](../gestao-entregas/pedidos/janela-117.md): sete fases, e entre
elas as fotos. O cenário é montado por
[`smoke-app.js`](../gestao-entregas/scripts/smoke-app.js), comando `janela-117 --fase N`.

### O ensaio, e o que ele encontrou

Rodei as sete fases ponta a ponta em 18/09, com o painel aberto e o entregador simulado, para não
descobrir problema de roteiro no dia. As cinco telas do painel saíram como a tabela promete: a fila
com três pedidos, a rota `A` *Pronta para sair* com *0 de 3*, a rota *Na rua* com o pino andando e a
parada marcada *Entregando agora*, e o painel vazio com o contador de entregues subindo de 7 para 10.

Dois ajustes vieram do ensaio, e os dois teriam estragado foto:

1. **A fase 1 semeava os três pedidos com `offset 10`**, que são endereços a 5 e 10 km um do outro.
   Rota de três paradas espalhadas assim não é a rota que o manual conta. Passou a usar `offset 0`,
   que são os três endereços mais próximos entre si da lista do gerador — menos de 500 m.
2. **`limpar` tira o pedido da tela do app, mas não da fila do painel.** Pedido sem entregador
   continua em *Pedidos sem rota* por até 6 h, e depois de uma tarde de ensaios a fila tinha **21
   pedidos de teste**. A primeira foto do #117 é justamente "três pedidos prontos na fila". Nasceu
   daí o comando **`arquivar-fila`**, que manda os pedidos de teste para `AGUARDANDO` — estado que as
   duas telas ignoram e que **não** entra na conta de entregas do dia, como `ENTREGUE` entraria. E a
   fase 1 passou a **abortar** se achar lote antigo, em vez de deixar o problema aparecer na foto.

### Três coisas que precisam estar de pé

1. **Caixa aberto na filial.** Sem caixa, a cobrança da fase 5 falha, e a fase 5 é o coração do
   manual. Na medição de 18/09 **não havia caixa aberto** na 39202.
2. **A tela de Gestão de Entregas aberta do meu lado.** É ela que grava o `painel_heartbeat`, e sem
   heartbeat o despacho automático não age — o que atrapalha só se a janela for demonstrar isso.
3. **Nenhum lote antigo em nenhuma das duas telas.** Pedido de outro lote estraga as duas metades de
   uma vez, e é o erro mais fácil de cometer. `limpar` limpa a do app, `arquivar-fila` a do painel.

## Decisão registrada: por que não existe `annotate.py` aqui

Os outros manuais têm um `annotate.py` que recorta, mede e desenha as etiquetas numeradas. Este não
tem, e não é esquecimento: o script se escreve **em cima da imagem**, medindo coordenada por
coordenada. Sem as treze imagens, ele seria treze chutes.

Pelo mesmo motivo não existe `texto-documentation.ia.md`: o prompt de publicação depende da ordem
final das imagens, e publicar manual com marcador `⏳` no meio seria pior do que não publicar.

## O que fazer quando as fotos chegarem

1. Conferir se os três números do pedido nas fotos do app são os que a fase 1 imprimiu.
2. Rodar a janela de novo, com os mesmos números, e capturar as sete do painel.
3. Escrever o `annotate.py` e as etiquetas numeradas.
4. Apagar os treze marcadores `⏳` e o aviso 🚧 do topo.
5. Escrever o `texto-documentation.ia.md` e publicar.

Se as fotos **não** chegarem, o manual fica assim, e está registrado no `CHECKLIST-MANUAIS.md` como
pendente de captura — não como pendente de escrita.
