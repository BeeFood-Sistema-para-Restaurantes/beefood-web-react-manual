# texto-documentation.ia.md — #15 Campanhas de WhatsApp

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `campanhas-whatsapp.md`
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

Crie um novo manual no app: em **Food Marketing**, adicione um manual chamado
**"Campanhas de WhatsApp"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/campanhas-whatsapp/campanhas-whatsapp.md`

2. **Imagens (use estas 7, nesta ordem):**
   - `beefood-web-react-manual/manuais/campanhas-whatsapp/imagens-tratadas/01-lista.png`
   - `beefood-web-react-manual/manuais/campanhas-whatsapp/imagens-tratadas/02-dropdown-filtro.png`
   - `beefood-web-react-manual/manuais/campanhas-whatsapp/imagens-tratadas/03-passo1-mensagem.png`
   - `beefood-web-react-manual/manuais/campanhas-whatsapp/imagens-tratadas/04-variacoes.png`
   - `beefood-web-react-manual/manuais/campanhas-whatsapp/imagens-tratadas/05-destinatarios.png`
   - `beefood-web-react-manual/manuais/campanhas-whatsapp/imagens-tratadas/06-resumo.png`
   - `beefood-web-react-manual/manuais/campanhas-whatsapp/imagens-tratadas/07-whatsapp-campanha.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `campanhas-whatsapp.md` exatamente como está (seções, textos e tabelas).
- Insira as 7 imagens na ordem acima, com as legendas da tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"**.
- Idioma **português do Brasil**, tom didático.
- Use números normais (`1`, `2`, `3`) — não use ①②③.
- **Não** publique o rodapé "Referências internas".

---

## Anexo — legendas das imagens (na ordem)

| 1 | `01-lista.png` | setas | Lista + Nova Campanha |
| 2 | `02-dropdown-filtro.png` | setas | RFV / filtro / segmentação |
| 3 | `03-passo1-mensagem.png` | setas | Passo Mensagem |
| 4 | `04-variacoes.png` | setas | Adicionar variação |
| 5 | `05-destinatarios.png` | setas | Lista (nomes borrados) |
| 6 | `06-resumo.png` | setas | Resumo + PUBLICAR |
| 7 | `07-whatsapp-campanha.png` | contexto | Celular (fake) |
