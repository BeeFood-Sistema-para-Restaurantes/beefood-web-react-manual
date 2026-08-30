# texto-documentation.ia.md — #66 Lançamentos: contas a pagar

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Financeiro**, adicione um manual chamado
**"Lançamentos: contas a pagar"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/lancamentos-contas-pagar/lancamentos-contas-pagar.md`

2. **Imagens (use estas 8, nesta ordem):**
   - `beefood-web-react-manual/manuais/lancamentos-contas-pagar/imagens-tratadas/01-menu-lancamentos.png`
   - `beefood-web-react-manual/manuais/lancamentos-contas-pagar/imagens-tratadas/02-novo-dropdown.png`
   - `beefood-web-react-manual/manuais/lancamentos-contas-pagar/imagens-tratadas/03-despesa-unico.png`
   - `beefood-web-react-manual/manuais/lancamentos-contas-pagar/imagens-tratadas/04-lista-a-vencer.png`
   - `beefood-web-react-manual/manuais/lancamentos-contas-pagar/imagens-tratadas/05-confirmar-pago.png`
   - `beefood-web-react-manual/manuais/lancamentos-contas-pagar/imagens-tratadas/06-lista-pago.png`
   - `beefood-web-react-manual/manuais/lancamentos-contas-pagar/imagens-tratadas/07-despesa-parcelado.png`
   - `beefood-web-react-manual/manuais/lancamentos-contas-pagar/imagens-tratadas/08-lista-parcelas.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `lancamentos-contas-pagar.md` exatamente como está (seções, textos e tabelas).
- Insira as 8 imagens na ordem acima, com as legendas da tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"**.
- Idioma **português do Brasil**, tom didático.
- Mantenha em destaque: a forma é a do **topo** de Formas Pagamento; **Conta** e categoria são opcionais; parcelado usa **Valor Parcela** e a 2ª cai no mês seguinte; **SALVAR (F2)** e o **cifrão** para quitar.
- **Não** publique o rodapé "Referências internas" nem o `fluxo-codigo.md`.

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-menu-lancamentos.png` | setas | Financeiro → Lançamentos, aba Contas a pagar |
| 2 | `02-novo-dropdown.png` | setas | Novo: Despesa ou Receita |
| 3 | `03-despesa-unico.png` | setas | Aluguel R$ 800 no Pix |
| 4 | `04-lista-a-vencer.png` | setas | Aluguel em Vencem hoje + cifrão |
| 5 | `05-confirmar-pago.png` | setas | Confirmar Pagamento |
| 6 | `06-lista-pago.png` | setas | Aluguel marcado como Pago |
| 7 | `07-despesa-parcelado.png` | setas | Máquina de café 2× R$ 150 no Boleto |
| 8 | `08-lista-parcelas.png` | setas | Parcela 1/2 no mês e aluguel pago |
