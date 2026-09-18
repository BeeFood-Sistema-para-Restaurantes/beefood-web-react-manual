# MEMÓRIA — #107 Despachar e acompanhar

Pasta: `manuais/gestao-entregas-despachar/` · Numeração: **#107** ·
Escrito em 18/09/2026 na sandbox **BeeFood3 - Manual** (`empresaID 38311`,
`filialID 39202`, entregador `194115` simulado por script).

Terceiro manual do painel. Continua **a mesma rota `A`** do
[#106](../gestao-entregas-montar-rota/MEMORIA.md), com os mesmos quatro pedidos (#1037,
#1038, #1044, #1039), de propósito: os dois manuais são lidos em sequência e o leitor
reconhece os pedidos de uma página para a outra.

## O recorte

O plano dizia que este é "o manual mais delicado do bloco", e a redação seguiu essa leitura:
**a seção de aviso vem antes das instruções**. Não é estilo — é que o clique de despachar
dispara WhatsApp para o cliente, baixa no marketplace e impressão, e nada disso tem desfazer.
Um manual que explicasse o botão primeiro e avisasse depois ensinaria a apertar antes de ler.

## O que mudou o texto depois de ler o backend

1. **Despachar é a única operação de roteirização que mexe no ERP.** Isso desenha a fronteira
   com o #106: lá nada sai da tela, aqui tudo sai.
2. **O alcance é a rota inteira.** Não existe despachar meia rota, então o manual não oferece
   a ideia.
3. **O servidor não confere se os pedidos estão prontos** — a checagem é aviso de tela. Virou
   a frase "o sistema avisa e obedece".
4. **Despachar duas vezes é no-op.** Entrou nas dicas, porque é a defesa contra clique duplo e
   o operador não tem como saber disso olhando a tela.
5. **Trocar entregador não notifica ninguém** (push é Fase 8, não existe). O manual manda
   ligar para os dois entregadores; sem isso o motoboy só descobre reabrindo a lista.
6. **Excluir rota despachada é permitido de propósito** e **não desfaz o aviso já enviado**.
   As duas metades foram escritas juntas, porque só a primeira seria um convite ao engano.

## O que a tela mostrou e o backend não contava

- Depois do despacho o **avião vira o botão de finalizar** no mesmo lugar do cabeçalho. Quem
  decorou a posição do avião aperta o finalizar sem perceber — está na seta 3 da foto 03.
- O rótulo do botão de finalizar é explícito: *"Finalizar rota A confirmando todas as
  entregas"*. Isso é do #108, mas foi medido aqui.
- O menu de três pontos da rota na rua tem **três** itens (trocar, remover, excluir). O
  *Adicionar N selecionados* só aparece com pedido marcado.
- O chip de situação passa a dizer **Na rua** — não *Em rota*, que é o rótulo do rodapé de
  entregadores e dos selos do topo. Dois nomes para o mesmo estado, e o manual usa os dois
  como a tela usa.
- A janela de troca de entregador se chama **"Entregador da rota A"**, não "Trocar
  entregador" (que é o nome do item de menu).

## Decisões de captura

- **Sete capturas, nenhuma encenada.** O despacho foi real: a rota saiu, o pedido mudou de
  situação no Delivery e os pinos mudaram de cor. É por isso que o #108 pôde começar da tela
  que este manual deixou.
- **O entregador andou de verdade** entre as fotos 03 e 04, com
  `cenario.js andar --entregador 194115 --para -23.4990,-47.4460 --passos 4`, chamado por
  `subprocess` de dentro do script de captura — para o movimento cair no meio da sessão do
  navegador e não antes dela.
- **Duas remendadas de geometria** foram necessárias, e as duas pela mesma razão: alvos que
  **mudam de identidade depois do despacho**. O chip vira *Na rua* (o seletor procurava *Em
  rota*) e o avião deixa de existir. `fix107.py` e `fix107b.py` remedem os `*.geo.json` de 03,
  04 e 06 e recapturam a foto 07 com a lista de alvos certa.
- **O pino do entregador no mapa não é o primeiro `.leaflet-marker-icon`** — esse é o pino do
  pedido `A1`. A seta 1 da foto 04 apontou para o alvo errado na primeira rodada, e o
  `cap108.py` (passo 0) mediu o marcador certo e corrigiu o JSON.
- As etiquetas do painel caem sempre em `x=1300`, sobre o mapa: a lateral tem texto em todas
  as linhas e número em cima dela taparia endereço.

## Scripts

| Arquivo | O que faz |
|---|---|
| `/tmp/ge/cap107.py` | As sete capturas, com geometria |
| `/tmp/ge/fix107.py` | Remedo do chip *Na rua* e dos alvos derivados do cabeçalho |
| `/tmp/ge/fix107b.py` | Botão de finalizar nos JSON de 03/04/06 e recaptura da foto 07 |
| `manuais/gestao-entregas/scripts/cenario.js` | Cenário: pedidos, presença e movimento do entregador |

## O que ficou de fora

- **Despacho automático** tem manual próprio (#109). Aqui só se diz que o selo do topo mostra
  se ele está ligado.
- **Impressão do cupom de entrega** é citada como consequência, sem foto: a impressora da
  sandbox não existe, e o cupom com código de barras já está no
  [#104](../gestao-entregas-liberar-entregador/gestao-entregas-liberar-entregador.md).
- **A mensagem de WhatsApp** que o cliente recebe é assunto do #110.
