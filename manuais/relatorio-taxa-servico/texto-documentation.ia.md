# texto-documentation.ia.md — Relatório de taxa de serviço

## PROMPT (copiar e colar)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `relatorio-taxa-servico.md`
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

Em **Desempenho**, adicione um item de menu por último chamado **Relatório de Taxa de
Serviço**.

Leia APENAS os arquivos abaixo:

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/relatorio-taxa-servico/relatorio-taxa-servico.md`
2. Imagens (nesta ordem):
   - `beefood-web-react-manual/manuais/relatorio-taxa-servico/imagens-tratadas/01-filtro-data.png`
   - `beefood-web-react-manual/manuais/relatorio-taxa-servico/imagens-tratadas/02-relatorio-taxa.png`
   - `beefood-web-react-manual/manuais/relatorio-taxa-servico/imagens-tratadas/03-produto-sem-taxa.png`
   - `beefood-web-react-manual/manuais/relatorio-taxa-servico/imagens-tratadas/04-detalhe-venda.png`
   - `beefood-web-react-manual/manuais/relatorio-taxa-servico/imagens-tratadas/05-caixa-resumo-taxa.png`

NÃO leia `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`.

- Apresentação IGUAL ao menu "Abrir Caixa".
- pt-BR. Manter a tabela **Taxa ≠ comissão** e o exemplo dos 4,2% da Ana.
- Linkar taxa obrigatória (#41), comissão cadastro (#83) e relatório de comissão (#84).
- Não publicar o rodapé interno.

## Estrutura da página

1. Taxa ≠ comissão
2. Filtre o dia
3. Ler o relatório
4. Produto sem taxa de serviço
5. Atalho no caixa: Resumo Presencial (só gerente)
6. Perguntas rápidas

## Anexo — legendas

| Ordem | Arquivo | Tipo | Legenda |
|-------|---------|------|---------|
| 1 | `01-filtro-data.png` | com setas | Calendário: isolar o dia |
| 2 | `02-relatorio-taxa.png` | com setas | KPIs e Taxa por Garçom |
| 3 | `03-produto-sem-taxa.png` | com setas | Switch Sem taxa de serviço |
| 4 | `04-detalhe-venda.png` | com setas | Venda da Ana, tipo % |
| 5 | `05-caixa-resumo-taxa.png` | com setas | Resumo Presencial: taxa por funcionário |
