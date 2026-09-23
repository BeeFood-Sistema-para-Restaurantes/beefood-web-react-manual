# MEMÓRIA — #121 O cliente acompanha a entrega no mapa

Status: **concluído** em 23/09/2026. Pasta `manuais/gestao-entregas-rastreio-cliente/`,
7 imagens. O estudo do código está em [`fluxo-codigo.md`](fluxo-codigo.md).

## Pedido do dono

> *"Surgiu uma nova feature no gestão de entregas sobre o rastreio do cliente do pedido. Nesse
> caso você vai precisar fazer nenhuma simulação, apenas interpretar os arquivos anexos (imagens
> e readme.md). Pode atualizar o fonte do beetech-server-node-2.0 e usar a branch
> beefood-web-react pra entender melhor se quiser. Sendo assim, crie o manual sobre essa nova
> funcionalidade."*

E, no meio da produção: *"pode deixar o link da imagem do whatsapp aparecendo. Todas imagens são
dados falsos."*

Foi o **primeiro manual do repositório sem nenhuma captura própria**: o material chegou pronto —
oito imagens e um `README.md` que já era um rascunho do manual, na voz da casa.

## O que mudou em relação ao material recebido

O rascunho tinha oito seções e oito imagens. O manual tem sete seções e **sete imagens**, e as
diferenças são decisões, não esquecimento:

| Decisão | Por quê |
|---|---|
| **Fora: o detalhe do pedido no computador** (a oitava imagem) | Regra 0 das boas práticas de imagem: o leitor não sai dela fazendo nada diferente. A imagem 6 (tela cheia no desktop) já prova que funciona no computador, e o texto diz que é o mesmo link |
| **A folha de itens entrou como recorte**, não como tela inteira | Com a lista aberta o mapa sai da tela; a captura inteira mostraria pouco mapa e pouca lista. A folha sozinha se lê e continua reconhecível (alça, cartão do entregador, endereço) |
| **Seção nova: "O que a tela escreve em cada situação"** | Saiu do código, não do rascunho. É a tabela que o atendente consulta quando o cliente liga lendo uma frase |
| **Duas fronteiras novas na seção 2** | `cabeRastreio` no código: retirada não tem acompanhamento, presencial não tem, e pedido fora de andamento perde a linha |
| **O link expirado tem dois textos** | Medido, não deduzido — ver abaixo |

## O achado: link vencido não cai em "Este link expirou"

O token da captura (`.../rastreio/7Kq2XbVn4pHs9dTmRcJw1e`, 22 caracteres) foi sondado no mesmo dia
da entrega:

```
$ curl -s https://cardapio-digital.beetechapi.be/api/rest/tempresaDelivery/rastreio/7Kq2XbVn4pHs9dTmRcJw1e
{"encontrado":false}        HTTP 404
```

`Este link expirou` só aparece quando o servidor **ainda conhece** o token e responde
`expirado: true`. Quando ele já não conhece, o cliente vê `Esse pedido não tem rastreio`. As duas
frases estão no manual e no FAQ, porque quem atende o telefone vai ouvir as duas.

## Como o código foi lido, sem clone

O rastreio **não** está no `beefood-web-react` nem no `beetech-server-node-2.0`: ele mora no
cardápio digital, que é um Nuxt 2 em repositório separado. Tentei os dois tokens do Bitbucket nas
duas formas de usuário — as quatro combinações continuam respondendo *"You may not have access to
this repository"*, como a seção 8 da `MEMORIA-GERAL.md` já registrava desde 01/09.

A saída foi ler o **bundle publicado** de `menu.beefood.com.br`. Está tudo lá: rota, componentes,
as frases de todos os estados, o arredondamento da distância, o piso de 5 segundos do relógio e o
`noindex, nofollow`. O caminho para redescobrir os chunks (os hashes mudam a cada publicação) está
no começo do [`fluxo-codigo.md`](fluxo-codigo.md).

**Vale como técnica geral:** quando o manual é de uma tela do **cardápio público**, o código está
a um `curl` de distância, sem depender de clone nem de token.

## Capturas

As oito chegaram pelo chat, já no padrão da casa — celular **780x1688** (viewport 390x844 em
DPR 2) e computador **2000x1250**. São de um pedido real, feito e entregue em 23/09 no cardápio
`menu.beefood.com.br/beefood3`, com entregador percorrendo o trajeto.

