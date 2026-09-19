# O que as telas fazem de verdade — #104 Liberar o entregador

Lido em `beefood-web-react`, em `beetech-server-node-2.0` (inclusive
`docs/gestao-entrega-2.0/19-codigo-de-barras-no-3.md`) e conferido contra o sandbox. Serve
para o manual não prometer o que a tela não faz.

## Os dois cadastros, e por que são dois

| Cadastro | Tela | Onde grava | Quem lê |
|---|---|---|---|
| Funcionário com função *Entregador* | `/cadastro-funcionarios` | `_Funcionario` (MSSQL) | o painel de entregas, o despacho automático e os relatórios |
| Usuário com *Aplicativos* ligado | `/usuarios` | `_Usuario`, com `funcionarioID` apontando para o de cima | o **login do app**, que roda no `node-2.0` (`tusuario/...`) |

São dois porque servem a coisas diferentes: o painel precisa da **pessoa** (para atribuir
rota e somar entrega), e o app precisa de uma **credencial**. O vínculo é o
`funcionarioID` no usuário — e é ele que faltando produz o sintoma mais confuso do manual:
login entra, lista vem vazia.

O switch **Aplicativos** é um campo do usuário, checado no login do app. Sem ele o servidor
recusa a credencial. Não há como ligar isso pelo app nem pelo painel.

## A função é exclusiva

A aba *Função* é um grupo de rádio, não um conjunto de caixinhas: *Garçom*, *Entregador* e
*Outra Função* se excluem. Quem trabalha nas duas pontas precisa de dois cadastros de
funcionário — e, na prática, de dois usuários, porque o app de garçom e o de entregador são
aplicativos diferentes.

`valorDiaria` e `valorKm` moram no próprio funcionário. **Nada no fluxo de entrega lê esses
dois campos**: eles só aparecem no relatório de fechamento do entregador. É por isso que o
manual manda deixar zero e voltar depois, em vez de travar o cadastro esperando o número.

## Como o entregador novo aparece no painel

O `GET /api/entrega2/gestao/painel/...` devolve `entregadores[]` com **todos** os
funcionários marcados como entregador, mesmo os que nunca abriram o app. Quem nunca entrou
vem sem linha em `entregador_status` (Aurora `beefood-entregas`), e a tela mostra isso como
**Nunca usou o app**, dentro do grupo *Offline*.

Ou seja: o cadastro deste manual é suficiente para o nome aparecer. O que o cadastro **não**
faz é colocar alguém *Disponível* — isso só o app faz, pelo
`POST /api/entrega2/gestao/presenca`.

## O código de barras no cupom

| | |
|---|---|
| Onde liga | `/impressao` → aba **Layout** → **Cupom Pedido** → aba **Texto Padrão** |
| Campo | `beeEntregaCodigoBarras`, no `ModalEditarImpressaoLayout.tsx` |
| Conteúdo impresso | o `preVendaID` do pedido, com um dígito a mais no fim |
| Condição para sair | pedido de **delivery com entrega** (não sai em retirada nem presencial) |

### Ler o código é despachar — não é conferir

Este é o ponto que muda a redação do manual. O app chama
`POST /tentrega/lerCodigoBarras`, e o controller roda a
`procProcessa_Entregador_LerCodigoBarras` e em seguida o **`SituacaoDeliveryUpdater` com
`'ENTREGA'`** — o mesmo orquestrador do botão *Despachar* da Gestão de Entregas. Portanto
uma leitura:

1. grava a situação **ENTREGA** no ERP;
2. atrela o pedido ao entregador que leu;
3. notifica o **marketplace** de origem, quando houver;
4. imprime o que estiver configurado para a mudança de situação;
5. **enfileira o WhatsApp** de saída para entrega.

Nada disso é desfeito pelo app. Por isso o manual avisa para não "testar o leitor" em pedido
de cliente, e diz que o acerto é no painel.

O controller também grava auditoria: coluna `Situação Delivery`, texto
`App Entregador: ENTREGA`, registro `Venda {numeroPreVenda}` — visível em **Histórico de
Alteração**. O `usuarioID` vai nulo de propósito, então o log diz *o que* aconteceu e não
*quem* clicou; quem foi se descobre pelo entregador atrelado ao pedido.

### Gate comercial

O `validaPlanoEntregador.js` libera o app do entregador para empresa com
`beetechPlanoID === 5`, com `entregaAtiva`, ou numa lista de 32 exceções. Quando barra, a
rota de código de barras **devolve 200** (e não erro) para o app não mostrar "erro na
leitura" a quem simplesmente não tem o recurso contratado. Efeito prático para o suporte:
**leitura que "não faz nada" pode ser plano, não bug.**

O gate existe na leitura de código de barras e no histórico do app; a lista principal de
entregas nunca foi barrada. Não é uniforme, e o manual não tenta explicar isso ao lojista.

## O que estas telas **não** fazem

- **Não** criam senha de funcionário: senha é do usuário.
- **Não** colocam o entregador disponível.
- **Não** validam nome repetido — dois "José" convivem e ficam indistinguíveis no mapa.
- **Não** avisam quando o switch *Aplicativos* está desligado: o erro só aparece no celular.

## Cenário para as capturas

Nenhum cenário de entrega foi necessário: as cinco primeiras telas são cadastro, e as duas
de impressão são configuração. A caixinha `Código de Barras App Entrega` já estava marcada
na sandbox e **não foi alterada** — o print é do estado real.

A foto do cupom impresso (`08-cupom-impresso.png`) é herdada do **#57**, com o endereço já
tarjado na origem. Ela continua correta: o desenho do pé do cupom não mudou.

```bash
# as capturas saíram destes scripts, na sandbox 38311/39202
python3 /tmp/ge/c104.py    # funcionários, ficha, aba Função, usuários, usuário novo
python3 /tmp/ge/c104c.py   # Impressão > Layout e a aba Texto Padrão
python3 /tmp/ge/c104d.py   # refez a geometria do lápis da lista de layouts
```
