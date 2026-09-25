# MEMORIA.md — #122 Cupom e cashback no totem

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `totem-cupom-cashback.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

## Pedido do dono

O recorte de 22/09/2026, palavra por palavra: *"crm no totem: cupom de desconto
e cashback"*. Era um dos seis manuais do estudo inicial e virou **um dos três**
quando o dono pediu para agrupar e ser mais direto. Aprovado com *"pode fazer,
sem parar"*.

Plano do bloco: [`PLANO-TOTEM.md`](../../.cursor/skills/manual-sistema/references/planos/PLANO-TOTEM.md).
    10|
## Escopo

As **duas chaves** que ligam o CRM ao totem — canal *Totem* no cupom e
modalidade *Pedidos via Totem* no cashback — e o que o cliente vê por causa
delas. O eixo do manual é a tradução: **regra marcada no CRM vira frase na tela
do aparelho**.

Fica fora: o cadastro completo do cupom e do cashback (já são manuais), e a
venda no painel (#123).

    20|## O achado que dá o eixo do manual

O totem **não tem configuração de cupom nem de cashback**. Ao abrir, ele faz duas
chamadas e desenha o que vem:

```
GET /api/venda2/cupomDescontoAtivo/38311/0?tipo=totem
GET /api/totem2/filial/38311/39202/0
```

A resposta dos cupons traz `regras[]` **em texto pronto**, uma frase por regra do
cadastro. Foi isso que virou a tabela "de onde sai cada frase" — e o argumento do
    30|manual: cupom com muita regra vira parede de texto na frente de um cliente de pé.

## Estado do sandbox (BeeFood3 - Manual, 38311/39202)

- **7 cupons ativos** com canal *Totem* (de 13 no total). O selo do aparelho diz
  exatamente **7 CUPONS DISPONÍVEIS** — o número fecha com o filtro de canal do
  painel, e isso está dito no manual.
- Cashback: `cashBackAtivo`, `cashBackDeliveryTotem` ligados, **3% em todos os
  dias**, validade de **35 dias**, sem saldo mínimo de resgate.
- Cliente de teste **Teste Manual**, (15) 99999-8888, com **R$ 1,19** de saldo no
  dia da captura (o mesmo telefone de teste da `MEMORIA-GERAL`).
    40|- **Nada foi alterado** no CRM: o cenário que o manual precisava já existia.

Os cupons do sandbox foram um presente: `FIRST` (primeira compra, com selo
LOGIN), `SMS` (cinco regras de uma vez), `10%BEBIDA` (desconto restrito a setor),
`10%SETIVERBOX` (liberado por produto), `10%DINHEIRO` e `PIX15%` (restritos por
forma de pagamento). Dá para mostrar cada tipo de frase com dado real.

## Ensaio, e o que não foi feito

O roteiro do aparelho **para na tela de confirmação**: o cupom não foi aplicado e
nenhum pedido foi criado por este manual. Aplicar queimaria o contador de uso do
CRM e, nos cupons de 1 uso/cliente, gastaria o do cliente de teste. A venda real
    50|(paga em dinheiro) é do **#123**, e de lá vieram as telas de pagamento.

## Imagens (8)

Painel em 2160×1350; aparelho em 1080×1920.

| Arquivo | Conteúdo |
|---------|----------|
| `01-crm-cupons-canal-totem.png` | Lista do CRM filtrada pelo canal **Totem**, com as etiquetas de canal no cartão |
| `02-crm-cupom-canais-regras.png` | O modal do cupom: *Canais de Visibilidade* à esquerda e *Regras* à direita, na mesma tela |
| `03-crm-cupom-avancadas.png` | Configurações avançadas: formas de pagamento, modo da regra, setores e produtos |
    60|| `04-crm-cashback-modalidades.png` | Programa de cashback, validade e a modalidade **Pedidos via Totem** |
| `05-crm-cashback-percentual.png` | O percentual por dia da semana — o número que o totem anuncia |
| `06-totem-identificacao-cashback.png` | *"Insira seu telefone e ganhe 3% de cashback"*, Confirmar e Pular identificação |
| `07-totem-confirmacao-cupom-cashback.png` | Selo de cupons, saldo com **USAR**, e *"Você ganhará de cashback R$ 0,84"* |
| `08-totem-cupons-regras.png` | A lista dos 7 cupons com as regras em texto, e o selo **LOGIN** |

Duas correções feitas na anotação, que valem de lição:

- a primeira versão da 02 cortava a coluna **Regras**. Como as duas colunas são
  o assunto da seção, a captura passou a **rolar o modal** até deixar as duas
  visíveis, em vez de virar duas imagens;
    70|- o percentual do cashback ficava fora da 04. Em vez de esticar o recorte,
  entrou a captura 05, que é onde o número mora. Uma imagem a mais é melhor do
  que uma imagem que não prova nada.

Recortes: `PAGINA` (0, 86, 2160, 1290) com faixa branca no alto — o 86 tira o
fragmento do logotipo da barra superior sem comer as abas; `TOTEM`
(0, 88, 1080, 1920) tira a barra do aparelho, onde o logotipo retangular sai
cortado. O modal do cupom usa `pad_right`, porque os interruptores ficam no fim
da linha e a etiqueta precisa de espaço à direita.

## Decisões de texto
    80|
- Abre com a tabela das **duas chaves**: quem só quer ligar o recurso resolve em
  dez segundos.
- A tradução cadastro → frase virou **tabela própria**, no fim da seção 8. É o
  que o suporte vai usar quando o lojista perguntar "de onde saiu esse texto".
- **"Por que o cupom não apareceu no totem?"** é seção numerada, não item de FAQ:
  é a pergunta que mais chega, e ela pede uma ordem de conferência.
- Dito com clareza o que o cliente perde ao **pular a identificação**, porque é a
  causa silenciosa de "o cashback não funciona".
- **Saldo × ganho**: o manual separa os dois, porque a tela mostra os dois juntos
   90|  e o lojista confunde na hora de explicar ao cliente.
- O aviso de que o saldo é processado **na madrugada** vem da própria tela do
  cashback — sem isso o lojista acha que o crédito falhou.
- Frete Grátis não vale no totem: provado no código (`tipoDesc === 'FRET'`
  desliga e trava o canal), e está na FAQ e nos problemas comuns.

## Scripts

- `capturar.py` — etapas `cupons`, `cupom`, `avancadas`, `cashback`,
  `percentual` e `aparelho`. O roteiro do aparelho monta um One Burger, digita o
  telefone e a mesa e para na confirmação, passando pela lista de cupons.
   100|- `annotate.py` — setas em pixels da imagem já recortada.

Manha de captura: dentro do modal do cupom, `scrollIntoView({block:'center'})`
num texto conhecido é mais confiável do que calcular `scrollTop`.

## Status

Concluído — 8 imagens, manual, fluxo de código e prompt de publicação.
