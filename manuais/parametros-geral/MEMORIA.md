# MEMÓRIA — #42 Parâmetros gerais

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `parametros-geral.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

Status: ✅ 21/08/2026.

**Motivo:** prova no PDV via desconto — modal **Motivo do Desconto** (Descrição *, mín. 2 palavras). O mesmo guard (`useDescontoGuard`) serve cancelamento.

**Operador:** Testar em `/parametros` abre **Teste de Validação de Operador** (teclado 6 casas). No salão, com o flag ON, aparece **Identificação do Operador** e bloqueia Novo Pedido / PDV. `contato@` não tem `funcionarioID` — por isso o Testar abre.

`operadorPDVObrigar` existe na API e no mobile — **sem switch no desktop**.
