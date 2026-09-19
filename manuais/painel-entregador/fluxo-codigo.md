# O que o Painel para Entregadores faz de verdade — lido no código

Fonte: `beefood-web-react`, commit `63098fc` *"Restrinziu painel entregador"* (19/09/2026),
o commit que fechou o recurso. Tudo aqui foi conferido no código e, quando dá, medido na
API de produção da sandbox 38311/39202.

## Os arquivos

| Arquivo | Papel |
|---|---|
| `src/pages/PainelEntregador.tsx` | a rota `/painel-entregador`: valida sessão e permissão, escolhe desktop ou mobile |
| `src/components/painel-entregador/PainelEntregadorConteudo.tsx` | a tela: cabeçalho, busca, tema, as duas colunas |
| `src/components/painel-entregador/ColunaPainel.tsx` | uma coluna (título, bolinha de cor, contador, estado vazio) |
| `src/components/painel-entregador/CartaoPedido.tsx` | o cartão de um pedido |
| `src/components/painel-entregador/ModalDetalhePedido.tsx` | a janela de detalhe, somente leitura |
| `src/components/painel-entregador/ModalPainelEntregador.tsx` | o painel dentro de um modal (homologação/desenvolvimento) |
| `src/components/mobile/painel-entregador/PainelEntregadorMobile.tsx` | o mesmo conteúdo, com as colunas empilhadas |
| `src/hooks/usePainelEntregador.ts` | de onde vêm os pedidos e como são filtrados |
| `src/utils/painelEntregador.ts` | quem pode ver e como o painel abre |
| `src/components/apps/PainelEntregadorAppModal.tsx` | a janela de apresentação em *Aplicativos*, com o mockup |
| `src/data/appCategories.ts` | o card **Painel para Entregadores** na categoria **Entrega** |
| `src/hooks/usePermissions.ts` | a permissão do card e da rota |
| `src/index.css` | `.painel-tema-claro`, o tema claro escopado só ao painel |

## Quem vê, e como abre

`podeVerPainelEntregador()` (`src/utils/painelEntregador.ts`) tem **lista de empresas
liberadas** na fase de testes:

```ts
const EMPRESAS_PAINEL_ENTREGADOR = [107, 38311];
```

A sandbox dos manuais é a **38311**, então o recurso é capturável em produção. Fora
dessas duas empresas o item do menu do Delivery e o card de Aplicativos **não aparecem**
(`canViewApp('painel-entregador')` devolve `false` antes de olhar qualquer permissão).

Além da lista, vale a permissão: `'painel-entregador': { category: 'entrega', key:
'gestaoEntregas' }`. **É a mesma chave do mapa de Gestão de Entregas** — quem não tem o
mapa não tem o painel, e a própria rota redireciona para `/delivery` quando
`canViewApp('gestao-entregas')` ou `isAppEnabled('gestao-entregas')` é falso.

`abrirPainelEntregador()` decide a forma de abrir:

| Ambiente | O que acontece |
|---|---|
| Produção (`beefood.app`) | `window.open('/painel-entregador', '_blank')` — **janela nova**, para arrastar para a TV |
| Desenvolvimento / preview | modal em tela cheia (`ModalPainelEntregador`) na própria aba |

Ou seja: no dia a dia do lojista o painel **sempre abre numa aba nova**. A modal existe
para o time de produto testar sem perder a tela de trás.

**Dois caminhos até ele**, e os dois têm a mesma condição:

1. `/delivery` → menu dos três pontinhos → **Painel Entregador** (ícone de bicicleta). No
   celular é um botão de bicicleta no cabeçalho, não um item de menu.
2. `/aplicativos` → **Entrega** → card **Painel para Entregadores**. O clique **não** abre
   a tela: abre a janela de apresentação (`PainelEntregadorAppModal`), com mockup e o
   botão **ABRIR PAINEL (F2)**. No celular o botão vem desabilitado, com o aviso de abrir
   pelo computador.

## De onde vêm os pedidos

`usePainelEntregador()` **não tem endpoint próprio**. Ele reaproveita o
`useDeliveryPedidos` da tela `/delivery`:

