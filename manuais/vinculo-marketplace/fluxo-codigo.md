# Fluxo de código — Vínculo Marketplace (#78)

Mapeamento técnico levantado em 02/09/2026 a partir de `beefood-web-react` (clone de leitura em
`~/refs/beefood-web-react`) e de leitura da API de produção. **Não publicar nada daqui no manual.**

---

## 1. Arquivos

| Arquivo | Papel |
|---------|-------|
    10|| `src/components/ModalVinculoMarketplace.tsx` | O modal principal. Um componente para os dois modos (`modo: 'listagem' \| 'venda'`) |
| `src/components/ModalSelecionarVinculoProduto.tsx` | A janela **Selecionar Vínculo** (escolha do item do cardápio) |
| `src/components/fiscal/ModalVinculoPendenteFiscal.tsx` | A janela de bloqueio da emissão fiscal |
| `src/hooks/useVinculoMarketplace.ts` | Listagem, listagem por venda, exclusão e criar-produto-e-vincular |
| `src/hooks/useVinculoMarketplaceVincular.ts` | Itens disponíveis do cardápio e a gravação do vínculo |
| `src/pages/Delivery.tsx` | Entrada 1: `⋮` → `Vínculo Marketplace` (`modo="listagem"`) |
| `src/components/VendaDetalhes.tsx` | Entradas 2 e 3: menu `^` do rodapé (`modo="venda"`) e a faixa no item |
| `src/hooks/useModalPagamentosLogic.ts` | O mesmo bloqueio fiscal no fluxo da tela de pagamento |
| `src/components/mobile/delivery/MobileDeliveryPage.tsx` | Mesma modal no celular |

    20|---

## 2. Rotas (base `https://app3.beetechapi.be`)

| Método | Rota | Uso |
|--------|------|-----|
| GET | `/api/venda2/vinculoMarketplace/{empresaID}/{usuarioID}` | Lista completa (modo listagem) |
| GET | `/api/venda2/vinculoMarketplace/{empresaID}/{usuarioID}?numeroPreVenda=N` | Itens de uma venda (modo venda) |
| GET | `/api/venda2/vinculoMarketplace/vincular/{empresaID}/{filialID}/{usuarioID}` | Itens do cardápio disponíveis |
| POST | `/api/venda2/vinculoMarketplace/vincular` | Grava o vínculo (array, lote) |
| POST | `/api/venda2/vinculoMarketplace/criarProdutoVincular` | Cria o produto e vincula (array, lote) |
    30|| DELETE | `/api/venda2/vinculoMarketplace` | Apaga vínculos (array, lote) |

Todas com `Authorization: Bearer <token>`. O token do app vem do `localStorage`
(`beefood_auth_token`), ofuscado por XOR com a chave `bf2024_secure_key_token` — ver
`src/lib/api.ts`.

### 2.1 Campos que interessam

`vinculoMarketplace` (listagem) devolve, por linha: `marketplaceVinculoID`, `filialID`,
`descricao` (o nome do marketplace), `complemento` (booleano) + `complementoStr`
(`Produto` / `Grupo Opção`), `vinculado`, `vinculoDescricao`, `setorProduto`, `impressora`, e os
    40|alvos possíveis do vínculo (`produtoID`, `obsID`, `complementoID`, `produtoGrupoOpcID`,
`materiaPrimaID`, `produtoGrupoID`).

**A listagem não devolve de qual marketplace veio a linha.** A rota por venda devolve:
`ifoodShortReference`, `aiqfomeId` / `aiqfomeCode`, `rappiOrderID`, `uaiRangoID`,
`muchDeliveryCode`, `uberEatsDisplayId`, `americanasOrderID`, além de `ordem` (1 = produto,
2 = opção), `preVendaServicoID`, `cpvspID` e um `ignorar` que **nenhuma tela usa**.

`vinculoMarketplace/vincular` devolve o cardápio achatado em quatro tipos (`tipoObs`):
`SETOR`, `PRODUTO`, `GRUPO`, `GRUPO_OPC`. A janela monta o acordeão a partir de
`produtoSetorID` / `produtoGrupoID`, e mostra `grupoProduto` entre parênteses — é o produto a que
    50|aquela opção pertence.

---

## 3. Regras que estão no front

1. **Tipos permitidos na escolha** (`ModalSelecionarVinculoProduto`): se algum item selecionado é
   do tipo Produto (`complemento === false`, ou `tipo === 'PRODUTO'` no modo venda), a lista
   filtra `['PRODUTO']`; se todos são Grupo Opção, filtra `['PRODUTO', 'GRUPO_OPC']`.
2. **O payload de gravação** monta `produtoID` só quando o alvo é `PRODUTO` e
   `produtoGrupoOpcID` só quando é `GRUPO_OPC`; `complemento` sai como
   `item.complemento ?? item.tipo !== 'PRODUTO'`.
    60|3. **Modo venda esconde ações**: `Criar produto e vincular` e `Excluir` só renderizam com
   `modo === 'listagem'`.
4. **Vincular não tem `ConfirmationDialog`** — o `Confirmar Vínculo` já dispara o POST. Excluir e
   criar produto têm.
5. **A filial vem do contexto** (`useFiliais().filialAtual`), não da linha, na hora de abrir a
   janela de escolha; no payload de exclusão e de criação vai o `filialID` da própria linha.
