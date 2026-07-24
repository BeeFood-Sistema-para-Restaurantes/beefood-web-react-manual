# texto-documentation.ia.md — Integração FoodCRM

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.
> O projeto do manual **já está anexo no contexto** — o prompt aponta os **arquivos exatos** a ler.

---

## PROMPT (copiar e colar)

Crie um novo manual no app: em **Aplicativos** (seção **Marketing e CRM / Integrações**), adicione um
manual por último chamado **"Integração FoodCRM"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/integracao-foodcrm/integracao-foodcrm.md`

2. **Imagens (use estas 6, nesta ordem):**
   - `beefood-web-react-manual/manuais/integracao-foodcrm/imagens-tratadas/01-foodcrm-integracoes.png`
   - `beefood-web-react-manual/manuais/integracao-foodcrm/imagens-tratadas/02-foodcrm-api-token.png`
   - `beefood-web-react-manual/manuais/integracao-foodcrm/imagens-tratadas/03-beefood-aplicativos-card.png`
   - `beefood-web-react-manual/manuais/integracao-foodcrm/imagens-tratadas/04-beefood-modal-cardapios.png`
   - `beefood-web-react-manual/manuais/integracao-foodcrm/imagens-tratadas/05-beefood-modal-apikey.png`
   - `beefood-web-react-manual/manuais/integracao-foodcrm/imagens-tratadas/06-beefood-ativo.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `integracao-foodcrm.md` exatamente como está (seções, textos e tabelas).
- Insira as 6 imagens na ordem acima, com as legendas indicadas na tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"** (mesmo tamanho, posição, legenda e estilo).
- Idioma **português do Brasil**, tom didático (usuário final / restaurante).
- Mantenha em destaque: é **uma única credencial** (a **API Key / Token** `fcrm_...` gerada no FoodCRM →
  Integrações → **Acessar a documentação**); a configuração é **por cardápio**; o envio das vendas é
  **automático e diário (madrugada)**; **gerar novo token** invalida a chave antiga; o **Código da loja
  não é necessário** no BeeFood.
- **Não** publique o rodapé "Referências internas" nem o `fluxo-codigo.md`.

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-foodcrm-integracoes.png` | com setas | FoodCRM → **Integrações** (1) → botão **Acessar a documentação** (2) |
| 2 | `02-foodcrm-api-token.png` | com setas | Painel **API de integração** → **API Key / Token** (1) + **Copiar** (2) |
| 3 | `03-beefood-aplicativos-card.png` | com setas | BeeFood → **Aplicativos** (1) → card **FoodCRM** (2) |
| 4 | `04-beefood-modal-cardapios.png` | com setas | Status do cardápio (1) + botão **+ Adicionar** (2) |
| 5 | `05-beefood-modal-apikey.png` | com setas | **API key** (1) + **Ativo** (2) + **SALVAR (F2)** (3) |
| 6 | `06-beefood-ativo.png` | com setas | Cardápio com status **Ativo** (1) + botão **Editar** (2) |
