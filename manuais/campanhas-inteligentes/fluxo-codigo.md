# fluxo-codigo.md — Campanhas Inteligentes

Mapeamento técnico da funcionalidade, no front (`beefood-web-react`) e no backend
(`beetech-server-node-2.0`, branch `beefood-web-react`). Documento interno — **não publicar**.

Levantado em 20/08/2026, com o código das duas pontas e conferência ao vivo na conta
**BeeFood3 - Manual** (produção).

---

## 1. Visão geral

```
Food Marketing -> Campanhas WhatsApp -> aba "Campanhas Inteligentes"
   /food-marketing/campanhas-whatsapp?tab=automacao
        |
        +-- GET  /whatsapp2/automacao/automacoes/{empresaID}/{usuarioID}      lista os cards
        +-- GET  /whatsapp2/automacao/{empresaID}/{usuarioID}/{id}            abre uma campanha
        +-- POST /whatsapp2/automacao                                          cria
        +-- PUT  /whatsapp2/automacao                                          salva
        +-- POST /whatsapp2/automacao/ativar                                   liga
        +-- POST /whatsapp2/automacao/pausar                                   pausa
        +-- POST /whatsapp2/automacao/restaurarPadrao                          volta ao original
        +-- GET  /whatsapp2/automacao/modelos/{empresaID}/{usuarioID}          os 6 modelos
        +-- POST /whatsapp2/automacao/modelo/aplicar                           modelo -> rascunho
        +-- GET  /whatsapp2/automacao/variaveis/{empresaID}/{usuarioID}        catálogo de variáveis
        +-- GET  /whatsapp2/automacao/envios/{empresaID}/{usuarioID}/{id}      histórico de envios
        +-- GET  /relatorio2/pixelAutomacoes/{empresaID}/{ini}/{fim}?tz=-3     ROI (Pixel)
```

Prefixo real das chamadas: `/datasnap/rest/...` (`src/lib/api/whatsappAutomacao.ts`).
O ROI usa outro host, via `createReportApiUrl`.

**Não é um item de menu.** É a terceira aba da página de Campanhas WhatsApp
(`src/pages/FoodMarketingCampanhasWhatsApp.desktop.tsx`), ao lado de **Indicadores** e
**Campanhas**. Só existe no desktop.

---

## 2. Componentes do front

| Arquivo | Papel |
|---------|-------|
| `src/components/whatsapp/automacao/WhatsAppAutomacaoTab.tsx` | Casca da aba |
| `AutomacaoListaView.tsx` | Grade de cards, switch, menu de ações, diálogos de confirmação |
| `AutomacaoEditorModal.tsx` | Editor em 3 passos (Sheet lateral) |
| `NovaAutomacaoModal.tsx` | "Usar um modelo pronto" / "Criar do zero" + catálogo de modelos |
| `VariaveisModal.tsx` | Catálogo de variáveis, com busca, chips e cadeado |
| `SpintaxAjudaSecao.tsx` | Ajuda da variação automática, dentro do catálogo |
| `AlertaRiscoInboundDialog.tsx` | Alerta vermelho de risco de banimento |
| `AutomacaoAcompanhamentoView.tsx` | Botão **Resultado**: jornadas, envios e ROI |
| `AutomacaoHistoricoView.tsx` | Botão **Histórico**: tabela de envios + CSV |
| `GatilhoBadge.tsx` | Os três selos de gatilho |
| `MidiaUpload.tsx` | Anexo por variação (máx. 10MB) |
| `src/hooks/useWhatsAppAutomacoes.ts` | Lista, ativar, pausar, excluir, restaurar |
| `src/utils/automacaoVariaveisGrupos.ts` | Agrupa variáveis e marca as que dependem de histórico |

---

## 3. Permissão

| Camada | Identificador |
|--------|---------------|
| Chave no JSON de permissões | `campanhaInteligente` |
| Item do grupo de acesso | **itemID 167** |
| Formulário (contratação) | **formularioID 127** |
| Rota protegida | `submenuKey="foodMarketing"`, `submenuItemKey="campanhas-inteligentes"` |

**São os mesmos 167/127 das Campanhas WhatsApp** — comentário explícito em
`src/models/empresa/grupoAcesso.js` (linhas 195-201): *"Liberada para todos que usam campanha
de WhatsApp"*. Logo, quem vê a aba **Campanhas** também vê a aba **Campanhas Inteligentes**;
não existe permissão separada, apesar de as duas chaves JSON serem distintas.

