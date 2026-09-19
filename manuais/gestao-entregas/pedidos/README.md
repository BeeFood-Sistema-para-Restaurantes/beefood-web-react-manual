# O que eu preciso de você — a pasta de pedidos

Três arquivos, e é tudo o que falta para a Gestão de Entregas 2.0 ficar documentada de ponta a
ponta. Onze manuais estão publicáveis hoje; um depende de foto.

| Arquivo | O que é |
|---|---|
| [`capturas-app.md`](capturas-app.md) | **26 prints do app**, em 10 pastas, com nome de arquivo, a cena, o manual que ganha a foto e o comando que monta a tela |
| [`janela-117.md`](janela-117.md) | o roteiro da **janela combinada**: sete fases, o que cada lado fotografa em cada uma, e o que fazer quando algo dá errado |
| [`../scripts/smoke-app.js`](../scripts/smoke-app.js) | o script que monta cada cena, **confere pela API do próprio app** e desmonta |

## Por onde começar

1. Leia [`capturas-app.md`](capturas-app.md) até a segunda tabela. Ela separa os **6 prints que
   bloqueiam** o #117 dos 20 que só melhoram manual já escrito.
2. Rode `node smoke-app.js casos` para ver os nove cenários e o que cada um destrava.
3. Marque uma hora para a janela do #117. É a única parte que precisa de nós dois ao mesmo tempo.

Os 20 prints de "só melhora" você faz sozinho, na ordem que quiser, sem me avisar. Cada linha da
tabela diz o comando e o gesto (`adb shell svc wifi disable`, e por aí vai).

## O que já está fechado

| Manual | Assunto | Fotos |
|---|---|---|
| **#104** a **#110** | o painel: liberar entregador, ler o mapa, montar rota, despachar, fechar, despacho automático, avisos de WhatsApp | minhas, feitas aqui |
| **#111** a **#116** | o app: entrar, as entregas do dia, chegar no endereço, código de barras, marketplace, receber na porta | as 63 que você mandou |
| **#117** | o ciclo completo, painel e app lado a lado | **esqueleto** — texto pronto, esperando os 6 prints |

Fora da numeração, dois relatórios entraram junto: **Operação de Entrega** e **Entregador (Taxa /
KM)**, os dois com dados de hoje da sandbox.

## O que o script não faz, e por quê

| Não faz | Motivo |
|---|---|
| tira foto do app | nenhum emulador Android roda aqui, e iOS está fora de qualquer hipótese. É a razão de esta pasta existir |
| apaga pedido | ele **desatribui** o entregador, que é o que tira o pedido da tela do app. `DELETE` em `_PreVenda` é caminho que pode errar o alvo, e o seeder do backend recusa pelo mesmo motivo |
| escreve fora da 38311/39202 | lista branca literal, herdada do `cenario.js`. Outra empresa aborta antes de abrir conexão |
| mexe em data de entrega sem aviso | só com `--permitir-passado`. Data de entrega é o que o relatório Operação de Entrega soma — mover uma entrega para ontem tira ela do total de hoje |

## Se as fotos não vierem

Nada se perde. Os seis manuais do app estão publicáveis, e o `MEMORIA.md` de cada um registra qual
foto falta e em que pergunta ela entraria. O #117 fica como esqueleto, com o lugar de cada imagem
marcado — é o único que não existe sem a janela.

## Quando quem fotografa não é você

Esta seção é a maquinaria do pacote, e fica de fora do zip de propósito: quem recebe o kit não
precisa saber como ele foi montado.

| Arquivo | O que é |
|---|---|
| [`montar-kit.sh`](montar-kit.sh) | monta o **zip auto-suficiente** — pedido, scripts, manuais com as imagens, material original e a árvore de pastas de saída já nomeada |
| [`instrucoes-ia-app.md`](instrucoes-ia-app.md) | o `LEIA-PRIMEIRO.md` do kit: o trabalho, o ambiente do emulador, as cinco regras do print e o que devolver. Escrito para uma IA operar sozinha |
| [`indice-referencia.md`](indice-referencia.md), [`arvore-de-entrega.md`](arvore-de-entrega.md) | os dois guias que viajam dentro do kit, um em cada pasta |

```bash
bash montar-kit.sh                 # sai um kit-teste-app-entregador.zip, ~24 MB
```

O script corta esta seção da cópia e reescreve os links relativos para a árvore do kit. As pastas
da referência vão com o nome que têm aqui, sem prefixo de número, para os links que os manuais fazem
entre si continuarem resolvendo lá dentro.
