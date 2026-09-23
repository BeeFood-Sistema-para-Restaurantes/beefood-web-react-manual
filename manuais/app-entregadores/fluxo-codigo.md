# fluxo-codigo.md — #57 BeeFood Entregador (uso interno, NÃO publicar)

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `app-entregadores.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

- Card **Aplicativos → Entrega → BeeFood Entregador** (`app.id === 'beefood-entregador'`). Modal: `BeeFoodEntregadorModal` — só orientação + links Play/App Store. Não grava parâmetro.
- Funcionário: `/cadastro-funcionarios` → `ModalEditarFuncionario` aba **Função**. Radio `entregador` (exclui `garcom` / `outro`). Campos opcionais `valorDiaria` e `valorPorKM`. **SALVAR (F2)**.
- Usuário: `/usuarios` → `ModalEditarUsuario`. Vincular `funcionarioID` + switch **Aplicativos** (`webAcesso`). No Windows antigo era “Acesso Aplicativos”. **SALVAR (F2)**.
- Cupom: `/impressao?tab=layout` → **Cupom Pedido** (`tipo === 'DELIVERY'`) → aba **Texto Padrão** → checkbox **Código de Barras App Entrega** (`beeEntregaCodigoBarras`).
- Impressão: `cupom-pedido-utils.ts` imprime o código de barras com `venda.preVendaID` só em pedido **DELIVERY + ENTREGA**, se `beeEntregaCodigoBarras` e (`beetechPlanoID === 5` ou `entregaAtiva`).
- App nativo: `com.beetechentregador` (Android) / `id6736578030` (iOS). Emulador Android **não** sobe neste Cloud Agent — prints do app reaproveitados do artigo antigo.
