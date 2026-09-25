# Fluxo de código — Configuração por KM

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `area-entrega-km.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

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
