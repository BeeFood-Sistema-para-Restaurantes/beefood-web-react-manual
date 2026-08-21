# fluxo-codigo.md — Taxa e obrigatoriedades (#41)

| Tela | Flag | Uso |
|------|------|-----|
| Taxa de Serviço Padrão | `taxaServicoPadrao` | `PDV.tsx` / `PedidoFields` preenche `taxaServico` se há mesa ou comanda |
| Valor da Taxa (%) | `taxaServicoValor` | percentual |
| Cliente obrigatório | `mesaClienteObrigatorio` | recusa gravar sem cliente |
| Comanda obrigatória | `appGarcomComandaObrigatoria` | `useMesasData` / `PedidoFields` |
| Mesa obrigatória | `appGarcomMesaObrigatoria` | idem |

Changelog do produto: flags valem no web e no app. Prova só no web.
