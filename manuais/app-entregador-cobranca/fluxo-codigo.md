# O que o aplicativo faz de verdade — #116

Fonte: `manuais/gestao-entregas/material-recebido/app-entregador/estudo/01-o-que-o-app-faz-hoje.md`
(seções 2.7 e 2.8) e os capítulos 11, 12 e 13 do material. **Nada aqui vai para o manual do
usuário.**

## 1. O parâmetro que liga a tela de pagamento

Chegou em 25/09/2026 e virou a seção 1 do manual. No front-end do painel o campo é
`entregadorRecebePagamento`, booleano:

| Onde | O que |
|---|---|
| `src/pages/Parametros.tsx` | o `Switch` do card **Delivery**, logo abaixo do `deliveryPagamentoAuto` |
| `src/components/mobile/parametros/MobileParametrosPage.tsx` | o mesmo campo na versão de celular do painel |
| `src/hooks/useEmpresaParametros.ts` | o campo na interface e **no objeto `log`** do salvamento — o histórico de quem alterou |
| `src/utils/configCache.ts` | o campo no cache global de configuração da empresa |

Três detalhes que mudaram o texto do manual:

**O padrão de exibição é `?? true`, não `?? false`.** Está escrito no plano de implementação, com o
motivo: `?? false` faria a chave piscar "desligado" durante o carregamento. Para o manual isso vale
como fato de comportamento — **quem nunca mexeu tem a tela de pagamento ligada** —, e é o que
autoriza a frase "de fábrica ela vem ligada".

**Não há botão de salvar.** O `updateField` agenda um `setTimeout` de **500 ms** e, passado o
prazo, envia os parâmetros, refaz o cache (`refreshCache()`) e mostra o toast *Parâmetros salvos*.
O manual diz "grava sozinha" e cita o aviso, porque sem isso o leitor fica procurando um botão.

**O parâmetro é da empresa, não do entregador.** Vive em `empresaConfig`, o mesmo lugar dos outros
parâmetros, e por isso o manual afirma que a chave vale para **todos** os entregadores da loja.

### O que não foi lido no código

A tela que o aplicativo mostra com a chave desligada — *pagamento pelo aplicativo desativado, a
loja pediu para registrar o recebimento só no caixa* — veio de **print enviado pelo dono**, não de
leitura de código: o aplicativo do entregador é React Native, em repositório que não temos aqui. Por
isso o manual **não descreve a tela** nem põe imagem dela: ele diz o que o aplicativo avisa e o que
o entregador faz em seguida. Se um dia o repositório do aplicativo entrar no alcance, vale conferir
se o botão **INICIAR COBRANÇA** desaparece ou se continua na tela mostrando o aviso — o manual foi
escrito para valer nos dois casos ("não abre a tela").

## 2. Cobrar e finalizar são a mesma chamada

A frase que abre o manual — *"cobrar é finalizar"* — não é didática, é literal: o envio do
pagamento **também dá a baixa da entrega** quando o pedido não está em rota, ou quando o
identificador da rota vai no corpo da requisição.

Isso explica a tela de sucesso dizer *Pagamento Confirmado!* e a entrega desaparecer da lista sem
nenhum outro toque. E explica o estado intermediário que virou pergunta do FAQ: quando o pagamento
entra e a baixa não, o aplicativo mostra *O pagamento foi registrado. Finalize a entrega — o
dinheiro já está no caixa.* Nesse caso há **duas operações**, e a segunda ficou faltando.

## 3. Com uma pessoa, a forma é escolhida depois

Parece detalhe de layout e é a diferença estrutural entre os dois modos:

| Modo | Onde a forma é escolhida |
|---|---|
| uma pessoa | o **CONFIRMAR PAGAMENTO** abre a folha de formas |
| conta dividida | **cada bloco** tem o próprio campo *Selecione a forma*, na tela |

Por isso a seção 4 do manual não é "uma variação da 3": o caminho muda de ordem. E por isso, na
divisão, **nenhuma forma vem pré-marcada** — o aplicativo não tem como adivinhar quem paga como,
enquanto no modo de uma pessoa ele marca a forma prevista do pedido.