Pré-requisito funcional: filiais com **`beeBotAdicional === true`** (o seletor de cardápio e o
campo **Cardápio** do editor só listam essas). Sem BeeBot, a aba de campanhas mostra
*"Configure as filiais no BeeBot para usar envios em massa."*

---

## 4. Os seis modelos padrão

Fonte: `src/models/automacao/modelos.js` (backend). São **6** modelos, e o seed cria todos em
qualquer empresa, marcados como `sistema: true` (selo **BeeFood** no card, não podem ser
excluídos — só restaurados).

`src/models/automacao/automacao.js`, `SEED_AUTOS` (linhas 216-221) define quais nascem ligadas:

| Ordem no seed | Chave | Nasce | Comentário do código |
|---|---|---|---|
| 1 | `carrinho` | **ativa** | por evento (Pixel) |
| 2 | `cardapio_sem_compra` | **ativa** | por evento (BeeBot) |
| 3 | `recuperacao` | **ativa** | público: Clientes sumidos |
| 4 | `cashback` | **ativa** | público: Cashback parado |
| 5 | `aniversario` | pausada | público: Aniversariantes do dia |
| 6 | `boas_vindas` | pausada | público: Clientes novos |

### Configuração de fábrica, por modelo

| Modelo (nome na tela) | Gatilho (`origemPublico`) | Público fixo | Horário | `janelaInboundDias` | `intervaloMinHorasGlobal` | `maxEnviosPorDia` | `atrasoDisparoMin` | `janelaEventoHoras` | Variações |
|---|---|---|---|---|---|---|---|---|---|
| **Recuperador de vendas** | SEGMENTACAO | `fixo-sumidos` | 10–21 | 120 | 2880 (120 d) | 2 | — | — | 5 |
| **Cashback parado** | SEGMENTACAO | `fixo-cashback` | 10–21 | 15 | 168 (7 d) | 5 | — | — | 4 |
| **Aniversário** | SEGMENTACAO | `fixo-aniversario` | 10–21 | 365 | 24 (1 d) | não definido | — | — | 4 |
| **Boas-vindas / 2ª compra** | SEGMENTACAO | `fixo-novos` | 10–21 | 30 | 8760 (365 d) | 5 | — | — | 5 |
| **Carrinho abandonado** | PIXEL_CARRINHO | — | 10–23 | 90 | 168 (7 d) | 7 | 15 | 3 | 9 |
| **Recebeu o cardápio e não pediu** | BEEBOT_SEM_COMPRA | — | 10–22 | 1 | 168 (7 d) | não definido | 15 | 24 | 9 |

`diasSemana` é `"0,1,2,3,4,5,6"` (todos) nos seis. `soQuemFalou` é `true` nos seis.
Onde `maxEnviosPorDia` não é definido, a tela exibe o próprio default do componente: **50**
(`a.maxEnviosPorDia ?? 50`, em `AutomacaoEditorModal.tsx`) — conferido na Aniversário do
sandbox, que mostra 50.

### Rótulos derivados do tipo (`AutomacaoListaView.tsx`)

| `tipo` | Descrição exibida no card |
|--------|---------------------------|
| RECUPERACAO | Traz de volta quem já comprou e sumiu |
| CASHBACK | Avisa quem tem cashback parado para usar |
| ANIVERSARIO | Parabeniza o cliente no dia dele |
| CARRINHO_ABANDONADO | Resgata quem montou a sacola e não finalizou |
| BEEBOT_SEM_COMPRA | Fala com quem recebeu o cardápio e não pediu |

Atenção: **Recebeu o cardápio e não pediu** tem `tipo: "RECUPERACAO"` no modelo, então herda a
descrição "Traz de volta quem já comprou e sumiu" — foi o que apareceu no card capturado. É
divergência do produto, não do manual.

### Selos de gatilho (`GatilhoBadge.tsx`)

| `origemPublico` | Selo |
|---|---|
| SEGMENTACAO | **Gatilho: Público de clientes** |
| PIXEL_CARRINHO | **Gatilho: Cardápio digital** |
| BEEBOT_SEM_COMPRA | **Gatilho: WhatsApp / BeeBot** |

---

## 5. Os três passos do editor

`STEPS` em `AutomacaoEditorModal.tsx` (linhas 87-91).

### Passo 1 — Identificação e público

| Campo | Detalhe |
|-------|---------|
| Nome (no cabeçalho) | `input` livre, placeholder **Nome do campanha inteligente** |
| **Cardápio** | Select; **Todos os cardápios** + filiais com `beeBotAdicional` |
| **Origem do público** | **Segmentação de clientes** / **Carrinho abandonado** / **Recebeu cardápio e não pediu** |
| **Segmentação** | Só quando origem = SEGMENTACAO |
| **Esperar antes de enviar (min)** | Só nos gatilhos por evento; default 15 |
| **Considerar eventos das últimas (h)** | Só nos gatilhos por evento; default 3; **desabilitado** em BEEBOT_SEM_COMPRA ("o controle é por pendência do dia") |

