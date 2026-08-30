# texto-documentation.ia.md — #67 Lançamentos: contas a receber

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Financeiro**, adicione um manual chamado
**"Lançamentos: contas a receber"**. Coloque-o logo depois de
**"Lançamentos: contas a pagar"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/lancamentos-contas-receber/lancamentos-contas-receber.md`

2. **Imagens (use estas 5, nesta ordem):**
   - `beefood-web-react-manual/manuais/lancamentos-contas-receber/imagens-tratadas/01-receber-vendas.png`
   - `beefood-web-react-manual/manuais/lancamentos-contas-receber/imagens-tratadas/02-detalhe-venda.png`
   - `beefood-web-react-manual/manuais/lancamentos-contas-receber/imagens-tratadas/03-receita-extra.png`
   - `beefood-web-react-manual/manuais/lancamentos-contas-receber/imagens-tratadas/04-lista-receita.png`
   - `beefood-web-react-manual/manuais/lancamentos-contas-receber/imagens-tratadas/05-todos.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `lancamentos-contas-receber.md` exatamente como está (seções, textos e tabelas).
- Insira as 5 imagens na ordem acima, com as legendas da tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"**.
- Idioma **português do Brasil**, tom didático.
- Mantenha em destaque: a venda paga **já** vira receber no **líquido**; receita extra usa categoria **Outras Receitas**; a forma da receita extra é a do **topo** de Formas Pagamento; aba **Todos** junta pagar e receber.
- **Não** publique o rodapé "Referências internas" nem o `fluxo-codigo.md`.

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-receber-vendas.png` | setas | Aba Contas a receber: venda #915 no líquido |
| 2 | `02-detalhe-venda.png` | setas | Original 14,00, líquido 13,69, taxa 2,19% |
| 3 | `03-receita-extra.png` | setas | Patrocínio R$ 200 no Pix, Outras Receitas |
| 4 | `04-lista-receita.png` | setas | Patrocínio recebido na lista |
| 5 | `05-todos.png` | setas | Todos lançamentos filtrado por Aluguel |
