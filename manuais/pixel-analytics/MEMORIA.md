# MEMORIA.md — #17 BeeFood Pixel Analytics

Manual de **leitura** do painel, agora com a seção de **campanha paga**
(Origem + UTM). Não configura nada.

Última atualização: 02/09/2026.

---

## 1. O pedido

Checklist item **#17**, aprovado: *Ler o funil do cardápio digital (Visitas →
Visualizações → Carrinho → Pedidos), filtrar por contexto, cardápio e origem,
entender os KPIs e o painel Ao vivo.*

Pedido extra (mesma pasta): estudar como analisar campanhas pagas com os
filtros; gerar URLs fake de anúncio de todas as plataformas no cardápio;
fechar pedidos para gerar conversão; e atualizar o manual.

Pasta: `manuais/pixel-analytics/`.

Não misturar com Pixel da Meta (#49/#50). O BeeFood Pixel é o analytics
próprio, ligado desde junho/2026, sem Pixel ID.

---

## 2. Escopo do texto

Cabe no manual:

1. O que é e onde fica
2. Filtros (período, contexto, cardápio, origem)
3. Funil — as 6 etapas, os dois modos, como ler a %
4. KPIs (receita, ticket, conversão)
5. Ao vivo
6. Segmentação por origem
7. **Campanha paga:** montar UTM, filtro Origem, Campanhas que mais vendem,
   UTM Source × Medium
8. O resto da página em bloco curto
9. Modal **Saiba como funciona**

Fora: configurar rastreamento (não existe tela), Meta Pixel, ROI das
campanhas inteligentes / WhatsApp.

---

## 3. Plano de imagens

| # | Arquivo | Tipo | Conteúdo |
|---|---------|------|----------|
| 1 | `01-menu-food-marketing.png` | setas | Menu Food Marketing → BeeFood Pixel Analytics |
| 2 | `02-filtros-topo.png` | setas | Período, contexto, origem, Excel, ajuda |
| 3 | `03-funil-colunas.png` | setas | Funil no modo Colunas (228 → 8) |
| 4 | `04-funil-classico.png` | contexto | Mesmo funil no modo Funil |
| 5 | `05-kpis-resumo.png` | setas | Receita R$ 281,52 / ticket R$ 35,19 / 4% |
| 6 | `06-ao-vivo.png` | setas | Painel ao vivo (Kwai, YouTube, pedido) |
| 7 | `07-como-funciona.png` | contexto | Modal de ajuda |
| 8 | `08-segmentacao.png` | setas | Top Origens com linha Google |
| 9 | `09-campanhas-vendem.png` | setas | UTM Campaign (manual-meta-feed, …) |
| 10 | `10-utm-source-medium.png` | setas | google · cpc, facebook · paid, instagram · paid |
| 11 | `11-origem-google.png` | setas | Origem = Google (12 visitas → 1 pedido, 8%) |

---

## 4. Regras de captura

- Conta **BeeFood3 - Manual** (`contato@beefood.com.br`).
- Tema claro. Widget flutuante escondido. Banner/NPS fechados.
- Spinner some + 5 s antes de cada print.
- Viewport admin 1440×900, DPR 1.5. Cardápio público: 390×844, DPR 2.
- Telefone de teste do checkout: `15999998888` — **não** entra em imagem
  publicada.

---

## 5. URLs fake e pedidos (02/09/2026)

Script: `pedido_anuncio.py`. Cada campanha = contexto Playwright novo.
Combo **One Burger + Batata frita + Coca 350ml**. Retirada + Dinheiro
(NÃO QUERO TROCO). Loja aberta até 23:59.

Checkout real do cardápio (Vue):

1. Home → combo → rádio das opções (clique no radio à direita, não no texto)
2. Adicionar → **Ver sacola** → **Continuar** (botão do rodapé)
3. `input[type=tel]` **dentro do diálogo** (o `input.first` é readonly da home)
4. Continuar → **Retirar no estabelecimento** → Continuar
5. **Outras formas de pagamento** → **Dinheiro** → **NÃO QUERO TROCO**
6. **Finalizar** → “Pedido enviado para o restaurante”

Pedidos gerados:

| Campanha | UTM | Resultado |
|----------|-----|-----------|
| google-ads | `utm_source=google&utm_medium=cpc&utm_campaign=manual-google-ads` + gclid | Pedido nº3 (933), R$ 32,05 |
| facebook-ads | `facebook / paid / manual-meta-feed` + fbclid | Pedido nº4 (934), R$ 37,05 |
| instagram-ads | `instagram / paid / manual-ig-stories` | Pedido nº5 (935), R$ 37,05 |
| tiktok-ads | `tiktok / paid / manual-tt-video` | Pedido nº6 (936), R$ 37,05 |
| youtube-ads | `youtube / cpc / manual-yt-instream` | parou no carrinho |
| kwai-ads | `kwai / paid / manual-kwai-clip` | parou no carrinho |

Houve também visitas de debug (`debug-tel`, `debug-ck2`, `debug-pag`) com
`utm_source=google` — por isso Origem Google ficou com **12 visitas / 1
pedido**. Não documentar esses nomes no `.md` do usuário.

O backend classifica a **Origem** pelo `utm_source` (Google, Instagram,
TikTok, YouTube, Kwai), mesmo quando o HTTP referrer é vazio (`direto`
no `localStorage.beefood_pixel_attrib`).

---

## 6. Diagnóstico do sandbox (02/09/2026, depois dos pedidos)

Empresa **38311**, filial **39202**. Últimos 7 dias, Delivery, todas as
origens:

| Etapa | Sessões | % |
|-------|--------:|--:|
| Visitas | 227–228 | 100% |
| Visualizações | 79 | 35% |
| Carrinho | 42 | 18–19% |
| Finalização | 39 | 17% |
| Pagamento | 29 | 13% |
| Pedidos | 8 | 4% |

Receita **R$ 281,52**, ticket **R$ 35,19**.

Origem Google isolada: **12 → 11 → 8 → 6 → 3 → 1 (8%)**, R$ 32,05.

Segmentação `utmCampaign` (API): `manual-google-ads` 6/1/R$32,05;
`manual-meta-feed` 1/1/R$37,05; `manual-ig-stories` 1/1/R$37,05;
`manual-tt-video` 1/1/R$37,05. YouTube/Kwai só visita+carrinho.

Ao vivo mostrou Kwai (carrinho), YouTube (carrinho) e PURCHASE Instagram.

---

## 7. Estado

- [x] Código do front lido
- [x] Diagnóstico da API no sandbox
- [x] URLs fake + 4 pedidos + 2 carrinhos
- [x] Recaptura (funil, KPIs, ao vivo, origens, campanhas, UTM, Google)
- [x] Anotação
- [x] Manual do usuário com seção de campanha paga
- [x] `texto-documentation.ia.md`
- [x] `validar-imagens.py` (11 imagens, 0 faltando, 0 órfãos)
