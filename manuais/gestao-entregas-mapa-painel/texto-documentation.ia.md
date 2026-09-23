# texto-documentation.ia.md — #105 Ler o mapa e o painel de entregas

## PROMPT (copiar e colar)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `gestao-entregas-mapa-painel.md`
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

Crie um item de menu novo chamado **Gestão de Entregas** e, dentro dele, a página
**Ler o mapa e o painel de entregas** — a primeira do grupo.

Leia APENAS os arquivos abaixo:

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/gestao-entregas-mapa-painel/gestao-entregas-mapa-painel.md`
2. Imagens (nesta ordem):
   - `.../imagens-tratadas/01-porta-delivery.png`
   - `.../imagens-tratadas/02-painel-inteiro.png`
   - `.../imagens-tratadas/03-selos.png`
   - `.../imagens-tratadas/05-filtro-preparacao-off.png`
   - `.../imagens-tratadas/04-lista-entregadores.png`
   - `.../imagens-tratadas/07-busca.png`
   - `.../imagens-tratadas/06-camadas-mapa.png`

NÃO leia `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`,
`*.geo.json`.

- Apresentação IGUAL ao menu "Abrir Caixa".
- pt-BR, didático. Manter as tabelas de setas (nº → onde → o que faz) embaixo de cada
  imagem.
- Avisar, no começo, que a **Gestão de Entregas está em liberação** e que a tela pode
  ainda não aparecer para todos (falar com o suporte). Não citar `empresaID`.
- Manter, sem enxugar, os quatro avisos que o cliente erra na prática:
  (a) **a tela precisa ficar aberta** para o despacho automático agrupar;
  (b) **selo apagado esconde pedido** — é o esconderijo mais comum quando "o pedido
  desapareceu";
  (c) **pedido sem endereço geolocalizado não aparece no mapa**, só na lista, e é isso que
  faz as duas contagens divergirem;
  (d) **a distância é em linha reta**, serve para comparar e não para estimar tempo.
- Manter a tabela das quatro situações do entregador (Disponível, Em rota, Em pausa,
  Offline) e a frase de que **quem muda a situação é o entregador, no aplicativo** — não há
  como fazer isso pelo painel.
- Manter o destaque sobre **"há N min" ser a idade da última posição**, não do último toque:
  é a explicação de entregador que "sumiu do mapa".
- Manter a seção 6 (camadas do mapa) com a tabela de quando cada uma ajuda.
- Manter a tabela final **Onde continuar**, com os links para os outros manuais do grupo.
- Não publicar rotas de API, nomes de tabela, nomes de componente nem `empresaID`.
- Não citar o `cenario.js` nem nada de bastidor de captura.

## Estrutura da página (mesma numeração do `.md`)

- Para que serve
- Antes de começar
- 1. Abrir o painel
- 2. As duas metades da tela
- 3. Os selos do topo
- 4. Quem está na rua
- 5. Achar um pedido
- 6. Trocar o desenho do mapa
- Dicas
- Onde continuar

## Anexo — legendas das imagens (na ordem)

1. `01-porta-delivery.png` — O botão **Entregas** na barra da tela Delivery.
2. `02-painel-inteiro.png` — O painel: mapa à esquerda, rotas à direita.
3. `03-selos.png` — Os quatro selos de situação, a pílula do despacho e o Recarregar.
4. `05-filtro-preparacao-off.png` — Com um selo desligado, aqueles pedidos saem do mapa e
   da lista.
5. `04-lista-entregadores.png` — A lista completa de entregadores, agrupada por situação.
6. `07-busca.png` — A busca filtrando a lista e o mapa ao mesmo tempo.
7. `06-camadas-mapa.png` — As quatro camadas do mapa.