```
GET /api/venda2/delivery/{empresaID}/{filialID}/{usuarioID}/6
```

O último parâmetro é a janela em horas, e está **fixo em 6**. Medido na sandbox: um pedido
criado às 00:18 não aparece com `horas` 6, 8 ou 12, e aparece com 16 — e **mover a
situação não o traz de volta**, porque a janela olha a hora em que o pedido foi criado,
não a da última mudança. Consequência prática para o manual: **o painel é do turno**, não
um histórico.

Três filtros, nessa ordem:

1. `tipoPedido === 'DELIVERY'` — retirada e consumo no local ficam fora. É o painel de
   **quem vai sair para entregar**.
2. `situacaoDelivery === 'PREPARO'` para a coluna da esquerda e `'PRONTO'` para a direita.
   Aguardando, Em entrega, Entregue e Cancelado não entram.
3. Ordem por `inicioEtapa` crescente — **o mais antigo em cima**, para quem espera mais
   aparecer primeiro.

O relógio da etapa vem de `dataHoraEmPreparo` (coluna Em preparo) ou `dataHoraPronto`
(coluna Pronto), com queda para `dataHoraPedido` quando falta o campo, lido por
`parseLocalDateTime` — sem conversão de fuso.

**Somente leitura.** O hook não chama nenhuma rota de escrita: nada no painel muda a
situação de um pedido.

## Como ele se atualiza

| Gatilho | Efeito |
|---|---|
| `setInterval` de **10 s** | recalcula os tempos e o alerta de atraso (só conta, não busca) |
| `setInterval` de **30 s** | `refetch()` da listagem — rede de segurança se o socket cair |
| WebSocket `DELIVERY_NOVO_PEDIDO` | `refetch()` imediato: pedido novo entra na hora |
| WebSocket `DELIVERY_SITUACAO_<id>_<situacao>` | `updatePedidoLocal` move o cartão de coluna **sem** ir ao servidor |

Por isso o cartão salta de *Em preparo* para *Pronto* no mesmo instante em que a cozinha
arrasta o pedido no kanban do Delivery.

## O cartão

```
#1043                      Em preparo há 11min
[logo]  9F23
[ref]   ────────────────────────────────
                    9F23
Restam 4 min
```

| Elemento | Campo | Regra |
|---|---|---|
| `#` pequeno, à esquerda | `numeroPedido`, com queda para `numeroPreVenda` | é o número **interno** do pedido no caixa |
| número grande | `ifoodShortReference` → `marketPlace` → `numeroPedido` → `numeroPreVenda` | marketplace manda o **seu** número; pedido próprio mostra o interno |
| logo | `getOrigemIcon(origem)` | iFood, 99Food, AIQFome, Rappi, DeliveryMuch, UaiRango, Keeta, Totem e Cardápio Digital têm ícone; **sem ícone cai na abelha do BeeFood** |
| texto embaixo do logo | `referenciaMarketplace` | só aparece quando é **diferente** do número grande |
| tempo, à direita | `Date.now() - inicioEtapa` | "Em preparo há Nmin" / "Pronto há Nmin" |
| borda e cor do tempo | `calcularAtrasoPedido` | amarelo ≥ 70% do prazo, laranja ≥ 85%, vermelho ≥ 100% |
| linha de baixo | `Restam Nmin` ou `Atrasado • Nmin` | agendamento atrasado sai como *Agendamento atrasado* |

O alerta de atraso é **o mesmo cálculo da tela `/delivery`**
(`src/utils/deliveryAtraso.ts`): compara o tempo desde `dataHoraPedido` com o prazo do
cabeçalho do delivery. Medido na sandbox em 19/09/2026:

```
GET /api/empresaDelivery2/cabecalhoDelivery/38311/39202/88711
{"deliveryTempoEntregaMinutos":45,"deliveryTempoRetiradaMinutos":25,
 "deliveryTempoEntregaMinutosMax":53}
```

Para delivery vale o **máximo** (53 min). Logo: amarelo a partir de ~37 min, laranja a
partir de ~45 min, vermelho depois de 53 min. Pedido **agendado** (com
`dataHoraRetirada`) usa a janela do pedido até o horário marcado, e não o prazo do
cabeçalho — é o que o texto do popover de informação na tela explica.

