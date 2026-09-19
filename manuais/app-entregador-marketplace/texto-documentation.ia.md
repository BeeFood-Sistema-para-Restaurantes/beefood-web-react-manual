# texto-documentation.ia.md — #115 App do entregador: pedido de iFood e de 99Food

## PROMPT (copiar e colar)

Dentro do menu **Gestão de Entregas**, crie a página **App do entregador: pedido de iFood e de
99Food**.

Leia APENAS os arquivos abaixo:

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/app-entregador-marketplace/app-entregador-marketplace.md`
2. Imagens (na ordem dos nomes, que é a ordem do texto):
   - `.../imagens-tratadas/01-chip-na-lista.png`
   - `.../imagens-tratadas/02-detalhes-ifood.png`
   - `.../imagens-tratadas/03-rodape-ifood.png`
   - `.../imagens-tratadas/04-tela-de-confirmacao-ifood.png`
   - `.../imagens-tratadas/05-codigo-preenchido.png`
   - `.../imagens-tratadas/06-detalhes-99food.png`
   - `.../imagens-tratadas/07-rodape-99food.png`
   - `.../imagens-tratadas/08-tela-de-confirmacao-99food.png`
   - `.../imagens-tratadas/09-copiado-lado-a-lado.png`
   - `.../imagens-tratadas/10-plataforma-nao-carrega.png`
   - `.../imagens-tratadas/11-plataforma-sem-confirmacao.png`

NÃO leia `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`.

- Apresentação IGUAL ao menu "Abrir Caixa".
- pt-BR, didático. Manter as tabelas de setas (nº → onde → o que é) embaixo de cada imagem.
- Avisar, no começo, que a **Gestão de Entregas está em liberação**. Não citar `empresaID`.
- **Este manual é para o entregador.** Tom de quem está com o celular na mão, na rua.
- Manter, sem enxugar:
  (a) a tabela de duas linhas que abre a página — **nada a receber** e **um passo a mais**;
  (b) que **não há linha *Cobrar R$*** no cartão de marketplace, e que isso **não é erro**;
  (c) que **não existe INICIAR COBRANÇA nem FINALIZAR SEM COBRAR** nesses pedidos;
  (d) que o **número laranja é do restaurante** e o **colorido é da plataforma**, cada um para um
  interlocutor;
  (e) o aviso destacado do **formato do código no 99Food**: o aplicativo mostra o que veio no
  pedido (6 dígitos, no exemplo) e o site pede um localizador de **8 dígitos**, que está no
  recibo;
  (f) a seção **A ordem certa das coisas**, com os dois passos numerados, e a frase de que **uma
  coisa não faz a outra**;
  (g) que o **X da tela de confirmação não desfaz nem finaliza nada**;
  (h) que a **tela de confirmação é um site** e precisa de internet;
  (i) as duas perguntas espelhadas do FAQ (*confirmei e esqueci de finalizar* / *finalizei e não
  confirmei*) — são as duas situações reais de suporte;
  (j) a tabela comparativa **iFood contra 99Food** da seção 4, inteira;
  (k) que, na tela de confirmação, **a faixa de cima é do aplicativo e o resto é do site** — faixa
  preenchida com página branca é problema de conexão, não de pedido —, e que o **copiar funciona**
  mesmo com a página vazia;
  (l) que, sem sinal, a página fica branca **sem mensagem de erro**;
  (m) que **a cor do selo não identifica a plataforma**: o da Keeta é amarelo como o do 99Food, e
  quem identifica é a marca dentro do selo;
  (n) que, na plataforma sem confirmação, o rodapé tem **só FINALIZAR**, e o roteiro do entregador
  encurta para conferir, entregar e finalizar.
- A quarta seção existe por causa de uma imagem montada com **duas telas lado a lado**. Publicar a
  imagem uma vez só, com a tabela de duas linhas embaixo, e depois a tabela comparativa.
- Não publicar rotas de API, nomes de campo nem endereços dos sites das plataformas. Em
  particular: não citar `ifoodLocalizer`, `nnID`, `correlationId`, `IfoodView` nem os domínios de
  confirmação do iFood e do 99Food.
- Não afirmar que toda plataforma tem confirmação: a seção 6 mostra o pedido que traz só o selo, e
  isso deve ser mantido como está.
- A seção 6 é a única que fala de coisa dando errado. Manter as duas subseções na ordem, e manter o
  passo a passo do que fazer quando a página não abre — é a parte que o suporte usa.
- Não citar bastidor de captura: nem emulador, nem material recebido, nem que as confirmações não
  foram concluídas, nem que os pedidos são de teste.
- Os nomes de cliente que aparecem nas imagens são de cadastro de teste. Não comentar na página.

## Estrutura da página (mesma numeração do `.md`)

- Para que serve
- Antes de começar
- 1. Como reconhecer na lista
- 2. Pedido de iFood
- 3. Pedido de 99Food
- 4. As duas plataformas, lado a lado
- 5. A ordem certa das coisas
- 6. Dois casos fora do roteiro
- Perguntas frequentes
- Onde continuar

## Anexo — legendas das imagens (na ordem do texto)

1. `01-chip-na-lista.png` — A lista com um pedido de iFood e um de 99Food, cada um com dois
   números.
2. `02-detalhes-ifood.png` — A observação laranja da integração e o selo do iFood junto aos itens.
3. `03-rodape-ifood.png` — O rodapé: PAGO ONLINE, COBRAR R$ 0,00, CONFIRMAR ENTREGA IFOOD e
   FINALIZAR.
4. `04-tela-de-confirmacao-ifood.png` — O site do iFood aberto no aplicativo, com o localizador na
   faixa de cima.
5. `05-codigo-preenchido.png` — Os oito dígitos preenchidos e o Continuar já ativo.
6. `06-detalhes-99food.png` — A observação e o selo amarelo do 99Food.
7. `07-rodape-99food.png` — O rodapé com PIX e o botão amarelo de confirmação.
8. `08-tela-de-confirmacao-99food.png` — O site do 99Food, com as duas etapas e a frase dos 8
   dígitos.
9. `09-copiado-lado-a-lado.png` — Os dois avisos de cópia, um ao lado do outro.
10. `10-plataforma-nao-carrega.png` — A tela de confirmação com o código no alto e a página do site
    em branco.
11. `11-plataforma-sem-confirmacao.png` — Um pedido de plataforma com selo, PAGO ONLINE, COBRAR
    R$ 0,00 e só o FINALIZAR no rodapé.
