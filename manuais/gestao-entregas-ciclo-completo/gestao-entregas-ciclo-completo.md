# Uma entrega do começo ao fim: painel e aplicativo lado a lado

> 🚧 **ESQUELETO — NÃO PUBLICAR AINDA.** O texto está pronto e conferido; faltam as **13 imagens**,
> marcadas uma por uma ao longo do arquivo. Seis são fotos do celular, que só existem com o painel
> agindo ao mesmo tempo, e sete são capturas do painel, que só valem se forem do **mesmo pedido** das
> seis. O roteiro dessa janela está em
> [`janela-117.md`](../gestao-entregas/pedidos/janela-117.md), e o cenário é montado por
> [`smoke-app.js`](../gestao-entregas/scripts/smoke-app.js). Detalhe em [`MEMORIA.md`](MEMORIA.md).

Os outros manuais da Gestão de Entregas ensinam uma tela cada. Este conta **uma história**: três
pedidos prontos no balcão, um entregador na porta, e o que acontece nas duas telas — a do operador e
a do celular — de um lado ao outro do percurso.

Serve para duas pessoas diferentes lerem a mesma coisa. O operador descobre o que o entregador vê
quando ele clica; o entregador descobre de onde vem o que aparece no celular dele. É a conversa que
normalmente acontece por telefone, no meio do turno.

> **Não é um manual de primeira leitura.** Se você nunca montou uma rota, comece em
> [Montar a rota](../gestao-entregas-montar-rota/gestao-entregas-montar-rota.md). Aqui cada passo
> aponta o manual que o explica em detalhe.

## Para que serve

- Entender o ciclo inteiro numa leitura, sem pular entre sete manuais.
- Saber, em cada clique do painel, o que muda no celular do entregador — e quando **não** muda nada.
- Treinar operador novo: é o roteiro de um turno, na ordem em que ele acontece.

## Antes de começar

- Um entregador cadastrado, com acesso ao aplicativo — veja
  [Liberar o entregador](../gestao-entregas-liberar-entregador/gestao-entregas-liberar-entregador.md).
- O entregador **online** no aplicativo. Todo o resto funciona sem isso, menos o pino no mapa.
- Pedidos com endereço e coordenada, ou seja, área de entrega configurada.
- **Caixa aberto** na filial, se a cobrança for na porta.

---

## O ciclo, em sete momentos

| Momento | O operador faz | O entregador vê |
|---|---|---|
| 1. Os pedidos prontos | a fila de quem espera entrega | **nada** |
| 2. A rota montada | agrupa e escolhe quem leva | a rota chega na lista |
| 3. O despacho | um clique que avisa o mundo | a rota vira **em rota** |
| 4. A rua | o pino andando no mapa | o Maps aberto |
| 5. A porta do cliente | a parada mudando de estado | cobra e dá baixa |
| 6. O fim da viagem | encerra a rota | a lista esvazia |
| 7. O dia seguinte | o relatório soma | o histórico guarda |

A linha mais importante da tabela é a primeira: **no momento 1 o celular do entregador está vazio**.
Pedido pronto não é pedido atribuído, e é a confusão número um da operação — o operador jura que
"mandou", o entregador jura que "não chegou", e os dois estão certos.

---

## 1. Os pedidos prontos, e o celular vazio

O ciclo começa na fila. Três pedidos saíram da cozinha, estão com endereço reconhecido e esperam
alguém para levar.

> ⏳ **Falta a imagem `01-fila-de-pedidos.png`** — capturo eu, no painel.
> A fila com os três pedidos prontos e o pino do entregador parado na loja.

O entregador já está online — o pino dele aparece no mapa, na loja. Mas a lista no celular dele está
**vazia**, e vai continuar vazia até alguém decidir quem leva o quê.

> É a primeira coisa a saber sobre o módulo: o que põe um pedido na tela do entregador é **ter
> entregador atribuído**, não estar pronto. Pedido pronto sem atribuição é pedido que ninguém viu.

Quem quer o vocabulário desta tela — os selos, os contadores, as cores do pino — tem o manual
[Ler o mapa e o painel de entregas](../gestao-entregas-mapa-painel/gestao-entregas-mapa-painel.md).

---

## 2. A rota montada, e a rota que chega

O operador marca os três pedidos, agrupa numa rota e escolhe o entregador.

