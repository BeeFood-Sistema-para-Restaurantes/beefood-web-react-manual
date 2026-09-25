# texto-documentation.ia.md — #87 Notificações de cada etapa do pedido

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `whatsapp-notificacoes.md`
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

Crie um novo manual no app: em **WhatsApp**, adicione um manual chamado
**"Notificações de cada etapa do pedido"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/whatsapp-notificacoes/whatsapp-notificacoes.md`

2. **Imagens (use estas 4, nesta ordem):**
   - `beefood-web-react-manual/manuais/whatsapp-notificacoes/imagens-tratadas/01-lista.png`
   - `beefood-web-react-manual/manuais/whatsapp-notificacoes/imagens-tratadas/02-editar-pedido-feito.png`
   - `beefood-web-react-manual/manuais/whatsapp-notificacoes/imagens-tratadas/03-editar-entregador.png`
   - `beefood-web-react-manual/manuais/whatsapp-notificacoes/imagens-tratadas/04-whatsapp-notificacao.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `whatsapp-notificacoes.md` exatamente como está (seções, textos e tabelas).
- Insira as 4 imagens na ordem acima, com as legendas da tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"**.
- Idioma **português do Brasil**, tom didático.
- Use números normais (`1`, `2`, `3`) — não use ①②③.
- **Não** publique o rodapé "Referências internas".

---

## Anexo — legendas das imagens (na ordem)

| 1 | `01-lista.png` | setas | Lista Delivery 11/11 |
| 2 | `02-editar-pedido-feito.png` | setas | Ficha Pedido feito |
| 3 | `03-editar-entregador.png` | setas | Raio km + texto |
| 4 | `04-whatsapp-notificacao.png` | contexto | Celular Pedido confirmado (fake) |
