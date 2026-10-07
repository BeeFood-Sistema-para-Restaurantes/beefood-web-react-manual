# MEMÓRIA — #126 Programa de pontos

Status: **concluído** em 07/10/2026. Pasta `manuais/programa-pontos/`, **17 imagens**, 76 setas.
O estudo do código está em [`fluxo-codigo.md`](fluxo-codigo.md).

## Pedido do dono

> *"nova funcionaldiade programa de pontos. disponivel em sistema beefood, cardapio digital, totem
> de autoatendimento e cardapio digital tablet. no manual vamos focar em mostrar somente no
> cardapio digital mas dizer dos outros tbm. faça git pull em tudo, estude como ficaria nosso
> manual, me traga noticias e eu aprovo em seguida"*

E, depois do estudo: *"seguir"*.

## O recorte, e por que ele ficou assim

O pedido manda mostrar **só o cardápio digital**. Mas o programa **não se liga pelo cardápio**: o
único lugar onde ele existe como configuração é a aba **Fidelidade (CRM) → Programa de pontos** do
painel. Então o manual tem duas metades e uma ordem que o pedido não dizia:

1. **Configuração no painel** (seções 1 a 5) — porque sem ela não há nada para fotografar no
   cardápio.
2. **O cardápio digital** (seções 6 a 8) — o que o pedido pediu, com as sete telas do cliente.
3. **Acompanhamento no painel** (seções 9 a 11) — histórico, saldo, extrato, crédito manual e
   migração, que é o dia a dia de quem atende.
4. **Os outros três canais** (seção 12) — **só texto**, numa tabela de canal por canal.

Totem e cardápio digital tablet não ganharam imagem **porque não há tela de pontos para
fotografar**: o bundle do totem não tem uma única menção a "pontos", e as três aparições do
recurso no cardápio dependem de `!isPresencial`, que é exatamente o que o totem é. O tablet é APK
Android, que não roda neste ambiente. Dizer isso em tabela é mais honesto que um print de tela sem
o recurso.

## Os três defeitos que o manual encontrou

Estão medidos no [`fluxo-codigo.md`](fluxo-codigo.md), com a evidência de cada um. Resumo, porque
são o achado do manual:

1. **Recompensa de produto cadastrada pelo painel não aparece para o cliente.** O painel grava o
   `produtoID` do cardápio interno (faixa 2624xxx); o cardápio público resolve pelo id do catálogo
   (2515xxx), e descarta em silêncio o que não encontra. A recompensa que o painel exibe como
   `Produto #2515303` é a que o cliente vê; a que ele exibe com nome (`CHICKEN DELUXE`) é a que o
   cliente **não** vê. As duas anomalias são o mesmo bug, vistas de lados opostos.
2. **A hora do painel está três horas à frente** da hora do cardápio para o mesmo lançamento
   (`15:23` contra `12:23`): o painel mostra UTC sem converter.
3. **No extrato do cliente, o ícone de ganho é vermelho e o de uso é verde** — invertidos em
   relação ao painel.

