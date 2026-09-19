# Manual 06 — Rota montada pelo restaurante

Até aqui a lista de entregas era uma lista: pedidos, um embaixo do outro, e você decidia a
ordem. Quando o restaurante usa a **Gestão de Entregas 2.0**, ele pode montar a rota para
você — escolher quais pedidos saem juntos e em que ordem — e a lista muda de cara.

Quem não usa rota não vê nada disso. A tela continua exatamente como nos capítulos
anteriores.

---

## A rota na lista

[Entender o cabeçalho da rota](01-rota-na-lista.md)

![Rota na lista](prints/01-rota-na-lista.png)

A rota aparece como um **grupo**, com cabeçalho próprio: a letra (**A**), o nome (**ROTA A**),
o contador **0 de 3 entregues** e o botão verde **INICIAR ROTA**.

Os pedidos dela ficam logo abaixo, **numerados 1, 2, 3** — e esse número é a ordem que o
restaurante definiu, não a posição na tela.

## O que não está na rota

[Entender a lista solta](02-outras-entregas.md)

![Outras entregas](prints/02-outras-entregas.png)

Pedido que o restaurante atribuiu a você sem colocar em rota nenhuma cai embaixo, sob o
título **OUTRAS ENTREGAS (1)**. Ele funciona como sempre funcionou.

Esse título só aparece quando as duas coisas estão na tela ao mesmo tempo. Sem rota, a lista
é a lista — sem cabeçalho.

## INICIAR ROTA

[Entender o que o botão faz](03-rota-no-maps.md)

![Rota no Google Maps](prints/03-rota-no-maps.png)

Um toque em **INICIAR ROTA** faz duas coisas de uma vez:

1. **avisa que você saiu** — os pedidos da rota passam para "em transporte", o painel do
   restaurante mostra isso na hora e o cliente recebe a mensagem de saiu para entrega;
2. **abre o Google Maps** com as paradas na ordem da rota, partindo de onde você está.

> É um caminho só de ida. Depois de iniciar, o restaurante já contou com você na rua.

## Depois de iniciar

[Entender o cabeçalho depois](04-rota-despachada.md)

![Rota despachada](prints/04-rota-despachada.png)

O cabeçalho muda: aparece **em rota** ao lado do contador e o botão verde vira o azul
**ABRIR NO MAPS**. Pode tocar quantas vezes quiser — ele só reabre o mapa, sem avisar
ninguém de novo.

## As entregas, uma a uma

A rota organiza o caminho; **entregar continua sendo pedido por pedido**. Toque no card,
confira os itens, receba (ou finalize sem cobrar) como nos capítulos
[11](../11-cobranca-na-porta/manual.md) e [13](../13-finalizar-sem-cobrar/manual.md).

Cada entrega concluída sobe o contador do cabeçalho: **1 de 3**, **2 de 3**. Quando a última
fecha, a rota se encerra sozinha e o grupo desaparece da tela.

O contador vem da rota, e não dos cards visíveis — por isso ele continua dizendo *de 3* mesmo
quando já sobraram dois cards na tela.

## O "MELHOR ROTA GOOGLE MAPS" do rodapé

Aquele botão azul do rodapé (capítulo [07](../07-melhor-rota/manual.md)) cobre **só as outras
entregas**, nunca as paradas de uma rota. Ele reordena os endereços por distância do
restaurante, o que jogaria fora a ordem que o operador definiu. Cada rota tem o próprio botão,
no cabeçalho dela.

E, com apenas uma entrega solta, o botão do rodapé nem aparece: não há o que ordenar.

## Se algo não funcionar

**Tenho duas rotas na tela.** É possível e é normal em restaurante movimentado. Cada uma tem
seu cabeçalho, sua letra e seu botão.

**"Despacho não confirmado".** O mapa é oferecido de qualquer forma, com um aviso. O app não
tem como saber se o restaurante registrou a saída — avise a loja.

**A rota sumiu.** O operador pode ter excluído a rota ou passado para outro entregador. Os
pedidos saem da sua lista junto.

**O Maps mostra um endereço um pouco diferente.** As paradas são enviadas por coordenada, e o
Maps exibe o endereço que ele reconhece naquele ponto. O endereço que vale é o do card no app.

---

## Como este capítulo foi produzido

A rota foi criada pelo caminho oficial do painel (`gestaoEntregaCriarRota`) pelo gerador de
cenário, com `--rota 3`: três dos quatro pedidos entraram na rota A e o quarto ficou solto, o
que é justamente o caso de "rota + outras entregas" na mesma tela.

O **INICIAR ROTA** foi tocado de verdade no emulador. O log do app registrou `3 de 3 paradas
viraram destino` e a URL montada com as três coordenadas na ordem da rota, partindo da posição
do aparelho. No banco, os três pedidos da rota saíram de *PRONTO/PREPARO* para *ENTREGA* — o
despacho aconteceu, não foi simulado.
