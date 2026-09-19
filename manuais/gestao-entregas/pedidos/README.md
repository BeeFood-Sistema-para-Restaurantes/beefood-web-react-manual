# O que eu precisei de você — a pasta de pedidos

> ## ✅ O bloco está fechado — e há uma segunda lista, que não bloqueia nada
>
> As fotos da primeira lista chegaram, o **#117 foi publicado**, e com ele o bloco da Gestão de
> Entregas 2.0 ficou completo: **16 manuais, #104 a #119, nenhum esqueleto**.
>
> | | |
> |---|---|
> | Pedido | 26 prints, em 10 pastas |
> | Chegaram | **24**, mais um `RELATORIO.md` de quem os tirou |
> | Cancelados | **2** — a pasta `25-ios`; o dono decidiu que o manual não usa imagem de iOS |
> | Onde estão | [`../material-recebido/app-entregador/capturas-2/`](../material-recebido/app-entregador/capturas-2/README.md) |
> | Para onde foram | 6 para o **#117** (a metade do celular) e 18 para os seis manuais do app, que passaram de 61 para **79 imagens** |
>
> A **segunda lista** é de qualidade, não de falta: [`capturas-app-2.md`](capturas-app-2.md) —
> **6 prints, em 3 pastas**. Ela troca a única imagem **composta** do bloco por uma real e fecha
> duas telas que hoje o manual descreve só por escrito. Se não vier nenhuma, nada se perde: o
> `## O que falta` dos dezesseis continua dizendo que não falta nada para publicar.

Três arquivos, e foi tudo o que faltou para a Gestão de Entregas 2.0 ficar documentada de ponta a
ponta.

| Arquivo | O que é |
|---|---|
| [`capturas-app.md`](capturas-app.md) | **26 prints do app**, em 10 pastas, com nome de arquivo, a cena, o manual que ganha a foto e o comando que monta a tela — **respondido em 19/09** |
| [`capturas-app-2.md`](capturas-app-2.md) | a **segunda lista**: 6 prints de melhora, no mesmo formato. Leitura de código de barras de verdade, histórico vazio e o app abrindo sem rede |
| [`janela-117.md`](janela-117.md) | o roteiro da **janela combinada**: sete fases, o que cada lado fotografa em cada uma, e o que fazer quando algo dá errado |
| [`../scripts/smoke-app.js`](../scripts/smoke-app.js) | o script que monta cada cena, **confere pela API do próprio app** e desmonta |

## Como foi, no fim

1. Os **6 prints que bloqueavam** o #117 saíram, e o roteiro da janela do
   [`janela-117.md`](janela-117.md) foi seguido só do lado do celular. O lado do painel foi
   **reencenado depois**, com os mesmos três pedidos: o estado de cada fase voltou ao banco e o
   painel fotografou o que o celular já tinha registrado. Deu no mesmo, e sem precisar de nós dois
   na mesma hora.