## O cabeçalho e o detalhe

- **Busca** por número, referência do marketplace, `preVendaID`, nome do cliente e origem.
  Ela filtra as duas colunas ao mesmo tempo.
- **Sol/lua** troca o tema do painel. O painel nasce com o tema do sistema
  (`next-themes`); o claro é escopado pela classe `.painel-tema-claro`, então mudar o tema
  do painel **não** mexe no resto do BeeFood.
- **ℹ️** abre o popover *Como o alerta de atraso é calculado*.
- **Contagem** por coluna no cabeçalho dela ("**3** pedidos").
- **Duas colunas internas** por etapa quando a tela tem **1500 px ou mais**
  (`LARGURA_MIN_GRADE_DUPLA`), com as fontes reduzidas para o texto não truncar.
- **Clicar no cartão** abre o `ModalDetalhePedido`: cliente, telefone, endereço,
  entregador, itens com opções e observação, totais e formas de pagamento. Ele chama
  `useVendaDetalhes` (`GET /api/venda2/vendaDetalhes/...`) e **não** reaproveita o
  `VendaDetalhes` do painel — é uma visão de fonte grande, sem nenhum botão de ação.

## O que o manual não pode prometer

- **Não há filtro por origem, por cardápio nem por entregador.** Só a busca.
- **Não há som, nem chamada de senha, nem tela cheia automática.** Quem põe em tela cheia
  é o navegador (F11).
- **Não há coluna de Aguardando nem de Em entrega.** O painel é de duas etapas.
- **O pedido de retirada não aparece**, mesmo pronto — o painel é dos entregadores.

## Achado do estudo da base: origem não é campo de entrada

Para montar o cenário de captura era preciso pedido de **iFood, Keeta, 99Food e Cardápio
Digital**, com cartões em preparo e prontos. A conclusão do teste, feita contra a API de
produção, muda o que o smoke teste pode montar:

- `POST /api/venda2/salvar` **grava sempre `origem = Manual`**. Foram testadas quatro
  posições para os campos de marketplace — na raiz, dentro de `delivery`, dentro de um
  `venda` aninhado e junto de `ifoodLocalizer`. Nas quatro o pedido nasceu, e nas quatro a
  listagem devolveu `origem: "Manual"`, `marketPlace: null`, `ifoodShortReference: null`,
  `keetaId: null`, `nnID: null`. O único campo que colou foi `filialIDOrigem`, e sozinho
  ele não muda a origem.
- Portanto `origem` é **gravada por quem recebe o pedido**: a integração do marketplace
  ou o cardápio digital. Pela tela do painel não há como forjá-la, e isso é bom sinal —
  significa que o ícone do cartão é confiável.
- Pedido com origem **Cardápio Digital** de verdade sai fazendo o pedido no cardápio
  público (`pedido_cardapio.py`). Pedido de **marketplace** exige o semeador do backend
  (`scripts/seed-gestao-entregas.js` do `beetech-server-node-2.0`), que escreve direto no
  `_PreVenda` — e o backend **não está clonado nesta máquina**, porque o
  `BITBUCKET_TOKEN` está inválido (as quatro combinações de usuário e token falham na
  autenticação).

O formato que o semeador antigo usou, lido na base pelos pedidos `[SEED-ENTREGAS]` de
19/09/2026, fica registrado aqui para quando o token voltar:

| Origem | Campos que a definem | Exemplo real da base |
|---|---|---|
| iFood | `marketPlace: true`, `ifoodShortReference`, `ifoodLocalizer`, `correlationId` | `"1851 - Coleta 3983"`, localizer `48731502` |
| 99Food | `marketPlace: true`, `nnID` **e** `ifoodShortReference` | `nnID 5764687241800647938`, ref `254023` |
| Keeta | `marketPlace: true`, `keetaId` | `keetaId 4900112233445566` |
| Cardápio Digital | `marketPlace: null`, `filialIDOrigem` preenchido, `usuarioID: null` | pedido do próprio cardápio |

O `nnID` tem precedência sobre o `ifoodShortReference`: o pedido do 99Food traz os dois e
a origem sai **99Food**.