| Imagem | O que mostra | Setas |
|---|---|---|
| `01-whatsapp-link.png` | a mensagem de *saiu para entrega* com o bloco **Acompanhe a entrega** | 3 |
| `02-pedido-em-preparo.png` | o pedido em preparo: barra, estado, aviso honesto e o mapa com loja e destino | 6 |
| `03-saiu-para-entrega.png` | o motoboy aparece: nome, distância e a moto no mapa | 5 |
| `04-mapa-tela-cheia.png` | a tela cheia no celular: voltar, cabeçalho, três pinos, folha | 6 |
| `05-itens-do-pedido.png` | recorte da folha, com a lista de itens aberta | 4 |
| `06-mapa-no-computador.png` | a tela cheia no computador, com o trajeto e o traço pontilhado | 6 |
| `07-pedido-concluido.png` | o ciclo fechado: data e hora, *Pedido concluído* e a avaliação | 3 |

O `annotate.py` traz as capturas do caminho de upload do chat (`~/.cursor/projects/.../assets`)
para `imagens-puras/` e recorta. **Esse caminho não sobrevive à sessão**, e é de propósito que o
script funcione sem ele: `preparar()` avisa e segue, usando a pura já versionada. Mesma regra do
`copiar-imagens.py` do #24 — o importador nunca escreve em `imagens-tratadas/`.

### O defeito que isso escondia: margem gravada na pura

A primeira versão copiava o `com_margem()` dos manuais do app, que **grava a margem dentro de
`imagens-puras/`**. Ali funciona, porque o material daqueles manuais é versionado
(`gestao-entregas/material-recebido/app-entregador`, 181 arquivos) e o `copiar()` reconstrói a pura
a cada execução — conferido: rodar o `annotate.py` do #111 duas vezes dá as 15 tratadas idênticas.

Aqui o material **não** é versionado, então a segunda execução não reconstruía nada: ela pegava a
pura que já tinha margem e acrescentava outra. Descoberto rodando o script com `MATERIAL` apontando
para uma pasta inexistente — as puras foram de 780 para 1026 px de largura e as tratadas para 1350,
com toda seta deslocada.

A correção é a regra geral: **pura é o print, e só.** A margem passou a ser montada dentro do
`annotate()`, a partir de `m` e `md`, e nada mais escreve em `imagens-puras/` depois do
`preparar()`. Agora as sete tratadas saem **byte a byte iguais** com ou sem o material na máquina,
e as puras não são tocadas.

**Onde isso morde de novo:** qualquer manual cujo material venha de upload de chat, e-mail ou pasta
temporária. Se a fonte não está versionada, a pura é a única fonte — e transformação que se acumula
sobre ela quebra a repetição.

Duas coisas de anotação que valem para o próximo manual feito de print de celular do **cardápio
público** (não do aplicativo):

- **A margem à direita foi necessária uma vez**, na imagem 03: a hora do despacho fica no canto
  direito da linha do estado, e alcançá-la pela esquerda traçava uma seta por cima de *"Pedido saiu
  para entrega"*. Com `md=0.13` a etiqueta vive fora da tela, à direita, e a seta entra pela borda.
- **Pino de mapa aceita seta na borda, texto não.** Nas quatro primeiras tentativas as pontas
  caíam sobre a primeira letra de *Pedido*, *Carlos*, *Acompanhe* e *1 item*. O alvo certo é o vão
  antes do texto (ou o ícone que abre a linha), e isso só aparece conferindo em tamanho real.

## Dados pessoais

**O dono liberou expressamente o print inteiro**, incluindo o link: os dados são falsos e o
ambiente é a sandbox. Por isso nada foi desfocado — nem o endereço, nem o código do link. Tinha
sido preparado um borrão sobre os 22 caracteres do token (a primeira versão das imagens saiu com
ele), desfeito depois do recado.

Se o material de um próximo manual vier de **loja real**, a decisão muda: aí vale a regra da seção
7 da `MEMORIA-GERAL.md`, e o que sai coberto é nome, telefone, e-mail — e, neste recurso, também o
**código do link**, que dá acesso ao endereço de entrega.

## Ambiente: o que foi alterado

**Nada.** Nenhum pedido criado, nenhuma situação movida, nenhuma escrita em banco. As únicas
chamadas de rede foram `GET`: o bundle do cardápio e duas sondagens da rota de rastreio (um token
inválido e o token da captura), ambas respondendo `{"encontrado": false}`.
