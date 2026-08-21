# Fluxo de código — Configuração por KM

> Manual **#36**. Fonte: `beefood-web-react`, 21/08/2026.

| Item | Valor |
|------|-------|
| Flag | `tipoEntregaKM` |
| UI | `ConfigKM.tsx` + `ModalKMConfig.tsx` |
| Hook | `useKmConfig.ts` |
| CRUD | `/api/empresaDelivery2/cardapioDigital/areaAtendimento/km` |

Campos da faixa: `km` (teto), `valor`, `valorFreteGratis`, `tempoEntregaAdicional`,
`valorEntregador`, `ativo`. A distância do cliente (Google Maps a partir do pin da loja)
cai na **menor faixa cujo teto ainda cabe**. Além da maior faixa: fora da área.

O valor do entregador só aparece no relatório *Resumo Taxa Entrega*.
