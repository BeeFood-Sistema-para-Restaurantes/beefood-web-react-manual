# fluxo-codigo.md — #17 BeeFood Pixel Analytics (uso interno, NÃO publicar)

Mapeamento técnico a partir do `beefood-web-react`. Backend não estava clonado nesta
sessão (`BITBUCKET_TOKEN` inválido). As regras de persistência dos eventos (definição
exata de sessão, classificação de referrer, captura de UTM no cardápio público) ficam
no servidor de relatórios; o que o usuário vê é calculado no front.

---

## O que é

Painel de leitura do tráfego dos cardápios BeeFood. **Não é** o Pixel da Meta (#49/#50)
nem Google Analytics. Não tem cadastro, switch nem auto-save: só consulta.

Acesso: **Food Marketing → BeeFood Pixel Analytics** (`/food-marketing/pixel-analytics`).
Atalho em Aplicativos: card **BeeFood Pixel** (`appCategories.ts`). Permissão:
`beefoodPixelAnalytics` (grupo Food Marketing).

---

## Telas

| Arquivo | Papel |
|---------|--------|
| `src/pages/FoodMarketingPixelAnalytics.tsx` | Desktop × mobile |
| `src/pages/FoodMarketingPixelAnalytics.desktop.tsx` | Página desktop |
| `src/components/mobile/food-marketing/pixel-analytics/MobilePixelAnalyticsPage.tsx` | Mesmos painéis, layout estreito |
| `src/components/food-marketing/pixel-analytics/*` | Filtros, funil, KPIs, tempos, engajamento, gráficos, tabelas, ao vivo, modal de ajuda |

---

## APIs

Base: `createReportApiUrl` → `https://app3.beetechapi.be` (front troca `/datasnap/rest/` por `/api/`).

| Rota | Quando |
|------|--------|
| `GET /api/relatorio2/pixelAnalytics/{empresaID}/{ini}/{fim}?tz=` | Carga da página e ao mudar o período. Devolve 7 blocos |
| `GET /api/relatorio2/pixelSegmentacao/{empresaID}/{ini}/{fim}/{grupo1}[/{grupo2}]?contexto=&filialID=&referrer=&tz=` | Tabela/teia de segmentação (sob demanda) |
| `GET /api/relatorio2/pixelAoVivo/{empresaID}/{ultimoEventoID}[/{filialID}]` | Poll a cada 5 s |

`tz` vem de `getBrowserTz()`. Filtros de contexto / cardápio / origem **não** vão no
`pixelAnalytics`: o front recorta em memória (`recorte` em `pixelAnalyticsFilters.ts`).
Só a segmentação e o ao vivo (filial) respeitam filtro no servidor.

### Payload de `pixelAnalytics`

```
funil[], tempos[], visitantesDia[], dispositivos[], cupomCashback[], produtos[], evolucaoDia[]
```

Cada linha carrega `filialID`, `contexto`, `referrer` para o recorte.

---

## Funil

Contagem **por sessão** (1 por etapa, se a sessão chegou lá):

| Card | Campo | Evento ao vivo |
|------|-------|----------------|
| Visitas | `sessoes` | `PAGEVIEW` |
| Visualizações | `visualizaram` | `VIEW_PRODUTO` |
| Carrinho | `sacola` | `ADD_CART` |
| Iniciou finalização | `checkout` | `INITIATE_CHECKOUT` |
| Iniciou pagamento | `pagamento` | `ADD_PAYMENT` |
| Pedidos | `pedidos` | `PURCHASE` |

`calcularFunil`: cada % é `etapa / visitas`. Receita e ticket médio vêm de `receita` /
`pedidos`. Conversão geral = `pedidos / visitas`.

Contexto **presencial** esconde o card **Iniciou pagamento** (QR Code / mesa não passa
por essa etapa).

Dois modos (`localStorage` `pixel-analytics:modo-funil`):

- **Colunas** (padrão): 6 cards com polígono e % na base.
- **Funil**: trapézios empilhados + perda % à direita (`−N%` vs etapa anterior).

---

## Filtros do topo

Estado inicial: `contexto=delivery`, `filialID=todos`, `referrer=todas`.

| Controle | Valores |
|----------|---------|
| Período | DateRangePicker. Mínimo **01/06/2026** (`DATA_MIN_PIXEL`). Padrão: últimos 7 dias (ou desde 01/06 se o intervalo cair antes) |
| Atualizar | Recarrega o período aplicado |
| Contexto | todos / delivery / presencial / totem / tablet (só os que existem nos dados + delivery sempre) |
| Cardápio | Só aparece se houver mais de uma filial **com dado** no período |
| Origem | Combobox das origens distintas do funil; vazio → `direto` |
| Exportar Excel | `pixelAnalyticsExport.ts` — abas do recorte + segmentações |
| Saiba como funciona | `ComoFuncionaModal` (texto estático, sem API) |

Trocar a data já dispara o fetch (não precisa clicar em Atualizar). Trocar contexto /
cardápio / origem **não** refetch: só recorta.

---

## Comparativo

Depois do período atual, o front busca o intervalo imediatamente anterior, de mesma
duração (`calcularPeriodoAnterior`). Badge verde/vermelho em quase todos os painéis.
Em tempos, `inverter=true` (menos tempo = melhor).

---

## Ao vivo

`usePixelAoVivo`: poll 5 s, pausa com aba oculta, cap 200 eventos. Primeiro tick não
dispara toast nem foguete. `PURCHASE` chama `celebrarNovoPedido()`. Eventos mapeados
no funil incrementam `eventoTicks` e o card pulsa. Refresh silencioso do painel com
throttle de 6 s.

Tipos do feed (rótulo na tela):

| Tipo | Rótulo |
|------|--------|
| PAGEVIEW | Novo acesso |
| VIEW_PRODUTO | Nova visualização |
| ADD_CART | Novo carrinho |
| INITIATE_CHECKOUT | Iniciou finalização |
| ADD_PAYMENT | Selecionou pagamento |
| PURCHASE | Novo pedido |
| REMOVE_CART | Removeu do carrinho |
| ADD_SHIPPING | Adicionou entrega |
| COUPON_APPLIED | Aplicou cupom |

Filtro do painel expandido: Todos / Pedidos / Carrinhos / Visualizações.

---

## Outros painéis (mesmo recorte)

| Painel | Fonte | Conta |
|--------|-------|-------|
| Análise de tempo | `tempos` | média ponderada (soma / qtd) entre etapas |
| Engajamento | `funil` | volumes **com repetição**: `totalViews`, `totalAddCarrinho`, `totalDistintos`, duração média |
| Análise de visitantes | `visitantesDia` | novos × recorrentes; mesmo visitante pode voltar em outro dia |
| Evolução | `evolucaoDia` | sessões, sacola, pedidos, receita por dia |
| KPIs | funil calculado | Receita total, Ticket médio, Conversão geral |
| Setores / Produtos | `produtos` | 1 por sessão (hint da tela). Taxa sacola e conversão sobre visitas do produto |
| Cupom & Cashback | `cupomCashback` | sessões com cupom/cashback, desconto e valor |
| Dispositivos | `dispositivos` | PC / celular / tablet e Android / iOS |
| Segmentação | API à parte | 11 dimensões: origem, contexto, cardápio, navegador, dia, hora, tipo, 5 UTMs. Tabela ou teia (Sankey). Presets prontos |

---

## O que este manual NÃO cobre

- Pixel da Meta + API de Conversões (#49) e Pixel da Meta somente (#50).
- ROI das campanhas inteligentes (`pixelAutomacoes`) e conversões do WhatsApp
  (`pixelWhatsapp`) — moram em Campanhas WhatsApp → Indicadores.
- Como o cardápio público emite o evento (repo do menu Vue, sem clone nesta sessão).
