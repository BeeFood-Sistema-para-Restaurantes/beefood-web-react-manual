# Roteiro e texto do carrossel

Quem lê é dono ou gerente de restaurante, no celular, entre dois pedidos. Ele não
procurou esse conteúdo: ele tropeçou nele. Isso define tudo abaixo.

## A novidade é matéria-prima, não roteiro

O texto publicado em `beefood.app/novidades` é registro de release: descreve o
**campo**, a **tela** e o **efeito**, na ordem em que o produto foi construído.
Carrossel não é isso. Recortar aquele parágrafo em oito pedaços e centralizar
cada pedaço num slide produz um changelog paginado, que ninguém arrasta.

O carrossel é uma **publicação nova, escrita a partir do fato**. Método:

1. **Extraia o fato.** Em três linhas, sem adjetivo: o que mudou, onde fica, o
   que passa a acontecer, e qual o limite. Isso vem da novidade e do manual.
2. **Ache o ângulo.** Qual cena reconhecível do restaurante esse fato toca? A
   bebida que fica na geladeira. A comanda que ninguém sabe se saiu. O custo que
   entra duas vezes no DRE. O ângulo é o que o leitor já viveu — não o recurso.
3. **Escreva da cena para a tela**, nunca o contrário. O nome do campo aparece
   quando o leitor já quer saber onde fica: slide 4, não slide 1.
4. **Nenhuma frase sobrevive igual.** Se uma frase do carrossel também está no
   texto da novidade, ela não foi escrita — foi copiada. Reescreva.

O `roteiro.md` registra as três etapas numa tabela **fato → ângulo → o que o
slide diz**. Isso é o que permite a outra pessoa auditar a reescrita: ela vê que
nada foi inventado, e vê que nada foi copiado.

### Exemplo

| Fato (da novidade) | Ângulo | O que o slide diz |
|--------------------|--------|-------------------|
| Campo novo "Destaque na impressão" no cadastro de produto e complemento | todo mundo tem uma gambiarra caseira para não esquecer a bebida | "Toda loja tem uma gambiarra para não esquecer a bebida" |
| A linha sai com fundo escuro e letra clara | o cupom trata todas as linhas igual, e por isso a bebida some no combo | "Um esquecido custa duas viagens" |
| Usar com critério; marcar tudo anula o efeito | destaque funciona por contraste | "Se tudo é destaque, nada é" |

## A regra do primeiro segundo

O slide 1 não anuncia a funcionalidade — ele nomeia **um incômodo que a pessoa
já teve** — e leva **uma imagem**. Capa só de texto perde para capa com imagem, e
a imagem certa é o resultado da novidade (o papel impresso, a tela nova), não um
ícone decorativo.

| Em vez de | Escreva |
|-----------|---------|
| "Novo campo Destaque na impressão" | "Toda loja tem uma gambiarra para não esquecer a bebida" |
| "Nova etapa Pronto no Delivery" | "Quem está pronto não é quem já saiu" |
| "DRE: controle Considerar Custo Vendas" | "Seu custo está entrando duas vezes no DRE" |

Teste rápido: leia só o slide 1 em voz alta. Se soa como changelog, reescreva.

## Estrutura que funciona (6 a 8 slides)

1. **Capa** — o incômodo em no máximo oito palavras, com imagem.
2. **O custo** — o que acontece quando o problema acontece. É aqui que o leitor
   se reconhece. Custo em cena concreta ("alguém sai de novo no meio do pico"),
   não em número inventado.
3. **A virada** — o que muda, mostrado. Antes × depois é o slide mais
   compartilhado do carrossel.
4. **Onde ligar** — mockup de computador com o caminho de menu e o realce no
   campo.
5. **O atalho** — como fazer em vários itens de uma vez, quando existir.
6. **Até onde vai** — o efeito nas outras pontas (cozinha, entregador, cliente).
7. **O limite** — o erro comum. Slide que gera confiança porque não vende.
8. **CTA** — um pedido só.

Não é camisa de força. Melhoria pequena cabe em quatro slides, e forçar oito
produz slide vazio — que é pior do que carrossel curto.

## Ritmo de imagem

Pelo menos metade dos slides tem imagem, e a capa nunca fica de fora. Três
slides de texto seguidos é sinal de que dois deveriam virar um.

## Escrita

- Frase curta. Ponto final em vez de vírgula.
- Verbo no imperativo na instrução: "filtre o setor", "grave com SALVAR E SAIR".
- Termo da tela em **negrito**, exatamente como aparece no sistema. Se o sistema
  escreve "Editar em Lote", não escreva "edição em lote".
- Caminho de menu na classe `.caminho`: `Cardápio → Produtos`. Um por slide; duas
  pílulas de caminho na mesma frase viram um bloco colorido difícil de ler.
- Número sempre `1.`, `2.`, `3.`.
- Emoji: no máximo um por slide, e só se a novidade publicada já usa aquele.
- Nada de "revolucionário", "incrível", "poderoso". O ganho concreto convence
  mais: "a equipe vê de longe o que conferir".
- **Número só se ele existir.** "Reduz 30% dos erros" não está na novidade nem no
  manual: é invenção, e invenção em post de produto volta como reclamação.

## Legenda de publicação

Vai no fim do `roteiro.md`, pronta para copiar:

- Primeira linha repetindo o gancho — é o que aparece cortado no feed.
- Dois ou três parágrafos curtos: o que é, onde liga, qual o limite.
- Fechamento apontando o manual dentro do sistema, quando existir.
- Cinco a seis hashtags, sem empilhar trinta.

## Checagem antes de renderizar

- [ ] Existe a tabela **fato → ângulo → slide** no `roteiro.md`.
- [ ] Nenhuma frase do carrossel aparece igual no texto da novidade.
- [ ] O slide 1 tem imagem.
- [ ] Cada slide tem **uma** ideia; o título do slide diz qual.
- [ ] Toda afirmação está no texto da novidade ou no manual — ou foi conferida
      na tela.
- [ ] Nenhum número aparece sem fonte.
- [ ] Todo slide com tela desenhada leva `.selo-ilustracao`.
- [ ] O CTA pede uma coisa só.
- [ ] Os pontos do rodapé marcam a posição certa do slide.
- [ ] Nenhum nome, telefone ou e-mail de cliente aparece em nenhum print.
