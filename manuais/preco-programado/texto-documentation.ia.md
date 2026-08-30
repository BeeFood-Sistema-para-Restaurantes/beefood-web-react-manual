# texto-documentation.ia.md — #69 Preço Programado

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

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
