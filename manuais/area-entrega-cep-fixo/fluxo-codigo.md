# Fluxo de código — Configuração por CEP Fixo

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `area-entrega-cep-fixo.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

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
