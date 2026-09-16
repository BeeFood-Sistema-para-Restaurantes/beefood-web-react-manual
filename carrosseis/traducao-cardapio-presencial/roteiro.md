# Carrossel — Cardápio presencial em inglês e espanhol

- **Novidade:** [Cardápio presencial em inglês e espanhol](https://beefood.app/novidades/traducao-cardapio-presencial) — Novidade, Cardápio + Aplicativos
- **Manual:** [Tradução do cardápio presencial: inglês e espanhol](https://ajuda.beefood.com.br/cardapio-presencial-ingles-espanhol)
- **Formato:** 4:5 (1080×1350), **7 slides**
- **Pasta:** `carrosseis/traducao-cardapio-presencial/`

Sete slides, não oito: a novidade tem uma ideia grande (o cliente lê o cardápio
na língua dele) e três apoios (totem, tablet, e o fato de não existir um segundo
cardápio para manter). Esticar para oito pediria um slide de "onde ativar", que é
exatamente o que este carrossel não é.

## O que este carrossel **não** faz

O manual ensina a configurar; o carrossel divulga. Então ficam **fora**:

- caminho de menu para ligar a tradução no totem (`Aplicativos → Totem →
  Configuração → Idiomas`);
- o aviso de que o sistema não traduz sozinho;
- a lista de campos traduzíveis e a de campos que não mudam;
- a tabela de problemas comuns.

Nada disso é mentira — é material de manual. Quem quer o passo a passo clica no
link; quem está no feed quer saber **o que muda no salão**.

Um cuidado que isso obriga: o carrossel **nunca insinua tradução automática**.
Ele não diz "você traduz sozinho" e também não diz "o sistema traduz". Mostra o
cadastro onde a versão em inglês mora (slide 5) e trata o trabalho como coisa
tranquila e parcial (slide 6). Promessa de tradução automática voltaria como
reclamação.

## Fato → ângulo → o que o slide diz

| Fato (novidade/manual) | Ângulo | O que o slide diz | Slide |
|---|---|---|---|
| O cliente troca o idioma tocando numa bandeira, no Totem e no Cardápio Digital no Tablet; os idiomas são português, inglês e espanhol | o turista que entrou e não pediu é venda que já estava dentro da loja | "Seu cardápio já fala inglês?" | 1 |
| O turista encontra o cardápio todo em português e desiste de pedir | ninguém vai embora por causa do preço nessa cena; vai embora porque não entendeu | o que ele faz hoje: tradutor no celular, mímica, ou a porta | 2 |
| No totem o seletor fica na tela de espera, embaixo do FAÇA SEU PEDIDO, e continua no topo durante o pedido | a decisão do idioma vem antes do pedido, e não trava nada se ele mudar de ideia | "Ele escolhe o idioma antes de pedir" | 3 |
| No tablet as bandeiras ficam na coluna da esquerda, sem configuração; os textos do app (SEARCH, MY CART, MY BILL) já vêm traduzidos | na mesa, quem resolve é o cliente — sem chamar ninguém | "No tablet é a mesma coisa" | 4 |
| Três bandeiras na linha do Nome; um único SALVAR E SAIR guarda português e as duas traduções; bolinha verde marca o idioma que já tem texto | o medo é manter dois cardápios; não é isso que acontece | "A versão em inglês mora no mesmo produto" | 5 |
| Item sem tradução continua em português, nada fica em branco; a ordem sugerida é setor → grupo de opções → mais vendidos | o que travaria a adoção é achar que precisa traduzir tudo antes de ligar | "Não precisa traduzir tudo hoje" | 6 |
| As bandeiras aparecem para lojas com Totem de Autoatendimento ou Cardápio Digital no Tablet | quem já tem o equipamento não precisa comprar nada | "Tem totem ou tablet? Então as bandeiras já estão aí" | 7 |

## Slides

| # | Arquivo | Tipo | Ideia única | Imagem |
|---|---------|------|-------------|--------|
| 1 | `01-capa.html` | capa com imagem | o cardápio passou a falar a língua do cliente | totem ilustrado com o cardápio em inglês, centralizado, com o pé saindo pela base |
| 2 | `02-cena.html` | texto | o turista não vai embora por preço | — |
| 3 | `03-totem.html` | mockup 3D + texto ao lado | ele escolhe a bandeira antes de começar | totem ilustrado na tela de espera, com o seletor embaixo do botão |
| 4 | `04-tablet.html` | mockup em sangria | na mesa as bandeiras já estão na lateral | tablet ilustrado com `Cola US` traduzido e o item de baixo em português |
| 5 | `05-mesmo-cadastro.html` | print real em janela | a tradução mora no mesmo produto | captura do cadastro da Coca Cola com as três bandeiras e as bolinhas verdes |
| 6 | `06-aos-poucos.html` | texto com lista | dá para traduzir aos poucos | — |
| 7 | `07-cta.html` | CTA com mockup | quem tem o equipamento já tem o recurso | página de novidades no celular, captura real |

Cinco dos sete slides têm imagem, e a capa é um deles.

## Decisões de roteiro

**A capa responde à própria pergunta.** "Seu cardápio já fala inglês?" só funciona
porque a imagem mostra um totem com o cardápio em inglês — a pergunta é retórica
e a resposta está na arte, não no texto. Sem a imagem, o dono lê "não" e passa. A
palavra em vermelho é **inglês**, uma só; o espanhol entra no subtítulo, que é
onde cabe a segunda informação.

**Qual tela vai na capa: o cardápio, não a de espera.** A tela de espera é mais
icônica — botão vermelho grande e as três bandeiras embaixo — e foi a primeira
tentativa. O problema apareceu no render: o miolo dela é um gradiente (no
aparelho de verdade roda um vídeo), e na capa isso virou um vão morto de uns
300 px no meio da imagem. O cardápio enche a tela e ainda prova a frase da capa,
com `DRINKS` e `Cola US`. O seletor foi para o slide 3, onde a coluna de texto ao
lado equilibra o vão.

**O subtítulo da capa tem uma linha.** Vale registrar porque contraria a rodada
anterior, em que duas linhas ficaram melhores: lá a imagem era um cupom deitado,
aqui é um aparelho **em pé**, que come 830 px de altura. Com duas linhas de
subtítulo o totem começava dentro do texto. Imagem em pé na capa custa uma linha
de subtítulo.

**Um setor em português na capa.** `MOLHOS ADICIONAIS` aparece sem tradução ao
lado de `DRINKS`, e dilui um pouco o "fala inglês". Ficou porque é o
comportamento real (setor sem tradução não fica em branco) e porque é o que o
slide 6 promete. Capa que promete mais do que o produto entrega volta como
reclamação — e esse detalhe é justamente o que faz um dono desconfiado acreditar
no resto.

**O slide 2 não fala de sistema.** É a cena do salão inteira — tradutor no
celular, mímica, a porta. É o slide que faz o dono reconhecer o problema antes de
ouvir a solução, e o que segura a atenção até o terceiro. A caixa de fecho existe
para nomear o custo: não foi o preço, foi o cardápio.

**Totem ilustrado, e com selo.** Totem e tablet rodam em Android e não sobem no
Cloud Agent (`MEMORIA-GERAL.md`, seção 6), então as duas telas são desenhadas em
CSS (`.tela-totem`, `.tela-tablet`) e os dois slides levam `.selo-ilustracao`.
O desenho só mostra o que está escrito no manual, e **usa só texto documentado**:
`DRINKS` (o setor Bebidas traduzido), `MOLHOS ADICIONAIS` (setor sem tradução,
que continua em português), `Cola US` / `The drink cola` (o produto do exemplo),
`SEARCH`, `MY CART`, `MY BILL` e `CANCEL ORDER` (textos do próprio aplicativo).
Nada de string inventada em inglês.

Duas coisas que o desenho ganhou no caminho, e que valem para o próximo
aparelho desenhado:

- **carcaça clara no slide escuro.** O totem preto em capa preta virou uma
  silhueta invisível. `.totem--claro` é o modelo branco do catálogo, e resolve
  sem inventar produto.
- **o que faz ler "tablet" e não "monitor"** é moldura proporcional e igual nos
  quatro lados (`padding: 2.2%`), canto de 38 px e suporte pequeno. Foram quatro
  variantes do mesmo slide renderizadas e comparadas: moldura em px encolhe
  quando o mockup cresce, canto de 20 px é canto de monitor, pé largo é base de
  monitor, e um berço na frente da moldura de baixo sai como borrão. A tela
  continua 16/10, que é a do tablet Android — 4/3 parece "mais tablet" e só
  encolhe a tela inventando um aparelho que o cliente não tem.

> **Pendente com o dono:** print real do Totem de Autoatendimento (tela de espera
> com o seletor e cardápio em inglês) e do Cardápio Digital no Tablet (bandeiras
> na coluna da esquerda). Quando chegarem, substituem os desenhos dos slides 1, 3
> e 4 e os selos saem.

**O único print real é o do cadastro, e é o slide mais importante dos apoios.**
O slide 5 responde ao medo que mata a adoção — "vou ter que manter dois
cardápios" — e a resposta só convence vendo: é o mesmo modal da Coca Cola, com as
três bandeiras na linha do Nome e duas bolinhas verdes. Desenhar essa tela seria
jogar fora o argumento; ela existe no sandbox e foi capturada.

**O 3D só no slide 3.** É o único em que o aparelho divide a faixa com uma coluna
de texto, que é a condição para girar (`MEMORIA-CARROSSEIS.md`, *Mockup 3D*). Na
capa, no 4 e no 7 a imagem está sozinha na faixa: vai centralizada, reta e no
maior tamanho que couber.

**A data no print do CTA fica.** O celular do slide 7 mostra a página de
novidades, e nela aparece "16/09/2026" — data que o site publica, dentro de um
print de verdade. É o caso que a memória abre ("Nada de data na arte"): a arte
não tem data, e essa é da página fotografada. Mesmo print do CTA do carrossel
anterior.

**Emoji em dois dos sete.** 🇺🇸 no slide 4 e 🌎 no 7, e a capa sem nenhum — ela já
tem a palavra em vermelho. Os dois são o assunto do post, então informam em vez
de enfeitar; nos slides de texto puro (2, 5 e 6) não entra nenhum, porque ali o
emoji só apareceria para animar parágrafo. As bandeiras **dentro** dos mockups
não são emoji soltos: são o emoji recortado em círculo (`.bandeira`), do jeito
que o sistema desenha o seletor.

**Duas frases voltaram do `conferir-texto.py`.** A bolinha verde ("então dá para
ver num relance o que falta") e o grupo de opções ("atende todos os produtos que
o usam") tinham saído iguais à novidade, palavra por palavra, sem que eu
percebesse — são as frases boas do release, e é justamente por serem boas que a
mão as copia. Foram reescritas.

## Capturas

```bash
python carrosseis/traducao-cardapio-presencial/capturar-telas.py
```

Sai em `imagens-puras/`:

- `05-cadastro-bandeiras.png` — modal do produto Coca Cola 350ml com as três
  bandeiras na linha do Nome (Brasil selecionado, inglês e espanhol com bolinha
  verde). É a janela em sangria do slide 5.
- `05-cadastro-recorte.png` — a faixa do Nome com as bandeiras, para o realce.
- `07-novidades-celular.png` — a página de novidades no celular, para o CTA.

Produto do exemplo: **Coca Cola 350ml** do setor **Bebidas** (BeeFood3 - Manual),
o mesmo que o manual usa — e que já tem inglês e espanhol cadastrados no
sandbox, por isso as duas bolinhas verdes aparecem.

O sandbox **tem** o recurso: a empresa de teste tem Cardápio Digital no Tablet,
então as bandeiras aparecem no cadastro. Se um dia desaparecerem, é contrato, não
bug (o manual diz que sem Totem nem Tablet não há bandeira).

## Render e entrega

```bash
python .cursor/skills/carrossel-novidades/scripts/renderizar.py \
    carrosseis/traducao-cardapio-presencial --contato
python .cursor/skills/carrossel-novidades/scripts/conferir-texto.py traducao-cardapio-presencial
python .cursor/skills/carrossel-novidades/scripts/empacotar.py traducao-cardapio-presencial
```

A legenda, o primeiro comentário e o texto alternativo de cada imagem estão em
[`copy-instagram.txt`](copy-instagram.txt). O que vai para quem publica é
`entrega/traducao-cardapio-presencial.zip`.
