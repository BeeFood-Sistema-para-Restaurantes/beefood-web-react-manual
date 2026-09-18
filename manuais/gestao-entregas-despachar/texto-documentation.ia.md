# texto-documentation.ia.md — #107 Despachar e acompanhar

## PROMPT (copiar e colar)

Dentro do menu **Gestão de Entregas**, crie a página **Despachar a rota e acompanhar no
mapa**.

Leia APENAS os arquivos abaixo:

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/gestao-entregas-despachar/gestao-entregas-despachar.md`
2. Imagens (nesta ordem):
   - `.../imagens-tratadas/01-rota-pronta.png`
   - `.../imagens-tratadas/02-confirmar-despacho.png`
   - `.../imagens-tratadas/03-rota-na-rua.png`
   - `.../imagens-tratadas/04-entregador-na-rua.png`
   - `.../imagens-tratadas/05-lista-em-rota.png`
   - `.../imagens-tratadas/06-menu-na-rua.png`
   - `.../imagens-tratadas/07-trocar-entregador.png`

NÃO leia `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`,
`*.geo.json`, `*.itens.txt`.

- Apresentação IGUAL ao menu "Abrir Caixa".
- pt-BR, didático. Manter as tabelas de setas (nº → onde → o que faz) embaixo de cada
  imagem.
- Avisar, no começo, que a **Gestão de Entregas está em liberação** e que a tela pode ainda
  não aparecer para todos (falar com o suporte). Não citar `empresaID`.
- **Manter a seção 1 ("Leia isto antes de clicar") como primeira seção, com a tabela dos
  quatro disparos e o aviso de que não existe desfazer.** É o ponto do manual; enxugar isso
  descaracteriza a página.
- Manter, sem enxugar, os avisos que mudam o resultado na prática:
  (a) **despachar avisa o cliente, o marketplace e a impressora** — e não tem desfazer;
  (b) **o sistema não impede despachar pedido em preparo**: avisa e obedece;
  (c) **despachar duas vezes não faz nada** (defesa contra clique duplo);
  (d) **trocar entregador não avisa ninguém** — é preciso ligar para os dois;
  (e) **excluir rota despachada é permitido**, devolve os pedidos e libera o entregador, mas
  **não desfaz o aviso já enviado ao cliente**;
  (f) **sem aplicativo aberto não há pino no mapa** — pino parado com horário envelhecendo é
  problema de celular.
- Não publicar rotas de API, nomes de tabela, nomes de coluna nem nomes de componente.
- Não citar "orquestrador", `situacaoDelivery`, `EM_ROTA`, `DESPACHADO` nem nomes de
  arquivo do servidor. Falar em "situação do pedido", "parada atual" e "saiu para entrega".
- Não citar Lambda, Aurora nem o `cenario.js`, e nada de bastidor de captura.
- Não prometer notificação push no aplicativo: ela não existe.

## Estrutura da página (mesma numeração do `.md`)

- Para que serve
- Antes de começar
- 1. Leia isto antes de clicar
- 2. Despachar a rota
- 3. O que muda no painel
- 4. Acompanhar o entregador no mapa
- 5. Trocar o entregador com a rota na rua
- 6. Quando a rota precisa ser desfeita
- Dicas
- Onde continuar

## Anexo — legendas das imagens (na ordem)

1. `01-rota-pronta.png` — A rota pronta para sair e o botão de avião que despacha.
2. `02-confirmar-despacho.png` — A janela de confirmação: entregador, paradas, situação de
   cada pedido na cozinha e os dois avisos.
3. `03-rota-na-rua.png` — O painel no segundo seguinte: rota *Na rua*, parada atual marcada e
   os selos do topo trocados.
4. `04-entregador-na-rua.png` — O entregador andando no mapa, a caminho da primeira parada.
5. `05-lista-em-rota.png` — A lista de entregadores com ele no grupo *Em rota*, com distância
   e bateria.
6. `06-menu-na-rua.png` — O menu da rota despachada: trocar entregador, remover entregador,
   excluir rota.
7. `07-trocar-entregador.png` — A janela de troca, com o aviso de que a rota já está na rua.
