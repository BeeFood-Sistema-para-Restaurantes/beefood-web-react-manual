# texto-documentation.ia.md — #110 Avisos de WhatsApp da entrega

## PROMPT (copiar e colar)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `gestao-entregas-avisos-whatsapp.md`
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

Dentro do menu **Gestão de Entregas**, crie a página **Avisos de WhatsApp da entrega**.

Leia APENAS os arquivos abaixo:

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/gestao-entregas-avisos-whatsapp/gestao-entregas-avisos-whatsapp.md`
2. Imagens (nesta ordem):
   - `.../imagens-tratadas/01-lista-notificacoes.png`
   - `.../imagens-tratadas/02-grupo-entregador.png`
   - `.../imagens-tratadas/03-modal-nova-entrega.png`
   - `.../imagens-tratadas/04-modal-relatorio-diario.png`
   - `.../imagens-tratadas/05-modal-entregador-proximo.png`
   - `.../imagens-tratadas/07-km-recusado.png`
   - `.../imagens-tratadas/10a-celular-do-entregador.png`
   - `.../imagens-tratadas/08a-conversa-entregador.png`
   - `.../imagens-tratadas/09a-conversa-cliente.png`

NÃO leia `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`, `*.geo.json`.

- Apresentação IGUAL ao menu "Abrir Caixa".
- pt-BR, didático. Manter as tabelas de setas (nº → onde → o que faz) embaixo de cada imagem.
- Avisar, no começo, que a **Gestão de Entregas está em liberação** e que a tela pode ainda não
  aparecer para todos (falar com o suporte). Não citar `empresaID`.
- Manter, sem enxugar, o que muda o resultado na prática:
  (a) **salvar o aviso *Entregador próximo* uma vez, mesmo sem mudar nada** — a tela mostra
  2 km antes de o valor existir, e sem salvar o aviso não sai. É a seção mais importante;
  (b) o aviso *Entregador próximo* é do **cliente**, e por isso está no grupo Delivery;
  (c) **sem Celular no cadastro do funcionário, o entregador não recebe nada** — e não aparece
  erro em tela nenhuma;
  (d) o campo é em **km** (0,1 a 50): `2000` é recusado, e é o erro de quem pensa em metros;
  (e) mudar a distância leva **até 30 minutos** para valer; o liga/desliga vale na hora;
  (f) *Entrega cancelada* significa "este pedido não é mais seu", **não** o cancelamento do
  pedido;
  (g) os marcadores do **Relatório diário** não estão na paleta de variáveis — quem apagar um
  deve usar **Restaurar padrão**.
- Deixar claro que as duas conversas de WhatsApp são **simulação**, e que o texto delas é o
  texto de fábrica das próprias mensagens.
- Não publicar rotas de API, nomes de tabela, nomes de coluna, números de tipo de mensagem nem
  nomes de componente. Em particular: não citar `_WhatsappMsgTipoFilial`,
  `raioProximidadeMetros`, "tipo 33" nem "tipo 4" — falar pelos nomes da tela (*Entregador
  próximo*, *Pedido saiu para entrega*).
- Não citar nome de cron, de servidor, de cache nem de arquivo de código. Onde o manual fala do
  tempo de 30 minutos, manter como comportamento do sistema.
- Não citar o `cenario.js`, o `mock110.py` nem nada de bastidor de captura. Onde o manual diz
  "conferimos os dois lados no nosso restaurante de teste", manter como relato de operação.
- Não citar quantidades da base de clientes (o "quase nenhum tem essa distância gravada" pode
  ficar, sem número).

## Estrutura da página (mesma numeração do `.md`)

- Para que serve
- Antes de começar
- 1. Onde ficam os quatro avisos
- 2. Nova entrega: o que o entregador recebe
- 3. Relatório diário: as entregas de ontem
- 4. Entregador próximo: o aviso do cliente, e o campo de km
- 5. Sem Celular no cadastro, o entregador não recebe nada
- 6. O que chega no celular
- Perguntas frequentes
- Onde continuar

## Anexo — legendas das imagens (na ordem)

1. `01-lista-notificacoes.png` — A lista de notificações automáticas, com o grupo Delivery, o
   interruptor de cada aviso e o lápis que abre o texto.
2. `02-grupo-entregador.png` — O grupo Entregador com os três avisos do motoboy, e o
   *Entregador próximo* logo acima, no grupo Delivery, porque quem recebe é o cliente.
3. `03-modal-nova-entrega.png` — O texto de fábrica da Nova entrega, o botão Restaurar padrão e
   a paleta de variáveis.
4. `04-modal-relatorio-diario.png` — Os marcadores da lista de entregas e do total de taxas no
   Relatório diário.
5. `05-modal-entregador-proximo.png` — O campo de distância em km, que só existe neste aviso,
   com as variações de mensagem e o botão SALVAR.
6. `07-km-recusado.png` — O que acontece ao digitar 2000 no campo de km: o aviso de que o valor
   tem de estar entre 0,1 e 50, e nada é gravado.
7. `10a-celular-do-entregador.png` — Os campos Telefone e Celular do cadastro de funcionário:
   é para onde as três mensagens do entregador vão.
8. `08a-conversa-entregador.png` — Simulação do celular do entregador: nova entrega, entrega
   cancelada e o resumo do dia anterior.
9. `09a-conversa-cliente.png` — Simulação do celular do cliente: o pedido saiu para entrega e o
   entregador está chegando.
