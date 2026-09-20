# Campanhas Inteligentes no WhatsApp

- **Gênero:** novidade
- **Fonte:** [Campanhas Inteligentes no WhatsApp](https://beefood.app/novidades/whatsapp-campanhas-inteligentes)
  — 28/07/2026, área Marketing
- **Manual:** [Campanhas Inteligentes](https://ajuda.beefood.com.br/campanhas-inteligentes-whatsapp)
  — na pasta, [`manuais/campanhas-inteligentes/`](../../manuais/campanhas-inteligentes/campanhas-inteligentes.md)
- **Formato:** 1080 × 1350 (4:5)
- **Slides:** 7

## O acervo, antes de escrever

As oito peças entregues falam de **cardápio, totem, tablet, dark kitchen e
entrega** — o pedido chegando e o pedido saindo. Nenhuma fala de **marketing**,
e não há em `imagens-puras/` nenhuma tela de Food Marketing, de WhatsApp ou de
segmentação. É a primeira peça deste módulo, e não há prova para reusar.

Do acervo vem método: a captura da página de novidades no celular para o CTA
(convenção da casa desde a peça 1) e o recorte por caixa medida no DOM, do
tablet e do painel do entregador.

**A capa não repete a forma da anterior.** O Painel para Entregadores usou o
*anúncio de chegada* ("Chegou o…"). Aqui o molde é **afirmação do fato**, com o
nome dentro da frase — e o fato é o mais forte que esta novidade tem: as
campanhas **já estão ligadas** na conta de quem lê. Placar dos moldes depois
desta peça: pergunta 2, afirmação 2, nome do recurso 1, anúncio de chegada 1,
ordem direta 0, antes × agora 0.

## O fato, o ângulo, e o que o slide diz

O manual foi escrito lendo o código-fonte (`modelos.js`), então os fatos de
configuração abaixo são mais duros que o release.

| Fato (release / manual) | Ângulo | O que vira slide |
|---|---|---|
| O recurso se chama **Campanhas Inteligentes** e é a terceira aba de Food Marketing → Campanhas WhatsApp. A conta já vem com **seis**, e **quatro nascem ligadas** | A novidade não é mais uma tela para configurar: ela **já está trabalhando**, e isso é notícia antes de ser argumento | Capa |
| "Você escolhe quem deve receber, o que vai ser enviado e quando. O BeeFood cuida do resto" — a campanha observa e dispara quando o cliente entra na regra | A diferença para a aba Campanhas é **quem escolhe o momento**: lá é você publicando, aqui é o cliente agindo | 2 |
| As seis: carrinho abandonado, recebeu o cardápio e não pediu, recuperador de vendas, cashback parado, aniversário, boas-vindas / 2ª compra. Cada uma com gatilho, horário e ritmo de fábrica | Cada campanha pega **um momento** em que o cliente já demonstrou interesse — não é lista de promoção para todo mundo | 3 |
| Variáveis (20, em três grupos) e variações (4 a 9 por campanha), mais a variação automática `{Olá\|Oi}` sorteada no envio | Cada cliente recebe um texto único, e é isso que separa conversa de disparo em massa | 4 |
| **Anti Banimento**: só envia para quem te mandou mensagem dentro de uma janela; ritmo limitado por dia; o alerta ao desligar descreve banimento definitivo | O medo de perder o número é real e é o que trava o lojista. O produto trata disso como configuração, não como aviso | 5 |
| **Resultado** (jornadas, envios e ROI atribuído pelo Pixel: acessos, sacola, checkout, pedidos, receita) e **Histórico** (mensagem como o cliente recebeu, com "Converteu?") | Marketing sem medida é palpite. Aqui a régua vem junto, e ela segue até o pedido | 6 |
| Está em Food Marketing → Campanhas WhatsApp → Campanhas Inteligentes, incluso; quatro já ativas, e o manual pede para revisar o texto delas | O pedido do fim não é "crie uma campanha": é **revisar as que já falam com o seu cliente** | 7 (CTA) |

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
| 1 | Capa | As Campanhas Inteligentes já estão trabalhando: seis prontas, quatro ligadas | `lista-campanhas.png` num notebook |
| 2 | Como funciona | Quem marca a hora de falar é o cliente, não o seu calendário | `passo-gatilho.png` |
| 3 | As seis | Cada campanha pega um momento em que o cliente já demonstrou interesse | `fileira-1/2/3.png` |
| 4 | A mensagem | O texto muda de cliente para cliente | `variacao.png` |
| 5 | Proteção | Só fala com quem já te chamou, e no ritmo que não queima o número | `anti-banimento.png` |
| 6 | Medida | Dá para ver quanto cada campanha trouxe de volta | `card-resultado.png` |
| 7 | CTA | Quatro já estão ligadas: abra e leia o texto delas hoje | `novidades-celular.png` |

O slide 4 nasceu com o título "Cada cliente recebe um texto diferente", e o
`conferir-texto.py` acusou: junto com o chapéu, a frase repetia seis palavras
do release. Virou "O texto muda de cliente para cliente".

## Decisões de arte

### O número verdadeiro é pequeno, e o remédio é recortar — não inventar

A loja de teste tem **um** pedido vindo de campanha: `R$ 34,02`, com 1 envio e
1 pedido. É o mesmo problema do Painel para Entregadores — dado real que não
vende —, mas aqui a saída **não** pode ser montar a cena: receita de campanha
inventada é promessa de resultado, e a skill proíbe número que não esteja no
release ou no manual.

Então o recorte é que muda. Os cartões do slide 3 entram cortados logo abaixo
do selo do gatilho, que é onde acaba o que aquele slide afirma — nome, gatilho
e estado. E o número que existe de verdade ficou para o slide 6, que é o único
que fala de resultado.

A tela de **Resultado** entrou na conta e saiu dela: o ROI é medido nos últimos
31 dias, e o único envio da loja de teste é de julho, então hoje aquele modal
está inteiro zerado. O cartão da campanha guarda o acumulado e por isso é ele
que prova a régua.

### A largura da captura foi escolhida pela escala no slide

A grade de campanhas tem três colunas acima de 1500 px e duas abaixo. Capturada
a 1600, a fileira de três cartões reduzida para a largura do slide deixa o nome
da campanha com 9 px — e o nome é o que o leitor vai procurar na tela depois. A
1150 a mesma grade vira duas colunas, e o par sai em escala 1.

A capa segue a mesma conta pelo outro lado: 1600 × 1000 é 16/10, a proporção
exata da tela do `.notebook`, então a moldura não corta faixa nenhuma.

### O quadro dizia 15 minutos, e o campo mostrava 5

No passo 1, o texto do modelo afirma que a campanha "dispara ~15 min após o
abandono" — o padrão de fábrica, lido no código pelo manual — e a loja de teste
tinha ajustado o campo para 5. Juntos na mesma imagem, os dois se desmentem.

O campo foi devolvido ao valor de fábrica **só para a foto**, e a tela fechada
por ESC. Não é montar cena: é desfazer, na imagem, um ajuste local que o manual
já registra como fora do padrão.

### A tela é de computador, e o aparelho é o notebook

As Campanhas Inteligentes só existem no desktop (registrado na memória do
manual). Notebook, e não janela de navegador: na capa o que se vende é alguém
sentado configurando uma vez — a cena — e não a página.

### Nada é salvo durante a captura

O editor não tem auto-save: só grava no **SALVAR (F2)** ou ao confirmar a
ativação. As telas de passo 1, 2 e 3 são abertas, fotografadas e fechadas por
**CANCELAR (ESC)**, e nenhuma chave de campanha é confirmada. O estado
encontrado é o mesmo do manual: quatro ativas, Boas-vindas pausada, Aniversário
em rascunho.
