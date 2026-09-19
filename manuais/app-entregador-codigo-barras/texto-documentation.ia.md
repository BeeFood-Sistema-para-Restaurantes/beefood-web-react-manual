# texto-documentation.ia.md — #114 Código de barras: ligar a etiqueta e ler o pedido

## PROMPT (copiar e colar)

Dentro do menu **Gestão de Entregas**, crie a página **Código de barras: ligar a etiqueta e ler o
pedido no aplicativo**.

Leia APENAS os arquivos abaixo:

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/app-entregador-codigo-barras/app-entregador-codigo-barras.md`
2. Imagens (nesta ordem):
   - `.../imagens-tratadas/01-impressao-layout.png`
   - `.../imagens-tratadas/02-cupom-texto-padrao.png`
   - `.../imagens-tratadas/03-cupom-impresso.png`
   - `.../imagens-tratadas/04-aba-codigo-barras.png`
   - `.../imagens-tratadas/05-leitor-aberto.png`
   - `.../imagens-tratadas/06-codigo-na-faixa.png`
   - `.../imagens-tratadas/07-etiqueta-ean13.png`

NÃO leia `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`, `*.geo.json`.

- Apresentação IGUAL ao menu "Abrir Caixa".
- pt-BR, didático. Manter as tabelas de setas (nº → onde → o que faz) embaixo de cada imagem.
- Avisar, no começo, que a **Gestão de Entregas está em liberação** e que a tela pode ainda não
  aparecer para todos (falar com o suporte). Não citar `empresaID`.
- **O aviso de que ler é despachar tem de ficar no topo da página**, em destaque, com as três
  consequências (cliente avisado, marketplace avisado, sem desfazer pelo aplicativo). É o ponto
  central do manual.
- Manter, sem enxugar:
  (a) a etiqueta **não vem ligada** — é uma caixinha no layout do **Cupom Pedido**, aba *Texto
  Padrão*, e ela fica no fim do formulário;
  (b) a confusão vizinha: **QR Code Cardápio Digital** é outra coisa;
  (c) a etiqueta só sai em **delivery com entrega**;
  (d) a tabela das **seis** mensagens da faixa de status, incluindo *Pedido já lido* (não é erro) e as
  **duas** de erro, que são casos diferentes: *Erro na leitura, tente novamente* é o envio que não saiu
  do celular, e *Erro: {mensagem}* é a loja recusando. Nas duas o pedido **não** foi despachado;
  (e) só **EAN-13**: QR Code e outros formatos não funcionam;
  (f) o pedido passa a ser de **quem bipou**;
  (g) a pergunta do FAQ sobre "diz sucesso e o pedido não muda": é recurso contratado, falar com
  o suporte.
- Não publicar rotas de API, nomes de tabela, nomes de coluna, nomes de procedure, nomes de
  servidor nem nomes de arquivo do app. Em particular: não citar `lerCodigoBarras`, `apiN3`,
  `preVendaID` nem `SituacaoDeliveryUpdater`.
- Não citar bastidor de captura: nem emulador, nem material recebido, nem que a imagem da faixa
  da câmera foi composta.

## Estrutura da página (mesma numeração do `.md`)

- Para que serve
- Antes de começar
- 1. Ligar a etiqueta no cupom
- 2. Onde a etiqueta sai
- 3. Abrir o leitor no aplicativo
- 4. Ler a etiqueta
- 5. O que a leitura dispara
- 6. A etiqueta é EAN-13, e só
- Perguntas frequentes
- Onde continuar

## Anexo — legendas das imagens (na ordem)

1. `01-impressao-layout.png` — A aba Layout de Configuração → Impressão, com o Cupom Pedido e o
   lápis que abre o layout.
2. `02-cupom-texto-padrao.png` — A aba Texto Padrão do layout, com a caixinha Código de Barras
   App Entrega, a vizinha do QR Code do cardápio e o botão de salvar.
3. `03-cupom-impresso.png` — O cupom do delivery com a etiqueta no pé, depois do endereço.
4. `04-aba-codigo-barras.png` — O rodapé do aplicativo, com a aba Código barras destacada.
5. `05-leitor-aberto.png` — A tela do leitor: título, faixa de status, faixa da câmera entre as
   linhas vermelhas e o botão VOLTAR.
6. `06-codigo-na-faixa.png` — A etiqueta posicionada dentro da faixa da câmera.
7. `07-etiqueta-ean13.png` — A etiqueta EAN-13 que o aplicativo lê.