> ⏳ **Falta a imagem `02-rota-montada.png`** — capturo eu, no painel.
> O painel de rotas com a rota A montada, três paradas e o entregador escolhido.

Neste instante, e antes de qualquer despacho, **a rota já aparece no celular**. É o detalhe que
surpreende quem vem de outro sistema: atribuir é o suficiente.

> ⏳ **Falta a imagem `03-rota-no-app.png`** — foto do emulador, do dono.
> A lista com o grupo ROTA recém-chegado, *0 de 3*, e o INICIAR ROTA verde.

O que o entregador vê:

| No celular | O que significa |
|---|---|
| O grupo **ROTA A** com as três paradas | a rota do operador, na ordem que o operador montou |
| **0 de 3 entregas** | nenhuma concluída ainda |
| O botão verde **INICIAR ROTA** | ele pode partir sem esperar o painel |

O **INICIAR ROTA** é a parte que confunde os dois lados. Ele existe para o caso comum de o
entregador já estar com os pedidos na mão, e o operador ainda não ter clicado em despachar. Se o
entregador tocar nele, o efeito é o mesmo do despacho: o cliente é avisado, o marketplace é
informado, e não há volta. O botão desaparece da tela depois disso.

Detalhe de cada tela: [Montar a rota](../gestao-entregas-montar-rota/gestao-entregas-montar-rota.md)
no painel, e
[App do entregador: chegar no endereço](../app-entregador-rota/app-entregador-rota.md) no celular.

> **A ordem das paradas é a do operador, e ela é frágil.** O botão **MELHOR ROTA** do aplicativo
> reordena tudo por distância a partir da loja, e a sequência que o painel montou desaparece. Se a
> ordem importa — item frágil, cliente que fechou mais cedo, bairro com trânsito —, diga ao
> entregador para não tocar nele.

---

## 3. O despacho: um clique que avisa o mundo

O operador clica no avião. É o clique mais importante do módulo, e o único deste manual que não tem
desfazer.

> ⏳ **Falta a imagem `04-confirmar-despacho.png`** — capturo eu, no painel.
> A janela de confirmação do despacho, com o nome do entregador e as três paradas.

De uma vez, para os três pedidos:

| O que acontece | Quem sente |
|---|---|
| o pedido passa para **Em entrega** | o Delivery, o caixa e o fechamento do dia |
| sai a mensagem de **pedido saiu para entrega** | o cliente, no WhatsApp |
| o marketplace é avisado | iFood, 99Food, aiqfome e os demais canais |
| a impressão de entrega dispara | a impressora da loja |

No celular, a mudança é discreta e importante: o cabeçalho da rota passa a mostrar a etiqueta **em
rota**, e o **INICIAR ROTA** verde dá lugar ao **ABRIR NO MAPS**.

> ⏳ **Falta a imagem `05-em-rota-no-app.png`** — foto do emulador, do dono.
> O cabeçalho da rota com a etiqueta *em rota* e o botão ABRIR NO MAPS.

Tocando na primeira parada, o entregador vê o que precisa para tocar a campainha: endereço com
complemento, telefone, os itens e — a linha que ele olha primeiro — **Cobrar R$**.

> ⏳ **Falta a imagem `06-primeira-parada.png`** — foto do emulador, do dono.
> Os detalhes da primeira parada: endereço com complemento, itens e Cobrar R$.

Detalhe de cada tela:
[Despachar a rota](../gestao-entregas-despachar/gestao-entregas-despachar.md) no painel, e
[App do entregador: as entregas do dia](../app-entregador-entregas-do-dia/app-entregador-entregas-do-dia.md)
no celular.

> **A ordem certa é cozinha pronta → entregador na porta → despachar.** O sistema deixa despachar
> pedido em preparo, e o resultado é um cliente avisado esperando por um pedido que ainda está no
> forno.

### Há um segundo caminho para chegar aqui

Em loja com balcão movimentado, quem despacha é o próprio entregador, lendo a etiqueta de código de
barras do cupom com a câmera do aplicativo. O efeito é idêntico ao do avião do painel — e é por isso
que **ler o código é despachar**, não conferir.

Está em
[Código de barras: ligar a etiqueta e ler o pedido](../app-entregador-codigo-barras/app-entregador-codigo-barras.md).

---

## 4. A rua

