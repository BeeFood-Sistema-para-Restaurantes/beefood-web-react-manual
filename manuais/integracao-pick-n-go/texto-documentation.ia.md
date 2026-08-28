# texto-documentation.ia.md — #58 Pick n Go!

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Aplicativos** (seção **Entrega**), adicione um manual por último chamado **"Pick N Go!"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/integracao-pick-n-go/integracao-pick-n-go.md`

2. **Imagens (use estas 3, nesta ordem):**
   - `beefood-web-react-manual/manuais/integracao-pick-n-go/imagens-tratadas/01-aplicativos-pick-n-go.png`
   - `beefood-web-react-manual/manuais/integracao-pick-n-go/imagens-tratadas/02-modal-credenciais.png`
   - `beefood-web-react-manual/manuais/integracao-pick-n-go/imagens-tratadas/03-modal-origens.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `integracao-pick-n-go.md` exatamente como está (seções, textos e tabelas).
- Insira as 3 imagens na ordem acima, com as legendas da tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"** (mesmo tamanho, posição, legenda e estilo).
- Idioma **português do Brasil**, tom didático (usuário final / restaurante).
- Mantenha em destaque: App ID + App Key; uma opção de sincronização; filtro de origens no automático; frota própria pula a cotação; cancelar na lixeira **não** cancela o pedido no BeeFood.
- **Não** publique o rodapé "Referências internas" nem o `fluxo-codigo.md`.

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-aplicativos-pick-n-go.png` | setas | Aplicativos → Entrega → Pick N Go! |
| 2 | `02-modal-credenciais.png` | setas | Modal: App ID, App Key, sincronização, SALVAR E SAIR |
| 3 | `03-modal-origens.png` | setas | PREPARO + origens da sincronização automática |
