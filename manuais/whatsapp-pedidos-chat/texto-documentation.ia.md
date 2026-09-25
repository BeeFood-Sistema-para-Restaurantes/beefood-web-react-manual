# texto-documentation.ia.md — #86 Pedidos pelo chat no WhatsApp

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `whatsapp-pedidos-chat.md`
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
**"Pedidos pelo chat no WhatsApp"** (também serve para busca: pedido pelo
WhatsApp, BeeBot, pedido pelo chat).

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/whatsapp-pedidos-chat/whatsapp-pedidos-chat.md`

2. **Imagens (use estas 5, nesta ordem):**
   - `beefood-web-react-manual/manuais/whatsapp-pedidos-chat/imagens-tratadas/01-beefood-whatsapp.png`
   - `beefood-web-react-manual/manuais/whatsapp-pedidos-chat/imagens-tratadas/02-login-bot.png`
   - `beefood-web-react-manual/manuais/whatsapp-pedidos-chat/imagens-tratadas/03-pedido-chat.png`
   - `beefood-web-react-manual/manuais/whatsapp-pedidos-chat/imagens-tratadas/04-whatsapp-iniciar.png`
   - `beefood-web-react-manual/manuais/whatsapp-pedidos-chat/imagens-tratadas/05-whatsapp-finalizar.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `whatsapp-pedidos-chat.md` exatamente como está (seções, textos e tabelas).
- Insira as 5 imagens na ordem acima, com as legendas da tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"**.
- Idioma **português do Brasil**, tom didático.
- Mantenha em destaque: o interruptor é **Pedido Chat** no BeeBot; WhatsApp precisa estar **conectado** para o cliente conversar; o bot usa o **mesmo cardápio** da loja; **1** confirma no resumo.
- **Mantenha a seção Perguntas frequentes inteira** (são as dúvidas de busca: pedido pelo WhatsApp sem cardápio, diferença da IA, atendente humano, entrega/retirada, preço, loja fechada, caixa de delivery).
- **Não** publique o rodapé "Referências internas" nem o `fluxo-codigo.md`.

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-beefood-whatsapp.png` | setas | WhatsApp → Abrir Conversas |
| 2 | `02-login-bot.png` | contexto | Login do BeeBot |
| 3 | `03-pedido-chat.png` | setas | Interruptor Pedido Chat |
| 4 | `04-whatsapp-iniciar.png` | contexto | Começar e escolher o produto |
| 5 | `05-whatsapp-finalizar.png` | contexto | Montar o lanche e o resumo |
