# texto-documentation.ia.md — #116 App do entregador: receber na porta

## PROMPT (copiar e colar)

Dentro do menu **Gestão de Entregas**, crie a página **App do entregador: receber na porta**.

Leia APENAS os arquivos abaixo:

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/app-entregador-cobranca/app-entregador-cobranca.md`
2. Imagens (**nesta** ordem — que não é a ordem dos nomes: a `20` abre a página, na seção 1,
   e a `14` entra no meio, na seção 4):
   - `.../imagens-tratadas/20-parametro-entregador-registra-pagamento.png`
   - `.../imagens-tratadas/01-rodape-de-cobranca.png`
   - `.../imagens-tratadas/02-conferir-destaque.png`
   - `.../imagens-tratadas/03-tela-de-pagamento.png`
   - `.../imagens-tratadas/04-forma-de-pagamento.png`
   - `.../imagens-tratadas/05-bandeira-do-cartao.png`
   - `.../imagens-tratadas/06-troco-para-quanto.png`
   - `.../imagens-tratadas/07-confirmar-cobranca.png`
   - `.../imagens-tratadas/08-pagamento-confirmado.png`
   - `.../imagens-tratadas/09-duas-pessoas.png`
   - `.../imagens-tratadas/10-duas-formas.png`
   - `.../imagens-tratadas/14-soma-nao-fecha.png`
   - `.../imagens-tratadas/11-confirmar-duas-linhas.png`
   - `.../imagens-tratadas/12-finalizar-sem-cobrar.png`
   - `.../imagens-tratadas/13-observacao-preenchida.png`
   - `.../imagens-tratadas/15-erro-no-pagamento.png`
   - `.../imagens-tratadas/16-pedido-ja-pago.png`
   - `.../imagens-tratadas/17-pagamento-sem-baixa.png`
   - `.../imagens-tratadas/18-pagamento-registrado.png`
   - `.../imagens-tratadas/19-nao-foi-possivel-dar-baixa.png`

NÃO leia `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`.

- Apresentação IGUAL ao menu "Abrir Caixa".
- pt-BR, didático. Manter as tabelas de setas (nº → onde → o que é) embaixo de cada imagem.
- Avisar, no começo, que a **Gestão de Entregas está em liberação**. Não citar `empresaID`.
- **Este manual é para o entregador, e é o manual do dinheiro.** Tom de quem está na porta do
  cliente. Nada de amenizar os avisos. **A seção 1 é a exceção:** ela fala com quem configura o
  sistema — dono ou gerente, no computador —, e é assim de propósito.
- **A seção 1 tem de ficar em primeiro lugar, antes de qualquer tela do aplicativo.** Ela responde
  a pergunta que passou a vir antes de todas: *o aplicativo do meu entregador tem tela de
  pagamento?*
- Manter, obrigatoriamente e sem enxugar, os blocos de aviso:
  (a) **"Cobrar é finalizar"**, logo no começo — é a informação que muda o comportamento;
  (b) **A soma precisa fechar com o valor a receber**, na divisão de conta;
  (c) **Entrega que não aconteceu não deve ser finalizada**, na seção 5;
  (r) **A tela de pagamento pode estar desligada**, no primeiro bloco da página, com a remissão à
  seção 1.
- Manter também, sem enxugar:
  (d) que a **forma do rodapé é uma previsão**, e que vale o que aconteceu de verdade — a frase
  sobre o fechamento de caixa é o argumento, não pode sair;
  (e) que **não tem como desfazer** nem a cobrança nem a finalização;
  (f) que **não se deve tocar duas vezes em CONFIRMAR**, e que a saída é **conferir no histórico**
  — nunca "tentar de novo";
  (g) que a **bandeira é opcional** e, na dúvida, se segue sem;
  (h) que a **lista de formas é o que o restaurante habilitou**, e que fiado, Pix automático e
  formas de marketplace ficam fora de propósito;
  (i) que, **com uma pessoa**, a forma é escolhida depois do CONFIRMAR PAGAMENTO, e que na
  **divisão** cada bloco tem a sua — é a diferença entre as duas seções;
  (j) que a divisão é **tudo ou nada**;
  (k) que a **observação sempre deve ser escrita** no caminho sem cobrança, com o exemplo;
  (l) a tabela **Quando usar cada caminho**, inteira, incluindo a linha do cliente ausente;
  (m) na seção 6, que **Pedido já pago** tem marca **verde** e não é erro, e que o entregador
  **não deve receber nada do cliente** nesse caso;
  (n) na seção 6, que a tela *Pagamento Confirmado!* do caso sem baixa é **igual** à do pagamento
  normal e que **só a frase de baixo diferencia** as duas;
  (o) na seção 6, o aviso de **não tocar em INICIAR COBRANÇA** quando o rodapé ainda mostra o valor
  a cobrar depois de o pagamento ter sido registrado — é o caminho que cobra em dobro;
  (p) na seção 6, que a saída do *Não foi possível dar baixa* é **atualizar a lista** e finalizar de
  novo, e que o botão não estava errado;
  (q) a tabela **O resumo dos quatro casos**, no fim da seção 6, inteira;
  (s) na seção 1: que o parâmetro é **Entregador registra pagamento**, que ele fica em
  **Configuração → Parâmetros**, card **Delivery**, que vem **ligado de fábrica**, que a tela
  **grava sozinha** e que **desligado o entregador continua vendo o valor a receber** — só não
  lança o pagamento pelo aplicativo;
  (t) na seção 1: o aviso de **não confundir com o Pagamento Automático Delivery**, que é a chave
  vizinha, e a tabela **O que muda no celular**, inteira.
- As seções 6 (**Quando a cobrança não fecha**) e 7 (**Regras que valem sempre**) são conteúdo, não
  apêndice. Publicar as duas no corpo da página.
- **O primeiro bloco das Perguntas frequentes — *A tela de pagamento do aplicativo* — vai inteiro,
  pergunta por pergunta, sem juntar nem resumir.** Ele existe para ser encontrado por busca e pela
  IA de atendimento: cada pergunta é uma forma diferente de perguntar a mesma coisa, e juntá-las
  desfaz o propósito.
- Não publicar rotas de API, nomes de tela do aplicativo, nomes de tabela nem de coluna. Em
  particular: não citar `Cobranca.js`, `CobrancaPessoa`, `Finalizar.js`, `_preVendaPagamento` nem
  os nomes internos de situação do pedido.
- Não citar que o seletor de pessoas vai até dez.
- Não citar bastidor de captura: nem emulador, nem material recebido, nem que a folha de bandeiras
  foi aberta só para a foto, nem que várias imagens são recortes de folhas.
- Os nomes de cliente que aparecem nas imagens são de cadastro de teste. Não comentar na página.
- Na imagem do card **Delivery** a chave *Entregador registra pagamento* aparece **desligada**, e o
  texto avisa que o padrão de fábrica é ligado. **Isso não é erro de captura — manter as duas
  coisas**, a imagem e o aviso.

## Estrutura da página (mesma numeração do `.md`)

- Para que serve
- Antes de começar
- 1. O restaurante decide se o entregador cobra
- 2. Por onde a cobrança começa
- 3. A tela de pagamento
- 4. Quando mais de uma pessoa paga
- 5. Finalizar sem cobrar
- 6. Quando a cobrança não fecha
- 7. Regras que valem sempre
- Perguntas frequentes (o primeiro bloco delas é **A tela de pagamento do aplicativo**)
- Onde continuar

## Anexo — legendas das imagens (na ordem do texto)

1. `20-parametro-entregador-registra-pagamento.png` — O card **Delivery** de Configuração →
   Parâmetros, com as duas chaves: *Pagamento Automático Delivery* e *Entregador registra
   pagamento*.
2. `01-rodape-de-cobranca.png` — O rodapé escuro: forma prevista, TOTAL, TROCO, COBRAR e os dois
   botões.
3. `02-conferir-destaque.png` — A folha CONFIRMA E ENTREGA DESSES PRODUTOS CORRETAMENTE?
4. `03-tela-de-pagamento.png` — A tela de pagamento com uma pessoa: o selo PEDIDO #1030, A RECEBER,
   DIVIDIR CONTA, valor, troco, observação e CONFIRMAR PAGAMENTO.
5. `04-forma-de-pagamento.png` — A lista de formas, com a prevista já marcada.
6. `05-bandeira-do-cartao.png` — A folha BANDEIRA, com o aviso de que é opcional.
7. `06-troco-para-quanto.png` — A folha Troco para quanto?, já preenchida.
8. `07-confirmar-cobranca.png` — A folha Confirmar cobrança?, com a linha da forma e do valor.
9. `08-pagamento-confirmado.png` — A tela Pagamento Confirmado!
10. `09-duas-pessoas.png` — A conta dividida em duas, com um bloco por pessoa.
11. `10-duas-formas.png` — Pix numa pessoa, dinheiro na outra, e a linha Troco para.
12. `14-soma-nao-fecha.png` — O aviso vermelho *A soma precisa ser R$ 19,90*, com as duas partes
    que não fecham.
13. `11-confirmar-duas-linhas.png` — A confirmação com uma linha numerada por pessoa.
14. `12-finalizar-sem-cobrar.png` — O aviso Finalizar sem cobrar?, com o valor em aberto.
15. `13-observacao-preenchida.png` — A folha Finalizar Entrega, com a observação escrita e o
    contador de caracteres.
16. `15-erro-no-pagamento.png` — A tela Erro no Pagamento, com TENTAR NOVAMENTE e VOLTAR PARA
    ENTREGAS.
17. `16-pedido-ja-pago.png` — A tela Pedido já pago, de marca verde, com FECHAR.
18. `17-pagamento-sem-baixa.png` — A tela Pagamento Confirmado! que pede para finalizar a entrega.
19. `18-pagamento-registrado.png` — O alerta Pagamento registrado sobre os detalhes, com o rodapé
    que ainda mostra o valor a cobrar.
20. `19-nao-foi-possivel-dar-baixa.png` — A janela Não foi possível dar baixa, sobre o FINALIZAR.
