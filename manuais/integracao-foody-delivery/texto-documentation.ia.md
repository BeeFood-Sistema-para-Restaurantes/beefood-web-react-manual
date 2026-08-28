# texto-documentation.ia.md — #58 Foody Delivery

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Aplicativos** (seção **Entrega**), adicione um manual por último chamado **"Foody Delivery"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/integracao-foody-delivery/integracao-foody-delivery.md`

2. **Imagens (use estas 7, nesta ordem):**
   - `beefood-web-react-manual/manuais/integracao-foody-delivery/imagens-tratadas/01-foody-menu-apis.png`
   - `beefood-web-react-manual/manuais/integracao-foody-delivery/imagens-tratadas/02-foody-criar-token.png`
   - `beefood-web-react-manual/manuais/integracao-foody-delivery/imagens-tratadas/03-foody-criar-webhook.png`
   - `beefood-web-react-manual/manuais/integracao-foody-delivery/imagens-tratadas/04-aplicativos-foody.png`
   - `beefood-web-react-manual/manuais/integracao-foody-delivery/imagens-tratadas/05-modal-foody-config.png`
   - `beefood-web-react-manual/manuais/integracao-foody-delivery/imagens-tratadas/06-modal-foody-origens.png`
   - `beefood-web-react-manual/manuais/integracao-foody-delivery/imagens-tratadas/07-whatsapp-acompanhamento.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `integracao-foody-delivery.md` exatamente como está (seções, textos e tabelas).
- Insira as 7 imagens na ordem acima, com as legendas da tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"** (mesmo tamanho, posição, legenda e estilo).
- Idioma **português do Brasil**, tom didático (usuário final / restaurante).
- Mantenha em destaque: Token + Token Webhook + as três formas de sincronização + o filtro de origens. Contratação é com a Foody, não com o BeeFood.
- **Não** publique o rodapé "Referências internas" nem o `fluxo-codigo.md`.

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-foody-menu-apis.png` | contexto | Foody: Minha Conta → APIs e Hooks |
| 2 | `02-foody-criar-token.png` | contexto | Criar credencial API |
| 3 | `03-foody-criar-webhook.png` | contexto | Criar gatilho webhook |
| 4 | `04-aplicativos-foody.png` | setas | Aplicativos (1) → Foody Delivery (2) |
| 5 | `05-modal-foody-config.png` | setas | Token (1), Token Webhook (2), sync (3), Salvar (4) |
| 6 | `06-modal-foody-origens.png` | setas | PREPARO (1), Todas as origens (2), canais (3), Salvar (4) |
| 7 | `07-whatsapp-acompanhamento.png` | contexto | WhatsApp com link de acompanhamento |
