# Fluxo de código — Configuração por bairro

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `area-entrega-bairro.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

> Manual **#37**. Fonte: `beefood-web-react`, 21/08/2026.

| Item | Valor |
|------|-------|
| Flag | `tipoEntregaCep` (nome legado — cobre bairro, CEP e faixa) |
| UI | `ConfigBairroCep.tsx` + `ModalBairroCepConfig.tsx` |
| Hook | `useBairroCepConfig.ts` |
| CRUD | `/api/empresaDelivery2/cardapioDigital/areaAtendimento/bairroCep` |

Cada grupo (`deliveryCepBairroID`) tem um valor e um tipo exclusivo (`bairro` | `cep` |
`cepFaixa`) com `opcoes[]`. O tipo trava depois da primeira opção. O cardápio compara
`bairroStr` (normalizado) ou o CEP do endereço do cliente. Sem match: fora da área.
