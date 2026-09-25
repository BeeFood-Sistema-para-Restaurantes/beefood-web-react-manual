# texto-documentation.ia.md — Relatório de comissão do garçom

## PROMPT (copiar e colar)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `relatorio-comissao-garcom.md`
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

Em **Desempenho**, adicione um item de menu por último chamado **Relatório de Comissão
do Garçom**.

Leia APENAS os arquivos abaixo:

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/relatorio-comissao-garcom/relatorio-comissao-garcom.md`
2. Imagens (nesta ordem):
   - `beefood-web-react-manual/manuais/relatorio-comissao-garcom/imagens-tratadas/01-filtro-data.png`
   - `beefood-web-react-manual/manuais/relatorio-comissao-garcom/imagens-tratadas/02-relatorio-comissao.png`
   - `beefood-web-react-manual/manuais/relatorio-comissao-garcom/imagens-tratadas/03-detalhe-itens.png`
   - `beefood-web-react-manual/manuais/relatorio-comissao-garcom/imagens-tratadas/04-caixa-resumo-comissao.png`

NÃO leia `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`.

- Apresentação das imagens IGUAL ao menu "Abrir Caixa".
- pt-BR. Manter: Mobile no título não significa “só app”; filtrar o dia; RECEBIDO;
  Resumo Presencial como atalho (taxa lista Ana/Bruno; Comissão Garçom no teste
  não listou as vendas web — fechamento fino no Desempenho).
- Linkar o cadastro (#83) e o relatório de taxa (#85).
- Não publicar o rodapé interno.

## Estrutura da página

1. Onde fica
2. Filtre o dia
3. Ler o relatório (KPIs, por garçom, itens)
4. Atalho no caixa: Resumo Presencial
5. Perguntas rápidas

## Anexo — legendas

| Ordem | Arquivo | Tipo | Legenda |
|-------|---------|------|---------|
| 1 | `01-filtro-data.png` | com setas | Calendário: não deixar 30 dias |
| 2 | `02-relatorio-comissao.png` | com setas | KPIs e Comissão por Garçom |
| 3 | `03-detalhe-itens.png` | com setas | Itens da Ana, R$ e % |
| 4 | `04-caixa-resumo-comissao.png` | com setas | Resumo Presencial do caixa |
