# MEMÓRIA — Manual do Modo Kiosk (Cardápio Digital Tablet)

> Memória detalhada deste manual (fluxo, uso, decisões e estado), para retomar a qualquer momento.
> Ver também a memória geral: `../../MEMORIA-GERAL.md`.

Status: ✅ **Concluído — texto e as 19 imagens marcadas no repositório** (aguardando publicação
do dono) — Última atualização: 2026-08-20

---

## 1. Escopo do manual

O manual é **só do aplicativo Android** *Cardápio Mesa/Comanda*, no próprio tablet. Ensina o
gestor a travar o aparelho no cardápio:

1. Abrir a tela de **Administração** (toque no logo, no canto superior esquerdo + senha).
2. Conceder as duas permissões do Android pelo assistente (**Acessibilidade** e
   **Launcher padrão**).
3. **ATIVAR MODO KIOSK**.
4. Conferir se travou (botão Início e barra de notificações).
5. **DESTRAVAR** quando precisar.

Fecha com a alternativa da **trava básica** (screen pinning, sem permissões) e um FAQ de sete
perguntas.

**O login ficou fora.** A versão original abria com uma "Parte 1 — Entrar no aplicativo", com as
capturas de login e de seleção de cardápio. O dono pediu para tirar em 20/08/2026: quem vai
travar o tablet já está com o cardápio aberto na tela. O manual passa a começar no logo.

**Fora do escopo:** o painel web. O evento `TRAVAR` da aba Tablets é outra coisa — está
mapeado no `fluxo-codigo.md`, com a tabela que diferencia as três travas.

Arquivo final: `cardapio-digital-tablet-modo-kiosk.md`.

## 2. Origem do texto — copiado primeiro, depois editado a pedido

O manual **já veio escrito** pelo dono, em
`c:\projetos\beetech-appgarcom-android\docs\manual-modo-kiosk.md`. Seguindo o que o
repositório já fez nos manuais **#8 (99 Entrega)** e **#11 (Uber Direct)**, o arquivo entrou
aqui **como estava**, sem reinterpretar — só com os caminhos `images/kiosk/` trocados por
`imagens-tratadas/` e CRLF virando LF.

**Em 20/08/2026 o dono pediu para editar**, e aí a cópia deixou de ser fiel. O que mudou, e só
isto:

| O que | Por quê |
|-------|---------|
| Saiu a **Parte 1 — Entrar no aplicativo**, com as duas capturas de login | Pedido direto do dono: "não precisamos dessa parte no manual". |
| As Partes 2 a 6 viraram **1 a 5**; a visão geral perdeu o passo do login e passou de 5 para 4 itens | Consequência da remoção. Havia também um "pule direto para a Parte 3" que sumiu com a seção. |
| "Antes de começar" pede a **senha de administrador** em vez de "usuário e senha do login" | Sem a seção de login, o pré-requisito é só a senha — que continua sendo a mesma. |
| Cada imagem marcada ganhou uma tabela **"Nº → o que fazer"**, e o texto cita os números | É a convenção do repositório para imagem com seta (`MEMORIA-GERAL.md`). |
| O trecho do aviso "O app está fixado" foi reescrito | O texto original mandava "toque em **Entendi**" na tela da `17-app-fixado`, mas ali o Android mostra só um aviso rápido, sem botão; o painel com o botão aparece **atrás** do diálogo na `16-kiosk-ativado`. Agora o manual descreve as duas coisas onde elas realmente estão. |
| Duas frases novas explicam por que a `19-home-travada` e a `20-destravado` não têm seta | Sem isso, imagem sem marcação no meio de dezessete marcadas parece esquecimento. |
| Frase nova no assistente: se o contador não mudar, tocar no ícone de recarregar | O ícone está visível no canto superior direito de todas as capturas do assistente e resolve a dúvida mais provável do passo. |

Tudo o que não está nessa tabela continua palavra por palavra igual ao original, inclusive o
FAQ inteiro e os textos alternativos das imagens.

> **Se o texto de origem for atualizado**, não sobrescreva este arquivo: refaça a cópia num
> lado, aplique de novo as mudanças da tabela acima e compare. Sobrescrever perde as edições.

