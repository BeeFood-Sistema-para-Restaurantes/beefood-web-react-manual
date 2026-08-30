# texto-documentation.ia.md — #65 Taxas das formas de recebimento

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Financeiro**, adicione um manual chamado
**"Taxas das formas de recebimento (faturado e realizado)"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/taxas-formas-pagamento/taxas-formas-pagamento.md`

2. **Imagens (use estas 9, nesta ordem):**
   - `beefood-web-react-manual/manuais/taxas-formas-pagamento/imagens-tratadas/01-formas-pagamento.png`
   - `beefood-web-react-manual/manuais/taxas-formas-pagamento/imagens-tratadas/02-debito-config.png`
   - `beefood-web-react-manual/manuais/taxas-formas-pagamento/imagens-tratadas/03-credito-config.png`
   - `beefood-web-react-manual/manuais/taxas-formas-pagamento/imagens-tratadas/04-vr-config.png`
   - `beefood-web-react-manual/manuais/taxas-formas-pagamento/imagens-tratadas/05-tabela-configurada.png`
   - `beefood-web-react-manual/manuais/taxas-formas-pagamento/imagens-tratadas/06-pdv-pago.png`
   - `beefood-web-react-manual/manuais/taxas-formas-pagamento/imagens-tratadas/07-detalhe-pagamento.png`
   - `beefood-web-react-manual/manuais/taxas-formas-pagamento/imagens-tratadas/08-desemp-recebimento.png`
   - `beefood-web-react-manual/manuais/taxas-formas-pagamento/imagens-tratadas/09-desemp-dados.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `taxas-formas-pagamento.md` exatamente como está (seções, textos e tabelas).
- Insira as 9 imagens na ordem acima, com as legendas da tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"**.
- Idioma **português do Brasil**, tom didático.
- Mantenha em destaque: a taxa é da **operadora** (não é desconto do cliente); uma venda em cada forma; débito **D+0** para ver faturado e realizado no mesmo dia; o relatório fica em **Desempenho → Vendas → Recebimento**; **SALVAR E SAIR (F2)**.
- **Não** publique o rodapé "Referências internas" nem o `fluxo-codigo.md`.

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-formas-pagamento.png` | setas | Financeiro → Formas Pagamento, bloco das vendas |
| 2 | `02-debito-config.png` | setas | Débito 2,50% e 0 dias |
| 3 | `03-credito-config.png` | setas | Crédito 3,49% e 30 dias |
| 4 | `04-vr-config.png` | setas | Vale Refeição 5% e 15 dias |
| 5 | `05-tabela-configurada.png` | setas | Crédito e débito na lista |
| 6 | `06-pdv-pago.png` | setas | Venda no crédito + lupa |
| 7 | `07-detalhe-pagamento.png` | setas | Taxa 3,49%, líquido e datas D+30 |
| 8 | `08-desemp-recebimento.png` | setas | Resumo do dia: débito e vale |
| 9 | `09-desemp-dados.png` | setas | Linhas do débito e do vale |
