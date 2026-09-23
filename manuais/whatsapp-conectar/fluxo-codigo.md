# fluxo-codigo.md — #90 Conectar o WhatsApp (QR Code) (uso interno, NÃO publicar)

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `whatsapp-conectar.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

- Tela: `/whatsapp?tab=configuracao` (`WhatsAppConexaoContent`).
- **Conectar**: `POST https://whatsapp-cron.beetechapi.be/api/rest/whatsapp/instancia/{empresaID}/{filialID}` (Basic beetech).
- Polling de instâncias a cada 3 s. QR em `instancia.qr_code` quando `status=connecting`.
- Modal Expandir: `WhatsAppConexaoCard` Dialog com img 64.
- Sandbox: gerou QR de verdade; **não** escaneado. Card ficou Conectando.

## Referências que estavam no rodapé do manual

Saíram de dentro do `whatsapp-conectar.md` em 23/09/2026: rodapé marcado "não publicar"
dentro do arquivo que o construtor lê na íntegra é vazamento esperando acontecer.

Código: `WhatsAppConexaoCard` (`POST …/whatsapp/instancia/{empresa}/{filial}`),
polling em `WhatsAppConexaoContent`. Pasta `manuais/whatsapp-conectar/`.
