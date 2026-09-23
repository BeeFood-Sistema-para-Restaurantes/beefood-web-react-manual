# texto-documentation.ia.md — #106 Montar a rota

## PROMPT (copiar e colar)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `gestao-entregas-montar-rota.md`
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

Dentro do menu **Gestão de Entregas**, crie a página **Montar a rota: agrupar pedidos e
escolher o entregador**.

Leia APENAS os arquivos abaixo:

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/gestao-entregas-montar-rota/gestao-entregas-montar-rota.md`
2. Imagens (nesta ordem):
   - `.../imagens-tratadas/01-selecao.png`
   - `.../imagens-tratadas/02-janela-criar-rota.png`
   - `.../imagens-tratadas/03-entregador-escolhido.png`
   - `.../imagens-tratadas/04-rota-criada.png`
   - `.../imagens-tratadas/05a-cabecalho-rota.png`
   - `.../imagens-tratadas/05b-paradas-da-rota.png`
   - `.../imagens-tratadas/08-otimizar-ordem.png`
   - `.../imagens-tratadas/06-adicionar-a-rota.png`
   - `.../imagens-tratadas/07-rota-com-parada-nova.png`
   - `.../imagens-tratadas/09-menu-da-rota.png`

NÃO leia `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`,
`*.geo.json`, `*.itens.txt`, `*.ordem.txt`.

- Apresentação IGUAL ao menu "Abrir Caixa".
- pt-BR, didático. Manter as tabelas de setas (nº → onde → o que faz) embaixo de cada
  imagem.
- Avisar, no começo, que a **Gestão de Entregas está em liberação** e que a tela pode ainda
  não aparecer para todos (falar com o suporte). Não citar `empresaID`.
- Manter, sem enxugar, os cinco avisos que mudam o resultado na prática:
  (a) **a rota nasce parada** — criar não despacha;
  (b) **Marcar prontos limpa a seleção**, então marque prontos antes de criar a rota;
  (c) **a letra da rota é reaproveitada** e não serve para falar de entrega passada;
  (d) **o pedido adicionado entra no fim da fila**, e em rota já despachada **o entregador
  não é avisado sozinho** — é preciso ligar para ele;
  (e) **Excluir rota não cancela pedido**: os pedidos voltam para *Pedidos sem rota*.
- Manter o aviso de que **o aplicativo do entregador pode desfazer a ordem** com o botão de
  *melhor rota*.
- Manter a observação de que o botão **Otimizar ordem só aparece quando há ordem melhor**.
- Manter a dica final de que **o sistema não bloqueia quase nada**, e que por isso o cuidado
  é do operador.
- Não publicar rotas de API, nomes de tabela, nomes de coluna nem nomes de componente.
- Não citar Haversine nem "linha reta" como termo técnico; dizer que a distância é medida em
  linha reta, em palavras simples.
- Não citar o `cenario.js` nem nada de bastidor de captura.

## Estrutura da página (mesma numeração do `.md`)

- Para que serve
- Antes de começar
- 1. Escolher os pedidos
- 2. Criar a rota
- 3. Ler o grupo da rota
- 4. Ordenar as paradas
- 5. Juntar um pedido a uma rota que já existe
- 6. Trocar o entregador e desfazer a rota
- Dicas
- Onde continuar

## Anexo — legendas das imagens (na ordem)

1. `01-selecao.png` — Três pedidos marcados e a barra de ação no pé da tela.
2. `02-janela-criar-rota.png` — A janela de criar rota: paradas, total e lista de
   entregadores.
3. `03-entregador-escolhido.png` — O entregador escolhido fica destacado.
4. `04-rota-criada.png` — A rota criada, na lateral e com a letra nos pinos do mapa.
5. `05a-cabecalho-rota.png` — O cabeçalho da rota: entregador, letra, situação e andamento.
6. `05b-paradas-da-rota.png` — As paradas: ordem, alça de arrastar e o visto de baixa.
7. `08-otimizar-ordem.png` — Depois de otimizar, a ordem das paradas muda.
8. `06-adicionar-a-rota.png` — Escolhendo em qual rota o pedido novo entra.
9. `07-rota-com-parada-nova.png` — O pedido novo entrou como última parada.
10. `09-menu-da-rota.png` — O menu da rota: trocar entregador, remover entregador, excluir.
