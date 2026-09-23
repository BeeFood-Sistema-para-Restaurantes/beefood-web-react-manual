# fluxo-codigo.md — #63 Uai Rango (uso interno, NÃO publicar)

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `integracao-uai-rango.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

- Card **Aplicativos → Delivery → UaiRango** (`app.id === 'uairango'`).
- Modal: `UaiRangoModal` + `MarketplaceModalBase` (abas `credenciais` / `formas-recebimento`).
- Botão **Manual** ainda aponta para o artigo antigo:
  `https://ajuda.beefood.com.br/baseconhecimento/ativar-integracao-uai-rango/`.
- Credencial: `UaiRangoConfigModal` — `token` + `filialIDOrigem` (`__matriz__` = cardápio
  principal). **SALVAR (F2)** → `POST /api/empresa2/uairango/restaurante`.
- Lista: `GET /api/empresa2/uairango/restaurante/{empresaID}/{usuarioID}`.
  Ativo se `estabelecimentoID` preenchido; senão badge **Aguardando comunicação**.
  Token trava (`disabled`) enquanto ativo.
- Excluir: `DELETE /api/empresa2/uairango/restaurante`.
- Formas: `UaiRangoFormasRecebimentoTab` — `GET /api/empresa2/uairango/pagamento/{empresaID}/{filialID}/{usuarioID}`.
  Select grava na hora (`POST /api/empresa2/uairango/pagamento`). Sem botão Salvar.
  Sem o botão Windows *Cadastro Forma Recebimento*.
- Banner fixo na aba Credenciais: *Entre em contato com o Suporte para ativar a integração.*
- Página `MobileUaiRango*` existe; este manual é só do painel desktop.
