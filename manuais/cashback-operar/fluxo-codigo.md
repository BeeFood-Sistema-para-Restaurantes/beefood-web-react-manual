# fluxo-codigo.md — #20 Cashback operar (uso interno, NÃO publicar)

- Abas: `historico` (`CashbackHistoricoCRMTab`), `saldoCliente` (`CashbackSaldoClienteCRMTab`), `filaProcessamento` (`CashbackFilaProcessamentoCRMTab`).
- Histórico: `GET .../cashbackHistorico/{empresa}/{filial}/{usuario}?dataInicio=&dataFim=`. `filialID=0` = todos.
- Saldo lista: `GET .../cashbackSaldoClientes/{empresa}/{filial}/{usuario}`.
- Extrato um cliente: `GET .../cashbackSaldoCliente/{empresa}/{filial}/{usuario}/{clienteID}`.
- Ajuste: `POST /api/cliente2/cashback/inserir` e `POST /api/cliente2/cashback/uso` (`useCashbackAjuste`). Motivo obrigatório.
- Fila: `GET /api/cliente2/cashback/fila/{empresa}/{usuario}`. `processado` + `resultado` → pendente / sucesso / erro.
- Na venda: `isCashbackHabilitadoNaVenda` (`cashbackPagamentoConfig.ts`) olha tipo PDV/MESA/DELIVERY + flags da filial. `PanelUsarCashback` + `ModalAplicarCashback` em `ModalPagamentos`.
- Saldo na venda: `GET /api/cliente2/cashback/saldo/{empresa}/{usuario}/{filial}/{clienteID}`.
- Cadastro do cliente: `ClienteCashbackTab` + o mesmo `ModalAjusteSaldo`.
- Cardápio: Perfil → Programa de fidelidade (pode pedir senha da conta). Aplicar no checkout é do Vue público.
- Crédito: só madrugada, pedido quitado. Uso: imediato no pagamento.
