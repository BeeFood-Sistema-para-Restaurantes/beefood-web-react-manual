# fluxo-codigo.md — Taxa e obrigatoriedades (#41)

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `mesas-taxa-obrigatorias.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

| Tela | Flag | Uso |
|------|------|-----|
| Taxa de Serviço Padrão | `taxaServicoPadrao` | `PDV.tsx` / `PedidoFields` preenche `taxaServico` se há mesa ou comanda |
| Valor da Taxa (%) | `taxaServicoValor` | percentual |
| Cliente obrigatório | `mesaClienteObrigatorio` | recusa gravar sem cliente |
| Comanda obrigatória | `appGarcomComandaObrigatoria` | `useMesasData` / `PedidoFields` |
| Mesa obrigatória | `appGarcomMesaObrigatoria` | idem |

Changelog do produto: flags valem no web e no app. Prova só no web.