## 4. O seletor vai de 1 a 10

O contador do **DIVIDIR CONTA** aceita até dez pessoas. O manual não cita o número: dez é fora da
realidade da calçada, e citar convida a testar. O que ele diz é a regra que trava: **a soma das
partes tem de fechar com o saldo**, e o aplicativo mostra *A soma precisa ser R$ …* enquanto não
fecha.

## 5. O envio é atômico

As partes vão juntas, numa chamada. Ou todas registram, ou nenhuma. Foi verificado no material:
a conta dividida em duas deixou **duas linhas** de pagamento para o mesmo pedido, ambas pagas — o
mesmo registro que o PDV do restaurante produziria.

Daí a instrução "confirme depois de receber de todos": não há pagamento parcial pendente para
completar depois.

## 6. Não há proteção contra duplicidade

Medido e declarado no estudo do material: **não existe trava de pagamento repetido** no servidor.
O que existe é o botão bloqueado durante o envio, no aplicativo.

É o motivo de o manual dizer, em negrito, para **conferir no histórico** antes de repetir um envio
que pode ter passado. Escrever "tente de novo" seria a instrução errada — a segunda cobrança
entraria como um segundo pagamento.

## 7. A ordem dos botões da folha de finalizar é intencional

**FINALIZAR** em cima, **CANCELAR** embaixo. O estudo registra o porquê: o FINALIZAR move o pedido
no ERP, avisa o cliente e o marketplace, então quem fica na zona de esbarrão do polegar é o
CANCELAR. O manual repete isso em uma linha, porque é informação útil para quem opera com uma mão.

## 8. Os três avisos do caminho sem cobrança

Não é excesso de zelo: cada um pega um erro diferente.

| Aviso | Pega |
|---|---|
| conferência dos itens em destaque | sacola incompleta |
| *Ainda há R$ … a receber* | toque por engano no botão errado |
| a observação obrigatória por costume | a pergunta que a loja fará depois |

A observação é o único registro que sobrevive à operação: ela vai para o histórico e fica lá. O
manual insiste nela por isso, não por burocracia.

## 9. O que não aparece na lista de formas

A lista vem do cadastro do restaurante, filtrada para delivery. Fiado, Pix automático e as formas
de marketplace ficam fora **de propósito**: não são dinheiro trocando de mão na calçada.

Vale a pena o manual dizer isso em vez de deixar o entregador procurar: a pergunta *"a forma que eu
preciso não está na lista"* tem resposta de cadastro, no painel, e não no celular.

## 10. O número do pedido está só nesta tela

O selo laranja *PEDIDO #1030* do topo é a **única** aparição do número do pedido no aplicativo. Na
lista de entregas e nos detalhes da entrega o crachá laranja é o mesmo desenho, mas vem só com o `#`.

Não é falha de captura: são dois campos. O crachá do cartão e o dos detalhes leem `numeroPedido`, que
é numeração de marketplace e fica **nulo** em pedido que entrou pelos canais do restaurante — medido
no banco de desenvolvimento, `_PreVenda.numeroPedido` é nulo nos 34 pedidos da filial 39202 usados
nas capturas. O selo desta tela lê `numeroPreVenda`, que sempre tem valor: é o
`numeroPreVenda: venda.numeroPreVenda` do `resumoVenda`, em
`src/models/gestaoEntrega/pagamentoEntregador.js`.

