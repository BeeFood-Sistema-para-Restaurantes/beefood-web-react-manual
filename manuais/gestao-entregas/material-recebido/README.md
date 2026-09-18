# Material recebido — Gestão de Entregas 2.0

Conteúdo **pronto, feito fora deste repositório**, que o dono enviou em **18/09/2026** por
WeTransfer para servir de base ao manual da Gestão de Entregas (`manuais/gestao-entregas/`).

**Isto não é manual publicável.** É matéria-prima: fica aqui como fonte e como registro do que
já foi apurado, para o manual não repetir trabalho nem contradizer o que já foi medido. O que
sair daqui para o manual passa pelo padrão da casa (imagem em `imagens-tratadas/`, seta verde
numerada, prompt de publicação).

| | |
|---|---|
| Origem | WeTransfer enviado pelo dono em 18/09/2026 (`wetransfer_manual-gestao-entregas-2_2026-09-18_1418.zip`, 18 MB) |
| Produzido em | 17 e 18/09/2026, fora deste repositório — máquina Windows do dono, com emulador Android |
| Pasta | [`app-entregador/`](app-entregador/) — o pacote como veio, com 3 correções pontuais (seção 4) |
| Volume | 152 arquivos: 15 capítulos, 63 prints, 4 documentos de estudo, 2 apêndices e 5 scripts |

## 1. O que tem dentro

`app-entregador/` é um **manual completo do app do entregador**, tela por tela, em 15
capítulos. Cada capítulo traz o `manual.md` do fluxo, os prints em `prints/` e **um arquivo de
explicação por print**. O [`README.md`](app-entregador/README.md) do pacote é o índice.

| Pasta | O que é |
|---|---|
| `01-primeiros-passos/` … `15-ajustes-e-sair/` | os 15 capítulos: permissões e login, disponibilidade, lista, detalhes, mapa, rota do restaurante, melhor rota, código de barras, iFood, 99Food, cobrança na porta, divisão de conta, finalizar sem cobrar, histórico, ajustes |
| `apendices/` | notificações e "o que o app não faz" |
| `estudo/` | os bastidores: o que o app faz hoje, a evolução por commits e os cenários — é aqui que estão os achados técnicos |
| `smoketests/` | como recriar cada cenário: scripts PowerShell do emulador e o gerador de EAN-13 |

**O pedido-padrão do material é sempre o mesmo:** `1x Combo One Burger` (One Burger + batata
frita + Coca Cola 350ml). É de propósito — muda a forma de pagamento, a situação, o
complemento, e o leitor reconhece o pedido de um capítulo para outro.

## 2. O que ele resolve, e o que ainda falta

O manual da Gestão de Entregas tem **três partes** (o escopo está na
[`../MEMORIA.md`](../MEMORIA.md)). Este material cobre uma delas por inteiro:

| Parte do manual | Este material entrega? |
|---|---|
| App do entregador (Android/iOS) | **sim, por inteiro** — 15 fluxos, 63 prints de aparelho real |
| Mapa da Gestão de Entregas no painel | **não** — só aparece de lado, no capítulo 06, como "o outro lado" da rota |
| Juntar as peças (operador ↔ entregador) | **não** — é o trabalho que sobra |

Os prints do app **não têm como ser refeitos neste Cloud Agent**: eles saíram de um emulador
Android (`Pixel_7_Pro`, Android 15) na máquina do dono, e os `smoketests/` são PowerShell. Para
o app, este pacote é a **única** fonte de imagem disponível aqui — trate os prints como
`imagens-puras` já capturadas.

## 3. Achados do material que valem para o manual inteiro

Vindos do `estudo/`, medidos e não supostos:

- **Não existe ambiente de desenvolvimento no backend da Gestão 2.0.** Host, usuário e senha
  são fixos no código e apontam para os RDS de **produção**. Todo cenário criado por script é
  escrita em produção, protegida apenas pela lista branca literal `38311 / 39202`.
- **A lista de entregas do app vem ordenada pela distância da loja**, não por ordem de chegada
  do pedido. Quando o restaurante monta uma rota, a ordem passa a ser a que ele definiu.
- **Cobrança na rua exige caixa aberto na filial**, senão o `POST /gestao/entregador/pagamento`
  é recusado antes de qualquer escrita.
- **O entregador de teste da filial tem telefone cadastrado — o da própria loja.** Associar
  rota a ele **enfileira WhatsApp "nova entrega"**. É a armadilha a evitar ao montar cenário.
- **O app fala com duas APIs**: `app.beetechapi.be` (login, 2.0) e `app3.beetechapi.be`
  (entregas, pagamento e histórico, 3.0).
- **Referência técnica do módulo mora em outro repositório:** `beetech-server-node-3.0`, pasta
  `docs/gestao-entrega-2.0/`. **Não temos esse repositório aqui** (nem por clone: o
  `BITBUCKET_TOKEN` do ambiente não autentica mais). Se ele for necessário, o caminho é o mesmo
  deste material — o dono envia a pasta.

## 4. O que eu mudei no pacote

Só o que estava quebrado. **Nenhum texto foi reescrito e nenhum print foi alterado.**

| Onde | O que era | O que ficou |
|---|---|---|
| 5 links entre capítulos | `../11-cobranca/`, `../09-ifood/`, `../10-99food/`, `03-confirmar-sair.md` | os nomes de pasta e arquivo que existem de verdade |
| 2 links do `estudo/` | apontavam para `../../../../beetech-server-node-3.0/docs/…` | referência em código, porque o repositório não existe aqui |
| 1 imagem do `estudo/` | `evidencias/00-captura-de-validacao.png`, que não veio no pacote | nota dizendo que falta, apontando o print equivalente do capítulo 01 |

Depois disso, os **255 links** do material resolvem — nenhum quebrado.

## 5. Dado pessoal: conferido antes de versionar

Os prints mostram **Destinatário: Ana Beatriz Moraes** e **Rafael Monteiro Dias**. Este
repositório é público, e a regra da casa é cobrir nome de cliente até na imagem pura — então o
nome foi conferido na base do sandbox antes de subir, em *Cadastros → Clientes*:

- os dois nomes aparecem **repetidos várias vezes**, com **telefone e e-mail vazios** e origem
  *Delivery Manual*, criados entre 30/08 e 17/09/2026 — assinatura de cliente **semeado por
  script**, e o próprio `estudo/` confirma que o telefone do cliente é nulo nos pedidos
  semeados;
- cliente de verdade na mesma base sai diferente: nome parecido, mas **com telefone**.

**Conclusão: são clientes sintéticos, e os prints podem ser versionados como estão.** Se o dono
preferir cobrir mesmo assim, o caminho é o `blur=` do `annotate.py`, como no `caixa-fechar`.
