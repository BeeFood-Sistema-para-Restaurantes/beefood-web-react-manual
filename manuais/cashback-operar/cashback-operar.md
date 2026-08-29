# Cashback — operar no dia a dia

Com o programa **ligado** (manual **Cashback — configurar**), este manual ensina
a **acompanhar**, **ajustar saldo** e **usar** o cashback na venda.

Três lugares:

1. **CRM → Cashback** — histórico, saldo por cliente e fila da madrugada
2. **PDV / Mesas / Delivery** — o operador aplica o saldo no pagamento
3. **Cardápio digital** — o cliente se identifica e usa sozinho

> As imagens têm **setas com números** (1, 2, 3…). No texto, cada número indica
> o campo ou botão correspondente na tela.

---

## Antes de começar

1. Programa **ativado** em **CRM → Cashback → Configuração**.
2. Cliente identificado (no painel ou no cardápio).
3. Nos testes, use o telefone fake **(11) 11111-1122** (Bruno XXX). Não use
   telefone de cliente real.

O crédito novo só entra **de madrugada**, em pedido **pago e finalizado**.
O **uso** na venda é na hora.

---

## Parte 1 — Histórico

Aba **Histórico**: quanto foi gerado, usado e vencido no período.

![Histórico de cashback](imagens-tratadas/01-historico.png)

| Nº | Campo | O que faz |
|----|--------|-----------|
| 1. | Aba **Histórico** | Abre o resumo do período |
| 2. | Período e busca | Filtra por data e por cliente |
| 3. | Cartões | Total gerado, usado, vencido e quantos clientes |
| 4. | Gráfico | Cashback por semana (ou dia / mês) |

**Excel** exporta a lista. **Top clientes** mostra quem mais gerou e quem mais
usou. Telefone e nome de cliente real não devem ir para material público —
nas capturas de teste use o número fake.

---

## Parte 2 — Saldo por cliente

Aba **Saldo por Cliente**. Busque pelo telefone de teste:

![Saldo filtrado pelo telefone fake](imagens-tratadas/02-saldo-clientes.png)

| Nº | Campo | O que faz |
|----|--------|-----------|
| 1. | Aba **Saldo por Cliente** | Lista quem tem saldo |
| 2. | Busca | Nome ou telefone. Aqui: `11111` |
| 3. | Cartão do cliente | Nome, telefone e **saldo total** |
| 4. | **Novo Saldo** | Atalho para creditar sem abrir o cartão |

Toque no cartão para ver o extrato e ajustar.

![Extrato do cliente](imagens-tratadas/03-detalhe-cliente.png)

| Nº | Campo | O que faz |
|----|--------|-----------|
| 1. | **Saldo atual** | Quanto o cliente pode usar agora |
| 2. | **Adicionar** | Credita (ajuste manual, com motivo) |
| 3. | **Remover** | Debita do saldo, também com motivo |
| 4. | **Extrato** | Gerado, usado e vencido, linha a linha |

**Adicionar** pede valor, motivo (obrigatório, vai para o log) e, se quiser,
validade em dias. Em branco, usa a validade da configuração.

![Adicionar saldo](imagens-tratadas/04-modal-ajuste.png)

| Nº | Campo | O que faz |
|----|--------|-----------|
| 1. | **Valor a adicionar** \* | Quanto creditar |
| 2. | **Motivo** \* | Ex.: bônus de cadastro. Fica no extrato |
| 3. | **Expira em (dias)** | Vazio = padrão do programa |
| 4. | **Adicionar saldo (F2)** | Grava. **Cancelar** não mexe em nada |

O mesmo fluxo existe no **cadastro do cliente** (aba Cashback).

---

## Parte 3 — Fila da madrugada

Aba **Fila Processamento**. Toda noite o sistema tenta creditar as vendas
quitadas.

![Fila de processamento](imagens-tratadas/05-fila-processamento.png)

| Nº | Campo | O que faz |
|----|--------|-----------|
| 1. | Aba **Fila Processamento** | Acompanha o lote da madrugada |
| 2. | Cartões | Total, pendentes, sucesso e erro |
| 3. | Status na tabela | **Pendente**, **Sucesso** ou **Erro** |
| 4. | Mensagem | Por que ainda não creditou (ou o valor gerado) |

