# O que o aplicativo faz de verdade — #116

Fonte: `manuais/gestao-entregas/material-recebido/app-entregador/estudo/01-o-que-o-app-faz-hoje.md`
(seções 2.7 e 2.8) e os capítulos 11, 12 e 13 do material. **Nada aqui vai para o manual do
usuário.**

## 1. Cobrar e finalizar são a mesma chamada

A frase que abre o manual — *"cobrar é finalizar"* — não é didática, é literal: o envio do
pagamento **também dá a baixa da entrega** quando o pedido não está em rota, ou quando o
identificador da rota vai no corpo da requisição.

Isso explica a tela de sucesso dizer *Pagamento Confirmado!* e a entrega desaparecer da lista sem
nenhum outro toque. E explica o estado intermediário que virou pergunta do FAQ: quando o pagamento
entra e a baixa não, o aplicativo mostra *O pagamento foi registrado. Finalize a entrega — o
dinheiro já está no caixa.* Nesse caso há **duas operações**, e a segunda ficou faltando.

## 2. Com uma pessoa, a forma é escolhida depois

Parece detalhe de layout e é a diferença estrutural entre os dois modos:

| Modo | Onde a forma é escolhida |
|---|---|
| uma pessoa | o **CONFIRMAR PAGAMENTO** abre a folha de formas |
| conta dividida | **cada bloco** tem o próprio campo *Selecione a forma*, na tela |

Por isso a seção 3 do manual não é "uma variação da 2": o caminho muda de ordem. E por isso, na
divisão, **nenhuma forma vem pré-marcada** — o aplicativo não tem como adivinhar quem paga como,
enquanto no modo de uma pessoa ele marca a forma prevista do pedido.

## 3. O seletor vai de 1 a 10

O contador do **DIVIDIR CONTA** aceita até dez pessoas. O manual não cita o número: dez é fora da
realidade da calçada, e citar convida a testar. O que ele diz é a regra que trava: **a soma das
partes tem de fechar com o saldo**, e o aplicativo mostra *A soma precisa ser R$ …* enquanto não
fecha.

## 4. O envio é atômico

As partes vão juntas, numa chamada. Ou todas registram, ou nenhuma. Foi verificado no material:
a conta dividida em duas deixou **duas linhas** de pagamento para o mesmo pedido, ambas pagas — o
mesmo registro que o PDV do restaurante produziria.

Daí a instrução "confirme depois de receber de todos": não há pagamento parcial pendente para
completar depois.

## 5. Não há proteção contra duplicidade

Medido e declarado no estudo do material: **não existe trava de pagamento repetido** no servidor.
O que existe é o botão bloqueado durante o envio, no aplicativo.

É o motivo de o manual dizer, em negrito, para **conferir no histórico** antes de repetir um envio
que pode ter passado. Escrever "tente de novo" seria a instrução errada — a segunda cobrança
entraria como um segundo pagamento.

## 6. A ordem dos botões da folha de finalizar é intencional

**FINALIZAR** em cima, **CANCELAR** embaixo. O estudo registra o porquê: o FINALIZAR move o pedido
no ERP, avisa o cliente e o marketplace, então quem fica na zona de esbarrão do polegar é o
CANCELAR. O manual repete isso em uma linha, porque é informação útil para quem opera com uma mão.

## 7. Os três avisos do caminho sem cobrança

Não é excesso de zelo: cada um pega um erro diferente.

| Aviso | Pega |
|---|---|
| conferência dos itens em destaque | sacola incompleta |
| *Ainda há R$ … a receber* | toque por engano no botão errado |
| a observação obrigatória por costume | a pergunta que a loja fará depois |

A observação é o único registro que sobrevive à operação: ela vai para o histórico e fica lá. O
manual insiste nela por isso, não por burocracia.

## 8. O que não aparece na lista de formas

A lista vem do cadastro do restaurante, filtrada para delivery. Fiado, Pix automático e as formas
de marketplace ficam fora **de propósito**: não são dinheiro trocando de mão na calçada.

Vale a pena o manual dizer isso em vez de deixar o entregador procurar: a pergunta *"a forma que eu
preciso não está na lista"* tem resposta de cadastro, no painel, e não no celular.

## 9. Procedência das imagens

Os treze prints vêm do material do dono (emulador `Pixel_7_Pro`, Android 15), dos capítulos 11, 12
e 13. Três cobranças foram feitas de ponta a ponta, sem atalho:

| Pedido | O que foi feito | O que ficou registrado |
|---|---|---|
| **#1030** | dinheiro, troco para R$ 50 | uma linha de pagamento, R$ 46,00, paga; pedido em *ENTREGUE* |
| **#1031** | dividido em duas de R$ 24,00, Pix e dinheiro | **duas linhas** de pagamento; pedido em *ENTREGUE* |
| **#1029** | finalizado sem cobrar, com observação | baixa sem pagamento, observação no histórico |

A folha de bandeiras foi aberta pelo Débito **só para a captura**, e desfeita antes de confirmar —
a cobrança que valeu foi em dinheiro.

## 10. Onde o manual escolheu ser mais direto que a tela

| Tela | Manual | Por quê |
|---|---|---|
| a cobrança e a baixa são telas diferentes | **"cobrar é finalizar"**, em bloco de aviso, antes de tudo | é o que muda o comportamento: ninguém cobra "para adiantar" |
| a forma prevista vem marcada, como sugestão | o manual diz que ela é **uma previsão** e que vale o que aconteceu | é o que protege o fechamento de caixa da noite |
| *Opcional* na folha de bandeira é uma linha de apoio | o manual dá a regra: **na dúvida, siga sem** | bandeira errada é pior que bandeira nenhuma |
| finalizar sem cobrar é um botão cinza do rodapé | seção própria, com os três avisos e a tabela de quando usar | é o botão que fecha entrega sem dinheiro, e o mais fácil de tocar por engano |
| "cliente não estava em casa" não tem tela | linha na tabela dizendo **nenhum dos dois** | era o vazio mais perigoso do capítulo |
