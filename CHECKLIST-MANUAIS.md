# ✅ Checklist de Manuais — BeeFood

> Controle central de **ideias de manuais**, o que já foi **executado** e o que já foi **publicado**.
> Regras: o **dono publica** e avisa → só então marcamos a coluna **Publicado**.
> Cada manual concluído fica em `manuais/<nome>/`.

Última atualização: 2026-08-19 (#13 Restrições de caixa concluído; os manuais de caixa
publicados pelo dono; #14 Segmentação de clientes aprovado e em estudo)

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
| 2 | **Fechar caixa** | Resolver vendas sem pagamento total, conferir os valores (1ª conferência, com a calculadora), entender a quebra de caixa, fechar e imprimir o resumo | `manuais/caixa-fechar/` | ✅ Concluído | 🌐 Sim |
| 3 | **Reabrir caixa** | Reabrir um caixa que já foi fechado (Reabrir Caixa) | `manuais/caixa-reabrir/` | ☑️ Aprovado | — |
| 4 | **Transferência entre caixas** | Transferir valores entre caixas (botão TRANSFERIR — requer permissão) | `manuais/caixa-transferir/` | ☑️ Aprovado | — |
| 5 | **Reforma Tributária (IBS/CBS)** | Os 6 campos novos, como editá-los na Edição Fiscal e como aparecem na nota (exemplo fake) | `manuais/reforma-tributaria-ibscbs/` | ✅ Concluído | — |
| 6 | **Ativação Aiqfome V2** | Conectar a loja do Aiqfome ao BeeFood (Store ID → cadastro em Aplicativos → autorização ID Magalu) | `manuais/ativacao-aiqfome/` | ✅ Concluído | — |
| 7 | **Integração Machine** | Despachar entregas pela central Machine: credenciais, config em Aplicativos → Entrega, despacho (manual/auto), acompanhamento e cancelamento | `manuais/integracao-machine/` | ✅ Concluído | — |
| 8 | **Integração 99 Entrega** | Solicitar **boleto** (único pagamento) + **ambiente de produção** e credenciais (Modo de desenvolvedor) na 99, cadastrar webhook, conectar em Aplicativos → Entregas, despachar com cotação, acompanhar e cancelar | `manuais/integracao-99-entrega/` | ✅ Concluído | — |
| 9 | **Integração Repediu** | Gerar Client ID/Secret (Repediu → Integrações) e Write Key (Repediu → Web/App Analytics), preencher em Aplicativos → Marketing e CRM → Repediu → Configurar e salvar (Tracker de Vendas + Cardápio Digital) | `manuais/integracao-repediu/` | ✅ Concluído | — |
| 10 | **Integração FoodCRM** | Gerar a API Key/Token (FoodCRM → Integrações → Acessar a documentação) e cadastrar por cardápio em Aplicativos → Marketing e CRM → FoodCRM (envio automático das vendas diariamente de madrugada) | `manuais/integracao-foodcrm/` | ✅ Concluído | — |
| 11 | **Integração Uber Direct** | Criar conta Uber + Uber Direct, cadastrar cartão e webhook, copiar a Chave de autenticação do webhook + credenciais (ID do usuário/ID de cliente/Client Secret), colar em Aplicativos → Entregas → Uber Direct e usar no dia a dia (despachar pedido, acompanhar e cancelar) | `manuais/integracao-uber-direct/` | ✅ Concluído | — |
| 12 | **Segunda conferência (dupla checagem)** | Por que recontar, abrir a conferência de um caixa fechado (Ver Conferência), Adicionar 2ª Conferência, recontar com a calculadora, observações, marcar como conferido (cadeado) e resolver a quebra de caixa | `manuais/caixa-conferencia-2/` | ✅ Concluído | 🌐 Sim |
| 13 | **Restrições de caixa (grupo de acesso)** | Todas as restrições de caixa que podem ser aplicadas a um usuário — Abrir e Fechar Caixa, Visualizar Valores de Referência, Visualizar Caixas Fechados, Transferência de Operações, Cadastro de Caixas, Função Gerente e o parâmetro Caixa por Usuário — cada uma com **como configurar** e **como o caixa fica** | `manuais/caixa-restricoes/` | ✅ Concluído | 🌐 Sim |
| 14 | **Segmentação de clientes** | Criar públicos em Food Marketing → Segmentação de Cliente: o que é, os 37 filtros disponíveis, como combinar com E/OU, testar o tamanho do público e usar em campanhas — com vários exemplos prontos de restaurante | `manuais/segmentacao-clientes/` | ☑️ Aprovado | — |

---

## 💡 Backlog de ideias (aguardando aprovação)

> Ideias propostas. Quando o dono aprovar, sobem para a tabela acima com um número.

| Ideia | Escopo resumido | Status |
|-------|-----------------|--------|
| Sangria | Retirar dinheiro do caixa (botão SANGRIA) | 💡 Ideia |
| Acréscimo / reforço | Adicionar dinheiro ao caixa (botão ACRÉSCIMO) | 💡 Ideia |
| Imprimir resumo do caixa | Resumo / Resumo Frete / Resumo Presencial | 💡 Ideia |
| ~~Ver conferência (caixa fechado)~~ | Consultar a conferência de um caixa já fechado (VER CONFERÊNCIA) | ❌ **Absorvida pelo #12** — é o mesmo componente do fechamento em modo leitura, não rende manual próprio |
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
- 2026-08-05 — **#8 recriado do zero** (a pedido: "delete e copie novamente de beefood3-server-entregas"). Fonte **totalmente atualizada**: pagamento da integração passou a ser **somente boleto** (não mais cartão), com novos passos de **solicitar boleto** e **pedir ambiente de produção** (ambos com análise da 99). Manual agora com **7 passos** (config + despacho/acompanhamento/cancelamento) e **24 imagens** na origem — o texto referencia `05`..`24` (20 imagens); `01`..`04` (fluxo antigo de cartão) ficam só em `imagens-puras/`. `fluxo-codigo.md` atualizado com os novos schemas (rename `nn_entregas_*`→`nn_entrega_*`, drops de colunas, IDs de marketplace). Aguardando publicação do dono.
- 2026-07-24 — **#9 Concluído.** Produzido do zero. Fluxo validado ao vivo: **Repediu** (`app.repediu.com.br`, login `integracao@beefood.com.br` — exigiu captcha + 2FA destravados pelo dono) para gerar Client ID/Secret (Integrações → Fontes de dados → BeeFood) e Write Key (Web/App Analytics → Configuração → BeeFood → Gerar chave); **BeeFood** (sandbox) em Aplicativos → Marketing e CRM → Repediu → Configurar, preenchendo os dois trackers e **salvando de verdade** (ambos ativos). **Descoberta:** os painéis do Repediu são modais laterais (~30% dir.) — para o screenshot capturar é preciso `browser_navigate` completo (não só cliques SPA) e navegador em foco. 10 imagens (setas verdes via `annotate.py`, exceto 08 contexto). Chaves mantidas visíveis (conta de teste). Aguardando publicação do dono.
- 2026-08-04 — **#11 reimportado (fonte atualizada — "faça o merge novamente").** Nova versão: **10 passos** (novo **passo 8: copiar a Chave de autenticação do webhook**) e conjunto de imagens agora **`01`..`21`** (removida a `00`; novas `19`/`21`; várias reexportadas). Refiz imagens (puras+tratadas), manual, `texto-documentation.ia.md` (21 imagens). Surgiram docs de API no fonte (`api-conta/credencial/entrega/webhook.md`, `README.md`, `schema-add-marketplace-ids.sql`) — consolidadas no `fluxo-codigo.md` (rotas `/api/uberDirect/*`, OAuth `eats.deliveries`, webhook HMAC via `webhook_signing_key`, tabelas `uber_direct_credencial/pedido/webhook`). Aguardando publicação do dono.
- 2026-08-04 — **#11 Concluído.** Importado de `beefood3-server-entregas/docs/uber-direct`. Manual **já vinha escrito** — havia dois `.md` (`onboarding-uber-direct.md` em MDX com Steps/Callout e `onboarding-uber-direct-preview.md` em plain markdown). Usei a versão **preview (plain markdown)** como `integracao-uber-direct.md` (casa com o padrão do repo), **sem reinterpretar**; único ajuste: caminhos `imagens/` → `imagens-tratadas/`. 20 imagens já prontas (`uber-direct-00`..`18` + `20`, sem a 19), copiadas para puras/tratadas. `fluxo-codigo.md` consolidado do código (`useCredenciaisEntrega.ts`, `appCategories.ts` — card ainda `disabled: 'Em breve!'`) + webhook `https://entregas.beefoodapi.be/api/uberDirect/webhook`. Cada loja tem conta/cartão próprios; Uber cobra no cartão. Aguardando publicação do dono.
- 2026-07-24 — **#10 Concluído.** Produzido do zero (após `git pull` do `beefood-web-react`, que trouxe o código novo do FoodCRM). Fluxo validado ao vivo: **FoodCRM** (`app.foodcrm.com.br`, login `beefood@foodcrm.com.br`, conta "BeeFood Teste") → **Integrações** → **Acessar a documentação** → copiar **API Key/Token** (`fcrm_...`); **BeeFood** (sandbox) em Aplicativos → Marketing e CRM → FoodCRM → cardápio → **+ Adicionar** → colar API key → Ativo → **SALVAR** (salvo de verdade, status Ativo). **Descobertas:** "Acessar a documentação" abre um **drawer lateral** (não página externa); o BeeFood pede **só** a `api_key` (Código da loja não é usado); existe um card "BeeFood" reverso (webhook) que **não** foi documentado. Integração = **envio automático das vendas, diário de madrugada**. 6 imagens (setas verdes via `annotate.py`), FoodCRM capturado em **tema claro**. Aguardando publicação do dono.
- 2026-08-19 — **#2 Concluído** (produzido do zero no Cloud Agent). **Escopo mudou durante o diagnóstico:** não existe modal separado de conferência — o `CaixaFecharModal` **é** a tela de conferência (título em tela: *Conferência de Valores - 1ª Conferência*) e é o mesmo componente do **Ver Conferência**, só com `readOnly`. Por isso o manual virou um percurso único e a **2ª conferência saiu do #2** e entrou como **#12** (aprovado pelo dono), reaproveitando o mesmo caixa. Fluxo executado ao vivo no **caixa1** (aberto em 17/07/2026): 74 vendas sem pagamento total, **uma quitada como exemplo** (venda #723, R$ 17,80 em Débito), 1ª conferência das 6 formas de pagamento com o **dinheiro contado pela calculadora** (R$ 50 + R$ 20 + R$ 20 + R$ 10 = R$ 100,00 contra R$ 102,55 apurados) gerando **quebra leve de R$ 2,55 (Falta)** — proposital, para ser resolvida no #12 — e **fechamento real** em 19/08/2026 10:18. 12 imagens (setas verdes, badges na margem do overlay). Numeração passou a usar **1, 2, 3** (o `③` ficava ilegível). **Atenção:** o caixa1 ficou fechado **sem** 2ª conferência de propósito; não clicar em *Adicionar 2ª Conferência* nele. Aguardando publicação do dono.
- 2026-08-19 — **#12 Concluído** (na sequência do #2, no mesmo caixa). Manual da **dupla checagem**, abrindo com a seção *por que a segunda conferência importa* (protege a equipe de suspeita injusta, deixa registro auditável, faz o saldo conferido refletir a recontagem). Fluxo real: **Ver Conferência** do caixa1 fechado → **Adicionar 2ª Conferência** → recontagem do dinheiro pela calculadora (**R$ 100,00 + R$ 2,55 = R$ 102,55**, os centavos estavam em moedas) → observação escrita → checkbox *Conferência realizada e valores conferidos* → **Conferir**. Resultado: **quebra de R$ 2,55 resolvida** (Quebra de Caixa passou a *Correto*, e a listagem mostra R$ 0,00 com check), **Conf. Saldo Final atualizado** de R$ 1.909,43 para R$ 1.911,98 e o caixa ganhou o **cadeado**, com a conferência travada. 9 imagens. **Descobertas:** a tela mantém a 1ª conferência numa coluna própria e um total **Quebra 1ª Conf.** (o histórico não é apagado); no envio, a API **inverte** os campos (1ª vai para `conferencia*2`); e o `tipo: CONFERIR` **regrava a Data/Hora Fechamento** (10:18 → 10:54). **Técnica usada:** todo o fluxo foi ensaiado sem clicar em *Conferir* (nada grava até a confirmação) e só depois executado de verdade. Aguardando publicação do dono.
