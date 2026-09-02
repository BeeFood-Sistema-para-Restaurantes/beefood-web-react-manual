# MEMORIA.md — #17 BeeFood Pixel Analytics

Manual de **leitura** do painel. Não configura nada.

Última atualização: 02/09/2026.

---

## 1. O pedido

Checklist item **#17**, aprovado: *Ler o funil do cardápio digital (Visitas →
Visualizações → Carrinho → Pedidos), filtrar por contexto, cardápio e origem,
entender os KPIs e o painel Ao vivo.*

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
6. O resto da página em bloco curto (tempos, engajamento, visitantes, produtos,
   setores, cupom/cashback, dispositivos, segmentação, Excel)
7. Modal **Saiba como funciona**

Fora: configurar rastreamento (não existe tela), Meta, Google, ROI de campanha
WhatsApp.

---

## 3. Plano de imagens

Poucas, só o essencial. Live feed escondido nos prints do painel (senão cobre
o canto). Expandido só no print do ao vivo.

| # | Arquivo | Tipo | Conteúdo |
|---|---------|------|----------|
| 1 | `01-menu-food-marketing.png` | setas | Menu Food Marketing → BeeFood Pixel Analytics |
| 2 | `02-filtros-topo.png` | setas | Período, contexto, origem, Excel, ajuda |
| 3 | `03-funil-colunas.png` | setas | Funil no modo Colunas |
| 4 | `04-funil-classico.png` | contexto | Mesmo funil no modo Funil |
| 5 | `05-kpis-resumo.png` | setas | Receita, ticket, conversão |
| 6 | `06-ao-vivo.png` | setas | Painel ao vivo aberto |
| 7 | `07-como-funciona.png` | contexto | Modal de ajuda |
| 8 | `08-segmentacao.png` | contexto | Tabela de origens (prova de que o recorte existe) |

Período da captura: o que o sandbox tiver com número visível — diagnosticar
pela API antes. Filtro padrão da tela é **Delivery**.

---

## 4. Regras de captura

- Conta **BeeFood3 - Manual** (`contato@beefood.com.br`).
- Tema claro. Widget flutuante escondido. Banner/NPS fechados.
- Spinner some + 5 s antes de cada print.
- Repositório público: se o ao vivo mostrar telefone/nome de cliente, cobrir
  na pura.
- Viewport 1440×900, DPR 1.5.

---

## 5. Estado

- [x] Código do front lido
- [ ] Diagnóstico da API no sandbox
- [ ] Capturas
- [ ] Anotação
- [ ] Manual do usuário
- [ ] `texto-documentation.ia.md`
- [ ] `validar-imagens.py`
