# Manual 12 — Divisão de conta

Três amigos pediram juntos e cada um quer pagar a sua parte, um no PIX e outro em dinheiro.
É para isso que existe o **DIVIDIR CONTA** na tela de pagamento: em vez de uma cobrança, você
registra **uma por pessoa**, cada uma com a sua forma.

Tudo acontece na mesma tela do capítulo [11](../11-cobranca-na-porta/manual.md) — o caminho até
ela é o mesmo.

---

## Quantas pessoas vão pagar

[Entender a divisão](01-duas-pessoas.md)

![Duas pessoas](prints/01-duas-pessoas.png)

Toque no **+** do **DIVIDIR CONTA**. O app divide o valor **em partes iguais** e cria um bloco
por pessoa: aqui, R$ 48,00 viraram **duas de R$ 24,00**.

Cada bloco ganha um campo próprio de **FORMA DE PAGAMENTO**. Com uma pessoa só, esse campo não
existe — a forma é escolhida no fim, e é a diferença mais visível entre cobrar dividido e
cobrar direto.

**O − volta atrás**, juntando as partes.

## A forma de cada um

[Entender a escolha por pessoa](02-forma-da-pessoa-1.md)

![Forma da pessoa 1](prints/02-forma-da-pessoa-1.png)

Toque em **Selecione a forma** no bloco da pessoa. A folha é a mesma de sempre, com um
subtítulo dizendo de quem é: **Pessoa 1**.

[Entender o resultado](03-duas-formas.md)

![Duas formas](prints/03-duas-formas.png)

Feito: **Pessoa 1 · PIX Manual · R$ 24,00** e **Pessoa 2 · Dinheiro · R$ 24,00**. Quem paga em
dinheiro ganha a linha **Troco para**, e as regras de troco são as do capítulo 11.

## Valores diferentes

O lápis ao lado do valor abre a edição. Use quando a divisão não é meio a meio — um paga R$ 30
e o outro R$ 18, por exemplo.

**A soma precisa fechar com o valor a receber.** É a única regra rígida aqui: se as partes não
somam o total, o app não deixa confirmar.

## A confirmação

[Entender a confirmação](04-confirmar-duas-linhas.md)

![Confirmar duas linhas](prints/04-confirmar-duas-linhas.png)

A folha final lista **uma linha por pessoa, numerada**, com a forma e o valor. É a hora de
conferir se cada um pagou o que está escrito.

[Entender a tela de sucesso](05-pagamento-confirmado.md)

![Pagamento confirmado](prints/05-pagamento-confirmado.png)

**Pagamento Confirmado!** com o valor cheio — R$ 48,00, a soma das partes. A entrega foi
finalizada na mesma operação.

## Como pensar na divisão

**Uma pessoa, uma forma.** Se a mesma pessoa quer pagar metade no cartão e metade em dinheiro,
trate como duas pessoas: para o caixa do restaurante o que importa é quanto entrou em cada
forma.

**É tudo ou nada.** As partes são enviadas juntas: ou todas registram, ou nenhuma. Não existe
"a Pessoa 1 pagou e a 2 ficou pendente".

**Confirme depois de receber de todos.** Uma vez confirmado, não há como mexer pelo app.

**Cobrar valor menor que o total** não é divisão de conta: aí é um pagamento só, com o valor
ajustado pelo lápis, e uma observação explicando.

## Se algo não funcionar

**Não consigo confirmar.** Confira se toda pessoa tem forma escolhida e se a soma das partes
bate com o valor a receber.

**Dividi em demasia.** O **−** reagrupa, e os valores voltam a ser divididos igualmente.

**A forma prevista não vem marcada nos blocos.** É esperado: com divisão, o app não tenta
adivinhar quem paga como.

---

## Como este capítulo foi produzido

A conta do pedido **#1031** (Combo One Burger, R$ 48,00) foi dividida em duas partes de R$
24,00 no emulador, uma em PIX Manual e outra em dinheiro sem troco, e confirmada.

No banco ficaram **duas linhas** em `_preVendaPagamento` para o mesmo pedido — PIX Manual R$
24,00 e Dinheiro R$ 24,00, ambas pagas — e o pedido foi para *ENTREGUE*. É o mesmo registro que
o PDV do restaurante produziria.
