# ✅ Checklist de Manuais — BeeFood

> Controle central de **ideias de manuais**, o que já foi **executado** e o que já foi **publicado**.
> Regras: o **dono publica** e avisa → só então marcamos a coluna **Publicado**.
> Cada manual concluído fica em `manuais/<nome>/`.

Última atualização: 2026-08-04 (2º reimport #11 Integração Uber Direct — +passos de despacho/cancelamento, 27 imagens)

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
| 9 | **Integração Repediu** | Gerar Client ID/Secret (Repediu → Integrações) e Write Key (Repediu → Web/App Analytics), preencher em Aplicativos → Marketing e CRM → Repediu → Configurar e salvar (Tracker de Vendas + Cardápio Digital) | `manuais/integracao-repediu/` | ✅ Concluído | — |
| 10 | **Integração FoodCRM** | Gerar a API Key/Token (FoodCRM → Integrações → Acessar a documentação) e cadastrar por cardápio em Aplicativos → Marketing e CRM → FoodCRM (envio automático das vendas diariamente de madrugada) | `manuais/integracao-foodcrm/` | ✅ Concluído | — |
| 11 | **Integração Uber Direct** | Criar conta Uber + Uber Direct, cadastrar cartão e webhook, copiar a Chave de autenticação do webhook + credenciais (ID do usuário/ID de cliente/Client Secret), colar em Aplicativos → Entregas → Uber Direct e usar no dia a dia (despachar pedido, acompanhar e cancelar) | `manuais/integracao-uber-direct/` | ✅ Concluído | — |

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
- 2026-07-24 — **#9 Concluído.** Produzido do zero. Fluxo validado ao vivo: **Repediu** (`app.repediu.com.br`, login `integracao@beefood.com.br` — exigiu captcha + 2FA destravados pelo dono) para gerar Client ID/Secret (Integrações → Fontes de dados → BeeFood) e Write Key (Web/App Analytics → Configuração → BeeFood → Gerar chave); **BeeFood** (sandbox) em Aplicativos → Marketing e CRM → Repediu → Configurar, preenchendo os dois trackers e **salvando de verdade** (ambos ativos). **Descoberta:** os painéis do Repediu são modais laterais (~30% dir.) — para o screenshot capturar é preciso `browser_navigate` completo (não só cliques SPA) e navegador em foco. 10 imagens (setas verdes via `annotate.py`, exceto 08 contexto). Chaves mantidas visíveis (conta de teste). Aguardando publicação do dono.
- 2026-08-04 — **#11 reimportado (fonte atualizada — "faça o merge novamente").** Nova versão: **10 passos** (novo **passo 8: copiar a Chave de autenticação do webhook**) e conjunto de imagens agora **`01`..`21`** (removida a `00`; novas `19`/`21`; várias reexportadas). Refiz imagens (puras+tratadas), manual, `texto-documentation.ia.md` (21 imagens). Surgiram docs de API no fonte (`api-conta/credencial/entrega/webhook.md`, `README.md`, `schema-add-marketplace-ids.sql`) — consolidadas no `fluxo-codigo.md` (rotas `/api/uberDirect/*`, OAuth `eats.deliveries`, webhook HMAC via `webhook_signing_key`, tabelas `uber_direct_credencial/pedido/webhook`). Aguardando publicação do dono.
- 2026-08-04 — **#11 Concluído.** Importado de `beefood3-server-entregas/docs/uber-direct`. Manual **já vinha escrito** — havia dois `.md` (`onboarding-uber-direct.md` em MDX com Steps/Callout e `onboarding-uber-direct-preview.md` em plain markdown). Usei a versão **preview (plain markdown)** como `integracao-uber-direct.md` (casa com o padrão do repo), **sem reinterpretar**; único ajuste: caminhos `imagens/` → `imagens-tratadas/`. 20 imagens já prontas (`uber-direct-00`..`18` + `20`, sem a 19), copiadas para puras/tratadas. `fluxo-codigo.md` consolidado do código (`useCredenciaisEntrega.ts`, `appCategories.ts` — card ainda `disabled: 'Em breve!'`) + webhook `https://entregas.beefoodapi.be/api/uberDirect/webhook`. Cada loja tem conta/cartão próprios; Uber cobra no cartão. Aguardando publicação do dono.
- 2026-07-24 — **#10 Concluído.** Produzido do zero (após `git pull` do `beefood-web-react`, que trouxe o código novo do FoodCRM). Fluxo validado ao vivo: **FoodCRM** (`app.foodcrm.com.br`, login `beefood@foodcrm.com.br`, conta "BeeFood Teste") → **Integrações** → **Acessar a documentação** → copiar **API Key/Token** (`fcrm_...`); **BeeFood** (sandbox) em Aplicativos → Marketing e CRM → FoodCRM → cardápio → **+ Adicionar** → colar API key → Ativo → **SALVAR** (salvo de verdade, status Ativo). **Descobertas:** "Acessar a documentação" abre um **drawer lateral** (não página externa); o BeeFood pede **só** a `api_key` (Código da loja não é usado); existe um card "BeeFood" reverso (webhook) que **não** foi documentado. Integração = **envio automático das vendas, diário de madrugada**. 6 imagens (setas verdes via `annotate.py`), FoodCRM capturado em **tema claro**. Aguardando publicação do dono.