## 3. Como as imagens chegaram (e o que não funcionou)

**Resolvido em 20/08/2026 por um link do Google Drive.** O dono subiu um `.zip` com as 21
capturas, compartilhou em "qualquer pessoa com o link" e passou o link; o
`copiar-imagens.py <link>` baixou os 20 MB, extraiu e distribuiu — 21/21, sem faltar nenhuma e
sem nenhum PNG sobrando. **Duas saíram depois**, junto com a Parte 1 (`01-login` e
`02-selecionar-cardapio`), e o manual ficou com 19.

Isso só é possível porque o VM tem **egresso de internet liberado**: o
`cursor-cloud-environment-info` devolve `egress: { restricted: false }`, e `drive.google.com`
responde ao `curl`.

**O que não funcionou, e vale não repetir:**

- **Imagem colada no chat.** Testado cinco vezes. O agente **enxerga** as capturas, mas elas
  chegam já decodificadas, sem caminho em disco e sem URL — não existe "baixar a imagem do
  chat", porque não há de onde baixar. Só o `.md` chegou como arquivo (foi para
  `~/.cursor/projects/workspace/uploads/`, o **único** lugar onde anexo aparece como arquivo).
- **`.zip` anexado no chat.** A teoria era boa — zip não é imagem, então deveria cair em
  `uploads/` como qualquer documento. Na prática **não chegou**: `uploads/` continuou só com o
  `.md`. Segue sendo caminho não confirmado.
- **Buscar numa versão publicada do manual.** `ajuda3.beefood.com.br/modo-kiosk` e
  `.../cardapio-digital-tablet-modo-kiosk` respondem **404** — ele ainda não foi publicado.

**Outros caminhos que servem, se o link não estiver à mão:**

| Caminho | Como |
|---------|------|
| **Liberar o repositório do app** (resolve de vez, para sempre) | Secret `BITBUCKET_TOKEN_APPGARCOM` (o `install.sh` já tem a entrada e já aceita vários tokens). Aí o agente pega as capturas na origem, sem link nenhum. Pedido já registrado no ambiente; só vale em **VM nova**. |
| **Rodar na máquina do dono** | `python copiar-imagens.py`, que já encontra `c:\projetos\beetech-appgarcom-android\docs\images\kiosk`, depois commit e push. |

> **Atenção ao link do Drive:** tem de ser link de **arquivo** (o `.zip`), não de pasta —
> pasta do Drive não dá para baixar sem credencial, e o script recusa esse link com essa
> explicação. E o compartilhamento precisa estar em "qualquer pessoa com o link"; senão o
> Drive devolve a página de login, e o script avisa que o que baixou não é zip.

### O jeito rápido: `copiar-imagens.py`

Dentro desta pasta:

```bash
python copiar-imagens.py                 # procura a origem sozinho
python copiar-imagens.py <pasta>         # usa essa pasta
python copiar-imagens.py <arquivo.zip>   # usa esse zip
python copiar-imagens.py <url-do-zip>    # baixa o zip dessa url
```

O script copia as capturas para `imagens-puras/` e imprime um relatório item a item. Ele **lê a
lista de arquivos do próprio manual**, na ordem em que as imagens aparecem — não tem lista
escrita dentro dele, então nunca fica dessincronizado do texto. Se alguma faltar, mostra quais e
sai com código 1; se houver PNG na origem que o manual não usa, avisa em vez de copiar em
silêncio.

> **Só para `imagens-puras/`, e isso é recente.** Até 20/08/2026 ele copiava para as duas
> pastas, porque não havia anotação. Depois que o `annotate.py` entrou, copiar por cima de
> `imagens-tratadas/` apagaria as setas — então a escrita nas tratadas ficou só com o
> `annotate.py`. A sequência correta agora é `copiar-imagens.py` e depois `annotate.py`, e o
> próprio script imprime isso no fim.

Origens procuradas automaticamente, nesta ordem:

1. `c:\projetos\beetech-appgarcom-android\docs\images\kiosk` (máquina do dono)
2. `~/refs/beetech-appgarcom-android/docs/images/kiosk` (Cloud Agent, se o repositório do app
   passar a ser clonado)
3. o **zip mais recente** em `~/.cursor/projects/workspace/uploads/` (Cloud Agent)