2. Os **18 de "só melhora"** viraram **seção nova** em quatro manuais, não retoque: *A lista muda
   sozinha* (#112), *Quando o servidor não confirma a saída* (#113), *Dois casos fora do roteiro*
   (#115) e *Quando a cobrança não fecha* (#116). A convenção da casa é FAQ sem imagem, então a
   pergunta aponta para a seção.
3. **Dois prints saíram diferentes do pedido**, e os dois viraram achado: sem rede o *MELHOR ROTA*
   responde *Permissão necessária*, e o "histórico vazio" veio com 22 entregas em três dias. O
   manual passou a descrever o que a tela faz.

O item 3 é o que gerou a segunda lista. O *Permissão necessária* virou resposta do #113 e não precisa
de mais nada; o histórico com 22 entregas mostrou que **o pedido estava errado**, não a foto — o
Histórico do app lê tudo o que o entregador já entregou, de qualquer dia, e o caso do script só
desatribuía o lote da execução. Daí os dois comandos novos, e daí a pasta 27 da lista nova.

## O que já está fechado

| Manual | Assunto | Fotos |
|---|---|---|
| **#104** a **#110** | o painel: liberar entregador, ler o mapa, montar rota, despachar, fechar, despacho automático, avisos de WhatsApp | minhas, feitas aqui |
| **#111** a **#116** | o app: entrar, as entregas do dia, chegar no endereço, código de barras, marketplace, receber na porta | as 63 da primeira rodada **mais 18 da segunda** |
| **#117** | o ciclo completo, painel e app lado a lado | **13** — 6 do celular, suas; 7 do painel, minhas |

Fora da numeração, dois relatórios entraram junto: **Operação de Entrega** e **Entregador (Taxa /
KM)**, os dois com dados de hoje da sandbox.

## O que a segunda lista muda, se vier

| Pasta | Prints | Manual | Efeito |
|---|--:|---|---|
| **26** código de barras | 4 | #114 | troca a **única imagem composta** do bloco por leitura real, e mostra as três faixas de resultado que hoje são tabela |
| **27** histórico vazio | 1 | #112, #111 | a tela *Nenhuma entrega no período*, que a rodada passada não conseguiu produzir |
| **28** abrir sem rede | 1 | #112 | o app **abrindo do zero** sem rede, que só existe em APK de produção |

Se der tempo para uma só, é a **26**: imagem montada é o único ponto do bloco em que a foto não é
prova. Está declarada como composta no `fluxo-codigo.md` do #114, o que é honesto, mas imagem real é
melhor que imagem declarada.

## O que o script não faz, e por quê

| Não faz | Motivo |
|---|---|
| tira foto do app | nenhum emulador Android roda aqui, e iOS está fora de qualquer hipótese. É a razão de esta pasta existir |
| apaga pedido | ele **desatribui** o entregador, que é o que tira o pedido da tela do app. `DELETE` em `_PreVenda` é caminho que pode errar o alvo, e o seeder do backend recusa pelo mesmo motivo |
| escreve fora da 38311/39202 | lista branca literal, herdada do `cenario.js`. Outra empresa aborta antes de abrir conexão |
| mexe em data de entrega sem aviso | só com `--permitir-passado`. Data de entrega é o que o relatório Operação de Entrega soma — mover uma entrega para ontem tira ela do total de hoje |

Os dois comandos novos — `historico-zerar` e `historico-voltar` — são a exceção que confirma a regra:
eles **mexem** no histórico inteiro do entregador, e por isso nasceram com desfazer. O `zerar` grava
quem era o entregador de cada entrega antes de escrever, o `voltar` só apaga o desfazer depois de
conferir que a conta fechou, e um segundo `zerar` sobre desfazer pendente é recusado.

## Se as fotos não viessem

Nada se perderia. Os seis manuais do app já estavam publicáveis, e o `MEMORIA.md` de cada um
registrava qual foto faltava e em que pergunta ela entraria. O #117 ficaria como esqueleto, com o
lugar de cada imagem marcado — era o único que não existia sem a janela.

Vieram, e hoje o `## O que falta` dos seis diz **"nada"** — nada que impeça publicar. Ficou escrito
assim de propósito: quando não falta nada, a memória tem que dizer isso com a mesma clareza com que
dizia o contrário. Onde a segunda lista melhora algo, o mesmo `## O que falta` diz qual print é, para
onde vai e por que o manual já funciona sem ele.

## Quando quem fotografa não é você

Os dois pacotes estão aqui, versionados. No GitHub, abra o arquivo e use o botão de download; é só
repassar para quem vai fotografar.

| Zip | Rodada | O que pede |
|---|---|---|
| **[`kit-teste-app-entregador.zip`](kit-teste-app-entregador.zip)** | 2 — respondida | 24 MB, 323 arquivos, os 26 prints de `capturas-app.md` |
| **[`kit-teste-app-entregador-2.zip`](kit-teste-app-entregador-2.zip)** | 3 — aberta | 39 MB, 393 arquivos, os 6 prints de `capturas-app-2.md`. Mais pesado porque leva também as 24 capturas da rodada 2 como referência de tela |

**O zip da rodada 2 está congelado como foi entregue, e é para ficar assim.** Regravá-lo hoje o
deixaria com 404 arquivos, porque a referência passou a incluir as 24 fotos que ele **pede** — um kit
que já traz a resposta do próprio pedido confunde quem o abre. A regra de regravar vale para o zip da
rodada **aberta**.

Esta seção é a maquinaria do pacote, e fica de fora do zip de propósito: quem recebe o kit não
precisa saber como ele foi montado.

| Arquivo | O que é |
|---|---|
| [`montar-kit.sh`](montar-kit.sh) | monta o **zip auto-suficiente** — pedido, scripts, manuais com as imagens, material original e a árvore de pastas de saída já nomeada |
| [`instrucoes-ia-app.md`](instrucoes-ia-app.md), [`instrucoes-ia-app-2.md`](instrucoes-ia-app-2.md) | o `LEIA-PRIMEIRO.md` de cada rodada: o trabalho, o ambiente do emulador, as cinco regras do print e o que devolver. Escrito para uma IA operar sozinha |
| [`indice-referencia.md`](indice-referencia.md), [`arvore-de-entrega.md`](arvore-de-entrega.md) | os dois guias que viajam dentro do kit da rodada 2, um em cada pasta |
| [`indice-referencia-2.md`](indice-referencia-2.md), [`arvore-de-entrega-2.md`](arvore-de-entrega-2.md) | os mesmos dois, da rodada 3 |

```bash
bash montar-kit.sh                 # rodada 3, o kit aberto; regrava o zip nesta pasta
bash montar-kit.sh 2 /tmp          # a rodada 2 ainda monta, mas fora daqui: o zip dela está congelado
```

A rodada muda quatro coisas e nada mais: o nome do zip, o pedido que é a tarefa, o `LEIA-PRIMEIRO` e
a árvore de pastas de saída. Scripts, manuais de referência, material original e ferramentas de
emulador são iguais, porque é igual o trabalho.

O script corta esta seção da cópia e reescreve os links relativos para a árvore do kit. As pastas
da referência vão com o nome que têm aqui, sem prefixo de número, para os links que os manuais fazem
entre si continuarem resolvendo lá dentro.

**Mexeu em algum dos arquivos que entram no kit? Rode o script e commite o zip junto.** Ele é uma
cópia, e cópia que não acompanha o original engana quem confia nela.
