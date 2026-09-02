# Manual — Classificação RFV

O BeeFood **classifica sozinho** cada cliente em um grupo — Campeão, Fiel, Em risco,
Perdido… Você **não escolhe** o grupo na ficha. O que você configura são os **limites**
que o sistema usa para dar as notas de 1 a 5.

Essas notas viram o grupo. O grupo entra na **segmentação**. E a segmentação é o
público das **campanhas inteligentes** (e também das campanhas de WhatsApp e SMS).

Este manual explica:

1. O que são R, F e V
2. Os 11 grupos
3. Como editar os limites
4. Onde a classificação aparece (lista e ficha)
5. Como ela chega na segmentação e na campanha — o básico; o detalhe já está nos
   manuais de [Segmentação de clientes](../segmentacao-clientes/segmentacao-clientes.md)
   e [Campanhas Inteligentes](../campanhas-inteligentes/campanhas-inteligentes.md)

> As imagens têm **setas numeradas** (1, 2, 3…). Cada número indica o campo
> correspondente na tela.

---

## Onde encontrar

No menu lateral, abra **Clientes**.

![Menu lateral com o item Clientes](imagens-tratadas/01-menu-clientes.png)

1. **Clientes** — a classificação RFV mora aqui, não em Configuração → Parâmetros

No topo da lista estão o botão **RFV**, o ponto de interrogação da ajuda e os chips
de cada grupo.

![Lista de clientes com o botão RFV e os chips](imagens-tratadas/02-lista-rfv-chips.png)

1. **RFV** — abre a tela para editar os limites das notas 1 a 5
2. **?** — explica os 11 grupos (Recência × FV)
3. Os **chips** — um por grupo que tem pelo menos um cliente; clique para filtrar a lista
4. O **emoji** na linha — o grupo daquele cliente

O chip só aparece quando aquele grupo tem alguém. Na loja da imagem não há Campeão
nem Novo Cliente, então esses chips não mostram.

---

## O que o sistema mede

Três notas, cada uma de **1 (baixo) a 5 (alto)**:

| Letra | Nome | O que mede | Nota 5 significa |
|-------|------|------------|------------------|
| **R** | Recência | Dias desde o **último pedido** | Comprou faz pouco tempo |
| **F** | Frequência | **Quantidade de pedidos** | Pediu muitas vezes |
| **V** | Valor | **Ticket médio** dos pedidos | O pedido médio é alto |

O grupo **não** usa as três notas soltas. O sistema junta F e V numa nota só,
chamada **FV** — a média arredondada das duas. Depois cruza **R × FV** e cai num
dos 11 grupos.

---

## Os limites das notas

Clique em **RFV**. Esta é a única tela em que você mexe.

![Editar Parâmetros RFV](imagens-tratadas/03-parametros-rfv.png)

1. **Recência** — até quantos dias desde o último pedido valem cada nota
2. **Frequência** — a partir de quantos pedidos vale cada nota
3. **Valor monetário** — a partir de qual **ticket médio** vale cada nota
4. **Resetar Padrão** — volta os números de fábrica da BeeFood

A loja da imagem está no padrão:

| Nota | Recência (dias) | Frequência (pedidos) | Ticket médio |
|------|-----------------|----------------------|--------------|
| 5 | até 5 | a partir de 12 | a partir de R$ 100,00 |
| 4 | 6 a 16 | 9 a 11 | R$ 80,00 a R$ 99,99 |
| 3 | 17 a 30 | 5 a 8 | R$ 50,00 a R$ 79,99 |
| 2 | 31 a 48 | 2 a 4 | R$ 30,00 a R$ 49,99 |
| 1 | acima de 49 | até 1 | até R$ 29,99 |

Ao mudar um limite, o vizinho se ajusta sozinho para não ficar buraco nem
sobreposição. Depois de **Salvar**, a classificação **não muda na hora**: o
sistema recalcula **uma vez por dia**. Espere até o dia seguinte para ver o
grupo novo na lista, na ficha e nas campanhas.

Não existe botão “recalcular agora”.

---

## Os 11 grupos

No **?** ao lado de RFV o sistema mostra cada grupo, com a faixa de R e de FV
e uma sugestão de ação.

![Ajuda da classificação RFV](imagens-tratadas/04-classificacoes.png)

1. **R** — a nota de recência (1 a 5)
2. **FV** — a média arredondada de Frequência e Valor
3. O **card do grupo** — quem entra e o que o sistema sugere fazer

A janela rola. Os 11 grupos, do mais urgente ao mais frio:

