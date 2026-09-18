# texto-documentation.ia.md — #113 App do entregador: chegar no endereço

## PROMPT (copiar e colar)

Dentro do menu **Gestão de Entregas**, crie a página **App do entregador: chegar no endereço**.

Leia APENAS os arquivos abaixo:

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/app-entregador-rota/app-entregador-rota.md`
2. Imagens (nesta ordem):
   - `.../imagens-tratadas/01-ver-no-mapa.png`
   - `.../imagens-tratadas/02-google-maps-uma-parada.png`
   - `.../imagens-tratadas/03-rota-na-lista.png`
   - `.../imagens-tratadas/04-cabecalho-da-rota.png`
   - `.../imagens-tratadas/05-outras-entregas.png`
   - `.../imagens-tratadas/07-rota-no-maps.png`
   - `.../imagens-tratadas/06-rota-despachada.png`
   - `.../imagens-tratadas/08-abrir-rota.png`
   - `.../imagens-tratadas/09-melhor-rota-no-maps.png`

NÃO leia `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`.

- Apresentação IGUAL ao menu "Abrir Caixa".
- pt-BR, didático. Manter as tabelas de setas (nº → onde → o que é) embaixo de cada imagem.
- **A ordem das imagens no `.md` não é a ordem do nome do arquivo**: `07` (a rota aberta no Maps)
  vem antes de `06` (o cabeçalho depois de iniciar), porque o texto mostra primeiro o que o toque
  abre e só então o que sobra na tela do aplicativo. Seguir a ordem do texto.
- Avisar, no começo, que a **Gestão de Entregas está em liberação**. Não citar `empresaID`.
- **Este manual é para o entregador.** Tom de quem está com o celular na mão, na rua.
- Manter, sem enxugar, e **sem transformar em nota de pé de página**:
  (a) a tabela dos **três caminhos** que abre a página — ela é o conteúdo principal;
  (b) o bloco de aviso de que **INICIAR ROTA faz duas coisas de uma vez** (avisa a saída e abre o
  mapa), que é **só de ida** e que não se toca nele "para só ver o caminho";
  (c) que o **endereço de uma entrega vai como texto** e por isso o mapa pode cair no lugar
  errado — e que, na dúvida, **vale o endereço do cartão**;
  (d) que o **Waze só aparece para uma entrega** e precisa estar instalado, senão o link abre uma
  página em vez de uma rota;
  (e) que os **números dos cartões da rota são a ordem que o restaurante definiu**;
  (f) que a faixa **OUTRAS ENTREGAS ({N})** só aparece quando há rota e entregas soltas juntas;
  (g) que **MELHOR ROTA GOOGLE MAPS ignora a rota do restaurante** e reordena os avulsos por
  distância — este é o aviso que evita desfazer o trabalho do operador;
  (h) que o **contador do cabeçalho é da rota**, não dos cartões visíveis (o "de 3" com dois
  cartões na tela);
  (i) que **ABRIR NO MAPS só reabre o mapa**, e pode ser tocado à vontade;
  (j) que, com **uma** entrega solta, o botão da melhor rota não aparece.
- Não publicar rotas de API, nomes de tabela, nomes de coluna nem nomes de arquivo do aplicativo.
  Em particular: não citar `CabecalhoRota`, `gestaoEntregaCriarRota` nem nomes de situação interna
  do pedido (*PRONTO*, *PREPARO*, *ENTREGA*).
- **Quatro imagens são telas do Google Maps**, não do aplicativo. Não comentar isso na página: para
  o entregador é a continuação natural do toque.
- Não citar bastidor de captura: nem emulador, nem material recebido, nem que duas imagens são
  recortes de um print maior.
- Os nomes de cliente que aparecem nas imagens são de cadastro de teste. Não comentar na página.

## Estrutura da página (mesma numeração do `.md`)

- Para que serve
- Antes de começar
- 1. Uma entrega: VER NO MAPA
- 2. Quando o restaurante monta a rota
- 3. Várias entregas soltas: MELHOR ROTA
- Perguntas frequentes
- Onde continuar

## Anexo — legendas das imagens (na ordem do texto)

1. `01-ver-no-mapa.png` — A folha que sobe ao tocar em VER NO MAPA, com GOOGLE MAPS e WAZE.
2. `02-google-maps-uma-parada.png` — A rota de uma entrega no Google Maps: origem, destino, tempo
   e distância.
3. `03-rota-na-lista.png` — A lista com a ROTA A no alto e as paradas numeradas abaixo.
4. `04-cabecalho-da-rota.png` — O cabeçalho da rota: letra, nome, contador e INICIAR ROTA.
5. `05-outras-entregas.png` — A faixa OUTRAS ENTREGAS (1) e o cartão solto.
6. `07-rota-no-maps.png` — A rota de três paradas no Google Maps, com "2 stops" no meio.
7. `06-rota-despachada.png` — O cabeçalho depois de iniciar: a etiqueta *em rota* e o botão azul
   ABRIR NO MAPS.
8. `08-abrir-rota.png` — O botão MELHOR ROTA GOOGLE MAPS (4) e a janela ABRIR ROTA.
9. `09-melhor-rota-no-maps.png` — As quatro paradas no Google Maps, com "3 stops" no meio.
