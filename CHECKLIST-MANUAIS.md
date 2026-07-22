# ✅ Checklist de Manuais — BeeFood

> Controle central de **ideias de manuais**, o que já foi **executado** e o que já foi **publicado**.
> Regras: o **dono publica** e avisa → só então marcamos a coluna **Publicado**.
> Cada manual concluído fica em `manuais/<nome>/`.

Última atualização: 2026-07-22 (adicionado #8 Integração 99 Entrega)

## Legenda de status

- 💡 **Ideia** — proposta, aguardando aprovação do dono.
- ☑️ **Aprovado** — aprovado, entrou na fila para execução.
- 🔨 **Em execução** — sendo produzido.
- ✅ **Concluído** — manual pronto no repositório.
- 🌐 **Publicado** — já publicado pelo dono (data informada por ele).

---

## Manuais (aprovados / em produção / concluídos)

| Nº | Manual | Escopo resumido | Pasta | Status | Publicado |
|----|--------|-----------------|-------|--------|-----------|
| 1 | **Abrir caixa** | Abrir o caixa, receber um pagamento em dinheiro (PDV) e consultar o valor no caixa | `manuais/caixa/` | ✅ Concluído | 🌐 Sim |
| 2 | **Fechar caixa + conferência** | Fechar o caixa, conferência de valores (1ª/2ª), quebra de caixa e saldo final | `manuais/caixa-fechar/` | ☑️ Aprovado | — |
| 3 | **Reabrir caixa** | Reabrir um caixa que já foi fechado (Reabrir Caixa) | `manuais/caixa-reabrir/` | ☑️ Aprovado | — |
| 4 | **Transferência entre caixas** | Transferir valores entre caixas (botão TRANSFERIR — requer permissão) | `manuais/caixa-transferir/` | ☑️ Aprovado | — |
| 5 | **Reforma Tributária (IBS/CBS)** | Os 6 campos novos, como editá-los na Edição Fiscal e como aparecem na nota (exemplo fake) | `manuais/reforma-tributaria-ibscbs/` | ✅ Concluído | — |
| 6 | **Ativação Aiqfome V2** | Conectar a loja do Aiqfome ao BeeFood (Store ID → cadastro em Aplicativos → autorização ID Magalu) | `manuais/ativacao-aiqfome/` | ✅ Concluído | — |
| 7 | **Integração Machine** | Despachar entregas pela central Machine: credenciais, config em Aplicativos → Entrega, despacho (manual/auto), acompanhamento e cancelamento | `manuais/integracao-machine/` | ✅ Concluído | — |
| 8 | **Integração 99 Entrega** | Cadastrar cartão + credenciais (Modo de desenvolvedor) na 99, conectar em Aplicativos → Entregas, despachar com cotação, acompanhar e cancelar | `manuais/integracao-99-entrega/` | ✅ Concluído | — |

---

## 💡 Backlog de ideias (aguardando aprovação)

> Ideias propostas. Quando o dono aprovar, sobem para a tabela acima com um número.

| Ideia | Escopo resumido | Status |
|-------|-----------------|--------|
| Sangria | Retirar dinheiro do caixa (botão SANGRIA) | 💡 Ideia |
| Acréscimo / reforço | Adicionar dinheiro ao caixa (botão ACRÉSCIMO) | 💡 Ideia |
| Imprimir resumo do caixa | Resumo / Resumo Frete / Resumo Presencial | 💡 Ideia |
| Ver conferência (caixa fechado) | Consultar a conferência de um caixa já fechado (VER CONFERÊNCIA) | 💡 Ideia |
| Entender a listagem de caixas | Colunas, status e filtro por usuário | 💡 Ideia |
| Cancelamentos | Aba Cancelamentos (perfil gerente) | 💡 Ideia |

---

## Histórico

- 2026-06-19 — Criado o checklist. Manual #1 (**Abrir caixa**) marcado como Concluído e Publicado.
- 2026-06-19 — Aprovados e adicionados: #2 Fechar caixa + conferência, #3 Reabrir caixa, #4 Transferência entre caixas. Demais ideias movidas para o backlog.
- 2026-06-19 — Iniciado #5 Reforma Tributária (IBS/CBS) — prioridade pedida pelo dono. **Bloqueio:** catálogo de CST/cClassTrib vazio no sandbox (selects sem opções); decisão de como seguir pendente. Imagens parciais já em `imagens-puras/`.
- 2026-06-19 — **Bloqueio resolvido:** API de produção estava desatualizada; após **logout + login** (limpa o cache de dados do localStorage) os catálogos de CST e cClassTrib passaram a carregar. Fluxo de edição validado de ponta a ponta no produto "10 mini churros" (CST 000, cClassTrib 000001, IBS UF 0,10, CBS 0,90 → **1 produto atualizado**). Novas imagens 07–10 salvas em `imagens-puras/`.
- 2026-06-19 — **#5 Concluído.** Geradas imagens anotadas (setas verdes 04, 07, 08, 09) e escrito `reforma-tributaria.md` (passo a passo + exemplo fictício de como aparece na nota). Aguardando publicação do dono.
- 2026-06-26 — **#6 Concluído.** Importado de `beefood-server-aiqfome/docs`, organizado no padrão (manual + MEMORIA + texto-documentation.ia + imagens-puras/tratadas). Texto melhorado conforme as imagens (rótulos exatos: SALVAR (F2), painel Geraldo, Status automático, etc.). Imagens já vieram prontas (sem `annotate.py`).
- 2026-07-08 — **#7 Concluído.** Importado de `beefood3-server-entregas/docs/machine`, organizado no padrão (manual + MEMORIA + texto-documentation.ia + fluxo-codigo + imagens-puras/tratadas). Base: `README.md` (manual) + APIs (`api-credencial.md`, `api-pedido-cancelamento.md`, SQL do webhook) consolidadas no `fluxo-codigo.md`. 7 imagens já prontas (destaques verdes), apenas copiadas. Aguardando publicação do dono.
- 2026-07-22 — **#8 Concluído.** Importado de `beefood3-server-entregas/docs/nn-entregas`. Manual **já vinha escrito** (`onboarding-99-entrega.md`) — copiado como está para `integracao-99-entrega.md` **sem reescrever** (único ajuste: caminhos `imagens/` → `imagens-tratadas/`). APIs (`api-cotacao.md` + `schema.sql`) consolidadas no `fluxo-codigo.md`. 15 imagens já prontas (setas/caixas verdes), apenas copiadas. Aguardando publicação do dono.
