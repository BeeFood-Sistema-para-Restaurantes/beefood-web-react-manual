# ✅ Checklist de Manuais — BeeFood

> Controle central de **ideias de manuais**, o que já foi **executado** e o que já foi **publicado**.
> Regras: o **dono publica** e avisa → só então marcamos a coluna **Publicado**.
> Cada manual concluído fica em `manuais/<nome>/`.

Última atualização: 2026-08-20 (#24 Modo Kiosk com o texto pronto; faltam só as 21 imagens)

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
| 5 | **Reforma Tributária (IBS/CBS)** | Os 6 campos novos, como editá-los na Edição Fiscal e como aparecem na nota (exemplo fake) | `manuais/reforma-tributaria-ibscbs/` | ✅ Concluído | 🌐 Sim |
| 6 | **Ativação Aiqfome V2** | Conectar a loja do Aiqfome ao BeeFood (Store ID → cadastro em Aplicativos → autorização ID Magalu) | `manuais/ativacao-aiqfome/` | ✅ Concluído | 🌐 Sim |
| 7 | **Integração Machine** | Despachar entregas pela central Machine: credenciais, config em Aplicativos → Entrega, despacho (manual/auto), acompanhamento e cancelamento | `manuais/integracao-machine/` | ✅ Concluído | 🌐 Sim |
| 8 | **Integração 99 Entrega** | Solicitar **boleto** (único pagamento) + **ambiente de produção** e credenciais (Modo de desenvolvedor) na 99, cadastrar webhook, conectar em Aplicativos → Entregas, despachar com cotação, acompanhar e cancelar | `manuais/integracao-99-entrega/` | ✅ Concluído | 🌐 Sim |
| 9 | **Integração Repediu** | Gerar Client ID/Secret (Repediu → Integrações) e Write Key (Repediu → Web/App Analytics), preencher em Aplicativos → Marketing e CRM → Repediu → Configurar e salvar (Tracker de Vendas + Cardápio Digital) | `manuais/integracao-repediu/` | ✅ Concluído | 🌐 Sim |
| 10 | **Integração FoodCRM** | Gerar a API Key/Token (FoodCRM → Integrações → Acessar a documentação) e cadastrar por cardápio em Aplicativos → Marketing e CRM → FoodCRM (envio automático das vendas diariamente de madrugada) | `manuais/integracao-foodcrm/` | ✅ Concluído | 🌐 Sim |
| 11 | **Integração Uber Direct** | Criar conta Uber + Uber Direct, cadastrar cartão e webhook, copiar a Chave de autenticação do webhook + credenciais (ID do usuário/ID de cliente/Client Secret), colar em Aplicativos → Entregas → Uber Direct e usar no dia a dia (despachar pedido, acompanhar e cancelar) | `manuais/integracao-uber-direct/` | ✅ Concluído | 🌐 Sim |
| 12 | **Segunda conferência (dupla checagem)** | Por que recontar, abrir a conferência de um caixa fechado (Ver Conferência), Adicionar 2ª Conferência, recontar com a calculadora, observações, marcar como conferido (cadeado) e resolver a quebra de caixa | `manuais/caixa-conferencia-2/` | ✅ Concluído | 🌐 Sim |
| 13 | **Restrições de caixa (grupo de acesso)** | Todas as restrições de caixa que podem ser aplicadas a um usuário — Abrir e Fechar Caixa, Visualizar Valores de Referência, Visualizar Caixas Fechados, Transferência de Operações, Cadastro de Caixas, Função Gerente e o parâmetro Caixa por Usuário — cada uma com **como configurar** e **como o caixa fica** | `manuais/caixa-restricoes/` | ✅ Concluído | 🌐 Sim |
| 14 | **Segmentação de clientes** | Criar públicos em Food Marketing → Segmentação de Cliente: o que é, os 37 filtros disponíveis, como combinar com E/OU, testar o tamanho do público e usar em campanhas — com vários exemplos prontos de restaurante | `manuais/segmentacao-clientes/` | ✅ Concluído | 🌐 Sim |
| 15 | **Campanhas de WhatsApp** | Criar campanha em massa: escrever a mensagem com variações (reduz risco de bloqueio), anexar mídia, montar a lista de destinatários pelos cinco caminhos (avulso, RFV, filtro avançado, segmentação, Excel), revisar e publicar — mais abortar campanha e ler o resultado | `manuais/campanhas-whatsapp/` | ☑️ Aprovado | — |
| 16 | **Campanhas Inteligentes** | As seis automações que disparam sozinhas (recuperador de vendas, cashback parado, aniversário, boas-vindas, carrinho abandonado, recebeu o cardápio e não pediu), o público de cada uma, agenda, ritmo de envio e a proteção **Anti Banimento** | `manuais/campanhas-inteligentes/` | ☑️ Aprovado | — |
| 17 | **BeeFood Pixel Analytics** | Ler o funil do cardápio digital (Visitas → Visualizações → Carrinho → Pedidos), filtrar por contexto, cardápio e origem, entender os KPIs e o painel Ao vivo | `manuais/pixel-analytics/` | ☑️ Aprovado | — |
| 18 | **Campanhas SMS** | Criar campanha de SMS, entender a contagem de créditos por segmento (e como economizar sem acento/emoji), comprar créditos por PIX e usar a blacklist / opt-out | `manuais/campanhas-sms/` | ☑️ Aprovado | — |
| 19 | **Cashback — configurar o programa** | Ativar o cashback, validade do saldo, saldo mínimo para resgate, percentual fixo ou por dia da semana, em quais canais o cliente ganha e as exceções de produto | `manuais/cashback-configurar/` | ☑️ Aprovado | — |
| 20 | **Cashback — operar no dia a dia** | Histórico, saldo por cliente, ajuste manual de saldo (creditar e debitar com motivo), fila de processamento e como o operador aplica o cashback no PDV e nas Mesas | `manuais/cashback-operar/` | ☑️ Aprovado | — |
| 21 | **Cupons de desconto** | Criar cupom nos quatro tipos (percentual, valor fixo, frete grátis e produto grátis), validade, dias da semana, canais, valor mínimo, limites de uso, link do cupom e histórico | `manuais/cupom-desconto/` | ☑️ Aprovado | — |
| 22 | **Painel Fidelidade** | Ler o resultado dos programas: desconto concedido, faturamento influenciado, ROI, cupom × cashback, participação no faturamento e aquisição × recorrência | `manuais/fidelidade-painel/` | ☑️ Aprovado | — |
| 23 | **Avaliações** | Está no menu Fidelidade (CRM), mas é reputação: nota geral, avaliações por período, por canal e como responder | `manuais/avaliacoes/` | ☑️ Aprovado | — |
| 24 | **Modo Kiosk (Cardápio Digital Tablet)** | **Só no tablet:** travar o aparelho no cardápio pela tela de Administração do app Android — abrir a Administração pelo logo, conceder as permissões de Acessibilidade e Launcher padrão pelo assistente, **ATIVAR MODO KIOSK**, testar, destravar, mais a alternativa de trava básica e o FAQ | `manuais/cardapio-digital-tablet-modo-kiosk/` | 🔨 Texto pronto (**faltam as 21 imagens**) | — |

---

## 💡 Backlog de ideias (aguardando aprovação)

> Ideias propostas. Quando o dono aprovar, sobem para a tabela acima com um número.

> **Food Marketing e Fidelidade (CRM) saíram do backlog** em 19/08/2026: viraram os itens
> **#15 a #23** na tabela acima. O que o sandbox já oferece para documentá-los está registrado
> na seção *Estado do sandbox*, mais abaixo.
>
> **API Oficial WhatsApp** fica de fora por enquanto: o item do menu está como *Em breve!* e não
> tem tela implementada.

### Outras áreas (levantamento de 19/08/2026)

> Inventário completo do sistema. A nota é "quanto o usuário final precisa de um manual disso".

| Ideia | Escopo resumido | Tamanho | Nota | Status |
|-------|-----------------|---------|------|--------|
| **Delivery** | Operar pedidos: colunas de situação, aceitar, despachar, entregador, pagamentos, cancelamento — e o **Aceite Automático** | 3 a 4 manuais | 5 | 💡 Ideia |
| **PDV** | Venda no balcão: carrinho, cliente, balança, desconto com senha de gerente, pagamento, reabrir e agrupar vendas | 3 a 4 manuais | 5 | 💡 Ideia |
| **Cardápio** | Produtos, grupos de opções e complementos — o modal do produto tem 6 abas; mais Exibir/Ocultar, Rodízio e importar do iFood | 4 a 5 manuais | 5 | 💡 Ideia |
| **Cardápio Digital** | Configurar a loja online na ordem certa: horário, área de entrega, formas de recebimento, pagamento online, pausa programada e avisos (11 abas) | 3 a 4 manuais | 5 | 💡 Ideia |
| **Fiscal** | Configuração fiscal, emissão e consulta de NFC-e e NF-e, inutilização, carta de correção e notas recebidas (a Reforma Tributária já é o #5) | 4 a 5 manuais | 5 | 💡 Ideia |
| **Mesas / Comandas** | Mapa do salão, abrir e fechar conta, agrupar mesas, reabrir | 2 manuais | 4 | 💡 Ideia |
| **Impressão** | Impressoras, impressão da cozinha, layout e os dois históricos | 2 a 3 manuais | 4 | 💡 Ideia |
| **WhatsApp / BeeBot** | Conectar o número, notificações automáticas de status, respostas automáticas, IA e resumo diário | 3 manuais | 4 | 💡 Ideia |
| **Usuários e permissões** | Criar usuário, montar grupo de acesso e o que cada permissão faz (complementa o #13, que só cobre caixa) | 1 a 2 manuais | 4 | 💡 Ideia |
| **Estoque** | Saldo e movimentações, importar NF-e de compra, receitas e ordens de produção | 3 manuais | 4 | 💡 Ideia |
| **Histórico de Vendas** | Consultar venda passada, filtros, detalhe, pagamentos e exportação | 1 manual | 4 | 💡 Ideia |
| **Totem / autoatendimento** | Contratar, configurar (5 abas) e a pesagem automática do self-service | 2 a 3 manuais | 4 | 💡 Ideia |
| **Clientes** | Cadastro, importação por Excel, duplicados e o que é a classificação RFV | 1 a 2 manuais | 3 | 💡 Ideia |
| **Financeiro** | Lançamentos a pagar e receber, recebimentos, pagamentos, DRE e cadastros auxiliares | 3 a 4 manuais | 3 | 💡 Ideia |
| **Fiado** | Visão geral, controle de dívidas e vendas sem pagamento | 1 manual | 3 | 💡 Ideia |
| **Cadastros** | Mesas e comandas (com QR Code), formas de recebimento e funcionários | 2 manuais | 3 | 💡 Ideia |
| **Cardápio no Tablet** | Cadastrar tablets, layout e eventos remotos | 2 manuais | 3 | 💡 Ideia — o modo kiosk saiu daqui e virou o **#24** |
| **Multilojas** | Link único listando várias lojas da rede | 1 manual | 3 | 💡 Ideia |
| **Pix Online** | Contratar, configurar e acompanhar o extrato | 1 manual | 3 | 💡 Ideia |
| **Início (Home)** | Ler o painel inicial, filtros e a senha que revela os valores | 1 manual | 2 | 💡 Ideia |

### Estado do sandbox (o que já dá para documentar)

Conferido em 19/08/2026 na conta **BeeFood3 - Manual**. Importa porque decide se um manual pode
ser produzido com dados reais ou se precisa de cenário montado antes.

| Área | O que já existe |
|------|-----------------|
| Cashback | Programa **ativado**, com histórico real e **6 usos** registrados |
| Cupons | **6 cupons** cadastrados (1 ativo) e **12 usos** |
| Painel Fidelidade | **18 vendas** com fidelidade, **R$ 66,95** de desconto concedido |
| Avaliações | 2 avaliações, nota geral **5,0** |
| Campanhas SMS | **100 créditos** de saldo e 1 campanha em rascunho |
| Campanhas WhatsApp | BeeBot conectado; campanhas antigas em rascunho |
| Pixel Analytics | Funcionando, com dados a partir de **junho/2026** |
| Clientes | 18 clientes classificados por RFV |
| Estoque | 45 produtos (nenhum com controle de estoque ligado) |
| Fiado | R$ 14,00 em dívidas, 3 clientes |

**Decisão pendente com o dono:** nos manuais **#15** e **#16**, publicar uma campanha ou ativar
uma automação **dispara mensagem de verdade** para os clientes da conta. Todo o caminho pode ser
capturado em rascunho; falta definir se um disparo real fica autorizado para a captura final.
No **#18**, enviar SMS consome os 100 créditos.

### Caixa (backlog antigo)

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

- 2026-08-20 — **#24 com o texto pronto; faltam as 21 imagens.** O `manual-modo-kiosk.md` do dono (origem: `c:\projetos\beetech-appgarcom-android\docs\`) chegou como arquivo e foi **copiado sem reescrever**, no mesmo padrão dos manuais #8 e #11 — as únicas mudanças foram os caminhos `images/kiosk/` → `imagens-tratadas/` e o fim de linha CRLF → LF. **Escopo corrigido:** o manual é **só do aplicativo Android no tablet** (Administração → Configurar Trava Avançada → as duas permissões → ATIVAR MODO KIOSK), e não do painel web como eu havia entendido na primeira rodada. `texto-documentation.ia.md` já escrito, com as 21 imagens na ordem. Falta apenas subir os PNG: eles vieram como imagem no chat, não como arquivo em disco. **Descobertas:** existem **três travas diferentes** e é fácil confundi-las (modo kiosk do app, trava básica por screen pinning e o evento `TRAVAR` do painel, que só bloqueia o botão *voltar*) — a tabela que as separa está no `fluxo-codigo.md`; e o repositório do app, `beetech-appgarcom-android`, **não é alcançável** por este ambiente.
- 2026-08-20 — **#24 iniciado e bloqueado.** Pedido: manual do **modo kiosk** do Cardápio Digital Tablet, a partir de um `manual-modo-kiosk.md` e de uma pasta `images` anexados ao chat. **Os anexos não chegaram ao VM do Cloud Agent** — procurados no repositório (inclusive todo o histórico e todas as branches), nos dois repositórios de referência, nas 81 branches do backend no Bitbucket e no sistema de arquivos inteiro. Entregue mesmo assim: o `fluxo-codigo.md` completo (rota, permissão, as três abas, regras de status/bateria, limite contratado que desloga tablet sozinho, os seis eventos, o POST `/api/tablet2/criarEvento` e o `procInsertEvento`) e um **rascunho** do manual com as etapas 1 a 6 (tudo feito pelo painel). Ficou pendente a etapa 7 (travar o próprio Android) e as 5 imagens — não escrevi o procedimento do Android por conta própria para não divergir do oficial. **Descoberta importante:** *Kiosk* aparece em dois lugares distintos do produto, e o do `TotemConfigModal.tsx` é o **Totem Windows**, não o tablet.
- 2026-08-19 — **Todos os 12 manuais concluídos marcados como publicados** (aviso do dono). Continuam apenas aprovados, sem produção, o #3 (Reabrir caixa) e o #4 (Transferência entre caixas). **Food Marketing e Fidelidade saíram do backlog e viraram os itens #15 a #23**, na ordem de prioridade pedida pelo dono (Food Marketing primeiro). O levantamento das demais 20 áreas do sistema fica no backlog, com tamanho estimado e nota de necessidade. Registrado também o **estado do sandbox** por área — o que decide se um manual pode ser produzido com dados reais. **Pendente:** definir se um disparo real de campanha (#15/#16) e um envio de SMS (#18) ficam autorizados para as capturas finais.
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
