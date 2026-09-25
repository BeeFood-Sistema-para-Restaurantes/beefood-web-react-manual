# texto-documentation.ia.md — #108 Fechar a entrega no painel

## PROMPT (copiar e colar)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `gestao-entregas-fechar-entrega.md`
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

Dentro do menu **Gestão de Entregas**, crie a página **Fechar a entrega no painel**.

Leia APENAS os arquivos abaixo:

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/gestao-entregas-fechar-entrega/gestao-entregas-fechar-entrega.md`
2. Imagens (nesta ordem):
   - `.../imagens-tratadas/01-antes-da-baixa.png`
   - `.../imagens-tratadas/02-uma-entregue.png`
   - `.../imagens-tratadas/03-tres-entregues.png`
   - `.../imagens-tratadas/04-depois-de-fechar.png`
   - `.../imagens-tratadas/05-chip-entregues.png`
   - `.../imagens-tratadas/05b-grupo-entregues.png`
   - `.../imagens-tratadas/06-entregador-de-volta.png`
   - `.../imagens-tratadas/07-pedido-no-delivery.png`

NÃO leia `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`, `*.geo.json`.

- Apresentação IGUAL ao menu "Abrir Caixa".
- pt-BR, didático. Manter as tabelas de setas (nº → onde → o que faz) embaixo de cada
  imagem.
- Avisar, no começo, que a **Gestão de Entregas está em liberação** e que a tela pode ainda
  não aparecer para todos (falar com o suporte). Não citar `empresaID`.
- Manter, sem enxugar, os avisos que mudam o resultado na prática:
  (a) **o visto age no clique, sem janela de confirmação** — e o motivo (finalizar, que é
  maior, também não pede);
  (b) **dar baixa fora de ordem é permitido**, e **não** muda quem está *Entregando agora*;
  (c) **a última baixa encerra a rota sozinha** e libera o entregador;
  (d) **o botão de finalizar confirma todas as paradas pendentes de uma vez**, sem perguntar —
  com o conselho de deixar a parada duvidosa para o fim;
  (e) **não existe "não entregue"**: o sistema só registra entrega;
  (f) **se a rota sumiu, ligue o selo *entregues*** — ela fica por cerca de duas horas.
- Manter a observação de que **duas rotas concluídas podem ter a mesma letra**, porque a letra
  é reaproveitada, e que para falar de entrega passada se usa o número do pedido.
- Não publicar rotas de API, nomes de tabela, nomes de coluna nem nomes de componente.
- Não citar `EM_ROTA`, `ENTREGUE`, `INSUCESSO`, "orquestrador" nem nomes de arquivo do
  servidor. Falar em "situação do pedido" e "parada atual".
- Não citar janela de 6 horas, view do ERP nem nada de banco de dados; a frase do manual
  ("os pedidos entregues continuam aparecendo um pouco mais") já basta.
- Não citar o `cenario.js` nem nada de bastidor de captura.

## Estrutura da página (mesma numeração do `.md`)

- Para que serve
- Antes de começar
- 1. Dar baixa em uma parada
- 2. Quando falta uma parada
- 3. Finalizar a rota inteira
- 4. Achar o que já foi entregue
- 5. Onde o pedido vai dar no Delivery
- Dicas
- Onde continuar

## Anexo — legendas das imagens (na ordem)

1. `01-antes-da-baixa.png` — A rota na rua, com o visto de cada parada e o botão de finalizar.
2. `02-uma-entregue.png` — A primeira parada entregue: linha apagada, contagem e selos do topo.
3. `03-tres-entregues.png` — Três entregues, uma pendente.
4. `04-depois-de-fechar.png` — O painel depois de a rota concluir: nada em rota, entregador
   disponível.
5. `05-chip-entregues.png` — O selo *entregues* ligado revela o grupo *Entregues*.
6. `05b-grupo-entregues.png` — O grupo aberto, com a rota concluída em verde e os pedidos
   entregues.
7. `06-entregador-de-volta.png` — O entregador de volta ao grupo *Disponível*.
8. `07-pedido-no-delivery.png` — O mesmo pedido na coluna *ENTREGUE* do Delivery.
