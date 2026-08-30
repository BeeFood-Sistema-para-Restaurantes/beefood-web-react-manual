# fluxo-codigo.md — #64 Desconto formas de recebimento (uso interno, NÃO publicar)

- Abas: `CardapioDigital.tsx` `tab=formasRecebimento` e `tab=pagamentoOnline`.
- Formas: `GET /api/empresaDelivery2/cardapioDigital/recebimento/{empresaID}/{filialID}/{usuarioID}`.
- Grava forma: `POST /api/empresaDelivery2/cardapioDigital/recebimento` com
  `deliveryRecebimentoID`, `descontoTipoAplicacao` (`DESCONTO` | `ACRESCIMO` | null),
  `descontoTipoValor` (`%` | `R$` | null), `descontoValor`, `ativo`, `delivery`,
  `retirada`. **Sem ajuste** = os três campos de desconto `null`.
- Editor: modal **Editar forma de recebimento** — **SALVAR (F2)**. Opções do
  combo: Sem ajuste, Desconto em %, Desconto em R$, Acréscimo em %, Acréscimo em R$.
- Pagamento Online: `GET /api/empresaDelivery2/cardapioDigital/pagamentoOnline/{empresaID}/{filialID}/{usuarioID}`.
- Grava PIX/MP: `POST .../pagamentoOnline` com `pixOnlineDescontoTipoAplicacao|TipoValor|Valor`
  e `creditoOnlineDesconto*`. Auto-save ao mudar combo/campo.
- PIX Online: só `Sem desconto` / `Desconto em %` / `Desconto em R$` (sem acréscimo).
- MP: mesmas cinco opções das formas (`Sem ajuste` + desconto/acréscimo).
- Cadastros `GET /api/empresa2/formaPagamento/{empresaID}/{usuarioID}` é o vínculo
  (`formaPagamentoID`). Desconto de lá é do **PDV**, não do cardápio.
- Cardápio Vue (`menu.beefood.com.br`): PIX Online em destaque; demais em
  “Outras formas de pagamento”. Badge “N% de desconto” / “N% de acréscimo”.
  Linha no resumo: `Desconto 5% (Pix) − R$ …` ou `Acréscimo 5% (Vale…) + R$ …`.
  Base = subtotal dos produtos. Cache `validaDelivery` ~1 min.
- IDs sandbox (BeeFood3): empresa 38311, filial 39202, usuário 88711.
  Dinheiro `deliveryRecebimentoID` 687811; Vale Alelo 6878xx (ativar + acréscimo).
