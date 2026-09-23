# MEMÓRIA — #41 Taxa e obrigatoriedades

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `mesas-taxa-obrigatorias.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

Status: ✅ 21/08/2026.

Prova da taxa: Mesas → Novo Pedido (F1) → Coxinha R$ 8,00 → **Taxa Serviço (10%) + R$ 0,80**, total **R$ 8,80**.

Mesa obrigatória: abre o modal **Selecionar Mesa**; Salvar fica indisponível sem mesa.

`operadorPDV` ligado bloqueia Novo Pedido com **Identificação do Operador** — desligar o operador antes de capturar o salão.

Flags: `taxaServicoPadrao`, `taxaServicoValor` (10), `mesaClienteObrigatorio`, `appGarcomComandaObrigatoria`, `appGarcomMesaObrigatoria`.
