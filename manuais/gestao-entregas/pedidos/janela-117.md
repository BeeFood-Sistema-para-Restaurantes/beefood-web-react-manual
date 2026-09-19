# A janela combinada — o roteiro do #117, fase por fase

O **#117** é o manual que mostra o mesmo pedido nas duas telas: o operador monta a rota, o
entregador recebe, o operador despacha, o entregador anda, o cliente é avisado, o entregador dá
baixa, o painel muda. É o único do bloco que **não dá para fazer por partes** — ou as duas metades
são fotografadas no mesmo pedido, ou o manual mente.

Este arquivo é o roteiro dessa janela. Ele existe porque a alternativa — uma sessão corrida de
vinte minutos, com o emulador de um lado e o painel do outro — não sobrevive a nenhum imprevisto.
Em fases, cada foto tem o tempo que precisa, e um erro custa uma fase, não a janela.

**Quanto dura:** sete fases. Entre uma e outra, as fotos; o script espera.

## Antes de começar

| Lado | O que precisa estar de pé |
|---|---|
| Você, no celular | app **online**, permissões de localização e notificação **Ativas**, GPS fixado na loja: `adb emu geo fix -47.4657927 -23.5061438` |
| Você, no celular | **nada de outro cenário na lista.** Se houver, `node smoke-app.js limpar` antes |
| Eu, no painel | **a fila sem lote de teste antigo**: `node smoke-app.js arquivar-fila`. A fase 1 aborta se achar, porque a primeira foto é justamente a fila com três pedidos |
| Eu, no painel | a tela de Gestão de Entregas aberta na filial 39202 — é ela que grava o *heartbeat*, e sem *heartbeat* o despacho automático não age |
| A filial | **caixa aberto**, se a fase 5 for cobrar de verdade. Sem caixa, a cobrança na rua falha |

O entregador é o **194115** (`BeeFood3 - Manual`), o único com o app instalado no seu emulador.

## O comando

```powershell
node smoke-app.js janela-117              # lista as sete fases e as fotos de cada uma
node smoke-app.js janela-117 --fase 1     # roda a fase 1
```

Quem roda as fases sou eu, do painel, exceto onde a tabela disser o contrário. Cada fase imprime,
no fim, as fotos que ela destravou — e a linha do comando da próxima.

O estado fica num arquivo local (`.smoke-app-estado.json`) com os `preVendaID` da janela. É o que
permite a fase 3 mexer no pedido que a fase 1 criou: a sentinela de escrita do script só autoriza
`UPDATE` em pedido que ele conhece, e sem memória entre execuções as fases não existiriam.

---

> **O roteiro já foi ensaiado.** Rodei as sete fases ponta a ponta em 18/09, com o painel aberto e o
> entregador simulado, e as cinco telas do painel saíram como esta página promete: a fila com três
> pedidos, a rota `A` *Pronta para sair* com *0 de 3*, a rota *Na rua* com o pino andando e a parada
> marcada *Entregando agora*, e o painel vazio com o contador de entregues subindo de 7 para 10. O
> que o ensaio não cobre é a sua metade — e é só por isso que a janela existe.

## Fase 1 — três pedidos prontos, nenhum atribuído

Eu semeio três pedidos com endereço e coordenada, marco como **PRONTO** e ponho você disponível,
parado na loja. Os três endereços são os mais próximos entre si da lista do gerador, a menos de
500 m um do outro: rota de três paradas espalhadas por 10 km não é a rota que o manual quer contar.

| Quem fotografa | A cena |
|---|---|
| eu | a fila com os três pedidos e o mapa com o seu pin **online** |

O script imprime os três números. **Anote-os** — é o que faz as duas metades do manual casarem.
Nada aparece na sua tela ainda: pedido sem entregador não existe para o app.

## Fase 2 — a rota criada, e o app recebe

Eu agrupo os três numa rota e escolho você como entregador. A rota **não** é despachada.

| Quem fotografa | A cena | Arquivo |
|---|---|---|
| eu | o painel de rotas com a rota nova e o entregador escolhido | — |
| você | a lista com o grupo **ROTA** recém-chegado, *0 de 3* | `01-rota-recebida.png` |

É aqui que o **INICIAR ROTA** verde existe na sua tela. Ele desaparece depois do despacho, então é
a única fase em que essa foto é possível.

## Fase 3 — o despacho

