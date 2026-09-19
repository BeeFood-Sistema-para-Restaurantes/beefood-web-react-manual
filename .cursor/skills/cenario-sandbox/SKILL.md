---
name: cenario-sandbox
description: Monta na sandbox do BeeFood o cenário que uma captura precisa e que a tela não sabe criar — pedido de iFood, 99Food, Keeta ou AIQFome, pedido atrasado, pedido já pago, fila cheia. Ensina a descobrir de onde um campo vem (smoke teste contra a API antes de qualquer SQL) e a escrever script de escrita no banco com lista branca, sentinela e ensaio. Use quando faltar dado para fotografar ou testar, ou quando o pedido falar de smoke teste, semear pedido, forjar origem, marketplace de teste ou inserir no banco. Não use para escrever o manual nem a arte — isso é manual-sistema e carrossel.
---

# Cenário de captura na sandbox

Manual e carrossel só existem se a tela **tiver o que mostrar**. Quando o cenário não
existe — nenhum pedido de iFood na fila, nenhum cartão vermelho de atraso, nenhuma
comanda aberta — esta skill é o caminho para montá-lo sem inventar print e sem estragar a
sandbox.

Ela serve às duas skills de conteúdo e não escreve em nenhuma das duas:

| Skill | O que ela pede daqui |
|---|---|
| `manual-sistema` | o estado que o passo a passo precisa fotografar |
| `carrossel` | a tela real que substitui o desenho em HTML |

## A regra que organiza tudo

> **Primeiro descubra de onde o dado vem. Só depois escolha a ferramenta.**

A ordem importa porque cada degrau é mais invasivo que o anterior, e a maioria dos
cenários morre no primeiro:

1. **Pela tela.** Se o produto cria aquilo, crie pela tela. É o único caminho que produz
   registro coerente de ponta a ponta, e é grátis.
2. **Pela rota que a tela usa.** Mais rápido para repetir vinte vezes, e ainda é o produto
   gravando. Aqui entra o smoke teste em Playwright, que já está autenticado.
3. **Por outra rota do produto.** Às vezes o campo que falta só é gravado por **outra**
   porta — o cardápio público, o app do entregador, o totem. Descobrir qual é o trabalho
   principal desta skill.
4. **Escrevendo no banco.** Último recurso, e mesmo assim **`UPDATE`, nunca `INSERT`**:
   o pedido nasce pela rota do produto, com número de venda, caixa e cliente coerentes, e
   o script só estampa a coluna que nenhuma rota grava.

Pular para o degrau 4 sem passar pelos outros é o erro clássico. Ele parece economia de
tempo e custa uma base com registro torto que ninguém sabe de onde veio.

## Degrau 2 e 3: como descobrir de onde um campo vem

