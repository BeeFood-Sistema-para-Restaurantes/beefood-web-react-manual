# texto-documentation.ia.md — #112 App do entregador: as entregas do dia e o histórico

## PROMPT (copiar e colar)

Dentro do menu **Gestão de Entregas**, crie a página **App do entregador: as entregas do dia e o
histórico**.

Leia APENAS os arquivos abaixo:

1. Conteúdo (use na íntegra):
   `beefood-web-react-manual/manuais/app-entregador-entregas-do-dia/app-entregador-entregas-do-dia.md`
2. Imagens (nesta ordem):
   - `.../imagens-tratadas/01-lista.png`
   - `.../imagens-tratadas/02-cartao.png`
   - `.../imagens-tratadas/03-fim-da-lista.png`
   - `.../imagens-tratadas/04-detalhes.png`
   - `.../imagens-tratadas/06-conferir-destaque.png`
   - `.../imagens-tratadas/05-rodape.png`
   - `.../imagens-tratadas/07-sem-complemento.png`
   - `.../imagens-tratadas/08-historico-dias.png`
   - `.../imagens-tratadas/09-dia-expandido.png`
   - `.../imagens-tratadas/10-detalhe-no-historico.png`

NÃO leia `fluxo-codigo.md`, `MEMORIA*.md`, `annotate.py`, `imagens-puras/`.

- Apresentação IGUAL ao menu "Abrir Caixa".
- pt-BR, didático. Manter as tabelas de setas (nº → onde → o que é) embaixo de cada imagem.
- **A ordem das imagens no `.md` não é a ordem do nome do arquivo**: a folha de conferência
  (`06`) aparece antes do rodapé (`05`), porque ela pertence à seção do item em destaque. Seguir
  a ordem do texto.
- Avisar, no começo, que a **Gestão de Entregas está em liberação**. Não citar `empresaID`.
- **Este manual é para o entregador.** Tom de quem está com o celular na mão, na rua.
- Manter, sem enxugar:
  (a) que a lista vem ordenada por **distância da loja**, e que pedido sem coordenada cai no fim;
  (b) que os **círculos numerados são do aplicativo** e valem a posição na sequência — não são o
  número do pedido;
  (c) que a lista **não tem** botão de cobrar nem de finalizar, de propósito;
  (d) que o **complemento é vermelho porque é o que mais se erra**;
  (e) que a **linha preta é conferência**, marcada linha a linha, e que ela abre uma folha de
  confirmação antes de cobrar ou finalizar;
  (f) que a **forma de pagamento é a que o cliente informou**, e pode ser trocada na cobrança;
  (g) que **o que não existe não aparece** — sem complemento, sem observação, sem coluna TROCO;
  (h) que o aplicativo **não tem filtro de data** no histórico, e que ele mostra só as entregas
  daquele entregador;
  (i) que a **observação escrita ao finalizar fica registrada para sempre**;
  (j) que os itens do pedido são buscados ao abrir o detalhe — sem internet, o cartão fica vazio.
- Não publicar rotas de API, nomes de tabela, nomes de coluna nem nomes de arquivo do aplicativo.
  Em particular: não citar `ItemEntrega`, `preVendaID`, `tipoPagStr` nem `entrega2/gestao`.
- Não citar bastidor de captura: nem emulador, nem material recebido, nem que duas imagens são
  recortes de um print maior.
- Os nomes de cliente que aparecem nas imagens são de cadastro de teste. Não comentar na página.

## Estrutura da página (mesma numeração do `.md`)

- Para que serve
- Antes de começar
- 1. A lista de entregas
- 2. Os detalhes da entrega
- 3. O histórico
- Perguntas frequentes
- Onde continuar

## Anexo — legendas das imagens (na ordem do texto)

1. `01-lista.png` — A lista com quatro entregas, com a faixa vermelha da sequência.
2. `02-cartao.png` — Um cartão da lista: número do pedido, previsão, flecha, círculo da parada e
   Cobrar R$.
3. `03-fim-da-lista.png` — O fim da lista, com ATUALIZAR e MELHOR ROTA GOOGLE MAPS (4).
4. `04-detalhes.png` — Os detalhes da entrega: endereço fixo, complemento, observações, VER NO
   MAPA, itens e a linha preta do item em destaque.
5. `06-conferir-destaque.png` — A folha CONFIRMA E ENTREGA DESSES PRODUTOS CORRETAMENTE?
6. `05-rodape.png` — O rodapé escuro: forma de pagamento, TOTAL / TROCO / COBRAR e os dois
   botões.
7. `07-sem-complemento.png` — Um pedido sem complemento e pago em Pix, sem a coluna TROCO.
8. `08-historico-dias.png` — O histórico agrupado por dia.
9. `09-dia-expandido.png` — As entregas de um dia, com o `!` de atraso e a etiqueta do
   marketplace.
10. `10-detalhe-no-historico.png` — O detalhe no histórico, com VALOR TOTAL DO PEDIDO e a linha do
    tempo.