Eu clico em despachar no painel. Três coisas acontecem de uma vez, e é por isso que esta fase é o
centro do manual: o ERP grava `ENTREGA`, o cliente recebe o aviso de saída no WhatsApp, e o
marketplace é informado nos pedidos que vierem de plataforma.

| Quem fotografa | A cena | Arquivo |
|---|---|---|
| eu | a rota despachada, com o carimbo de saída | — |
| você | o cabeçalho com a etiqueta **em rota** e o botão **ABRIR NO MAPS** | `02-em-rota.png` |
| você | os detalhes da primeira parada: endereço e **Cobrar R$** | `03-primeira-parada.png` |

> **Não toque em MELHOR ROTA nesta janela.** Ele reordena as paradas por distância e desfaz a ordem
> que o painel montou — e o manual está contando a história da ordem do operador. A melhor rota tem
> manual próprio (#113).

## Fase 4 — o entregador andando

Eu movo a sua posição em seis passos, da loja até a primeira parada, escrevendo no Aurora o mesmo
que a Lambda de rastreamento escreveria.

| Quem fotografa | A cena |
|---|---|
| eu | o mapa com o pin longe da loja e o rastro da rota |

Nada muda na sua tela. Se você preferir andar de verdade com o `adb emu geo fix`, melhor ainda — me
diga, e eu pulo esta fase.

## Fase 5 — a primeira entrega

**Esta fase é sua.** Quem dá a baixa é o entregador, na porta do cliente, porque é isso que o
manual mostra. Eu só confiro depois.

| Quem fotografa | A cena | Arquivo |
|---|---|---|
| você | a tela de sucesso depois de registrar o pagamento | `04-cobranca-concluida.png` |
| eu | a parada marcada como entregue e o contador em *1 de 3* | — |

O primeiro pedido da rota nasce em **dinheiro com troco para R$ 50,00**, de propósito: é a cobrança
com mais tela — forma, troco, conferência e confirmação. Depois de fotografar, rode
`node smoke-app.js conferir` e me avise: o painel e o app precisam contar a mesma história antes de
a fase 6 rodar.

## Fase 6 — o resto da rota, e o fechamento

Eu concluo as duas paradas que sobraram e finalizo a rota.

| Quem fotografa | A cena | Arquivo |
|---|---|---|
| eu | a rota sem paradas abertas, e depois finalizada | — |
| você | a lista sem o grupo da rota | `05-lista-sem-a-rota.png` |

Se você quiser dar baixa nas duas pelo app, melhor — me diga antes, e eu só finalizo a rota no fim.
O manual fica mais verdadeiro com as três baixas vindas do celular.

## Fase 7 — o depois

Eu tiro você de online e leio o relatório.

| Quem fotografa | A cena | Arquivo |
|---|---|---|
| eu | **Desempenho › Delivery › Operação de Entrega** com a data de hoje, já contando as três | — |
| você | o **Histórico** do dia com as três entregas | `06-historico-do-dia.png` |

É o fecho do manual: o ciclo que começou com três pedidos na fila termina como três linhas num
relatório. E é a única parte do #117 que prova que a operação do dia virou número.

---

## Se algo der errado no meio

| Aconteceu | O que fazer |
|---|---|
| a rota não chegou no app | `node smoke-app.js conferir`. Se a API mostra a rota e a tela não, puxe a lista para atualizar |
| a lista veio com pedido de outro lote | `node smoke-app.js limpar` e recomeçar da fase 1. Número trocado estraga as duas metades |
| a fase 1 abortou falando de lote antigo | `node smoke-app.js arquivar-fila`, e rode a fase 1 de novo |
| a cobrança falhou na fase 5 | quase sempre é **caixa fechado** na filial. Abra o caixa e tente de novo |
| você tocou em MELHOR ROTA | não é perda total: fotografe e me diga. A ordem mudou, e o manual passa a dizer isso |
| deu meia-noite no meio | pare. O relatório da fase 7 soma **por data**, e uma janela partida em dois dias não fecha |

## No fim

Combinamos na hora: ou você finaliza as três pelo app, ou eu desfaço pelo painel. O que não pode é
ficar entrega aberta na sandbox — ela reaparece no painel de amanhã e estraga a próxima captura.

Depois, do meu lado: `limpar` tira o que sobrou da sua tela, `arquivar-fila` tira o que sobrou da
minha, e a janela fecha limpa.
