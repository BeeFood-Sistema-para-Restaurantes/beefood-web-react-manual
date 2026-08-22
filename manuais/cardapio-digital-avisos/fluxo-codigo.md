# Fluxo de código — Avisos do cardápio digital

> Mapeamento técnico do que o manual **#47 Avisos do cardápio digital** documenta.
> Fonte: `beefood-web-react` e `beetech-server-node-2.0` (branch `beefood-web-react`),
> somente leitura. Levantado em 22/08/2026. Painel em produção: **v3.220826.1102**.

---

## 1. Onde fica

| Item | Valor |
|------|-------|
| Página | `src/pages/CardapioDigital.tsx` |
| Rota | `/cardapio-digital?tab=avisos` |
| Aba desktop | `src/components/cardapio-digital/AvisosTab.tsx` |
| Aba mobile | `src/components/mobile/cardapio-digital/MobileAvisosTab.tsx` (reusa `AvisosTab` com `mobile`) |
| Card do painel | `src/components/cardapio-digital/AvisoPreviewCard.tsx` |
| Modal | `src/components/cardapio-digital/ModalAvisoEditor.tsx` |
| Hook | `src/hooks/useCardapioDigitalAvisos.ts` |
| Validação da imagem | `src/utils/avisoImagemValidation.ts` |
| Menu | `src/components/AppSidebar.tsx` — `permissionKey: "avisos"`, `isNew: true` |
| Permissão | `src/hooks/usePermissions.ts` — `'avisos': 'avisos'` |

O cardápio público (Vue, `beetech-beeshop-nuxt`) **não está neste repositório**. Agenda
no cliente: mesmo helper dos banners (`utils/helpers/bannerAgenda.js`).

---

## 2. API

```
GET  /api/empresaDelivery2/cardapioDigital/avisos/{empresaID}/{filialID}/{usuarioID}
POST /api/empresaDelivery2/cardapioDigital/avisos
```

Body do POST: `{ empresaID, filialID, usuarioID, usuario, avisos: [...] }`.

Coluna `_EmpresaDelivery.avisosJson`, **separada** de `bannersJson`. Documento vazio
grava `NULL` (a faixa some do `validaDelivery`). Teto do JSON: **8000** caracteres
(`AVISOS_JSON_GRANDE` → HTTP 400, campo `mensagem`).

Limites na resposta (o painel usa estes, com piso de 10 no `maxAvisos`):

| Campo | Valor |
|-------|-------|
| `maxAvisos` | 10 |
| `maxTitulo` | 60 |
| `maxDescricao` | 500 |

Cada item: `id, url, titulo, descricao, ordem, dias, todoDia, hIni, hFim, ctx, on`.

`dias`: domingo=1 … sábado=7. `ctx`: `D` e/ou `P`. Sem dia válido ou sem ctx, o
backend assume todos / os dois.

---

## 3. Salvamento no painel

Não há barra de salvar. `persistir` reindexa `ordem` 1..N e chama `salvar`. Ações
que gravam: upload (depois do modal), F2 do editor, drag-and-drop, confirmar
lixeira.

Upload: `useUploadImageS3` em `{filialID}/avisos`, só imagem, `AVISO_MAX_MB = 2`,
otimização automática (maior lado 1200). Vídeo e SVG bloqueados. GIF > 1 MB só
alerta. Proporção fora de ~1:1 só alerta.

Aviso novo sem título: fechar o modal remove o item da lista local (`pendenteId`)
e **não** chama o POST.

---

## 4. Agenda no cardápio

Porte do helper (preview do painel em `bannerAgenda.ts`):

- `on === false` → some
- `ctx` não inclui o canal atual → some
- dia = `getDay() + 1`
- `todoDia` → vale o dia inteiro
- senão `minutos >= hIni` e `minutos < hFim` (fim exclusivo)
- janela não cruza meia-noite

Reavalia a cada ~60 s no cliente. O cache que alimenta o cardápio (Lambda
`valida_delivery` + cron) explica o atraso de até 1 minuto.

---

## 5. Sanitização no backend

`src/models/empresaDelivery/avisosCardapio.js`:

- sem URL `https` o item é **descartado** (não vira retângulo cinza)
- título/descrição: corta controle e aplica o teto
- `hIni >= hFim` ou hora inválida → **dia inteiro**, não exclui
- log de auditoria: resumo curto (`resumirAvisos`), não o JSON inteiro

---

## 6. O que este manual não cobre

- Capas e Destaques (vídeo, rotação automática) — aba Configurações
- Pausa programada / pausa temporária — manuais #32 e #33
- Banner verde de cupom e card amarelo de cashback do cardápio público
