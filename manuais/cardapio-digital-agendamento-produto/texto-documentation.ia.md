# texto-documentation.ia.md — #73 Produto só com agendamento (encomenda)

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Cardápio Digital**, adicione um manual chamado
**"Produto só com agendamento (encomenda)"**, logo depois de
**"Agendamento do cardápio digital"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/cardapio-digital-agendamento-produto/cardapio-digital-agendamento-produto.md`

2. **Imagens (use estas 8, nesta ordem):**
   - `beefood-web-react-manual/manuais/cardapio-digital-agendamento-produto/imagens-tratadas/01-lista-antes.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-agendamento-produto/imagens-tratadas/02-lote-selecao.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-agendamento-produto/imagens-tratadas/03-lote-campo.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-agendamento-produto/imagens-tratadas/04-lote-resultado.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-agendamento-produto/imagens-tratadas/05-lista-depois.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-agendamento-produto/imagens-tratadas/06-produto-switch.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-agendamento-produto/imagens-tratadas/07-par-encomenda.png`
   - `beefood-web-react-manual/manuais/cardapio-digital-agendamento-produto/imagens-tratadas/08-cardapio-digital.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `cardapio-digital-agendamento-produto.md` exatamente como está (seções, textos e tabelas).
- Insira as 8 imagens na ordem acima, com as legendas da tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"**.
- Idioma **português do Brasil**, tom didático.
- Mantenha em destaque: filtrar o setor **antes** de abrir o Editar em Lote; o valor **Sim / Não** do campo (é por ele que se desfaz); o **SALVAR E SAIR** do cadastro individual; a etiqueta **Encomenda** no cardápio; o **Continuar** que abre o **AGENDAR PEDIDO** mesmo com **Hoje** marcado; e o aviso de que sem o **Agendamento** da aba ligado a marca não segura o pedido.
- Aponte o manual **"Agendamento do cardápio digital"** como leitura complementar.
- **Não** publique o rodapé "Referências internas" nem o `fluxo-codigo.md`.

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-lista-antes.png` | setas | Setor Sobremesas filtrado e o botão Editar em Lote |
| 2 | `02-lote-selecao.png` | setas | Etapa 1: três pudins marcados, Brownie de fora |
| 3 | `03-lote-campo.png` | setas | Etapa 2: Somente Agendamento em Sim |
| 4 | `04-lote-resultado.png` | setas | Etapa 3: 3 de 3 produtos, 3 sucesso |
| 5 | `05-lista-depois.png` | setas | Ícone de calendário nos pudins; Brownie sem |
| 6 | `06-produto-switch.png` | setas | Cadastro do produto: Opções avançadas e o switch |
| 7 | `07-par-encomenda.png` | par | Painel: Sim → cardápio: etiqueta Encomenda |
| 8 | `08-cardapio-digital.png` | setas | Cardápio no celular: etiqueta, explicação e AGENDAR PEDIDO |
