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

2. **Imagens (use estas 13, nesta ordem):**
   - `beefood-web-react-manual/manuais/taxas-formas-pagamento/imagens-tratadas/01-formas-pagamento.png`
   - `beefood-web-react-manual/manuais/taxas-formas-pagamento/imagens-tratadas/02-debito-config.png`
   - `beefood-web-react-manual/manuais/taxas-formas-pagamento/imagens-tratadas/02b-debito-bandeiras.png`
   - `beefood-web-react-manual/manuais/taxas-formas-pagamento/imagens-tratadas/03-credito-config.png`
   - `beefood-web-react-manual/manuais/taxas-formas-pagamento/imagens-tratadas/04-vr-config.png`
   - `beefood-web-react-manual/manuais/taxas-formas-pagamento/imagens-tratadas/05-tabela-configurada.png`
   - `beefood-web-react-manual/manuais/taxas-formas-pagamento/imagens-tratadas/06-pdv-pago.png`
   - `beefood-web-react-manual/manuais/taxas-formas-pagamento/imagens-tratadas/07-detalhe-pagamento.png`
   - `beefood-web-react-manual/manuais/taxas-formas-pagamento/imagens-tratadas/07b-detalhe-mastercard.png`
   - `beefood-web-react-manual/manuais/taxas-formas-pagamento/imagens-tratadas/07c-detalhe-credito.png`
   - `beefood-web-react-manual/manuais/taxas-formas-pagamento/imagens-tratadas/07d-detalhe-vale.png`
   - `beefood-web-react-manual/manuais/taxas-formas-pagamento/imagens-tratadas/08-desemp-resumo.png`
   - `beefood-web-react-manual/manuais/taxas-formas-pagamento/imagens-tratadas/09-desemp-pagamentos.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `taxas-formas-pagamento.md` exatamente como está (seções, textos e tabelas).
- Insira as 13 imagens na ordem acima, com as legendas da tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"**.
- Idioma **português do Brasil**, tom didático.
- Mantenha em destaque: a taxa é da **operadora**; bandeira ativa precisa de taxa (senão vira fantasma); se a bandeira está configurada, **preencha a bandeira** na venda; débito **Visa 2,19%** (duas vendas) e **Mastercard 2,89%** no mesmo dia; o relatório fica em **Desempenho → Vendas → Resumo** com a data de hoje (não é Vendas → Recebimento); **SALVAR E SAIR (F2)**.
- **Não** publique o rodapé "Referências internas" nem o `fluxo-codigo.md`.

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-formas-pagamento.png` | setas | Financeiro → Formas Pagamento, bloco das vendas |
| 2 | `02-debito-config.png` | setas | Débito geral 2,50% e 0 dias |
| 3 | `02b-debito-bandeiras.png` | setas | Visa 2,19% e Mastercard 2,89% |
| 4 | `03-credito-config.png` | setas | Crédito 3,49% e 30 dias |
| 5 | `04-vr-config.png` | setas | Vale Refeição 5% e 15 dias |
| 6 | `05-tabela-configurada.png` | setas | Lista: Mastercard, Visa e geral |
| 7 | `06-pdv-pago.png` | setas | Venda débito Visa + lupa |
| 8 | `07-detalhe-pagamento.png` | setas | Visa 2,19%, líquido 13,69, D+0 |
| 9 | `07b-detalhe-mastercard.png` | setas | Mastercard 2,89%, líquido 13,60, D+0 |
| 10 | `07c-detalhe-credito.png` | setas | Crédito 3,49%, líquido 13,92, D+30 |
| 11 | `07d-detalhe-vale.png` | setas | Vale 5%, líquido 13,30, D+15 |
| 12 | `08-desemp-resumo.png` | setas | Vendas → Resumo: pago 183,26 × realizado 95,56 |
| 13 | `09-desemp-pagamentos.png` | setas | Débito, crédito e vale: faturado × realizado |
