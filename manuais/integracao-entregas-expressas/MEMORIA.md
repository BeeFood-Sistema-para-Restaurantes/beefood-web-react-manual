# MEMORIA.md — #127 Entregas Expressas (integração pela API Aberta)

## O pedido

O dono mandou o artigo público do parceiro —
`ajuda.entregasexpressas.com.br/hc/articles/5/75/388/como-integrar-a-beefood-ao-entregas-expressas`
— e pediu: *"copie as imagens e o manual para a nossa estrutura… apenas modifique o caminho, é
possível cadastrar o webhook e credencial direto pelo Aplicativos → API Aberta dentro do
BeeFood. Estude e adapte pro nosso padrão."*

Então o manual **não** é tradução do artigo. O artigo ensina pelo portal de desenvolvedor
(`developer.beefood.com.br`); aqui o caminho é o painel. O resto — o que a integração faz, as
opções do lado do parceiro, o FAQ — vem dele, reorganizado no padrão da casa.

## O que o estudo do código mudou no texto, e por quê

O detalhe está no `fluxo-codigo.md`; o que importou para a escrita:

- **A troca de caminho corrige a armadilha, não só encurta o passo.** O artigo avisa em letras
  maiúsculas que o portal vem com *Sandbox* marcado e que credencial de teste não recebe pedido
  real. Pelo painel, `create` e `webhookSave` forçam `sandbox: false` no back-end, e as duas
  listagens escondem o que é de sandbox. **Não existe a escolha que se erra.** Isso virou o
  aviso que abre o manual e duas perguntas do FAQ.
- **A credencial principal já existe.** `chamar('main')` a traz pronta — o Passo 2 é copiar, não
  criar. O artigo tem um passo de criação que aqui é opcional, e virou o Passo 4 com o motivo
  certo (uma credencial por parceiro se desliga sem derrubar as outras).
- **O segredo não se perde.** O artigo diz que o `clientSecret` aparece *uma única vez*. No
  painel, o ícone de olho chama `GET /credentials/<id>/secret` e revela de novo. Foi a correção
  mais fácil de errar por copiar o artigo sem conferir.
- **Os nomes colidem no webhook.** O BeeFood rotula a autenticação Basic como
  `clientId (usuário)` / `clientSecret (senha)`; o que vai ali é o **Usuário** e a **Senha** do
  Entregas Expressas, não a credencial da API. Ganhou aviso no passo, na tabela e no FAQ,
  porque é o erro que o próprio rótulo convida a cometer.
- **Dois segredos diferentes na mesma tela.** O *Secret do webhook* que a BeeFood devolve ao
  salvar é dela, para quem recebe conferir a legitimidade do aviso; o parceiro não pede por ele.
- **O card não aparece para todo mundo.** `API_ABERTA_ALLOWED_EMPRESAS` tem **quatro** empresas
  (107, 38311, 5687, 11543). Virou pré-requisito e primeira linha da tabela de problemas — sem
  isso o leitor procura um botão que a conta dele não tem.
