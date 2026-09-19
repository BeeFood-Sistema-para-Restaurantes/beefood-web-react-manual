# Capturas do app, segunda lista — 6 prints, em 3 pastas

Para o dono, depois de fechar o bloco da Gestão de Entregas 2.0 com as 24 capturas da rodada
anterior ([`capturas-app.md`](capturas-app.md), respondida em 19/09/2026).

> **Nada aqui bloqueia manual nenhum.** Os dezesseis manuais do bloco estão publicáveis hoje, e o
> `## O que falta` de cada um diz *nada*. Esta lista é de **qualidade**: seis telas que hoje o texto
> descreve por escrito, e uma delas substitui a **única imagem composta** de todo o bloco.
>
> Se não vierem, nada se perde. Se vierem, o #114 deixa de ter imagem montada e o #112 ganha as duas
> telas que hoje são só frase.

## O que muda de verdade

| | Prints | Efeito |
|---|--:|---|
| **Troca imagem composta por imagem real** | 4 | o #114 é o único manual do bloco com uma imagem **sobreposta** — o emulador não tem câmera, e a etiqueta dentro da faixa foi montada. As outras três nunca foram fotografadas: as faixas de resultado da leitura |
| **Fecha duas frases sem tela** | 2 | o histórico realmente vazio (o print da rodada passada veio com 22 entregas) e o aplicativo abrindo **sem rede** |

Se der tempo para uma coisa só, faça a pasta **26** — ela é a que tira uma imagem montada de um
manual publicado.

## Antes de tudo: duas travas que valem para as seis

**1. Ler a etiqueta DESPACHA o pedido de verdade.** Não é conferência. A leitura chama a mesma rota
que o botão de despachar do painel (`POST tentrega/lerCodigoBarras` → `SituacaoDeliveryUpdater` com
`'ENTREGA'`), e isso avisa o cliente por WhatsApp e registra a saída no marketplace.

Então: **só bipe etiqueta de pedido semeado pelo script**, nunca de pedido que apareceu na fila por
outro caminho. Os pedidos do `preparar --caso lista` são de clientes sintéticos, **sem telefone e sem
e-mail** (conferido na base antes de versionar o material da primeira rodada), e não são de
plataforma. Neles a leitura não dispara WhatsApp para ninguém nem avisa marketplace nenhum.

**2. O histórico do aplicativo não é o lote da execução.** Ele lê **tudo** o que o entregador já
entregou. É o que fez a foto do histórico vazio voltar errada na rodada passada. O comando para isso
é novo e está explicado na pasta 27.

## Os scripts, e o que mudou neles

```
manuais/gestao-entregas/scripts/smoke-app.js
```

Mesmos comandos da rodada anterior, mais dois:

```powershell
node smoke-app.js casos                     # a lista, com a foto de cada caso
node smoke-app.js preparar --caso lista      # monta e confere
node smoke-app.js conferir                   # confere de novo, quantas vezes quiser
node smoke-app.js limpar                     # tira tudo da tela do app

node smoke-app.js historico-zerar            # NOVO: tira TUDO do Histórico, e guarda o desfazer
node smoke-app.js historico-voltar           # NOVO: devolve exatamente o que o zerar tirou
```

Os dois novos foram exercitados de ponta a ponta antes de virar pedido: zeraram as 8 entregas
concluídas do entregador de teste, a trava recusou um segundo `zerar` sobre um desfazer pendente, e o
`voltar` devolveu as 8 com as datas originais intactas. O desfazer mora em
`.smoke-app-historico.json`, ao lado do script, e é apagado só quando a conta fecha.

---

## 26. A leitura de código de barras de verdade (4)

| Arquivo | A cena | Onde entra |
|---|---|---|
| `26-codigo-de-barras/prints/01-codigo-na-faixa.png` | a etiqueta EAN-13 **de papel** dentro da faixa da câmera | #114, seção 4 — **substitui** a imagem composta |
| `26-codigo-de-barras/prints/02-lido-com-sucesso.png` | a faixa verde **Pedido lido com sucesso!** | #114, a tabela das cinco faixas |
| `26-codigo-de-barras/prints/03-faixa-vermelha.png` | a faixa vermelha de erro no envio | #114, e o FAQ *Bipo e a faixa fica vermelha* |
| `26-codigo-de-barras/prints/04-pedido-ja-lido.png` | **Pedido já lido.** — a mesma etiqueta bipada duas vezes | #114, a mesma tabela |

