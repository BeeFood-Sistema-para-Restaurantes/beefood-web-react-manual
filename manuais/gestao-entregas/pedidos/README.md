# O que eu precisei de você — a pasta de pedidos

> ## ✅ Fechado em 19/09/2026 — **não falta mais nada**
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
> | Para onde foram | 6 para o **#117** (a metade do celular) e 18 para os seis manuais do app, que passaram de 61 para **79 imagens** |
>
> Esta pasta continua aqui como **registro e como maquinaria**: se um dia precisar de mais prints do
> aplicativo, o pedido, o kit e o smoke test estão prontos para uma nova rodada. Nada nela é lista
> aberta hoje.

Três arquivos, e foi tudo o que faltou para a Gestão de Entregas 2.0 ficar documentada de ponta a
ponta.

| Arquivo | O que é |
|---|---|
| [`capturas-app.md`](capturas-app.md) | **26 prints do app**, em 10 pastas, com nome de arquivo, a cena, o manual que ganha a foto e o comando que monta a tela |
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

## O que já está fechado

| Manual | Assunto | Fotos |
|---|---|---|
| **#104** a **#110** | o painel: liberar entregador, ler o mapa, montar rota, despachar, fechar, despacho automático, avisos de WhatsApp | minhas, feitas aqui |
| **#111** a **#116** | o app: entrar, as entregas do dia, chegar no endereço, código de barras, marketplace, receber na porta | as 63 da primeira rodada **mais 18 da segunda** |
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

## Se as fotos não viessem

Nada se perderia. Os seis manuais do app já estavam publicáveis, e o `MEMORIA.md` de cada um
registrava qual foto faltava e em que pergunta ela entraria. O #117 ficaria como esqueleto, com o
lugar de cada imagem marcado — era o único que não existia sem a janela.

Vieram, e hoje o `## O que falta` dos seis diz **"nada"**. Ficou escrito assim de propósito: quando
não falta nada, a memória tem que dizer isso com a mesma clareza com que dizia o contrário.

## Quando quem fotografa não é você

O pacote pronto está aqui, versionado:
**[`kit-teste-app-entregador.zip`](kit-teste-app-entregador.zip)** — 24 MB, 323 arquivos. No GitHub,
abra o arquivo e use o botão de download; é só repassar para quem vai fotografar.

Esta seção é a maquinaria do pacote, e fica de fora do zip de propósito: quem recebe o kit não
precisa saber como ele foi montado.

| Arquivo | O que é |
|---|---|
| [`montar-kit.sh`](montar-kit.sh) | monta o **zip auto-suficiente** — pedido, scripts, manuais com as imagens, material original e a árvore de pastas de saída já nomeada |
| [`instrucoes-ia-app.md`](instrucoes-ia-app.md) | o `LEIA-PRIMEIRO.md` do kit: o trabalho, o ambiente do emulador, as cinco regras do print e o que devolver. Escrito para uma IA operar sozinha |
| [`indice-referencia.md`](indice-referencia.md), [`arvore-de-entrega.md`](arvore-de-entrega.md) | os dois guias que viajam dentro do kit, um em cada pasta |

```bash
bash montar-kit.sh                 # regrava o zip nesta pasta; commite o resultado
```

O script corta esta seção da cópia e reescreve os links relativos para a árvore do kit. As pastas
da referência vão com o nome que têm aqui, sem prefixo de número, para os links que os manuais fazem
entre si continuarem resolvendo lá dentro.

**Mexeu em algum dos arquivos que entram no kit? Rode o script e commite o zip junto.** Ele é uma
cópia, e cópia que não acompanha o original engana quem confia nela.
