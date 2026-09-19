# Cardápio Digital no Tablet: a mesa pede sozinha

- **Gênero:** função do sistema (a quarta peça do gênero, depois de
  `dark-kitchen-multimarcas`, `totem-autoatendimento` e da página de desconto)
- **Pauta:** [`beefood.com.br/cardapio-digital-tablet`](https://beefood.com.br/cardapio-digital-tablet/)
  — página inteira, servida pelo próprio WordPress (não é casca)
- **Manuais lidos:**
  [`cardapio-digital-tablet-modo-kiosk`](../../manuais/cardapio-digital-tablet-modo-kiosk/cardapio-digital-tablet-modo-kiosk.md)
  (a trava do aparelho, e o `fluxo-codigo.md` dele, que mapeia o painel) e
  [`traducao-cardapio-presencial`](../../manuais/traducao-cardapio-presencial/traducao-cardapio-presencial.md)
  (quem escreve o cardápio em inglês é a loja)
- **Novidade que sustenta o fato:**
  [`tablet-kiosk-conta-cashback-pedido`](https://beefood.app/novidades/tablet-kiosk-conta-cashback-pedido)
  (26/08/2026) — conta da mesa, identificação do cliente e pedido
- **Formato:** 4:5 (1080×1350), 9 slides
- **Imagens:** 4 **capturas** do painel de produção (feitas para esta peça), 2
  **prints de produção** do aplicativo Android que já estavam em `manuais/`,
  1 tela **desenhada** e 1 **prova reaproveitada** — as duas últimas vêm do
  carrossel da tradução (slides 6 e 7)

## A pauta veio errada na primeira leitura, de novo — e foi ferramenta

O `pauta.py` devolveu esta página **sem três blocos inteiros**: *Layout
otimizado*, *Rodízio sem complicação* e *Fechamento de conta simplificado*, e
sem nenhuma resposta do FAQ. Só que desta vez a página **não** é casca: ela se
serve sozinha, com todo o texto no HTML.

O defeito era do leitor. O editor do site embrulha cada parágrafo em
`<span style="font-weight: 400">`, e o leitor tratava `span` como bloco: ao
abrir o `span`, ele fechava o `<p>` e jogava o texto na pilha de "menu e rótulo
de ícone", que é descartada. Somando a isso o fato de que título sem corpo era
filtrado, os três blocos sumiram — título e texto, cada um por um motivo.

Agora `a` e `span` só contam como bloco quando **não há bloco aberto**, e
título de nível 3 sobrevive sem corpo. A peça foi escrita depois da correção.

> É a segunda pauta seguida em que a leitura pobre era da ferramenta, não da
> página. A pergunta continua valendo: **"esta página se serve sozinha?"** — e
> ganhou uma irmã, **"o meu leitor lê tudo o que ela serve?"**

## O que a página promete e a peça não repete

| Da página | Por que fica de fora |
|---|---|
| "Aumento de até 40% do ticket médio" | resultado prometido, não comportamento do produto — a régua de número é manual ou tela |
| "traduzido automaticamente para inglês e espanhol" | o manual da tradução diz o contrário: **quem escreve a versão em inglês é a loja**, campo por campo |
| Modo Rodízio | não tem manual, não tem tela no painel do sandbox e não está em nenhum print: não dá para provar |
| Avaliação do cliente | existe na tela (o atalho `AVALIE` está no print), mas não sobrou slide — está na legenda |

## O fato, inteiro

Conferido no painel de produção, no manual e nos prints do aplicativo:

### O que o cliente faz no tablet

1. **A tela inicial é vitrine.** Banner grande com setas, faixa `Recomendados`
   com cartões de produto, e a coluna da esquerda com `DESTAQUES`, `CARDÁPIO`,
   `AVALIE` e as três bandeiras. Barra de topo com o logo da loja, `BUSCAR`,
   `CARRINHO DE COMPRAS` e `MINHA CONTA` (print `03-home-logo`).
2. **O banner leva a algum lugar.** No painel, cada slide tem
   `tipoRedirecionamento`; a novidade diz que o banner "leva direto ao setor ou
   ao produto anunciado".
3. **O produto abre em tela cheia**, com foto e descrição, antes das escolhas;
   os complementos seguem as regras cadastradas, e o que falta é avisado em vez
   de só travar (novidade, item 4).
4. **O cliente chama o garçom escolhendo o que precisa.** A lista é do painel:
   Açúcar, Adoçante, Copo, Fechar a Conta, Gelo, Guardanapo, Ketchup, Limão
   Espremido, Limpar Mesa, Maionese, Mostarda, Pimenta, Rodelas de Laranja,
   Rodelas de Limão, Sal, Talheres. A chave do painel diz o que acontece:
   **"Imprime cupom com a solicitação"**.
5. **A conta fecha na mesa.** Duas chaves, com o texto da própria tela:
   `Solicitar Fechamento de Conta` — *"Exibe no tablet o botão para o cliente
   pedir o fechamento da conta"* — e `Pix online` — *"Permite o fechamento da
   conta com Pix"*. O resumo mostra produtos, complementos e valores, com item
   excluído riscado, e taxa de serviço e valor por pessoa quando fazem sentido
   (novidade, item 2).
6. **O cardápio tem três idiomas.** As bandeiras estão na coluna da esquerda do
   print, e o print `09` do manual da tradução mostra a tela em inglês
   (`SEARCH`, `MY CART`, `MY BILL`). O texto do produto é o que a loja escreveu.

### O que o dono faz no painel

7. **Uma tela para todos os tablets**, em `Cardápio no Tablet`, com três abas:
   `Tablets`, `Layout` e `Eventos`.
8. **Cada aparelho é um cartão** com status, mesa vinculada, marca e modelo,
   bateria em %, tempo desde o último sinal e versão do aplicativo. Em cima,
   cinco contadores: `Contratados`, `Total`, `Online`, `Ausentes`, `Offline`.
9. **O status sai do último sinal**: menos de 1 hora é Online, entre 1 e 6 é
   Ausente, 6 ou mais é Offline (`tablet-helpers.tsx`, no `fluxo-codigo.md`).
10. **Seis eventos** para os aparelhos escolhidos: Atualizar Cardápio e Layout,
    Travar, Destravar, Vincular Mesa/Comanda, Remover Vínculo de Mesa/Comanda,
    Deslogar Usuário. O evento é **fila**: o painel grava e o tablet executa no
    próximo sinal — por isso a aba Eventos tem *Pendente* e *Processado*.
11. **Vincular a mesa dispensa o QR Code.** O evento grava `mesaFixa: true`;
    sem ele, o cliente precisa apontar a câmera para o QR Code da mesa a cada
    pedido (`fluxo-codigo.md`, seção 4).
12. **O layout é configurado por filial**: logo do topo, tema claro ou escuro,
    lista completa ou por etapas, e as três chaves de funcionalidade.

### O limite, que não vira slide

13. **A trava de verdade é no aparelho, não no painel.** O `TRAVAR` do painel
    bloqueia só o botão *voltar* dentro do aplicativo; o **modo kiosk** — o que
    impede sair para o Android — é ativado no próprio tablet, em Administração,
    com senha, e volta sozinho depois que o aparelho reinicia. São duas coisas,
    e o `fluxo-codigo.md` abre justamente avisando para não confundir. A peça
    não fala de trava em nenhum slide: com uma linha só, a chance de dizer a
    errada é grande demais.

## O ângulo, e de onde ele sai

O totem fica na entrada e resolve um pedido. **O tablet fica na mesa e
acompanha a refeição inteira** — a primeira rodada, a segunda, o gelo que
faltou, a conta dividida no fim. É essa permanência que a peça vende, porque é
o que separa este canal de todos os outros.

E permanência, para quem está sentado, se chama **não esperar**: a segunda
rodada não depende de alguém passar na mesa, e o garçom entra quando é chamado.
É daí que sai a manchete da capa — e não do fechamento de conta, que foi por
onde a primeira versão tentou, errado (ver *Decisões de arte*).

Do lado do dono, a mesma permanência vira **frota**: dez, vinte aparelhos
ligados no salão, cada um numa mesa, com bateria e sinal para acompanhar. A
página chama isso de "controle todos os tablets em uma única tela", e o painel
entrega exatamente isso.

| Fato | Ângulo | O que o slide diz |
|---|---|---|
| o cardápio está na mesa, e o pedido entra na comanda pelo próprio tablet (1 e 3) | pedir deixa de depender de alguém passar | **capa** |
| tela inicial com banner, recomendados e atalhos (1) | o cardápio na mesa é vitrine, e vitrine oferece antes de ser perguntada | slide 3 |
| produto em tela cheia, complementos com regra (3) | o pedido sai montado, sem tradução de garçom | slide 2 |
| dezesseis opções de chamada, com cupom impresso (4) | o cliente pede o que precisa, e a equipe já sabe o que levar | slide 4 |
| fechamento de conta e Pix online, por chave (5) | a mesa fecha sem três idas e vindas até o caixa | slide 5 |
| bandeiras na coluna e tela em inglês (6) | mesa de turista deixa de depender de quem fala a língua | slide 6 |
| o texto em outro idioma é um campo do próprio produto (6) | não existe segundo cardápio para manter | slide 7 |
| frota com mesa, bateria e sinal (7 a 11) | o salão inteiro cabe numa tela, e o cardápio novo sai daí | slide 8 |

## Os slides

| # | Arquivo | Tipo | Ideia única | Imagem |
|---|---|---|---|---|
| 1 | `01-capa.html` | capa + mockup | o cliente pede no tablet sem esperar o garçom | tablet com a tela inicial de verdade |
| 2 | `02-como-funciona.html` | texto | o caminho do pedido, do primeiro item à conta | — |
| 3 | `03-vitrine.html` | recorte | a primeira tela já oferece o combo | banner + `Recomendados`, ampliados |
| 4 | `04-chamar-garcom.html` | captura | o cliente pede gelo, talher, guardanapo — e sai cupom | aba `Garçom Opções` do painel |
| 5 | `05-conta.html` | captura | a conta fecha na mesa, com Pix | as três chaves de funcionalidade |
| 6 | `06-idiomas.html` | mockup | o mesmo cardápio em inglês | tela desenhada, do carrossel da tradução |
| 7 | `07-mesmo-cadastro.html` | captura reusada | o inglês é um campo no produto que já existe, e vale em todo canal | linha do Nome com as três bandeiras |
| 8 | `08-painel.html` | captura | o salão inteiro numa tela, com mesa e bateria | aba `Tablets` com a frota |
| 9 | `09-cta.html` | capa + mockup | a página do sistema tem o resto | tablet com a tela inicial |

## Decisões de arte

**A tela do tablet é print de produção, e isso é o segundo degrau — o primeiro
não existe.** O aplicativo é Android (`Cardápio Mesa/Comanda`) e não roda no
Cloud Agent. A ordem da skill é *captura feita para o carrossel > print de
produção > print pedido ao dono > desenho*, e aqui o primeiro degrau está
fora: o que sobra é o print que o dono já mandou para o manual do modo kiosk,
em 2560×1600 — que é **16/10, a mesma proporção da tela do mockup**. Entra
inteiro na capa e recortado no slide 3.

**O painel, ao contrário, é captura nova.** Quatro telas tiradas para esta peça
no `/cardapio-digital-tablet` do sandbox, porque o painel é web e o leitor
desta peça é quem vai olhar para ele.

**A frota do slide 7 vem de um `tablets.json`.** O sandbox tem **um** aparelho,
offline, sem mesa — e "controle todos os tablets em uma única tela" com um
cartão só mostra o contrário do que diz. É o mesmo caso do cupom no totem:
o recurso está ligado e a **vitrine** é que falta. A rota
`tablet2/aparelhos/{empresa}/{usuario}` devolve a lista deste arquivo, com os
campos do aparelho de verdade — mesa, marca, modelo, bateria, sinal e versão —
e quem desenha a tela, conta os cinco cartões e pinta o status é o painel.

**As chaves do slide 4 e do slide 5 são ligadas na tela, sem salvar.** Os
interruptores da aba `Garçom Opções` chegam desligados no sandbox, e uma lista
inteira em cinza não mostra o recurso. Ligar na interface é o estado de quem
está configurando; **`SALVAR` não é tocado**, então o sandbox fica como estava.

**O que a peça não mostra do painel:** a aba `Eventos` e o modal `Enviar
Evento`. Os dois são bons, e os dois puxariam a peça para a trava — que é o
assunto em que as duas travas se confundem (fato 13).

**A capa saiu vendendo o ponto fraco, e foi refeita.** A primeira versão era
*"Cada mesa pede e fecha a própria conta"*, com **conta** em vermelho. O
fechamento existe no produto — as duas chaves do slide 5 provam —, mas
**pagamento é a promessa do totem**, e a capa do totem já diz *"O cliente pede
e paga sozinho no totem"*. Pendurar esta peça no mesmo gancho fazia ela
competir com a irmã justamente no ponto em que é mais fraca, e ainda gastava a
manchete com o que o leitor menos vai usar.

O conserto veio de reler a página. O topo dela tem três promessas, e uma delas
é resultado em % (ticket médio), que não vira manchete. As outras duas são
*"Garanta agilidade: o cliente só chama o garçom se quiser"* e *"Reduza o tempo
de atendimento e elimine erros nos pedidos"* — e o FAQ repete as duas, com
*"Clientes fazem pedidos com autonomia, sem esperar pelo garçom"* e *"Redução
de erros de comunicação entre salão e cozinha"*. O bloco do Chamar Garçom ainda
dá a imagem: *"sem precisar levantar a mão, acenar ou esperar"*.

Manchete e subtítulo ficaram com um eixo cada:

| | |
|---|---|
| manchete | **"O cliente pede no tablet, sem esperar o garçom"** |
| subtítulo | **"E o pedido entra na comanda como ele montou."** |

**"sem esperar" é o vermelho, e a posição não é acidente.** No totem o vermelho
cai em *"e paga"*; aqui cai em *"sem esperar"*, no mesmo lugar da frase. As duas
capas são da mesma família, e quem vê os dois posts lê a diferença entre os dois
canais sem precisar que ninguém explique.

O subtítulo é o *"elimine erros"* da página **ancorado no que o slide 2 prova**:
o pedido entra na **comanda** como o cliente montou. Não fala em cozinha — o
fato garante a comanda, não o caminho até o fogão.

Cinco rascunhos foram renderizados antes deste. Os que caíram ensinaram duas
coisas: título que não nomeia o aparelho (*"Ninguém levanta a mão para pedir de
novo"*) vira manchete-conceito e entrega o assunto à pílula; e abrir com
*"No tablet da mesa…"* põe a palavra **tablet** na linha logo abaixo de uma
pílula que já termina em **TABLET**, o que pesa. Com o aparelho no meio da
frase os dois problemas somem.

**O slide 7 é prova emprestada, e o que viajou foi a prova — não a arte.** O
print é o mesmo `05-cadastro-ingles.png` do carrossel da tradução, porque a
tela de cadastro **não muda por canal**: o produto é um só, e o tablet lê o
registro que o totem e o cardápio por QR Code também leem. Recapturar
devolveria o mesmo arquivo com outro nome.

O candidato mais óbvio era outro, e foi recusado: os dois recortes do cartão em
inglês e espanhol, que já estavam prontos e já tinham sido reusados no totem.
Eles são prova **do totem**, e numa peça de tablet seriam arte desmentindo a
frase do slide. A pergunta que resolveu: **esta prova é do módulo, ou do
canal?**

Duas coisas viajaram junto com a imagem. O **limite** — a página do tablet
também promete "traduzido automaticamente", e o manual continua dizendo que
quem escreve é a loja. Com este slide, a peça parou de só *evitar* a frase e
passou a **mostrar como é**: um campo a mais no produto que já existe. E a
**copy não viajou**: o slide de lá fala com quem ainda não tem o recurso
(*"Você escreve uma vez, e pronto"*); aqui o leitor já está escolhendo um
canal, então o argumento é o cadastro único.

**Onde ele entra é decisão de arco, não de cronologia.** Poderia abrir a peça,
junto do resto do cadastro. Entrou depois do slide 6 porque os dois formam um
par: lá está o que o **cliente** lê, aqui está **onde aquele texto foi
escrito**. É a virada do lado do cliente para o lado do dono, que o slide do
painel completa.

**E ele custou o teto de 8 slides**, pela mesma razão do totem: os nove dizem
nove coisas diferentes, e o corte só tiraria conteúdo.

**O suporte do mockup foi reaberto e ficou como estava.** Numa peça que se
chama "no tablet", vale conferir se o aparelho lê como tablet — e na folha do
catálogo o `.tablet` tem a mesma silhueta do `Monitor de mesa`. Três variantes
foram renderizadas em escala de capa contra a foto do site, inclusive uma com a
chapa medida no alfa da foto (38% no topo, 65% no pé): essa última devolveu o
"chapéu chinês" que a memória da skill já tinha registrado em outra rodada.

A conclusão foi para a memória, na seção *o suporte do tablet é um limite do
desenho frontal*: o que faz a peça ler como chapa na foto é a curvatura vista
de lado, que é informação de perspectiva, e o mockup é frontal. A chapa larga
atual é a menos pior aproximação. Mexer nisso de verdade pede `.cena3d`, e o
`.tablet` já é usado por outro carrossel publicado — não é conserto para fazer
no meio de uma peça nova.
