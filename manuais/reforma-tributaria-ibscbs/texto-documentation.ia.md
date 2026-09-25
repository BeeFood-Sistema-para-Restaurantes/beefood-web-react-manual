# texto-documentation.ia.md — Reforma Tributária (IBS/CBS)

> **O que é este arquivo:** o **texto pronto** (prompt) para colar no construtor de documentação
> do app e gerar o manual na interface do BeeFood. Copie o bloco abaixo da linha `---` e cole.
> O projeto do manual **já está anexo no contexto** — o prompt aponta os **arquivos exatos** a ler.

---

## PROMPT (copiar e colar)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `reforma-tributaria-ibscbs.md`
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

Crie um novo manual no app: em **Fiscal**, adicione um **item de menu por último** chamado **"Reforma Tributária"**.

**Leia APENAS os arquivos abaixo (não varra o resto do projeto):**

1. **Conteúdo do manual (use na íntegra):**
   `beefood-web-react-manual/manuais/reforma-tributaria-ibscbs/reforma-tributaria.md`

2. **Imagens (use estas 8, nesta ordem):**
   - `beefood-web-react-manual/manuais/reforma-tributaria-ibscbs/imagens-tratadas/01-edicao-fiscal-grade.png`
   - `beefood-web-react-manual/manuais/reforma-tributaria-ibscbs/imagens-tratadas/02-grupos-colunas-ibscbs.png`
   - `beefood-web-react-manual/manuais/reforma-tributaria-ibscbs/imagens-tratadas/03-colunas-ibscbs-grade.png`
   - `beefood-web-react-manual/manuais/reforma-tributaria-ibscbs/imagens-tratadas/04-produto-selecionado-editar-impostos.png`
   - `beefood-web-react-manual/manuais/reforma-tributaria-ibscbs/imagens-tratadas/07-cst-catalogo-carregado.png`
   - `beefood-web-react-manual/manuais/reforma-tributaria-ibscbs/imagens-tratadas/08-modal-preenchido.png`
   - `beefood-web-react-manual/manuais/reforma-tributaria-ibscbs/imagens-tratadas/09-revisar-alteracoes.png`
   - `beefood-web-react-manual/manuais/reforma-tributaria-ibscbs/imagens-tratadas/10-concluido.png`

**NÃO leia** outros arquivos do projeto (ex.: `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

**Como montar a página:**
- Use o conteúdo do `reforma-tributaria.md` exatamente como está (seções, textos e tabelas "Nº da seta → campo").
- Insira as 8 imagens na ordem acima, com as legendas indicadas na tabela no fim deste arquivo.
- **Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa"** (mesmo tamanho, posição, legenda e estilo).
- Idioma **português do Brasil**, tom didático (usuário final).
- Mantenha em destaque: a tela é **somente desktop**; editar **grava no produto mas não emite nota** (reversível); o exemplo de nota é **fictício**.
- **Não** publique o rodapé "Referências internas" do `.md`.

---

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|------:|----------------------------------|------|---------|
| 1 | `01-edicao-fiscal-grade.png` | contexto | Tela **Edição Fiscal** (planilha de produtos) |
| 2 | `02-grupos-colunas-ibscbs.png` | contexto | Ativando o grupo de colunas **"IBS/CBS (Reforma)"** |
| 3 | `03-colunas-ibscbs-grade.png` | contexto | Colunas de IBS/CBS visíveis na planilha |
| 4 | `04-produto-selecionado-editar-impostos.png` | com setas | ① marcar produto · ② botão **EDITAR IMPOSTOS** |
| 5 | `07-cst-catalogo-carregado.png` | com setas | ① busca de CST · ② opção **000 – Tributação integral** |
| 6 | `08-modal-preenchido.png` | com setas | ① CST IBS/CBS · ② cClassTrib · ③ Alíq. IBS UF · ④ Alíq. CBS · ⑤ **PRÓXIMO** |
| 7 | `09-revisar-alteracoes.png` | com setas | ① alterações a aplicar · ② **CONFIRMAR (F2)** |
| 8 | `10-concluido.png` | contexto | Tela **"Concluído! 1 produto atualizado"** |
