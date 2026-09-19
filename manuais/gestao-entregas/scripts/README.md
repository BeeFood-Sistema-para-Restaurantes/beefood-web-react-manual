# Os dois scripts de cenário

Todo manual da Gestão de Entregas 2.0 precisa de um cenário montado à mão. A tela abre vazia, o
entregador não aparece no mapa sem ping de GPS, o relatório só mostra número depois que alguém
entregou, e a lista do app só existe quando uma coluna do pedido tem o funcionário certo. Montar
isso clicando dá meia hora por manual e sai diferente cada vez — daí os dois arquivos.

| Script | Monta o que | Usado por |
|---|---|---|
| [`cenario.js`](cenario.js) | o que o **painel** precisa: pedidos, presença, movimento, rota, despacho, baixa, fechamento | #104 a #110, e os dois relatórios |
| [`smoke-app.js`](smoke-app.js) | o que a **tela do celular** precisa: nove cenários de captura e a janela de sete fases do #117 | #111 a #117 |

O `smoke-app.js` usa o `cenario.js` como biblioteca: quem fala com a API de rota continua sendo um
arquivo só, para existir um lugar único onde a rota nasce e é despachada.

## Antes da primeira execução

Nenhuma credencial mora nestes arquivos — o repositório é público. Host, senha e segredo saem do
clone do backend, e o clone precisa dos dois drivers de banco:

```bash
cd ~/refs/beetech-server-node-2.0 && npm install --no-save mssql mysql2
```

Se o clone não estiver no caminho padrão, passe `--backend <caminho>` ou exporte
`BEETECH_BACKEND`. No Windows, o caminho é o do repositório `beetech-server-node`.

## `cenario.js` — o painel

```bash
node cenario.js estado                     # o que existe hoje na filial
node cenario.js limpar-fantasma             # tira o rotaIDAtual órfão do entregador
node cenario.js semear --qtd 4              # pedidos com endereço e coordenada
node cenario.js presenca --status DISPONIVEL
node cenario.js andar --para -23.4930,-47.4548 --passos 6
node cenario.js rota-criar --pedidos 59515246,59515250
node cenario.js rota-despachar --rota 121
node cenario.js parada-entregar --rota 121 --pedido 59515246
node cenario.js rota-finalizar --rota 121
node cenario.js ciclo-completo --qtd 3      # o que dá dado de HOJE ao relatório
```

O `ciclo-completo` é o atalho dos relatórios: ele semeia, monta rota, despacha, anda, entrega e
finaliza, deixando a data de hoje com número para somar.

## `smoke-app.js` — o app

```bash
node smoke-app.js casos                     # os nove cenários, com a foto de cada um
node smoke-app.js estado                    # o que o app está vendo agora
node smoke-app.js preparar --caso lista      # monta e confere
node smoke-app.js conferir                   # confere de novo
node smoke-app.js limpar                     # tira tudo da tela do app
node smoke-app.js arquivar-fila              # tira da fila do painel, lotes antigos
node smoke-app.js janela-117 --fase 1        # o roteiro dos dois lados
```

Cada `--caso` é **uma foto pedida** em [`../pedidos/capturas-app.md`](../pedidos/capturas-app.md).
A conferência é a parte que vale: ela lê a **API do próprio app**, não o banco, porque entre os dois
moram o agrupamento de rota, o filtro de situação e a ordenação por distância — e já aconteceu de o
banco estar certo e a tela vir vazia.

| Caso | A tela que ele produz |
|---|---|
| `lista` | quatro entregas abertas, com quatro formas de pagamento diferentes |
| `rota-viva` | três paradas numa rota **não despachada**, mais uma entrega solta |
| `marketplace` | um pedido de iFood e um de 99Food, os dois já pagos |
| `keeta` | pedido de plataforma **sem** botão de confirmação — só o selo |
| `pago` | saldo zero sem marketplace: a folha *Pedido já pago* |
| `notificacao` | o aviso chegando na tela, no instante da atribuição |
| `troca` | a entrega sendo tirada do entregador |
| `historico-vazio` | a aba Entregas sem nenhuma entrega, que é a tela de trabalho recém-logado. O nome vem do pedido original e é mais largo que o caso: o Histórico **não** esvazia, porque ele lê tudo o que aquele entregador já entregou |
| `historico-dias` | o histórico agrupado por dia, com dias anteriores |

## Como eles evitam estrago

Os dois compartilham as travas, e o `smoke-app.js` acrescenta uma.

1. **Lista branca de alvo** literal: `38311/39202`. Outra empresa aborta antes de abrir conexão.
   Destravar exige editar o arquivo, não passar uma flag — semear pedido falso em loja real seria
   pior que qualquer bug, porque o lojista sairia entregando.
2. **Rota e parada vão pela API**, nunca por SQL. Assim o log do ERP, o socket e o `rota_evento`
   acontecem como no uso real.
3. **Sentinela de escrita no ERP** (só no `smoke-app.js`): `UPDATE` apenas em `_PreVenda`, apenas
   em `preVendaID` que o script criou na janela, apenas nas colunas da lista branca
   `COLUNAS_GRAVAVEIS`, e sempre com `filialID` da lista branca no `WHERE`.
4. **Data de entrega exige `--permitir-passado`.** É a única escrita que altera histórico — e
   histórico é o que o relatório Operação de Entrega soma por data.
5. **`--dry-run` em tudo.**
6. **`limpar` não apaga pedido.** Ele desatribui o entregador, que é o que tira o pedido da tela do
   app sem mexer no que o ERP registrou.
7. **`arquivar-fila` tem sentinela própria, e mais forte:** o `WHERE` exige o marcador
   `[SEED-ENTREGAS]` que o seeder grava em `Observacoes`. Pedido de verdade não tem esse marcador,
   então não há como o comando alcançar um.

## `limpar` e `arquivar-fila` resolvem telas diferentes

Achado do ensaio da janela do #117, e vale saber antes de fotografar: **`limpar` tira o pedido da
tela do app, mas não do painel.** Ele desatribui o entregador, e pedido sem entregador continua em
*Pedidos sem rota* por até 6 h. Depois de uma tarde de ensaios a fila do painel tinha **21 pedidos de
teste** — e a primeira foto do #117 é justamente "três pedidos prontos na fila".

O `arquivar-fila` resolve isso mandando os pedidos de teste para `AGUARDANDO`. É o estado certo,
porque a view do painel filtra `PREPARO`/`PRONTO`/`ENTREGA`/`ENTREGUE` e o app ignora `AGUARDANDO`: o
pedido sai das duas telas sem ser apagado e **sem entrar na conta de entregas do dia** — o que
`ENTREGUE` faria, inflando o relatório Operação de Entrega.

A fase 1 da janela do #117 **aborta** se achar lote antigo na fila, em vez de deixar você descobrir
na foto.

> **`beetech_leitura` engana pelo nome.** O usuário do MSSQL que todo o backend usa é
> `db_datareader` **+ `db_datawriter` + `db_ddladmin`**, com `EXECUTE` no banco inteiro. É por isso
> que os scripts funcionam daqui. Trate como escrita em produção, porque é.

## O arquivo de estado

O `smoke-app.js` guarda os `preVendaID` e `rotaID` da janela em `.smoke-app-estado.json`, ignorado
pelo git. Ele existe por causa da sentinela: as sete fases do #117 acontecem em execuções
diferentes, com o dono fotografando entre uma e outra, e sem memória a fase 3 não teria autorização
para mexer no pedido que a fase 1 criou.

Se um lote antigo travar o script — *"pedido fora do estado deste script"* —, apague o arquivo.
