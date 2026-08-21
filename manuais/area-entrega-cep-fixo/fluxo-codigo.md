# Fluxo de código — Configuração por CEP Fixo

> Manual **#38**. Fonte: `beefood-web-react`, 21/08/2026.

| Item | Valor |
|------|-------|
| Flag | `tipoEntregaCepFixo` |
| UI | `ConfigCEPFixo.tsx` |
| Hook | `useCepFixoConfig.ts` |
| GET/POST | `/api/empresaDelivery2/cardapioDigital/areaAtendimento/cepFixo` |

Dois campos na filial: `cepFixo` (8 dígitos) e `cepFixoValor`. **Não há auto-save** — só
**Salvar (F2)**. No cardápio (`PedidoFields` / `ModalEnderecoEntrega`), o CEP do cliente
limpo é comparado com `cepFixo`; iguais → `cepFixoValor`; diferentes → fora da área.

Não há frete grátis nem tempo adicional neste tipo.
