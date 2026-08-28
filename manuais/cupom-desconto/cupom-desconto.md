# Cupom de Desconto — todos os campos e o que o cliente vê

O cupom é um código que o cliente usa no **cardápio digital** (e, se você ligar, no
PDV, nas Mesas e no Totem). Você desenha a regra em **CRM → Cupom de Desconto**.
Este manual explica **cada campo** e, no fim, como isso aparece no cardápio.

Manuais de **estratégia** (qual cupom criar para Pix, primeira compra, só bebida…)
ficam para depois. Aqui o assunto é o funcionamento.

> As imagens do BeeFood têm **marcações em verde** (setas e números).

---

## Antes de começar

1. Acesso a **CRM → Cupom de Desconto**.
2. Pelo menos um **cardápio** ativo.
3. Link do cardápio digital da loja (no sandbox: `menu.beefood.com.br/beefood3`).

---

## Parte 1 — Abrir e criar

### Passo 1. Ir até os cupons

No menu, abra **Fidelidade (CRM)** e clique em **Cupom de Desconto** (1).
Para criar, clique em **Adicionar Cupom** (2).

![Lista de cupons](imagens-tratadas/01-lista-cupons.png)

Cada cartão mostra o código, o benefício, a validade, os canais e quantas vezes
já foi usado. **Copiar Link** gera o endereço do cardápio já com o cupom — o
cliente abre o link e o código entra sozinho.

A aba **Histórico** (ao lado de Cupons) soma desconto, faturamento e usos. Não
entra neste manual.

---

## Parte 2 — Código, tipo, valor e validade

No modal **Novo Cupom**:

![Modal — código, tipo e validade](imagens-tratadas/02-modal-novo-topo.png)

| Nº | Campo | O que faz |
|----|--------|-----------|
| 1. | **Código do Cupom** \* | O que o cliente digita. Vai para maiúsculas e sem espaço. Ex.: `PIX15%` |
| 2. | **Tipo de Benefício** | **Desconto** (% ou R$), **Frete Grátis** ou **Produto** (brinde) |
| 3. | **Valor do Desconto** | Só no tipo Desconto. **%** até 100 ou **R$** até 999,99 |
| 4. | **Validade — Início** | A partir de quando vale |
| 5. | **Dias da Semana** | Sem o dia marcado, o cupom não vale naquele dia |

**Término** é o switch ao lado de Início. Desligado = sem data final. Ligado =
preenche 30 dias à frente, e você ajusta.

**Ativo** (canto do modal) liga ou desliga o cupom sem apagar.

**Frete Grátis** só faz sentido no Delivery. PDV, Mesas e Totem ficam
desligados. **Produto** pede um item do cardápio (botão **Buscar**).

---

## Parte 3 — Canais e regras

Role o modal. Os canais ficam à esquerda; as regras, à direita.

![Modal — canais e regras](imagens-tratadas/03-modal-novo-regras.png)

| Nº | Campo | O que faz |
|----|--------|-----------|
| 1. | **Canais de Visibilidade** | Onde o cupom pode ser usado: Delivery, PDV, Mesas/Comandas, Totem |
| 2. | **Regras** | Travas do cupom (mínimo, limite, primeira compra…) |
| 3. | **Confirmar telefone por SMS** | Código por SMS **só no cardápio digital e no totem**. No painel o operador aplica sem SMS |

### Cada regra

| Campo | Ligado / preenchido | Efeito |
|-------|---------------------|--------|
| **Valor mínimo** | R$ maior que zero | Pedido abaixo do valor: recusa |
| **1 uso/cliente** | Ligado | Cada telefone usa uma vez |
| **Limite total** | Ligado + quantidade | Depois do N-ésimo uso, acaba |
| **Apenas primeira compra** | Ligado | Só cliente que nunca pediu nessa loja |
| **Exibir no BeeBot e Cardápio** | Ligado (padrão) | Entra na faixa verde e na lista do cardápio |
| **Apenas retirada e consumo no local** | Ligado | Pedido de **entrega** é recusado |
| **Não aplicar em produtos em promoção** | Ligado | Item já promocional fica de fora da conta. Se **todos** os itens estiverem em promoção, o cupom é recusado |
| **Confirmar telefone por SMS** | Ligado | 1 crédito de SMS por confirmação (`Food Marketing → Campanhas SMS`). Sem saldo o cupom **passa** sem pedir o código. Número já confirmado vale 30 dias no cardápio |

**Exibir no BeeBot e Cardápio** desligado: o cupom continua válido se alguém
souber o código (ou o operador colar no painel), mas **não** aparece na faixa
nem na lista do cliente.