Exemplos de mensagem:

- **Pendente:** *Venda ainda não paga — aguardando pagamento*
- **Erro:** *Venda cancelada*
- **Sucesso:** *Cashback gerado: R$ …*

Não adianta “forçar” na hora: a fila roda de madrugada. Regularize o pagamento
e espere o próximo processamento.

---

## Parte 4 — Usar no PDV (e nas Mesas)

No PDV, selecione o cliente (telefone fake **11111-1122**), coloque o item e
abra **Receber (F3)**.

![Usar cashback no pagamento](imagens-tratadas/06-pdv-usar-cashback.png)

| Nº | Campo | O que faz |
|----|--------|-----------|
| 1. | Cliente na venda | Sem cliente, o botão de cashback **não aparece** |
| 2. | **Usar cashback** | Mostra o saldo disponível |
| 3. | Total da venda | O cashback não pode passar desse valor |

Toque em **Usar cashback**:

![Modal Usar Cashback](imagens-tratadas/07-pdv-modal-aplicar.png)

| Nº | Campo | O que faz |
|----|--------|-----------|
| 1. | **Saldo disponível** | Quanto o cliente tem |
| 2. | **Máximo aplicável** | O menor entre saldo e o que falta pagar |
| 3. | **Valor a aplicar** | Já vem no máximo; você pode diminuir |
| 4. | **Aplicar (F2)** | Entra como desconto. **Cancelar** não usa |

O mesmo painel existe no pagamento das **Mesas** e do **Delivery**.
Respeita saldo mínimo e o dia da semana configurados.

Neste manual o modal foi aberto e **cancelado** — o saldo do teste não foi
gasto.

---

## Parte 5 — O cliente no cardápio digital

Identificado com o telefone fake, o cliente monta o pedido e abre a **Sacola**.
No **fechamento** (depois de escolher Entrega ou Retirada) o saldo aparece.

O sistema já tenta usar o cashback sozinho. Se você **Cancelar**, fica assim:

![Saldo na sacola](imagens-tratadas/08-cardapio-checkout-saldo.png)

| Nº | O que o cliente vê |
|----|--------------------|
| 1. | **R$ 1.233,21 de cashback disponível** — o saldo do telefone de teste |
| 2. | **Usar** — aplica como desconto (não pode passar do total) |
| 3. | **Ganhe R$ … de cashback** — o que esta compra ainda vai creditar (de madrugada) |

Toque em **Usar** (ou deixe o sistema aplicar sozinho):

![Cashback aplicado no fechamento](imagens-tratadas/09-cardapio-checkout-usar.png)

| Nº | O que acontece |
|----|----------------|
| 1. | **Utilizando R$ … de desconto** — o saldo entrou no pedido |
| 2. | **CANCELAR** — tira o cashback e volta o total cheio |
| 3. | **Desconto cashback** no resumo |
| 4. | **Total R$ 0,00** — neste teste o saldo cobriu o combo inteiro |

Cupom **não combina** com cashback ativo. **Finalizar** neste manual **não foi
tocado** — o saldo do teste continua inteiro.

Se a faixa da home não atualizar depois de ligar o programa, espere **1 minuto**.

---

## Problemas comuns

| Sintoma | O que verificar |
|---------|-----------------|
| Botão **Usar cashback** some | Cliente selecionado? Canal do PDV/Mesas ligado? Dia da semana marcado? |
| Não aplica o valor | Saldo abaixo do **mínimo**? Valor maior que a venda? |
| Pedido de ontem sem crédito | Entrou na **fila**? Está **pago**? Olhe a mensagem |
| Cliente no cardápio sem saldo | Identificou o telefone certo? Esperou a madrugada do crédito? |

---

## Precisa de ajuda?

Fale com o **suporte BeeFood** com o **número da venda**, o **telefone de teste**
e um print da fila ou do modal **Usar cashback**.

---

*Última atualização: agosto/2026 — BeeFood · Cashback (operar no dia a dia)*
