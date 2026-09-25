# texto-documentation.ia.md — #69 Preço Programado

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `preco-programado.md`
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

Crie um novo manual no app: em **Cardápio**, adicione um manual chamado
**"Preço programado"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/preco-programado/preco-programado.md`

2. **Imagens (use estas 4, nesta ordem):**
   - `beefood-web-react-manual/manuais/preco-programado/imagens-tratadas/01-lista-preco-programado.png`
   - `beefood-web-react-manual/manuais/preco-programado/imagens-tratadas/02-modal-config.png`
   - `beefood-web-react-manual/manuais/preco-programado/imagens-tratadas/03-modal-produtos.png`
   - `beefood-web-react-manual/manuais/preco-programado/imagens-tratadas/04-cardapio-digital.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `preco-programado.md` exatamente como está (seções, textos e tabelas).
- Insira as 4 imagens na ordem acima, com as legendas da tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"**.
- Idioma **português do Brasil**, tom didático.
- Mantenha em destaque: botão **Novo Preço Programado (F1)**; comportamento fixo **Alterar Preço**; desconto só depois de **selecionar** o produto; **APLICAR** no modal de desconto e **SALVAR** no modal pai; canal **Cardápio Digital**; tabela sem dia = `0d`; cache de **até 5 minutos**; Exibir/Ocultar e Rodízio são outras telas.
- **Não** publique o rodapé "Referências internas" nem o `fluxo-codigo.md`.

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-lista-preco-programado.png` | setas | Lista + Novo Preço + card Happy hour |
| 2 | `02-modal-config.png` | setas | Alterar Preço, canais e dias |
| 3 | `03-modal-produtos.png` | setas | Milk Shake 20% / R$ 15,12 |
| 4 | `04-cardapio-digital.png` | setas | Cardápio: 15,12 \| 18,90 \| −20% |
