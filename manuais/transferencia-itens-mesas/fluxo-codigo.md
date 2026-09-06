# Fluxo de código — #94 Transferir item entre mesas e comandas

Documento interno: **não publicar**.

## Onde vive

| Caminho | Rota | Componente |
|---------|------|------------|
| Mesas/Comandas → painel da venda | `/mesas` | `VendaDetalhes.tsx` + `ModalTransferirProdutos.tsx` |

O mesmo `VendaDetalhes` aparece em Histórico, Caixa e mobile. O botão **Transferir**
só renderiza se `venda.tipo === 'MESA'` e `!isReadOnly`.

`isReadOnly` = marketplace **ou** agrupado **ou** cancelada **ou**
`situacao === 'RECEBIDO'` em MESA/PDV. Desabilitado também se `produtos.length === 0`,
`fechamentoSolicitado` ou venda cancelada.

Produtos enviados ao modal: `produtos.filter(p => !p.excluido)`.

## Assistente (3 passos)

`ModalTransferirProdutos`:

1. Produtos — `Set` de `preVendaServicoID`. A linha inteira vai (`qtd` como está).
2. Destino — `GET /datasnap/rest/venda2/mesa/{empresaID}/{usuarioID}`, filtrado
   `preVendaID !== origem` e `situacao === "ABERTO"`. Empty:
   *Nenhuma venda disponível para transferência*.
3. Confirmar — POST ` /datasnap/rest/venda2/transferir`. Toast:
   `N produto(s) transferido(s) com sucesso!`

Body: `origem` + `destino` (preVendaID, número, mesa/comanda IDs e labels) e
`produtos[]` (`produtoID`, `descricao`, `qtd`, `venda`, `preVendaServicoID`).
`funcionarioID` do operador efetivo.

## O que não é isto

- Chip azul/laranja no `VendaDetalhes` → `ModalSelecionarMesaComanda` (troca a
  mesa/comanda **da mesma** venda).
- TRANSFERIR do caixa → `CaixaSelecionarModal` / `caixa2/transferir` (backlog #4).

Não há permissão específica de grupo para este botão (não entra no #75).

Bug interno (não documentar): o `useEffect` de autofocus testa `if (!open)` mas a
prop é `isOpen`.

## Help

Registrar em `help-manuais.ts` (repo `beefood-web-react`, não este):

- `/mesas` → acrescentar slug `transferencia-itens-mesas`