Consequência para o suporte, e é o que o [#117](../gestao-entregas-ciclo-completo/gestao-entregas-ciclo-completo.md)
usa: como a cobrança é o último passo da parada, **antes dela o entregador não tem número para
conferir ao telefone**. A conversa que funciona em qualquer momento é por endereço e valor.

## 11. Procedência das imagens

Os treze prints vêm do material do dono (emulador `Pixel_7_Pro`, Android 15), dos capítulos 11, 12
e 13. Três cobranças foram feitas de ponta a ponta, sem atalho:

| Pedido | O que foi feito | O que ficou registrado |
|---|---|---|
| **#1030** | dinheiro, troco para R$ 50 | uma linha de pagamento, R$ 46,00, paga; pedido em *ENTREGUE* |
| **#1031** | dividido em duas de R$ 24,00, Pix e dinheiro | **duas linhas** de pagamento; pedido em *ENTREGUE* |
| **#1029** | finalizado sem cobrar, com observação | baixa sem pagamento, observação no histórico |

A folha de bandeiras foi aberta pelo Débito **só para a captura**, e desfeita antes de confirmar —
a cobrança que valeu foi em dinheiro.

### As seis da segunda rodada

Vêm de `capturas-2/22-erros-de-cobranca/` e de `capturas-2/_triagem/`, no mesmo emulador, app
`3.3.0` (build Android `1.0.1.2`), na madrugada de 19/09/2026.

| Imagem | Como a cena foi produzida |
|---|---|
| `14-soma-nao-fecha.png` | conta dividida em duas e o valor da Pessoa 1 baixado à mão para R$ 5,00 |
| `15-erro-no-pagamento.png` | wifi desligado **entre** escolher a forma e confirmar |
| `16-pedido-ja-pago.png` | pedido de marketplace já pago, detalhes abertos, toque em cobrar |
| `17`, `18` e `19` | **a rota foi excluída no painel** com a folha *Confirmar cobrança?* aberta no celular |

O último caso é o que o pedido de capturas marcava como "talvez não saia", e a solução é registrável:
em vez de tentar cortar a rede no meio de dois pedidos HTTP, tirou-se a rota debaixo do aplicativo.
O pagamento entrou — rota não tem nada com o caixa — e a baixa falhou, porque o celular mandou o
identificador de uma rota que já não existia. Depois da captura o pedido foi finalizado pela mesma
porta do FINALIZAR, para não sobrar entrega aberta na sandbox.

### A vigésima, do navegador

`20-parametro-entregador-registra-pagamento.png` é a única imagem deste manual que não vem do
celular: é o card **Delivery** de Configuração → Parâmetros, capturado na sandbox pelo
`capturar-parametro.py` — Playwright, tema claro forçado, recorte do card com 14 px de folga.

O script é **somente leitura**: ele não toca em interruptor nenhum. Na sandbox o
`entregadorRecebePagamento` já estava **desligado** quando a captura foi feita, provavelmente pelo
dono testando o aplicativo, e a decisão foi fotografar como estava e **dizer no texto que o padrão
de fábrica é ligado**. Mexer na chave para a foto ficar "certa" significaria mudar configuração de
empresa em ambiente que não é só nosso.

**O relógio da barra de status do emulador estava em UTC**, três horas à frente do fuso da loja. As
três telas de resultado não mostram hora nenhuma; a `18` e a `19` têm o recorte começando abaixo da
barra, e a hora que aparece nelas — *Realizado às 19/09/2026 00:48* — é a do aplicativo, que é a
gravada no servidor.

## 12. Onde o manual escolheu ser mais direto que a tela

| Tela | Manual | Por quê |
|---|---|---|
| o parâmetro é uma linha num card de configuração | **seção 1 do manual**, antes de qualquer tela do aplicativo | é a pergunta que passou a vir primeiro: "meu entregador tem essa tela?" |
| a cobrança e a baixa são telas diferentes | **"cobrar é finalizar"**, em bloco de aviso, antes de tudo | é o que muda o comportamento: ninguém cobra "para adiantar" |
| a forma prevista vem marcada, como sugestão | o manual diz que ela é **uma previsão** e que vale o que aconteceu | é o que protege o fechamento de caixa da noite |
| *Opcional* na folha de bandeira é uma linha de apoio | o manual dá a regra: **na dúvida, siga sem** | bandeira errada é pior que bandeira nenhuma |
| finalizar sem cobrar é um botão cinza do rodapé | seção própria, com os três avisos e a tabela de quando usar | é o botão que fecha entrega sem dinheiro, e o mais fácil de tocar por engano |
| "cliente não estava em casa" não tem tela | linha na tabela dizendo **nenhum dos dois** | era o vazio mais perigoso do capítulo |
