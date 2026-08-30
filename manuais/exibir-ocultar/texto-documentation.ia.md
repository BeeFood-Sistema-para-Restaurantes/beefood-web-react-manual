# texto-documentation.ia.md — #68 Exibir / Ocultar

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Cardápio**, adicione um manual chamado
**"Exibir e ocultar produtos"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/exibir-ocultar/exibir-ocultar.md`

2. **Imagens (use estas 4, nesta ordem):**
   - `beefood-web-react-manual/manuais/exibir-ocultar/imagens-tratadas/01-lista-exibir-ocultar.png`
   - `beefood-web-react-manual/manuais/exibir-ocultar/imagens-tratadas/02-modal-config.png`
   - `beefood-web-react-manual/manuais/exibir-ocultar/imagens-tratadas/03-modal-produtos.png`
   - `beefood-web-react-manual/manuais/exibir-ocultar/imagens-tratadas/04-cardapio-digital.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `exibir-ocultar.md` exatamente como está (seções, textos e tabelas).
- Insira as 4 imagens na ordem acima, com as legendas da tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"**.
- Idioma **português do Brasil**, tom didático.
- Mantenha em destaque: botão **Nova Tabela (F1)**; comportamento fixo **Ocultar Item**; canal **Cardápio Digital** obrigatório para a loja online; tabela sem dia = `0d` e não vale; aba Produtos **salva sozinha**; cache de **até 5 minutos**; Preço Programado e Rodízio são outras telas.
- **Não** publique o rodapé "Referências internas" nem o `fluxo-codigo.md`.

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-lista-exibir-ocultar.png` | setas | Lista + Nova Tabela + card do Brownie |
| 2 | `02-modal-config.png` | setas | Ocultar Item, canais e dias |
| 3 | `03-modal-produtos.png` | setas | Brownie na aba Produtos |
| 4 | `04-cardapio-digital.png` | setas | Cardápio: Brownie visível × oculto (dois celulares) |
