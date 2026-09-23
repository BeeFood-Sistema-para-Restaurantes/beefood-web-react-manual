# texto-documentation.ia.md — #60 Let's Express

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.

---

## PROMPT (copiar e colar)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `integracao-lets-express.md`
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

Crie um novo manual no app: em **Aplicativos** (seção **Entrega**), adicione um manual por último chamado **"Let's Express"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/integracao-lets-express/integracao-lets-express.md`

2. **Imagens (use estas 6, nesta ordem):**
   - `beefood-web-react-manual/manuais/integracao-lets-express/imagens-tratadas/01-aplicativos-lets-express.png`
   - `beefood-web-react-manual/manuais/integracao-lets-express/imagens-tratadas/02-modal-credenciais.png`
   - `beefood-web-react-manual/manuais/integracao-lets-express/imagens-tratadas/03-modal-sincronizacao.png`
   - `beefood-web-react-manual/manuais/integracao-lets-express/imagens-tratadas/04-adicionar-entregador.png`
   - `beefood-web-react-manual/manuais/integracao-lets-express/imagens-tratadas/05-modal-entregador.png`
   - `beefood-web-react-manual/manuais/integracao-lets-express/imagens-tratadas/06-modal-solicitar.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `integracao-lets-express.md` exatamente como está (seções, textos e tabelas).
- Insira as 6 imagens na ordem acima, com as legendas da tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"** (mesmo tamanho, posição, legenda e estilo).
- Idioma **português do Brasil**, tom didático (usuário final / restaurante).
- Mantenha em destaque: **Api Key** e **Empresa ID** obrigatórios; sincronização manual / PREPARO / PRONTO; filtro de origens; cancelar a Let's Express **não** cancela o pedido no BeeFood; **não há cotação** nesta integração.
- **Não** publique o rodapé "Referências internas" nem o `fluxo-codigo.md`.

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-aplicativos-lets-express.png` | setas | Aplicativos → Lets Express |
| 2 | `02-modal-credenciais.png` | setas | Api Key, Empresa ID e SALVAR |
| 3 | `03-modal-sincronizacao.png` | setas | PREPARO, minutos e origens |
| 4 | `04-adicionar-entregador.png` | setas | Adicionar Entregador |
| 5 | `05-modal-entregador.png` | setas | Escolher Lets Express |
| 6 | `06-modal-solicitar.png` | setas | Pagamento, retorno e CONFIRMAR |
