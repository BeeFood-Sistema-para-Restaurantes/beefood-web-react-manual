# Fluxo de código — Capas e Destaques do cardápio digital

> Mapeamento técnico do que o manual **#48 Capas e Destaques** documenta.
> Fonte: `beefood-web-react` e `beetech-server-node-2.0` (branch `beefood-web-react`),
> somente leitura. Levantado em 22/08/2026.

---

## 1. Onde fica

| Item | Valor |
|------|-------|
| Página | `src/pages/CardapioDigital.tsx` |
| Rota | `/cardapio-digital?tab=configuracoes` |
| Aba | `src/components/cardapio-digital/ConfiguracoesTab.tsx` |
| Card-resumo | `src/components/cardapio-digital/BannersDestaquesResumo.tsx` |
| Modal | `src/components/cardapio-digital/ModalBannersDestaques.tsx` |
| Linha de mídia | `src/components/cardapio-digital/BannerMidiaLinha.tsx` |
| Recorte 16:9 | `src/components/cardapio-digital/ModalRecortarVideoBanner.tsx` |
| Hook | `src/hooks/useCardapioDigitalBanners.ts` |
| Validação | `src/utils/bannerMidiaValidation.ts` |
| Agenda (preview) | `src/utils/bannerAgenda.ts` |
| Recorte no browser | `src/utils/recortarVideoBanner.ts` (WebCodecs, sem áudio) |
| Prévia celular | `src/components/cardapio-digital/preview/PreviewCardapioDigital.tsx` |

A capa **fixa** (`fotoCapa`) mora no mesmo card de Aparência, no preview clicável do
topo. Aceita só imagem (`png/jpeg/webp`). Os **destaques da capa** (grupo `capas`)
é que entram no carrossel **junto** com essa capa e aceitam vídeo.

O cardápio público (Vue, `beetech-beeshop-nuxt`) **não está neste repositório**.
Agenda no cliente: mesmo helper dos avisos (`bannerAgenda`).

---

## 2. Dois grupos

| Grupo | Chave API | Onde o cliente vê |
|-------|-----------|-------------------|
| Destaques da capa | `capas` | Carrossel do topo, sobre/depois da `fotoCapa` |
| Destaques da sua loja | `lojas` | Vitrine no corpo, junto das categorias |

Teto: **5 mídias por grupo** (`MAX_ITENS_POR_GRUPO` / `maxPorGrupo` da API).
Contador `N/5` no modal.

---

## 3. API

```
GET  /api/empresaDelivery2/cardapioDigital/banners/{empresaID}/{filialID}/{usuarioID}
POST /api/empresaDelivery2/cardapioDigital/banners
```

Body do POST: `{ empresaID, filialID, usuarioID, usuario, capas: [...], lojas: [...] }`.

Coluna `_EmpresaDelivery.bannersJson`, **separada** de `avisosJson`. Documento vazio
grava `NULL` (some do `validaDelivery`). Teto do JSON: **8000** caracteres
(`BANNERS_JSON_GRANDE` → HTTP 400, campo `mensagem`).

Cada item: `id, url, tipo (I|V), ordem, dias, todoDia, hIni, hFim, ctx, on`.

`dias`: domingo=1 … sábado=7. `ctx`: `D` e/ou `P`. Sem dia válido ou sem ctx, o
backend assume todos / os dois.

---

## 4. Salvamento no painel

**Não tem auto-save.** O modal acumula em estado local (`dirty`). Só o
**SALVAR (F2)** chama o POST. **FECHAR (ESC)** com alteração abre
“Descartar alterações”. Clique fora do modal é bloqueado.

Atalhos: F2 salva, ESC fecha.

Upload: `useUploadImageS3` em `{filialID}/banners`, `otimizar: false` (a
validação já otimizou a imagem). Tipos: JPG, PNG, WEBP, GIF, MP4, WEBM, MOV
(H.264 reembalado como MP4).

---

## 5. Validação da mídia (antes do S3)

`bannerMidiaValidation.ts` — alvo: navegador de celular.

| Regra | Efeito |
|-------|--------|
| Horizontal (largura > altura) | Imagem vertical é recusada; vídeo vertical abre recorte 16:9 |
| Imagem | JPG/PNG/WEBP/GIF, teto 2 MB (otimiza sozinha até 1920 px) |
| Vídeo | MP4/WEBM/M4V, teto **15 MB**, maior lado ≤ 1920 px |
| HEVC/H.265 | Bloqueado (tela preta no Android sem evento de erro) |
| AVI / MKV / SVG | Bloqueados |
| GIF > 1 MB | Aviso: preferir MP4 |
| Vídeo > 5 MB | Aviso: pode demorar no 4G |
| Recorte | Só se o vídeo tiver até **60 s**; saída 1280×720, **sem áudio** |

---

## 6. Agenda no cardápio

Porte do helper (`bannerAgenda.ts` / shop):

- `on === false` → some
- `ctx` não inclui o canal atual → some
- dia = `getDay() + 1`
- `todoDia` → vale o dia inteiro
- senão `minutos >= hIni` e `minutos < hFim` (fim **exclusivo**)
- janela **não cruza meia-noite**

Quem decide é o relógio **do celular do cliente**. Reavalia a cada ~60 s.
Cache do `validaDelivery` ~1 min — o changelog e o toast pedem essa espera.

No backend, `hIni >= hFim` ou hora inválida vira **dia inteiro** (não descarta
a mídia). No painel, o F2 recusa se faltar hora ou se início = fim.

---

## 7. Prévia do celular (aba Configurações)

`PreviewCardapioDigital` (visível em `xl`):

- a `fotoCapa` entra como **primeiro slide** se existir
- depois rodam os `capas` no ar
- a vitrine de `lojas` fica abaixo do nome da loja
- setas e bolinhas quando há mais de um slide
- alternador Delivery / Presencial se o presencial estiver habilitado
- vídeos tocam mudos; no fim avançam o carrossel

---

## 8. O que este manual não cobre

- Aviso (recado operacional, só imagem 1:1) — manual #47
- Horário de atendimento / pausa — #32 e #33
- Banner verde de cupom e card amarelo de cashback do cardápio público