- **RECICLAR é o botão que derruba a integração** (*"todas as conexões atuais param
  imediatamente"*). Ganhou seta própria com aviso, e uma linha na tabela de problemas para o
  sintoma "parou de uma hora para outra".

## As imagens: duas pontas, duas origens

Onze tratadas, de nove puras. Cinco são nossas e quatro são do parceiro.

| Tratada | Origem |
|---|---|
| 01 a 04, 08 a 10 | capturadas em `beefood.app` pelo `capturar-painel.py` |
| 05 a 07, 11 | baixadas do artigo público pelo `importar.py` |

- **`02` e `03` saem da mesma pura.** O painel da API Aberta tem 1950 px de altura com a lista
  de oito permissões aberta; numa imagem só o texto fica ilegível na página publicada. Um print,
  dois recortes, via `saida=` no `annotate.py`.
- **Viewport alto só para o painel.** A tela de Aplicativos saiu no padrão (1440x900 em DPR 1,5);
  o painel precisou de 1440x1300 para o `SALVAR PERMISSÕES` e o `CRIAR CREDENCIAL` caberem na
  mesma captura. Com 900 de altura, os dois ficam abaixo da dobra e o manual precisaria de uma
  imagem extra só para mostrar botão.
- **Faixa clara dos dois lados**, não só à esquerda. O padrão do #101 põe a faixa à esquerda,
  e ela resolve as etiquetas de quem aponta texto. Mas o painel tem três elementos encostados na
  borda **direita** — o ícone de olho, o selo *Ativa* e o selo *Ativo* do webhook — e mirar neles
  da esquerda faz a seta atravessar o rótulo inteiro. Por isso `preparar()` ganhou margem nos
  dois lados, com `ESQ_PAINEL`/`DIR_PAINEL` nomeando onde cada etiqueta mora.
- **Telefone e e-mail saem cobertos na pura.** A captura do pedido no painel do parceiro trazia
  telefone e e-mail; o `importar.py` borra as três regiões **antes** de gravar a pura, porque a
  pura também é versionada. Os nomes ficaram: *ESTABELECIMENTO TESTE* e *Cliente Teste Entregas*
  são rótulos de teste do próprio artigo, e borrar o que é evidentemente falso só piora a imagem.
- **O `importar.py` precisa de `User-Agent` de navegador.** O servidor do parceiro devolve **403**
  para o agente padrão do `urllib` (o `curl` passava). Ele também **avisa e segue** quando não há
  rede: as puras versionadas bastam para rodar o `annotate.py`, e o manual não depende de o
  artigo continuar no ar.
- **Duas setas mudaram de lugar na revisão.** A do `segundos` em `07` mirava a borda do campo e
  atravessava a palavra *segundos.*; passou a mirar depois dela. E em `06`, as etiquetas de
  *Coleta*, *Forma de Pagamento* e *Tipo de Serviço* nasciam **fora** da imagem (os campos ficam
  no pé daquele print) — os três aparecem inteiros no print seguinte, e lá eles são citados.

## O cenário: o que foi mexido no sandbox, e como voltou

A conta é a **BeeFood3 - Manual** (`contato@beefood.com.br`), empresa **38311**, num BeeFood de
**produção**. Duas decisões para não deixar sujeira:

- **O webhook foi criado e apagado na mesma execução.** O manual precisa da tela com um webhook
  cadastrado e ativo. Deixá-lo de pé mandaria pedido real da loja para fora, então o
  `capturar-painel.py` apaga o que criou e confere que a lista voltou a *Nenhum webhook
  cadastrado* — a última linha que ele imprime é essa conferência. Nenhum pedido foi feito na
  janela em que ele existiu, então nada chegou a ser enviado. A URL é de exemplo
  (`https://webhook.entregasexpressas.com.br/beefood/exemplo`).
- **Credencial: nada foi criado.** O diálogo *Nova credencial adicional* entrou pela **técnica
  do ensaio** — abre, fotografa, cancela. Criar de verdade obrigaria a apagar depois, e apagar
  credencial numa empresa com integração ativa é risco sem ganho. As permissões também não foram
  tocadas: o `SALVAR PERMISSÕES` só habilita depois de uma mudança, e por isso a foto é segura.
- **O `Secret do webhook` visível na imagem 10 é de um webhook que não existe mais** — foi
  apagado na mesma execução. Fica versionado como qualquer credencial de sandbox.

Estado em que o sandbox ficou: igual ao de antes. Uma credencial principal e uma adicional, as
duas *Ativas*, e **nenhum** webhook cadastrado.

## Os arquivos desta pasta

| Arquivo | Para que serve |
|---|---|
| `integracao-entregas-expressas.md` | o manual |
| `fluxo-codigo.md` | o que a tela faz de verdade, lido no código (uso interno) |
| `texto-documentation.ia.md` | o prompt de publicação |
| `capturar-painel.py` | as cinco capturas do BeeFood (e o desfazer do webhook) |
| `importar.py` | as quatro capturas do artigo do parceiro, já com o dado pessoal coberto |
| `annotate.py` | setas e etiquetas das onze imagens |
| `conferir-setas.py` | confere se o texto e as setas falam a mesma coisa |

Para refazer tudo, nesta ordem: `importar.py` → `capturar-painel.py` → `annotate.py` →
`conferir-setas.py`.

## O que ficou para depois

- **A aba Avançado não entrou.** *Aplicativos conectados* lista as conexões **OAuth**, em que o
  parceiro pede autorização e o lojista aprova sem copiar e colar credencial. O Entregas
  Expressas não usa esse caminho hoje. No dia em que usar, o Passo 1 deste manual deixa de ser
  necessário, e a aba merece manual próprio — ela vale para qualquer parceiro, não só este.
- **O ciclo completo não foi observado de ponta a ponta.** Nenhum pedido foi criado para ver a
  coleta virar *despachado* e a entrega virar *entregue* no painel do BeeFood: isso exigiria uma
  conta ativa no Entregas Expressas e um entregador de verdade. O manual atribui essas
  afirmações ao parceiro, e não as apresenta como tela fotografada.
- **O `conferir-setas.py` é deste manual, de propósito.** Rodado nos 119 manuais da pasta, só 22
  passam: os estilos antigos de `annotate.py` e de citação no texto variam demais. Generalizar
  exigiria ler cada um, e não é o que este manual precisava.
