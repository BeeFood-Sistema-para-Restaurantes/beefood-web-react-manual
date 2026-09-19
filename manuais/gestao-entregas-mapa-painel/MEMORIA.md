# MEMORIA — #105 Ler o mapa e o painel de entregas

## Estado

**Concluído** em 18/09/2026. 7 imagens. Primeiro manual do bloco **Gestão de Entregas 2.0**
e pré-requisito de leitura dos outros.

## Recorte

Este manual **só ensina a ler**. Toda ação (criar rota, despachar, dar baixa, configurar
despacho) foi tirada daqui e vive em manual próprio. A decisão veio de uma constatação
simples: a Gestão de Entregas é uma tela única que faz cinco coisas, e um manual de tela
inteira viraria trinta imagens que ninguém lê até o fim.

O preço disso é a **dependência cruzada**: cinco manuais que só fazem sentido lidos em
ordem. Daí a tabela *Onde continuar* no fim, e daí os outros quatro começarem dizendo que
pressupõem este.

## O que foi medido, e não suposto

| Afirmação do manual | Como foi confirmada |
|---------------------|---------------------|
| O despacho automático depende da tela aberta | texto da própria janela + `13-despacho-automatico.md` |
| "há N min" é idade da **posição**, não do toque | `entregadores[].posicaoIdadeMinutos` no `GET /painel` |
| Distância é em linha reta | Haversine no back; conferido contra dois pontos conhecidos |
| Pedido sem coordenada não vai ao mapa | `resumoPedidos.semLocalizacao` |
| Não há como o painel pôr alguém disponível | varredura das rotas de `gestaoEntregasRota.ts` — só o app tem `POST /presenca` |
| A rota fecha sozinha na última baixa | observado: ao marcar a 3ª parada, a rota saiu da lista e o entregador voltou a `DISPONIVEL` |

## Cenário

Montado por `manuais/gestao-entregas/scripts/cenario.js`. Para a captura deste manual:
nove pedidos em três situações, dois entregadores disponíveis com posição recente e
**nenhuma rota** — o painel em repouso, que é o estado que o leitor vê antes de aprender a
mexer.

**Limpar a rota fantasma antes de capturar.** O sandbox tinha o entregador `194115`
apontando para a rota `120`, que já não existia. Efeito: ele nunca aparecia como disponível,
e a lista de entregadores da janela de criar rota sairia mentindo. `limpar-fantasma` resolve
em um comando, e vale como primeiro passo de qualquer sessão.

## Técnica nova: coordenada de seta a partir do DOM

**As setas deste manual não foram medidas em grade.** A captura sai em 2160×1350 (viewport
1440×900 com `device_scale_factor=1.5`), então **pixel da imagem = coordenada CSS × 1,5**.
O script de captura grava, junto de cada pura, um `*.geo.json` com o
`getBoundingClientRect()` de cada alvo no instante do print, já convertido. O `annotate.py`
lê esse arquivo.

Resultado medido neste manual: **as setas nasceram no lugar em todas as capturas**, contra
cerca de 80% da grade, e caiu a zero o número de imagens de conferência geradas. Onde a
grade ainda ganha é em **alvo sem elemento próprio** — o pino do Leaflet, que não tem caixa
(`w=0, h=0`), e a etiqueta do número, que depende de onde há espaço vazio e continua sendo
decisão de quem escreve.

Duas correções que a técnica exigiu e que valem para o próximo manual:

1. **Contêiner alto engana.** O cabeçalho *Disponível (1)* da lista de entregadores é o
   elemento que envolve o grupo inteiro (490 px de altura). Mirar o centro punha a seta na
   terceira linha do grupo, apontando para o entregador errado. Daí o `borda='topo-esq'` e o
   `altura='topo'` na etiqueta.
2. **Duas etiquetas no mesmo ponto.** O número do selo *em preparação* e o do botão
   *Centralizar mapa* caíram sobre a mesma coordenada, e um cobriu o outro. A saída não foi
   empurrar um deles: foi **tirar os selos da imagem inteira** e dar a eles um recorte só,
   com espaço embaixo para as quatro etiquetas.

## Detalhes de captura deste painel

- **`dispatch_event("click")`, não `click()`.** O Leaflet ocupa a metade esquerda e o
  Playwright recusa boa parte dos controles com *element is not visible*.
- **Esconder o mapa para fotografar janela, e mostrar de novo em seguida.** No headless o
  Leaflet compõe **sobre** o modal e a janela sai em branco. Sem o "mostrar de novo", a
  captura seguinte sai com um retângulo branco no lugar do mapa — dois prints foram perdidos
  assim.
- **O `aria-label` não é confiável aqui.** Os cards e o rodapé têm rótulo acessível no
  primeiro render e perdem depois que a lista remonta (o painel se atualiza a cada poucos
  segundos). Localizar por **texto** é o que aguenta a sessão inteira.
- **O pino do pedido não abre balão.** Tentar clicar nele não rendeu nada; a informação do
  pedido está no cartão da lista, e foi assim que o manual ficou.

## Decisões de texto

- **"Selo", não "chip".** É o que o lojista chamaria de etiqueta colorida.
- **Não falar de rota de API, tabela nem cron.** Tudo isso está no `fluxo-codigo.md`.
- **A janela de ±6 h entrou** como tranquilidade, não como aviso: o lojista precisa saber
  que pedido velho sai da tela sozinho.
- **O aviso da tela aberta foi repetido três vezes** (seção 1, seção 3 e Dicas). É o único
  comportamento da tela que tem consequência silenciosa: com o painel fechado, o despacho
  automático simplesmente não acontece, e nada avisa.

## Pendências

Nenhuma para este manual. O que ficou de fora entrou nos manuais seguintes do bloco.
