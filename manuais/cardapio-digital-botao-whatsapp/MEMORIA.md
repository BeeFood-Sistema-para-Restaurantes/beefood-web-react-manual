# MEMORIA.md — #128 Botão de WhatsApp no cardápio digital

## O pedido, e o corte que ele traz

O dono avisou que a novidade havia acabado de entrar no `beefood-web-react` e pediu: *"existe
muitas configurações e muitas possibilidades, não vamos documentar tudo. Apenas crie uma
configuração básica e legal de botão flutuante no canto direito, que faça sentido, e mostre como
fica no cardápio digital desktop e mobile… a ideia é mostrar a funcionalidade e não ensinar fazer
100% das possibilidades pq se não seria um manual muito grande e sem sentido, já que a tela é
auto explicativa 100%. Faça um manual curto, sensato e com SEO."*

Então **o escopo é o produto deste manual**, não uma limitação dele. A tela tem cinco posições,
catorze formatos, agenda por dia e por hora, canais, subtítulo, pulsar e tamanho — e um texto
explicativo embaixo de cada opção. Documentar isso daria uma página que ninguém lê para resolver
o problema que a traz até aqui, que é *"como ponho o WhatsApp no meu cardápio"*.

O manual monta **uma** configuração, mostra o resultado nos dois aparelhos e resume o resto em
uma seção sem imagem. Sete imagens, dezessete setas.

## A configuração escolhida, e por quê

| Campo | Valor | Por que este |
|---|---|---|
| Onde o botão aparece | **Flutuante sobre o cardápio** | é a que o pedido nomeia, e a única que acompanha o cliente na rolagem inteira |
| Formato | **Pílula** | mostra ícone **e** texto. O círculo puro é mais bonito e ensina menos: com ele o campo *Texto do botão* não teria efeito visível, e a imagem do cardápio seria uma bolinha verde sem explicação |
| Lado da tela | **Direita** | o pedido diz "canto direito", e é o canto onde esse botão é esperado |
| Tamanho | **100%** | o padrão; mexer aqui só acrescentaria um número a conferir |
| Cor | **#25D366** | o verde do WhatsApp é o que o cliente reconhece sem ler |
| Texto | *Falar no WhatsApp* | é o padrão do campo, e lê bem nas duas capturas |
| Quando / dias / horário | sempre, todos os dias, dia inteiro | qualquer restrição aqui obrigaria o manual a explicar a regra de visibilidade inteira para a imagem fazer sentido |
| Telefone | `47 99999-8888` | **o número do próprio _placeholder_ do campo**. O repositório é público: nada de telefone de gente |
| Mensagem | *Olá! Vim pelo cardápio digital da {loja} e gostaria de tirar uma dúvida.* | usa `{loja}`, e assim a captura do cardápio prova a variável funcionando |

## O que o estudo do código mudou no texto

O detalhe está no `fluxo-codigo.md`; o que mudou a escrita:

- **A tela salva sozinha.** `useAutoSave` grava a cada mudança, com o toast *Salvo
  automaticamente*, e **não existe botão Salvar** — é a única tela do Cardápio Digital assim.
  Virou aviso no Passo 1, pergunta no FAQ e linha da tabela de problemas, porque quem mexe
  "só para ver" já mudou o cardápio do cliente.
- **Quatro validações travam a gravação**, não avisam e seguem: horário inicial maior que o
  final, telefone ausente quando a filial não tem WhatsApp, telefone incompleto e mensagem acima
  de 300. É o sintoma *"a tela não salva"*, e sem saber disso o leitor culpa a internet.
- **A configuração é por filial** (`empresaID` + `filialID` no POST). Quem tem duas lojas
  configura uma e acha que o sistema perdeu a outra. Ganhou linha na tabela e pergunta no FAQ.
- **A aba tem porta dupla:** a permissão `botaoWhatsApp` do grupo de acesso **e** uma lista de
  empresas liberadas no código (`WHATSAPP_BOTAO_EMPRESAS`, hoje duas). Virou pré-requisito e
  primeira linha da tabela de problemas — sem isso o leitor procura uma aba que a conta dele não
  tem, e o suporte procura defeito onde não há.
- **Os limites vêm do servidor.** O GET devolve as regras junto com a configuração (300
  caracteres de mensagem, 30 de rótulo, tamanho de 80 a 140); o arquivo local é só o que vale
  enquanto a resposta não chega. Por isso o manual cita os números como estão hoje e **não**
  promete que a lista de formatos é fechada.
- **Existe outro WhatsApp na mesma tela.** O *Exibir WhatsApp* da aba *Configurações* põe o ícone
  entre as redes sociais da loja, e é um recurso diferente. A própria aba avisa isso numa caixa
  azul; o manual repete no Passo 2 e no FAQ, senão o leitor liga duas vezes a mesma coisa.
- **O clique é medido, mas não é mostrado.** Cada toque dispara o evento `contato_whatsapp` no
  Pixel, e `contato_whatsapp` não aparece em lugar nenhum do painel. A pergunta *"quantos
  clicaram?"* está no FAQ com essa resposta, em vez de prometer relatório.

