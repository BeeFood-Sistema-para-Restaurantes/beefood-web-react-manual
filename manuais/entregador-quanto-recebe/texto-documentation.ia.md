# texto-documentation.ia.md — Quanto o entregador recebe

## PROMPT (copiar e colar)

Dentro do menu **Gestão de Entregas**, crie a página
**Quanto o entregador recebe: taxa, valor, diária e KM**.

Leia APENAS os arquivos abaixo:

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/entregador-quanto-recebe/entregador-quanto-recebe.md`
2. Imagens (nesta ordem):
   - `.../imagens-tratadas/01-area-grupo.png`
   - `.../imagens-tratadas/02-grupo-valores.png`
   - `.../imagens-tratadas/04-pedido-sem-valor.png`
   - `.../imagens-tratadas/05-pedido-editando.png`
   - `.../imagens-tratadas/06-pedido-com-valor.png`
   - `.../imagens-tratadas/03-funcionario-diaria-km.png`
   - `.../imagens-tratadas/07a-cabecalho.png`
   - `.../imagens-tratadas/07b-cartoes.png`
   - `.../imagens-tratadas/07c-resumo.png`
   - `.../imagens-tratadas/08-modo-area.png`
   - `.../imagens-tratadas/09-modo-km.png`
   - `.../imagens-tratadas/10-ida-e-volta.png`
   - `.../imagens-tratadas/11-todos-os-detalhes.png`
   - `.../imagens-tratadas/12-detalhe-entregador.png`

NÃO leia `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`, `*.geo.json`.

- Apresentação IGUAL ao menu "Abrir Caixa".
- pt-BR, didático. Manter as tabelas de setas (nº → onde → o que é) embaixo de cada imagem.
- **Manter a tabela de abertura** com os dois valores (taxa do cliente × valor do entregador):
  é o que evita o erro mais comum do assunto.
- Avisar, no começo, que a **Gestão de Entregas está em liberação**. Não citar `empresaID`.
- Manter, sem enxugar, os avisos que mudam o resultado na prática:
  (a) o valor do entregador **entra no pedido na hora do cálculo do endereço** — mudar a área
  não mexe no histórico;
  (b) **é o valor do pedido que manda**, e por isso o lápis no pedido existe;
  (c) **o valor do entregador não aparece para o cliente**;
  (d) **diária e valor por KM não fazem nada sozinhos** — servem ao relatório;
  (e) a coluna **KM (Ida)** mostra **dinheiro**, não distância;
  (f) **a diária é somada por cima** em qualquer modo, e é contada por dia com entrega;
  (g) o período precisa de **Confirmar**;
  (h) pedido que aparece em **Sem entregador** não entra na conta de ninguém.
- Não publicar rotas de API, nomes de tabela, nomes de coluna de banco, `localStorage`, nomes de
  componente nem nomes de arquivo. Em especial: **não citar** que o valor é gravado numa coluna
  de taxa de serviço.
- Não citar Delphi, relatório antigo nem limite de 999,99 do campo.
- Não citar o `cenario.js` nem nada de bastidor de captura.

## Estrutura da página (mesma numeração do `.md`)

- (abertura com a tabela dos dois valores)
- Para que serve
- Antes de começar
- 1. O valor padrão: na área de atendimento
- 2. O valor de uma entrega específica: no pedido
- 3. Diária e valor por KM: no cadastro do funcionário
- 4. O relatório: Entregador (Taxa / KM)
- 5. Conferir pedido por pedido
- Dicas
- Onde continuar

## Anexo — legendas das imagens (na ordem)

1. `01-area-grupo.png` — A área de atendimento: a faixa mostra frete do cliente e valor do
   entregador.
2. `02-grupo-valores.png` — A janela da faixa, com *Valor pago ao entregador* no meio.
3. `04-pedido-sem-valor.png` — O pedido com *Valor do entregador: Não definido* e o lápis.
4. `05-pedido-editando.png` — O campo aberto, com o visto e o X.
5. `06-pedido-com-valor.png` — O valor gravado no pedido.
6. `03-funcionario-diaria-km.png` — Diária e valor por KM na aba *Função* do funcionário.
7. `07a-cabecalho.png` — O cabeçalho do relatório: ida e volta, os três modos, impressão e Excel.
8. `07b-cartoes.png` — Os cinco números do topo.
9. `07c-resumo.png` — O resumo por entregador no modo da taxa do cliente.
10. `08-modo-area.png` — A mesma tabela no modo da área de atendimento: coluna *Taxa Entregador*.
11. `09-modo-km.png` — No modo do cadastro do funcionário: coluna *KM (Ida)*, que traz o valor.
12. `10-ida-e-volta.png` — Com ida e volta ligado: três colunas de KM.
13. `11-todos-os-detalhes.png` — Uma linha por entrega, com a linha da diária.
14. `12-detalhe-entregador.png` — O fechamento de um entregador, com as diárias registradas.