O caso completo, com números, está no
[`fluxo-codigo.md` do #120](../../../manuais/painel-entregador/fluxo-codigo.md). O método,
em quatro movimentos:

### 1. Mandar o campo e reler

Mande o campo em **todas as posições plausíveis** do corpo — raiz, objeto aninhado,
sub-objeto do cliente — e depois **releia o registro pela API**. Não confie no `200`: as
rotas do BeeFood respondem `resultado: true` para corpo que elas ignoraram inteiro. Seis
rotas de atualização de venda responderam `true` e nenhuma gravou o identificador que
tinham recebido.

### 2. Farejar a rede de quem consegue

Se alguma parte do produto grava aquele valor, ela faz uma chamada. Abra a tela que
consegue e **grave a requisição inteira** — corpo e cabeçalhos:

```python
page.on("request", lambda req: ...)   # req.post_data e req.all_headers()
```

Foi assim que apareceu a rota do cardápio público
(`POST app.beetechapi.be/datasnap/rest/tmesa/pedido`) e, com ela, o `Authorization: Basic`
sem o qual a rota responde **401**.

> **Credencial farejada não entra no repositório.** O repositório é público, e esse
> `Basic` não é da sandbox: é a autenticação do cardápio com o ERP de qualquer loja.
> Grave em `/tmp` e leia de lá, abortando com instrução clara quando o arquivo não existir.

### 3. Varrer nomes de rota com corpo vazio

Rota que existe reclama de parâmetro; rota que não existe devolve 404. Um `POST {}` em
quinze candidatas mapeia o servidor **sem criar registro nenhum** — é a varredura mais
barata e mais segura que existe.

Ela também revela a arquitetura de graça: se o 404 é do Express e o erro é do Node, aquele
caminho `/datasnap/rest/...` de cara legada é atendido pelo backend Node, não por um
servidor Delphi separado.

### 4. Ler a lista branca de quem já fez

Script de sessão anterior que mexeu na mesma tabela é a melhor documentação que existe da
base — melhor que a base. A lista de colunas graváveis do
[`smoke-app.js`](../../../manuais/gestao-entregas/scripts/smoke-app.js) foi o que revelou
que `origem` **não é coluna que se grave**: ela não estava na lista, e ainda assim os
pedidos daquele lote apareciam como iFood.

O argumento que fechou a prova merece registro, porque é o formato de raciocínio a
procurar: aquele script pegava pedidos genéricos de um semeador e **só depois** decidia
qual receberia o selo de iFood e qual o de 99Food. O semeador não podia adivinhar a
distribuição — logo a origem só podia vir do selo.

## O que já está descoberto no BeeFood

### A origem do pedido é derivada

`origem` não é campo de entrada de rota nenhuma, e não é coluna que se grave. Ela sai do
identificador de plataforma que o pedido carrega em `_PreVenda`:

| Identificador preenchido | `origem` que a API devolve |
|---|---|
| `ifoodLocalizer` | iFood |
| `nnID` | 99Food |
| `keetaId` | Keeta |
| `aiqfomeId` | AIQFome |
| `filialIDOrigem` | Cardápio Digital |
| nenhum deles | Manual |

Consequência prática: **para o cartão mostrar o logo do canal, basta estampar o
identificador.** Não existe, e não precisa existir, rota que aceite `origem`.

### Qual rota grava o quê

| Rota | Quem usa | `origem` que grava | Aceita do corpo |
|---|---|---|---|
| `POST app3/api/venda2/salvar` | a tela `/delivery` | sempre **Manual** | itens, cliente, pagamento |
| `POST app/datasnap/rest/tmesa/pedido` | o cardápio público | sempre **Cardápio Digital** | itens, cliente, pagamento, frete — e **exige** o `Authorization: Basic` do cardápio |
| `POST app3/api/venda2/atualizaSituacaoDelivery` | o kanban | — | move entre AGUARDANDO / PREPARO / PRONTO / ENTREGA |

### A janela de tempo das telas de fila

A tela `/delivery` e o Painel para Entregadores pedem a listagem com uma **janela em
horas** no fim da URL, e essa janela olha a **criação** do pedido, não a última mudança de
situação. Pedido velho **não volta** para a tela mudando a situação dele. Medido: um pedido
das 00:18 não aparece com 6, 8 ou 12 horas, e aparece com 16.

Ou seja: cenário de fila se monta com pedido **novo**. Reaproveitar pedido de ontem não
funciona, e é uma hora perdida quando não se sabe disso.

## Degrau 4: escrever no banco sem risco

Três modelos prontos no repositório, e vale abrir o mais próximo do seu caso antes de
escrever linha nenhuma:

| Arquivo | Para que serve |
|---|---|
| [`marketplace-db.js`](../../../manuais/painel-entregador/marketplace-db.js) (#120) | estampa identificador de plataforma; é o menor e o mais fácil de copiar |
| [`smoke-app.js`](../../../manuais/gestao-entregas/scripts/smoke-app.js) (#111–#117) | nove cenários do app do entregador, com `preparar → conferir → limpar` |
| [`cenario.js`](../../../manuais/gestao-entregas/scripts/cenario.js) (#104–#110) | monta, move e conclui cenário do painel de Gestão de Entregas |

A estrutura vale para qualquer escrita. **Seis travas, e nenhuma é opcional:**

| Trava | Como | Por que |
|---|---|---|
| **Ensaio por padrão** | escreve só com `--gravar`; sem a flag imprime o SQL e sai | o contrário do padrão de ferramenta de banco, de propósito |
| **Lista branca de alvo** | empresa e filial **literais** no código | destravar exige editar o arquivo, não passar uma flag |
| **Lista branca de coluna** | `Set` com comentário em cada uma | é ela que impede erro de digitação virar escrita em coluna fiscal |
| **Sentinela de registro** | `WHERE ... CHARINDEX('[SMOKE-...]', Observacoes) = 1` | registro de verdade não tem o marcador, então o script não alcança um |
| **`UPDATE`, nunca `INSERT`** | o registro nasce pela rota do produto | inserir venda à mão produz registro incoerente |
| **Nada de credencial versionada** | variáveis de ambiente ou clone do backend | o repositório é público |

Três detalhes que já custaram tempo:

- **`CHARINDEX`, não `LIKE`.** Em T-SQL os colchetes de `[SMOKE-PAINEL]` são classe de
  caracteres: `LIKE '[SMOKE-PAINEL]%'` devolve **zero linha em silêncio**. Medido num lote
  em que o `LIKE` achou 0 e o `CHARINDEX` achou 11.
- **Marcador com prefixo ambíguo não casa.** `[SMOKE-PAINEL]` **não** é prefixo de
  `[SMOKE-PAINEL-ENTREGADOR]` — o `]` difere. Ao renomear um marcador, a limpeza tem de
  reconhecer os dois.
- **O comando de plano tem de funcionar sem banco.** Monte o SQL e imprima antes de exigir
  conexão. É o que permite conferir a ferramenta numa máquina sem acesso — e foi assim que
  o `marketplace-db.js` foi validado.

### Onde as credenciais moram

Dois caminhos, nesta ordem:

1. **Variáveis de ambiente** — `BEETECH_MSSQL_HOST`, `_USER`, `_PASSWORD`, `_DATABASE`,
   cadastradas em **Cursor Dashboard → Cloud Agents → Secrets**. Não depende do Bitbucket.
2. **Clone do backend** `beetech-server-node-2.0` (`src/config/execSQLQuery.js` e
   `node_modules/mssql`), que é onde host e senha já estão configurados.

> **O caminho 2 quebra sozinho.** Ele depende do `BITBUCKET_TOKEN` do ambiente, que já
> expirou mais de uma vez — e quando expira, o backend não clona e as credenciais somem
> junto. Secret novo só entra em **VM nova**, então renovar não desbloqueia a sessão em
> andamento. Prefira o caminho 1, e faça o script abortar com essa explicação em vez de um
> erro de módulo não encontrado.

## Roteiro completo, do zero ao print

```bash
# 1. o que a tela enxerga agora
python pedido_marketplace.py estado

# 2. criar os pedidos-base pela rota do produto (nascem AGUARDANDO)
python pedido_marketplace.py semear ifood 99food keeta aiqfome

# 3. ensaio da escrita: mostra o UPDATE e não grava
node marketplace-db.js estampar --pedidos <ids>

# 4. estampar de verdade
node marketplace-db.js estampar --pedidos <ids> --gravar

# 5. pôr nas colunas que a tela mostra
python smoketeste.py preparo <preVendaID>
python smoketeste.py pronto  <preVendaID>

# 6. conferir antes de fotografar
python pedido_marketplace.py estado

# 7. quando as fotos estiverem prontas
node marketplace-db.js limpar --pedidos <ids> --gravar
python smoketeste.py limpar
```

## O que nunca fazer

- **Fotografar dado inventado.** Se o cenário não existe, monte-o ou diga que não deu. Print
  desenhado em manual é o pior desfecho possível.
- **Finalizar pelo app um pedido estampado.** Identificador de plataforma que não existe do
  outro lado faz a baixa **tentar avisar o marketplace de verdade**.
- **`UPDATE` sem a sentinela do marcador.** Sem ela, um `preVendaID` digitado errado alcança
  pedido de cliente.
- **Versionar credencial farejada da rede.** Ela não é da sandbox, e o repositório é público.
- **Deixar lixo na fila.** Cenário montado tem comando de limpeza, e ele roda no fim. O que
  não se apaga, o próximo manual fotografa por engano.
- **Ação destrutiva sem confirmar com o dono.** Passo irreversível pede a técnica do ensaio:
  rodar o fluxo sem o clique final, revisar, e só então repetir para valer.

## Memória

Aprendizado de **captura** (espera de spinner, conta de teste, comportamento de tela)
continua na
[`MEMORIA-GERAL.md`](../manual-sistema/references/MEMORIA-GERAL.md) da skill de manual.
Aqui fica o que é de **cenário**: de onde um campo vem, qual rota grava o quê, e como
escrever no banco sem risco. Quando um cenário novo for montado, o registro entra nesta
página — é ela que evita repetir a descoberta.