## As imagens: o que a captura ensinou

Sete tratadas, de oito puras (`06-previa-computador.png` ficou de reserva e não é citada).
Cinco do painel, duas do cardápio do cliente.

- **A tela rola por dentro.** O conteúdo mora num `div` com `overflow-y-auto` de 2455 px:
  `window.scrollTo` e `page.mouse.wheel` não movem nada. Rolar é escrever no `scrollTop` desse
  `div`, e as três telas do manual são três valores fixos (0, 545, 1200).
- **Viewport de 1100 de altura**, não os 900 do padrão. O formulário tem a prévia ao lado, e o
  cartão de formatos é alto; com 900 cada passo precisaria de duas imagens.
- **As coordenadas das setas foram medidas no DOM**, não na grade de frações. O
  `capturar.py medir` imprime a caixa de cada alvo já em pixel da pura
  (`getBoundingClientRect() * 1.5`). Num formulário com campo colado em campo isso é mais rápido
  e mais exato, e deixa a conta auditável: quem desconfiar de uma seta roda `medir` e compara.
- **Faixa clara dos dois lados**, como no #126. Três alvos encostam na borda **direita** do
  cartão — a chave de ligar, o seletor de formato e o *Lado da tela* — e etiquetá-los pela
  esquerda faz a seta atravessar o rótulo inteiro.
- **Uma seta a menos, de propósito.** Na imagem 03 havia uma terceira seta para a chave
  *Computador*; a linha de texto logo abaixo atravessa a imagem inteira, e a seta vinda de baixo
  cortava a frase. As duas chaves ficaram com uma seta só, e a tabela explica as duas.
- **A seta da aba chega pela linha de baixo.** Na altura do rótulo, a etiqueta 2 da imagem 01
  terminava no ícone de recarregar, que mora logo depois da última aba.
- **O cardápio do cliente guarda cache.** Depois de salvar, o botão levou alguns minutos para
  aparecer em `menu.beefood.com.br`. O `capturar.py` confere a presença de `a.be-wa__alvo` e
  **avisa** em vez de gravar um print sem botão — e o atraso virou a primeira causa da linha
  *"liguei e o botão não aparece"* na tabela de problemas.
- **Celular em DPR 2 com `is_mobile`.** O formato *Pílula recolhida* e os deslocamentos de
  rodapé dependem de o cardápio se entender como celular; sem `is_mobile` o print sai com a
  geometria de computador numa tela estreita.

## O cenário: o que ficou no sandbox

Conta **BeeFood3 - Manual** (`contato@beefood.com.br`), empresa **38311**, filial **39202** — uma
das duas empresas liberadas para a aba. O botão ficou **ligado** ao fim do trabalho, com a
configuração da tabela acima, e é o que se vê em `menu.beefood.com.br/beefood3`.

Deixar ligado é de propósito: é uma loja de teste sem cliente, o telefone é falso, e assim as
capturas podem ser refeitas sem montar o cenário de novo. Nada foi apagado nem desligado, e
nenhum dado de outra empresa foi tocado — o POST carrega `empresaID` e `filialID`, e só.

## Os arquivos desta pasta

| Arquivo | Para que serve |
|---|---|
| `cardapio-digital-botao-whatsapp.md` | o manual |
| `fluxo-codigo.md` | o que a tela faz de verdade, lido no código (uso interno) |
| `texto-documentation.ia.md` | o prompt de publicação |
| `capturar.py` | as capturas do painel e do cardápio, e o `medir` que dá as coordenadas |
| `annotate.py` | setas e etiquetas das sete imagens |
| `conferir-setas.py` | confere se o texto e as setas falam a mesma coisa |

Para refazer tudo, nesta ordem: `capturar.py` → `annotate.py` → `conferir-setas.py`.

## O que ficou para depois

- **As outras quatro posições não têm imagem.** Topo, antes dos destaques, rodapé e dentro da
  sacola estão citadas na seção de resumo. Cada uma tem a sua lista de formatos, e fotografar
  todas daria mais de trinta imagens para um recurso que a tela explica sozinha. Se um dia o
  suporte perceber que uma delas gera dúvida, ela merece uma seção — não o manual inteiro.
- **A agenda não foi exercitada.** *Quando aparece*, dias da semana e faixa de horário estão no
  resumo e no FAQ, mas não houve captura do botão aparecendo e desaparecendo pelo relógio:
  provar isso exige mexer no horário do aparelho ou esperar o dia virar.
- **O evento do Pixel não foi conferido no destino.** O código dispara `contato_whatsapp`; não
  foi aberto o Gerenciador de Eventos da Meta para ver o evento chegando. O manual não afirma
  que chega — diz que o clique é registrado no Pixel e que o painel não mostra o total.
- **O `conferir-setas.py` é deste manual, de propósito** — veio do #127. Os estilos antigos de
  `annotate.py` variam demais para um script único na pasta `scripts/`.
