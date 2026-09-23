# texto-documentation.ia.md — O cliente acompanha a entrega no mapa (#125)

## PROMPT (copiar e colar)

Em **Entrega**, crie um novo item de menu por último chamado **O cliente acompanha a entrega no
mapa**.

Leia APENAS os arquivos abaixo (não varra o resto do projeto):

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/gestao-entregas-rastreio-cliente/gestao-entregas-rastreio-cliente.md`
2. Imagens (nesta ordem):
   - `beefood-web-react-manual/manuais/gestao-entregas-rastreio-cliente/imagens-tratadas/01-whatsapp-link.png`
   - `beefood-web-react-manual/manuais/gestao-entregas-rastreio-cliente/imagens-tratadas/02-pedido-em-preparo.png`
   - `beefood-web-react-manual/manuais/gestao-entregas-rastreio-cliente/imagens-tratadas/03-saiu-para-entrega.png`
   - `beefood-web-react-manual/manuais/gestao-entregas-rastreio-cliente/imagens-tratadas/04-mapa-tela-cheia.png`
   - `beefood-web-react-manual/manuais/gestao-entregas-rastreio-cliente/imagens-tratadas/05-itens-do-pedido.png`
   - `beefood-web-react-manual/manuais/gestao-entregas-rastreio-cliente/imagens-tratadas/06-mapa-no-computador.png`
   - `beefood-web-react-manual/manuais/gestao-entregas-rastreio-cliente/imagens-tratadas/07-pedido-concluido.png`

NÃO leia outros arquivos (`fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`).

- Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa".
- pt-BR, didático; o leitor é o **lojista**, e o assunto é o que o **cliente dele** vê.
- Não publicar o rodapé de referências internas.
- Palavras que o leitor vai buscar e que devem sobreviver na página: *onde está meu pedido*,
  *rastreio do pedido*, *rastrear entrega*, *acompanhar entrega no mapa*, *link de
  acompanhamento*, *rastreamento em tempo real*, *mapa do entregador*, *delivery com rastreio*,
  *quanto tempo falta*, *meu pedido saiu para entrega*.

## Estrutura da página (na ordem do `.md`)

1. Título e para que serve — a mentalidade: **o cliente se serve da informação sozinho**, em vez
   de ligar para a loja. Fecha com "você não precisa configurar nada".
2. Antes de começar — os quatro pré-requisitos (GPS do entregador, nome cadastrado, endereço com
   localização, notificação de *saiu para entrega* ligada).
3. **1. O link que o cliente recebe no WhatsApp** — o que é seu e o que o sistema acrescenta, o
   código de 22 caracteres, a expiração, e quando o link **não** aparece (posição dos últimos 15
   minutos).
4. **2. O cliente não depende do WhatsApp** — a segunda porta, em *Pedidos* no cardápio, e as duas
   fronteiras: só entrega, só em andamento.
5. **3. Pedido aceito, comida ainda na cozinha** — o mapa antes de existir motoboy, e por que ele
   já aparece.
6. **4. Saiu para entrega: o motoboy aparece** — nome, distância em linha reta, a moto; e por que
   a tela não estima horário de chegada.
7. **5. A tela cheia do acompanhamento** — o mesmo link do WhatsApp, o voltar do navegador, o
   horário da última posição, a frequência de atualização, os itens e a versão de computador.
8. **6. Pedido entregue** — o ciclo fechado e a avaliação.
9. **7. O que a tela escreve em cada situação** — tabela de consulta, **só texto**.
10. Perguntas frequentes.
11. Onde continuar.

## Anexo — legendas das imagens (na ordem)

| Ordem | Arquivo (em `imagens-tratadas/`) | Tipo | Legenda |
|---|---|---|---|
| 1 | `01-whatsapp-link.png` | com setas (3) | A mensagem de *saiu para entrega* no WhatsApp do cliente, com o bloco **Acompanhe a entrega** e o link de acompanhamento |
| 2 | `02-pedido-em-preparo.png` | com setas (6) | O pedido em preparo no celular do cliente: número, barra de etapas, estado, o aviso *Avisaremos assim que sair para entrega* e o mapa com a loja e o endereço |
| 3 | `03-saiu-para-entrega.png` | com setas (5) | O pedido a caminho: o estado com a hora, o nome do entregador, a distância em linha reta e a moto no mapa |
| 4 | `04-mapa-tela-cheia.png` | com setas (6) | O acompanhamento em tela cheia no celular: **Ir para o pedido**, cabeçalho, os três pontos do mapa e a folha deslizante |
| 5 | `05-itens-do-pedido.png` | com setas (4) | A folha de baixo com a lista de itens aberta, o nome do entregador e o horário da última posição |
| 6 | `06-mapa-no-computador.png` | com setas (6) | A mesma tela no computador: informações à esquerda, mapa à direita, e o traço pontilhado entre a moto e o destino |
| 7 | `07-pedido-concluido.png` | com setas (3) | O pedido concluído: data e hora no cabeçalho, a faixa **Pedido concluído** e o convite para avaliar |

## Observações de conteúdo

- O manual é **sobre a tela do cliente**, não sobre a operação. Ele não ensina a montar rota,
  despachar nem dar baixa — os links de *Onde continuar* levam a esses manuais.
- **Manter a honestidade das duas caixas de destaque:** a tela não estima horário de chegada, e a
  distância é em **linha reta**. Isso é posição de produto, não limitação a esconder.
- **Manter a seção 7 só em texto.** Ela é tabela de consulta para quem atende o cliente; imagem
  ali não acrescenta nada.
- As capturas são de um pedido de **demonstração com dados falsos**, liberado pelo dono — por isso
  o link e o endereço aparecem inteiros. Se a página for reilustrada com pedido de loja real, o
  código do link precisa sair coberto.
