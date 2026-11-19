# MEMORIA.md — #134 Natural Bot (ativação pela API Aberta)

## O pedido

O dono passou o acesso ao painel de homologação do parceiro
(`hml-painel.naturalbot.com`, usuário `beefood@beefood.com.br`) e o roteiro inteiro:

> *"novo manual de integração Natural Bot. acessa nossa empresa de testes → aplicativos → api
> aberta → criar nova credencial"*, com a lista dos seis acessos; *"acessa o painel deles →
> configurações → integrações → ativa BeeFood, preenche tudo"*; *"depois vai em cardápio →
> produtos → Sync. BeeFood → e sincroniza o cardápio"*; e o limite:
> *"o manual mostra só como ativar as integrações entre uma e outra, dúvidas de uso deve ser
> tirada direto com a natural bot."*

Três instruções que deram a forma do manual:

1. **A credencial se cria pelo painel**, como no #129 — e não no portal, que é o que a tela da
   Natural Bot manda fazer.
2. **Os seis acessos são lista fechada**, e são exatamente os que a tela do parceiro pede. Isso
   mudou a Parte 1 em relação ao #129: lá o leitor **confere** permissões que já vêm ligadas;
   aqui ele **desliga** dez interruptores até sobrarem seis.
3. **O escopo é a ativação, e o manual repete isso duas vezes** — na abertura e no fim da Parte
   3. Nenhum passo de operação do robô entrou, e a seção *Precisa de ajuda?* divide o suporte em
   dois.

## A descoberta que mudou o manual: não existe Parte 3 de webhook

O #127 e o #129 terminam de volta no BeeFood, cadastrando o webhook à mão e devolvendo o
*Secret do webhook* ao parceiro. Aqui **não**. Com `webhook:write` na credencial, a Natural Bot
cadastra o próprio aviso ao salvar a integração. Conferido na API, logo depois do **Salvar**:

```
GET /v1/webhooks → {"items":[ … ]}
  id 98, active true, sandbox true,
  eventTypes [order_delivery_updated, order_updated],
  url https://dash-api-hml.naturalbot.com/api/v1/webhooks/beefood/<uuid da filial>,
  ownerEmail developer@naturalbot.com
```

Dois detalhes para quem for repetir a conferência: a resposta vem embrulhada em **`items`** (ler
`data` ou `webhooks` dá zero e parece que o webhook não existe), e a lista traz os webhooks de
produção e de sandbox juntos, cada um com a sua etiqueta `sandbox` — o da Natural Bot é
`sandbox: true`. Foi por isso que ele apareceu na aba **Webhooks** do painel de produção durante
o estudo.

Por isso o Passo 12 virou o fim da Parte 2 (é lá que está a linha **Webhook de status: ativo**)
e o manual tem uma nota avisando quem veio dos outros dois manuais que a etapa não existe mais.
Sem essa nota, o leitor vai procurar a aba **Webhooks** e achar que faltou algo.

## O erro que custou duas rodadas: homologação do parceiro fala com a sandbox da BeeFood

A credencial de **produção**, criada pelo painel com os seis acessos, foi recusada pelo painel de
homologação da Natural Bot:

> *Falha na conexão com a BeeFood — Autenticação na BeeFood: A BeeFood recusou o client ID ou o
> client secret.*

A credencial estava certa (`POST api.beefood.app/v1/oauth/token` devolveu 200 com os seis scopes
no token). O que acontece é que **existem dois bancos de credenciais**, e o HML do parceiro fala
com o de teste:

| | Produção | Sandbox |
|---|---|---|
| API | `api.beefood.app/v1` → `{"status":"ok","sandbox":false}` | `api-sandbox.beefood.app/v1` → `…"sandbox":true` |
| Empresa de testes | 38311 (`contato@beefood.com.br`) | 56179 (`developer-contato@beefood.com.br`) |
| Onde se cria | painel **ou** portal | só no portal, escolhendo **Ambiente → Sandbox** |

A mesma credencial de produção, mandada ao `api-sandbox`, devolve `401 Invalid client
credentials` — a cara exata do erro do painel do parceiro. Com isso:

