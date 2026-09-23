# texto-documentation.ia.md — #109 Despacho automático: as sete regras

## PROMPT (copiar e colar)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `gestao-entregas-despacho-automatico.md`
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

Dentro do menu **Gestão de Entregas**, crie a página **Despacho automático: as sete regras**.

Leia APENAS os arquivos abaixo:

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/gestao-entregas-despacho-automatico/gestao-entregas-despacho-automatico.md`
2. Imagens (nesta ordem):
   - `.../imagens-tratadas/01a-janela-avisos.png`
   - `.../imagens-tratadas/01b-janela-regras.png`
   - `.../imagens-tratadas/02-janela-ligada.png`
   - `.../imagens-tratadas/03-rota-automatica.png`
   - `.../imagens-tratadas/04-rota-associada.png`

NÃO leia `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`, `*.geo.json`.

- Apresentação IGUAL ao menu "Abrir Caixa".
- pt-BR, didático. Manter as tabelas de setas (nº → onde → o que faz) embaixo de cada imagem.
- Avisar, no começo, que a **Gestão de Entregas está em liberação** e que a tela pode ainda não
  aparecer para todos (falar com o suporte). Não citar `empresaID`.
- Manter, sem enxugar, os avisos que mudam o resultado na prática:
  (a) **o automático agrupa e escolhe entregador, mas NÃO despacha** — e o motivo (despachar
  avisa o cliente);
  (b) **só roda com a tela de Gestão de Entregas aberta** em algum computador da loja;
  (c) **pedido com mais de 2 horas nunca é agrupado**, e esse limite não se configura;
  (d) **sem SALVAR nada vale**, nem as regras nem o interruptor;
  (e) a rota nasce **sem entregador** (*Montando*) e ganha dono numa segunda etapa — não é
  falha;
  (f) a tabela das quatro causas de rota que fica em *Montando*, incluindo **GPS velho**, que
  foi o caso real do teste.
- Manter as três observações da seção 2 que a janela não explica: a fila começa pelo pedido mais
  antigo, a distância é conferida contra todos os pedidos do grupo, e a ordem das paradas é
  refeita depois.
- Não publicar rotas de API, nomes de tabela, nomes de coluna nem nomes de componente.
- Não citar nomes de arquivo do servidor, "orquestrador", `EM_ROTA`, `PRONTO` nem nome de cron.
  Falar em "situação do pedido" e "pedido pronto".
- Não citar o `cenario.js` nem nada de bastidor de captura. Onde o manual diz "foi a tolerância
  de GPS que segurou a nossa rota", manter o relato como exemplo de operação, sem falar de
  script.

## Estrutura da página (mesma numeração do `.md`)

- Para que serve
- Antes de começar
- 1. O que ele é, e os dois avisos da janela
- 2. As sete regras
- 3. Ligar
- 4. A rota nasce sem entregador
- 5. O entregador entra depois
- 6. Desligar
- Dicas
- Onde continuar

## Anexo — legendas das imagens (na ordem)

1. `01a-janela-avisos.png` — A janela do despacho automático: a explicação do topo, o
   interruptor e os dois avisos (tela aberta e limite de 2 horas).
2. `01b-janela-regras.png` — As sete regras, em duas colunas: o que junta os pedidos e o que
   escolhe o entregador.
3. `02-janela-ligada.png` — O interruptor ligado, o texto de confirmação e o botão SALVAR.
4. `03-rota-automatica.png` — A rota criada sozinha, ainda *Sem entregador* e em *Montando*.
5. `04-rota-associada.png` — A mesma rota depois da segunda etapa: entregador escolhido,
   *Pronta para sair* e o avião esperando o seu clique.
