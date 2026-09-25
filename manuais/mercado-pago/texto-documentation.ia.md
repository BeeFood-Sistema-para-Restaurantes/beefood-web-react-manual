# texto-documentation.ia.md — #56 Mercado Pago (cartão no cardápio)

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `mercado-pago.md`
  e das imagens listados neste prompt.
- **Não publique**, em nenhuma seção: rota ou URL de API (`/api/...`); nome de campo,
  de arquivo, de componente, de tabela ou de coluna; bloco de código, JSON ou
  `campo=true`; nem as palavras *backend*, *endpoint*, *payload*, *array*, *bundle*.
  Se a frase só faz sentido para quem programa, ela não entra. Única exceção: a URL
  completa de webhook que o lojista copia para o painel do parceiro.
- Se você leu **qualquer outro arquivo** desta pasta — `fluxo-codigo.md`,
  `MEMORIA.md`, `annotate.py`, `capturar.py` —, **descarte o que leu**: são anotações
  internas de quem produziu o manual.
- Em 23/09/2026 uma página publicada saiu com a rota da API do cupom e dois nomes de
  campo do cashback, porque esta regra não estava aqui em cima.

Crie um novo manual no app: em **Aplicativos** (seção **Pagamento Online**), adicione um manual por último chamado **"Mercado Pago"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/mercado-pago/mercado-pago.md`

2. **Imagens (use estas 8, nesta ordem):**
   - `beefood-web-react-manual/manuais/mercado-pago/imagens-tratadas/01-mp-criar-aplicativo.png`
   - `beefood-web-react-manual/manuais/mercado-pago/imagens-tratadas/02-mp-preencher-app.png`
   - `beefood-web-react-manual/manuais/mercado-pago/imagens-tratadas/03-mp-ativar-credenciais.png`
   - `beefood-web-react-manual/manuais/mercado-pago/imagens-tratadas/04-mp-formulario-industria.png`
   - `beefood-web-react-manual/manuais/mercado-pago/imagens-tratadas/05-mp-credenciais-producao.png`
   - `beefood-web-react-manual/manuais/mercado-pago/imagens-tratadas/06-mp-copiar-chaves.png`
   - `beefood-web-react-manual/manuais/mercado-pago/imagens-tratadas/07-beefood-aplicativos.png`
   - `beefood-web-react-manual/manuais/mercado-pago/imagens-tratadas/09-beefood-modal-chaves.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `mercado-pago.md` exatamente como está (seções, textos e tabelas).
- Insira as 8 imagens na ordem acima, com as legendas indicadas na tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"** (mesmo tamanho, posição, legenda e estilo).
- Idioma **português do Brasil**, tom didático (usuário final / restaurante).
- Mantenha em destaque: Public Key + Access Token de produção + switch Habilitar Cartão de Crédito. NÃO testar com o próprio cartão.
- **Não** publique o rodapé "Referências internas" nem o `fluxo-codigo.md`.

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-mp-criar-aplicativo.png` | contexto | Criar aplicativo no MP |
| 2 | `02-mp-preencher-app.png` | contexto | Preencher aplicativo |
| 3 | `03-mp-ativar-credenciais.png` | contexto | Ativar credenciais |
| 4 | `04-mp-formulario-industria.png` | contexto | Indústria e site |
| 5 | `05-mp-credenciais-producao.png` | contexto | Credenciais de produção |
| 6 | `06-mp-copiar-chaves.png` | contexto | Copiar Public Key e Access Token |
| 7 | `07-beefood-aplicativos.png` | setas | Aplicativos (1) → Mercado Pago (2) |
| 8 | `09-beefood-modal-chaves.png` | setas | Public Key (1), Access Token (2), switch (3), Salvar (4) |