6. **Bloqueio fiscal** (dois pontos, mesma regra):
   `VendaDetalhes.handleEmitirNFCe` e `useModalPagamentosLogic.handleEmitirNFCe` filtram
   `produtoID === null` **antes** de emitir e abrem `ModalVinculoPendenteFiscal`. O
   `onEmitir` da modal chama `handleEmitirNFCe(true)`, que pula a checagem.
    70|   - **Só produto entra no filtro.** Opção pendente (`produtoGrupoOpcID`/`complementoID` nulos)
     não bloqueia e não gera aviso na tela.
   - Antes disso, duas validações derrubam a emissão: `valorPago <= 0` e
     `valorPago < valorTotal`.
7. **A faixa no item** (`VendaDetalhes`, ~linha 6035) renderiza com `produto.produtoID === null` e
   chama `ModalSelecionarVinculoProduto` em `modo="venda"` com um item só.
8. **Emissão fiscal bloqueada por estado**: `src/lib/bloqueioFiscalEstado.ts` recusa emissão em
   **SC** (`ESTADOS_FISCAL_BLOQUEADOS`), e o botão exige `filialConfigVenda.fiscalAtivo`.

---
    80|
## 4. Impressão da cozinha (por que o vínculo importa)

`ImpressaoCozinhaTab` tem o card **Local de Impressão padrão para Marketplace**, com
`cozinhaMarketplacePrinterCupom` e `cozinhaMarketplaceModo`:

| Modo | Comportamento |
|------|---------------|
| `TODOS` | Todo pedido de marketplace vai inteiro para aquela impressora, ignorando setor/produto |
| `FALLBACK` | Itens com vínculo seguem setor/produto; **só os sem vínculo** caem na impressora de marketplace |

    90|O próprio texto da tela diz o motivo: *"Pedidos de marketplace às vezes chegam com produtos
ainda não vinculados aos produtos do sistema. Nos modos por setor e por produto, esses itens não
imprimiriam."* Sem impressora escolhida no modo `FALLBACK`, o item sem vínculo cai na impressora
padrão do sistema.

---

## 5. Medições no sandbox (02/09/2026, empresa 38311 / filial 39202)

Antes do manual: **786 linhas** de vínculo — 69 vinculadas, 717 pendentes; 525 do tipo Produto e
   100|261 do tipo Grupo Opção; todas na filial 39202. Os 69 vínculos existentes eram **todos**
produto → produto (nenhum apontava para opção).

Cardápio disponível para vínculo: 351 linhas = 7 setores, 67 produtos, 64 grupos e 213 opções.

Vendas de marketplace: 22 em 936 vendas de 2026 (21 AIQFome + 1 iFood).

| Venda | Origem | Itens | Pendentes | Serviu para |
|------:|--------|------:|----------:|-------------|
| 871 | iFood | 6 | 4 | Modo venda: 2 produtos vinculados + 4 opções pendentes (nível 2º) |
| 865 | AIQFome | 1 | 1 | A faixa *Produto não associado no pedido* |
   110|| 769 | AIQFome | 1 | 1 | O bloqueio fiscal (já estava paga, `valorPago = valorTotal`) |
| 770, 664, 633, 628, 627 | AIQFome | 0 | 0 | Canceladas: a rota devolve lista vazia |

### 5.1 O que o "Criar produto e vincular" faz de fato

Item **Salada Caesar** → criou o `produtoID 2540502`:

```
descricao: "Salada Caesar"   venda: null       (sem preço)
produtoSetor: "Vínculo Marketplace"  produtoSetorID: 216602   (setor criado na hora)
ativo: true   delivery: true   presencial: true   estoque: false   s3Link: null
```

   120|Ou seja: **nasce ativo nos dois canais e sem preço**. O manual insiste em completar o cadastro
por causa disso.

### 5.2 Vincular pelo pedido também alimenta a lista (testado)

`Complemento 1 - Segundo Nível`, do pedido 871, estava **Pendente** na lista geral. Depois de
vinculá-lo por dentro do pedido, a linha da lista passou a **Vinculado**, com o produto e o setor
preenchidos. Confirma o texto do manual: o vínculo feito no pedido vale para os próximos.

### 5.3 Marcar pagamento na venda não alimenta `valorPago`

Na venda 865, o botão **Marcar como pago** da linha de pagamento gravou `pago: true` no
   130|pagamento, mas `venda.valorPago` continuou **0** — e a emissão fiscal, que olha `valorPago`,
recusou com *"nenhum pagamento registrado"*. Foi por isso que o bloqueio fiscal foi fotografado
na venda **769**, que já tinha recebimento de verdade. O botão **Marcar como não pago** não
reverteu o estado (duas tentativas, sem toast e sem mudança na API).

---

## 6. Pontos que o front não resolve

- Não há **coluna/filtro por marketplace** na listagem: a rota não devolve o dado.
- Não há confirmação no **Vincular**, nem desfazer no **Excluir**.
   140|- O campo `ignorar` (rota por venda) não tem UI.
- Não existe permissão de grupo de acesso específica para esta tela: quem abre o Delivery abre o
  vínculo. (O diálogo *"Aplicativo sem permissão"* do Delivery é sobre **abrir pedidos** de um
  marketplace, não sobre vincular — e o dono confirmou em 02/09/2026 que essa permissão por
  marketplace **não existe**, mantendo o que o #75 já dizia.)
