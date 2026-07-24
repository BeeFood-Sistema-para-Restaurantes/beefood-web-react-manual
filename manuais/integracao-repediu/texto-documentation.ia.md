# texto-documentation.ia.md — Integração Repediu

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.
> O projeto do manual **já está anexo no contexto** — o prompt aponta os **arquivos exatos** a ler.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Aplicativos** (seção **Marketing e CRM / Integrações**), adicione um
manual por último chamado **"Integração Repediu"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/integracao-repediu/integracao-repediu.md`

2. **Imagens (use estas 10, nesta ordem):**
   - `beefood-web-react-manual/manuais/integracao-repediu/imagens-tratadas/01-repediu-integracoes-beefood.png`
   - `beefood-web-react-manual/manuais/integracao-repediu/imagens-tratadas/02-repediu-credenciais-vendas.png`
   - `beefood-web-react-manual/manuais/integracao-repediu/imagens-tratadas/03-repediu-analytics-cards.png`
   - `beefood-web-react-manual/manuais/integracao-repediu/imagens-tratadas/04-repediu-writekey-gerar.png`
   - `beefood-web-react-manual/manuais/integracao-repediu/imagens-tratadas/05-repediu-writekey-gerada.png`
   - `beefood-web-react-manual/manuais/integracao-repediu/imagens-tratadas/06-beefood-aplicativos-repediu.png`
   - `beefood-web-react-manual/manuais/integracao-repediu/imagens-tratadas/07-beefood-repediu-modal-status.png`
   - `beefood-web-react-manual/manuais/integracao-repediu/imagens-tratadas/08-beefood-form-configurar.png`
   - `beefood-web-react-manual/manuais/integracao-repediu/imagens-tratadas/09-beefood-form-preenchido.png`
   - `beefood-web-react-manual/manuais/integracao-repediu/imagens-tratadas/10-beefood-repediu-ativo.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `integracao-repediu.md` exatamente como está (seções, textos e tabelas).
- Insira as 10 imagens na ordem acima, com as legendas indicadas na tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"** (mesmo tamanho, posição, legenda e estilo).
- Idioma **português do Brasil**, tom didático (usuário final / restaurante).
- Mantenha em destaque: são **duas credenciais** geradas em **dois lugares** do Repediu (Integrações →
  Client ID/Secret; Web/App Analytics → Write Key); o Tracker de Vendas precisa dos **dois** campos ou
  nenhum; o Tracker de Cardápio Digital é **independente**; **redefinir** a Write Key invalida a antiga.
- **Não** publique o rodapé "Referências internas" nem o `fluxo-codigo.md`.

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-repediu-integracoes-beefood.png` | com setas | Repediu → Integrações → card **BeeFood** → **Habilitado** |
| 2 | `02-repediu-credenciais-vendas.png` | com setas | **client_id** (1) e **client_secret** (2) |
| 3 | `03-repediu-analytics-cards.png` | com setas | Web/App Analytics → Configuração → card **BeeFood** → **Habilitar** |
| 4 | `04-repediu-writekey-gerar.png` | com setas | Modal Chave de escrita → **Gerar chave** |
| 5 | `05-repediu-writekey-gerada.png` | com setas | **Write key** (1) + **Copiar** (2) |
| 6 | `06-beefood-aplicativos-repediu.png` | com setas | BeeFood → **Aplicativos** (1) → card **Repediu** (2) |
| 7 | `07-beefood-repediu-modal-status.png` | com setas | Status (1) + botão **Configurar** (2) |
| 8 | `08-beefood-form-configurar.png` | contexto | Formulário com os dois trackers |
| 9 | `09-beefood-form-preenchido.png` | com setas | Client ID (1), Client Secret (2), Write Key (3), **SALVAR** (4) |
| 10 | `10-beefood-repediu-ativo.png` | com setas | **Tracker de Vendas ativo** (1) e **Cardápio Digital ativo** (2) |
