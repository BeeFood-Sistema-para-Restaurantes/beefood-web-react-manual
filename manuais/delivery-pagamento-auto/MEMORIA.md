# MEMÓRIA — #43 Delivery pagamento automático

Status: ✅ 21/08/2026.

Flag: `deliveryPagamentoAuto`. Backend `alteraSituacaoDelivery.js`: ao ir para ENTREGUE, se o flag está on **e** (`tipoPag` > 0 ou `tipoPagStr` preenchido) **e** `valorPago === 0`, registra o pagamento.

Prova: Novo Pedido → Coxinha R$ 8,00 → modal **Intenção de Pagamento** = **Dinheiro** → pedido #4 (849) no Preparo.

Contraprova já existente no sandbox: venda #843 (Temaki R$ 28) foi a Entregue **sem** intenção — botão PAGAMENTO permaneceu / filtro Sem pagamento.

O clique em Entregue no kanban às vezes não abre o detalhe (estado “Carregando…”). A intenção gravada é a condição que o backend exige.
