# fluxo-codigo.md — #19 Cashback configurar (uso interno, NÃO publicar)

- Página canônica: `Cashback.desktop.tsx` → aba `configuracao` → `CashbackConfiguracaoCRMTab`.
- API: `GET/PUT /api/empresaDelivery2/cardapioDigital/cashback2/{empresaID}/{usuarioID}`.
- Hook: `useCashbackCRM` — percentuais na API são decimal (0.03 = 3%); a UI converte ×100.
- Auto-save: `updateField` / `updateMany` gravam ao mudar switch/campo.
- Canais: `cashBackCDDelivery` sempre true na UI (`lockedTrue`). Demais: presencial, manual, mesas, PDV, totem.
- Dia desmarcado: `cashBackPorDia` + flags `cashBackSegunda`… — desmarcado = não acumula **e** não usa (`CashbackConfiguracaoCRMTab` aviso vermelho).
- Exceção de produto: `useCashbackProdutoExcecao` → `POST .../cashback2/produto`. `cashBackAtivo === false` no produto.
- Bloqueio: filial sem `cardapioAdicional` ou sem `linkAcesso`.
- Aba antiga: `CardapioDigital.tsx` `tab=cashback` → `AbaMigradaAviso` para `/cashback`.
- Cardápio público (Vue, `menu.beefood.com.br`): faixa “Ganhe dinheiro de volta”; identificação em **Perfil** (`input[type=tel]` + 11 dígitos + CONTINUAR). No fechamento (`?modal=carrinho`) o saldo aparece e pode aplicar sozinho. Cache ~1 min.
- Aplicativos → Cashback aponta para `/cardapio-digital?tab=cashback` (o aviso).