A busca é **recursiva** tanto em pasta quanto em zip: não importa se os PNG estão na raiz ou
dentro de `images/kiosk/`.

> Testado em 20/08/2026 num diretório temporário fora do repositório, com 21 PNG de 1×1
> gerados na hora, metade na raiz e metade em subpasta, mais um PNG sobrando. O zip foi
> servido por um `http.server` em `localhost` para exercitar o download de verdade.
>
> Passaram: URL, zip local, pasta com subpastas, auto-detecção do zip em `uploads/` — 21/21 em
> todos, com o arquivo sobrando apontado no relatório. Deram código 1, cada um com a mensagem
> certa: origem incompleta, origem inválida, link de pasta do Drive, URL 404, URL que devolve
> HTML em vez de zip, host recusando conexão e link do Drive sem id.
>
> Os seis formatos de link do Drive que aparecem na prática (`/file/d/<id>/view` com
> `usp=sharing` e com `usp=drive_link`, `open?id=`, `uc?export=download&id=`, o endpoint
> `drive.usercontent.google.com` e uma URL comum de outro host) foram conferidos um a um na
> conversão para download direto.
>
> **Bug encontrado e corrigido no teste:** cada URL que falhava deixava uma pasta em `/tmp`,
> porque o erro sai por `SystemExit` antes do `finally` que limpa. Depois da correção, cinco
> falhas seguidas não deixaram resíduo.

As 19 estão nas duas pastas, todas **2560×1600**. Os nomes têm de ser exatamente estes — cada
um foi conferido contra a legenda escrita no manual, e a coluna *Setas* diz quantos badges o
`annotate.py` desenha em cada uma:

| # | Arquivo | Setas | Tela |
|---|---------|:-----:|------|
| 1 | `03-home-logo.png` | 1 | Tela inicial do cardápio, com o logo no topo à esquerda |
| 2 | `04-senha-administracao.png` | 2 | *Administração* pedindo a senha, com o teclado aberto |
| 3 | `05-painel-administracao.png` | 2 | Painel destravado: ATUALIZAR, TRAVAR, CONFIGURAR TRAVA AVANÇADA |
| 4 | `06-assistente-inicio.png` | 4 | *Bloquear tablet (Modo Kiosk)* — 0 de 2 permissões |
| 5 | `07-aviso-acessibilidade.png` | 2 | *Uso do serviço de acessibilidade* (consentimento) |
| 6 | `08-android-acessibilidade.png` | 1 | Android → Acessibilidade, serviço em *Apps baixados* |
| 7 | `09-android-servico-kiosk.png` | 1 | Página do serviço com a chave desativada |
| 8 | `10-android-confirmar-servico.png` | 1 | Android pedindo *Permitir* controle total |
| 9 | `11-android-servico-ativo.png` | 1 | Página do serviço com a chave ativada (azul) |
| 10 | `12-assistente-1de2.png` | 3 | Assistente — 1 de 2, Acessibilidade em verde |
| 11 | `13-android-launcher.png` | 1 | *Definir app de início padrão?* com o Pixel marcado |
| 12 | `14-android-launcher-selecionado.png` | 2 | Mesma tela com *Cardápio Mesa/Comanda* marcado |
| 13 | `15-assistente-pronto.png` | 2 | Assistente — 2 de 2 e o botão **ATIVAR MODO KIOSK** |
| 14 | `16-kiosk-ativado.png` | 2 | Alerta *Tablet bloqueado (Modo Kiosk)* |
| 15 | `17-app-fixado.png` | 1 | Aviso do Android *O app está fixado* |
| 16 | `19-home-travada.png` | — | Cardápio na tela depois do teste do botão Início |
| 17 | `18-painel-destravar.png` | 1 | Painel travado: ATUALIZAR e **DESTRAVAR** |
| 18 | `20-destravado.png` | — | Painel de volta ao estado destravado |
| 19 | `21-trava-basica.png` | 2 | Assistente com **PULAR E USAR TRAVA BÁSICA AGORA** (laranja) |

> A ordem de exibição não é a ordem numérica: a `19` aparece **antes** da `18`, porque o teste
> da Parte 4 vem antes do destravamento da Parte 5. É assim no texto de origem — manter.

