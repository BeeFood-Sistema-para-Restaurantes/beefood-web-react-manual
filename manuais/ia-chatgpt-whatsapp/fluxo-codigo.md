# fluxo-codigo.md — #58 IA ChatGPT no WhatsApp (uso interno, NÃO publicar)

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `ia-chatgpt-whatsapp.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

- Card **Aplicativos → Marketing e CRM → Inteligência Artificial** (`app.id === 'ia'`,
  url `/ia`) e item de menu **WhatsApp → Inteligência Artificial**.
- Página `InteligenciaArtificial.tsx`: passos 1 `IAStep1BoasVindas`, 2
  `IAStep2AssociarConta` (campo `Chave Secreta` / `sk-proj-…`), 3
  `IAStep3Configuracoes`.
- Passo 3 abre quando `assistant_id` começa com `asst_`.
- Token: `useIAToken` → `https://ia.beetechapi.be/api/rest/chatGPT/token`.
- Config: `useIAChatGPTConfig` → `empresaDelivery2/chatGPT`
  (`chatGPT`, `chatGPTNome`, `chatGPTTipo` SUP/INT/ESP).
- Modelos na UI: `gpt-4o-mini`, `gpt-4o`, `gpt-4-turbo`, `gpt-3.5-turbo`.
- Conhecimento extra: `ModalConhecimentoIA` + `useIAConhecimento`.
- `IAModal` em Aplicativos só redireciona para `/ia`.
- Botão **MANUAL DE CONFIGURAÇÃO** ainda aponta para o artigo antigo do
  ajuda.beefood.
