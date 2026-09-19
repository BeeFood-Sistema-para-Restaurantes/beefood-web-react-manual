# Totem de Autoatendimento: o cliente pede e paga sozinho

- **Gênero:** função do sistema (a segunda peça do gênero, depois de
  `dark-kitchen-multimarcas`)
- **Pauta:** [`beefood.com.br/totem-de-autoatendimento`](https://beefood.com.br/totem-de-autoatendimento/),
  que é **servida por um app externo** — ver a seção abaixo
- **Manuais lidos:** nenhum documenta o totem. Sustentam parte do fato:
  [`venda-sugestiva-upsell`](../../manuais/venda-sugestiva-upsell/venda-sugestiva-upsell.md)
  (a sugestão vale no totem, e o produto desativado no totem fica de fora),
  [`cupom-desconto`](../../manuais/cupom-desconto/cupom-desconto.md) (o totem é
  um dos **canais de visibilidade** do cupom),
  [`cashback-configurar`](../../manuais/cashback-configurar/cashback-configurar.md)
  (o totem é uma das **modalidades** do cashback, e o saldo cai em venda
  quitada) e
  [`traducao-cardapio-presencial`](../../manuais/traducao-cardapio-presencial/traducao-cardapio-presencial.md)
  (o totem se configura em `Aplicativos → Totem de Autoatendimento`)
- **Formato:** 4:5 (1080×1350), 9 slides
- **Imagens:** 9 **capturas** do aplicativo de produção — 7 do
  `capturar-telas.py` desta pasta e 2 do `capturar-totem.py` da skill, que é o
  mesmo script do carrossel da tradução. Nenhuma tela desenhada

## A página parecia vazia, e não estava

**A primeira leitura desta pauta estava errada, e vale mais do que a correção.**
`beefood.com.br/totem-de-autoatendimento/` responde com o menu, o rodapé e um
`<div class="super-loader">Carregando…</div>` no lugar do corpo. Foi conferido
no HTML servido, na REST do WordPress e com a página aberta no navegador — as
três coisas devolveram a mesma casca, e a conclusão foi que a página não tinha
conteúdo publicado. A peça inteira foi escrita nessa premissa.

Ela é falsa. O conteúdo existe e é montado por um **app externo**: o endereço
está no próprio HTML da casca, e o app entrega HTML pronto.

```
https://beefood.com.br/totem-de-autoatendimento/  →  casca com "Carregando…"
https://beefood-com-br.lovable.app/totem          →  a página de verdade
```

Lá estão a seção de fidelidade, a demonstração do aparelho e o FAQ. O
`pauta.py` agora **percebe a casca e segue o endereço** — a correção é de
ferramenta, porque diagnóstico que depende de alguém lembrar não se repete.

Isso não muda a régua do fato, que segue sendo **manual > tela capturada >
página**: página de vendas é pauta. O que muda é que a pauta existe, e ela
pautou duas coisas nesta rodada — a capa e o CTA.

O totem é web (`totem.beefood.app`), abre no Playwright e tem uma loja de
exemplo com cardápio de verdade, então **tudo o que a peça mostra continua
sendo print do aplicativo de produção**, e tudo o que ela afirma foi visto ali
ou está num manual.

**Nenhum pedido foi criado.** O roteiro de captura para no botão `Ir para
pagamento`, que é a última tela antes do pinpad, e não toca no `Aplicar cupom`,
que é um POST ao servidor da loja.

### O que entra de fora da loja, e por quê

Duas coisas, as duas pela interceptação de API que a skill já usava no carrossel
da tradução:

| O que | Por quê | De onde vem |
|---|---|---|
| a **arte de fundo** da tela de espera e da faixa do cardápio | a loja de exemplo anuncia um pudim com preço, e num post sobre autoatendimento o olho lê o preço do pudim em vez da tela | `assets/fundos/` |
| a **lista de cupons** | `venda2/cupomDescontoAtivo?tipo=totem` responde `[]`, e sem lista o totem **esconde a tela de cupom inteira** | [`cupons.json`](cupons.json) |
| a **tradução** do cardápio (slide 8) | a loja de exemplo tem `aaTraducao: null`, e sem isso o totem esconde o seletor de idioma | [`traducoes.json`](../traducao-cardapio-presencial/traducoes.json) do carrossel da tradução |

O que o arquivo de cupons tem é o que o restaurante escreveria no painel:
código, título, benefício e regra. O aplicativo lê esses campos da resposta sem
traduzir nada, e quem desenha a tela, os cartões tracejados e o campo de código
é ele. O recorte do slide 5 **começa abaixo do cabeçalho**, onde está o
logotipo da loja: cupom de exemplo não pode parecer promoção anunciada por um
cliente nosso.

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
6. **o cupom tem tela própria no totem.** Na confirmação há a linha `Cupom de
   desconto` com o selo `2 cupons disponíveis`; ela abre `Adicionar cupom`, com
   o campo `Digite o código`, o botão `Aplicar cupom` e a lista `Cupons
   disponíveis`, cada cartão com código, benefício e as regras. Cupom de
   primeira compra ou de um uso por cliente ganha o selo `Login`, porque exige
   telefone. O manual `cupom-desconto` confirma o totem entre os **canais de
   visibilidade**, e que a confirmação por SMS existe no cardápio digital e no
   totem.
7. **o cashback aparece três vezes, e nasce no telefone.** No item: `Ganha
   R$ 1,20 em cashback!`. Na identificação: `Insira seu telefone e ganhe 5% de
   cashback`. Na confirmação: a carteira do cliente (`Carteira vazia… por
   enquanto!`, para quem não tem saldo) e, na barra, `Você ganhará de cashback
   R$ 1,20`. Quem tem saldo vê `Cashback disponível` e o botão `Usar`. O manual
   `cashback-configurar` confirma o totem entre as **modalidades** e diz que o
   crédito entra em pedido **pago e finalizado**.
8. **cupom e cashback não se somam.** O próprio aplicativo avisa: *Não combina
   com cupom — remova o cupom para usar.*
9. **o totem pergunta como será o pedido**: `Para viagem` (Levar o pedido) ou
   `Comer aqui` (Consumo no local).
10. **o pagamento é no próprio aparelho.** A barra de baixo mostra `Total` e o
    botão é `Ir para pagamento`.
11. **a loja escolhe o que não entra.** `Desativar Totem`, no menu do produto,
    tira o item do totem — e ele não é oferecido nem na venda sugestiva, mesmo
    estando na lista (manual `venda-sugestiva-upsell`).
12. **o totem se configura no painel**, em `Aplicativos → Totem de
    Autoatendimento → aba Configuração` (manual `traducao-cardapio-presencial`).
13. **o aparelho fala português, inglês e espanhol.** O seletor é uma pílula de
    três bandeiras, na tela de espera (abaixo do `FAÇA SEU PEDIDO`) e no topo
    do cardápio. Escolhido o idioma, mudam setor, nome e descrição — e os
    textos do próprio aplicativo (`CANCEL ORDER`, `Your bag is empty`). Foto e
    preço não mudam: `FRENCH FRIES` e `PAPAS FRITAS` são o mesmo item a
    `R$ 11,00`. O manual `traducao-cardapio-presencial` confirma o totem como
    um dos dois aparelhos em que as bandeiras aparecem.

E dois fatos que são **da página**, achados só na segunda leitura:

14. **a própria página roda um pedido inteiro no aparelho**, do `FAÇA SEU
    PEDIDO` ao pagamento, com barra de progresso, botão de pausa e setas para
    andar tela a tela. É o único fato desta peça que está na página e em lugar
    nenhum mais, e é ele que sustenta o CTA.
15. **a página anuncia cashback, cupons, fidelidade por pontos, WhatsApp e
    CRM** como um conjunto, na seção *Transforme cada venda em uma nova
    oportunidade de compra*. Cada item é um **cartão com ícone, nome e uma
    linha de descrição** — e é desse desenho que saíram os selos da capa. Dos
    cinco, a peça só anuncia os dois que ela prova na tela do totem.

Fora da peça: a tela da carteira de cashback na confirmação (o recorte
mostraria o nome e o telefone de teste que o script digita), o aviso de que
cupom e cashback não se combinam (é regra fina, e o slide entrega uma ideia só)
e a tradução do cardápio, que já é a peça `traducao-cardapio-presencial`.

## O ângulo, e de onde ele sai

O ângulo é **o pedido que não passa por ninguém**: o cliente escolhe, monta,
aplica o cupom, deixa o telefone do cashback, decide se come ali ou leva e paga,
tudo na mesma tela. Ele sai do que a empresa afirma do próprio produto
("pedidos e pagamentos diretamente no totem") e do que a tela mostra — não de
cena inventada sobre a rotina de ninguém. A peça não diz que existe fila no
balcão dele, não diz quantos atendentes ele tem, não promete economia e não
promete que o cliente volta: nada disso está na tela nem no manual.

| Fato | Ângulo | O que o slide diz |
|---|---|---|
| Da tela de espera ao `Ir para pagamento`, quem toca é o cliente | o pedido inteiro acontece sem ninguém do outro lado | "O cliente pede **e paga** sozinho no totem" (1) |
| Seis toques do começo ao fim, todos na mesma tela | quem nunca viu um não sabe até onde o aparelho vai | "O totem conduz o pedido do começo ao fim" (2) |
| O cardápio do totem é o cadastro da loja, com foto e preço | é o cardápio dele, não um cardápio à parte para manter | "O cardápio do totem é o seu" (3) |
| `QUER TURBINAR O SEU BURGER?` no item e `Peça também` na sacola | o aparelho oferece mais duas vezes, e sem depender de quem atende | "Ofereça o adicional duas vezes no mesmo pedido" (4) |
| `Cupom de desconto` é linha na confirmação, com campo de código e lista | o cupom do CRM não para no delivery | "O seu cupom vale no totem também" (5) |
| `Insira seu telefone e ganhe 5% de cashback` | o autoatendimento não é anônimo: ele cadastra e credita | "Quem deixa o telefone ganha cashback" (6) |
| `Para viagem` ou `Comer aqui`, `Total` e `Ir para pagamento` | o cliente sai do totem com o pedido pago | "Comer aqui ou levar, e o pagamento termina ali" (7) |
| A pílula de três bandeiras, e o mesmo item em `FRENCH FRIES` e `PAPAS FRITAS` | quem não fala português também pede sem ninguém do outro lado | "E o mesmo cardápio fala a língua de quem chega" (8) |
| A página tem a seção de plataforma inteira — PDV, KDS, fiscal, estoque, fidelidade | quem lê pode não ter conta, e o totem é uma porta para o resto | "Conheça todas as funcionalidades" (9) |

## Os slides

| # | Arquivo | Tipo | Ideia única | Imagem |
|---|---|---|---|---|
| 1 | `01-capa.html` | capa com cena | o cliente pede e paga sozinho, e a fidelidade entra no pedido | o totem inteiro com o cardápio, e dois `.selo-recurso`: `Cupom` e `Cashback` |
| 2 | `02-como-funciona.html` | texto + lista | o aparelho vai do toque ao pagamento | nenhuma: são os seis passos em lista |
| 3 | `03-cardapio.html` | recorte grande | o cardápio do totem é o cadastro da loja | topo do cardápio: setores, foto e preço |
| 4 | `04-venda-sugestiva.html` | dois recortes | o totem oferece mais em dois momentos | `QUER TURBINAR O SEU BURGER?` e `Peça também` |
| 5 | `05-cupom.html` | recorte grande | o cupom do CRM funciona no aparelho | `Adicionar cupom` e a lista `Cupons disponíveis` |
| 6 | `06-cashback.html` | recorte largo | o totem cadastra e credita | `Insira seu telefone e ganhe 5% de cashback` |
| 7 | `07-pagamento.html` | dois recortes | o pagamento termina no aparelho | `Como será o pedido?` e `Ir para pagamento` |
| 8 | `08-idiomas.html` | dois recortes lado a lado | o aparelho atende quem não fala português | o mesmo cartão em `FRENCH FRIES` e `PAPAS FRITAS` |
| 9 | `09-cta.html` | capa + mockup | a página do sistema, que tem mais do que o carrossel mostrou | o totem parado, na tela de espera |

## Decisões de arte

**A capa é o aparelho inteiro, e não um recorte de tela.** O assunto é o cliente
de pé na frente de uma máquina: sem a máquina, o post vira "cardápio digital".
O `.totem` vai reto, como manda a `mockups.md` — armário em pé girado lê como
armário tombando.

**Na tela da capa vai o cardápio, e a tela de espera foi para o fim.** A regra é
da skill: *na capa, tela cheia ganha de tela ícone*. A tela de espera é uma foto
com um botão, e dentro de um aparelho de 360 px vira mancha escura com um risco
vermelho; o cardápio tem nove cartões com foto, nome e preço, e lê "aqui se
compra" mesmo pequeno. No slide 8 a ordem se inverte: ali o aparelho parado,
esperando o próximo cliente, fecha o arco — e repetir a mesma tela nas duas
pontas seria repetir a imagem.

**Os dois selos da capa são a promessa da peça.** Cupom e cashback são o que o
carrossel entrega além do pedido, e sem eles a capa promete menos do que a peça
tem. Eles são desenhados, e não recortados da tela: o recorte real da linha de
cupom tem 1032 px de largura e, reduzido para caber ao lado do aparelho, fica
ilegível — e posto por cima do vidro cobriria nome e preço de produto, que é o
que a `mockups.md` chama de defeito de render.

**E o selo tem duas alturas, porque uma não cabe.** Ao lado de um aparelho em
pé sobra uma coluna de ~320 px, e nela um selo de uma linha só entra em corpo
22 — que ao lado de um título de 68 lê como legenda de rodapé, não como
promessa. Quebrado em nome grande (`Cupom`, `Cashback`) e nota em caixa alta
(`DE DESCONTO`, `COM O TELEFONE`), o nome vai a 50 px e sobrevive à miniatura
do feed. Virou o `.selo-recurso` da `base.css`.

**O selo amarelo diz `Cashback`, e não `5% de cashback`.** Os 5% são a
configuração da loja de exemplo. Dentro da captura do slide 6 eles saem da tela
do cliente e são o que são; num selo desenhado sairiam da nossa boca, e a capa
passaria a dizer que o sistema define a porcentagem — que quem configura o
programa escolhe. Na peça, número que o lojista define só aparece **dentro de
print**.

**A nota do selo amarelo não pode somar com a do vermelho.** Cupom e cashback
não se combinam (fato 8), então `NO MESMO PEDIDO` estava fora: os dois selos
lado a lado já sugerem soma, e a nota não podia confirmar. `COM O TELEFONE` diz
de onde o cashback nasce, que é o fato 7, e é o que o slide 6 desenvolve.

**E os selos deixaram de ser adesivo quando entraram atrás do aparelho.** A
volta do dono foi *"é a questão do layout do design mesmo, tá só um texto com
um painel atrás"*, e estava certa: dois retângulos coloridos pousados na arte
não têm relação nenhuma com o totem. O que resolveu não foi mais efeito, foi
**oclusão** — cada selo entra ~60 px atrás da carcaça e a silhueta do aparelho
corta a ponta dele, com padding maior desse lado (o que some é margem, nunca
texto) e o gradiente escurecendo para lá, porque tab que dobra para trás entra
na sombra. Virou o `.selo-recurso--encaixado` da `base.css`.

**Depois veio a luz, em três camadas, e cada uma com o seu modo de mistura.**

| camada | o que faz | mistura |
|---|---|---|
| brilho da tela, atrás do aparelho | o cardápio é uma tela acesa, e tela acesa derrama no escuro: é o que faz o totem parecer ligado | `screen` |
| a luz do pé, do vermelho do cupom ao âmbar do cashback | **uma** luz, e não duas poças: com duas, os selos ficavam em cenas diferentes | `screen` |
| a tinta na carcaça | prova que a luz bate no aparelho, e não só no fundo | `multiply` |

A terceira é a que quase não existiu. A primeira tentativa acendeu a carcaça
com `screen`, e não mudou **nada**: branco já é o teto do `screen`. Quem tinge
branco é `multiply` — e só sobre o painel, nunca sobre o vidro, onde moram nome
e preço de produto. Mais a sombra de contato na quina, sem a qual o selo
encosta no aparelho mas não entra nele.

**Os ícones vieram da página, e mudaram o que se lê primeiro.** A seção
*Transforme cada venda…* (fato 15) anuncia cada recurso como um cartão com
ícone, nome e uma linha de descrição, e os selos passaram a ter a mesma
estrutura: bilhete picotado para o cupom, cifrão com seta de volta para o
cashback. Não é enfeite — na miniatura do feed a palavra `Cupom` tem 9 px de
altura e o desenho tem 30, então o ícone é o que sobrevive ao tamanho em que a
capa é decidida. São **SVG inline** com `stroke: currentColor`: herdam a cor do
selo, escalam sem borrar e não viram arquivo para manter.

`COM O TELEFONE` saiu e entrou `PRÓXIMA COMPRA`. A nota antiga contava **como
se entra** no cashback, que é assunto do slide 6; a nova conta **o que se
ganha**, que é o que um selo de capa tem de dizer. E ela cabe: a nota é
`nowrap`, porque nota quebrada em duas linhas deixa um selo mais alto que o
outro e os dois param de ler como par — quando não coube, quem encurta é o
texto.

**E o subtítulo levou duas voltas antes de acertar.** A primeira versão era
*"E o programa de fidelidade entra no pedido"*, que descreve **onde o recurso
fica** — informação de menu, não de capa. A segunda foi *"E cada venda já sai
puxando a próxima"*, uma metáfora nossa que não estava em lugar nenhum e soava
forçada.

A terceira veio da página, que tem a linha exata para este par no cartão de
fidelidade: *"Aumente a recorrência com cashback e cupons."* Virou **"Mais
recorrência, com cashback e cupom."** — o benefício primeiro, os dois meios
depois. Palavra da casa, e não invenção de quem está escrevendo o slide.

**Do slide 3 ao 7 o print vai sem aparelho em volta.** É a escolha contrária à
da capa, e pelo mesmo motivo: ali a tela precisa ser **lida**. A tela do totem é
1080×1920; dentro de um mockup de 420 px de largura a letra do cardápio sai com
11 px no feed. Recortada e mostrada com 940 px de largura, a mesma letra sai com
24 px. O aparelho já foi estabelecido na capa, e o `.recorte` preto continua
lendo como tela de totem porque o aplicativo é escuro.

**Cada recorte é uma faixa contínua da tela, nunca uma montagem.** Os slides 4 e
7 têm dois recortes porque são duas telas (4) e duas faixas distantes da mesma
tela (7). Empilhá-las coladas as faria passar por uma tela só, que é o que elas
não são; por isso vão separadas, com respiro.

**A venda sugestiva perdeu um slide quando a fidelidade ganhou dois.** Eram dois
slides — o adicional no item e o `Peça também` na sacola — e viraram um, com as
duas faixas mais baixas. A ideia de uso é a mesma (a tela oferece antes de
deixar fechar) e o ganho precisa chegar cedo: com dois slides de venda
sugestiva, o cupom cairia no sexto, e quem rola o feed costuma parar no quinto.

**O item é avulso, não combo.** No combo o preço aparece como `A partir de
R$ 35,90`, e a peça fala de preço e de adicional com valor fechado. `ONE BURGER
R$ 24,00` mais `+ R$ 4,00` de bacon é uma conta que o leitor acompanha — e os
5% do cashback dão o `R$ 1,20` que aparece na barra do slide 7. É um jogo de
números só, na peça inteira.

**No slide do cashback a tela é a da identificação, e o campo está vazio.** São
duas telas possíveis: esta, em que o totem **oferece** o programa, e a da
carteira, em que ele mostra o saldo. A primeira serve melhor porque é o que o
cliente sem saldo vê — e porque o recorte da segunda traria o nome e o telefone
de teste que o roteiro de captura digita.

**O CTA errou duas vezes para o mesmo lado: o de querer ser esperto.**

*"Conheça o totem por dentro"* foi a primeira, e "por dentro" sugere hardware —
o que existe lá dentro são as telas que o leitor acabou de ver em oito slides.

*"Passe pelo pedido inteiro, tela por tela"* foi a segunda, e é a mais
instrutiva porque **o fato era verdadeiro**: a página roda um pedido no
aparelho, com pausa e setas (fato 14). O slide ainda assim ficou pior. De
dentro do feed ninguém sabe que existe uma demonstração do outro lado, então a
frase virou instrução para uma coisa que o leitor não viu — e CTA que precisa
de contexto não é CTA.

Ficou a **convenção**: *"Conheça todas as funcionalidades"* e o endereço. Ela
funciona por dois motivos. O leitor já sabe o que fazer com ela, sem
explicação. E ela promete **mais do que o carrossel mostrou** — a página tem
uma seção inteira de plataforma (PDV, KDS, fiscal, financeiro, estoque,
fidelidade), então a frase é verdadeira e é a única razão de sair do feed.

Com o título curto, o texto cabe em três linhas e o aparelho sobe: a sangria
volta de `490` para `430` e o mockup cresce de 400 para 430 px.

**O slide de idioma é o mesmo do carrossel da tradução, e no penúltimo lugar.**
A prova já existia e não precisava ser reinventada: o mesmo item, recortado do
mesmo ponto da tela, nos dois idiomas — foto igual, `R$ 11,00` igual, e o nome
saindo de `FRENCH FRIES` para `PAPAS FRITAS`. Dois recortes e não três: em
português o cartão sai mais alto, porque a altura da fileira segue o nome mais
longo do setor, e o português já está em cinco slides desta peça.

O lugar dele contraria a cronologia de propósito. A bandeira fica na **primeira**
tela, então o slide caberia em quarto — e empurraria cupom e cashback para o
sexto e o sétimo, desfazendo o que a rodada anterior tinha feito de subir os
dois. Idioma não é um passo do pedido, é um **modo do aparelho**: o cliente
escolhe antes de tudo e não volta a pensar nisso. No penúltimo lugar ele é o
"e ainda atende quem não fala português", que é leitura de quem chegou até ali.

**E o slide não diz que o sistema traduz.** Quem escreve a versão em inglês do
cardápio é o dono da loja. A peça mostra o resultado na tela do cliente e para
— prometer tradução automática volta como reclamação, e foi a lição do
carrossel da tradução.
