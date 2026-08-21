# fluxo-codigo.md — Senha gerente (#39)

Fonte: `beefood-web-react` (somente leitura). Rota `/parametros`. API `GET`/`POST` `/api/empresa2/empresaConfig`. Auto-save ~500 ms (`useEmpresaParametros`).

## Flags

| Tela | Flag | Uso |
|------|------|-----|
| Cancelar Operação Caixa | `geCai` | `CaixaVerModal`, `useCaixaVerDetalhes` |
| Cancelar Pagamento | `gePag` | `useModalPagamentosLogic`, `VendaDetalhes` |
| Cancelar Venda | `geVen` | PDV, Delivery, `usePDV` |
| Cancelar Produto Lançado | `gePro` | item já persistido no PDV |
| Editar Estoque | `geEst` | `ModalAlterarEstoque` |
| Aplicar Desconto | `geDesc` | `useDescontoGuard` |
| Desconto máximo (%) | `geDescMax` | só com `geDesc`; `0` = sem limite; **vale para gerente** |

Modal: `src/components/ModalValidarSenhaGerente.tsx`. Atalho: se `config_cache.gerente === true`, sucesso imediato (sem modal).

Fluxo do desconto (`useDescontoGuard.ts`): teto (`geDescMax`) → motivo (`motivoCancelamento`) → senha (`geDesc`).

Vídeo embutido na rota (não repetir): Senha Gerente `CeXewqyMX6w`.