O entregador toca em **ABRIR NO MAPS** e o telefone assume. Do ponto de vista do sistema, é a fase
mais silenciosa do ciclo: nenhuma tela muda de estado, e a única coisa que acontece é o aplicativo
mandando a posição a cada poucos minutos.

No painel, essa posição vira o pino andando.

> ⏳ **Falta a imagem `07-mapa-ao-vivo.png`** — capturo eu, no painel.
> O mapa com o pino longe da loja e o traçado da rota.

É aqui que o segundo aviso de WhatsApp pode sair: o **entregador está próximo**, disparado quando a
distância até o cliente entra no raio configurado. Ele não sai sozinho — depende de uma configuração
que precisa ser **salva uma vez** por loja, e é a armadilha explicada em
[Avisos de WhatsApp da entrega](../gestao-entregas-avisos-whatsapp/gestao-entregas-avisos-whatsapp.md).

> **Pino parado não é entregador parado.** Antes de ligar para ele, olhe a bateria e a idade da
> última posição na lista de entregadores. Celular em economia de energia para de mandar
> localização, e o pino congela no último ponto.

---

## 5. A porta do cliente

O entregador chega, entrega, e cobra. No aplicativo, essas três coisas são **uma só ação**: registrar
o pagamento dá baixa na entrega. Não existe "cobrei mas não finalizei".

> ⏳ **Falta a imagem `08-cobranca-concluida.png`** — foto do emulador, do dono.
> A tela de sucesso depois de registrar o pagamento da primeira entrega.

O que ele fez, em quatro toques: **INICIAR COBRANÇA**, escolher a forma, conferir o troco, confirmar.
Se a conta for dividida entre duas pessoas, a soma das partes tem de fechar com o total — é a única
regra rígida da tela.

No painel, a parada muda de estado e o contador anda.

> ⏳ **Falta a imagem `09-uma-de-tres.png`** — capturo eu, no painel.
> A parada marcada como entregue e o contador em *1 de 3*.

Detalhe de cada tela:
[App do entregador: receber na porta](../app-entregador-cobranca/app-entregador-cobranca.md) no
celular, e
[Fechar a entrega no painel](../gestao-entregas-fechar-entrega/gestao-entregas-fechar-entrega.md) no
painel.

> **A baixa pode vir dos dois lados, e é melhor vir do celular.** O operador também consegue marcar a
> parada como entregue pelo painel — e deve, quando o entregador liga avisando que o aplicativo
> travou. Mas a baixa feita no celular é a que registra forma de pagamento e valor recebido. A do
> painel registra só que chegou.

### Quando o pedido é de plataforma

Pedido de iFood ou 99Food chega **já pago**: o **Cobrar R$** vem zerado e, no lugar do botão de
cobrança, aparece o botão de confirmação da plataforma. O entregador confirma ali, dentro do
aplicativo, e a entrega é dada por concluída no mesmo gesto.

Está em
[App do entregador: pedido de iFood e de 99Food](../app-entregador-marketplace/app-entregador-marketplace.md).

---

## 6. O fim da viagem

Concluída a terceira parada, o grupo da rota desaparece da lista do celular.

> ⏳ **Falta a imagem `10-lista-sem-a-rota.png`** — foto do emulador, do dono.
> A lista sem o grupo da rota, depois da terceira entrega.

E no painel a rota fica sem paradas abertas, pronta para o operador encerrar.

> ⏳ **Falta a imagem `11-rota-finalizada.png`** — capturo eu, no painel.
> A rota sem paradas abertas, e o botão de finalizar.

> **Finalizar a rota confirma tudo o que estiver pendente**, sem janela de confirmação e sem volta.
> Se houver uma parada duvidosa, resolva a dúvida antes de clicar.

A rota encerrada sai da tela, e é normal o operador achar que ela se perdeu. Ela não se perdeu —
[Fechar a entrega no painel](../gestao-entregas-fechar-entrega/gestao-entregas-fechar-entrega.md)
mostra onde achar o que já foi entregue.

---

## 7. O que sobra do dia

O ciclo acabou nas duas telas, e o que sobra é número.

No painel, o relatório **Desempenho › Delivery › Operação de Entrega** conta as três entregas do dia,
com tempo médio e distância.

> ⏳ **Falta a imagem `12-relatorio-do-dia.png`** — capturo eu, no painel.
> Operação de Entrega com a data de hoje, contando as três entregas.

