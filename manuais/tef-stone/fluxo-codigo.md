# fluxo-codigo.md — #53 TEF Stone (AutoTEF) (uso interno, NÃO publicar)

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `tef-stone.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

- Página `/configuracao-tef` (`ConfiguracaoTef`).
- **Novo TEF Stone (F1)** abre `ModalEditarTefConfig` com `tipoIndex === 4`.
- Campos exclusivos Stone: `codTerminal`, `portaPinPad`.
- Limite: `qtdTefStone` no `config_cache`. No sandbox da captura: 0/0 — botão existe, mas o modal Novo não abriu (quota).
- Card Aplicativos → AutoTEF Stone é contratação (`AutoTefStoneModal`), não cadastro.

