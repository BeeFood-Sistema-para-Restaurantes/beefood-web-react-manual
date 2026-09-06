# fluxo-codigo.md — #90 Conectar o WhatsApp (QR Code) (uso interno, NÃO publicar)

- Tela: `/whatsapp?tab=configuracao` (`WhatsAppConexaoContent`).
- **Conectar**: `POST https://whatsapp-cron.beetechapi.be/api/rest/whatsapp/instancia/{empresaID}/{filialID}` (Basic beetech).
- Polling de instâncias a cada 3 s. QR em `instancia.qr_code` quando `status=connecting`.
- Modal Expandir: `WhatsAppConexaoCard` Dialog com img 64.
- Sandbox: gerou QR de verdade; **não** escaneado. Card ficou Conectando.

