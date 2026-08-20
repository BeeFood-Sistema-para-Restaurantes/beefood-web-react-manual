# fluxo-codigo.md — Fiado: Cobrança agrupada

Mapeamento técnico. Documento interno — **não publicar**.

---

## 1. Entrada

**Fiado → Controle de Dívidas → Cobrança agrupada** (`BotaoCobrancaAgrupada.tsx` → `ModalCobrancaAgrupada.tsx`).

Badge **NOVO** no botão. Rascunhos em `localStorage` via `cobrancaAgrupadaStorage.ts` (por `empresaID`).

---

## 2. Stepper (4 fases)

| Fase | Componente | Validação `podeAvancar` |
|------|------------|-------------------------|
| 1 Seleção | `FaseSelecaoClientes` | `clientesSel.length > 0` |
| 2 Extrato | `FaseExtratoAgrupado` | extrato carregado com pendências |
| 3 Pagamentos | `FasePagamentos` + `LinhaPagamento` | ≥1 pagamento válido; total ≤ dívida |
| 4 Processamento | `FaseProcessamento` | executa POSTs de pagamento fiado |

---

## 3. Fase 1 — Seleção

- Lista só clientes com `saldo < 0` (`clientesComDivida`).
- **Data limite de corte** opcional (`dataCorteISO`); sem data = histórico ativo inteiro.
- Checkbox por cliente; clique na linha também alterna.

---

## 4. Fase 2 — Extrato consolidado

- Hook `useCobrancaAgrupadaExtrato` busca extrato detalhado por cliente.
- Mesma lógica de timeline e rateio por produto do extrato individual.
- Impressão: `exportarCobrancaAgrupadaPDF` ou cupom térmico (`ModalEscolherFormatoImpressao`).

---

## 5. Fase 3 — Pagamentos

- Várias linhas; formas disponíveis excluem **Fiado** e **PIX Beetech**.
- **Pagamento parcial** permitido — rateio proporcional (`cobrancaAgrupadaRateio.ts`).
- Não pode exceder total da dívida.

---

## 6. Fase 4 — Processamento

- `FaseProcessamento` chama API `POST /api/fiado2/pagamento` por cliente/rateio.
- Barra de progresso; retentativas em falha.
- Resultado = pagamentos fiado normais (caixa, relatórios).

---

## 7. Rascunhos

- Botão **Salvar** grava estado local (clientes, data corte, pagamentos).
- Dropdown ao lado do botão lista rascunhos para retomar ou excluir.
- Ao fechar com alterações: **Salvar e fechar** ou **Descartar**.
- **Somente neste computador/navegador** — não sincroniza entre dispositivos.

---

## 8. Observações para o manual

1. Processamento real altera saldos — usar valor simbólico no sandbox (ex.: R$ 1,00).
2. Borrar dados pessoais nas fases 1 e 2.
3. Manual separado do #25 (operar no dia a dia) por complexidade do fluxo.
