# Fluxo de código — Configuração por bairro

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
