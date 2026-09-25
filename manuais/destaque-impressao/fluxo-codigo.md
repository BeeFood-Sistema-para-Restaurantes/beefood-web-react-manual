# fluxo-codigo.md — #99 Destaque na impressão (uso interno, NÃO publicar)

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `destaque-impressao.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

## Campo

- API: `destaqueImpressao` boolean (`true` ligado, `null`/`false` desligado).
- Gravação segue o padrão de `semTaxaServico`: `formData.destaqueImpressao ? true : null`.
- Vale para **produto e complemento**. Não é o switch **Destaque** do cardápio digital (`formData.destaque`).

## Cadastro

- Desktop: `ModalEditarProduto.tsx` — switch `#destaqueImpressao` **abaixo do campo Descrição**, visível também quando `isComplemento`.
- Rótulo: **Destaque na impressão**.
- Texto: *Ativo: o item sai em destaque na impressão do pedido.* / *Inativo: o item é impresso normalmente.*
- Mobile: `MobileEditarProdutoPage.tsx`.
- Estado: `useEditarProdutoLogic.ts`. Grava no **SALVAR E SAIR** (`useSalvarProduto`). Sem auto-save.
- Depois de salvar: `limparDestaqueImpressaoCache()` + aviso aos servidores de impressão.

## Editar em Lote

- `ModalEditarLote.tsx` etapa 2: `ToggleField` **Destaque na impressão** (`destaqueImpressaoCheck` + `destaqueImpressao`).
- O switch Sim/Não só aparece depois de marcar o checkbox do campo. Default do valor é `null` → **Não**.
- Sem restrição `!isComplemento` — existe no lote de **Produtos** e de **Complementos**.
- `useEditarLote.ts`: POST `/api/produto2/cardapio/editarLote` em lotes de 5. Limpa o cache ao terminar.

## Impressão

- A venda (`ProdutoVenda` / `OpcaoVenda`) **não** traz o campo. O front monta mapas por `produtoID` e `produtoGrupoOpcID` em `destaque-impressao-cache.ts`:
  - GET `cardapio2/cardapio/{empresa}/{usuario}/{delivery}/{presencial}/1` (as duas visões)
  - GET `cardapio2/grupoOpcoes/{empresa}/{usuario}/{delivery}/{presencial}/1`
  - Cache `localStorage` `beefood_destaque_impressao_v3:{empresa}:{usuario}`, TTL **12 h**. Falha = conjuntos vazios (cupom igual ao antigo).
  - `limparDestaqueImpressaoCache()` roda **no navegador que salvou**. Outra estação só troca a lista quando o TTL vence (até 12 h) — é o que o manual chama de "um computador imprime com destaque e o outro não".
- Cupom Pedido: `cupom-pedido-utils.ts` marca a linha com `invertido` (fundo preto, letra branca). Preço na linha de baixo **não** inverte.
  - `invertido` é o mesmo estilo usado na **observação** quando `config.obsNegrito` está ligado — daí a resposta "é igual ao da observação".
  - `gerarLinhasCupomPedido` é compartilhado por `VendaDetalhes`, `useModalPagamentosLogic` e `AceiteAutomatico` → o destaque vale para **presencial e delivery**, inclusive na impressão do aceite automático.
- Cozinha (fallback do navegador): `VendaDetalhes.imprimirCozinhaFallback` — mesma regra, sem valores.
- Cozinha via BeeImpressão (`POST /imprimirCozinha` em `localhost:1317`) manda só IDs (`preVendaID`) — o layout é montado no servidor, que não recebe o mapa de destaques. O fundo escuro na cozinha está comprovado no caminho do navegador; pelo BeeImpressão depende de o servidor de impressão ter a regra. **Não afirmar no manual publicado.**
- Fichas do PDV ficaram de fora nesta versão (não carregam `produtoID` no topo).

## Cloud Agent

- Abortar `localhost:1316` (cupom) e `localhost:1317` (cozinha) para cair no iframe `#beefood-print-frame`.
- IDs sandbox: empresa `38311`, filial `39202`, usuário `88711`.
