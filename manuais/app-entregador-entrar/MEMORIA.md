# MEMÓRIA — #111 App do entregador: instalar, entrar e ficar disponível

## O recorte

Três capítulos do material do dono viraram **um** manual: 01 primeiros passos, 02 disponibilidade
e 15 ajustes e sair. Não é economia de página — é o recorte por pergunta. Quem abre o aplicativo
pela primeira vez faz uma pergunta só: *como eu começo a trabalhar com isto?* Permissão, login,
pílula e sair são as quatro partes da mesma resposta, e separá-las obrigaria o motoboy a abrir
três páginas para completar o primeiro turno.

A conta de imagens confirmou: 15 prints no material, **13 no manual**. Saíram duas — o login
preenchido com a senha oculta (a tela vazia e a senha revelada já contam a história) e a pílula
em pausa/offline em tela cheia, que viraram um recorte só, lado a lado.

## A técnica de anotar print de celular

Herdada do #114, que foi o primeiro. Duas coisas novas apareceram aqui:

- **`rec(caixa)`**, na cabeça do `annotate.py`. No #114 eu convertia à mão de pixel para fração
  depois de cada recorte, e qualquer ajuste de recorte invalidava as medições. Agora eu meço
  **uma vez** na prévia de 473x1024 (a proporção exata de 1440x3120) e o `rec()` recebe o mesmo
  recorte passado ao `copiar()`. Trocar o recorte não pede remedição nenhuma — e eu troquei
  quatro, nesta rodada, porque a barra de status vazava.
- **Margem em cima, não só à esquerda.** A tela de trabalho tem três coisas na mesma linha do
  cabeçalho (menu, título e pílula) e a faixa da senha tem duas (o texto e o olho). Com etiqueta
  só na margem esquerda, duas delas cairiam uma sobre a outra. Faixa clara em cima resolve, e as
  etiquetas apontam para baixo.

### A armadilha das setas

Na primeira rodada, **oito das vinte e nove setas paravam sobre o texto do alvo** — a ponta caía
na primeira letra de *Online*, de *Usuário*, de *Localização*. Fica legível, mas fica feio, e a
correção é sempre a mesma: mirar na **borda esquerda do elemento**, não no rótulo. Vale para
botão, cartão e caixinha. Anotado aqui porque vai se repetir nos outros quatro manuais do app.

## O que eu esperava e não era assim

| Eu esperava | O que é |
|---|---|
| A pílula de disponibilidade **filtrar** o despacho | Ela só informa. Nada no servidor impede despachar para quem está OFFLINE — a própria folha admite isso em letra cinza |
| Ficar offline encerrar a entrega que já está na mão | As entregas continuam do entregador até ele finalizar ou o restaurante passar para outro |
| Sair e ficar offline serem parecidos | Sair **também** marca presença offline, desativa push, para o GPS e limpa cache. É um superconjunto |
| A sessão expirar sozinha | Não expira. Só o SAIR, a recusa do servidor na tela de carga, ou limpar dados no Android |
| As permissões serem pedidas depois do login | Três vêm **antes** do formulário; só a de notificações vem depois |

O primeiro item é o que mais mudou o texto. Ele virou seção com nome próprio (*O que a
disponibilidade faz — e o que ela não faz*) e citação literal da frase da tela. Entregador que
entende a pílula como tranca vai brigar com o restaurante pelo pedido que chegou depois do
"acabei" — e quem está errado, aí, é o manual que deixou isso implícito.

## Decisões de imagem

- **As três pílulas juntas (`10`) não têm etiqueta numerada.** É comparação de cor: número em
  cima cobriria a própria pílula, que é o assunto. A legenda dá conta.
- **O selo *Ativa* da tela de permissões ficou fora das setas.** Ele vive na mesma linha do nome
  da permissão, e a seta atravessaria o cartão inteiro na diagonal. Foi para o parágrafo.
- **O login preenchido com senha oculta não entrou.** Entre ele e a senha revelada, a segunda
  ensina mais — e a primeira é a tela do login vazio com texto.
- **A senha da conta de teste aparece legível** na imagem da senha revelada. É sandbox, e a regra
  do repositório permite; o `texto-documentation.ia.md` só pede para não usar o valor como
  exemplo no texto publicado.

## O que falta

Nada para este manual. Das 12 capturas pedidas em
[`../gestao-entregas/pedidos/capturas-app.md`](../gestao-entregas/pedidos/capturas-app.md), duas
tocam este assunto de raspão e ficariam boas aqui se chegarem:

| Captura pedida | Onde entraria |
|---|---|
| Permissão de localização **recusada** (a tela de Permissões com *Inativa*) | seção 5, ao lado da tela com as quatro Ativas |
| A pílula com o ícone de nuvem cortada (sem confirmação do servidor) | a pergunta *A pílula não fica ONLINE* |

Nenhuma das duas impede publicar: o texto já descreve os dois casos.
