# fluxo-codigo.md — Fiado (operar no dia a dia)

Mapeamento técnico no front (`beefood-web-react`) e backend (`beetech-server-node-2.0`).
Documento interno — **não publicar**.

Levantado em 20/08/2026.

---

## 1. Visão geral

```
Menu lateral -> Fiado                    (/fiado, chave permissão: fiado)
   |
   +-- Aba Visão Geral                   FiadoVisaoGeralTab
   +-- Aba Controle de Dívidas           FiadoControleDividasTab
   +-- Aba Vendas sem Pagamento          FiadoVendasSemPagamentoTab (migração Conta Corrente)
```

API base: `/api/fiado2/*` (`src/api/routes/fiadoRouter2.js`).

| Endpoint | Uso |
|----------|-----|
| `GET /visaoGeral/{empresaID}/{usuarioID}` | KPIs: totalDivida, totalClientesDivida, totalSemPagamentoHa30DiasMais |
| `GET /visaoGeralData/{empresaID}/{usuarioID}` | Operações do período (valor < 0 = venda fiado; > 0 = recebimento) |
| `GET /clientes/{empresaID}/{usuarioID}` | Lista de clientes com saldo |
| `GET /cliente/{empresaID}/{usuarioID}/{clienteID}` | Extrato do cliente |
| `POST /pagamento` | Registrar pagamento ou dívida manual |
| `POST /pagamentoNaoPago` | Cancelar pagamento (exige gerente) |

---

## 2. Convenção de sinal

Na tabela `fiado`, **valores negativos = dívida gerada**; **positivos = pagamento recebido**.
O extrato exibe saldo acumulado a partir desses lançamentos.

---

## 3. Gerar dívida na venda

Origens: **PDV**, **Mesas/Comandas**, **Delivery** — modal `ModalPagamentos`.

Regra (`useModalPagamentosLogic.ts`):

- Forma `tipo === 'Fiado'` exige `venda.clienteID`; senão toast de erro.
- Campo **Observação (opcional)** quando Fiado selecionado.
- Ao confirmar, backend grava pagamento fiado e lança dívida via `inserirDivida`.

Forma de recebimento tipo **Fiado** cadastrada em **Cadastros → Formas de recebimento**.

---

## 4. Registrar pagamento pelo módulo Fiado

`fiadoPagamentoPOST.js`:

- **Exige caixa aberto** (`retornaCaixaAberto`); senão HTTP 400.
- Insere lançamento positivo e operação no caixa (`procInsertCaixaOperacaoFiado`).
- Formas **Fiado** e **PIX Beetech** ficam ocultas no modal de pagamento manual.

Modal **Registrar dívida** (`ModalRegistrarDivida`): valor negativo + **observação obrigatória**.

---

## 5. Extrato e extrato detalhado

- `ModalExtratoCliente`: drawer lateral — botões **PAGAMENTO**, **DÍVIDA**, **Extrato Detalhado**, imprimir PDF/cupom.
- `ModalExtratoDetalhado`: rateio por produto (`fiadoRateioProduto.ts`), abas *Somente dívida* / *Extrato completo*.
- Cancelamento: `useFiadoPagamentoNaoPago` + motivo (se parâmetro) + `ModalValidarSenhaGerente`.

Também existe aba **Fiado** no cadastro de **Clientes** (`ClienteFiadoTab.tsx`) — mesmos modais.

---

## 6. Aba Vendas sem Pagamento (migração)

**Não é** pendência de fechamento de caixa.

- Hook `useMigracaoCliente` → `GET /api/empresa2/migracao/cliente/{empresaID}/{usuarioID}`.
- Botão **Converter para Fiado** → `POST /api/empresa2/migracao/cliente` com `preVendaID`.
- Contexto: migração **Conta Corrente → Fiado** (`MigrarDados.tsx`).

---

## 7. Caixa

- Conferência de fechamento inclui coluna **Fiado** (`useCaixaFecharDetalhes.ts`).
- Resumo do caixa filtra `op.fiado === true` (`caixaResumoFilter.ts`).
- Pagamentos de fiado registrados pelo módulo entram como operação no caixa aberto.

---

## 8. Permissões

Rota protegida: `ProtectedRoute menuKey="fiado"` (`App.tsx`).
Visibilidade: `canViewMenuItem('/fiado')` / `isMenuItemEnabled('/fiado')` (`AppSidebar.tsx`).

---

## 9. Observações para o manual

1. Diferenciar **venda fiado no PDV** de **ajuste manual** no extrato.
2. **Caixa aberto** é pré-requisito para receber pagamento pelo Fiado.
3. Borrar **nome e telefone** de clientes nas capturas (repositório público).
4. A aba **Vendas sem Pagamento** só interessa lojas em migração; no sandbox havia ~240 itens (19/08/2026).
