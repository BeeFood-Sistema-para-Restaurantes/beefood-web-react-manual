# texto-documentation.ia.md — #116 App do entregador: receber na porta

## PROMPT (copiar e colar)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `app-entregador-cobranca.md`
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

Dentro do menu **Gestão de Entregas**, crie a página **App do entregador: receber na porta**.

Leia APENAS os arquivos abaixo:

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/app-entregador-cobranca/app-entregador-cobranca.md`
2. Imagens (**nesta** ordem — que não é a ordem dos nomes: a `14` chegou depois e entra
   no meio, na seção 3):
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
  cliente. Nada de amenizar os avisos.
- Manter, obrigatoriamente e sem enxugar, os blocos de aviso:
  (a) **"Cobrar é finalizar"**, logo no começo — é a informação que muda o comportamento;
  (b) **A soma precisa fechar com o valor a receber**, na divisão de conta;
  (c) **Entrega que não aconteceu não deve ser finalizada**, na seção 4.
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
  (m) na seção 5, que **Pedido já pago** tem marca **verde** e não é erro, e que o entregador
  **não deve receber nada do cliente** nesse caso;
  (n) na seção 5, que a tela *Pagamento Confirmado!* do caso sem baixa é **igual** à do pagamento
  normal e que **só a frase de baixo diferencia** as duas;
  (o) na seção 5, o aviso de **não tocar em INICIAR COBRANÇA** quando o rodapé ainda mostra o valor
  a cobrar depois de o pagamento ter sido registrado — é o caminho que cobra em dobro;
  (p) na seção 5, que a saída do *Não foi possível dar baixa* é **atualizar a lista** e finalizar de
  novo, e que o botão não estava errado;
  (q) a tabela **O resumo dos quatro casos**, no fim da seção 5, inteira.
- As seções 5 (**Quando a cobrança não fecha**) e 6 (**Regras que valem sempre**) são conteúdo, não
  apêndice. Publicar as duas no corpo da página.
- Não publicar rotas de API, nomes de tela do aplicativo, nomes de tabela nem de coluna. Em
  particular: não citar `Cobranca.js`, `CobrancaPessoa`, `Finalizar.js`, `_preVendaPagamento` nem
  os nomes internos de situação do pedido.
- Não citar que o seletor de pessoas vai até dez.
- Não citar bastidor de captura: nem emulador, nem material recebido, nem que a folha de bandeiras
  foi aberta só para a foto, nem que várias imagens são recortes de folhas.
- Os nomes de cliente que aparecem nas imagens são de cadastro de teste. Não comentar na página.

## Estrutura da página (mesma numeração do `.md`)

- Para que serve
- Antes de começar
- 1. Por onde a cobrança começa
- 2. A tela de pagamento
- 3. Quando mais de uma pessoa paga
- 4. Finalizar sem cobrar
- 5. Quando a cobrança não fecha
- 6. Regras que valem sempre
- Perguntas frequentes
- Onde continuar

## Anexo — legendas das imagens (na ordem do texto)

1. `01-rodape-de-cobranca.png` — O rodapé escuro: forma prevista, TOTAL, TROCO, COBRAR e os dois
   botões.
2. `02-conferir-destaque.png` — A folha CONFIRMA E ENTREGA DESSES PRODUTOS CORRETAMENTE?
3. `03-tela-de-pagamento.png` — A tela de pagamento com uma pessoa: o selo PEDIDO #1030, A RECEBER,
   DIVIDIR CONTA, valor, troco, observação e CONFIRMAR PAGAMENTO.
4. `04-forma-de-pagamento.png` — A lista de formas, com a prevista já marcada.
5. `05-bandeira-do-cartao.png` — A folha BANDEIRA, com o aviso de que é opcional.
6. `06-troco-para-quanto.png` — A folha Troco para quanto?, já preenchida.
7. `07-confirmar-cobranca.png` — A folha Confirmar cobrança?, com a linha da forma e do valor.
8. `08-pagamento-confirmado.png` — A tela Pagamento Confirmado!
9. `09-duas-pessoas.png` — A conta dividida em duas, com um bloco por pessoa.
10. `10-duas-formas.png` — Pix numa pessoa, dinheiro na outra, e a linha Troco para.
11. `14-soma-nao-fecha.png` — O aviso vermelho *A soma precisa ser R$ 19,90*, com as duas partes
    que não fecham.
12. `11-confirmar-duas-linhas.png` — A confirmação com uma linha numerada por pessoa.
13. `12-finalizar-sem-cobrar.png` — O aviso Finalizar sem cobrar?, com o valor em aberto.
14. `13-observacao-preenchida.png` — A folha Finalizar Entrega, com a observação escrita e o
    contador de caracteres.
15. `15-erro-no-pagamento.png` — A tela Erro no Pagamento, com TENTAR NOVAMENTE e VOLTAR PARA
    ENTREGAS.
16. `16-pedido-ja-pago.png` — A tela Pedido já pago, de marca verde, com FECHAR.
17. `17-pagamento-sem-baixa.png` — A tela Pagamento Confirmado! que pede para finalizar a entrega.
18. `18-pagamento-registrado.png` — O alerta Pagamento registrado sobre os detalhes, com o rodapé
    que ainda mostra o valor a cobrar.
19. `19-nao-foi-possivel-dar-baixa.png` — A janela Não foi possível dar baixa, sobre o FINALIZAR.