Com PIXEL_CARRINHO a tela monta a frase-resumo: *"Envia para quem abandonou entre {atraso} min
e {janela} h atrás."*

### Passo 2 — Mensagem (com variações)

Cada variação tem anexo (`MidiaUpload`, máx. 10MB), textarea, contador de caracteres e
**Prévia**. Botões: **+ Variação**, a tag obrigatória `{{meu_link}}`, **Inserir variável** e
lixeira (quando há mais de uma).

Avisos:
- Falta link: *"Inclua {{meu_link}} ou cole o link do seu cardápio digital (shop.beetech.com.br
  ou menu.beefood.com.br) para medir as vendas."*
- Variável de foto no texto: *"Esta variação será enviada como imagem + legenda com a foto do
  produto. Se o produto não tiver foto, envia só o texto."*
- Origem SEGMENTACAO: dica de que as variáveis de histórico funcionam melhor.
- Origem por evento: *"Neste gatilho não há histórico do cliente: só resolvem as variáveis
  globais."*

A **Prévia** (`aplicarExemplos`) troca as variáveis pelos exemplos do catálogo, mas **não
sorteia a variação automática** — o `{a|b}` continua visível na prévia. O sorteio acontece no
envio (confirmado no histórico do sandbox, item 8 abaixo).

### Passo 3 — Agenda e anti-spam

| Campo | Detalhe |
|-------|---------|
| Aviso fixo | *"As mensagens só são enviadas quando o cardápio digital estiver aberto para pedidos."* Dias e horários **apenas restringem** essa janela, nunca ampliam |
| **Dias da semana** | Botões D S T Q Q S S |
| **Horário de início / de fim** | `input type=time` |
| **Só enviar para quem já me mandou mensagem** | Switch + selo **Anti Banimento**; default ligado |
| **Considerar mensagens recebidas nos últimos (dias)** | Só com a proteção ligada; default 30 |
| **Intervalo mín. entre mensagens (dias)** | Grava em horas (`intervaloMinHorasGlobal = dias * 24`), mínimo 1 dia |
| **Ritmo: envios por dia (0 = sem limite)** | Default do componente: 50 |

---

## 6. Catálogo de variáveis

Fonte: `src/models/automacao/variaveis.js` (backend). **20 variáveis.** O front agrupa por
`src/utils/automacaoVariaveisGrupos.ts`:

| Grupo | Critério | Quantidade |
|-------|----------|-----------|
| **Básicas** | `meu_link`, `primeiro_nome`, `nome`, `saldo_cashback` | 4 |
| **Foto** | chave termina em `_foto` | 4 |
| **Produto & Promoção** | as demais | 12 |

`{{meu_link}}` é a **única obrigatória** (`obrigatoria: true`). Motivo técnico: o cérebro troca
a tag pelo link do cardápio e acrescenta `?a={automacaoID}`, que é o que permite atribuir a
venda à campanha no Pixel. Alternativa aceita: link direto de domínio conhecido
(`LINK_CARDAPIO_DOMINIOS` = `shop.beetech.com.br`, `menu.beefood.com.br`) — domínio próprio
não vale.

As **9 que dependem do histórico do cliente** (`DEPENDEM_HISTORICO`) aparecem com cadeado e
botão **Inserir** desabilitado quando a origem é PIXEL_CARRINHO ou BEEBOT_SEM_COMPRA, porque
nesses gatilhos não há `clienteID`:

`produto_preferido`, `produto_preferido_foto`, `setor_preferido`, `setor_preferido_foto`,
`ultimo_produto_comprado`, `dias_desde_ultima_compra`, `preco_produto_preferido`,
`produto_melhor_promocao_preferido`, `produto_melhor_promocao_preferido_foto`.

`{{saldo_cashback}}` tem regra própria: se a mensagem usa a tag, **só é enviada a quem tem
saldo maior que zero**.

Variação automática (Spintax): `{opção1|opção2|opção3}`, sorteada por envio, aninhável
(resolve de dentro para fora). Não misturar com `{{variáveis}}` — chaves duplas são variável,
chaves simples são sorteio.

---

## 7. O que grava e o que não grava