- **o portal `docs.beefood.app` entrou no roteiro de captura**, pelo caminho *Entrar → Cliente
  BeeFood* (mesmo login do painel). Ele mostra as duas empresas, produção e sandbox, e é o único
  lugar onde se escolhe o ambiente da credencial;
- a credencial de sandbox usada para conectar é `2fa1ea6d-420d-4792-a2ad-01f793764d55`, criada
  no portal com os seis acessos. **O secret dela não está versionado**: ele sai do ícone de
  chave na lista do portal, ou cria-se outra credencial igual. O `capturar-naturalbot.py` o lê
  de `BF_SANDBOX_CLIENT_ID` / `BF_SANDBOX_CLIENT_SECRET`;
- credencial de sandbox **não aparece** em *Todas as credenciais* no painel:
  `carregarLista` filtra `!c.sandbox`. Foi o que explicou por que o `clientId` que já estava
  salvo na filial de homologação não constava em lugar nenhum do painel.

## As duas credenciais das capturas, e por que são duas

- **Produção**, criada e fotografada pelo `capturar-beefood.py` (imagens 03 e 04). O
  `clientSecret` aparece inteiro na imagem 04, então o `limpar-credencial.py` **apaga** essa
  credencial no fim — mesmo cuidado do #129: o segredo versionado é de uma credencial que não
  existe mais.
- **Sandbox**, criada no portal, é a que conecta de verdade nas imagens 07 a 12. Ela não aparece
  em imagem nenhuma: o campo de secret é de senha e o `clientId` só reaparece mascarado
  (`2fa1***4d55`) na imagem 09.

O estudo também deixou uma credencial de produção **exploratória**, criada antes das capturas
para medir os escopos. Ela foi apagada no fim, pelo mesmo script
(`python3 limpar-credencial.py <clientId>`), para a empresa de testes ficar como estava.

A imagem 06 (formulário preenchido) mostra a de **produção**, pela técnica do ensaio — preenche,
fotografa, **não** clica em *Conectar*. É o que mantém o `clientId` da imagem 04 e o da 06
iguais, que é o que o leitor vai comparar.

## Chamar a API da BeeFood de script

`api.beefood.app` e `api-sandbox.beefood.app` estão atrás de Cloudflare, e ele responde
**403 `error code: 1010`** para o `User-Agent` padrão do `urllib`. Não é credencial nem escopo:
basta mandar um `User-Agent` de navegador. O 401 de credencial, quando é credencial mesmo, vem
em JSON: `{"message":"Invalid client credentials","status":401}`.

## O acesso do parceiro, e o que ficou versionado

O painel é de **homologação** — ambiente descartável, como manda a regra da casa para sandbox.
Mesmo assim, é painel de **outra empresa**, e a senha não entrou no repositório: o
`naturalbot.py` lê de `NB_SENHA` e o estado de sessão fica em `/tmp/naturalbot-storage.json`. O
usuário (`beefood@beefood.com.br`) está no código, porque sem ele o script não se explica.

## O que o painel do parceiro ensinou, e entrou no manual

- **Um gestor de PDV por vez.** *"Ao ativar um novo gestor, o anterior será desativado
  automaticamente."* A BeeFood entra como gestor de PDV, ao lado de Colibri, Saipos, CCM e
  outros. Virou seta na imagem 05 e linha na tabela de problemas.
- **Para mexer nos interruptores de sincronização, feche a loja.** O aviso
  *"Feche a loja para alterar estas configurações"* vale para as duas chaves do bloco
  **Sincronização de pedidos** — mas **não** para conectar nem para salvar, que funcionaram com
  a loja aberta.
- **O de-para de pagamentos é sugerido, não decidido.** A Natural Bot propõe o par (Pix → PIX
  Manual, e assim por diante) e avisa que *"só vale depois que você salvar"*. Trocar de cardápio
  apaga o de-para do anterior.
- **A verificação pós-salvar fala duas línguas.** A linha verde diz se a credencial foi aceita;
  o amarelo é configuração do cardápio no BeeFood. Na loja de sandbox veio
  *"o canal delivery deste cardápio da BeeFood não aceita pedidos de entrega nem de retirada"*,
  e isso ficou na imagem 08 de propósito, com tabela explicando.
