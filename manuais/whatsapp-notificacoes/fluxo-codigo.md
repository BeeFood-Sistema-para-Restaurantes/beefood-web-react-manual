# fluxo-codigo.md — #87 Notificações de cada etapa do pedido (uso interno, NÃO publicar)

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `whatsapp-notificacoes.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

- Tela: `/whatsapp?tab=notificacaoAutomatica`.
- GET `/api/whatsapp2/notificacao/{empresa}/{usuario}`.
- Tipo 33 = entregador próximo (`raioProximidadeMetros`, default 2000).
- Até 4 textos (msgPadrao + 3). Spintax `{a|b}`.
- Print de celular: mockup (sandbox desconectado).

## Referências que estavam no rodapé do manual

Saíram de dentro do `whatsapp-notificacoes.md` em 23/09/2026: rodapé marcado "não publicar"
dentro do arquivo que o construtor lê na íntegra é vazamento esperando acontecer.

`WhatsAppNotificacaoAutomaticaTab`, `ModalEditarNotificacao`, tipo 33 =
entregador próximo. Pasta `manuais/whatsapp-notificacoes/`.
