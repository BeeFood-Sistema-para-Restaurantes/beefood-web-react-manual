# texto-documentation.ia.md — #21 Cupom de Desconto

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `cupom-desconto.md`
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

Crie um novo manual no app: em **Fidelidade (CRM)**, adicione um manual chamado
**"Cupom de Desconto"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/cupom-desconto/cupom-desconto.md`

2. **Imagens (use estas 6, nesta ordem):**
   - `beefood-web-react-manual/manuais/cupom-desconto/imagens-tratadas/01-lista-cupons.png`
   - `beefood-web-react-manual/manuais/cupom-desconto/imagens-tratadas/02-modal-novo-topo.png`
   - `beefood-web-react-manual/manuais/cupom-desconto/imagens-tratadas/03-modal-novo-regras.png`
   - `beefood-web-react-manual/manuais/cupom-desconto/imagens-tratadas/04-modal-avancado.png`
   - `beefood-web-react-manual/manuais/cupom-desconto/imagens-tratadas/05-cardapio-banner.png`
   - `beefood-web-react-manual/manuais/cupom-desconto/imagens-tratadas/06-cardapio-lista-cupons.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `cupom-desconto.md` exatamente como está (seções, textos e tabelas).
- Insira as 6 imagens na ordem acima, com as legendas indicadas na tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"** (mesmo tamanho, posição, legenda e estilo).
- Idioma **português do Brasil**, tom didático (usuário final / restaurante).
- Mantenha em destaque: a diferença **libera o cupom** vs **recebe o desconto**; a aba Promoções do cardápio **não** é lista de cupom; SMS só no cardápio/totem.
- **Não** publique o rodapé "Referências internas" nem o `fluxo-codigo.md`.

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-lista-cupons.png` | setas | Menu CRM + Adicionar Cupom |
| 2 | `02-modal-novo-topo.png` | setas | Código, tipo, valor, validade, dias |
| 3 | `03-modal-novo-regras.png` | setas | Canais, regras, SMS |
| 4 | `04-modal-avancado.png` | setas | Formas de pagamento + três modos |
| 5 | `05-cardapio-banner.png` | setas | Faixa de cupons no cardápio |
| 6 | `06-cardapio-lista-cupons.png` | setas | Campo do código secreto + lista dos visíveis |
