---
name: carrossel
description: Produz carrossel de Instagram (prints reais, mockups e slides em PNG 1080x1350) sobre uma novidade publicada em beefood.app/novidades ou sobre uma função do sistema BeeFood (páginas de beefood.com.br, temas, segmentos como dark kitchen). Use quando o pedido falar de carrossel, post, arte, slides, divulgação ou comunicação de novidade ou de funcionalidade. Não use para escrever manual de usuário — isso é a skill manual-sistema.
---

# Carrossel do BeeFood

Transforma um fato do sistema em **publicação** para o Instagram: texto escrito a
partir do fato (não recortado do release nem da página de vendas), telas reais do
produto em mockup de celular e de computador, e slides exportados no tamanho
exato do feed.

## Quando usar, e quando não

| Pedido | Onde ele é atendido |
|--------|---------------------|
| "faz um carrossel da novidade X", "post sobre o KDS", "arte para o Instagram" | **aqui** |
| "carrossel da função X", "post sobre dark kitchen", "carrossel desta página do site" | **aqui**, no gênero *função* — ver abaixo |
| "cria o manual de X", "documenta a tela Y", "atualiza o manual Z" | skill `manual-sistema` — **não é esta** |

## Dois gêneros, e a diferença é o leitor

A peça é a mesma máquina — capa nomeia, slide 2 explica, slide 3 mostra — mas
**quem lê muda**, e com ele mudam a pauta, a pílula da capa e o pedido do fim:

| | **Novidade** | **Função do sistema** |
|---|---|---|
| Pauta | release em `beefood.app/novidades` (`pauta.py`) | página de `beefood.com.br`, tema ou segmento (`pauta.py --pagina`) |
| Leitor | **já é cliente** e vai ligar o recurso hoje | pode **não ter conta**; está escolhendo sistema |
| Capa | pílula `Novidade`; o título nomeia o recurso | pílula do tema (`Dark Kitchen`, `PDV`), nunca `Novidade`; o título nomeia o recurso **e o segmento** |
| Onde mora o fato | novidade + manual | manual quando existe; **senão, a tela do sistema** |
| CTA | caminho de menu, "já está no ar" | a página do site ou criar conta — caminho de menu não serve para quem não tem painel |
| O que não cabe | — | "novidade", "agora", "acabou de sair": o recurso pode ter anos |