> **Os nomes não foram renumerados** de `03…21` para `01…19` depois da remoção da Parte 1. São os
> mesmos do repositório do app, e o `copiar-imagens.py` casa a origem com a lista lida do
> manual — renumerar quebraria a próxima ressincronização por um ganho só cosmético.

**Sobre compressão:** ninguém recomprimiu de propósito, mas passar pelo `annotate.py` reescreve o
PNG com o codificador do Pillow, e as tratadas saíram ~10% menores que as puras. É **lossless** —
conferido com `ImageChops.difference`: as duas de contexto ficaram **pixel a pixel idênticas** às
puras, e nas marcadas a única diferença é o retângulo onde a seta foi desenhada.

### As marcações (`annotate.py`)

Existe `annotate.py` nesta pasta desde 20/08/2026, quando o dono pediu as marcações. Antes disso
não existia, e as duas pastas eram idênticas — **hoje não são mais**: `imagens-puras/` guarda os
originais do dono e `imagens-tratadas/` as versões com seta, que é o que a convenção do
repositório manda. Nunca editar as tratadas à mão: mexer na coordenada dentro do script e rodar
de novo.

Padrão igual ao dos outros manuais: seta verde fina com badge numerado, coordenadas em fração,
`passthrough()` para as imagens de contexto. Sem `borrao` — a única tela com dado identificável
era o login, que saiu.

Duas particularidades destas capturas:

- **Quase toda tela do app é um diálogo centralizado** com o cardápio escurecido em volta. Os
  badges vão nessa margem escura e as setas entram no diálogo, o que mantém a tela do app limpa.
  Nas telas de Configurações do Android, que têm fundo claro, o badge vai no espaço vazio da
  própria lista.
- **A seta mira a borda inferior dos botões, não o meio.** Na primeira geração a ponta caía em
  cima da palavra (`CONCEDER`, `AGORA NÃO`, `CONCORDAR E CONTINUAR`) e cobria uma letra. Vale
  para qualquer botão com texto centralizado.

Para medir as coordenadas, o que funcionou bem foi gerar uma cópia temporária de cada captura com
uma grade de frações sobreposta (linha a cada 0,05, rótulo a cada 0,10) e ler os valores direto
da grade — bem mais rápido e preciso que estimar no olho, e vale copiar em qualquer manual novo.
Ainda assim, conferir cada imagem gerada em tamanho real no fim: foi só nessa conferência que as
pontas em cima do texto apareceram.

> **Um efeito colateral bom:** antes, `19-home-travada` era byte a byte igual a `03-home-logo`, e
> `20-destravado` igual a `05-painel-administracao`. Como as duas primeiras ganharam seta e as
> outras ficaram de contexto, a duplicata desapareceu sozinha em `imagens-tratadas/`. Em
> `imagens-puras/` os dois pares continuam idênticos, e isso é esperado: o teste da trava mostra
> justamente que a tela **não muda**, e destravar devolve o painel ao estado anterior.

## 4. Histórico (o caminho até aqui)

