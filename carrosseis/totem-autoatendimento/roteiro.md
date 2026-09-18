# Totem de Autoatendimento: o cliente pede e paga sozinho

- **Gênero:** função do sistema (a segunda peça do gênero, depois de
  `dark-kitchen-multimarcas`)
- **Pauta:** [`beefood.com.br/totem-de-autoatendimento`](https://beefood.com.br/totem-de-autoatendimento/)
  — **a página não tem conteúdo publicado**, ver a seção abaixo
- **Manuais lidos:** nenhum documenta o totem. Sustentam parte do fato:
  [`venda-sugestiva-upsell`](../../manuais/venda-sugestiva-upsell/venda-sugestiva-upsell.md)
  (a sugestão vale no totem, e o produto desativado no totem fica de fora) e
  [`traducao-cardapio-presencial`](../../manuais/traducao-cardapio-presencial/traducao-cardapio-presencial.md)
  (o totem se configura em `Aplicativos → Totem de Autoatendimento`)
- **Formato:** 4:5 (1080×1350), 7 slides
- **Imagens:** 6 **capturas** do aplicativo de produção (`capturar-telas.py`).
  Nenhuma tela desenhada

## A página está vazia, e por isso o fato vem da tela

`beefood.com.br/totem-de-autoatendimento/` responde com o menu, o rodapé e um
`Carregando…` no lugar do corpo — conferido no HTML servido e com a página
renderizada no navegador. O `pauta.py --pagina` devolve dois blocos sem texto.

Da página sobra uma frase, a descrição que ela dá ao buscador:

> *Deixe seus clientes fazerem pedidos e pagamentos diretamente no totem de
> autoatendimento enquanto sua equipe foca em outras questões.*

É afirmação funcional, e é dela que sai o **ângulo**. Fato ela não é: a régua
segue sendo **manual > tela capturada > tela desenhada**, e aqui o degrau que
existe é o do meio, que é melhor do que a peça de dark kitchen teve. O totem é
web (`totem.beefood.app`), abre no Playwright e tem uma loja de exemplo com
cardápio de verdade — então **tudo o que a peça mostra é print do aplicativo de
produção**, e tudo o que ela afirma foi visto ali ou está num manual.

O que é nosso nas capturas: só a **arte de fundo**. A loja de exemplo anuncia um
pudim na tela de espera e na faixa do cardápio, e num post sobre autoatendimento
o olho lê o preço do pudim em vez da tela. Entram as duas artes de
`assets/fundos/`, pela mesma interceptação que o carrossel de tradução usa.

**Nenhum pedido foi criado.** O roteiro de captura para no botão `Ir para
pagamento`, que é a última tela antes do pinpad.

## O fato, inteiro

Conferido tela por tela, do toque até o pagamento:

1. **a tela de espera tem um botão só**, `FAÇA SEU PEDIDO`, em cima de uma arte
   em tela cheia — que é a que a loja sobe no sistema.
2. **o cardápio é o da loja**: setores na coluna da esquerda, e cada item com
   foto, nome e preço. Combo sai como `A partir de R$ 35,90`; item avulso sai
   com preço fechado (`ONE BURGER R$ 24,00`).
3. **o totem conduz a montagem por grupos numerados.** No hambúrguer avulso são
   três: `QUER TURBINAR O SEU BURGER? Escolha até 4`, com adicional e preço
   (`+ R$ 4,00` o bacon, `+ R$ 8,00` a carne), e `QUER RETIRAR ALGUM
   INGREDIENTE?`, com as retiradas `Grátis`. Cada passo tem `Pular`, e o total
   na barra de baixo sobe junto.
4. **grupo obrigatório trava o avanço.** No combo, `Obrigatório 0/1`, e o
   aplicativo responde *Necessário selecionar uma opção para "BURGER"*.
5. **a sacola sugere o que falta**: bloco `Peça também` com o selo `Gerada por
   IA`, e os itens com foto e preço.
6. **o totem pergunta como será o pedido**: `Para viagem` (Levar o pedido) ou
   `Comer aqui` (Consumo no local).
7. **o pagamento é no próprio aparelho.** A barra de baixo mostra `Total` e o
   botão é `Ir para pagamento`.
8. **a loja escolhe o que não entra.** `Desativar Totem`, no menu do produto,
   tira o item do totem — e ele não é oferecido nem na venda sugestiva, mesmo
   estando na lista (manual `venda-sugestiva-upsell`).
9. **a sugestão é a mesma do painel**, e o que ela vendeu sai em `Desempenho →
   Presencial → Sugestões` (manual `venda-sugestiva-upsell`).
10. **o totem se configura no painel**, em `Aplicativos → Totem de
    Autoatendimento → aba Configuração` (manual `traducao-cardapio-presencial`).

Fora da peça: a identificação por telefone e nome, e o cashback que ela dá. A
tela existe e foi capturada, mas o que apareceria na arte são o nome e o
telefone de teste que o script digita — e o assunto do post não é cadastro de
cliente. A tradução do cardápio também fica de fora: já é a peça
`traducao-cardapio-presencial`.

## O ângulo, e de onde ele sai

O ângulo é **o pedido que não passa por ninguém**: o cliente escolhe, monta,
decide se come ali ou leva e paga, tudo na mesma tela. Ele sai do que a empresa
afirma do próprio produto ("pedidos e pagamentos diretamente no totem") e do que
a tela mostra — não de cena inventada sobre a rotina de ninguém. A peça não diz
que existe fila no balcão dele, não diz quantos atendentes ele tem e não promete
economia: nada disso está na tela nem no manual.

| Fato | Ângulo | O que o slide diz |
|---|---|---|
| Da tela de espera ao `Ir para pagamento`, quem toca é o cliente | o pedido inteiro acontece sem ninguém do outro lado | "O cliente pede **e paga** sozinho no totem" (1) |
| Cinco toques do começo ao fim, todos na mesma tela | quem nunca viu um não sabe até onde o aparelho vai | "O totem conduz o pedido do começo ao fim" (2) |
| O cardápio do totem é o cadastro da loja, com foto e preço | é o cardápio dele, não um cardápio à parte para manter | "O cardápio do totem é o seu" (3) |
| `QUER TURBINAR O SEU BURGER?` oferece bacon a `+ R$ 4,00` em todo pedido | o adicional é o que sobe o ticket, e ele é oferecido sempre | "Ofereça o adicional em todo pedido" (4) |
| `Peça também`, com o selo `Gerada por IA`, na sacola | a última chance de vender é antes de fechar | "E a sacola ainda sugere o que falta" (5) |
| `Para viagem` ou `Comer aqui`, `Total` e `Ir para pagamento` | o cliente sai do totem com o pedido pago | "Comer aqui ou levar, e o pagamento termina ali" (6) |
| O aparelho, o cardápio e o pagamento estão na página do sistema | quem lê pode não ter conta | "Conheça o totem por dentro" (7) |

## Os slides

| # | Arquivo | Tipo | Ideia única | Imagem |
|---|---|---|---|---|
| 1 | `01-capa.html` | capa com imagem | o cliente pede e paga sozinho | o totem inteiro, com a tela de espera (captura) |
| 2 | `02-como-funciona.html` | texto + lista | o aparelho vai do toque ao pagamento | nenhuma: são os cinco passos em lista |
| 3 | `03-cardapio.html` | recorte grande | o cardápio do totem é o cadastro da loja | topo do cardápio: setores, foto e preço (captura) |
| 4 | `04-adicional.html` | recorte grande | o adicional é oferecido em todo pedido | `QUER TURBINAR O SEU BURGER?` com os preços (captura) |
| 5 | `05-peca-tambem.html` | recorte largo | a sacola sugere antes de fechar | `Peça também` com o selo `Gerada por IA` (captura) |
| 6 | `06-pagamento.html` | dois recortes | o pagamento termina no aparelho | `Como será o pedido?` e `Ir para pagamento` (capturas) |
| 7 | `07-cta.html` | capa + mockup | a página do sistema | o totem com o cardápio, sangrando pela base (captura) |

## Decisões de arte

**A capa é o aparelho inteiro, e não um recorte de tela.** O assunto é o cliente
de pé na frente de uma máquina: sem a máquina, o post vira "cardápio digital".
O `.totem` vai reto, como manda a `mockups.md` — armário em pé girado lê como
armário tombando — e a tela é a captura de 720p, porque em 1080p reduzida para
420 px o `FAÇA SEU PEDIDO` vira um risco vermelho.

**Do slide 3 ao 6 o print vai sem aparelho em volta.** É a escolha contrária à
da capa, e pelo mesmo motivo: ali a tela precisa ser **lida**. A tela do totem é
1080×1920; dentro de um mockup de 420 px de largura a letra do cardápio sai com
11 px no feed. Recortada e mostrada com 940 px de largura, a mesma letra sai com
24 px. O aparelho já foi estabelecido na capa, e o `.recorte` preto continua
lendo como tela de totem porque o aplicativo é escuro.

**Cada recorte é uma faixa contínua da tela, nunca uma montagem.** O slide 6 tem
dois recortes porque são duas partes distantes da mesma tela — o topo e a barra
de baixo — e entre elas há 800 px de fundo vazio. Empilhá-las coladas as faria
passar por uma tela só, que é o que elas não são; por isso vão separadas, com
espaço e com legenda própria.

**O item é avulso, não combo.** No combo o preço aparece como `A partir de
R$ 35,90`, e a peça fala de preço e de adicional com valor fechado. `ONE BURGER
R$ 24,00` mais `+ R$ 4,00` de bacon é uma conta que o leitor acompanha.

**O CTA repete o aparelho, com o cardápio na tela.** No fim a tela não precisa
ser lida — precisa dizer "é o mesmo aparelho do começo". Ele sangra pela base,
que é o que a `mockups.md` autoriza no totem: a borda de baixo lê como chão.
