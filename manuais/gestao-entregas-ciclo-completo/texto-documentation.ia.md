# texto-documentation.ia.md — #117 Uma entrega do começo ao fim

## PROMPT (copiar e colar)

⛔ **REGRA ZERO — o manual é "como eu uso", nunca "como o sistema faz".**

- A página sai **somente** do `gestao-entregas-ciclo-completo.md`
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

Dentro do menu **Gestão de Entregas**, crie a página **Uma entrega do começo ao fim: painel e
aplicativo lado a lado**.

Leia APENAS os arquivos abaixo:

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/gestao-entregas-ciclo-completo/gestao-entregas-ciclo-completo.md`
2. Imagens (na ordem dos nomes, que é a ordem do texto):
   - `.../imagens-tratadas/01-fila-de-pedidos.png`
   - `.../imagens-tratadas/02-rota-montada.png`
   - `.../imagens-tratadas/03-rota-no-app.png`
   - `.../imagens-tratadas/04-confirmar-despacho.png`
   - `.../imagens-tratadas/05-em-rota-no-app.png`
   - `.../imagens-tratadas/06-primeira-parada.png`
   - `.../imagens-tratadas/07-mapa-ao-vivo.png`
   - `.../imagens-tratadas/08-cobranca-concluida.png`
   - `.../imagens-tratadas/09-uma-de-tres.png`
   - `.../imagens-tratadas/10-lista-sem-a-rota.png`
   - `.../imagens-tratadas/11-rota-fora-da-tela.png`
   - `.../imagens-tratadas/12-relatorio-do-dia.png`
   - `.../imagens-tratadas/13-historico-do-dia.png`

NÃO leia `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`.

- Apresentação IGUAL ao menu "Abrir Caixa".
- pt-BR, didático. Manter as tabelas de setas (nº → onde → o que é) embaixo de cada imagem.
- Avisar, no começo, que a **Gestão de Entregas está em liberação**. Não citar `empresaID`.
- **Este manual tem dois leitores ao mesmo tempo**: o operador do painel e o entregador com o
  celular na mão. O tom é de quem explica a mesma cena para os dois lados. Não transformar em
  manual só do painel.
- Manter, obrigatoriamente e sem enxugar, os blocos de aviso:
  (a) **as duas metades são a mesma viagem** — os mesmos três pedidos e a mesma rota. É o que dá
  autoridade ao manual, e é a primeira coisa que o leitor precisa saber;
  (b) que **não é manual de primeira leitura**, com o link para *Montar a rota*;
  (c) **pedido pronto não é pedido atribuído** — a explicação do momento 1 e a razão de o celular
  estar vazio;
  (d) que a **rota chega no celular antes do despacho**, e que o **INICIAR ROTA** do aplicativo tem
  o mesmo efeito do avião do painel, sem volta;
  (e) que o **MELHOR ROTA desfaz a ordem que o operador montou**;
  (f) que a **ordem certa é cozinha pronta → entregador na porta → despachar**;
  (g) que **pino parado não é entregador parado**, com a bateria e a idade da última posição;
  (h) que **cobrar é finalizar**, e que a baixa pelo celular registra forma e valor enquanto a do
  painel registra só que chegou;
  (i) que a **rota se encerra sozinha na última baixa** e **sai da tela** — e que o botão de
  finalizar serve para o outro caso, confirmando todas as paradas pendentes sem confirmação;
  (j) que **lista vazia com a pílula ONLINE acesa é fim de viagem**, não queda de internet;
  (k) que as **médias de tempo do relatório pedem volume** (mínimo 20 pedidos), e que
  *Taxas do entregador* em branco é entregador sem valor configurado — nos dois casos, não é erro.
- Manter a seção **Como as duas telas se encontram** inteira, com a tabela e a frase final sobre a
  pergunta que funciona ao telefone. É a seção mais útil do manual para o suporte.
- Manter a tabela **O ciclo, em sete momentos** logo no começo, e a frase que diz que a primeira
  linha é a mais importante.
- Manter a seção **O mesmo ciclo, sem operador** e as **cinco coisas que a operação de verdade
  ensina**.
- Não publicar rotas de API, nomes de tela do aplicativo, nomes de tabela nem de coluna. Em
  particular: não citar `_PreVenda`, `FuncionarioIDMotoboy`, `situacaoDelivery`,
  `SituacaoDeliveryUpdater`, `viewRotaAberta`, `rota.status` nem os nomes internos de situação.
- Não citar bastidor de captura: nem emulador, nem material recebido, nem que a metade do painel
  foi reencenada com os mesmos pedidos, nem que o relatório do dia foi limpo antes da imagem.
- Não citar que o relógio da barra de status do emulador estava adiantado, nem que os recortes
  começam abaixo dela.
- Não citar Android nem iOS: o manual fala do aplicativo, não do sistema do aparelho.
- Os nomes de cliente e o nome do entregador que aparecem nas imagens são de cadastro de teste. Não
  comentar na página.

## Estrutura da página (mesma numeração do `.md`)

- Para que serve
- Antes de começar
- O ciclo, em sete momentos
- 1. Os pedidos prontos, e o celular vazio
- 2. A rota montada, e a rota que chega
- 3. O despacho: um clique que avisa o mundo
- 4. A rua
- 5. A porta do cliente
- 6. O fim da viagem
- 7. O que sobra do dia
- Como as duas telas se encontram
- O mesmo ciclo, sem operador
- As cinco coisas que a operação de verdade ensina
- Onde continuar

## Anexo — legendas das imagens (na ordem do texto)

1. `01-fila-de-pedidos.png` — A fila com três pedidos prontos, sem rota, e o entregador parado na
   loja.
2. `02-rota-montada.png` — A rota A montada: entregador escolhido, *Pronta para sair*, *0 de 3
   entregues* e o avião ainda por clicar.
3. `03-rota-no-app.png` — A lista do aplicativo com o grupo ROTA A recém-chegado e o INICIAR ROTA.
4. `04-confirmar-despacho.png` — A janela de confirmação do despacho, com as três paradas.
5. `05-em-rota-no-app.png` — O cabeçalho da rota com a etiqueta *em rota* e o ABRIR NO MAPS.
6. `06-primeira-parada.png` — Os detalhes da primeira parada: endereço, observação, itens e COBRAR.
7. `07-mapa-ao-vivo.png` — O mapa com o pino longe da loja, a rota *Na rua* e *Entregando agora*.
8. `08-cobranca-concluida.png` — A tela Pagamento Confirmado!, com o valor registrado.
9. `09-uma-de-tres.png` — A primeira parada entregue e o contador em *1 de 3*.
10. `10-lista-sem-a-rota.png` — A lista do aplicativo vazia, com a pílula ONLINE acesa.
11. `11-rota-fora-da-tela.png` — O painel de rotas vazio e o contador do dia em *3 entregues*.
12. `12-relatorio-do-dia.png` — Operação de Entrega com a data de hoje: *Entregas 3* e
    *R$ 126,60*.
13. `13-historico-do-dia.png` — O Histórico do dia com as três entregas e as horas das baixas.