No celular, o **Histórico** guarda as mesmas três, agrupadas por dia, com o que foi recebido em cada
uma.

> ⏳ **Falta a imagem `13-historico-do-dia.png`** — foto do emulador, do dono.
> O Histórico do dia com as três entregas e o que foi recebido.

As duas telas leem a **mesma data de entrega**, e é por isso que elas concordam. Se um dia elas
discordarem, é sinal de entrega que foi dada baixa depois da virada da meia-noite.

Os dois relatórios do módulo:
[Operação de Entrega](../relatorio-operacao-entrega/relatorio-operacao-entrega.md), que mede a
operação, e [Entregador (Taxa / KM)](../entregador-quanto-recebe/entregador-quanto-recebe.md), que
mede o quanto o entregador tem a receber.

---

## O mesmo ciclo, sem operador

Vale saber que existe um caminho em que os momentos 1 e 2 acontecem sozinhos: o **despacho
automático** agrupa os pedidos prontos e associa um entregador disponível, por conta própria, a cada
poucos minutos.

Ele **não despacha** — o clique do momento 3 continua sendo do operador — e ele só age em filial onde
alguém está com a tela de Gestão de Entregas aberta. As sete regras que ele usa estão em
[Despacho automático](../gestao-entregas-despacho-automatico/gestao-entregas-despacho-automatico.md).

---

## As cinco coisas que a operação de verdade ensina

1. **Pedido pronto não é pedido atribuído.** Se o entregador diz que não chegou nada, olhe a coluna
   de entregador antes de olhar o celular dele.
2. **Despachar avisa o cliente.** Não é um rótulo interno. Despachar cedo é mentir para o cliente.
3. **Cobrar é finalizar.** No celular não existe registrar pagamento e deixar a entrega aberta — e é
   por isso que o entregador deve cobrar **na porta**, não no carro.
4. **O botão MELHOR ROTA desfaz o trabalho do operador.** Se a ordem importa, combine antes.
5. **Pino parado quase sempre é bateria.** A lista de entregadores mostra a idade da última posição;
   ela responde a pergunta antes da ligação.

---

## Onde continuar

| Manual | O que cobre |
|--------|-------------|
| [Liberar o entregador](../gestao-entregas-liberar-entregador/gestao-entregas-liberar-entregador.md) | cadastro, acesso ao aplicativo e a etiqueta de código de barras |
| [Ler o mapa e o painel de entregas](../gestao-entregas-mapa-painel/gestao-entregas-mapa-painel.md) | o vocabulário da tela do operador |
| [Montar a rota](../gestao-entregas-montar-rota/gestao-entregas-montar-rota.md) | agrupar pedidos e escolher quem leva |
| [Despachar a rota](../gestao-entregas-despachar/gestao-entregas-despachar.md) | o clique que avisa o mundo, e o mapa ao vivo |
| [Fechar a entrega no painel](../gestao-entregas-fechar-entrega/gestao-entregas-fechar-entrega.md) | baixa por parada e encerramento da rota |
| [Despacho automático](../gestao-entregas-despacho-automatico/gestao-entregas-despacho-automatico.md) | as sete regras, e por que ele não despacha |
| [Avisos de WhatsApp da entrega](../gestao-entregas-avisos-whatsapp/gestao-entregas-avisos-whatsapp.md) | os quatro avisos, e o que liga o de proximidade |
| [App do entregador: instalar, entrar e ficar disponível](../app-entregador-entrar/app-entregador-entrar.md) | permissões, login e a pílula de disponibilidade |
| [App do entregador: as entregas do dia](../app-entregador-entregas-do-dia/app-entregador-entregas-do-dia.md) | a lista, os detalhes e o histórico |
| [App do entregador: chegar no endereço](../app-entregador-rota/app-entregador-rota.md) | ver no mapa, iniciar rota e melhor rota |
| [App do entregador: receber na porta](../app-entregador-cobranca/app-entregador-cobranca.md) | cobrança, divisão de conta e finalizar sem cobrar |
| [App do entregador: pedido de iFood e de 99Food](../app-entregador-marketplace/app-entregador-marketplace.md) | pedido de plataforma, já pago |
| [Código de barras](../app-entregador-codigo-barras/app-entregador-codigo-barras.md) | ligar a etiqueta no cupom e ler o pedido |
