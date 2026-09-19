# O que eu precisei de você — a pasta de pedidos

> ## ✅ O bloco está fechado, e não há lista aberta
>
> As fotos chegaram, o **#117 foi publicado**, e com ele o bloco da Gestão de Entregas 2.0 ficou
> completo: **16 manuais, #104 a #119, nenhum esqueleto**.
>
> | | |
> |---|---|
> | Pedido | 26 prints, em 10 pastas |
> | Chegaram | **24**, mais um `RELATORIO.md` de quem os tirou |
> | Cancelados | **2** — a pasta `25-ios`; o dono decidiu que o manual não usa imagem de iOS |
> | Onde estão | [`../material-recebido/app-entregador/capturas-2/`](../material-recebido/app-entregador/capturas-2/README.md) |
> | Para onde foram | 6 para o **#117** (a metade do celular) e 17 para os seis manuais do app |
>
> **Uma segunda lista foi escrita e descartada** sem sair daqui. O porquê está em
> [O pedido que não fiz](#o-pedido-que-não-fiz), e é a parte desta pasta que vale reler antes de
> abrir qualquer outra: o que decide um pedido de imagem não é o que ainda não foi fotografado.

Três arquivos, e foi tudo o que faltou para a Gestão de Entregas 2.0 ficar documentada de ponta a
ponta.

| Arquivo | O que é |
|---|---|
| [`capturas-app.md`](capturas-app.md) | **26 prints do app**, em 10 pastas, com nome de arquivo, a cena, o manual que ganha a foto e o comando que monta a tela — **respondido em 19/09** |
| [`janela-117.md`](janela-117.md) | o roteiro da **janela combinada**: sete fases, o que cada lado fotografa em cada uma, e o que fazer quando algo dá errado |
| [`../scripts/smoke-app.js`](../scripts/smoke-app.js) | o script que monta cada cena, **confere pela API do próprio app** e desmonta |

## Como foi, no fim

1. Os **6 prints que bloqueavam** o #117 saíram, e o roteiro da janela do
   [`janela-117.md`](janela-117.md) foi seguido só do lado do celular. O lado do painel foi
   **reencenado depois**, com os mesmos três pedidos: o estado de cada fase voltou ao banco e o
   painel fotografou o que o celular já tinha registrado. Deu no mesmo, e sem precisar de nós dois
   na mesma hora.
2. Os de "só melhora" viraram **seção nova** em quatro manuais, não retoque: *A lista muda sozinha*
   (#112), *Quando o servidor não confirma a saída* (#113), *Dois casos fora do roteiro* (#115) e
   *Quando a cobrança não fecha* (#116). A convenção da casa é FAQ sem imagem, então a pergunta
   aponta para a seção.
3. **Dois prints saíram diferentes do pedido**, e um dos dois virou achado: sem rede o *MELHOR ROTA*
   responde *Permissão necessária* — uma permissão negada, não a falha de cálculo que o pedido
   esperava —, e o #113 passou a ensinar isso. O outro, o "histórico vazio", não virou nada: veio
   com 22 entregas em três dias porque o Histórico lê tudo o que o entregador já entregou, e a
   conclusão certa era que **a foto não servia para nada**, não que o pedido precisava de mais uma
   volta.

## O pedido que não fiz

Depois da entrega, escrevi uma segunda lista — 6 prints em 4 pastas — e o dono a recusou na
leitura, antes de delegar. Ela pedia a leitura de código de barras dando certo e dando errado, a
tela de *Nenhuma entrega no período* e o app abrindo sem rede. A recusa foi curta: *"que tipo de
manual estamos fazendo? mostrar uma imagem de um aplicativo sem pedidos é totalmente fora de
realidade. o manual precisa mostrar utilidade"*.

Ele estava certo, e o erro não era de execução: eu estava cobrindo o aplicativo em vez de escrever
o que alguém procura. As três tinham a mesma falha, e ela é fácil de repetir sem perceber:

| O que eu pedi | Por que não servia |
|---|---|
| a tela de histórico **de verdade vazia** | ninguém abre um manual para descobrir como é a tela quando não há nada nela. E para produzi-la eu tinha escrito dois comandos que apagavam o histórico do entregador — trabalho, e risco, por uma imagem que não ensina nada |
| o app **abrindo sem rede** | não há o que fazer com a resposta. Sem rede o entregador já sabe que está sem rede, e o manual não muda o que ele faz |
| as **faixas de resultado** da leitura, uma foto para cada | são seis mensagens curtas. Seis frases numa tabela são mais úteis que quatro fotos quase iguais de uma faixa colorida — e a tabela já está no #114 |

O critério que ficou está na [memória geral](../../../.cursor/skills/manual-sistema/references/MEMORIA-GERAL.md),
e é uma pergunta só: **o leitor sai daí fazendo algo diferente?** Tela de erro com saída ganha
imagem — a janela *Despacho não confirmado* do #113 ganhou, porque manda ligar para a loja e avisa
para não tocar de novo. Tela de ausência, não ganha.

## O que já está fechado

| Manual | Assunto | Fotos |
|---|---|---|
| **#104** a **#110** | o painel: liberar entregador, ler o mapa, montar rota, despachar, fechar, despacho automático, avisos de WhatsApp | minhas, feitas aqui |
| **#111** a **#116** | o app: entrar, as entregas do dia, chegar no endereço, código de barras, marketplace, receber na porta | as 63 da primeira rodada **mais 17 da segunda** |
| **#117** | o ciclo completo, painel e app lado a lado | **13** — 6 do celular, suas; 7 do painel, minhas |

Fora da numeração, dois relatórios entraram junto: **Operação de Entrega** e **Entregador (Taxa /
KM)**, os dois com dados de hoje da sandbox.

## O que o script não faz, e por quê

| Não faz | Motivo |
|---|---|
| tira foto do app | nenhum emulador Android roda aqui, e iOS está fora de qualquer hipótese. É a razão de esta pasta existir |
| apaga pedido | ele **desatribui** o entregador, que é o que tira o pedido da tela do app. `DELETE` em `_PreVenda` é caminho que pode errar o alvo, e o seeder do backend recusa pelo mesmo motivo |
| escreve fora da 38311/39202 | lista branca literal, herdada do `cenario.js`. Outra empresa aborta antes de abrir conexão |
| mexe em data de entrega sem aviso | só com `--permitir-passado`. Data de entrega é o que o relatório Operação de Entrega soma — mover uma entrega para ontem tira ela do total de hoje |
| apaga histórico de entregador | chegou a existir, para a foto do histórico vazio, e saiu junto com ela. Um comando que reescreve o passado inteiro de um entregador precisa valer muito mais que isso |

## Se as fotos não viessem

Nada se perderia. Os seis manuais do app já estavam publicáveis, e o `MEMORIA.md` de cada um
registrava qual foto faltava e em que pergunta ela entraria. O #117 ficaria como esqueleto, com o
lugar de cada imagem marcado — era o único que não existia sem a janela.

Vieram, e hoje o `## O que falta` dos seis diz **"nada"**. Ficou escrito assim de propósito: quando
não falta nada, a memória tem que dizer isso com a mesma clareza com que dizia o contrário.

## Quando quem fotografa não é você

O pacote está aqui, versionado: **[`kit-teste-app-entregador.zip`](kit-teste-app-entregador.zip)**,
24 MB, 323 arquivos, o pedido das 26 fotos com tudo o que ele precisa para se explicar sozinho. No
GitHub, abra o arquivo e use o botão de download; é só repassar para quem vai fotografar.

**O zip está congelado como foi entregue, e é para ficar assim.** Regravá-lo hoje o deixaria maior,
porque a referência passou a incluir as 24 fotos que ele **pede** — um kit que já traz a resposta do
próprio pedido confunde quem o abre.

Esta seção é a maquinaria do pacote, e fica de fora do zip de propósito: quem recebe o kit não
precisa saber como ele foi montado.

| Arquivo | O que é |
|---|---|
| [`montar-kit.sh`](montar-kit.sh) | monta o **zip auto-suficiente** — pedido, scripts, manuais com as imagens, material original e a árvore de pastas de saída já nomeada |
| [`instrucoes-ia-app.md`](instrucoes-ia-app.md) | o `LEIA-PRIMEIRO.md` do kit: o trabalho, o ambiente do emulador, as cinco regras do print e o que devolver. Escrito para uma IA operar sozinha |
| [`indice-referencia.md`](indice-referencia.md), [`arvore-de-entrega.md`](arvore-de-entrega.md) | os dois guias que viajam dentro do kit, um em cada pasta |

```bash
bash montar-kit.sh /tmp     # monta fora daqui: o zip desta pasta está congelado
```

O script corta esta seção da cópia e reescreve os links relativos para a árvore do kit. As pastas
da referência vão com o nome que têm aqui, sem prefixo de número, para os links que os manuais fazem
entre si continuarem resolvendo lá dentro.

**Se uma próxima rodada existir**, ela começa pela pergunta da seção
[O pedido que não fiz](#o-pedido-que-não-fiz), e não por esta: a maquinaria funciona, o que falhou
foi o critério do que pedir.