| Quando | O que aconteceu |
|--------|-----------------|
| 1ª rodada | Pedido chegou citando o `manual-modo-kiosk.md` e a pasta `images` como anexos. **Nada chegou ao VM.** Escrevi um rascunho com o escopo errado (o painel web) e mapeei o código do painel. |
| 2ª rodada | O dono mandou as 21 imagens no chat e esclareceu: **o manual é só no tablet**. Informou o caminho de origem, `c:\projetos\beetech-appgarcom-android\docs\manual-modo-kiosk.md`. Testei o acesso ao repositório do app no Bitbucket: **sem acesso** (o `BITBUCKET_TOKEN` alcança só o `beetech-server-node-2.0`). |
| 3ª rodada | O `.md` foi anexado de um jeito que **caiu em disco**. Manual copiado, escopo corrigido, `texto-documentation.ia.md` escrito. Sobraram só as imagens. |
| 4ª rodada | O dono tentou o `.zip` e ele **não chegou** — `uploads/` continuou só com o `.md`, e as imagens vieram outra vez como imagem no chat. Varredura nova no VM (`find /` por PNG/JPG/ZIP criados no dia) não achou nada, e a versão publicada do manual não existe para servir de origem (404 no `ajuda3`). Pedido do secret `BITBUCKET_TOKEN_APPGARCOM` registrado formalmente para o ambiente. |
| 5ª rodada | O dono perguntou se **Google Drive** funcionaria. Funciona: o ambiente reporta `egress: { restricted: false }` e o Drive responde ao `curl`. O `copiar-imagens.py` passou a aceitar **URL** como origem, com conversão do link de compartilhamento do Drive para download direto. Testado de ponta a ponta com um zip servido por HTTP. |
| 6ª rodada | O dono mandou o link do `.zip` no Drive. **Resolvido:** 20 MB baixados, 21/21 copiadas, `validar-imagens.py` limpo. Manual completo. |
| 7ª rodada | O dono pediu para **interpretar as imagens e marcá-las**, e para **remover a Parte 1** (login). Saíram a seção e as duas capturas; as partes foram renumeradas; entrou o `annotate.py` com 29 setas em 17 imagens, e o texto passou a citar os números em tabelas. O `copiar-imagens.py` deixou de escrever em `imagens-tratadas/` para não apagar as marcações. |

**Lição principal, já registrada no `MEMORIA-GERAL.md`:** anexo do chat não chega ao VM por
padrão. Quando cai em `~/.cursor/projects/workspace/uploads/`, chegou; se não estiver lá, não
chegou. Vale conferir essa pasta antes de concluir que o material não existe. E para imagem,
que nunca chega como arquivo, **o caminho é URL**: o VM baixa de qualquer host.

## 5. Decisões tomadas

- **Copiar, não reescrever — e depois editar só o que foi pedido.** O texto do dono já está no
  tom certo e descreve telas que eu não tenho como validar sozinho (o código do app é
  inacessível). Na 7ª rodada ele pediu mudanças, e mesmo aí a régua foi mexer no mínimo: a
  tabela da seção 2 lista cada divergência, e o resto continua palavra por palavra.
- **Marcar tudo o que o texto manda tocar, e nada além.** Cada seta corresponde a uma ação ou a
  uma conferência que o texto já pedia. Não inventei marcação em elemento que o manual não
  menciona — seta sem número citado no texto só suja a imagem.
- **Descartei o rascunho da 1ª rodada.** Ele documentava o painel web, que o dono disse
  explicitamente não ser o assunto. O trabalho não foi perdido: virou o `fluxo-codigo.md`.
- **Mantive o `fluxo-codigo.md`** com uma tabela que separa as três travas. Foi a confusão que
  me fez errar o escopo na primeira rodada, e é a mesma confusão que o suporte tende a ter.
- **`texto-documentation.ia.md` pronto para colar.** As 19 imagens já estão no lugar, então o
  bloqueio de publicação saiu. O prompt foi corrigido para dizer que as imagens **têm** seta
  numerada e que as tabelas "Nº" precisam ficar junto da imagem certa — antes ele mandava o
  contrário, porque na época não havia marcação.
- **Não recomprimi as capturas de propósito.** O que houve foi o reencode do `annotate.py`, que é
  lossless e ainda economizou ~10% (ver seção 3). `imagens-puras/` guarda os bytes originais.
- **Não renomeei os arquivos** depois de remover as duas primeiras imagens. O manual começa na
  `03-home-logo`, o que parece estranho de início, mas os nomes são os do repositório do app e
  renumerar quebraria a ressincronização.

## 6. Detalhes técnicos que o texto de origem traz

- Versão do app nas capturas: **1.0.2.8**, em tablet **Android 15**.
- A senha da tela de **Administração** é a **mesma do login** do app.
- As duas permissões: **Acessibilidade** (detecta a tentativa de sair e devolve o app) e
  **Launcher padrão** (faz o botão Início abrir o cardápio).
- **Volume e power não são bloqueáveis** sem provisionar o tablet como *Device Owner*, o que
  exige reset de fábrica. Está avisado na própria tela do assistente.
- A trava **sobrevive ao reinício** do tablet.
- Fabricantes como Xiaomi e Motorola podem matar o app em segundo plano: marcar o app como
  **sem restrição** na otimização de bateria.
