# texto-documentation.ia.md — Senha gerente (#39)

> Cole o bloco abaixo na IA de documentação do app.

---

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `senha-gerente.md`
  e das imagens listados neste prompt.
- **Não publique**, em nenhuma seção: rota ou URL de API (`/api/...`); nome de campo,
  de arquivo, de componente, de tabela ou de coluna; bloco de código, JSON ou
  `campo=true`; nem as palavras *backend*, *endpoint*, *payload*, *array*, *bundle*.
  Se a frase só faz sentido para quem programa, ela não entra. Única exceção: a URL
  completa de webhook que o lojista copia para o painel do parceiro.
- Se você leu **qualquer outro arquivo** desta pasta — `fluxo-codigo.md`,
  `MEMORIA.md`, `annotate.py`, `capturar.py` —, **descarte o que leu**: são anotações
  internas de quem produziu o manual.
- Em 23/09/2026 uma página publicada saiu com a rota da API do cupom e dois nomes de
  campo do cashback, porque esta regra não estava aqui em cima.

Crie um novo manual no app: em **Configuração**, item **"Senha do gerente"**.

**Leia APENAS:**

1. `beefood-web-react-manual/manuais/senha-gerente/senha-gerente.md`
2. As imagens, nesta ordem:
   - `.../senha-gerente/imagens-tratadas/01-menu-parametros.png`
   - `.../senha-gerente/imagens-tratadas/03-switches-ligados.png`
   - `.../senha-gerente/imagens-tratadas/06-novo-usuario.png`
   - `.../senha-gerente/imagens-tratadas/07-usuario-criado.png`
   - `.../senha-gerente/imagens-tratadas/08-atendente-parametros.png`
   - `.../senha-gerente/imagens-tratadas/10-pdv-coxinha.png`
   - `.../senha-gerente/imagens-tratadas/11-modal-desconto.png`
   - `.../senha-gerente/imagens-tratadas/13-pede-senha.png`
   - `.../senha-gerente/imagens-tratadas/04-testar-como-gerente.png`

**NÃO leia** `fluxo-codigo.md`, `MEMORIA.md`, `annotate.py`, `imagens-puras/`.

Use o `.md` na íntegra. Números `1`, `2`, `3` (nunca ①). Português do Brasil. Não publique senha de gerente. Destaque: o teto % vale inclusive para o gerente; usuário gerente não vê o modal.
