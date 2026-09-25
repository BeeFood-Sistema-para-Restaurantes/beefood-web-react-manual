# MEMÓRIA — #108 Fechar a entrega no painel

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `gestao-entregas-fechar-entrega.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

Pasta: `manuais/gestao-entregas-fechar-entrega/` · Numeração: **#108** ·
Escrito em 18/09/2026 na sandbox **BeeFood3 - Manual** (`empresaID 38311`,
`filialID 39202`, entregador `194115` simulado por script).

Quarto manual do painel, e o que fecha o ciclo do operador: #106 monta, #107 manda para a rua,
#108 encerra. A rota `A` é a mesma nos três, com os mesmos quatro pedidos.

## O recorte

Duas formas de fechar, e a ordem delas no manual não é cronológica, é pedagógica: **baixa por
parada primeiro** (o uso normal, uma linha por vez) e **finalizar rota depois** (o atalho de
fim de viagem). O contrário ensinaria o atalho antes do hábito.

A quarta seção — *achar o que já foi entregue* — não estava no plano e virou a seção mais útil
do manual. Ela existe porque a rota **desaparece** da tela quando conclui, e essa é a dúvida
que a operação de verdade gera.

## O que a captura descobriu, e o que mudou por causa disso

1. **Não há modal em nenhuma das duas ações.** O script de captura esperava uma janela de
   confirmação no visto da parada: não veio. Depois esperou uma janela no botão de finalizar:
   não veio, e a rota fechou no clique. O prompt do backend confirma que isso é decisão
   (`lovable/08`, seção "o que não fazer"). O manual passou a avisar em destaque, em vez de
   descrever um botão inofensivo.
2. **O botão de finalizar confirma tudo o que está pendente.** O rótulo dele é explícito
   (*"Finalizar rota A confirmando todas as entregas"*) e o efeito é irreversível. Virou o
   aviso mais forte do manual, com o conselho prático: deixe a parada duvidosa para o fim.
3. **A rota concluída não sumiu do sistema — sumiu da tela.** Ela fica por 2 h, mas o painel
   esconde rota sem parada visível, e o selo `entregues` **nasce desligado**. Com o selo
   ligado, a rota reaparece verde, *Concluída*, `4 de 4 entregues · há 56 min`. Duas peças que
   só juntas explicam o desaparecimento — e que só ficaram claras porque a rota foi fechada de
   verdade.
4. **Duas rotas concluídas com a letra `A` na mesma tela.** A foto `05b` prova o
   reaproveitamento de letra que o #106 só afirmava. Rendeu um parágrafo curto no manual, com a
   regra prática: para falar de entrega passada, use o número do pedido.
5. **O mapa se reposiciona na parada seguinte** a cada baixa. Foi visível entre as fotos 02 e
   03 (o mapa saltou para a parada 4, no outro extremo da cidade) e explica por que a tela
   "pula" sem ninguém ter mexido nela.
6. **Dar baixa fora de ordem não move o *Entregando agora***. A promoção só acontece quando
   nenhuma parada está em trânsito. Sem isso, o manual teria prometido algo que a tela não faz.

## Decisões de captura

- **O ciclo foi fechado de verdade**: três baixas pelo visto (#1037, #1038, #1044) e o
  finalizar para a última (#1039). A sandbox terminou o dia com 10 pedidos entregues, e é esse
  dado que o relatório
  [Operação de entrega](../relatorio-operacao-entrega/MEMORIA.md) usa.
- **Quatro scripts em sequência**, e não um só, porque metade das telas deste manual **não dá
  para prever antes de fechar a rota**: só depois do clique no finalizar é que se descobre que
  não havia modal, que a rota sai da lateral e que o selo `entregues` é o interruptor de tudo.
- **O kanban do Delivery** foi capturado com a rolagem horizontal no fim, para a coluna
  *ENTREGUE* caber na foto. A primeira tentativa saiu com o balãozinho de "Abrir Mesas ao
  lado": o mouse parava em `(700, 60)`, que naquela tela é a barra de ferramentas. Nas capturas
  do Delivery o mouse passou a parar em `(700, 850)`.
- Sem foto de "menu da parada": a linha da parada tem três botões (arrastar, confirmar,
  remover) e nenhum menu.

## Scripts

| Arquivo | O que faz |
|---|---|
| `/tmp/ge/cap108.py` | As baixas, a foto antes, a de uma entregue e a de três; remendo do pino do #107 |
| `/tmp/ge/cap108b.py` | O painel depois de fechar e a primeira tentativa do kanban |
| `/tmp/ge/cap108c.py` | O selo `entregues` ligado e o kanban sem balãozinho |
| `/tmp/ge/cap108d.py` | O grupo *Entregues* aberto, com as duas rotas concluídas |
| `/tmp/ge/diag-finalizar.py` | Diagnóstico: o botão de finalizar não abre janela nenhuma |
| `/tmp/ge/diag108.py` | Os rótulos dos botões da linha da parada |

## O que ficou de fora

- **Insucesso / "não entregue"**: não existe no sistema. O manual diz isso como limite, sem
  sugerir contorno.
- **Fechamento financeiro por entregador**: é o
  [Quanto o entregador recebe](../entregador-quanto-recebe/MEMORIA.md) e o relatório Taxa/KM.
- **Baixa pelo aplicativo do entregador** (inclusive por código de barras): é do bloco do app,
  no #114. Este manual é só o painel.