**Por que esta pasta é a que mais importa.** O #114 descreve cinco faixas de status numa tabela e não
mostra nenhuma. E a imagem que ele mostra da leitura — `06-codigo-na-faixa.png` — é a única imagem
**composta** do bloco inteiro: o emulador vê uma sala virtual, e a etiqueta foi sobreposta ali pelo
`compor-leitura.ps1`. Está declarado no `fluxo-codigo.md` do manual, o que é honesto, mas imagem real
é melhor que imagem declarada.

### Como montar a cena

1. `node smoke-app.js preparar --caso lista` — quatro pedidos abertos, clientes sintéticos.
2. `node smoke-app.js estado` e anote o `preVendaID` de um pedido em **PREPARO** ou **PRONTO**.
   Pedido já em `ENTREGA` responderia *Pedido já lido* na primeira tentativa.
3. Gere a etiqueta desse pedido com o gerador que já veio no kit:
   `3-referencia/material-original/smoketests/codigo-de-barras/gerar-ean13.js`. Ele monta o EAN-13 a
   partir do `preVendaID` — **os 12 primeiros dígitos são o identificador do pedido** e o 13º é o
   verificador. Rodei aqui para conferir: `node gerar-ean13.js 59588083` sai com o código
   `0000595880834`, num PNG de 840x340, e o comentário do próprio script diz que o módulo é largo
   **porque a imagem vai ser lida pela câmera do emulador** — quem o escreveu já tinha esse caminho
   em mente.
4. Ponha a etiqueta na frente da câmera. **Duas formas, escolha a que der:**
   - **Aparelho físico** com a etiqueta impressa em papel. É a melhor: é o gesto do entregador.
   - **Emulador, com a etiqueta na cena virtual.** O emulador Android aceita trocar o pôster da
     parede da `virtualscene` por um PNG seu (na pasta de recursos do emulador, o arquivo
     `Toren1BD.posters`, com um bloco `poster custom` apontando para o PNG). Aí a leitura é **real**
     — a câmera enxerga o código, não há sobreposição. **Não conferi isso daqui**, só a geração do
     código; se não funcionar em duas tentativas, anote no relatório e siga: a imagem composta que o
     manual tem hoje continua servindo, e está declarada como composta.
5. No app: aba **Código barras** no rodapé, e aproxime. A leitura é automática, sem tocar em nada.

### As três faixas

| Foto | Como produzir |
|---|---|
| `02-lido-com-sucesso` | a leitura acima, com rede ligada. A faixa fica **verde** e o pedido vai para *ENTREGA* |
| `04-pedido-ja-lido` | **sem sair da tela do leitor**, aproxime a mesma etiqueta de novo. O app bloqueia a releitura na mesma sessão e a faixa diz *Pedido já lido.* — nada é enviado |
| `03-faixa-vermelha` | abra o leitor **com rede**, depois desligue (`adb shell svc wifi disable` e `svc data disable`) e só então aproxime a etiqueta de **outro** pedido. A leitura acontece no celular e o envio falha: é exatamente o caso do FAQ |

A ordem importa: faça `02` e `04` primeiro, com rede, e `03` no fim — é a que precisa da rede
desligada, e ela deixa o pedido **sem** despachar, que é o que o FAQ afirma.

> **Se a faixa vermelha não sair na primeira tentativa, siga.** O aplicativo tem 20 s de timeout
> nesta chamada, e em rede caindo devagar ele pode demorar a desistir. Desligar wifi **e** dados
> antes de aproximar resolve na maioria das vezes.

---

## 27. O histórico realmente vazio (1)

| Arquivo | A cena | Onde entra |
|---|---|---|
| `27-historico-vazio/prints/01-historico-vazio.png` | **Nenhuma entrega no período** + *As entregas que você concluir aparecem aqui.* | #112, a pergunta *O histórico está vazio*; e o #111 |

Este foi pedido na rodada passada e voltou como outra coisa: a tela veio com **22 entregas em três
dias**. Não foi erro de quem fotografou — foi erro do pedido. O caso `historico-vazio` desatribui os
pedidos **do lote da execução**, e o Histórico do aplicativo lê tudo o que aquele entregador já
entregou, de qualquer dia. Sobrou o que estava lá de antes.

