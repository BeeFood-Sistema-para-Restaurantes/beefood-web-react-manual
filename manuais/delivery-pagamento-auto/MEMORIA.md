# MEMÓRIA — #43 Delivery pagamento automático

Status: ✅ Refação 21/08/2026 (segunda). A primeira rodada tirou print com o
painel em **Carregando...**. A segunda esperou 5 s, mas ainda fotografou
**Atualizando...** no meio do Pronto.

## Regra de captura (dono)

**Depois de cada clique, esperar o spinner sumir e só então contar 5 segundos.**

Textos que bloqueiam o print:

- `Carregando...`
- `Atualizando...` (aparece ao mudar Preparo → Pronto → Entregue)

Gravado também em `/cursor/stores/self/artifacts/captura-playwright.md`.

## Prova completa (terceira rodada — venda 850)

Flag `deliveryPagamentoAuto` ON. Operador OFF (senão o teclado bloqueia o Novo Pedido).

1. Novo Pedido → Coxinha R$ 8,00.
2. Intenção **Dinheiro** (modal Intenção de Pagamento) → Salvar.
3. Pedido no kanban: **#5 (850)** “agora”.
4. Detalhe da **Venda Nº 850** carregado: PREPARO, Coxinha, **Intenção de Pagamento — Dinheiro**,
   botões **PAGAMENTO** + **PEDIDO PRONTO**.
5. **PEDIDO PRONTO** → situação Pronto/Entrega (17:59), botão vira **PEDIDO ENTREGUE**,
   pagamento ainda pendente, intenção ainda visível.
6. **PEDIDO ENTREGUE** → badge **ENTREGUE**, bloco **Formas de Pagamento — Dinheiro —
   Pago R$ 8,00**, aviso *Remova o pagamento para alterar.* Filtro **Sem pagamento**
   caiu de 2 para **1**.

Backend (`alteraSituacaoDelivery.js`): ENTREGUE + intenção (`tipoPag` / `tipoPagStr`) +
`valorPago === 0` → lança o pagamento.

Contraprova: venda **#843** (Temaki R$ 28) foi a Entregue **sem** intenção — o automático
não rodou.

A venda **#849** (mesma Coxinha) foi a prova da segunda rodada; o manual publicado
usa a **850**, que é o pedido criado nesta sessão.

## Botões do detalhe (não inventar “Entregue” solto)

`VendaDetalhes.getAcaoPrincipal`: PREPARO → **PEDIDO PRONTO** (vai para ENTREGA);
PRONTO/ENTREGA → **PEDIDO ENTREGUE** (vai para ENTREGUE). Clicar “Entregue” no kanban
não substitui esses dois passos.
