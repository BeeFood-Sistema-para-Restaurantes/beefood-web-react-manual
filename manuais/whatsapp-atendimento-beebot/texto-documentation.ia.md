# texto-documentation.ia.md — #91 Atender no BeeBot

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `whatsapp-atendimento-beebot.md`
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
**"Atender no BeeBot"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/whatsapp-atendimento-beebot/whatsapp-atendimento-beebot.md`

2. **Imagens (use estas 3, nesta ordem):**
   - `beefood-web-react-manual/manuais/whatsapp-atendimento-beebot/imagens-tratadas/01-inbox.png`
   - `beefood-web-react-manual/manuais/whatsapp-atendimento-beebot/imagens-tratadas/02-switches.png`
   - `beefood-web-react-manual/manuais/whatsapp-atendimento-beebot/imagens-tratadas/03-whatsapp-atendimento.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `whatsapp-atendimento-beebot.md` exatamente como está (seções, textos e tabelas).
- Insira as 3 imagens na ordem acima, com as legendas da tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"**.
- Idioma **português do Brasil**, tom didático.
- Use números normais (`1`, `2`, `3`) — não use ①②③.
- **Não** publique o rodapé "Referências internas".

---

## Anexo — legendas das imagens (na ordem)

| 1 | `01-inbox.png` | setas | Inbox + interruptores |
| 2 | `02-switches.png` | setas | Coluna Anti Banimento / Resposta / Pedido Chat |
| 3 | `03-whatsapp-atendimento.png` | contexto | Tira: humano + pedido assistido (fake) |