O aplicativo **não tem filtro de data** nessa tela (ele manda a data de hoje nos dois campos do
período e o servidor devolve mais do que isso), então não há como chegar a *Nenhuma entrega no
período* pela tela. A única forma é o entregador não ter entrega concluída nenhuma — e é para isso que
os dois comandos novos existem.

```powershell
node smoke-app.js limpar               # a aba Entregas vazia
node smoke-app.js historico-zerar      # o Histórico vazio, com o desfazer guardado
#   --> abra a aba Histórico e tire a foto
node smoke-app.js historico-voltar     # devolve tudo, com as datas originais
```

**O `historico-voltar` é obrigatório, e logo depois da foto.** Enquanto o histórico está zerado, as
entregas não contam no relatório Operação de Entrega — e é o relatório que o #118 documenta com dados
dessa mesma filial.

Ele é reversível por construção: o `zerar` grava quem era o entregador de cada entrega **antes** de
escrever no banco, e o `voltar` só apaga o desfazer depois de conferir que a conta fechou. Se não
fechar, ele avisa e **mantém** o arquivo.

---

## 28. O aplicativo abrindo sem rede (1)

| Arquivo | A cena | Onde entra |
|---|---|---|
| `28-abrir-sem-rede/prints/01-app-sem-rede-do-zero.png` | o aplicativo **aberto do zero** sem rede — a tela que ele mostra antes de ter qualquer lista em cache | #112, *A lista não carrega* |

O que o #112 mostra hoje é outra coisa, e está correto: com o aplicativo **já aberto** e a rede
desligada, a lista fica congelada no que estava em cache e o *puxar para atualizar* não muda nada.
Sem mensagem de erro. É o que o entregador vê na maioria das vezes, e é o que o manual descreve.

Falta o outro caminho: **abrir o aplicativo do zero**, sem rede, sem cache. O relatório da rodada
passada explica por que não saiu — no build de desenvolvimento o aplicativo não carrega o bundle
JavaScript sem o Metro, então "sem rede" derruba o próprio app antes de qualquer tela. **Num APK de
produção esse caminho existe.**

### Como montar a cena

1. Instale o **APK de produção** (o da Play Store serve: `com.beetechentregador`).
2. Entre com o entregador de teste **com rede**, para o login e a lista existirem.
3. Force a parada do aplicativo e limpe o cache — **não** os dados, para não perder o login
   (`adb shell pm clear` derrubaria a sessão e o token de push).
4. Desligue wifi e dados, e abra o aplicativo.
5. Fotografe o que aparecer. **Qualquer tela serve como resposta**, inclusive "nada de especial, a
   lista abre vazia": se não houver mensagem, escreva isso no relatório e o manual passa a dizer que
   não há. O que não serve é a suposição.

---

## Como me entregar

Mesmo caminho das duas vezes: **WeTransfer**, um zip só, com as pastas exatamente como estão nas
tabelas. Sem renomear e sem recortar — o recorte é feito aqui, pelo `annotate.py` de cada manual.

```
capturas-3/
├── 26-codigo-de-barras/prints/    01-codigo-na-faixa.png  02-lido-com-sucesso.png
│                                  03-faixa-vermelha.png   04-pedido-ja-lido.png
├── 27-historico-vazio/prints/     01-historico-vazio.png
├── 28-abrir-sem-rede/prints/      01-app-sem-rede-do-zero.png
└── RELATORIO.md
```

A pasta se chama `capturas-3` porque é a **terceira leva de material** — `capturas-2` foi a rodada
de 19/09. Os números 26, 27 e 28 continuam a numeração dos capítulos, que é o que identifica cada
cena de verdade.

### O relatório, de novo, é a parte que faz o material valer

Três coisas, e a terceira é a que mais rendeu na rodada passada:

1. **A versão do app** e a data da captura.
2. **O aparelho**: emulador (qual AVD, qual Android) ou aparelho físico, qual. Aqui isso importa
   mais que nunca: a pasta 26 pode sair de aparelho físico e as outras do emulador, e o manual
   precisa saber qual é qual.
3. **Uma linha por print que saiu diferente do pedido**, dizendo o que aconteceu antes — e uma linha
   por print que **não saiu**, dizendo por quê.

Na rodada passada foi o item 3 que virou achado: o *Permissão necessária* no lugar da falha da melhor
rota mudou uma resposta do #113, e o "histórico vazio" com 22 entregas gerou os dois comandos novos do
script. **Print que sai diferente do pedido é informação, não defeito** — mas só se vier com a linha
que explica o que foi feito antes dele.