| Ação na tela | Grava? |
|---|---|
| Abrir a campanha e navegar pelos 3 passos | **Não** |
| Mexer em qualquer campo do editor | **Não** (estado local) |
| Abrir o catálogo de variáveis / a ajuda do Spintax | **Não** |
| Clicar no switch do card | **Não** — apenas abre o diálogo de confirmação |
| Confirmar **ATIVAR (ENTER)** / **PAUSAR (ENTER)** | **Sim** |
| **SALVAR (F2)** | **Sim** |
| **SALVAR (F2)** com o Anti Banimento desligado | **Não** na primeira vez: `handleSave` retorna antes da API e abre o `AlertaRiscoInboundDialog` (linhas 204-208) |
| **ATIVAR AUTOMAÇÃO** no editor | **Sim** (salva e ativa) |
| **Restaurar padrão** confirmado | **Sim** |

Não há auto-save em nenhum ponto do editor. Foi o que permitiu capturar todas as telas deste
manual sem alterar campanha alguma.

**Ativar não dispara em massa na hora.** O backend só faz `setStatus(..., "ATIVA")`; o envio
depende do gatilho (evento do Pixel, pendência do BeeBot ou varredura do público) e da agenda.

---

## 8. Estado do sandbox em 20/08/2026

Retorno de `GET /whatsapp2/automacao/automacoes/38311/88711`:

| id | Nome | Status | Envios | Pedidos | Receita |
|----|------|--------|--------|---------|---------|
| 35 | Carrinho abandonado | ATIVA | 1 | 1 | R$ 34,02 |
| 36 | Recebeu o cardápio e não pediu | ATIVA | 1 | 1 | R$ 3,89 |
| 37 | Recuperador de vendas | ATIVA | 0 | 0 | R$ 0,00 |
| 38 | Cashback parado | ATIVA | 0 | 0 | R$ 0,00 |
| 39 | Aniversário | RASCUNHO | 0 | 0 | R$ 0,00 |
| 40 | Boas-vindas / 2ª compra | PAUSADA | 0 | 0 | R$ 0,00 |

Duas observações que valem para qualquer conta:

**1. Instância antiga não recebe a melhoria do modelo.** A Carrinho abandonado do sandbox tem
as 9 variações com Spintax, iguais ao modelo atual. A Aniversário tem 4 variações **sem**
Spintax (`"Feliz aniversário, {{primeiro_nome}}! ..."`), enquanto o modelo no código traz
`"{Feliz aniversário|Parabéns pelo seu dia}, ..."`. Ou seja: a campanha foi criada por um seed
anterior e não é atualizada sozinha. Quem quiser os textos novos precisa de **Restaurar
padrão**.

**2. Parâmetro ajustado não volta ao padrão.** A Carrinho abandonado do sandbox está com
**Esperar antes de enviar = 5 min**, e não os 15 do modelo. A frase-resumo da tela acompanha:
*"Envia para quem abandonou entre 5 min e 3 h atrás."*

Envio real registrado no histórico da Carrinho abandonado (26/07/2026 17:37), útil como prova
de como a mensagem sai:

```
Olá Bruno! 🛒 O seu pedido está quase pronto. Conclua agora para não perder o que
você escolheu: https://menu.beefood.com.br/beefood3?a=35
```

O texto cadastrado é `{Olá|Oi}, {{primeiro_nome}}! 🛒 O seu pedido está {quase pronto|quase
completo}. {Conclua|Finalize} agora ...`. No envio, o Spintax foi sorteado, `{{primeiro_nome}}`
virou "Bruno" e `{{meu_link}}` virou o link do cardápio **com `?a=35`** — o id da campanha,
que é como o Pixel atribui a venda. Situação **Enviado**, **Converteu? Sim**.

---

## 9. Divergências e pontos de atenção

1. **"Campanhas Inteligentes" não tem permissão própria** — usa itemID 167 / form 127 das
   Campanhas WhatsApp, apesar da chave JSON separada.
2. **Concordância dos textos da tela**: "Nossos campanhas inteligentes", "Novo campanha
   inteligente", "Nenhum campanha inteligente ainda", "Campanha inteligente salvo". O manual
   escreve em português correto e não reproduz o erro, exceto quando cita um botão literal.
3. **Descrição do card da campanha do BeeBot** sai como "Traz de volta quem já comprou e sumiu"
   por causa do `tipo: RECUPERACAO` — não descreve o que a campanha faz.
4. **Mobile não tem a aba.** Nenhum equivalente em `src/components/mobile`.
5. O card mostra receita e conversão do período todo, sem filtro; o filtro de data existe só
   dentro de **Resultado** (ROI) e **Histórico**.
