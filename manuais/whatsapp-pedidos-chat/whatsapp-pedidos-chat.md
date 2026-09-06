# Pedidos pelo chat no WhatsApp

O cliente manda mensagem no **WhatsApp da loja** e o **BeeBot** monta o pedido
sozinho: setor, produto, grupos de opção (ponto da carne, bebida, adicional),
quantidade, entrega ou retirada, pagamento e confirmação.

Com o **Pedido Chat** ligado, não é obrigatório abrir o **cardápio digital**. O
atendimento automático tira o pedido **pelo chat**, do começo ao fim, e o
pedido entra no Delivery igual aos outros.

O interruptor mora no painel do BeeBot (`bot.beefood.com.br`), não no cardápio.

> As imagens do BeeFood e do BeeBot têm **setas numeradas** (1, 2, 3…). Cada
> número indica o campo ou botão correspondente na tela.

---

## O que é o Pedido Chat

**Pedido Chat** é a função do BeeFood que transforma a conversa do WhatsApp num
pedido de verdade. O bot pergunta, o cliente responde com o **número** da opção
ou **digitando o nome do produto**, e no fim confirma o resumo.

Serve para delivery e para retirada. Preço, taxa de entrega, formas de
pagamento e área de entrega são os **mesmos do cardápio** da loja — o bot não
tem um cardápio paralelo.

Não confundir com a **IA do ChatGPT**: a IA responde pergunta em texto livre
(“quanto custa a Coca?”). O Pedido Chat **anota o pedido** e manda para a
cozinha. São dois interruptores. A IA tem manual próprio.

---

## Antes de começar

