# texto-documentation.ia.md — #20 Cashback operar

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Fidelidade (CRM)**, adicione um manual chamado
**"Cashback — operar no dia a dia"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/cashback-operar/cashback-operar.md`

2. **Imagens (use estas 9, nesta ordem):**
   - `beefood-web-react-manual/manuais/cashback-operar/imagens-tratadas/01-historico.png`
   - `beefood-web-react-manual/manuais/cashback-operar/imagens-tratadas/02-saldo-clientes.png`
   - `beefood-web-react-manual/manuais/cashback-operar/imagens-tratadas/03-detalhe-cliente.png`
   - `beefood-web-react-manual/manuais/cashback-operar/imagens-tratadas/04-modal-ajuste.png`
   - `beefood-web-react-manual/manuais/cashback-operar/imagens-tratadas/05-modal-remover.png`
   - `beefood-web-react-manual/manuais/cashback-operar/imagens-tratadas/06-fila-processamento.png`
   - `beefood-web-react-manual/manuais/cashback-operar/imagens-tratadas/07-pdv-usar-cashback.png`
   - `beefood-web-react-manual/manuais/cashback-operar/imagens-tratadas/08-pdv-modal-aplicar.png`
   - `beefood-web-react-manual/manuais/cashback-operar/imagens-tratadas/09-cardapio-checkout.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `cashback-operar.md` exatamente como está (seções, textos e tabelas).
- Insira as 9 imagens na ordem acima, com as legendas da tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"**.
- Idioma **português do Brasil**, tom didático.
- Mantenha em destaque: **Adicionar** e **Remover** saldo com **motivo**; fila só de **madrugada**; **Usar cashback** some sem cliente; telefone de teste **(15) 99999-8888**.
- **Não** publique o rodapé "Referências internas" nem o `fluxo-codigo.md`.

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-historico.png` | setas | Histórico filtrado pelo telefone de teste |
| 2 | `02-saldo-clientes.png` | setas | Busca pelo telefone de teste |
| 3 | `03-detalhe-cliente.png` | setas | Extrato e botões Adicionar / Remover |
| 4 | `04-modal-ajuste.png` | setas | Adicionar saldo (valor + motivo) |
| 5 | `05-modal-remover.png` | setas | Remover saldo (valor + motivo) |
| 6 | `06-fila-processamento.png` | setas | Fila da madrugada |
| 7 | `07-pdv-usar-cashback.png` | setas | Botão no pagamento do PDV |
| 8 | `08-pdv-modal-aplicar.png` | setas | Modal Usar Cashback |
| 9 | `09-cardapio-checkout.png` | setas | Cardápio: saldo + uso na sacola (dois celulares) |
