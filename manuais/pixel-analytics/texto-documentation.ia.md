# texto-documentation.ia.md — #17 BeeFood Pixel Analytics

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Food Marketing**, adicione um manual por último chamado
**"BeeFood Pixel Analytics"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/pixel-analytics/pixel-analytics.md`

2. **Imagens (use estas 11, nesta ordem):**
   - `beefood-web-react-manual/manuais/pixel-analytics/imagens-tratadas/01-menu-food-marketing.png`
   - `beefood-web-react-manual/manuais/pixel-analytics/imagens-tratadas/02-filtros-topo.png`
   - `beefood-web-react-manual/manuais/pixel-analytics/imagens-tratadas/03-funil-colunas.png`
   - `beefood-web-react-manual/manuais/pixel-analytics/imagens-tratadas/04-funil-classico.png`
   - `beefood-web-react-manual/manuais/pixel-analytics/imagens-tratadas/05-kpis-resumo.png`
   - `beefood-web-react-manual/manuais/pixel-analytics/imagens-tratadas/06-ao-vivo.png`
   - `beefood-web-react-manual/manuais/pixel-analytics/imagens-tratadas/08-segmentacao.png`
   - `beefood-web-react-manual/manuais/pixel-analytics/imagens-tratadas/11-origem-google.png`
   - `beefood-web-react-manual/manuais/pixel-analytics/imagens-tratadas/09-campanhas-vendem.png`
   - `beefood-web-react-manual/manuais/pixel-analytics/imagens-tratadas/10-utm-source-medium.png`
   - `beefood-web-react-manual/manuais/pixel-analytics/imagens-tratadas/07-como-funciona.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `pixel-analytics.md` exatamente como está (seções, textos e tabelas).
- Insira as 11 imagens na ordem acima, com as legendas da tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"**.
- Idioma **português do Brasil**, tom didático.
- Mantenha em destaque: o Pixel já está ligado (sem Pixel ID da Meta); a % do funil é sobre as **visitas**; contexto **Presencial** esconde **Iniciou pagamento**; rastreio desde **01/06/2026**; campanha paga se lê com **Origem** (plataforma) + **UTM** (`utm_campaign`, `utm_source` × `utm_medium`).
- **Não** publique o rodapé "Referências internas" nem o `fluxo-codigo.md`.

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-menu-food-marketing.png` | setas | Food Marketing (1) → BeeFood Pixel Analytics (2) |
| 2 | `02-filtros-topo.png` | setas | Período, contexto, cardápio, origem, Excel, ajuda |
| 3 | `03-funil-colunas.png` | setas | As 6 etapas do funil |
| 4 | `04-funil-classico.png` | contexto | Mesmo funil no modo Funil |
| 5 | `05-kpis-resumo.png` | setas | Receita, ticket médio e conversão |
| 6 | `06-ao-vivo.png` | setas | Painel Ao vivo |
| 7 | `08-segmentacao.png` | setas | Segmentação por origem (Top Origens) |
| 8 | `11-origem-google.png` | setas | Funil recortado na origem Google |
| 9 | `09-campanhas-vendem.png` | setas | Campanhas que mais vendem (UTM Campaign) |
| 10 | `10-utm-source-medium.png` | setas | UTM Source × Medium |
| 11 | `07-como-funciona.png` | contexto | Modal Saiba como funciona |