| Grupo | R | FV | Em uma frase |
|-------|---|----|--------------|
| 🚨 Não posso perder | 1 | 5 | Altíssimo valor, sumiu |
| 🔥 Em risco | 1–2 | 3–5 | Era bom cliente e está se afastando |
| ❄️ Hibernando | 2 | 2 | Sumiu e já comprava pouco |
| ❌ Perdidos | 1–2 | 1–2 | Praticamente inativo |
| ⚠️ Precisam de atenção | 3 | 3 | Mediano: pode melhorar ou piorar |
| 💤 Quase dormentes | 3 | 1–2 | Recência média, pouco pedido e pouco ticket |
| 🏆 Campeões | 5 | 5 | Comprou agora, pede muito e gasta bem |
| 💎 Fiéis | 3–5 | 4–5 | Cliente constante de bom valor |
| ⭐ Em potenciais | 4–5 | 2–3 | Comprou recente e ainda pode crescer |
| 🌱 Promissores | 4 | 1 | Compra recente, ainda pouco engajado |
| 🆕 Novos | 5 | 1 | Primeira compra bem recente |

**Em potenciais** e **Potenciais fiéis** são o mesmo quadrado — dois nomes para
o mesmo cruzamento. A lista pode mostrar qualquer um dos dois.

Você **não atribui** Campeão ou Perdido na mão. Se o grupo parece errado, o
caminho é rever os **limites** da tela RFV — e esperar o recálculo do dia.

---

## A ficha do cliente (só leitura)

Abra um cliente e vá na aba **Indicadores**. As notas e o grupo estão lá, sem
campo para editar.

![Aba Indicadores da ficha do cliente](imagens-tratadas/05-ficha-indicadores.png)

1. Aba **Indicadores**
2. O **selo do grupo** (aqui, Fiéis)
3. **Atualizado a cada 24h** — as notas não são ao vivo
4. **Recência** — nota da última compra
5. **Frequência** — nota da quantidade de pedidos
6. **Valor** — nota do ticket médio

O cliente da imagem tem Recência 4, Frequência 5 e Valor 2. A média de 5 e 2
arredonda para FV 4; com R 4 isso cai em **Fiéis**.

O círculo do Valor traz o rótulo “Total gasto”, mas a **nota** segue o
**ticket médio** da tela de parâmetros. Neste cliente o ticket é R$ 34,89
(nota 2) e o total de vendas é R$ 1.919,05 — se a nota usasse o total, seria 5.

---

## De onde a campanha pega o RFV

A campanha inteligente **não lê a classificação direto**. Ela lê uma
**segmentação**. A segmentação é que pode filtrar por grupo, por Recência, por
Frequência ou por Valor.

```
Limites RFV (Clientes → RFV)
        ↓  recálculo diário
Notas + grupo gravados no cliente
        ↓
Segmentação filtra por classificação / R / F / V
        ↓
Campanha inteligente (origem “Segmentação de clientes”)
```

### Na segmentação

Em **Food Marketing → Segmentação de Cliente**, ao montar um público, a
categoria **RFV** tem quatro filtros.

![Categoria RFV ao escolher o campo da segmentação](imagens-tratadas/06-segmentacao-rfv.png)

1. A categoria **RFV** (4 filtros)
2. **Classificação RFV (público)** — o grupo (Campeões, Fiéis, Perdidos…). Também
   dá para filtrar pela nota 1 a 5 de Recência, Frequência ou Valor

O passo a passo de criar o público, testar o tamanho e combinar E/OU está no
manual de [Segmentação de clientes](../segmentacao-clientes/segmentacao-clientes.md).

### Na campanha inteligente

Quatro das seis campanhas padrão falam com um **público de clientes**:
Recuperador de vendas, Cashback parado, Aniversário e Boas-vindas. No passo 1,
a origem do público é **Segmentação de clientes**.

![Passo 1 da campanha inteligente com o campo Segmentação](imagens-tratadas/07-campanha-inteligente-segmentacao.png)

1. **Origem do público** — aqui, Segmentação de clientes
2. **Segmentação** — qual público a campanha avalia todo dia

As de fábrica já vêm com um público da BeeFood (sumidos, aniversariantes,
cashback, novos). Esse público **pode** ser trocado por um seu que filtre RFV
— por exemplo, só **Em risco** ou só **Não posso perder**.

Carrinho abandonado e “Recebeu o cardápio e não pediu” disparam por **evento**,
não por segmentação: o RFV não entra.

O detalhe dos seis modelos, das variáveis e do anti-banimento está no manual
de [Campanhas Inteligentes](../campanhas-inteligentes/campanhas-inteligentes.md).

Campanha de WhatsApp em massa e campanha de SMS também usam segmentação (e a
de WhatsApp ainda pode montar a lista direto por RFV). Isso fica nos manuais
dessas telas.

---

## Relatório

Em **Desempenho → Clientes → Análise RFV** o sistema mostra a mesma
classificação em gráfico, na ordem de prioridade dos grupos. Não se edita
limite por lá — só se lê o resultado.

---

## O que lembrar

- O grupo é **calculado**. Não se marca Campeão na ficha.
- Você edita só os **limites** das notas 1 a 5, em **Clientes → RFV**.
- Depois de salvar, espere o recálculo do **dia seguinte**.
- A campanha inteligente usa RFV **através da segmentação**, não direto.
- Segmentação e campanha inteligente já têm manual próprio; aqui basta o elo.

---

## Referências internas

- Código: [`fluxo-codigo.md`](fluxo-codigo.md)
- Memória: [`MEMORIA.md`](MEMORIA.md)
