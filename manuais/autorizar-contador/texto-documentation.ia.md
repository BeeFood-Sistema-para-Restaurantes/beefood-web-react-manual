# texto-documentation.ia.md — #95 Autorizar o contador

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Fiscal**, adicione um manual chamado
**"Autorizar o contador"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/autorizar-contador/autorizar-contador.md`

2. **Imagens (use estas 7, nesta ordem):**
   - `beefood-web-react-manual/manuais/autorizar-contador/imagens-tratadas/01-aba-contadores.png`
   - `beefood-web-react-manual/manuais/autorizar-contador/imagens-tratadas/02-dialog-autorizar.png`
   - `beefood-web-react-manual/manuais/autorizar-contador/imagens-tratadas/06-email-primeiro-acesso.png`
   - `beefood-web-react-manual/manuais/autorizar-contador/imagens-tratadas/07-email-conta-existente.png`
   - `beefood-web-react-manual/manuais/autorizar-contador/imagens-tratadas/04-dialog-permissoes.png`
   - `beefood-web-react-manual/manuais/autorizar-contador/imagens-tratadas/03-menu-acoes.png`
   - `beefood-web-react-manual/manuais/autorizar-contador/imagens-tratadas/05-confirmar-encerrar.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `autorizar-contador.md` exatamente como está (seções, textos e tabelas).
- Insira as 7 imagens na ordem acima, com as legendas da tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"**.
- Idioma **português do Brasil**, tom didático.
- Use números normais (`1`, `2`, `3`) — não use ①②③.
- **Não** publique o rodapé "Referências internas".

A ordem das imagens no prompt segue o texto do `.md` (lista → autorizar → e-mails → permissões → menu → encerrar), não a numeração dos arquivos.

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|-------|----------------------------------|------|---------|
| 1 | `01-aba-contadores.png` | setas | Aba Contadores, com status e permissões |
| 2 | `02-dialog-autorizar.png` | setas | Formulário de autorizar, empresa inteira |
| 3 | `06-email-primeiro-acesso.png` | setas | E-mail com CRIAR MINHA SENHA |
| 4 | `07-email-conta-existente.png` | setas | E-mail com ACESSAR O PORTAL e 2 CNPJs |
| 5 | `04-dialog-permissoes.png` | setas | Alterar as três permissões |
| 6 | `03-menu-acoes.png` | setas | Menu da linha ativa |
| 7 | `05-confirmar-encerrar.png` | setas | Confirmação para encerrar o acesso |
