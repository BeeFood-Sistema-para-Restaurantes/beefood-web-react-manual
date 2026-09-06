# fluxo-codigo.md — #87 Notificações de cada etapa do pedido (uso interno, NÃO publicar)

- Tela: `/whatsapp?tab=notificacaoAutomatica`.
- GET `/api/whatsapp2/notificacao/{empresa}/{usuario}`.
- Tipo 33 = entregador próximo (`raioProximidadeMetros`, default 2000).
- Até 4 textos (msgPadrao + 3). Spintax `{a|b}`.
- Print de celular: mockup (sandbox desconectado).