---

## Parte 4 — Configurações avançadas

Abra **Configurações avançadas** no fim do modal.

![Modal — configurações avançadas](imagens-tratadas/04-modal-avancado.png)

| Nº | Campo | O que faz |
|----|--------|-----------|
| 1. | **Formas de pagamento** | Vazio = qualquer forma. Preenchido = só aquelas formas (as outras bloqueiam na hora de pagar). No cardápio, a forma de recebimento vira a forma de pagamento. Pix pelo app = tipo **PIX BeeFood** |
| 2. | **Como o cupom se aplica?** | Um modo por cupom (veja a tabela abaixo) |

### Os três modos (o ponto que mais confunde)

Pedido de **R$ 100**, sendo **R$ 30 em bebidas**, cupom de **10%**:

| Modo na tela | O que precisa ter no carrinho | Onde cai o desconto | Neste exemplo |
|--------------|-------------------------------|---------------------|---------------|
| **Ao pedido inteiro (padrão)** | Nada específico | Pedido todo | R$ 10,00 |
| **Só quando o carrinho tiver certos itens** | Pelo menos um setor/produto escolhido | Pedido **todo** | R$ 10,00 se tiver bebida |
| **Só sobre certos itens do pedido** | — | **Só** aqueles setores/produtos | R$ 3,00 (10% de R$ 30) |

No segundo e no terceiro modo aparecem os seletores de **setores** e
**produtos**. Dá para combinar setor + produto **dentro do mesmo modo**.

O terceiro modo (**só sobre certos itens**) existe só no tipo **Desconto**. Em
Frete Grátis e Produto não há base para restringir.

Clique em **CRIAR CUPOM** (cupom novo) ou **SALVAR** (edição).

---

## Parte 5 — O que o cliente vê no cardápio digital

Com **Exibir no BeeBot e Cardápio** ligado e o cupom **Ativo**, o cliente abre o
cardápio e vê a faixa verde no topo: **Você tem N cupons! Aproveite!**

![Faixa de cupons no cardápio](imagens-tratadas/05-cardapio-banner.png)

| Nº | O que é |
|----|---------|
| 1. | Faixa verde — toque aqui (não é a aba **Promoções** do rodapé; essa aba é de **produto em promoção**, outro assunto) |

O toque abre **ADICIONAR CUPOM**. O cliente tem **dois caminhos**:

![Lista de cupons no cardápio](imagens-tratadas/06-cardapio-lista-cupons.png)

| Nº | O que o cliente faz |
|----|---------------------|
| 1. | Digita o código que recebeu (WhatsApp, SMS, campanha) — mesmo que **não apareça na lista** — e toca em **Adicionar**. É a promoção “secreta”. No exemplo, `ANIVERSARIO` |
| 2. | Ou escolhe um da lista **Cupons disponíveis** — só entram os que você deixou com **Exibir no BeeBot e Cardápio** ligado |

Os dois caminhos estão na mesma tela: a lista é vitrine; o campo é o código que chegou na mão do cliente.

**Ver todas as regras** no cartão abre o detalhe (validade, mínimo, canais).

O desconto entra no pedido. Se a regra falhar (mínimo, dia, entrega quando o
cupom é só retirada, item em promoção, forma de pagamento…), o cardápio
**tira o cupom e avisa** — o cliente continua comprando.

O **link copiado** no painel já chega com o cupom aplicado.

SMS: se a regra estiver ligada, o cardápio pede o código enviado ao telefone
**antes de pagar**. No PDV, Mesas e Delivery do painel isso **não** aparece.

---

## Problemas comuns

| Sintoma | O que verificar |
|---------|-----------------|
| Cliente não vê a faixa | **Exibir no BeeBot e Cardápio** está ligado? Cupom **Ativo**? Canal **Delivery** ligado? |
| Cupom recusado na entrega | **Apenas retirada e consumo no local** está ligado? |
| Desconto saiu menor do que o esperado | Modo **só sobre certos itens**? Ou **não aplicar em promoção** tirou parte do carrinho? |
| Forma de pagamento travada | **Formas de pagamento** no avançado: a forma que o cliente escolheu está na lista? |
| SMS não pediu código | Vale só cardápio/totem. Sem crédito de SMS o cupom passa. Canal Delivery ou Totem precisa estar ligado |

---

## Precisa de ajuda?

Fale com o **suporte BeeFood** com o **código do cupom** e o que o cliente
viu (print da faixa ou da recusa).

---

*Última atualização: agosto/2026 — BeeFood · Cupom de Desconto (campos + cardápio)*