- **A importação duplica categoria de mesmo nome.** A filial já tinha uma *Bebidas* criada à mão;
  a importação criou a sua, e a página de Produtos ficou com duas abas *Bebidas*. Entrou na
  tabela de problemas.
- **A lista de Produtos abre na primeira categoria**, que pode estar vazia — foi o que fez a
  primeira captura da lista de produtos sair com *"Nenhum produto cadastrado"* depois de uma
  importação bem-sucedida. Essa foto saiu do manual na segunda rodada (o dono cortou: o que o
  leitor precisa é do caminho da importação), mas a pegadinha ficou, como aviso de texto no
  último passo.

## A segunda rodada: o dono cortou quatro imagens

A primeira entrega tinha dezesseis imagens e dezesseis passos. O dono leu e pediu objetividade,
nomeando o que cortar — e cada corte tem a mesma lógica: **foto que mostra estado em vez de
ação não vale o espaço.**

| O que tinha | O que ficou | Por quê |
|---|---|---|
| a credencial principal e o `CRIAR CREDENCIAL` em duas fotos | uma foto costurada, da aba direto para o botão | *"precisa ser mais objetivo, mostre direto como criar a credencial nova"* |
| o diálogo de permissões *como abre* e *como fica* | só *como fica* | *"resuma, só mostrando o que deve ficar ativo"* |
| a aba *Integrações* e o card da BeeFood em duas fotos | uma foto costurada, com a BeeFood **em primeiro** e **sem os concorrentes** | o painel do parceiro é cheio de PDV concorrente, e manual nosso não os divulga |
| a lista de produtos já importada | nada — só o caminho da importação | *"não precisa mostrar produtos importados, somente o caminho de como importar"* |

Daí saíram duas coisas reaproveitáveis:

- **`montagem()`, no `annotate.py`.** Costura recortes de print numa imagem só, com os
  marcadores ainda em pixel da pura de cada fatia, e desenha a emenda **tracejada**. É o que
  deixa um passo que mora em duas alturas da mesma tela — ou em duas telas — caber numa foto sem
  mentir: o tracejado diz que ali existe tela que não está na foto.
- **Card de concorrente se tira mudando o card de lugar, não apagando o vizinho.** A BeeFood é o
  décimo segundo gestor de PDV no painel do parceiro. O recorte pega só o card dela e o encosta
  na coluna onde ficava o primeiro — as coordenadas da grade são as mesmas, então o resultado é
  indistinguível de um print de uma lista com um item.

## Capturas

| Script | O que faz |
|---|---|
| `capturar-beefood.py` | puras 01 a 04 — cria a credencial de produção com os seis acessos e fotografa os dois diálogos |
| `capturar-naturalbot.py` | puras 05a a 12 — conecta, escolhe cardápio, salva e importa o cardápio |
| `limpar-credencial.py` | apaga a credencial de produção que foi fotografada |
| `annotate.py` | as 12 tratadas, 42 setas; duas delas são **costuradas** de dois recortes |
| `conferir-setas.py` | cruza as setas desenhadas com os números citados no `.md` |

Dois detalhes do `annotate.py` que valem para o próximo manual com painel de parceiro:

- os diálogos da Natural Bot são **mais largos** que os da BeeFood e começam em x=580 na captura
  de 2160 px — daí a geometria `dialogo_nb()`, separada da `dialogo()`;
- o `conferir-setas.py` do #129 confundia tupla de quatro números — o `corte=`, a caixa de uma
  fatia — com marcador de seta. A correção (tirar toda tupla de quatro campos numéricos do bloco
  antes de procurar marcador) está na versão daqui.

## Pendências

- O manual descreve o painel de **produção** do parceiro, mas as capturas são do de
  **homologação**. As telas são as mesmas; se um dia o parceiro mudar o layout de produção, as
  imagens envelhecem sem aviso.
- A filial de homologação ficou **conectada** à empresa de sandbox 56179, com o cardápio
  importado (1 categoria, 4 produtos). Se o dono quiser o ambiente limpo, é desligar a chave do
  card BeeFood e apagar os produtos importados pela própria Natural Bot.
