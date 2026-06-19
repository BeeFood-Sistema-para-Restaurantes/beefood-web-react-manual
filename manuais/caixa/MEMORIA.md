# MEMÓRIA — Manual de Caixa

> Memória detalhada deste manual (fluxo, uso, decisões e estado), para retomar a qualquer momento.
> Ver também a memória geral: `..\..\MEMORIA-GERAL.md`.

Status: ✅ **Concluído** — Última atualização: 2026-06-18

---

## 1. Escopo do manual

Ensinar o usuário final a:
1. **Abrir um caixa**.
2. **Receber um pagamento** (que cai automaticamente no caixa).
3. **Consultar o valor** no caixa aberto.

Arquivo final: `caixa.md`. Mapa técnico do código: `fluxo-codigo.md`.

---

## 2. Conteúdo da pasta

```
manuais\caixa\
├─ MEMORIA.md          (este arquivo)
├─ caixa.md            (manual final)
├─ fluxo-codigo.md     (mapeamento do código: rotas, componentes, labels, API)
├─ annotate.py         (gera imagens-tratadas a partir de imagens-puras)
├─ imagens-puras\      (01..09 originais — backup)
└─ imagens-tratadas\   (03,05,06,08,09 com setas/números — usadas no manual)
```

---

## 3. Fluxo executado (passo a passo real)

Ambiente: conta **BeeFood3 - Manual** (`contato@beefood.com.br`), tema claro.

1. **Abrir caixa** (`/caixa` → botão **Abrir Caixa**):
   - Saldo Inicial em Dinheiro **R$ 50,00** (obrigatório).
   - Caixa: **caixa1** (obrigatório, já vinha pré-selecionado).
   - Tipos de Venda: Presencial + Delivery (padrão ligados).
   - Botão **ABRIR CAIXA** → toast "Caixa aberto com sucesso".
   - Resultado: caixa1 aberto em **18/06/2026 21:29**, status "Em aberto".
2. **Receber pagamento** (`/pdv`):
   - Produto: **Coca Cola 350ml — R$ 4,44** (item mais barato, p/ valor baixo).
   - Botão **Receber (F3)** → modal "Conferir e Dividir — Venda #571".
   - Forma de pagamento: **Dinheiro** → valor R$ 4,44 → **CONFIRMAR (ENTER/F1)**.
   - Resultado: "Dinheiro — Pago", "Pagamento completo". Venda #571 finalizada.
3. **Consultar** (`/caixa` → **Ver Caixa** na linha "Em aberto"):
   - Operações: `Venda Nº 571 — R$ 4,44 — Dinheiro` e `ABERTURA CAIXA — R$ 50,00`.
   - Resumo Dinheiro: SALDO INICIAL R$ 50,00 | VENDAS EM DINHEIRO R$ 4,44 | **VALOR EM CAIXA R$ 54,44**.
   - Confere: 50,00 + 4,44 = 54,44. ✔

---

## 4. Mapa das imagens (número da seta → alvo)

| Arquivo | Etapa | Setas |
|---------|-------|-------|
| `01-caixa-listagem.png` | (contexto) listagem antes de abrir | — |
| `03-modal-abrir-caixa-preenchido.png` | Abrir | ① Saldo Inicial* ② Caixa* ③ Tipos de Venda ④ ABRIR CAIXA |
| `04-caixa-aberto-listagem.png` | (contexto) caixa recém-aberto | — |
| `05-pdv-formas-pagamento.png` | Pagamento | ① Dinheiro ② Valor/Falta |
| `06-pdv-dinheiro-valor.png` | Pagamento | ① Valor do pagamento ② CONFIRMAR |
| `07-pdv-pagamento-resultado.png` | (contexto) "Pagamento completo" | — |
| `08-caixa-listagem-aberto.png` | Consulta | ① Ver Caixa (lupa) ② Em aberto |
| `09-ver-caixa-check.png` | Consulta | ① operação Venda 571 ② VENDAS EM DINHEIRO ③ VALOR EM CAIXA |

> Coordenadas das setas estão no `annotate.py` (frações 0..1). Para reanotar: `python annotate.py`.

---

## 5. Resumo técnico (ver `fluxo-codigo.md` para detalhes)

- Abrir: `src/components/CaixaAbrirModal.tsx` → `POST /datasnap/rest/caixa2/abrir`
  (payload: `saldoDinheiroInicial`, `obs`, `delivery`, `presencial`, `satID`).
- Pagamento de venda: `POST /datasnap/rest/venda2/pagamentoPago` (`caixaID: null`; backend associa ao caixa aberto).
- Consulta: `src/components/CaixaVerModal.tsx`; detalhes via `caixa2/caixaDetalhes/...`.
- Operações manuais: **SANGRIA** (saída) e **ACRÉSCIMO** (entrada; "suprimento") — `caixa2/operacaoManual`.
- Labels do Resumo Dinheiro: SALDO INICIAL, ENTRADA MANUAL, SANGRIAS, VENDAS EM DINHEIRO, VALOR EM CAIXA, TOTAL.

---

## 6. Estado deixado no sistema

- **Caixa1 segue ABERTO** na conta BeeFood3 - Manual, contendo a venda #571 (R$ 4,44) + abertura (R$ 50,00).
- Pendência opcional: fechar esse caixa (**FECHAR CAIXA** → conferência) se o usuário quiser limpar o ambiente.

---

## 7. Possíveis próximos incrementos deste manual

- Adicionar seção de **Sangria** e **Acréscimo** com prints próprios.
- Adicionar seção de **Fechar Caixa / Conferência**.
- Mostrar pagamento em outras formas (PIX, Cartão) e como aparecem no resumo.
