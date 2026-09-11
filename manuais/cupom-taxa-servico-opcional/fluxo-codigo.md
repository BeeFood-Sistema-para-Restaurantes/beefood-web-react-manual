# fluxo-codigo.md — Taxa de serviço opcional no cupom (#98)

## Tela

| Peça | Arquivo |
|------|---------|
| Rota `/impressao?tab=layout` | `src/pages/Impressao.tsx` |
| Lista por cardápio | `src/components/ImpressaoLayoutTab.tsx` |
| Modal | `src/components/ModalEditarImpressaoLayout.tsx` |
| GET/POST | `src/hooks/useImpressaoLayout.ts` → `/api/empresa2/impressaoLayout` |

`tipo === 'DELIVERY'` é o rótulo **Cupom Pedido** (não é só delivery).

## Campos do rodapé

| Campo da API | Coluna da aba Texto Padrão | Quem usa |
|--------------|----------------------------|----------|
| `descricaoRodapeDelivery` | Texto padrão Delivery → Rodapé | venda `tipo === 'DELIVERY'` |
| `descricaoRodape` | Texto padrão Presencial → Rodapé | mesa, comanda, PDV |

Montagem: `src/lib/cupom-pedido-utils.ts` (`gerarLinhasCupomPedido`). O rodapé
personalizado entra **depois** do QR do cardápio e **antes** do rodapé BeeFood.

```
const rodape = isDelivery ? config.descricaoRodapeDelivery : config.descricaoRodape;
linhas.push(...textoParaLinhas(rodape, { pequeno: true }));
```

`textoParaLinhas` só faz `split(/\r?\n/)`. Sem markdown.

## Cache

`src/lib/impressao-config-cache.ts` — TTL 12 h, chave por
`(empresa, filial, usuário)`. O POST do layout chama `limparCacheImpressaoConfig()`.

## Impressão no Cloud Agent

`imprimirViaIframe` (`src/lib/impressao-service.ts`) escreve no iframe oculto
`#beefood-print-frame`. Sem BeeImpressão, é o fallback depois de
`checkPrinterConnection()` falhar.