1. BeeBot contratado na loja.
2. Acesso ao menu **WhatsApp** (ou ao site [bot.beefood.com.br](https://bot.beefood.com.br)).
3. Cardápio com produtos, grupos de opção, formas de pagamento e área de entrega
   (ou retirada) já cadastrados — o bot usa o mesmo cardápio da loja.
4. Para o **cliente** conversar de verdade, o WhatsApp da loja precisa estar
   **conectado**. Mesmo desconectado, você já consegue ligar o Pedido Chat.

---

## Parte 1 — Como abrir o BeeBot

No BeeFood, abra **WhatsApp** (1). A aba **Conexão** mostra se o número está
ligado. Clique em **Abrir Conversas WhatsApp** (2).

![WhatsApp → Abrir Conversas](imagens-tratadas/01-beefood-whatsapp.png)

| Nº | Item | O que faz |
|----|--------|-----------|
| 1. | **Conexão** | Status do número. *Desconectado* não impede abrir o painel |
| 2. | **Abrir Conversas WhatsApp** | Abre o painel do BeeBot numa nova aba |

O botão verde **Conectar** desta tela é outra coisa: ele gera o QR Code do
número. O Pedido Chat não fica aqui.

Também dá para ir direto em [bot.beefood.com.br](https://bot.beefood.com.br), com o
**mesmo usuário e senha** do BeeFood.

![Login do BeeBot](imagens-tratadas/02-login-bot.png)

---

## Parte 2 — Como ativar o pedido pelo WhatsApp

No BeeBot, a coluna da esquerda tem os interruptores da loja. Ligue **Pedido Chat**
(1). O sistema grava na hora: aparece *Pedido via Chat ativado com sucesso.*

![Interruptor Pedido Chat](imagens-tratadas/03-pedido-chat.png)

| Nº | Item | O que faz |
|----|--------|-----------|
| 1. | **Pedido Chat** | Ligado, o bot monta o pedido pela conversa. Desligado, ele não entra nesse fluxo |

Os outros interruptores desta coluna (**Resposta**, **Notificação Campanhas**,
**Som Alerta**, **ChatGPT**) são assuntos à parte. Para receber pedido pelo
WhatsApp, o que importa é o **Pedido Chat** verde.

> Sem o WhatsApp **conectado**, o cliente não recebe as mensagens. O interruptor
> pode estar ligado e o chat da loja, não: os dois precisam estar ok.

---

## Parte 3 — Como o cliente faz o pedido no WhatsApp

O cliente manda **fazer pedido** (ou uma frase equivalente). O bot lista os
**setores** do cardápio. Dá para responder com o **número** ou **digitar o nome**
de um produto para buscar — “burger”, “coca”, “pizza”.

![Começar e escolher o produto](imagens-tratadas/04-whatsapp-iniciar.png)

No exemplo: o cliente escolhe o setor **1**, depois o **Junior Burger**. Se o
produto tem grupo de opção (ponto da carne, bebida, adicional, borda), o bot
pergunta **um grupo por vez**, com mínimo e máximo — o mesmo cadastro do PDV e
do cardápio digital.

Em seguida vem a quantidade, o item entra no carrinho e o bot pergunta como
continuar:

- **1** — Continuar pedido (outro item no mesmo pedido)
- **2** — Visualizar pedido
- **3** — Finalizar pedido

Na finalização: entrega, compartilhar localização ou **retirada**; observação
do pedido; forma de pagamento (PIX, dinheiro, cartão…); e o **resumo** para
confirmar.

![Montar o lanche e o resumo](imagens-tratadas/05-whatsapp-finalizar.png)

No resumo, **1** confirma e o pedido entra no **Delivery** da loja, como se
tivesse vindo do cardápio. **2** cancela. **V** volta uma etapa.

---

## Palavras que o cliente pode escrever no meio do pedido

O cliente pode escrever isto a qualquer momento:

| O que escrever | O que acontece |
|----------------|----------------|
| **Cancelar** | Sai do pedido atual |
| **Voltar** ou **V** | Volta uma etapa |
| **Ajuda** | Mostra o que já está no carrinho e as ações (setores, finalizar, atendente, cancelar) |
| **Atendente** | Cancela o pedido em andamento e chama um humano |

Também vale **digitar o nome do produto** em vez de escolher o setor: se achar,
lista os resultados; se não achar, volta a mostrar os setores.

---

## O que o bot pergunta, na ordem

1. Setor ou busca de produto
2. Produto (e confirmação, se precisar)
3. Grupos de opção, um de cada vez
4. Observação do item (ou **1** para seguir)
5. Quantidade
6. Continuar, visualizar ou finalizar
7. Entrega, localização ou retirada
8. Endereço (se for entrega: bairro/CEP, número, complemento)
9. Observação do pedido
10. Forma de pagamento
11. Resumo → confirmar

A retirada usa o endereço da loja. A entrega só segue se o endereço estiver na
**área de entrega** cadastrada; fora da área, o bot oferece de novo as opções
(retirada ou outro tipo de entrega).

---

## Problemas comuns

| Sintoma | O que verificar |
|---------|-----------------|
| O cliente pede e o bot não monta o pedido | **Pedido Chat** está ligado? WhatsApp está **conectado**? |
| Não aparece setor / produto | O item está ativo no cardápio e liberado no canal Delivery? |
| Endereço fora da área | Confira a área de entrega da loja. Fora dela, só resta retirada |
| Forma de pagamento não entra | A forma precisa estar ativa no **cardápio digital** (é essa lista que o bot usa) |
| Pedido não chega no painel | No resumo, o cliente clicou em **1 - Confirmar Pedido**? Caixa de delivery aberto? |

---

## Perguntas frequentes

**O cliente pode fazer pedido pelo WhatsApp sem abrir o cardápio?**
Sim. Com o Pedido Chat ligado, a conversa substitui o cardápio digital: o bot
lista os setores, monta o item e pede a confirmação. O link do cardápio continua
existindo; quem preferir pedir pelo site ou pelo Instagram ainda pode.

**Como ativar o pedido pelo chat no BeeFood?**
Abra **WhatsApp → Conexão → Abrir Conversas WhatsApp** (ou entre em
bot.beefood.com.br). Na coluna da esquerda, ligue **Pedido Chat**. Não é o botão
**Conectar** da tela de Conexão — aquele só gera o QR Code do número.

**Qual a diferença entre Pedido Chat e a IA do ChatGPT?**
O Pedido Chat **fecha a venda**: escolhe produto, complemento, endereço e
pagamento. A IA **responde pergunta** (“vocês abrem domingo?”, “tem coca zero?”)
com os dados da loja. Dá para ter os dois ligados; cada um tem o próprio
interruptor.

**O que o cliente precisa escrever para começar?**
A frase **fazer pedido** (ou a opção equivalente que o bot mostrar). Depois ele
responde com o número da lista ou digita o nome do produto para buscar.

**O pedido pelo WhatsApp cai no Delivery igual aos outros?**
Sim. Depois do **1 - Confirmar Pedido**, entra na fila de Delivery do BeeFood,
com o mesmo número, impressão e notificações dos pedidos do cardápio.

**Funciona com pizza, hambúrguer, açaí e grupo de opções?**
Sim. O bot usa o cadastro do cardápio: se o produto tem grupo (sabor, ponto,
adicional, borda), ele pergunta grupo por etapa, com mínimo e máximo. O que
não estiver no cardápio não aparece no chat.

**Dá para pedir entrega e retirada no mesmo bot?**
Sim. Na finalização o bot pergunta como o cliente prefere: entrega, compartilhar
a localização ou retirar na loja. A taxa de entrega é a da área cadastrada. Fora
da área, o bot avisa e oferece retirada (ou outra opção que a loja tiver).

**Como o cliente chama um atendente humano?**
Escreve **Atendente**. O pedido em andamento é cancelado e a conversa espera
alguém da loja. **Ajuda** só mostra as opções; não chama gente.

**O bot cobra o mesmo preço do cardápio digital?**
Sim. Preço, desconto ou acréscimo da forma de pagamento e taxa de entrega vêm
do mesmo cadastro. Não existe tabela só para o WhatsApp.

**Preciso de WhatsApp Business para o Pedido Chat?**
O BeeBot conecta o número da loja pelo QR Code no BeeFood. Para o cliente
conversar, esse número precisa estar **conectado**. A loja desconectada consegue
ligar o interruptor, mas ninguém recebe mensagem até conectar.

**Posso desligar o Pedido Chat e deixar só o cardápio?**
Sim. Desligue **Pedido Chat**. O WhatsApp continua para notificação, resposta
automática e campanha; o cliente deixa de montar o pedido pelo chat e volta a
usar o link do cardápio.

**O cliente pode colocar mais de um produto no mesmo pedido?**
Sim. Depois de adicionar o item, a opção **1 - Continuar pedido** volta aos
setores. **2** mostra o que já está no carrinho. **3** finaliza.

**O pedido aparece se a loja estiver fechada?**
Quem chama no WhatsApp com a loja fechada pode receber a mensagem de
**Respostas** (loja fechada), com o horário da grade. Pausa e horário se
configuram nos manuais de horário e de fechar a loja — não neste interruptor.

**Precisa de PIX Online para pedir pelo WhatsApp?**
Não. O bot lista as formas ativas no cardápio digital: dinheiro, cartão na
entrega, PIX com chave, PIX Online (se a loja tiver). O cliente escolhe na hora
do pagamento.

**O cliente vê o resumo antes de confirmar?**
Sim. O último passo mostra itens, total, tipo de entrega e forma de pagamento.
Só depois do **1** o pedido segue para a loja. Até lá ele pode **V** (voltar)
ou **2** (cancelar).

**O pedido pelo chat usa caixa de delivery?**
Sim. Como todo pedido de Delivery, precisa de caixa aberto com o canal de
delivery. Sem caixa, o resumo até aparece; a confirmação pode falhar.

---

## Manuais relacionados

| Manual | O que traz |
|--------|------------|
| **IA ChatGPT no WhatsApp** | A IA que responde pergunta; não monta o pedido |
| **Horário de atendimento** | A grade que também vale para o chat |
| **Fechar a loja fora do horário** | Pausa e a mensagem de loja fechada no WhatsApp |
| **Área de entrega** | Bairro, CEP, mapa e KM — o bot usa essa área |
| **Formas de recebimento** | O cadastro das formas; no chat vale a lista do cardápio digital |

---

## Precisa de ajuda?

Fale com o **suporte BeeFood** informando: nome da loja e **CNPJ**.

---

*Última atualização: setembro/2026 — BeeFood · Pedidos pelo chat no WhatsApp*
