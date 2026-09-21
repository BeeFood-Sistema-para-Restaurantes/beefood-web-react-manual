# Campanhas Inteligentes no WhatsApp

- **Gênero:** novidade
- **Fonte:** [Campanhas Inteligentes no WhatsApp](https://beefood.app/novidades/whatsapp-campanhas-inteligentes)
  — 28/07/2026, área Marketing
- **Manual:** [Campanhas Inteligentes](https://ajuda.beefood.com.br/campanhas-inteligentes-whatsapp)
  — na pasta, [`manuais/campanhas-inteligentes/`](../../manuais/campanhas-inteligentes/campanhas-inteligentes.md)
- **Formato:** 1080 × 1350 (4:5)
- **Slides:** 6 (eram 7; ver *a capa herdou o slide 3*)

## O acervo, antes de escrever

As oito peças entregues falam de **cardápio, totem, tablet, dark kitchen e
entrega** — o pedido chegando e o pedido saindo. Nenhuma fala de **marketing**,
e não há em `imagens-puras/` nenhuma tela de Food Marketing, de WhatsApp ou de
segmentação. É a primeira peça deste módulo, e não há prova para reusar.

Do acervo vem método: a captura da página de novidades no celular para o CTA
(convenção da casa desde a peça 1) e o recorte por caixa medida no DOM, do
tablet e do painel do entregador.

**A capa não repete a forma da anterior.** O Painel para Entregadores usou o
*anúncio de chegada* ("Chegou o…"). Aqui o molde é o **nome do recurso**, com o
canal dentro dele — "Campanhas Inteligentes no seu WhatsApp" —, e o que a
novidade tem de mais forte (seis prontas, quatro ligadas) fica no subtítulo.
Placar dos moldes depois desta peça: pergunta 2, afirmação 1, nome do recurso
2, anúncio de chegada 1, ordem direta 0, antes × agora 0.

## O fato, o ângulo, e o que o slide diz

O manual foi escrito lendo o código-fonte (`modelos.js`), então os fatos de
configuração abaixo são mais duros que o release.

| Fato (release / manual) | Ângulo | O que vira slide |
|---|---|---|
| O recurso se chama **Campanhas Inteligentes**, roda **no WhatsApp** e é a terceira aba de Food Marketing → Campanhas WhatsApp. A conta já vem com **seis**, e **quatro nascem ligadas**. As seis: carrinho abandonado, recebeu o cardápio e não pediu, recuperador de vendas, cashback parado, aniversário, boas-vindas / 2ª compra | O nome e o canal são a notícia; a prova é ver as seis, com nome, gatilho e estado, sem precisar abrir nada | Capa |
| "Você escolhe quem deve receber, o que vai ser enviado e quando. O BeeFood cuida do resto" — a campanha observa e dispara quando alguém entra na regra; no carrinho abandonado o padrão de fábrica são 15 min | A diferença para a aba Campanhas é **quem marca a hora**: lá é o lojista publicando, aqui é o movimento de quem compra | 2 |
| Variáveis (20, em três grupos) e variações (4 a 9 por campanha), mais a variação automática `{Olá\|Oi}` sorteada no envio | Cada pessoa recebe um texto único, e é isso que separa conversa de disparo em massa | 3 |
| **Anti Banimento**: só envia para quem te mandou mensagem dentro de uma janela; ritmo limitado por dia; o alerta ao desligar descreve banimento definitivo | O medo de perder o número é real e é o que trava o lojista. O produto trata disso como configuração, não como aviso | 4 |
| **Resultado** (jornadas, envios e ROI atribuído pelo Pixel: acessos, sacola, checkout, pedidos, receita) e **Histórico** (mensagem como o cliente recebeu, com "Converteu?") | Marketing sem medida é palpite. Aqui a régua vem junto, e ela segue até o pedido | 5 |
| Está em Food Marketing → Campanhas WhatsApp → Campanhas Inteligentes, incluso; quatro já ativas, e o manual pede para revisar o texto delas | O pedido do fim não é "crie uma campanha": é **revisar as que já falam com o seu cliente** | 6 (CTA) |

**Ficou de fora, de propósito:**

- **o Histórico com cliente identificado.** A tela mostra nome e telefone de um
  cliente real, e este repositório é público. A prova de "cada um recebe um
  texto" fica na variação cadastrada, que mostra a mesma coisa sem expor
  ninguém;
- **os números de receita dos cards.** Quatro das seis marcam `R$ 0,00` na loja
  de teste, e a que tem número fez `R$ 34,02` — ver *o número verdadeiro é
  pequeno* abaixo;
- **`Restaurar padrão`, o limite de 10MB do anexo, o `{{meu_link}}`
  obrigatório e a lista de 20 variáveis uma a uma.** São fatos verdadeiros e
  nenhum deles é motivo para abrir a tela;
- **a concordância errada da interface** ("Nossos campanhas inteligentes",
  "Novo campanha inteligente"). Aparece dentro de print e fica; nenhuma frase
  nossa a repete.

## Slide a slide

| # | Tipo | Ideia única | Imagem |
|---|---|---|---|
| 1 | Capa | Campanhas Inteligentes no seu WhatsApp: seis prontas, quatro ligadas | `fileira-1/2/3.png` |
| 2 | Como funciona | Quem larga a sacola recebe o recado em 15 minutos | `passo-gatilho.png` |
| 3 | A mensagem | O texto chega diferente para cada pessoa | `variacao.png` |
| 4 | Proteção | Só fala com quem já te chamou, e no ritmo que não queima o número | `anti-banimento.png` |
| 5 | Medida | Dá para ver quanto cada campanha trouxe de volta | `card-resultado.png` |
| 6 | CTA | Quatro já estão ligadas: abra e leia o texto delas hoje | `novidades-celular.png` |

O slide da mensagem nasceu com o título "Cada cliente recebe um texto
diferente", e o `conferir-texto.py` acusou: junto com o chapéu, a frase repetia
seis palavras do release.

## O que a revisão do dono mudou (2ª versão)

Três retornos, e os três viraram regra na skill.

### A capa herdou o slide 3, e a peça encurtou

*"Slide 3 é o mais legal, deveria ser o 1."* Era: as seis campanhas com nome,
gatilho e estado são a única imagem que dá o tamanho do recurso de uma vez. A
capa mostrava a mesma tela inteira dentro de um `.notebook`, onde cada nome sai
com 9 px — reconhecível e ilegível.

A prova subiu, o texto da capa foi reescrito em volta dela e o slide das seis
deixou de ter assunto próprio: **7 slides viraram 6**. E a capa **perdeu o
aparelho**, porque a imagem promovida é prova de leitura, e é o mockup que come
a largura de que os nomes precisam.

### O canal faz parte do nome

*"Faltou clareza, são campanhas inteligentes no WhatsApp."* A capa dizia "As
Campanhas Inteligentes já estão trabalhando": nome próprio no título, o que o
recurso faz no subtítulo, e nenhuma das duas linhas explicava **onde** aquilo
acontece — podia ser e-mail, SMS, push. Título novo: **Campanhas Inteligentes
no seu WhatsApp**, com o release inteiro no nome.

### "O cliente" é quem lê

*"'Quem marca a hora de falar é o cliente'. Mas quem tá lendo já é o cliente."*
Nesta peça a palavra tem dois donos: quem abre o post é cliente da BeeFood, e
quem larga a sacola é cliente dele. Sem posse, ela cai no leitor.

O título virou **"Quem larga a sacola recebe o recado em 15 minutos"** — a
pessoa nomeada pela ação, que é como o cartão da tela se chama. A varredura
pegou mais três: "de cliente para cliente" (virou "para cada pessoa"), "as
conversas que o cliente começou" e "o jeito em que o cliente leu" (os dois
ganharam o possessivo).

## Decisões de arte

### O número verdadeiro é pequeno, e o remédio é recortar — não inventar

A loja de teste tem **um** pedido vindo de campanha: `R$ 34,02`, com 1 envio e
1 pedido. É o mesmo problema do Painel para Entregadores — dado real que não
vende —, mas aqui a saída **não** pode ser montar a cena: receita de campanha
inventada é promessa de resultado, e a skill proíbe número que não esteja no
release ou no manual.

Então o recorte é que muda. Os cartões da capa entram cortados logo abaixo do
selo do gatilho, que é onde acaba o que ela afirma — nome, gatilho e estado. E o
número que existe de verdade ficou para o slide 5, que é o único que fala de
resultado.

A tela de **Resultado** entrou na conta e saiu dela: o ROI é medido nos últimos
31 dias, e o único envio da loja de teste é de julho, então hoje aquele modal
está inteiro zerado. O cartão da campanha guarda o acumulado e por isso é ele
que prova a régua.

### A largura da captura foi escolhida pela escala no slide

A grade de campanhas tem três colunas acima de 1500 px e duas abaixo. Capturada
a 1600, a fileira de três cartões reduzida para a largura do slide deixa o nome
da campanha com 9 px — e o nome é o que o leitor vai procurar na tela depois. A
1150 a mesma grade vira duas colunas, e o par sai em escala 1.

A capa, na 2ª versão, é a mesma conta levada ao limite: as fileiras de 934 px de
captura saem em 904 px de slide, escala 0,97. A captura larga (`lista-campanhas.png`,
1600 × 1000 para a tela do `.notebook`) ficou na pasta e fora da arte.

### O quadro dizia 15 minutos, e o campo mostrava 5

No passo 1, o texto do modelo afirma que a campanha "dispara ~15 min após o
abandono" — o padrão de fábrica, lido no código pelo manual — e a loja de teste
tinha ajustado o campo para 5. Juntos na mesma imagem, os dois se desmentem.

O campo foi devolvido ao valor de fábrica **só para a foto**, e a tela fechada
por ESC. Não é montar cena: é desfazer, na imagem, um ajuste local que o manual
já registra como fora do padrão.

### A tela é de computador, e a peça acabou sem aparelho

As Campanhas Inteligentes só existem no desktop (registrado na memória do
manual), e a 1ª versão levava isso para a capa com um `.notebook`. Com a
promoção da prova, o único aparelho da peça é o celular do CTA — e é o
suficiente, porque a arte não precisa dizer em que máquina a tela abre: o
caminho de menu do CTA já diz onde ela fica.

### Nada é salvo durante a captura

O editor não tem auto-save: só grava no **SALVAR (F2)** ou ao confirmar a
ativação. As telas de passo 1, 2 e 3 são abertas, fotografadas e fechadas por
**CANCELAR (ESC)**, e nenhuma chave de campanha é confirmada. O estado
encontrado é o mesmo do manual: quatro ativas, Boas-vindas pausada, Aniversário
em rascunho.
