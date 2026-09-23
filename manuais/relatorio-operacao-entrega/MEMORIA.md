# MEMÓRIA — Relatório Operação de Entrega

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `relatorio-operacao-entrega.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

Pasta: `manuais/relatorio-operacao-entrega/` · Escrito em 18/09/2026 na sandbox
**BeeFood3 - Manual** (`empresaID 38311`, `filialID 39202`).

Não estava na lista original de 14 manuais do bloco. Entrou por pedido do dono:

> *"relatorios: analise de entregas -> desempenho -> operacao de entrega (vai lançar junto com
> gestao entregas 2.0) ja esta disponivel paa empresa 38311 -> filtre a data de hoje com base
> no que foi feito no manual para ver os dados"*

E é o manual que fecha o ciclo do bloco: os quatro manuais do painel ensinam a operar, este
ensina a **ler o resultado do que foi operado**. O filtro em *Hoje* é o pedido literal do dono
— as 13 entregas das fotos são as rotas `A` dos manuais #106 a #109.

## O recorte

O relatório tem nove blocos e uma aba de dados crus. Poderia render três manuais (tempos,
prazos, mapa) e não deveria: é uma tela, uma pergunta — *onde o tempo se perde*. O manual segue
a ordem da tela de cima para baixo, porque a tela já foi desenhada nessa ordem.

Duas seções que não são "onde clicar" e ficaram de propósito:

- **As regras de leitura** (traço ≠ zero, mínimo de 20, cobertura). Sem elas o lojista lê
  *Poucos pedidos* como defeito e abre chamado.
- **O aviso do *Confirmar*** no seletor de período. Custou duas rodadas de captura: escolher
  *Hoje* sem confirmar deixa a tela nos 30 dias, e eu capturei assim antes de perceber.

## O que a captura descobriu

1. **O cartão *Taxas do entregador* fica em traço mesmo com valor gravado.** Pus R$ 3,50 em
   três pedidos do dia, entreguei os três, e o cartão não mudou — enquanto o relatório
   *Entregador (Taxa / KM)* mostrou R$ 10,50 no mesmo dia. Está registrado com detalhe em
   `fluxo-codigo.md`. O manual não afirma causa: descreve o traço e manda fechar pagamento no
   relatório vizinho.
2. **Duas contagens diferentes de "entregas" entre relatórios vizinhos**: 13 aqui (pedido
   entregue) e 15 no Taxa/KM (pedido de entrega do período, com ou sem entregador). Não é bug,
   é recorte diferente — mas quem compara os dois sem saber acha que um está errado.
3. **A divisão loja × rua não apareceu**, e o bloco explica a ausência em vez de desaparecer.
   Boa decisão de produto, e virou aviso no manual.
4. **Quase toda média ficou em *Poucos pedidos*.** Com 13 entregas num dia e mínimo de 20, é o
   comportamento correto — e é também o que a maioria das lojas pequenas vai ver. Manter as
   fotos assim é mais honesto do que forçar volume artificial.
5. **O mapa é por tempo, não por volume.** Ele é vizinho do *Mapa de Calor* (que é volume) e a
   tela avisa isso no subtítulo. O manual repete, porque a confusão é natural.

## Capturas

Dez fotos, todas do relatório em `Hoje (1 dia)`, menos a 02, que mostra o seletor aberto por
cima dos 30 dias:

| Foto | Bloco |
|---|---|
| `01-menu-delivery` | o caminho no menu |
| `02-periodo-hoje` | seletor de período |
| `03-kpis` | os seis indicadores |
| `04-metricas-tempo` | as quatro etapas + loja × rua |
| `06-prazos` | os quatro cartões de prazo |
| `08-por-hora` | o gráfico por hora (sem seta — gráfico) |
| `09-mapa` | o mapa e suas escolhas |
| `09b-mapa-bairros` | a tabela por bairro |
| `10-filtros` | a janela de filtros |
| `11-dados` | a aba Dados |

Três armadilhas de captura que vão doer se esquecidas:

- **Roda do mouse sobre o mapa dá zoom, não rolagem.** A primeira rodada produziu duas fotos
  do mapa aberto no mundo inteiro. A rolagem tem de ser `scrollIntoView` no contêiner
  (`.overflow-y-auto.thin-scrollbar`), pelo texto do bloco.
- **A tela mora num `<iframe>`.** A geometria medida dentro dele é relativa ao frame; sem somar
  a origem do iframe, toda seta cai ~150 px acima e ~330 px à esquerda. Resolvido em
  `alvos.medir_frame`.
- **Rótulo repetido casa fora da tela.** "Bairro", "Tempo de rua" e "Pedidos" existem em vários
  pontos da coluna rolável de 4.000 px; a primeira medição mandou seta para `y=4280` numa imagem
  de 1.350 px. Resolvido com `igual_visivel` (só considera o que está dentro da janela).

## O cenário

Não foi montado para este manual: é o **rastro** dos manuais #106 a #109 — 15 pedidos do dia,
13 entregues em duas rotas `A` (uma manual, uma automática), um entregador. Foi por isso que
este manual ficou por último no bloco do painel: ele precisa que os outros tenham acontecido.

Os horários dos pedidos semeados têm uma inconsistência de fuso (pedido gravado em UTC, evento
de rota em hora local), o que empurra algumas etapas para *não medido*. Não é comportamento do
relatório, é limitação do pedido semeado — e ela **não aparece** nas fotos escolhidas.

## Se for mexer neste manual

- Se recapturar com outro volume, revise as frases de *Poucos pedidos*: com 20+ pedidos os
  cartões mostram minutos, e as tabelas de seta mudam de conteúdo.
- O bloco **Por loja** não existe nas fotos porque a sandbox tem uma filial só. Em rede, ele
  aparece entre *Evolução* e *Por hora do dia*.
- O gráfico **Evolução** foi deixado fora: com período de um dia ele tem um ponto só e não
  ensina nada. Entra se o manual algum dia mostrar 30 dias.
