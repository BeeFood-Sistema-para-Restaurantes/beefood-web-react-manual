# fluxo-codigo.md — #21 Cupom de Desconto (uso interno, NÃO publicar)

- Página `CupomDesconto` → `CupomDescontoCRMPage`: abas Cupons / Histórico.
- Lista: `CupomListagemCRM` (`toggleAtivo`, `cupomLink`, filtros).
- Modal: `ModalEditarCupomCRM`. Grava `useCupomDescontoCRM` → API
  `empresaDelivery2` / cupom.
- Tipos: `tipoDesc` DESC | FRET | PROD; DESC usa `tipo` PERCENTUAL | VALORFIXO.
- Novos campos (ago/2026): `formasPagamento`, `setoresLibera`, `setoresRestrito`,
  `produtosLibera`, `produtosRestrito`, `apenasRetiradaConsumo`,
  `naoAplicarEmPromocao`, `validarTelefoneSms`.
- Modo na UI: `NENHUM` | `LIBERA` | `RESTRINGE` (um por cupom). RESTRINGE some
  em FRET/PROD.
- Opções do accordion: `useOpcoesCupomAvancado` (setores, produtos, formas).
- Cardápio público: faixa `promo-banner` (“Você tem N cupons”) abre overlay
  **ADICIONAR CUPOM** (Vue). Aba **Promoções** do rodapé é outra feature
  (produto com preço promocional).
- Na venda (painel): `ModalAplicarCupomDesconto`, `cupomDescontoGuards`,
  bloqueio de forma em `ModalPagamentos` — fora deste manual.