O manual não esconde nenhum: o 1 virou aviso em destaque na seção 5 ("confira no cardápio depois de
cadastrar") com o sintoma descrito, e o 2 e o 3 viraram linha de FAQ. O
[`texto-documentation.ia.md`](texto-documentation.ia.md) registra que **o aviso da seção 5 sai da
página** quando o produto corrigir o id.

## O achado de produto que mudou o texto

**O que se digita em *Motivo* aparece inteiro para o cliente.** O campo é obrigatório no
ADICIONAR/REMOVER/TRANSFERIR e parecia ser nota interna; ele é renderizado na terceira linha de
cada lançamento da janela *Meus pontos*, no celular. O crédito de teste deste manual saiu como
*"Ajuste manual: Credito de teste para as capturas do manual"* na tela do cliente — e é por isso
que a frase está nas capturas 08 e 15, que viraram a prova do aviso.

Outros dois que o texto aproveitou:

- **Cashback e pontos são exclusivos por cardápio.** O diálogo do
  `ConfirmarExclusividadeFidelidade` é montado por template, então o manual pôde citar o texto e o
  rótulo do botão (`ATIVAR E DESATIVAR O CASHBACK`) palavra por palavra.
- **"Entrega grátis com pontos" não dá entrega grátis.** O subtítulo do próprio cartão diz o que
  ele faz: *"O cliente acumula pontos também sobre a taxa de entrega."* Frete grátis por pontos se
  faz com uma **recompensa de desconto** no valor da taxa. O manual explica a diferença em vez de
  corrigir o nome, porque o leitor vai procurar pelo rótulo que está na tela dele.

## Cenário montado na sandbox

O `cenario.py` desta pasta monta o que a tela não sabe criar. Ele é **ensaio por padrão**
(`VALENDO=1` para valer) e tem três comandos:

| Comando | O que faz |
|---|---|
| `estado` | lê e imprime a configuração, as recompensas e o saldo do cliente de teste — sem escrever nada |
| `pontos` | credita no cliente de teste a diferença até `ALVO_PONTOS` (121), pelo próprio ADICIONAR da tela. **Idempotente**: rodar de novo não credita nada |
| `recompensa` | cadastra a recompensa de produto, pelo seletor da tela |

Nada foi escrito direto no banco: as duas escritas passam pelo formulário do sistema, que é o
caminho que o lojista usa. O estado em que a sandbox ficou:

- programa **ativo**, 1 ponto por R$ 1,00, validade 90 dias, bônus de boas-vindas 50, acúmulo sobre
  a taxa de entrega ligado (1 ponto por R$ 1,00 de taxa), **as seis modalidades ligadas**;
- **3 recompensas de desconto** (R$ 5,00/50, R$ 10,00/100 e R$ 20,00/180) e **2 de produto**
  (uma de 100 pontos, que o cliente vê, e a de 80 que cadastramos e ele não vê — ela ficou de
  propósito, é a evidência do defeito 1);
- cliente **Teste Manual** `(15) 99999-8888` com **121 pontos**;
- fila com 3 vendas (1 pendente, 2 com sucesso).

**Nenhum pedido foi fechado.** O resgate das capturas 10 e 11 foi feito na sacola e abandonado ali,
então ele não consumiu ponto — o saldo continua 121. É a técnica do ensaio aplicada ao cardápio:
tudo até o clique final.

## Capturas

Duas resoluções, as duas do padrão da casa:

| Script | O que captura | Tamanho |
|---|---|---|
| `capturar-painel.py` | as 5 telas de configuração e as 5 de acompanhamento | painel 1440x900 em DPR 1,5 → 2160x1350, e recortes de cartão |
| `capturar-cardapio.py` | as 6 telas do celular e 1 do computador | celular 390x844 em DPR 2 → 780x1688; computador em DPR 1,5 |

Os dois são **somente leitura** — nenhum deles escreve, e o do cardápio para antes de fechar o
pedido. Rodar de novo refaz as 17 puras.

### Três armadilhas de captura que valem para o próximo

- **As abas do Programa de pontos não são `role="tab"`.** São botões comuns; `get_by_role("button",
  name=...)` resolve, e `[role="tab"]` só dá timeout.
- **A página não rola — o conteúdo rola.** `full_page=True` devolveu 900 px de uma tela de 2000. A
  coluna da aba Configuração é um `div.flex-1.overflow-y-auto.min-h-0`, e é o `scrollTop` **dele**
  que precisa andar. Para medir as duas caixas de um recorte de dois cartões, role **uma vez** e
  meça as duas no **mesmo quadro**: medir, rolar e medir de novo mistura dois quadros e corta o
  primeiro cartão.
- **O rodapé do cardápio não navega por texto.** Os quatro itens (`Cardápio`, `Promoções`,
  `Pedidos`, `Perfil`) só respondem em `.v-bottom-navigation .v-btn`. E **Perfil** deslogado abre
  o login e depois volta para a home: é preciso tocar em **Perfil** de novo.

### Cobrir telefone na pura, não na tratada

O repositório é público, então as duas telas do painel que listam clientes (14 e 15) saem com os
telefones borrados **já na pura**. O borrão é feito no navegador, antes do print, e tem uma regra
que não é óbvia:

```js
// só o mais interno de cada cadeia: borrar o ancestral apagaria a linha inteira
candidatos.forEach((e) => {
  if (candidatos.some((o) => o !== e && e.contains(o))) return;
  e.style.filter = 'blur(5px)';
});
```

A primeira versão pulava qualquer elemento com filho e não achava nada, porque o telefone mora num
`span` ao lado de um `svg`. O script imprime quantos borrou (1 nas imagens 14 e 15, 0 nas outras),
e esse número é a conferência.

O telefone do **cliente de teste** fica à vista de propósito: é o número da sandbox, já publicado
na `MEMORIA-GERAL.md`, e é ele que o leitor vai usar para testar.

## Anotação

As coordenadas foram medidas na **grade de frações** sobreposta a cada pura (gerada em `/tmp`, fora
do repositório). Três coisas novas em relação ao #125:

- **O `annotate()` ganhou margem em cima (`topo`)**, e não só nos lados. As duas telas de tabela
  (13 e 14) têm o cabeçalho das colunas **abaixo** da linha da busca: seta vinda de faixa lateral
  atravessa a busca inteira. Com faixa em cima, a seta desce direto na coluna.
- **Os seis prints de celular usam as mesmas duas margens** (0,22 e 0,10), mesmo quando uma sobra.
  Largura final igual nos seis; imagem publicada em sequência com largura diferente fica torta.
- **Botão e selo se miram pela borda de fora.** As primeiras versões das imagens 09, 10 e 11 saíram
  com a seta atravessando `RESGATAR`, `INSUFICIENTE`, `ADICIONAR`, `REMOVER` e `Disponível` por
  cima do rótulo, porque a etiqueta está à direita e o alvo era a borda **esquerda**. Mirando a
  borda direita, a seta encosta e não cobre nada. É a mesma lição do #27, aplicada a elemento que
  vive encostado na margem.

A margem continua montada **em memória**, dentro do `annotate()`: rodar o script duas vezes dá as
17 tratadas byte a byte iguais — conferido depois da renumeração, com `git diff` vazio em
`imagens-tratadas/`.

**A ordem dos arquivos é a ordem do texto.** As puras foram capturadas na ordem do painel
(configuração, acompanhamento, cardápio) e **renumeradas** depois que a estrutura do manual ficou
decidida, para que `06` a `12` sejam o cardápio digital e `13` a `17` o acompanhamento. É convenção
da casa desde o #116, e vale o `git mv`.

## Ambiente: o que foi alterado

Três escritas, todas pelo formulário do sistema, todas na sandbox:

1. **121 pontos** creditados no cliente de teste, com motivo
   *"Ajuste manual: Credito de teste para as capturas do manual"*.
2. **1 recompensa de produto** cadastrada (CHICKEN DELUXE por 80 pontos) — a que comprovou o
   defeito 1, e que fica.
3. Nada mais. A configuração já estava como está, nenhum pedido foi fechado, nenhuma migração de
   programa foi executada (as duas zeram saldo de todos os clientes e são irreversíveis).
