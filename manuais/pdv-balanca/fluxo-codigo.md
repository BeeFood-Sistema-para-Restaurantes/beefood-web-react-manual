# fluxo-codigo.md — PDV balança (#46)

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `pdv-balanca.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

`src/utils/balancaParser.ts` — `parseCodigoBalanca`, `gerarCodigoBalanca`, `isCodigoBalanca`.

Config: `balancaAtivada`, `balancaTipoLeitura` (0 Peso / 1 Valor), `balancaDigitoCodigo`, `balancaDigitoCodigoFim`, `balancaDigitoPreco`, `balancaDigitoPrecoFim`. Defaults no código: 1–5 / 6–11.

Consumo: `PDV.tsx`, `usePDV.ts`, `useModalPedidos.ts` — se `isBalanca` e acha `produto.codigo`, insere com `quantidade` e `valorOriginal`.

Peso: `qtd = valor / 1000`. Valor: `qtd = (valor / 100) / precoProduto`, arredonda 4 casas.