**A página de vendas é pauta, não fato.** Ela já é copy, escrita para busca e
conversão, e recortá-la dá o pior changelog possível. Da página vêm os eixos e o
público, e dá para afirmar o que ela diz do **funcionamento** do produto ("cada
marca tem cardápio, canais e relatórios próprios") — mas **não** o que ela diz da
empresa: "+100 mil negócios", "melhor avaliação no Google", "melhor suporte do
Brasil" são claim institucional e não entram na arte.

**E a novidade pode não ter release nenhum.** Módulo **em liberação** chega ao
sistema antes de chegar ao feed: a Gestão de Entregas tinha dezoito manuais
conferidos no código e zero linha em `beefood.app/novidades`. A peça continua
sendo do gênero *novidade* — o leitor é cliente, a pílula diz `Novidade`, o CTA
é caminho de menu —, e o que muda é só de onde vem a pauta: o **manual** passa a
ser fonte única, e é o material do qual é mais fácil recortar sem perceber (ver
passo 6). Sem release não há data para amarrar, então o `copy-instagram.txt`
pede a quem publica que confirme a liberação antes de postar — a arte não leva
data de todo jeito, e por isso ela pode esperar na fila.

**E a página pode estar vazia, sem que isso derrube a peça.** A do totem só tem
menu, rodapé e um `Carregando…`; o que sobrou foi a descrição de busca, uma
afirmação funcional, e ela bastou para o ângulo. Pauta é a parte substituível —
o que não pode faltar é o **fato**, e ele vive na tela. Quando o CTA mandar para
uma página assim, avise no `copy-instagram.txt` para conferirem antes de
publicar.

**O tema entra no título, e a pílula não basta.** *"Várias marcas num painel só"*
descreve o arranjo e não diz para quem serve — multimarca acontece em franquia,
em praça de alimentação, em food hall. Quem rola o feed lê o título, não a
pílula. Virou *"A dark kitchen de várias marcas num painel só"*.

**Capa de assunto que converge é cena, não recorte.** Quando o título promete
várias coisas *chegando* num lugar só, recorte de tela mostra o fim do caminho e
nunca o caminho — e a capa sai pobre mesmo com a prova certa. Aí a capa monta
uma cena com `.origem` + `.fio` + `.selo-ok` (ver `references/mockups.md`), e a
tela ganha uma versão própria, de tipo maior: na capa ela é **lida**, e não
atmosfera.

E **afirmar não é provar**: a prova visual sai do manual, da tela capturada ou da
tela **desenhada** (passo 3), nunca da ilustração da própria página. Detalhe em
[`references/roteiro-e-copy.md`](references/roteiro-e-copy.md), seção *o gênero
muda o leitor*.

Esta skill **não altera** nada da `manual-sistema`: nem a `MEMORIA-GERAL.md`,
nem o `CHECKLIST-MANUAIS.md`, nem `manuais/`. Ela lê esse material e escreve só
em `carrosseis/` e na própria pasta. O manual continua com o foco dele: passo a
passo com setas numeradas para o usuário final.

## Conhecimento que vem do manual (leia antes de capturar)

Captura de tela do BeeFood já está resolvida pelos manuais. Não reinvente:
leia [`references/conhecimento-compartilhado.md`](references/conhecimento-compartilhado.md),
que mapeia exatamente quais seções da `MEMORIA-GERAL.md` abrir e por quê.
O resumo curto: **espere o spinner sumir e mais 5 segundos antes de cada print**,
use a conta sandbox, tema claro, e cubra dado pessoal na imagem pura.

Se a novidade tem manual, o manual é a fonte de verdade do comportamento — ele
foi conferido no sistema. O `pauta.py` aponta o manual correspondente sozinho.

## Fluxo

### 1. Pauta

```bash
python .cursor/skills/carrossel/scripts/pauta.py
python .cursor/skills/carrossel/scripts/pauta.py --slug <slug>
python .cursor/skills/carrossel/scripts/pauta.py --pagina https://beefood.com.br/sistema-dark-kitchen/
```

Sem argumento, lê o RSS de `beefood.app/novidades` (título, data, tipo, áreas,
texto completo) e indica o manual relacionado, com a contagem de capturas que já
existem lá.

**Quando ele disser que não achou manual, confira à mão.** O casamento é por
nome de pasta, e nome de pasta não segue o título do release — o do Painel para
Entregadores mora em `manuais/painel-entregador/` e passou batido por uma letra
de plural. O script lista as pastas mais próximas justamente para isso; um
`ls manuais/ | grep <palavra>` custa segundos e o manual costuma trazer o
recurso lido no código-fonte, que é fato mais duro que o release.

Com `--pagina`, lê uma página de `beefood.com.br` e devolve a mesma coisa para o
gênero *função*: os blocos da página, a lista de funcionalidades, o FAQ — e o
cruzamento com `manuais/`, que é o que separa **o que tem manual** (fato
conferido) do que vai precisar de tela. Ele também lista o que **não** pode
virar slide: os números institucionais da página.

**Parte do site é uma casca.** O endereço público devolve menu, rodapé e um
`Carregando…`, e o conteúdo vem de um app externo. Aconteceu com o totem, e a
peça inteira saiu sem a seção de fidelidade, sem a demonstração do aparelho e
sem o FAQ que estavam lá — `curl`, navegador e REST do WordPress concordaram
que a página estava vazia, e os três olhavam para o lugar errado. O script
agora percebe a casca sozinho e avisa na saída:

```
- O endereço público é uma casca; o conteúdo veio de https://…/totem
```

Se a leitura de uma página vier suspeitosamente pobre, **desconfie da
ferramenta antes de concluir que a página está vazia**. A pergunta não é "a
página tem conteúdo?", é "esta página se serve sozinha?".

#### E a pauta tem uma segunda metade: o acervo

Antes de escrever uma linha, **leia os carrosséis que já existem**. Não é
curiosidade, é levantamento: os produtos da BeeFood compartilham módulos, e
metade da prova que a peça nova precisa costuma já estar capturada, recortada e
aprovada em outra pasta.

```bash
cat carrosseis/README.md                 # o índice, com gênero e fonte de cada peça
ls carrosseis/*/slides/                  # que assuntos já viraram slide
ls carrosseis/*/imagens-puras/           # que provas já estão capturadas
ls carrosseis/*/*.json                   # dados de exemplo (traduções, cupons, frota)
```

Depois abra o `roteiro.md` das peças do **mesmo gênero** e das que tocam o mesmo
módulo, e responda duas perguntas:

1. **Quais provas já existem sobre este assunto?** No plural. O acervo quase
   nunca tem uma só, e a primeira que aparece na busca costuma não ser a
   melhor — a escolhida é a que prova a **manchete inteira**.
2. **O que a peça vizinha já prometeu, e como esta se diferencia dela?** Duas
   capas da mesma linha não podem vender o mesmo gancho.
3. **Que erro ela já cometeu neste assunto?** O `roteiro.md` de cada peça
   registra o que deu errado e por quê. Repetir erro documentado é o
   desperdício mais caro do acervo.

**Isso pesa muito mais no gênero `função` do que no gênero `novidade`.** Uma
novidade é um recorte no tempo: ela tem um fato próprio, e reaproveitar prova de
outra peça quase sempre significa falar de outra coisa. Uma função é um **canal
da mesma plataforma** — totem, tablet, QR Code e app do garçom leem o mesmo
cadastro, o mesmo cardápio, o mesmo programa de fidelidade. Aí o reuso não é
atalho: é o que mantém as peças **coerentes entre si**.

**E reusar é adaptar, não copiar.** A prova viaja; o slide, não. O slide
reaproveitado é escrito do zero para responder a pergunta que **esta** peça
deixou aberta — trocar as palavras e manter o ângulo da peça de origem é o erro
que parece resolvido e não está.

**Quando a melhor prova é do canal errado, redesenhe.** Os recortes do cartão em
inglês e espanhol são do totem; na peça do tablet eles foram refeitos com o
componente de tela do tablet, a foto da biblioteca e o texto do arquivo de
tradução da peça de origem. O que se reusa aí é a **ideia da prova**, e não o
arquivo.

Regra e limites em
[`references/roteiro-e-copy.md`](references/roteiro-e-copy.md), seção *o acervo
é parte da pauta*.

### 2. Roteiro — antes de qualquer imagem

**O texto da fonte é matéria-prima, não roteiro.** A novidade é registro de
release: descreve o campo, a tela e o efeito na ordem em que o produto foi
construído. A página do site é pior: já é copy. Recortar um dos dois em oito
pedaços e centralizar cada pedaço num slide produz changelog paginado ou anúncio
paginado, e ninguém arrasta nenhum dos dois. O carrossel é uma **publicação
nova, escrita a partir do fato**:

1. **fato** — o que o recurso faz, onde fica, o que passa a acontecer, qual o
   limite; em três linhas, sem adjetivo. Em novidade sai do release + manual; em
   função sai do manual e, quando ele não existe, **da tela do sistema**;
2. **ângulo** — qual cena reconhecível do restaurante esse fato toca;
3. **texto** — escrito da cena para a tela. Nenhuma frase pode aparecer igual à
   da fonte; se apareceu, foi copiada (`conferir-texto.py`, com `--fonte` quando
   a origem é uma página do site).

A ordem dos três primeiros slides é fixa nos dois gêneros: a capa **nomeia** o
recurso, o slide 2 **explica** o recurso e o slide 3 **mostra** o recurso na
tela. Conceito na capa e história no slide 2 são os dois jeitos de perder o
leitor antes da prova — e **cena na capa é um terceiro**, que passa despercebido
porque a frase sai boa.

#### Três regras de título, e as três vieram do mesmo retorno

Nomear era regra da **capa**, e por nove peças os slides de dentro ficaram
livres para ser espertos. Na décima o dono leu slide por slide e devolveu seis
linhas; elas fecham em três regras, que valem para todo título de todo slide.

**1. Nome, dois-pontos, o que ele te dá.** Cada slide de dentro nomeia o recurso
que ele mostra — não o módulo, que é da capa, mas a coisa daquele slide, com o
nome que o leitor vai procurar no menu depois. O ângulo não sai: ele vira a
segunda metade do título.

| Recusado | Publicado |
|---|---|
| "No pico, a rota já chega montada" | "**Roteirização automática**: a rota já chega montada" |
| "Quanto da entrega é cozinha, e quanto é rua" | "**Relatório de Operação**: quanto é cozinha, quanto é rua" |
| "Escolha como pagar, e o relatório fecha a conta" | "**Relatório do Entregador**: quanto pagar a cada um" |

Nome no **chapéu não conta**: chapéu é versalete pequeno, lido depois do título
quando é lido, e a checagem de três leituras passa só pelos títulos porque é
assim que o feed se lê.

A exceção é **uma**, e é estrutural: o slide 2 explica o recurso que a capa
acabou de nomear, então ele não repete o nome — ali o título é a explicação.
Nos outros, quem lê os títulos em fila tem de conseguir montar a lista do que o
módulo passou a fazer.

**2. Pronome no título é sempre erro.** *"quem marca é ele — ele quem?"* e
*"abre no celular dele — dele quem?"* O antecedente existia nos dois casos, no
chapéu e no slide anterior, e não serviu de nada: **o título é a única parte da
peça que se lê fora de ordem** — sozinho na miniatura, sozinho na folha de
contato, sozinho para quem passa o dedo e para no meio. `ele`, `dele`, `dela`,
`isso`, `aquilo` não entram em título; a pessoa é nomeada ali mesmo ("quem marca
é **o entregador**"). No corpo o pronome exige o substantivo antes dele, no
mesmo slide.

**3. Frase de manchete de jornal não é frase de carrossel.** *"Como estamos
chegando num texto tão tosco assim?"* — sobre "Lista vazia com a pílula verde é
sinal que deu certo". O defeito é o **estilo telegráfico**: manchete de jornal
corta artigo, come `de que` e empilha substantivo porque paga por centímetro de
coluna. Aqui a voz é de uma empresa conversando com um cliente, e o corte não
soa econômico, soa mal escrito. Artigo não se corta para ganhar linha; se a
frase estoura com ele, corte conteúdo, não gramática. E corpo que começa em "Na
ordem que…", "Pela taxa cobrada…", "Quatro etapas medidas…" é legenda de foto no
lugar de parágrafo — falta o verbo principal.

> **Leia cada slide em voz alta, no ritmo de quem conversa.** É o único teste
> que pega os três defeitos, porque na leitura silenciosa quem escreveu já sabe
> o que quis dizer. Onde a respiração tropeça, falta palavra.

O raciocínio inteiro, com o retorno na íntegra, está em
[`references/roteiro-e-copy.md`](references/roteiro-e-copy.md) — *a regra do nome
vale para os slides de dentro*, *pronome no título é sempre erro* e *frase de
manchete de jornal não é frase de carrossel*.

**A pasta nasce numerada.** O nome é `NN-<slug>`, com `NN` sendo a **ordem de
entrega** — o próximo número livre em `carrosseis/`. É o que faz a listagem do
diretório sair na ordem em que as peças foram publicadas, e o `.zip` chegar ao
cliente já ordenado (`empacotar.py` usa o nome da pasta). Ordem alfabética não
diz nada sobre um acervo, e por isso o índice do
[`carrosseis/README.md`](../../../carrosseis/README.md) tem coluna `#` em vez da
palavra "entregue" repetida em toda linha.

Crie `carrosseis/<NN-slug>/roteiro.md` com a tabela **fato → ângulo → o que o slide
diz** (é o que permite auditar que nada foi inventado e nada foi copiado) e a
tabela de slides (arquivo, tipo, ideia única, imagem). A legenda não fica aqui:
ela é peça de entrega e mora em `copy-instagram.txt` (passo 7).
Método completo em [`references/roteiro-e-copy.md`](references/roteiro-e-copy.md).

Roteiro aprovado primeiro; captura depois. Print tirado antes do roteiro quase
sempre é print que não entra.

### 3. Imagens

**A primeira pergunta não é de onde vem a imagem. É se ela mostra o resultado ou
o painel de controle.**

Durante nove peças esta seção começava por *onde a tela mora*, e ordenava a
imagem por facilidade de captura — desenho no último degrau, como pobreza. O
efeito foi o que o dono nomeou na décima: *"nossos carrosséis ficam só com imagem
de configuração de campos e printscreen das telas"*. A causa está na ordem, não
no descuido de quem executou: quando captura é o degrau mais alto, ganha a tela
que se captura mais fácil — e a mais fácil é sempre o formulário, que abre com um
clique, não precisa de cena montada e fica pronto sem dado nenhum dentro.

**Tela de configuração não é imagem de carrossel.** Campo, formulário,
interruptor, janela de ajuste, modal de regras, lista de parâmetros com um
marcado: tudo isso mostra **onde se mexe**, e carrossel não ensina a mexer —
carrossel mostra **o que passa a acontecer**. Quem precisa do campo abre o
manual, onde aquele print já está, com seta e número.

A ordem é esta, e substitui a antiga:

| Degrau | O que é | Quando |
|---|---|---|
| 1 | **tela de resultado, capturada** | a tela mostra o recurso funcionando: o mapa com as rotas correndo, o cardápio montado, o cupom impresso, o painel operando |
| 2 | **tela de resultado, desenhada pela peça** | o resultado existe e a captura não o alcança: aparelho que não roda aqui, cenário que o sandbox não tem, ou resultado espalhado por três telas |
| — | **tela de configuração** | **nunca** — nem capturada, nem desenhada |

O degrau 2 não é o porão. É onde a peça **constrói** a prova que a tela solta não
dá, e as imagens mais fortes das nove primeiras peças saíram dele: o cupom
térmico, as três marcas da dark kitchen, a rota dentro do app do entregador.

**Quando o fato é uma regra de configuração, a arte é o efeito da regra.** O
despacho automático tem sete campos numa janela; o slide não mostra os sete
campos, mostra a rota nascendo — *pedidos sem rota* → *Rota A · sem entregador ·
Montando* → *Rota A · Diego Souza · Pronta para sair*. As duas etapas estão no
manual, então o desenho não inventa produto: ele troca o painel de controle pelo
que o painel de controle produz.

**O teste, slide por slide: tampe a copy e olhe só a imagem — acontece alguma
coisa ali?** Se o que aparece é um campo com número dentro, um interruptor verde
ou uma lista de opções com um tique, a imagem é de manual e o slide está sem
prova. Isso vale também para a revisão da folha de contato (passo 6): imagem de
configuração é motivo de refazer, no mesmo nível de texto ilegível.

Decidido que a imagem é de resultado, **aí** vem onde a tela mora — é isso que
define se existe captura:

| Tela | O que fazer |
|------|-------------|
| painel web (`beefood.app`) | `capturar.py --rota /cardapio` |
| cardápio digital público | `capturar.py --url <link> --publico --dispositivo celular` |
| cardápio digital com mídia nossa dentro | `capturar-cardapio.py --conteudo midias.json` (banner, vídeo e cartaz de aviso entregues na resposta da API) |
| Totem de Autoatendimento | é **web**. `capturar-totem.py` faz o caminho da tradução; para outro caminho, escreva o roteiro em `carrosseis/<slug>/capturar-telas.py` — o aplicativo vai do cardápio ao pagamento, passando por cupom e cashback. **Não finalize pedido e não aplique cupom** (os dois são gravação no servidor da loja) |
| app Android (Garçom, Entregador, Tablet) | não roda no Cloud Agent: **peça o print ao dono** (zip em URL pública, seção 6 da `MEMORIA-GERAL.md`) e, enquanto ele não vem, desenhe a tela em CSS copiando layout e paleta do print de produção (passo 4) |
| regra de configuração (despacho automático, avisos, formas de pagamento) | a janela de campos **não** entra: desenhe o **efeito** da regra, com os rótulos que o sistema usa nos dois lados dela |
| cupom impresso | `ganchar_cupom` + `salvar_cupom`: o cupom nasce num iframe que vai para a impressora, então não dá para fotografar a tela |
| coisa que não é tela (impressora, balança) | desenho em CSS, copiando o aparelho do print de produção |
| cenário que a conta de teste não tem (segunda marca, pedido de marketplace chegando) | **desenhe a tela**: `carrosseis/<slug>/telas/*.html` + `desenhar-telas.py` |

**Antes de desenhar, ande no aplicativo.** A pergunta não é "existe captura
desta tela?", é "até onde esse aplicativo me deixa ir clicando até chegar no
resultado?" — o script que já existe costuma parar bem antes do fim, e a peça do
totem provou que dá para levar uma peça inteira até o fim clicando.

**Cenário que o sandbox não tem: desenhe a tela.** Apareceu inteiro na peça de
dark kitchen: o sandbox é uma loja, e o assunto eram três marcas.
O fragmento fica em `carrosseis/<slug>/telas/`, declara a medida no elemento raiz
(`<div class="tela" data-medida="1080x480">`) e sai em `imagens-puras/` pelo
`desenhar-telas.py`, com `assets/telas/painel.css` — o cinza de página, o cartão
branco, o selo de `Ativo`, o chip de ícone e a coluna de kanban do painel.

Desenhar **não** é inventar produto, e são três obrigações: o **rótulo é o do
sistema** (`Aguardando`, `Pronto/Entrega`, `Por Cardápio`, `Em Preparo` — lidos
de print de produção); **número é exemplo**, um jogo só na peça e com as somas
fechando; e a **arte da página do site não entra recortada** — ela é referência
de layout, como print de manual. Quando a tela é para ler de longe (KDS na parede
da cozinha), use `.tela--grande` e menos fichas por coluna: tela de 1280 px
reduzida a 860 no feed leva corpo de 14 px para 9. O `roteiro.md` diz, tela por
tela, o que é captura e o que é desenho.

**Print do manual que não serve, você refaz — não desenha.** O cupom do manual
*Destaque na impressão* sai com duas linhas em preto porque o manual precisava
mostrar que complemento também destaca; a capa do carrossel precisava de uma.
A saída foi montar no sandbox um pedido com só a bebida marcada e imprimir o
cupom dele (`registrar_pedido` no `capturar-telas.py` do carrossel). Continua
sendo impressão de verdade. Separe **registrar** de **imprimir**: registrar cria
venda no sandbox, reimprimir não cria nada, e a arte pode ser refeita à vontade.

**Sandbox sem o dado que o slide precisa: cadastre o dado.** O único produto com
tradução no sandbox era um refrigerante, e o carrossel mostrava hambúrguer e
porção — fotografar o produto errado sai mais caro que escrever a tradução no
produto certo (`gravar_traducao` no `capturar-telas.py` do carrossel da
tradução). Vale para o que o slide mostra; para **ligar recurso na loja de
exemplo de um cliente**, não: aí a saída é interceptar a resposta da API.

**Recurso desligado na loja de exemplo se liga na resposta da API.** O totem de
exemplo não tinha tradução cadastrada, então o `capturar-totem.py` intercepta
`/api/totem2/filial|setores|produtos`, devolve o mesmo JSON com `aaTraducao:
true` e com o campo `traducao` preenchido a partir de um `traducoes.json` da
pasta, e o **aplicativo de produção renderiza**. O que veio de fora é só o texto
que o restaurante escreveria. O script está pronto e é de uso geral; as
armadilhas (resolução, setor por índice, service worker, setor de combo) estão
em [`references/mockups.md`](references/mockups.md).

**E lista vazia esconde a tela inteira, que é o segundo uso da mesma rota.** A
loja de exemplo não tem cupom cadastrado: `venda2/cupomDescontoAtivo?tipo=totem`
responde `[]`, e sem lista o totem não desenha nem a linha de cupom. Aqui o
recurso estava ligado e a **vitrine** é que faltava; a rota devolve os cupons de
um `cupons.json` da pasta. Três cuidados:

- **leia o bundle antes de inventar o formato.** Os campos saíram do JavaScript
  do aplicativo, que lê a resposta sem mapear nada — formato adivinhado devolve
  tela em branco, ou pior, tela que não é a de verdade.
- **o que entra é o que o lojista escreveria**: código, título, benefício,
  regra. Quem desenha a tela é o aplicativo.
- **recorte fora o cabeçalho com o logotipo da loja.** Exemplo inventado
  embaixo de marca real lê como promoção anunciada por um cliente nosso. E
  avise no `copy-instagram.txt` que aquele dado é exemplo.

**E o terceiro uso: o dado real existe e desmente o produto.** Os dois casos
acima são de falta — recurso desligado, lista vazia. Aqui a tela abria e
funcionava: o Painel para Entregadores da sandbox mostrava **sete cartões
vermelhos**, todos "Atrasado • 1h38min", porque os pedidos de teste são da
manhã e ninguém os moveu. Tudo verdade, e a peça montada com aquilo vende "o
sistema que atrasa tudo".

Antes de fotografar, pergunte **o que esta tela diz sobre o produto para quem
não conhece o produto**. Se a resposta for o contrário do que a peça promete, a
cena se monta — e monta-se o mínimo:

- **o que é prova fica.** Pedidos, origens, números de marketplace: são reais e
  é deles que vem a credibilidade da imagem.
- **muda-se o que o tempo parado estragou** — situação e relógio —, e **um
  problema fica de pé**: tela boa demais não é turno, e o slide do alerta
  precisa ter o que provar.
- **o que sobra da cena, some.** Um pedido antigo fora do arquivo de cena
  continuava entrando vermelho ao lado dos ajustados, e uma coluna com dois
  regimes de tempo é pior que qualquer um dos dois.
- **registre**: um `cena.json` na pasta diz o que mudou e por quê, o script
  ganha `--cru` para mostrar a tela como ela está, e o `copy-instagram.txt`
  avisa quem publica.

**E há o caso em que montar a cena seria mentir: aí quem decide é o recorte.**
Os cartões das Campanhas Inteligentes declaram `R$ 0,00 de receita gerada` em
quatro das seis, e o estrago é o mesmo do painel — só que **receita não se
monta**. Relógio e situação são o estado que o tempo parado estragou; receita,
conversão e pedidos são o que o produto ainda não fez, e escrevê-los é prometer
resultado. Sem cena, sobra escolher o quadro: leia o título do slide, ache na
tela a linha em que ele **para de afirmar** e corte ali (no caso, logo abaixo do
selo do gatilho). O número que existe de verdade fica para o slide que fala de
resultado.

**A largura do viewport é decisão de arte.** A grade de campanhas tem três
colunas acima de 1500 px e duas abaixo; capturada larga, o nome da campanha
chega ao slide com 9 px. A conta é uma divisão — largura do recorte ÷ largura
que ele terá no slide —, e abaixo de 1 alguma coisa some. Capture na largura em
que o recorte sai em escala 1, e escolha a medida do viewport pela proporção da
moldura que vai recebê-lo (1600 × 1000 é 16/10, a tela do `.notebook`).

**Duas partes da mesma captura podem se desmentir.** O quadro do produto dizia
"dispara ~15 min" e o campo logo abaixo mostrava 5, porque a loja de teste
ajustou. O campo voltou ao padrão só para a foto — o editor só grava no
`SALVAR (F2)` — e o foco saiu antes do print, senão o campo sai com anel
vermelho e lê como erro de validação.

Duas armadilhas de relógio, que custaram duas rodadas de captura: o front pode
ler a data **ignorando o fuso** (meça `new Date(<o que vai injetar>)` contra
`Date.now()` no navegador da captura, em vez de confiar no sufixo `Z`), e o
mesmo cartão pode ter **duas contas** — o tempo de etapa e o alerta de atraso
vinham de campos diferentes, e mexer em um só produzia um estado que o sistema
nunca geraria. Detalhe em
[`references/MEMORIA-CARROSSEIS.md`](references/MEMORIA-CARROSSEIS.md), seção
*a cena honesta pode ser a pior peça de venda*.

**Quando o recurso é a mídia que o lojista sobe, você faz a mídia.** Capa e
vitrine em vídeo não têm captura: o cardápio modelo está vazio e o de produção
tem a campanha de um cliente. O `fazer-midia.py` renderiza as artes de
`assets/midia/artes/` e gera os MP4 (6 s, H.264, mudos); o `capturar-cardapio.py`
entrega tudo ao cardápio público na resposta do `validaDelivery` e fotografa o
aplicativo de verdade renderizando. A arte usa a **paleta da loja**, não a da
BeeFood, e o formato é **1920×580** com 14% de margem segura — o cardápio corta
com `object-fit: cover` (~4,1/1 no computador, ~2,6/1 no celular). Detalhes em
[`references/mockups.md`](references/mockups.md).

**A campanha da loja de exemplo não pode virar o assunto da arte.** O totem de
exemplo anunciava "Pudim R$ 16,90" na tela de espera, e numa capa sobre cardápio
em inglês o olho lia o preço do pudim. A mesma interceptação troca a arte de
fundo por uma foto nossa, que o `preparar-fundo.py` tira de um vídeo de comida —
as duas prontas estão em `assets/fundos/`. O logotipo da loja continua o dela.

Tela que abre direto numa rota:

```bash
python .cursor/skills/carrossel/scripts/capturar.py <slug> \
    --rota /cardapio --nome 02-produtos
python .cursor/skills/carrossel/scripts/capturar.py <slug> \
    --url https://beefood.app/novidades --nome 01-pagina --publico
python .cursor/skills/carrossel/scripts/capturar.py <slug> \
    --rota /cardapio-digital --nome 04-menu --dispositivo celular
```

Tela que exige clique: escreva `carrosseis/<slug>/capturar-telas.py` importando
`sessao`, `esperar` e `limpar` do `capturar.py` — mesmo padrão dos manuais, que
têm um script por pasta. Veja
[`carrosseis/01-destaque-impressao/capturar-telas.py`](../../../carrosseis/01-destaque-impressao/capturar-telas.py).

**Recorte é obrigatório em tela de painel.** Um modal inteiro reduzido para a
largura do slide fica ilegível no feed. O teto depende de como o slide exibe o
recorte:

| Exibição | Recorte máximo (largura lógica) |
|----------|--------------------------------|
| `.navegador` / `.recorte` dentro da margem | ~440 px (faixa de um campo) |
| `.sangria--janela` (1120 px, sangrando pela direita) | ~620 px (meia tela) |

Prefira fechar a borda do recorte em área vazia — corte no meio de uma palavra
parece defeito. O viewport de captura é **1440×900 com DPR 2**, então a fração
que você passa em `--recorte` vira pixels sobre 900 de altura, não sobre 1350:
confira a medida do arquivo com Pillow antes de calcular porcentagem de realce.

**E o layout mais rico da tela não é o melhor para o slide.** O Painel para
Entregadores passa a duas colunas internas por etapa acima de 1500 px, e cabe
quase o dobro de pedido — é para isso que existe TV grande. Capturado assim, o
cartão estreita e `2740 - Coleta 6118` sai cortado no meio da palavra: na TV de
50 polegadas ninguém repara, num slide lido no celular aquilo lê como **bug**.
A captura foi refeita mais estreita, e a vantagem do modo largo virou uma linha
de legenda. O critério da arte é um só — *o que precisa ser lido está
legível?* — e vantagem de operação que não sobrevive à miniatura se escreve,
não se fotografa.

**O print do manual é referência, não imagem do carrossel.** Ele existe para
ensinar um caminho: traz a tela inteira, o estado que o manual precisava e o
ruído do momento. Leia-o para saber quais campos existem, que valores são reais
e qual tela prova o quê — e então **faça a sua**, com o exemplo do carrossel
montado. A ordem de preferência é:

> **captura de resultado feita para o carrossel > tela de resultado desenhada
> pela peça > print de resultado pedido ao dono.**

O print do manual não está na lista, e é de propósito: ele não é degrau nenhum da
arte, nem recortado. Quando o único print que existe é de configuração — e no
manual é o caso mais comum, porque manual ensina caminho —, ele serve para você
saber o que a tela faz, e a imagem do slide sai desenhada mostrando o efeito.

Duas coisas acontecem quando o carrossel se serve do print do manual, e as duas
aconteceram na peça de *desconto por forma de pagamento*:

- **o ruído do print vem junto.** A capa saiu com "R$ 5,00 de cashback
  disponível!" e "Que tal usar um cupom? 8 disponíveis" ocupando o terço de cima
  do celular — dois avisos de outros recursos na imagem que precisava vender
  este. O manual conviveu com eles porque estava ensinando; o próprio texto dele
  manda cancelar o cashback antes de ler o total.
- **o exemplo continua sendo o do manual.** Manual mostra **um** caminho, e o
  desse usou 5% em tudo. Para mostrar a amplitude (% e R$, desconto e acréscimo)
  a peça pegou um segundo print de outro manual, com outra configuração — e
  publicou dois jogos de número para o mesmo recurso.

Some-se a isso que **moldura emprestada se recorta, não se muda**: todo problema
de arte vira problema de recorte, e o trabalho vai para medir borda de cartão e
sombra de pílula em vez de escolher o que aparece na tela.

Reaproveitar continua certo quando o objeto **não tem estado nem moldura** — o
cupom impresso do #99 é o mesmo cupom, fotografado do papel. Fora disso, o
print do manual paga o seu valor sendo lido, não colado.

**E print de manual nunca sustenta afirmação de slide.** O slide "combo de
quarta aparece só na quarta" saiu com o print do manual, que tem **os sete dias
acesos**, e a arte desmentia o título. Quando o slide afirma um estado da
interface, fotografe aquele estado — no sandbox, deixando a tela como estava
(abra, ajuste, capture e **devolva a configuração anterior**).

**Antes de capturar, olhe a prateleira.** Fotos de produto, tela de espera do
totem e faixa do cardápio já estão em `assets/fotos/`, e os aparelhos já estão
desenhados — o índice é [`references/mockups.md`](references/mockups.md), com a
folha do catálogo em `assets/catalogo/catalogo.png`. No slide, imagem da
biblioteca vai com o prefixo `skill:`, que o renderizador resolve:

```html
<img src="skill:fotos/foto-batata.png" alt="">
```

O que é prova de um carrossel só continua em `imagens-puras/`, com caminho
relativo. Regra: **se o próximo carrossel pode querer, entra na biblioteca.**

### 4. Slides

Cada slide é um **fragmento de body** em `carrosseis/<slug>/slides/NN-nome.html`
— sem `<html>`, `<head>` ou `<!DOCTYPE>`, e sem `<script>`. O renderizador
embrulha o fragmento com a fonte Mulish, o `base.css` e a medida do formato, de
modo que o que você revisa é exatamente o que sai em PNG.

Comece copiando um modelo de `assets/slides/`:

| Modelo | Serve para |
|--------|-----------|
| `capa.html` | slide 1: gancho **mais uma imagem** |
| `texto.html` | o custo, o limite, o "vale lembrar" |
| `mockup-computador.html` | tela do painel em janela de navegador, com realce |
| `mockup-celular.html` | tela de celular (cardápio digital, app) |
| — (`.notebook`, `.monitor` no `base.css`) | página deitada vista como **cena**, não como página: capa e slide de resultado |
| `mockup-totem.html` | Totem de Autoatendimento: tela em pé sobre coluna, com cardápio de exemplo |
| `mockup-tablet.html` | Cardápio Digital no Tablet: tela deitada em suporte de mesa, com cardápio de exemplo |
| `ilustracao-app.html` | tela que não dá para capturar, desenhada em CSS |
| `antes-depois.html` | comparação; traz um cupom térmico desenhado em CSS |
| `cta.html` | último slide, um pedido só |

Os modelos de totem e de tablet saem **prontos**, com a tela e as fotos da
biblioteca: troque o texto e os itens, não o aparelho.

As classes disponíveis estão comentadas em
[`assets/slides/base.css`](assets/slides/base.css). Cores, fontes e tom de voz
ficam em [`assets/marca.json`](assets/marca.json) — mudar a marca é mudar esse
arquivo, não os slides.

O logo não é `<img>`: use `<span class="logo"></span>`. A marca tem **duas artes
oficiais** e o renderizador injeta as duas; o `base.css` escolhe pelo fundo do
slide:

| Arquivo | Onde | O que muda |
|---|---|---|
| `logo-beefood-fundo-claro.png` | `.slide`, `.slide--suave` | "BEE" em preto |
| `logo-beefood-fundo-escuro.png` | `.slide--capa` | "BEE" em branco, e contorno branco no selo |

Asa branca, cabeça preta, tarja amarela e "food" vermelho ficam iguais nas duas.
**Nunca derive uma da outra**: filtro achata a marca em branco e negativo pixel a
pixel inverte a asa e a cabeça. Falta uma versão? Peça o arquivo ao dono.

#### Onde a imagem fica na faixa

A regra que manda nas outras:

> **Imagem sozinha na faixa vai centralizada e no maior tamanho que couber, e
> reta. Encostar numa borda e inclinar só se paga quando o outro lado tem
> conteúdo.**

| Situação | Como |
|----------|------|
| imagem ocupa a faixa toda, sem sangrar | `.figura` — no fluxo, centralizada, na maior largura que a base aceita |
| mockup sozinho na faixa, sangrando | `.sangria` com recuo **igual** dos dois lados; sangra só pela base |
| mockup dividindo a faixa com texto | `.sangria` encostada + `.cena3d`/`.g3d`; é aqui que o 3D tem função |

Sangrar não é ficar torto: mockup encostado num lado com o outro lado vazio troca
tamanho por nada.

#### Mockup em sangria

Aparelho inteiro dentro da margem sai com ~420 px numa arte de 1080, e a tela
dentro dele não se lê no feed. O padrão é **sangria**: o mockup ocupa pouco mais
de meia largura, começa por volta de 27% da altura e sai pela borda — ganha
escala, e o corte passa a sensação de que a tela continua.

- **Celular** (`.sangria .sangria--celular`) sangra pela **base**.
- **Computador** (`.navegador .sangria .sangria--janela`) sangra pela
  **direita**, porque é deitado; é assim que ele passa de 1000 px de largura.
- **Pela base à vontade; pela lateral, só o que não tem texto.** É a diferença
  entre sangria e corte: base cortada lê "a tela continua", e palavra cortada no
  meio lê erro de render. O notebook da capa de dark kitchen desceu de 940 para
  930 px por causa de uma pílula que virava `Mar`. Vale também para aparelho por
  cima de aparelho: sobreposição em cima de coisa decorativa (o menu lateral do
  painel) vira profundidade; em cima de rótulo, vira defeito.
- **Notebook** (`.notebook`) e **monitor** (`.monitor`) são a outra saída para
  tela deitada: a janela mostra a **página**, e eles mostram a **cena** — alguém
  sentado, olhando aquilo. Numa capa isso vale mais que 100 px a mais de tela.
- **Totem** (`.totem`) e **tablet** (`.tablet`) já estão desenhados, com largura
  de uso e tela de exemplo — veja [`references/mockups.md`](references/mockups.md)
  e a folha `assets/catalogo/catalogo.png`. Mexer neles pede rodar o
  `catalogo.py` de novo: as três primeiras tentativas do tablet leram como
  monitor de mesa, e a folha é o que pega isso.
- **Nos dois, a caixa do elemento é só o corpo da tela** e coluna, painel e
  suporte são absolutos pendurados embaixo.
- **Regra de moldura é sempre filho direto** (`.totem__tela > img`). `.moldura
  img` alcança também as fotos de dentro de uma tela desenhada, e o `height:
  100%` de lá anula o `aspect-ratio` delas.
- **Seletor de idioma** é `.bandeira` (emoji de bandeira recortado em círculo)
  com `.bandeira--anel` no idioma em uso. No tablet ele é retangular
  (`.bandeira--retangular`) e empilhado.
- **O texto mora todo acima do mockup.** A coluna que sobra ao lado tem 288 px,
  estreita demais para corpo de 38 px. Orçamento: com o celular em `top: 530px`
  cabem chapéu + título de 2 linhas + 2 linhas de corpo; com a janela em
  `top: 700px`, chapéu + título de 2 linhas + 4 linhas de corpo.
- **`.realce`** é o anel vermelho sobre o mockup. Posicione em porcentagem do
  `.navegador__tela` e **meça a posição no arquivo** — estimar na miniatura
  circula a linha errada, já aconteceu duas vezes.

#### Mockup 3D, só quando divide a faixa

`.cena3d` no contêiner e `.g3d .g3d--na-direita` (ou `--na-esquerda`) no mockup
põem o aparelho em perspectiva. O modificador é o **lado do slide em que o mockup
está**, e o giro é sempre **para dentro**: a quina que aponta para o texto é a que
afunda, e o aparelho parece entrar no slide. Ao contrário, ele parece cair para
fora da arte.

- **Só em celular e em janela de computador.** Totem e tablet vão sempre retos:
  o 3D valoriza a espessura da peça girando, e armário em pé não tem espessura —
  girado, lê como armário tombando.
- **Só com conteúdo ao lado.** É a coluna de texto ao lado que dá licença para o
  mockup sair do centro e girar. Sozinho na faixa, ele vai centralizado, grande e
  reto — inclinar ali troca tamanho por efeito.
- **Um a cada dois ou três mockups.** Serve para dar ritmo; em todos, vira efeito.
- **Nunca no slide em que o leitor precisa ler rótulo da interface.** A face que
  recua come contraste justo onde está a informação. Slide de "onde ligar" fica
  reto; slide de ilustração ou de resultado aceita 3D.
- **Aparelho que termina dentro do slide mostra a base da tela.** Aí a barra de
  ação da ilustração vai para lá (`flex: 1` no `.tela-app__corpo` e
  `margin-top: auto` no `.tela-app__aviso`), senão sobra um vazio de 300 px e a
  tela parece render pela metade. Em mockup que sangra pela base é o contrário.
- **`.rasgado`** serrilha a base do recorte, para corte de papel não parecer erro
  de render. Vai no **mesmo elemento** do `.g3d` (a máscara recorta box-shadow e
  pseudo-elemento junto) e **come a sombra** — o que é irrelevante em fundo
  escuro e custa caro em slide claro.

#### Quando a tela não existe: ilustrar

Ordem de preferência: **captura de resultado > desenho do resultado > print de
resultado pedido ao dono**, e nenhum print de configuração em nenhum dos três
(passo 3, em *a imagem do slide*).

Desenhar é o degrau de quem **não consegue capturar o resultado** — app Android,
impressora, balança, cenário que a conta de teste não tem, regra cujo efeito
mora em três telas. Não é o degrau de quem não conseguiu capturar *a tela*: se a
tela existe no navegador mas é um formulário, capturar não resolve nada, porque o
problema não era o acesso, era o assunto da imagem.

Quando o desenho é do aparelho, vale procurar o print de produção antes — não
para recortar, para **copiar layout, paleta e hierarquia**. O **manual da mesma
novidade** costuma ter o print do aparelho, e ele pode estar só no `main`
(o Cloud Agent parte de um snapshot). Antes de concluir que não existe, rode
`git fetch origin main` e
`git ls-tree -r --name-only origin/main -- manuais/<slug>`.

**Print que existe mas não encaixa não vira lixo.** Quando a proporção é outra
(print de totem em paisagem, tela do aparelho em retrato) ou quando a tela
cheia reduzida fica ilegível no feed, desenhe a tela em CSS copiando **layout,
paleta e hierarquia** do print, e traga dele as **fotos reais** com um script de
recorte na pasta do carrossel — coordenadas medidas no arquivo com Pillow, não
estimadas. Foto de comida inventada é o que mais denuncia tela desenhada.

Só ilustre (`.tela-app`, `.tela-totem`, `.tela-tablet`; modelos
`ilustracao-app.html`, `mockup-totem.html`, `mockup-tablet.html`, catálogo em
[`references/mockups.md`](references/mockups.md)) com as duas
condições: o comportamento desenhado está escrito na novidade ou no manual; e o
desenho usa o vocabulário do carrossel e **não** imita a interface real pixel a
pixel. Registre no `roteiro.md` o que é captura, o que é desenho e o print que
você pediu ao dono, para trocar depois.

**Nada de carimbo "ILUSTRAÇÃO" na arte.** Existiu, e saiu: numa peça de venda é
a única palavra que o leitor não esperava, rouba o olho no feed e avisa que o
que ele está vendo não é o produto. A honestidade fica onde não atrapalha a
peça — no desenho fiel (layout, paleta e **fotos reais** do aparelho) e no
`roteiro.md`.

**Texto de interface em outro idioma só entra se vier da tela.** `SEARCH`,
`MY CART`, `Order`, `Your bag is empty` é o aplicativo falando: tire de print ou
de captura, nunca do seu inglês. **Nome e descrição de produto são o contrário**:
quem escreve a versão em inglês do cardápio é o dono da loja, então traduzir
`BATATA FRITA COM CHEDDAR E BACON` para o exemplo não afirma nada sobre o
produto — desde que o carrossel não insinue tradução automática. Guarde essa
tradução num `traducoes.json` na pasta do carrossel e use **a mesma** na tela, no
print do cadastro e na legenda.

**Tela desenhada que é cortada tem de ser cortada num lugar limpo.** A
`.tela-totem__rolagem` corta o conteúdo que não cabe, com a barra da sacola fixa
no pé — sem isso sobra um vão branco de 200 px no meio da tela. O `font-size` da
tela é o que move o corte (tudo lá dentro é `em`): varra alguns valores e fique
com o que deixa o último cartão inteiro ou cortado **dentro da foto**. Corte em
cima de `R$ 8,90` lê como falha de render.

Pílula escura na capa escura desaparece: se a arte tiver alguma peça de
interface em `rgba(30,30,30,…)`, faça a versão clara antes de usá-la ali.

Cupom desenhado em `.cupom` é o caso mais tranquilo: bobina térmica em
monoespaçada é claramente desenho, e é a única forma de mostrar o "antes", que
não existe como captura.

**Relatório desenhado: o número é exemplo, e a copy não o repete.** Relatório é
onde o desenho compensa mais, porque o sandbox nunca tem volume para ele —
média que pede vinte pedidos sai *Poucos pedidos*, e traço em toda parte é a
prova de que a loja não usou o recurso, não de que ele funciona. O que o desenho
precisa entregar é a **estrutura**, que está toda no manual: os cartões do topo,
as etapas na ordem, as colunas da tabela, o gráfico por hora. Três regras seguram
a honestidade:

- **um jogo de números, e as somas fecham.** Se o cartão diz 128 entregas, a soma
  da coluna por entregador dá 128; se o modo é KM, `86,3 km × R$ 1,50` tem de dar
  o total da linha. É a primeira coisa que o lojista confere, e conta errada numa
  imagem nossa desmente a peça inteira.
- **a copy não cita o número.** O relatório responde *quanto é cozinha e quanto é
  rua*; a divisão de uma loja é dela. Escrito na copy, o exemplo vira promessa de
  resultado nosso.
- **a legenda diz que o dado é de exemplo**, uma vez, no texto do post — não
  carimbado na arte.

### 5. Render

```bash
python .cursor/skills/carrossel/scripts/renderizar.py \
    carrosseis/<slug> --contato
```

Sai em `carrosseis/<slug>/png/`, mais a folha de contato para ver o conjunto de
uma vez. O script recusa PNG fora da medida e recusa mais de 10 slides.
`--formato 1:1` ou `9:16` quando o pedido não for o 4:5 padrão.
`--guias` pinta o que a interface do Instagram cobre naquele formato: no feed é
só o **contador do carrossel**, no canto superior direito (por isso o topo
direito do slide leva só o `.contador`, nunca informação); no story (9:16)
são faixas largas no topo e na base. A saída de `--guias` e de `--formato`
diferente do padrão ganha sufixo no nome, para não sobrescrever a arte final.

#### Slide em vídeo, quando a novidade é movimento

O carrossel do Instagram aceita vídeo no lugar de uma imagem. Quando o recurso
**é** movimento (capa em vídeo, vitrine em vídeo), a capa parada gasta o melhor
argumento da peça:

```bash
python .cursor/skills/carrossel/scripts/filmar-slide.py \
    carrosseis/<slug>/slides/01-capa.html --tomada pc-capa-video \
    --conteudo carrosseis/<slug>/midias.json \
    --saida carrosseis/<slug>/video/01-capa.mp4
```

O slide não muda: o script mede no DOM a caixa da tela do mockup, fotografa o
cardápio quadro a quadro (avançando o `currentTime` do vídeo na mão) e costura
o filme por cima do PNG. O `empacotar.py` leva o MP4 numa pasta `video/` do
zip, e o PNG parado continua lá — quem publica escolhe.

Antes de filmar, **desligue os temporizadores da página** (o script faz isso):
cada quadro custa quase um segundo de relógio real, e o carrossel do cardápio
troca de mídia sozinho no meio da filmagem.

Filme a `--fps 25`, mesmo custando 2,5 min de captura: abaixo disso o MP4 sai a
25 fps com quadro repetido, o movimento anda aos pares e no feed parece
trepidação, não avanço de lente.

**Não filme arte com texto encostado na margem.** O zoom que dá vida ao banner é
o mesmo que empurra o título contra a borda, e o aplicativo já cortou a faixa
antes disso. Foi por aí que a capa em vídeo de *capas e destaques* saiu da
entrega: do quarto segundo em diante faltava letra no selo e no preço, e baixar o
zoom devolve o filme que não anda. Filmar compensa quando o que se mexe é foto,
produto ou interface — para arte com letra, ou ela nasce com 22% de folga na
margem, ou o slide é parado.

### 6. Revisão

```bash
python .cursor/skills/carrossel/scripts/conferir-texto.py <slug>
python ... <pasta> --novidade <slug-publicado>   # pasta com nome mais curto
python ... <pasta> --fonte <url>                 # gênero função: a página do site
python ... <pasta> --fonte manuais/<slug> --fonte manuais/<outro>   # e quando a fonte é o manual
```

Acusa qualquer sequência de seis palavras que apareça igual no texto (ou no
título) da novidade — nenhum rótulo do sistema chega a seis palavras, então o que
ele pega é cópia. Ele não julga o roteiro; para isso existe a tabela
fato → ângulo → slide.

**O manual é a fonte mais perigosa das três, e por isso `--fonte` também
recebe caminho.** Módulo em liberação não tem release nem página de vendas: o
fato vive só em `manuais/`, e ali o texto foi escrito pela casa. É bom, está à
mão, e recortá-lo não soa como cópia — soa como usar o que já existe. Passe
todos os manuais do grupo, repetindo `--fonte`; pasta vale pelo `.md` de dentro
dela. Na peça da Gestão de Entregas, dezoito manuais pegaram três frases, e as
três eram as **melhores** do roteiro, que é justamente o motivo de elas terem
sobrevivido a duas leituras: a frase do sistema no alto da janela do despacho
estava também **na imagem do mesmo slide**, e reescrevê-la devolveu uma linha
inteira de copy que estava sendo gasta duas vezes.

E há a armadilha da inflexão: `manda a rota para a rua` passa e `mandar a rota
para a rua` não. Quando o conferidor pega a versão do texto alternativo e deixa
a do slide, as duas são a frase do manual — troque as duas, não só a acusada.

**Ele também compara a peça com os outros carrosséis**, e isso é `AVISO`, não
erro. Prova se reusa entre peças de propósito; **a copy, não** — o slide
reaproveitado fala com um leitor diferente, e repetir o texto entrega duas
peças que parecem a mesma. Para o aviso ser sinal e não ruído, ficam de fora da
comparação a interface desenhada dentro dos mockups, o cromo do slide
(contador, pontos, `arraste`) e o texto alternativo, que descrevem prova. Fica
dentro o que a peça **escreveu**: a copy dos slides e a legenda.

Nem todo aviso é defeito. O CTA de peça de função repete de propósito — ele é
convenção, e a frase mais comum possível é a que funciona. Mas agora a decisão
é tomada, em vez de passar batida.

1. Abra a folha de contato: o conjunto tem ritmo, ou três slides de texto seguidos?
   A capa tem imagem?
1a. E, com tudo renderizado, **se você só pudesse publicar um slide, qual
   seria?** Se não for o 1, a capa está entregando o segundo melhor: a prova
   forte sobe, o texto da capa se reescreve em volta dela, e o slide que ficou
   sem prova costuma sair — peça de seis com o mais forte na frente vale mais
   que sete com ele no meio. Se a imagem promovida é prova de **leitura**, a
   capa perde o aparelho e fica com o recorte.
1b. **Tampe a copy e passe só pelas imagens.** Em quantas acontece alguma coisa?
   Imagem em que o que aparece é campo, interruptor ou lista de opções é tela de
   configuração, e tela de configuração se refaz — é motivo de voltar ao passo 3,
   no mesmo nível de texto ilegível. Peça inteira de configuração é o defeito que
   o dono reclamou três vezes antes de a skill mudar a ordem.
2. Abra em **tamanho real** os slides com print. Miniatura esconde texto ilegível
   e esconde realce fora de lugar — os dois erros mais comuns.
3. Confira que o mockup em sangria não cobriu nenhuma linha de texto nem os
   pontos do rodapé, que o mockup em 3D não caiu no slide que pede leitura de
   rótulo, e que nenhuma imagem sozinha na faixa ficou encostada numa borda —
   sozinha, ela vai centralizada e grande.
4. Toda afirmação do slide está no manual ou na novidade? Vale também para o que
   a frase afirma **sobre o leitor**: pergunte *quem poderia desmentir isto?* Se
   ele pode responder "não, eu não faço isso", é invenção e sai. O `roteiro.md`
   diz quais telas são captura e quais são desenho? E a imagem de cada slide
   **prova o título**, ou só ilustra o assunto dele?
5. A capa diz o fato **inteiro**? Nenhum eixo da novidade (o "ou" e o "e" do
   título) ficou de fora, e nenhum **exemplo** do release virou manchete. E o
   carrossel tem **um** jogo de números, o mesmo em todos os slides.
5a. **Leia só os títulos, em fila, e em voz alta.** Três perguntas, e cada uma
   pega um defeito que a leitura silenciosa do slide inteiro não pega:
   *(a)* dá para montar a lista do que o módulo passou a fazer? Título que só
   tem o ângulo ("a rota já chega montada") não nomeia nada — o nome entra antes
   dos dois-pontos, e nome no chapéu não conta;
   *(b)* sobrou algum `ele`, `dele`, `dela`, `isso`? Título se lê fora de ordem,
   então antecedente no chapéu ou no slide anterior não resolve;
   *(c)* a respiração tropeçou em algum? Ali falta palavra — artigo cortado
   ("lista vazia"), `de que` comido ("é sinal que deu certo") ou corpo sem verbo
   principal. Estilo telegráfico é de manchete de jornal, não de carrossel.
6. A capa diz o **nome do recurso**, e o subtítulo diz o que ele faz? Leia só
   ela e responda às duas: *qual é o nome?* e *o que aquilo faz?* Falha nas
   duas pontas — em conceito ("Cada forma de pagamento com o seu preço") e em
   cena ("O entregador chega e vê sozinho se o pedido já saiu"): as duas são
   boas frases e nenhuma nomeia. Em peça de **função** a pílula é o tema e já
   nomeia; em **novidade** ela diz "Novidade", então o nome só tem o título.
   O nome vai **inteiro**: se o release o batiza com um canal ("Campanhas
   Inteligentes **no WhatsApp**"), o canal é eixo e não sai por concisão —
   pergunte ao título *onde isso acontece?*.
   E o slide 2 **explica** esse recurso, em vez
   de contar história — a cena do release cabe ali, em uma frase.
7. Alguma imagem da arte veio de `manuais/`? Sai: print de manual é referência,
   e a arte usa captura feita para o carrossel. E o sandbox voltou à
   configuração em que você o encontrou?
7a. Olhe as capturas como quem **não conhece o produto**: elas dizem o que a
   peça promete, ou o contrário? Sandbox parada gera estado verdadeiro e
   péssimo (o painel com sete pedidos atrasados há 1h38min). Se a cena precisou
   ser montada, existe `cena.json` na pasta, `--cru` no script e aviso no
   `copy-instagram.txt`? E duas capturas da mesma peça concordam na **cena** —
   mesmos pedidos, mesmas colunas, mesmos contadores? (O relógio pode variar um
   minuto entre capturas; o que não pode é o painel ter sete itens num slide e
   seis no outro.)
8. Alguma frase explica enfeite de tela ("a bolinha verde marca…")? Algum
   diminutivo? Algum "ele" que não é o leitor nem o cliente dele? Os três saem
   — e o que fica no lugar é a consequência para o negócio.
8a. Procure **"o cliente"** na copy e responda, em cada aparição: *cliente de
   quem?* Quem lê é cliente da BeeFood, então "o cliente" sozinho é o leitor.
   Quando a frase fala de quem compra dele, ou entra o possessivo ("seu
   cliente") ou — melhor — a pessoa é nomeada pela ação: "quem largou a
   sacola", "quem tem cashback parado", que é como o cartão da tela se chama.
9. Algum slide alivia um trabalho ("não precisa traduzir tudo hoje", "aos
   poucos")? Sai: é aviso de limite, e ele planta a objeção justo antes do CTA.
   E o slide do problema — normalmente o 2 — elogia o leitor antes de mostrar o
   furo, ou entrega uma fatura na cara dele?
9a. **O CTA vende, ou ensina a ligar o recurso?** Cadastro, instalação e
   permissão são trabalho, e trabalho no último slide é a fatura antes da
   venda. Em peça de novidade o molde da série é chapéu **Já está no ar**,
   título no imperativo com **hoje**, subtítulo com o primeiro passo mais a
   linha de fechamento, e a pílula apontando para o **módulo que a peça
   vendeu** — não para um acessório de um slide do meio. E a arte dele pode ser
   **a mesma da capa**, no mesmo lugar e no mesmo tamanho: é a única repetição
   de prova que a skill aprova dentro de uma peça, porque o CTA manda abrir
   justamente o que a capa mostrou, e a peça abre e fecha na mesma cena.
   Detalhe em [`references/roteiro-e-copy.md`](references/roteiro-e-copy.md),
   em *o CTA de novidade não ensina a ligar o recurso*.
10. Nos slides de fundo escuro, o logo do topo é a arte de fundo escuro — "BEE"
    em branco, contorno branco no selo, tarja amarela e "food" vermelho?
11. Nenhum slide tem data na arte? O topo direito é só `.contador`, a capa
    inclusive. (Data impressa dentro de um print de verdade pode ficar.)
12. Saiu peça nova de uso geral (aparelho, tela desenhada, foto, script)? Ela
    **sobe** para a skill: foto e tela em `assets/fotos/`, aparelho no
    `base.css` + `catalogo.py`, script em `scripts/`. Atualize
    [`references/mockups.md`](references/mockups.md) e rode o `catalogo.py`.
13. Registre o que aprendeu em
    [`references/MEMORIA-CARROSSEIS.md`](references/MEMORIA-CARROSSEIS.md).

### 7. Entrega

Arte renderizada não é entrega. Quem publica precisa de **três coisas**: as
imagens uma por uma, a legenda pronta para colar e um arquivo único para baixar.

Escreva `carrosseis/<slug>/copy-instagram.txt` com, nesta ordem:

1. **cabeçalho** — novidade, data, formato e a ordem de publicação;
2. **legenda** — o texto que vai no campo de legenda, com as hashtags no fim;
3. **primeiro comentário** — uma pergunta, opcional;
4. **texto alternativo** — um por imagem, para o campo de acessibilidade.

A legenda **não é a soma dos slides**: ela é o mesmo assunto em prosa corrida,
para quem leu a capa e desceu. Vale o gancho repetido da capa (é o que amarra o
post), mas nunca o texto do release — o `conferir-texto.py` mede a legenda na
mesma régua dos slides.

```bash
python .cursor/skills/carrossel/scripts/empacotar.py <slug>
```

Gera `carrosseis/<NN-slug>/entrega/<NN-slug>.zip` com os PNG e o `.txt`, em nomes
soltos na raiz do zip (quem recebe arrasta direto para o celular, e a ordem de
publicação é a ordem alfabética). Capa alternativa e slide em vídeo entram em
subpastas (`capa-alternativa/`, `video/`), separados de propósito — quem arrasta
tudo leva só o carrossel. A folha de contato fica fora: é ferramenta de revisão,
e no meio das imagens alguém posta uma imagem a mais por engano.

Feche com commit e push, como manda a regra de commit por ação da
`MEMORIA-GERAL.md`.

## Estrutura da pasta de saída

```
carrosseis/<slug>/
├── roteiro.md            # fato→ângulo→slide e decisões de arte
├── copy-instagram.txt    # legenda, primeiro comentário e texto alternativo
├── capturar-telas.py     # só quando a captura exige clique
├── traducoes.json        # conteúdo injetado na captura, quando houver
├── imagens-puras/        # prints como saíram do navegador, nunca editados
├── slides/               # NN-nome.html (fragmentos de body)
├── png/                  # a arte final, 1080x1350
├── video/                # slide em vídeo, quando a novidade é movimento
├── entrega/NN-<slug>.zip # png + copy, o arquivo que vai para quem publica
└── folha-de-contato.png  # todos os slides numa imagem
```

## O que a skill guarda de um carrossel para o outro

```
.cursor/skills/carrossel/
├── assets/slides/base.css   # os aparelhos e as telas desenhadas
├── assets/slides/*.html     # modelos de slide, prontos para copiar
├── assets/telas/painel.css  # a aparência do painel, para a tela desenhada
├── assets/fotos/            # biblioteca: fotos de produto e telas reusáveis
├── assets/fundos/           # arte de fundo que entra no totem na captura
├── assets/midia/            # banner, cartaz de aviso e MP4 do cardápio digital
├── assets/catalogo/         # os aparelhos fotografados, e a folha com todos
├── scripts/capturar-totem.py, capturar-cardapio.py, fazer-midia.py,
│          filmar-slide.py, preparar-fundo.py, catalogo.py,
│          desenhar-telas.py
└── references/mockups.md    # o índice da prateleira: o que já existe e a medida
```

Carrossel novo começa por aí, e não por CSS novo. O que virou geral **sai** da
pasta do carrossel e vem para cá — foi o caso do capturador do totem, das fotos
de produto e do fundo de comida, que nasceram dentro do carrossel da tradução, e
do estúdio de mídia do cardápio digital, que nasceu no de capas e destaques.

## Regras de arte

- **Nenhuma data na arte.** O topo direito leva só o `.contador` ("1 de 7"), na
  capa também. Carrossel aprovado entra na fila de conteúdo e é publicado dias
  depois: data na arte faz a novidade parecer velha e impede reaproveitar o post.
  Data **dentro de print de verdade** fica (a do cupom é do pedido, não do post),
  e a data da novidade mora no `roteiro.md` e no cabeçalho da copy.
- **Uma ideia por slide.** Duas frases longas no mesmo slide são dois slides.
- **Tantos slides quantos a novidade tiver de assunto**, entre 6 e 8 (o teto
  técnico é 10). Oito não é meta: o carrossel da tradução fecha em 7 porque o
  oitavo slide só existiria para chegar a oito. Quem lê no feed costuma parar no
  quinto, então ponha o ganho no começo.
- **Slide novo custa slide velho.** Quando o assunto cresce e a peça bate no
  teto, não estique: pergunte **quais dois slides já entregam a mesma ideia de
  uso** e funda os dois. Na peça do totem, o adicional no item e o `Peça
  também` na sacola viraram um — os dois diziam "a tela oferece antes de deixar
  fechar" — e o cupom subiu do sexto para o quinto lugar, que é onde o leitor
  ainda está. Quando não há mais o que fundir e o corte só tira conteúdo, é o
  teto que cede: escreva o motivo no roteiro.
- **Prova boa se reusa entre peças.** Pedido do tipo "inclua aquele slide que já
  fizemos" não pede recaptura: o script de captura mora na skill e o conteúdo
  injetado mora na pasta do outro carrossel, então apontar um para o outro
  devolve a mesma tela. E o que se reusa não é a imagem, é o **par** — o mesmo
  item, no mesmo ponto da tela, nas duas versões; recapturar daria outro
  produto em outra posição, e a comparação perderia o que a torna prova.
  Junto com a imagem viaja **o limite do que a peça afirma** (a peça da
  tradução mostra o resultado e não promete traduzir), e o slide reusado entra
  pela **função que cumpre no arco**, não pela ordem em que o cliente encontra
  aquilo na tela.
- **Em novidade, a capa ANUNCIA: o título diz o nome do recurso e o subtítulo
  diz o que ele faz.** A forma varia (são seis moldes, e repetir a forma da
  peça anterior é o quarto vício); o **nome** não varia. Em peça de função ele
  costuma caber na pílula, que é o tema; em novidade a pílula diz "Novidade" e
  não nomeia nada, então **o título é o único lugar**. Três degraus, e o vício mora
  no do meio: "Nova etapa Pronto no Delivery" é changelog; "O entregador chega
  e vê sozinho se o pedido já saiu" é **enigma** — concreto, com cena, e sem o
  nome de nada; "Chegou o Painel para Entregadores" é a notícia. A cena do
  release vai para o slide 2, que é onde há espaço para contá-la. Teste, com
  **duas** perguntas: quem leu só a capa sabe dizer **o nome** do que chegou, e
  **o que aquilo faz**?
- **O nome do recurso vai inteiro, e o canal faz parte dele.** "As Campanhas
  Inteligentes já estão trabalhando" tem nome próprio, passa nas duas perguntas
  e voltou: falta **onde**. Se o release batiza o recurso com o canal ("no
  WhatsApp", "na impressão", "no Tablet"), o canal é eixo, e concisão corta
  palavra, nunca eixo — o subtítulo não cobre isso, porque se lê depois.
  Terceira pergunta do teste: **onde isso acontece?**
- **A capa leva o melhor slide da peça, e isso se decide na folha de contato.**
  A capa se escreve no roteiro, antes de existir captura; a melhor prova
  aparece depois. Com tudo renderizado, pergunte *se eu só pudesse publicar um
  slide, qual seria?* — se não for o 1, o que sobe é a **prova**, e o texto da
  capa se reescreve em volta dela. O slide que ficou sem prova normalmente sai,
  e encurtar a peça é ganho. Quando a imagem promovida é prova de **leitura**
  (o nome de cada campanha, o rótulo de cada gatilho), a capa perde o aparelho
  e fica com o recorte: ali o mockup é justamente o que come a largura.
- **"O cliente" é quem lê.** Quem abre o post é cliente da BeeFood, então "o
  cliente" sozinho aponta para ele — "quem marca a hora de falar é o cliente"
  voltou por isso. Para falar de quem compra dele, use o possessivo ("seu
  cliente") ou, melhor, nomeie pela ação: "quem largou a sacola", "quem tem
  cashback parado", que é como o cartão da tela se chama. Nomear pela ação é
  dizer o que a pessoa fez no sistema; narrar a pessoa é a vala do cinema.
- **O slide 2 explica o recurso que a capa nomeou** — o que se marca, sobre o que
  a conta incide, onde o cliente vê. Não é história ("você já faz isso no
  balcão") e não é manual: caminho de menu só no CTA.
- **Palavra concreta ganha de metáfora.** Se o recurso chama desconto, acréscimo
  e ajuste, é isso que o slide escreve — "preço", "o que mais entra" e parentes
  soam bem e não dizem o que a coisa é.
- **Pergunta de incômodo cabe no chapéu, não no título.** "Cansou de bebida
  esquecida na sacola?" prende — e as capas que abriram assim saíram sem dizer
  o nome de nada. Se o incômodo é mesmo a melhor porta, ele vira o chapéu e o
  título continua sendo o anúncio.
- **Cada slide entrega uma ideia de uso, com o verbo na frente.** A pergunta na
  cabeça de quem lê é "isso serve pra quê na minha loja?". "Destaque o combo do
  dia no meio do cardápio" entrega a ideia; "Você pode pôr um banner no meio do
  cardápio" só avisa que o recurso existe e pede licença. Destaque, mostre,
  programe, suba, apague, comece.
- **Nenhuma abertura se repete.** Sete imperativos em fila são template do mesmo
  jeito que sete "você pode" — a regra é sobre o conjunto, não sobre a frase.
  Varie entre o imperativo, o ganho dito direto e o reconhecimento do que ele já
  fez. "Você" não é cota nem palavra proibida.
- **As duas valas: o manual e o cinema.** Nomear campo e ensinar a mexer é uma
  ("Você marca em que dias a mídia aparece, de que horas a que horas"); narrar a
  cena do cliente em close é a outra ("Seu cliente rola o dedo e acha o combo").
  Fugir de uma não é cair na outra. Detalhe e antes-e-depois em
  `references/roteiro-e-copy.md`.
- **Clareza antes de piada, e antes de qualquer cota de sujeito.** "Combo de
  quarta aparece só na quarta" venceu "Na quinta você nem lembra", que é mais
  engraçada e não diz o que o recurso faz. Se a frase mais clara tem o recurso
  como sujeito, ela fica.
- **O registro muda com a voz.** Nos slides fala a BeeFood com o dono, em tom
  claro e correto ("Suba o seu primeiro vídeo hoje"). Nas artes de mídia fala o
  dono da loja no cartaz dele, em imperativo de rua ("Pede a grande. Confia.").
  O truncado que é marca do cartaz é erro no slide.
- **É peça de venda, na voz do site.** `beefood.com.br` é a régua: manchete é
  ganho ("Mais pedidos, menos filas no seu restaurante"), a linha de apoio é
  concreta ("Menos necessidade de garçons extras") e o slide fecha no que muda
  para o negócio — fila que anda, mesa que fecha mais alta, equipe que rende
  mais. Descrever funcionamento sem consequência é documentação, não post.
- **Nunca avise o limite do recurso.** "Não precisa traduzir tudo hoje", "aos
  poucos", "com calma": parece gentileza e entrega o contrário — aliviar um
  trabalho é admitir que existe um trabalho, e plantar essa objeção no slide
  antes do CTA é derrubar a peça no fim. Quem precisa do limite abre o manual.
  Honestidade se faz mostrando a tela certa (o cadastro onde o texto em inglês é
  escrito), não com aviso.
- **Quando o slide 2 é o do problema, ele elogia antes de cobrar.** Slide 2 é
  onde o leitor decide se arrasta: "Quanto seu salão **perde** por não falar
  inglês?" entrega uma fatura, e ninguém salva post para ler a própria conta.
  Comece pelo que ele já tem funcionando ("Seu cardápio é o seu melhor
  **vendedor**") e traga o furo depois, na mesma frase que traz a solução. Em
  peça que abre nomeando o recurso, porém, o slide 2 é a **introdução** dele, e
  não o problema.
- **Se a tela prova, o slide é a tela.** Antes de escrever cinco linhas
  explicando que o cardápio existe em outro idioma, veja se dois recortes da
  mesma tela não dizem isso sozinhos — mesmo item, mesma foto, mesmo preço, nome
  diferente. Recorte medido no DOM (mesma caixa nos dois idiomas) e capturado em
  escala 2; o texto vira uma linha.
- **Microdetalhe de interface não é conteúdo.** "A bolinha verde marca o idioma
  que já tem texto" é correto e não agrega nada a quem está no feed — é material
  de manual. Teste cada frase com "o que muda para ele se eu tirar isso?"; se a
  resposta é "ele sabe menos um detalhe da tela", corta e ponha a consequência
  no lugar. Enfeite de tela, nome de campo e regra fina de comportamento entram
  quando **são** o assunto do slide, nunca como explicação de brinde.
- **Nada de diminutivo.** "Bandeirinha", "bolinha", "telinha": aparece quando a
  gente tenta soar simpático e faz o recurso parecer pequeno. Escreva
  "bandeira", "sinal", "tela". Exceção só para nome próprio de produto.
- **Emoji: pouco e onde couber.** Até um por slide, e não em todos. Prefira os
  que a novidade usa (🖨️ 🛵) e os do assunto (🥤). Emoji que aponta (👇) vai
  encostado com `&nbsp;`, senão cai sozinho na linha. Slide de limite não leva.
- **A capa é a frase mais curta do carrossel**, com **uma** palavra no `.destaque`
  vermelho e nenhum emoji junto dela. Duas palavras vermelhas não destacam nada,
  e emoji ao lado do vermelho é grifo em cima de grifo.
- **A capa não repete a forma da capa anterior.** Três carrosséis seguidos
  abriram com pergunta e, no perfil, isso lê como fórmula. Leia as capas já
  entregues antes de fechar a sua e troque o molde: pergunta, afirmação do fato
  novo, ordem direta ou antes × agora. Afirmação tem um bônus — ela entrega a
  notícia na única linha que todo mundo lê, e obriga a escolher **qual** é o
  fato ("Sua capa agora é um carrossel" no lugar de "já tem vídeo?").
- **Emoji nenhum na frase que tem vermelho** — em qualquer slide, não só na
  capa. Se todos os títulos têm grifo, o emoji vai para o rótulo de um cartão,
  ou fica de fora: carrossel sem emoji passa, emoji colado no grifo não.
- **A capa tem imagem**, e a imagem é o resultado da novidade (o papel impresso,
  a tela nova) — nunca um ícone decorativo. Capa só de texto perde no feed.
- **A imagem da capa mostra um destaque só.** Cupom com duas linhas marcadas
  contradiz o slide que pede critério. Se a captura que existe não dá para
  recortar até sobrar um destaque, gere uma captura nova em que só ele apareça.
- **Na capa, tela cheia ganha de tela icônica.** Tela cujo miolo é gradiente ou
  foto (a de espera do totem, por exemplo) deixa um vão morto no meio da capa.
  Prefira a tela que mostra o recurso funcionando e enche a área útil — e, se a
  peça tiver duas pontas com o mesmo aparelho, deixe a tela icônica para o CTA.
- **Na capa, selo desenhado ganha de recorte ilegível.** Quando a capa precisa
  anunciar mais de um eixo, a tentação é pendurar recortes de tela ao lado do
  aparelho. Recorte de 1000 px reduzido para a coluna que sobra fica com 11 px
  de letra, e aumentado cobre o vidro — ou seja, rótulo e preço. Use o
  `.selo-recurso` com **a cor que a interface usa**, ao lado do aparelho e
  nunca em cima do vidro: na capa a tela é atmosfera, e prova é do miolo.
- **O selo de capa tem duas alturas.** Ao lado de um aparelho em pé sobra uma
  coluna de ~320 px, e nela a frase inteira em uma linha não passa de corpo 22
  — que ao lado de um título de 68 lê como crédito de rodapé e some na
  miniatura. Quebre em **nome grande** (`Cupom`, 50 px) e **nota em caixa alta
  pequena** (`DE DESCONTO`): o que estoura a largura é a frase, não a fonte.
- **Não desenhe número que o lojista configura.** Dentro de um print, o `5% de
  cashback` é da loja que aparece ali. Num selo desenhado ele vira promessa
  nossa, e quem escolhe a porcentagem é o restaurante. Todo dado que sai do
  print e vira arte **muda de dono** — no selo fica o nome do recurso.
- **E a nota do selo não afirma o que dois recursos juntos não fazem.** Dois
  selos lado a lado já sugerem soma; se os recursos não se combinam (cupom e
  cashback não se combinam), a nota não pode confirmar a sugestão.
- **Selo que só encosta no aparelho lê como adesivo.** O retorno vem nesta
  forma: *"tá só um texto com um painel atrás"*. Não é acabamento, é
  profundidade — e quem resolve é **oclusão**, não efeito. Use
  `.selo-recurso--encaixado`: a ponta entra ~60 px atrás da carcaça, com
  **padding maior desse lado** (o que some é margem, nunca texto) e gradiente
  **escurecendo para a ponta oculta**. Passando atrás, o selo também deixa de
  ter como cobrir o vidro.
- **Selo de capa leva ícone, porque o ícone é o que sobrevive à miniatura.** Na
  miniatura do feed o nome do recurso tem 9 px de altura e o desenho tem 30 —
  vale roubar espaço do texto para ele existir. Use `.selo-recurso--com-icone`
  com **SVG inline** e `stroke: currentColor` (emoji não serve: cada máquina
  desenha o seu). Com o ícone o texto perde ~90 px, e nota que quebra em duas
  linhas deixa um selo mais alto que o outro: o bloco é `nowrap`, e quem
  encurta é a frase.
- **Luz tem modo de mistura, e branco não acende com `screen`.** `.luz`
  (`screen`) para o fundo escuro atrás do aparelho; `.luz--tinta` (`multiply`)
  para a carcaça clara, que é a camada que prova que a luz bate no aparelho, e
  não só no fundo. Acender carcaça branca com `screen` não muda um pixel, e a
  correção é a mistura, não a opacidade. Nenhuma das duas passa por cima do
  **vidro**: ali moram nome e preço. Com mais de um selo colorido, faça **uma**
  luz que vá de uma cor à outra — duas poças separadas põem os selos em cenas
  diferentes. Detalhe em [`mockups.md`](references/mockups.md).
- **Imagem em pé na capa custa uma linha de subtítulo.** Aparelho em pé come
  ~830 px de altura: com título de 2 linhas cabe **1** linha de subtítulo, e o
  resto do recado vai para a legenda.
- **Metade dos slides, no mínimo, tem imagem.** Três slides de texto seguidos é
  sinal de que dois deveriam virar um.
- **Mockup em sangria**, não aparelho inteiro pequeno no meio do slide. E se ele
  está sozinho na faixa, a sangria vai centralizada, com recuo igual dos dois
  lados.
- **Número só se ele existir** na novidade ou no manual. "Reduz 30% dos erros"
  é invenção, e invenção em post de produto volta como reclamação.
- **Um jogo de números por carrossel.** A peça de desconto por forma de pagamento
  saiu com 5% nos slides do cardápio e −1,00%/+3,00%/+R$ 5,00 nos do caixa,
  porque cada print vinha de um manual com outra configuração. Lê como duas
  versões do produto. Monte **um** exemplo no sandbox e capture todas as telas
  com ele.
- **A capa diz o fato inteiro.** Antes de cortar, escreva o fato com todos os
  eixos — o "ou" e o "e" do título da novidade. "Desconto **ou** acréscimo, em %
  **ou** em R$" tem três eixos, e "Dê 5% de desconto no Pix" entregou um quarto
  do recurso. Concisão corta palavra, nunca eixo; e **exemplo do release não é
  manchete** ("Exemplos: 5% de desconto no Pix…" está lá para mostrar a
  amplitude). A imagem da capa também carrega os eixos: a lista de formas com um
  selo de desconto numa e um de acréscimo na outra mostra o par numa imagem só.
- **Ordem direta só quando o recurso tem um objeto só.** O verbo obriga a
  escolher o que se manda fazer; se o recurso vai nos dois sentidos, escolher um
  é jogar metade fora. Aí a capa é afirmação.
- **Toda afirmação é sobre o produto.** Inclusive o elogio do slide 2: "Seu
  cardápio é o seu melhor vendedor" descreve o cardápio e fica; "você já faz isso
  no balcão" descreve o leitor, não está em lugar nenhum e sai. Teste: **quem
  poderia desmentir esta frase?**
- **Números normais** (`1.`, `2.`, `3.`) — nunca ①②③. Mesma regra dos manuais.
- **Sem seta e sem número dentro da imagem.** Anotação assada no arquivo é
  linguagem de manual. Para dirigir o olhar no carrossel: recorte mais fechado e,
  se ainda faltar, o `.realce` — que é CSS no slide, não pixel no print.

## O que nunca fazer

- **Pôr tela de configuração na arte.** Campo, formulário, interruptor, janela de
  regras, lista de opções com um tique: mostra onde se mexe, e o slide precisa
  mostrar o que acontece. Vale capturada e vale desenhada — o defeito é o assunto
  da imagem, não a técnica. Quando o fato **é** a configuração, a arte é o efeito
  dela (passo 3, em *a imagem do slide*).
- **Carimbar "ILUSTRAÇÃO" na arte.** A pílula existiu e foi removida da skill: é
  a única palavra da peça que o leitor não esperava ler, e avisa que aquilo não
  é o produto justo no slide que devia vender.
- **Ilustrar comportamento que ninguém conferiu.** É o que o carimbo tentava
  compensar, e não compensava. O desenho mostra o que está escrito na novidade
  ou no manual, com layout, paleta e fotos reais do aparelho — e nada além
  disso. O `roteiro.md` registra o que é captura e o que é desenho.
- **Falar de um "ele" que não é quem lê.** Quem lê é o dono do restaurante, e a
  frase é dirigida a ele. Mas corrigir isso narrando o cliente em close é a vala
  do lado oposto: "seu cliente rola o dedo e acha o combo" tem o dono na frase e
  soa igualmente estranho.
- **Escrever "o cliente" quando o cliente é o leitor.** Sem possessivo, a
  palavra volta para quem está lendo o post. Ou "seu cliente", ou o nome da
  ação ("quem largou a sacola").
- **Entregar permissão em vez de ideia.** "Você pode ___" avisa que o recurso
  existe; o slide precisa dizer o que vale a pena fazer com ele.
- **Batizar o chapéu com o nome do campo.** "Destaques da capa", "Aba nova:
  Avisos", "Agendamento": o chapéu é o que se diz antes da frase, e ninguém diz
  isso em voz alta. Isso não é motivo para o nome do recurso ficar **só** no
  chapéu: ele vai no título, que é o que se lê.
- **Deixar o título sem o nome do recurso.** "No pico, a rota já chega montada"
  é frase boa e não se procura no menu. O molde é *nome, dois-pontos, o que ele
  te dá* — o ângulo fica na segunda metade.
- **Pôr pronome no título.** "quem marca é ele", "abre no celular dele": o
  título se lê fora de ordem, então antecedente no chapéu ou no slide anterior
  não vale. Nomeie a pessoa no próprio título.
- **Cortar artigo, comer o `de que`, deixar o corpo sem verbo.** "Lista vazia
  com a pílula verde é sinal que deu certo" é manchete de jornal, que paga por
  centímetro de coluna. Aqui lê como texto mal escrito, e o teste que pega isso
  é a leitura em voz alta.
- **Recortar a novidade em slides.** O carrossel se escreve a partir do fato; o
  texto do release não vai para a arte.
- **Afirmar o que o leitor faz, tem ou sente.** "Você já faz isso no balcão", "no
  caixa você propõe na hora", "isso te incomoda desde que você abriu a loja":
  não está na novidade, não está no manual e não está na tela. Nomeie o custo
  (ele é do produto) e pare aí.
- **Servir-se do print do manual para a arte.** Ele vem com o estado e o ruído de
  que o manual precisava — cashback, cupom, a tela inteira — e com o exemplo do
  manual, não o seu. E como manual ensina caminho, o print que ele tem é quase
  sempre de configuração. Leia o print para entender a tela; a imagem do slide
  você captura ou desenha.
- **Deixar o sandbox configurado do seu jeito.** Os manuais capturam no mesmo
  sandbox. Anote o que encontrou, capture, restaure.
- **Publicar dado pessoal.** Este repositório é público; nome, telefone e e-mail
  de cliente saem na imagem **pura**, não só na arte.
- **Editar `manuais/`, `MEMORIA-GERAL.md` ou `CHECKLIST-MANUAIS.md`.**
- **Prometer comportamento não conferido.** Se a novidade é vaga, diga menos.
