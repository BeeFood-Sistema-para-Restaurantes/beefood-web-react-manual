# Botão de WhatsApp no cardápio digital

- **Gênero:** novidade
- **Fonte:** [Botão WhatsApp no Cardápio Digital 💬](https://beefood.app/novidades/cardapio-digital-botao-whatsapp)
  — 19/10/2026, áreas Cardápio Digital e Marketing.
- **Manual:** [Botão WhatsApp](https://ajuda.beefood.com.br/cardapio-digital-botao-whatsapp)
  — na pasta,
  [`manuais/cardapio-digital-botao-whatsapp/`](../../manuais/cardapio-digital-botao-whatsapp/cardapio-digital-botao-whatsapp.md),
  com o [estudo de código](../../manuais/cardapio-digital-botao-whatsapp/fluxo-codigo.md)
  que leu o painel **e** o bundle publicado do cardápio. O fato duro desta peça
  vem de lá: o manual documenta **uma** configuração, de propósito, e o estudo
  de código tem as outras.
- **Nome de venda × nome do release:** os dois são o mesmo, e é raro. O release
  batiza *Botão WhatsApp no Cardápio Digital*, a aba do painel se chama **Botão
  WhatsApp** e é por *botão de WhatsApp* que o lojista pergunta — a pergunta
  frequente do manual é literalmente *"como coloco o WhatsApp no meu cardápio
  digital?"*. Não há tradução a fazer.
- **Formato:** 1080 × 1350 (4:5)
- **Slides:** 7

## O acervo, antes de escrever

Quatorze peças entregues, e **seis** encostam neste assunto: três no cardápio
digital (#3 capas e destaques, #7 cardápio no tablet, #11 — cuja tela de
rastreio é uma página do cardápio) e três no WhatsApp (#9 Campanhas
Inteligentes, #10 avisos de entrega, #11 o link dentro do aviso).

**E as seis contam a mesma direção: a loja falando.** Campanha dispara, aviso
sai, link é anexado — em todas, quem abre a conversa é o restaurante. Esta é a
primeira peça em que **quem fala primeiro é quem está comprando**, e é isso que
a separa da #9. A #9 vende alcance: seis campanhas trabalhando sozinhas no
WhatsApp do cliente dele. Esta vende o contrário do alcance — uma porta aberta
no lugar e na hora em que a dúvida aparece.

| Pergunta da skill | Resposta |
|---|---|
| Quais provas já existem? | duas conversas de WhatsApp **desenhadas**: `zap-avisos.html` (#10, duas conversas lado a lado, quatro avisos) e `zap-rastreio.png` (#11, uma conversa, do lado de quem pediu). Nenhuma das duas desenha o que esta peça precisa — ver *a conversa desta peça é o campo de envio* |
| O que a vizinha já prometeu? | #9: *"Campanhas Inteligentes no seu WhatsApp"*, com o canal dentro do nome. Aqui o canal também é o nome, e por isso a capa não podia repetir o molde — ver *a capa* |
| Que erro ela já cometeu? | a #3 publicou, sob o título *"combo de quarta aparece só na quarta"*, o print do manual com **os sete dias acesos**: a arte desmentia o título. O equivalente aqui seria escrever *somente com a loja fechada* em cima de uma captura de loja aberta. É por isso que o slide 5 é capturado com a loja **fechada** |

Do acervo veio método, em dois pontos: a **interceptação da resposta da API**
para o cardápio de produção desenhar (do totem, do tablet e da #11) e a escolha
do **cardápio modelo** `oneburger` em vez do sandbox dos manuais — ver *a cena*.

### A capa é ordem direta, e é a primeira da série

Placar dos moldes antes desta peça: afirmação do fato 5, anúncio de chegada 3,
pergunta 2, nome + dois-pontos 2 (a #14), nome + canal 1, nome + para quem 1 —
**ordem direta 0** e antes × agora 0.

A ordem direta estava zerada por uma razão, que a #13 registrou: ela *"só se
paga quando o recurso tem um objeto"*, porque o verbo obriga a escolher o que se
manda fazer. Aqui o recurso **é** um objeto, e um só: um botão. Não há metade
nenhuma para jogar fora escolhendo o verbo, e o que se manda fazer é
literalmente o nome do recurso — *ponha o botão de WhatsApp no seu cardápio*.

Os outros moldes foram escritos e caíram:

- **afirmação do fato** daria *"O seu cardápio digital agora tem botão de
  WhatsApp"*, e o sujeito é **o cardápio**, que é o lugar onde o recurso mora.
  Quem lê a primeira metade é informado de que tem um cardápio digital. É o erro
  de sujeito da #11, com outro substantivo;
- **antes × agora** pediria um "antes" em que a dúvida do cliente se perdia — e
  quem pode desmentir isso é o dono da loja, não nós;
- **nome + canal** foi o molde da #9, e aqui o canal já é o nome: sobraria
  "Botão de WhatsApp no WhatsApp".

E a ordem direta não colide com o CTA, apesar de os dois serem imperativos: a
capa manda **pôr** o botão no cardápio, que é o resultado, e o CTA manda
**ligar** a chave, que é o primeiro passo. A peça abre no fim e fecha no começo,
de propósito — é o mesmo arco que faz a arte do CTA repetir a da capa.

## O fato, o ângulo, e o que o slide diz

| Fato (release + manual + código) | Ângulo | O que vira slide |
|---|---|---|
| O cardápio digital passou a ter um **botão de WhatsApp**: o cliente toca e cai numa conversa com a loja | A capa manda fazer a única coisa que há para fazer — o recurso tem um objeto só | Capa |
| A conversa abre **com a mensagem já escrita**, e ela é a que o lojista escreveu: até **300 caracteres**, com **`{loja}`** virando o nome da loja | Quem tem dúvida não precisa nem saber como começar a falar; e a loja recebe a pergunta já identificada | 2 |
| **`{link}`** vira o endereço da página em que a pessoa clicou — dentro de um produto, chega o link daquele produto | É a diferença entre "oi, tudo bem?" e uma dúvida que já diz sobre o quê. Quem atende abre o link e vê o mesmo que ela está vendo | 3 |
| São **cinco lugares**: flutuante sobre o cardápio, abaixo do cabeçalho, antes dos destaques, no rodapé da loja e **dentro da sacola**. A posição decide a lista de formatos | O botão não é um enxerto no canto: ele entra no lugar do cardápio em que a dúvida costuma travar o pedido | 4 |
| **Quando aparece:** sempre, somente com a loja aberta ou **somente com a loja fechada** — esta "para pegar o cliente que não consegue fechar pedido sozinho" | Fora do horário o cardápio não fecha pedido, e hoje a pessoa simplesmente vai embora | 5 |
| **Em quais telas:** celular e tablet, computador ou os dois. No celular o flutuante fica **acima da barra da sacola** e sobe quando ela aparece, sem cobrir o botão de finalizar | A objeção é uma só — "isso não vai atrapalhar quem está pedindo?" — e a resposta é a imagem | 6 |
| Está em **Cardápio Digital → Botão WhatsApp**, a última aba da linha, e **a tela salva sozinha** | CTA: o primeiro passo é ligar a chave, e não há botão Salvar para procurar depois | 7 (CTA) |

**Ficou de fora, de propósito:**

- **a prévia ao lado do formulário.** É o fato mais simpático do release — ela
  responde na hora, nos dois aparelhos, e simula loja aberta e sacola cheia —
  e é **tela de configuração**: a arte dela seria um formulário com um desenho
  ao lado. Foi para a legenda, que é onde quem publica responde "dá para ver
  antes?";
- **o número de formatos.** O manual escreve "catorze" na introdução; o estudo
  de código avisa que **a lista vem do servidor** (`layoutsPorPosicao` chega no
  GET) e que formato novo aparece no painel sem deploy. Número de produto que
  pode mudar sozinho não vira manchete — o slide 4 fala da **posição**, que é
  fechada em cinco, e diz que a lista de formatos muda com ela;
- **dias da semana, faixa de horário e canais.** São a mesma régua do slide 5 e
  entrariam como lista de campos. Uma linha na legenda;
- **o evento `contato_whatsapp` do Pixel.** Cada clique é registrado e **não há
  tela no painel que mostre esse total**. Dizer "é medido" sem poder mostrar
  onde é prometer relatório;
- **a liberação por etapas.** A aba depende da permissão `botaoWhatsApp` e de
  uma lista de empresas no código. É verdade, é limite, e limite antes do CTA é
  a fatura antes da venda — está na legenda, que é por onde o suporte responde;
- **o outro WhatsApp, o do cabeçalho.** *Exibir WhatsApp*, da aba
  *Configurações*, é a confusão mais provável do suporte e por isso ocupa duas
  seções do manual. Num carrossel, explicar que o recurso **não** é um outro
  recurso gasta um slide ensinando a diferença entre duas coisas que o leitor
  ainda nem sabe que existem. Ficou uma linha no primeiro comentário.

## Slide a slide

| # | Arquivo | Título | Imagem |
|---|---|---|---|
| 1 | `01-capa.html` | Ponha o botão de **WhatsApp** no seu cardápio | `cel-flutuante.png` num `.celular` sangrando pela base — **captura** |
| 2 | `02-mensagem-pronta.html` | A conversa abre com a **mensagem já escrita** | `zap-botao.png` — **desenho** da conversa, no campo de envio |
| 3 | `03-link-da-pagina.html` | **Link da página**: a dúvida chega dizendo sobre o quê | `pc-produto.png` num `.navegador` com o endereço na barra — **captura** |
| 4 | `04-cinco-lugares.html` | **Cinco lugares**: no canto, no corpo do cardápio ou na sacola | `rec-flutuante.png` + `rec-sacola.png` — **captura**, dois recortes |
| 5 | `05-loja-fechada.html` | **Loja fechada**: o pedido que não dá para fazer vira conversa | `rec-fechada.png` — **captura**, com a loja fechada |
| 6 | `06-nos-dois-aparelhos.html` | **Celular e computador**: o botão sobe quando a sacola aparece | `pc-home.png` num `.notebook` + `rec-sacola-cheia.png` — **captura** |
| 7 | `07-cta.html` | Ligue o botão **hoje** | `cel-flutuante.png`, o mesmo da capa |

Lidos em fila, os sete títulos montam a lista do que o recurso faz, e nenhum
tem pronome. O slide 2 é a exceção estrutural da regra do nome: ele explica o
recurso que a capa acabou de nomear.

## Decisões de arte

### A cena: o cardápio modelo, e não o sandbox dos manuais

O botão **está no ar de verdade** em `menu.beefood.com.br/beefood3`, configurado
pelo manual #128 e deixado ligado de propósito. E essa é a captura que **não**
entra na arte, por três motivos que nada têm a ver com o recurso:

- a loja se chama **"BeeFood3 - Manual"**, escrito em letra grande no alto da
  tela. Numa peça publicada, o cliente lê o nome da nossa loja de teste;
- o logotipo dela é um marcador de lugar;
- o topo tem *"Você tem 13 cupons! Aproveite!"* e *"Acumule pontos a cada compra
  🎁"* — dois avisos de outros recursos ocupando o terço de cima da imagem que
  precisa vender este. É exatamente o ruído que a peça #4 trouxe junto com o
  print do manual.

A cena é o **cardápio modelo da casa**, `menu.beefood.com.br/oneburger` (ONE
STAND HAMBURGUERIA) — o mesmo da #3 e da #11. Não é loja de cliente, e por isso
o nome e o logotipo podem aparecer.

### A configuração entra pela resposta da API, e o cardápio de produção desenha

O cardápio modelo não tem o botão configurado (`whatsappJson: null`). Ligá-lo
pela tela significaria mexer na configuração de uma loja para capturar — o que
a skill proíbe sem devolver o estado, e aqui nem é preciso: o cardápio lê a
configuração de **uma** chave da resposta da loja.

```
POST .../api/rest/tempresaDelivery/validaDelivery/1   →  whatsappJson
```

O `capturar-telas.py` busca a resposta de verdade, troca **só** essa chave pelo
documento da tomada e devolve. Quem desenha o botão é o cardápio publicado: o
`pilulaRecolhe` que encolhe na rolagem, as folgas de 16/68 px do celular e de
24/24 px do computador, o selo dentro da sacola, a cor do tema. Nada disso é
CSS nosso, e nenhuma loja é alterada — é a mesma interceptação que o totem, o
tablet e a #11 já usavam.

Três detalhes que custaram rodada:

- **a resposta é comprimida.** O corpo é uma *string* JSON com zlib em base64
  (`eJ…`), não um objeto: trocar a chave é descomprimir, mexer e comprimir de
  volta. Lido como objeto, o script quebra em `'str' object does not support
  item assignment`;
- **`service_workers="block"`.** O cardápio é PWA, e sem isso o service worker
  responde do cache e a interceptação não vê a chamada (lição da #11);
- **o formato do documento saiu do bundle**, e está no `fluxo-codigo.md`. Campo
  adivinhado não é tela errada: `v > 1` e `on !== true` devolvem `null`, e o
  botão simplesmente não aparece.

O `cena.json` registra, tomada por tomada, o documento injetado, e `--cru`
mostra o que o cardápio modelo responde hoje — que é nenhum botão.

### A loja fechada é uma chave, e é ela que o slide 5 afirma

A loja modelo abre 01:00 e fecha 23:59, todos os dias: a janela em que ela está
fechada dura uma hora e não dá para esperá-la. O payload tem `aberto`,
`abertoDelivery` e `abertoPresencial`, e a tomada do slide 5 manda as três como
`false` junto com `quando: "fechada"`.

Não é maquiagem: é o estado em que aquela loja realmente entra todo dia à
meia-noite, e é a única condição em que o botão daquela configuração aparece. O
alternativa era escrever *"somente com a loja fechada"* em cima de uma captura
de loja aberta — que é o erro de arte da #3, documentado e evitado.

### A conversa desta peça é o campo de envio, e isso não é detalhe

As duas conversas desenhadas do acervo mostram **mensagem recebida**: balão
branco, do lado da loja, com o aviso que o sistema mandou. Aqui não há mensagem
recebida nenhuma — o `wa.me/…?text=` abre a conversa com o texto **no campo de
envio**, ainda não enviado. O manual diz isso com todas as letras: *"o cliente
pode apagar e escrever outra"*.

Então o desenho é a tela do WhatsApp com o campo preenchido e o botão de enviar
aceso, e é essa a imagem que prova o título do slide 2. Mostrar um balão já
enviado seria afirmar que a mensagem sai sozinha, que é precisamente o que o
produto não faz.

Por que desenhada, e não capturada: **não há número de WhatsApp conectado na
sandbox** — mesmo motivo da #10 e da #11. O que entra no desenho não foi escrito
à mão: o texto é o do `cena.json`, o nome da loja é o do payload e o endereço é
o da página capturada no slide 3, lido do `href` do próprio botão.

### O endereço na barra do navegador é o do print

O slide 3 afirma que o endereço que chega na mensagem é o da página em que a
pessoa clicou. A prova tem duas metades na mesma imagem: o botão no canto e o
endereço na barra, e as duas têm de ser do **mesmo** print — por isso a URL do
`.navegador__url` é lida da página capturada, e não escrita à mão.

O `href` do botão foi medido no navegador da captura e guardado no
`medidas.json`: é ele que mostra o endereço do produto já dentro do `?text=`.

### Recorte, e não aparelho, nos slides 4, 5 e 6

A capa, o CTA e o slide 6 levam aparelho; os slides 4 e 5 levam **recorte**. O
critério é o da skill: aparelho quando a capa quer reconhecimento, recorte
quando o que precisa ser lido é o que está escrito na tela. No slide 4 o assunto
é o botão em dois lugares diferentes da mesma página, e duas molduras de celular
lado a lado deixariam cada tela com 280 px.

Todos os cortes são **medidos no DOM** pela própria captura e gravados em
`medidas.json` — a caixa do `a.be-wa__alvo` e a da barra da sacola —, não
estimados na miniatura. É a regra herdada da #7, da #10 e da #11.

### O jogo de números

Um só, e ele vem do servidor: **300** caracteres de mensagem, **30** de texto do
botão, **cinco** posições. O tamanho de 80% a 140% e a lista de formatos ficam
de fora da arte pelo motivo escrito acima. Nenhum número de resultado aparece na
peça — o painel não tem a tela que o mostraria.

### O sandbox voltou como estava

Nada foi alterado em loja nenhuma: a única escrita desta peça é a troca de uma
chave na resposta de um POST, dentro do Chromium da captura. A configuração que
o manual deixou ligada em `beefood3` continua exatamente a mesma, e está
copiada no `cena.json` em *configuracaoEncontrada* para o caso de alguém
precisar conferir.
