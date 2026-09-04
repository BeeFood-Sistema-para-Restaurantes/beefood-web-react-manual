# Fluxo de código — Cadastrar forma de recebimento (#82)

Levantado em 03/09/2026 em `~/refs/beefood-web-react` (leitura) e no sandbox.
**Não publicar nada daqui no manual.**

---

## 1. As três telas (a origem da confusão)

| Tela | Rota | Entidade | Papel |
|------|------|----------|-------|
    10|| **Cadastros → Formas Recebimento** | `/formas-recebimento` | `formaPagamento` | Formas das **vendas**; flags `delivery` e `presencial` |
| **Cardápio Digital → Formas Recebimento** | `/cardapio-digital?tab=formasRecebimento` | `deliveryRecebimento` (por filial) | O que o **cliente** vê na sacola; flags `delivery` e `retirada`; vínculo opcional `formaPagamentoID` |
| **Financeiro → Formas Pagamento** | `/formas-pagamento` | formas financeiras | Contas a pagar/receber + espelho **read-only** das formas de venda com taxas |

Arquivos: `src/pages/Cadastros.tsx` +
`src/components/cadastros/CadastroFormasRecebimentoTab.tsx` +
`src/components/ModalEditarFormaRecebimento.tsx` (o modal das três abas);
`src/components/cardapio-digital/FormasRecebimentoTab.tsx` +
`ModalAdicionarRecebimento.tsx`; `src/pages/FormasPagamento.tsx`.
    20|Permissões independentes: `cadastros.formasRecebimento`, `cardapioDigital.formasRecebimento`,
`financeiro.formasPagamento`.

---

## 2. Canais: como o filtro funciona

`useModalPagamentosLogic` decide o que aparece na hora de receber:

```
tipo === 'DELIVERY' ? fp.delivery === true : fp.presencial === true
    30|&& (fp.usuarioID === usuarioLogado || fp.usuarioID === null)
&& fp.beetech !== true && fp.mercadoPago !== true
```

Ou seja:

- **Não existe flag de PDV.** PDV, mesa e comanda caem em `presencial`.
- Forma com `usuarioID` só aparece para aquele usuário.
- Formas de integração (`beetech`, `mercadoPago`) são **ocultadas** do operador e ficam
  read-only na listagem (badges **BeeFood** / **Mercado Pago**).
    40|- A **intenção de pagamento** do delivery exclui `Fiado` e `PIX Beetech` da sugestão.

---

## 3. Campos do modal (Cadastros)

**Aba Configuração:** `Título` (obrigatório — toast *"Informe o título da forma de recebimento"*),
`Tipo` (radio), `Ativo`, `Delivery/Retirada`, `Presencial`, `Aplicativo Garçom`,
`Aplicativo Garçom Stone`, `Ajuste no pagamento` (+ `Percentual (%)` / `Valor (R$)`), `Ordem`,
`Usuário Vinculado`.

    50|Os `id` dos radios de tipo são `tipo-<valor>` (ex.: `#tipo-Vale Refeição`) — foi assim que a
captura selecionou o tipo; clicar no texto do rótulo **não** marca o radio.

**Tipos** (`tiposForma`): `Dinheiro`, `Cartão de Crédito`, `Cartão de Débito`, `Crédito Loja`,
`Vale Alimentação`, `Vale Refeição`, `Carteira Digital` (rótulo *Carteira Digital (PIX)*),
`PIX Beetech` (rótulo *PIX Online*), `Fiado`, `Outros`.

**Aba Taxas e Bandeiras:** desabilitada para `Dinheiro`, `Fiado` e `PIX Beetech`
(`title="Não disponível para este tipo de pagamento"`). Tem `Taxa (%)`,
`Desconto Fixo (R$)` (mutuamente exclusivos), `Dias para Recebimento`, `Conta Bancária` e a grade
    60|de bandeiras (`Ativo`, `Taxa (%)`, `Desc. Fixo`, `Dias Receb.` por bandeira). No sandbox a grade
tem 20+ bandeiras, incluindo *Sodexo*, *Alelo* e *VR*.

**Aba TEF (Stone/PayGo):** `Provedor Padrão` (texto) e a lista `TEF Vinculada`. Vincular exige a
forma já salva (*"É necessário salvar a forma de recebimento antes de vincular TEF"*).

**Rodapé:** `FECHAR (ESC)` e `SALVAR E SAIR (F2)`. **Trocar de aba salva a forma** quando ela
ainda não tem ID (toast *"Forma de recebimento salva!"*) — foi assim que a captura gravou antes de
preencher as taxas.

---
    70|

## 4. Rotas de API

| Operação | Método | Caminho |
|----------|--------|---------|
| Listar (cadastro) | GET | `/api/empresa2/formaRecebimentos/{empresaID}/{usuarioID}` |
| Detalhe | GET | `/api/empresa2/formaRecebimento/{empresaID}/{usuarioID}/{formaPagamentoID}` |
| Salvar | POST | `/api/empresa2/formaRecebimento` |
| Flags/ordem (switches da lista) | POST | `/api/empresa2/formaRecebimentos/atualizaFlags` |
| Taxas e bandeiras | GET/POST | `/api/empresa2/formaRecebimento/config[...]` |
    80|| Vincular TEF | POST | `/api/empresa2/formaRecebimento/tef` |
| Lista usada na venda | GET | `/datasnap/rest/empresa2/formaPagamento/{empresaID}/{usuarioID}` |
| Cardápio digital | GET/POST/DELETE | `/datasnap/rest/empresaDelivery2/cardapioDigital/recebimento[...]` |
| Financeiro | GET/POST/DELETE | `/api/financeiro2/formaRecebimento[s][...]` |

**A listagem de Cadastros não tem exclusão** — só `Ativo`. A exclusão existe no financeiro e no
cardápio digital.

---

    90|## 5. Medições no sandbox (03/09/2026, empresa 38311 / filial 39202)

- Antes: **20 formas** no cadastro de vendas e **18** no cardápio digital.
- Criada a forma **Vale Refeição Sodexo** (tipo `Vale Refeição`, `delivery` e `presencial`
  ligados, `Taxa 4,5%`, `Dias para Recebimento 30`, ordem 1) → **21 formas**.
- A forma apareceu **na primeira posição** da tela de recebimento de uma mesa, com atalho
  **CTRL+1** — prova do canal `presencial` (a venda era de mesa).
- Descobertas de tela que viraram texto:
  - a aba **Taxas e Bandeiras** nasce **desabilitada** porque o tipo padrão é `Dinheiro`;
  - `Taxa (%)` e `Desconto Fixo (R$)` se bloqueiam mutuamente;
   100|  - as formas com ajuste mostram o valor **na tela de recebimento**, embaixo do nome
    (`-1,00%` no Dinheiro, `+3,00%` no Crédito, `+R$ 5,00` no Vale Alimentação).
- **Nada foi recebido**: a tela de pagamento da mesa 2 foi aberta apenas para fotografar a lista e
  fechada sem confirmar.
