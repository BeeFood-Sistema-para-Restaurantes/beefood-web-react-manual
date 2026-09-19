# texto-documentation.ia.md — Relatório Operação de Entrega

## PROMPT (copiar e colar)

Dentro do menu **Gestão de Entregas**, crie a página
**Relatório Operação de Entrega: onde o tempo da entrega se perde**.

Leia APENAS os arquivos abaixo:

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/relatorio-operacao-entrega/relatorio-operacao-entrega.md`
2. Imagens (nesta ordem):
   - `.../imagens-tratadas/01-menu-delivery.png`
   - `.../imagens-tratadas/02-periodo-hoje.png`
   - `.../imagens-tratadas/03-kpis.png`
   - `.../imagens-tratadas/04-metricas-tempo.png`
   - `.../imagens-tratadas/06-prazos.png`
   - `.../imagens-tratadas/08-por-hora.png`
   - `.../imagens-tratadas/09-mapa.png`
   - `.../imagens-tratadas/09b-mapa-bairros.png`
   - `.../imagens-tratadas/10-filtros.png`
   - `.../imagens-tratadas/11-dados.png`

NÃO leia `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`, `*.geo.json`.

- Apresentação IGUAL ao menu "Abrir Caixa".
- pt-BR, didático. Manter as tabelas de setas (nº → onde → o que lê) embaixo de cada imagem.
- Avisar, no começo, que a **Gestão de Entregas está em liberação** e que o item pode ainda não
  aparecer no menu (falar com o suporte). Não citar `empresaID`.
- Manter, sem enxugar, as regras de leitura que evitam conclusão errada:
  (a) **traço (—) é "não medido", nunca zero**;
  (b) **média só a partir de 20 pedidos** — *Poucos pedidos* não é erro;
  (c) **toda média vem com a cobertura embaixo**, e cobertura baixa é número frágil;
  (d) **entrega acima de 4 h sai da média**;
  (e) **escolher o atalho de período não basta: precisa Confirmar**;
  (f) **sem horário prometido não há pontualidade**, e o prometido vem do marketplace;
  (g) **traço em *Taxas do entregador*** manda fechar pagamento no relatório
  *Entregador (Taxa / KM)*;
  (h) a divisão **loja × rua** exige horário de saída gravado.
- Manter as duas tabelas auxiliares: a das quatro etapas (do quê até quê) e a de colunas da
  tabela de bairros.
- Não publicar rotas de API, nomes de tabela, nomes de coluna, nomes de componente nem nomes de
  arquivo. Não citar cache, endpoint, iframe nem período máximo de 366 dias.
- Não citar `ENTREGUE`, `EM_ROTA` nem nome de campo de banco. Falar em "pedido entregue" e
  "horário de saída".
- Não citar diferença de contagem entre relatórios em número de linha de código; se quiser
  mencionar, use a frase do manual (este conta pedido entregue; o vizinho monta pagamento).
- Não citar o `cenario.js` nem nada de bastidor de captura.

## Estrutura da página (mesma numeração do `.md`)

- Para que serve
- Antes de começar
- 1. Achar o relatório
- 2. Escolher o período
- 3. Os seis números do topo
- 4. Métricas de tempo: as quatro etapas
- 5. Análise dos prazos de entrega
- 6. Por hora do dia
- 7. Onde a rua custa mais
- 8. Filtrar
- 9. A aba Dados
- Dicas
- Onde continuar

## Anexo — legendas das imagens (na ordem)

1. `01-menu-delivery.png` — O caminho: Desempenho → Delivery → Operação de Entrega.
2. `02-periodo-hoje.png` — O seletor de período aberto, com os atalhos e o Confirmar.
3. `03-kpis.png` — Os seis indicadores do topo, o Comparativo, o funil e a aba Dados.
4. `04-metricas-tempo.png` — As quatro etapas, com *Não medido*, *Poucos pedidos* e o bloco
   da divisão entre loja e rua.
5. `06-prazos.png` — Os quatro cartões de prazo e a nota de cobertura.
6. `08-por-hora.png` — Pedidos e tempo médio hora a hora.
7. `09-mapa.png` — O mapa por tempo de entrega, com as escolhas de cor e de pontos.
8. `09b-mapa-bairros.png` — A tabela por bairro, com tempo de rua, pontualidade e cobertura.
9. `10-filtros.png` — A janela de filtros da operação.
10. `11-dados.png` — A aba Dados, uma linha por pedido, com o botão de Excel.
