# MEMÓRIA GERAL — Boas práticas para criação de manuais BeeFood

> Memória mestre do projeto de manuais. **Ler SEMPRE no início de cada sessão.**
> Cada manual tem ainda sua própria `MEMORIA.md` dentro da sua pasta.

Última atualização: 2026-08-30 (**#71** Aparência e layout; **#70** Agendamento do cardápio digital; **#68/#69** Exibir/Ocultar e Preço Programado; **#66/#67** Lançamentos; **#65** Taxas formas de recebimento; **#64** Desconto formas de recebimento; **#19** e **#20** Cashback; **#59–#63** entregas/marketplace; **#21** Cupom; **#18** SMS; **#58** IA ChatGPT; **#57** BeeFood Entregador; **#48** Capas e Destaques; **#49–#56** migrados do
ajuda.beefood em `PLANO-MIGRACAO-AJUDA.md`; screenshot Playwright
precisa de `type="png"`; prévia `aside` pode sair com 5000+ px — recortar o aparelho;
`get_by_role(name=lambda)` quebra no Playwright Python desta VM; banner de cupom
do cardápio público nem sempre fecha por `Dispensar`; **espera de 5 s após cada
clique vale para SEMPRE**, qualquer manual — spinner some primeiro, só então
contar os 5 s; bloco Área de Entrega #34–#38; ler no código o que grava antes de
capturar; dado pessoal coberto na imagem pura; widget flutuante escondido por CSS;
diagnóstico do ambiente pela API; anexo do chat não chega ao Cloud Agent; imagem
colada no chat não tem como ser baixada, mas **zip numa URL pública o agente
baixa** — o VM tem egresso liberado; escopo real do `BITBUCKET_TOKEN`; backend
clonado no Cloud Agent; tela de login mudou; telas com auto-save; captura com
Playwright; **medir coordenada de seta com grade de frações** e mirar a borda do
botão, não o centro)

---

## 1. Objetivo

Criar **manuais de funcionalidades para o USUÁRIO FINAL** do sistema BeeFood, combinando:
- **Código** do projeto `beefood-web-react` (`C:\projetos\beefood-web-react`) → entender a lógica real.
- **Produção** (`https://beefood.app`) → capturar telas reais.

Saída: arquivos **`.md`** + imagens anotadas.

---

## 2. Estrutura de pastas (PADRÃO — seguir sempre)

```
C:\beefood-web-react-manual\
├─ MEMORIA-GERAL.md            <- esta memória (boas práticas, contas, ferramentas)
└─ manuais\
   └─ <nome-do-manual>\        <- UMA PASTA POR MANUAL (ex.: caixa, delivery, pdv...)
      ├─ MEMORIA.md                 <- memória detalhada do manual (fluxo, uso, decisões, estado)
      ├─ <nome>.md                  <- o manual final (para o usuário)
      ├─ fluxo-codigo.md            <- mapeamento técnico (a partir do código)
      ├─ texto-documentation.ia.md  <- PROMPT pronto p/ criar o manual no app (ver seção 12)
      ├─ annotate.py                <- script de anotação (setas/números) deste manual
      ├─ imagens-puras\             <- screenshots ORIGINAIS (BACKUP, nunca referenciado)
      └─ imagens-tratadas\          <- TODAS as imagens do manual (com setas + contexto). Única pasta referenciada
```

**Regra de ouro:** ao iniciar um manual novo, criar uma pasta nova em `manuais\<nome>\`
com TODAS as subpastas/arquivos acima.

---

## 3. Boas práticas de imagens

1. **Sempre salvar a imagem PURA primeiro** em `imagens-puras\` (backup, **nunca referenciado** no `.md` nem no `texto-documentation.ia.md`).
2. Depois gerar a versão **tratada** em `imagens-tratadas\` via `annotate.py`. **`imagens-tratadas\` deve conter TODAS as imagens usadas no manual:** as principais com setas + as de **contexto** (sem setas, via `passthrough()` do `annotate.py`). Assim só essa pasta é referenciada.
3. Nomeação sequencial por etapa: `NN-descricao.png` (ex.: `03-modal-abrir-caixa.png`).
4. **Poucas fotos, sem excesso** — apenas as essenciais de cada etapa.
5. Cada foto essencial leva **setas verdes + número**. O texto do manual referencia cada número e
   destaca campos **obrigatórios (\*)**.
   - **Numeração:** usar SEMPRE números normais **`1.`, `2.`, `3.`** (com ponto). **NÃO** usar
     números circulados (①②③) nem em parênteses — no texto, nas tabelas e nas legendas.
   - **Não printar a tela ainda carregando.** Depois de cada clique: esperar sumir
     `Carregando...` / `Atualizando...` / `Calculando…` e **só então esperar 5 segundos**.
     Vale para **todo** manual. Detalhe na seção 6.
6. As imagens em produção saem em **1508×1274** (DPR alto). `annotate.py` usa coordenadas
   em **frações 0..1**, então independe da resolução.
7. **Dados pessoais de clientes precisam sair ilegíveis.** Telas que listam clientes (nome,
   telefone, e-mail) não podem ir para o repositório como estão — ele é **público**. A decisão
   da seção 11 vale para as *credenciais* de teste, não para dados de terceiros. O `annotate.py`
   de `manuais\segmentacao-clientes\` tem o parâmetro `borrao` (regiões em frações, aplicadas
   com `GaussianBlur` antes das setas); copie de lá quando precisar.

### Antes de dar um manual por concluído: `validar-imagens.py`

Na raiz do repositório, rodar `python validar-imagens.py` (ou
`python validar-imagens.py <pasta-do-manual>` para um só). Ele confere, em todos os manuais:

- se **toda imagem referenciada existe** em `imagens-tratadas/` — sai com **código 1** quando
  falta alguma, porque manual com imagem faltando não pode ser publicado;
- se o `texto-documentation.ia.md` lista alguma imagem que o manual **não usa**;
- se há **órfão** em `imagens-tratadas/` (arquivo na pasta que ninguém referencia).

Órfão e divergência do prompt são **avisos**, não erram a saída.

> Existe porque manual com imagem faltando **quebra em silêncio**: o markdown continua válido,
> o texto continua legível, e só quem abre a página publicada descobre. Foi o que aconteceu no
> #24, cujas capturas vivem em outro repositório. Auditoria de 20/08/2026: dos 14 manuais, 13
> estavam íntegros (164 imagens) e só o #24 acusou as 21 faltando; nenhum órfão.

### Como anotar (Pillow)
- Requisitos: Python 3.10+ e Pillow (já instalados nesta máquina).
- `annotate.py` lê de `imagens-puras\` e escreve em `imagens-tratadas\`.
- Config por imagem: lista de marcadores `(numero, alvo_x, alvo_y, badge_x, badge_y)` em frações.
- Rodar dentro da pasta do manual: `python annotate.py`.
- **Sempre conferir visualmente** as imagens tratadas e ajustar coordenadas se necessário.

**Para medir as coordenadas, sobreponha uma grade de frações na captura** em vez de estimar no
olho: uma cópia temporária com linha a cada 0,05 e rótulo a cada 0,10, e os valores são lidos
direto da grade. É rápido de escrever (umas 20 linhas de Pillow, em `/tmp`, fora do repositório)
e acerta quase tudo de primeira. Usado no #24 em 16 capturas: das 29 setas, 24 nasceram no lugar.

### Padrão oficial — tira de celulares (cardápio público)

Não coloque vários prints altos de celular soltos no `.md`. Monte **uma tira**
com os aparelhos lado a lado. O cliente lê o conjunto numa olhada; o arquivo
único também cabe melhor na página publicada.

**Captura (Playwright):**

- Viewport **390×844**, `device_scale_factor=2` → pura **780×1688**
- `is_mobile=True`, `has_touch=True`, `locale="pt-BR"`, `LANG=pt_BR.UTF-8`
- Cardápio: `https://menu.beefood.com.br/beefood3`
- **Não clicar Retirada na home** (abre o mapa Leaflet). Modalidade =
  **Retirar no estabelecimento** dentro da sacola
- Combo de teste: One Burger + Batata frita + Coca 350ml = **R$ 39,00**
- Telefone de teste: **(15) 99999-8888** (`15999998888` no `input[type=tel]`)
- Opções do combo: clique JS/mouse em `.modal-product__details .option-item`
  (o `click` do Playwright falha “outside viewport”)

**Montagem (`montar_celulares` no `annotate.py` — copiar do #19/#20/#64):**

| Constante | Valor | Função |
|-----------|------:|--------|
| `PHONE_W` | 380 | Largura de cada aparelho na tira |
| `GAP` | 18 | Espaço entre aparelhos |
| `PAD` | 22 | Margem do canvas |
| `CAP_H` | 44 | Faixa do título acima do aparelho |
| raio | 26 | Canto arredondado + máscara |
| fundo | `(244, 244, 245)` | Cinza claro |

- Puras **individuais** ficam em `imagens-puras/` como **fonte**. Não entram no `.md`.
- `montar_celulares` grava a tira **também em `imagens-puras/`**.
- Só a tira (já anotada) entra no `.md` e no `texto-documentation.ia.md`.
- 2 ou 3 aparelhos. Três ainda lê fácil (~1220 px de largura). Quatro aperta.
- Título curto acima de cada um (“PIX Online — 5%”).
- Setas na tira: `no_painel(i, tx, ty, W, H, ph_h)` — `tx/ty` são frações
  **dentro daquele celular**, não da tira inteira.

Usado no **#19**, **#20** e **#64**.

**Mire a borda do elemento, não o centro, quando ele tem texto.** Seta apontada para o meio de um
botão cai em cima do rótulo e cobre uma letra — aconteceu em quatro botões do #24 (`CONCEDER`,
`AGORA NÃO`, `CONCORDAR E CONTINUAR`, `ACESSAR`). A borda inferior ou lateral marca o mesmo
elemento sem tapar nada. Vale também para campo de texto: apontar ao lado do rótulo, não nele.

> Só a conferência **em tamanho real** revela isso. Numa folha de contato reduzida as quatro setas
> pareciam perfeitas. Faça as duas coisas: folha de contato para ver o conjunto, e depois abrir
> uma a uma as que têm alvo pequeno ou botão com texto.

**Se as capturas vêm de fora do repositório, o script que as importa não pode escrever em
`imagens-tratadas\`** — ele apagaria as setas na próxima execução. Que ele alimente só
`imagens-puras\`, e que imprima no fim o lembrete de rodar o `annotate.py`. Foi o ajuste feito no
`copiar-imagens.py` do #24 quando o manual deixou de ser só contexto.

---

## 4. Padrão de escrita do manual (.md)

- Idioma: **português do Brasil**, tom didático para usuário final.
- Estrutura: Título → objetivo → pré-requisitos → etapas numeradas → dicas.
- Cada etapa: passos numerados + imagem tratada + **tabela** relacionando **nº da seta** (`1.`, `2.`, `3.` — números normais, nunca ①②③) → campo → o que fazer.
- Sinalizar claramente o que é **obrigatório**.
- Caminhos de imagem no `.md` são **relativos** à pasta do manual: `imagens-tratadas/arquivo.png`.

**Onde o número entra no texto, para não gerar ambiguidade.** Duas posições, e só essas:

- **`(N)` inline** no parágrafo **imediatamente antes** da imagem em que a seta N está desenhada
  ("Toque no logo do estabelecimento (1)", e a imagem vem em seguida).
- **Tabela "Nº → o que fazer"** imediatamente **depois** da imagem a que se refere.

Quando a ação está numa imagem **anterior**, escrever **"a seta N da imagem acima"** em vez de
`(N)`. Sem essa regra o leitor não sabe para qual das duas imagens vizinhas o número aponta — e o
risco é real: no #24, um "toque em CONCEDER (2)" ficava colado numa imagem cuja seta 2 era
*AGORA NÃO*. Vale conferir no fim que **toda seta desenhada é citada** e que **todo número citado
existe** na imagem: um script curto que compara o `.md` com os marcadores do `annotate.py` acha
isso em segundos, e foi assim que a ambiguidade apareceu.

---

## 5. Contas de acesso (produção https://beefood.app)

| Conta | Login | Senha | Observação |
|-------|-------|-------|------------|
| beefood1 | `beefood1` | `beefood123` | Conta de teste inicial (tem caixas históricos). |
| **BeeFood3 - Manual** | `contato@beefood.com.br` | `1q2w3e4r` | **Sandbox dedicado aos manuais.** Usar esta. Usuário **Principal**, Gerente, grupo **Administrador2**. |
| caixa.manual | `caixa.manual` | `manual123` | Usuário **restrito** criado em 19/08/2026 para o manual de restrições de caixa. Grupo **Acesso Funcionário**, **sem** função Gerente. Serve para ver o produto com permissões reduzidas. |

> **Telefone de teste no cardápio digital (BeeFood3):** use **(15) 99999-8888**
> (cliente **Teste Manual**, saldo de cashback **R$ 5,00**). Digite **11 dígitos**
> `15999998888` no `input[type=tel]`. Não use telefone de cliente real nas capturas
> (o repositório é público). Cache do cardápio público: até **1 minuto**.

> **Atenção ao testar permissão no login principal:** o usuário Principal **não** ignora as
> restrições do grupo (comprovado). Logo, desligar uma permissão do grupo **Administrador2**
> afeta você. Nunca desligue **Usuários** nesse grupo — você perde a própria tela de
> permissões e não há como religar de dentro do sistema.

> Login em `/login`. A tela mudou em 2026-08: agora são **um campo só** para identificação
> (`input#emailOrWhatsapp`, rótulo "Digite seu e-mail ou WhatsApp") e `input#password`, botão
> **ENTRAR**. Logins que não são e-mail (ex.: `caixa.manual`) entram por esse mesmo campo.
> Demora ~2-4s. **Trocar de conta:** menu de usuário (ícone pessoa, canto sup. direito) → **Sair**.

---

## 6. Ferramentas e procedimentos (navegador)

### No Windows (máquina do dono) — MCP do navegador

- MCP `cursor-ide-browser`: `browser_navigate`, `browser_snapshot`, `browser_take_screenshot`,
  `browser_click`, `browser_fill`, `browser_press_key`, `browser_lock`.
- Fluxo de lock: `navigate` → `lock` → interações → `unlock`.
- Screenshots brutos caem em `C:\Users\T-GAMER\AppData\Local\Temp\cursor\screenshots\`.
  Copiar os escolhidos para `imagens-puras\` do manual.
- **Tema:** SEMPRE **claro/branco** nas capturas. Ativar pelo botão **"Alterar tema"** (canto sup. direito).
- **Depois de cada clique, esperar o spinner sumir e mais 5 segundos antes do
  print.** Mesma regra da seção Playwright — vale no Windows também.
- Refs do snapshot mudam a cada render — pegar snapshot novo antes de clicar se der "Element not found".

### No Cloud Agent (Linux) — capturar com Playwright

O MCP `cursor-ide-browser` **não existe** no Cloud Agent. Lá o navegador é o **Playwright**
(instalado pelo `.cursor/install.sh`), dirigido por script Python. O que funcionou no #2:

- Rodar com `export PATH="$HOME/.local/bin:$PATH"`.
- Logar uma vez e reaproveitar a sessão: `storage_state` salvo em arquivo e passado ao
  `new_context` — evita relogar em cada script (o login leva ~10s).
- `viewport={"width":1440,"height":900}` com `device_scale_factor=1.5` → imagens 2160×1350,
  nítidas o bastante para ler os valores das tabelas.
- Salvar o `screenshot` **direto** em `imagens-puras/` do manual.
- Fechar o **banner promocional** do topo antes de capturar (botão × do banner), senão ele
  aparece em todas as imagens.
- **Espera obrigatória após cada clique (dono, 21/08/2026 — permanente):**
  1. Clique (ou `goto`, ou troca de aba).
  2. Se aparecer `Carregando...`, `Atualizando...`, `Calculando…` ou spinner,
     esperar sumir (timeout 20–30 s).
  3. **Mais 5 segundos** depois do spinner sumir — não durante.
  4. Só então `screenshot`.
  Não basta `wait_for_timeout(400)` / `800` / `1500`. A regra **não é do #43**: é de
  Delivery, PDV, Mesas, Parâmetros, cardápio, área de entrega e qualquer tela nova.
  O #43 saiu com o painel em `Carregando...` e depois com `Atualizando...` no Pronto
  justamente porque o print veio cedo. Helper sugerido:

  ```python
  WAIT = 5000
  def after_click(page):
      for _ in range(30):
          busy = (
              page.locator("text=Carregando...").count()
              or page.locator("text=Atualizando...").count()
              or page.locator("text=Calculando").count()
          )
          if not busy:
              break
          page.wait_for_timeout(1000)
      page.wait_for_timeout(WAIT)
  ```
- **Sempre escopar o clique dentro do modal certo:**
  `page.locator('div[role="dialog"]').filter(has_text="...").last`. As tabelas de fundo têm os
  mesmos textos e as mesmas classes (`bg-green-500`, badges "Débito"), e o clique vai para o
  elemento errado ou fica preso em "subtree intercepts pointer events".
- Quando a tela oferecer **atalho de teclado**, prefira-o ao clique (ex.: `Control+3` para
  escolher Débito no pagamento, `Enter` para confirmar). É mais robusto que caçar seletor.
- Dividir a captura em **scripts curtos por etapa**, deixando as ações irreversíveis (pagar,
  fechar caixa) em scripts separados dos idempotentes — assim é possível repetir a parte que
  falhou sem repetir o que não tem volta.
- **Ler a resposta da API vale mais que ler a tela.** Registrando `page.on("response", ...)` dá
  para imprimir exatamente o que o servidor devolveu (flags de permissão, número de linhas) —
  isso mostra a causa, não só o efeito, e evita conclusão errada por cache de tela.
- **Cuidado com telas que salvam sozinhas.** Configuração → Parâmetros faz auto-save 500 ms
  depois do clique, sem botão Salvar: clicar num switch "só para ver" já altera o ambiente.
  Antes de clicar em qualquer switch, conferir o estado (`data-state`) e anotar para restaurar.
- Para achar o controle de um item quando o texto não é rótulo acessível, localizar o texto e
  **subir os elementos-pai** até encontrar `[role="switch"]` — filtrar `div` por texto costuma
  cair no elemento errado.
- **Ao mudar permissão, relogue.** O front guarda o `config_cache` no `localStorage`; recarregar
  a página não basta. E o servidor guarda o grupo por ~1 min. Ou seja: espere ~70s e faça login
  de novo antes de concluir que a mudança não pegou.
- **Cuidado ao regravar o `storage_state`.** Se você salvar a sessão enquanto uma permissão está
  desligada, o `config_cache` congela nesse estado e a conta parece continuar restrita mesmo
  depois de religar. O sintoma é a tela redirecionar para a home sem erro. A saída é relogar.
- O banner promocional do topo fecha por `button[aria-label="Dispensar"]`.
- **Esconda o widget flutuante de suporte antes de capturar.** É um `div.fixed.bottom-6` de
  56×56 no canto inferior esquerdo e cobre conteúdo de cards baixos. `page.add_style_tag` com
  `div.fixed.bottom-6 { display:none !important }` resolve, sem alterar nada no produto.
- **Diagnostique o estado pela API antes de planejar o manual.** Um script curto que só abre a
  tela e imprime a resposta da listagem já diz quantos registros existem, em que estado estão e
  se há dados suficientes para as capturas — evita planejar imagens que o ambiente não tem.
  Foi assim que se descobriu, antes de escrever qualquer coisa, que as campanhas inteligentes
  já tinham os três estados e dois envios reais para fotografar.
- Alguns elementos ficam em **listas com rolagem própria** (o modal de permissões, por exemplo).
  Aumentar o viewport não resolve; use `scroll_into_view_if_needed()` no item desejado.
- **Campo de hora e de data sai em AM/PM se você não mexer no `LANG` do Chromium.** Telas com
  `input type="time"` (Horário Atendimento) ou `type="date"` (Pausa Programada) renderizam
  "02:30 AM" quando o navegador está em inglês — e o usuário brasileiro vê "02:30". O que corrige
  é a **variável de ambiente do processo**: `launch(env={**os.environ, "LANG": "pt_BR.UTF-8",
  "LANGUAGE": "pt_BR"})`. Testado em 21/08/2026: nem `new_context(locale="pt-BR")` nem o
  argumento `--lang=pt-BR` mudam o formato do campo, só o `env`. Um teste rápido sem OCR: medir a
  largura do campo, que cai de **189 px** (12h) para **137 px** (24h). Vale passar também
  `timezone_id="America/Sao_Paulo"`.
- **Modal nem sempre é `div[role="dialog"]`.** No assistente de horário e no modal de pausa, o
  seletor não casa (o wizard não usa `role=dialog`; o de pausa usa, mas em outro elemento).
  Quando falhar, localize pelo texto do próprio conteúdo ou pelo índice do campo, e confirme com
  um dump de `innerText`.
- **Se o traceback do Playwright citar um seletor que você já trocou**, desconfie de cache do
  script: criar um arquivo novo com outro nome resolveu (visto em 21/08/2026, manual #33).

### Aplicativos Android — o emulador NÃO funciona no Cloud Agent (testado em 2026-08-19)

Investigação completa, para não se repetir o teste:

**O que o ambiente tem de sobra:**

| Recurso | Situação |
|---------|----------|
| Android SDK | Instala em **~40 s** (`commandlinetools-linux`, platform-tools, plataforma 34, emulador, imagens) |
| Java / Node / Yarn | OpenJDK 21, Node 22, Yarn 1.22 — já instalados |
| KVM | **Funciona de verdade.** Teste por `ioctl`: `KVM_CREATE_VM` com sucesso, 4 vCPUs, virtualização aninhada `Y` |
| Display | `DISPLAY=:1` com X ativo, Xvfb disponível |
| Máquina | 4 CPUs, 15 GB de RAM, 233 GB livres |
| `sudo` | Sem senha (dá para `chmod 666 /dev/kvm`) |

**O que não funciona:** o emulador sobe o QEMU, mas **o guest nunca inicia**. Testadas quatro
configurações (imagem `google_apis` com skin de tablet e swiftshader; imagem `default` com
`-gpu off`; a mesma sem Bluetooth; e com `-show-kernel`). Em todas, o log para exatamente na
mesma linha —

```
INFO | Activated packet streamer for bluetooth emulation
```

— e a CPU do QEMU cai para **0,2%**. Com `-show-kernel`, **nenhuma linha do kernel do Android
aparece**: não é lentidão, é travamento antes do boot. O `adb` enxerga `emulator-5554 offline`
indefinidamente. Provável bloqueio de syscall no sandbox do container; o KVM em si está sadio.

**Segundo obstáculo, independente do primeiro:** o **código dos apps não está acessível**. O
token do GitHub alcança 2 repositórios (`beefood-web-react` e `beefood-web-react-manual`), e a
organização no GitHub não tem nenhum projeto Android. O código deve estar no Bitbucket, como o
backend. Os três apps publicados são:

| Pacote | App |
|--------|-----|
| `com.beetechappgarcom` | App Garçom |
| `com.beetechentregador` | BeeFood Entregador |
| `com.cardapiodigitalmesacomanda` | Cardápio Digital Mesa/Comanda (o do tablet) |

> **Confirmado em 20/08/2026 (manual #24):** o código está no Bitbucket, em
> `beetechbr/beetech-appgarcom-android` — na máquina do dono, `c:\projetos\beetech-appgarcom-android`.
> É lá que ficam os `docs/manual-modo-kiosk.md` e `docs/images/kiosk/`. O `BITBUCKET_TOKEN`
> atual **não alcança** esse repositório (Access Token é escopado a um repositório só); o
> `.cursor/install.sh` já tem a entrada e aceita vários tokens via `TOKENS_BITBUCKET`, mas
> falta cadastrar o secret `BITBUCKET_TOKEN_APPGARCOM` — e secret só entra em **VM nova**.

> Sobre `yarn android`: é comando de React Native e **não resolve sozinho** — ele compila e
> instala num device conectado, ou seja, ainda depende de emulador funcionando ou de aparelho
> físico via `adb`.

**Como produzir manual de app Android, então:** as capturas precisam vir de **aparelho real**
(print do próprio Android, ou `scrcpy` espelhando na máquina do dono), ou de um **emulador na
máquina dele** (Android Studio no Windows, onde a virtualização é nativa). O Cloud Agent
continua servindo para escrever o manual, tratar as imagens e documentar a parte **web** do
app (por exemplo, Cardápio Digital Tablet tem as abas Tablets, Layout e Eventos no painel).

### Arquivo anexado no chat NÃO chega ao Cloud Agent (comprovado em 2026-08-20)

Ao pedir o manual do **modo kiosk** (#24), o dono anexou um `manual-modo-kiosk.md` e uma
pasta `images`. **Nenhum dos dois existia no VM.** Foi procurado no repositório, em todo o
histórico do Git, em todas as branches remotas, nos dois repositórios de referência, nas 81
branches do backend no Bitbucket e no sistema de arquivos inteiro (`find /`).

O anexo fica no contexto da conversa. Se o conteúdo não vier **inline no texto da mensagem**,
o agente não tem como abri-lo — e imagem nunca vem inline.

> **Correção, no mesmo dia:** existe um caso em que o anexo **chega**. Quando o arquivo é
> enviado como **documento**, ele é gravado em
> `~/.cursor/projects/workspace/uploads/<nome>_<hash>.<ext>` — foi assim que o
> `manual-modo-kiosk.md` do #24 finalmente chegou. **Antes de concluir que um anexo não
> existe, olhe essa pasta.** Arquivos gravados lá vêm com **CRLF**; converter com
> `tr -d '\r'` antes de comparar com algo do repositório.

**Imagem é a exceção, e isso importa muito para este projeto.** Testado cinco vezes em
20/08/2026: imagem enviada no chat aparece para o modelo (ele descreve o conteúdo sem
dificuldade) mas **nunca** vira arquivo em `uploads/` — não há como gravá-la em disco nem
commitá-la. Foi o que travou as 21 capturas do #24.

O agente recebe a imagem já decodificada, como imagem, sem caminho em disco e sem URL.
Não existe, portanto, "baixar a imagem do chat": não há de onde baixar. É a pergunta que o
dono fez em 20/08 e a resposta é essa. Também não serve reproduzir a tela desenhando algo
parecido: o manual precisa da captura real do aplicativo.

> **O `.zip` era a aposta, e ela falhou na prática.** A ideia era boa — zip não é imagem,
> então deveria cair em `uploads/` como qualquer documento. Só que na tentativa de 20/08 o
> `.zip` **não chegou** (`uploads/` seguiu com apenas o `.md`), e as imagens vieram outra vez
> como imagem no chat. Trate o zip como caminho **não confirmado**: vale tentar, mas não
> planeje o manual em cima dele.

### O caminho que resolve: zip numa URL pública (o agente baixa)

**O VM tem saída de internet liberada.** Confirmado em 20/08/2026 pelo
`cursor-cloud-environment-info`, que devolve `egress: { restricted: false }`. Ou seja: não há
allowlist de domínios, e o agente alcança qualquer host. `drive.google.com`, `docs.google.com`
e `github.com` foram testados com `curl` e respondem.

**Então o jeito de mandar imagem para o Cloud Agent é publicá-la numa URL e passar o link.**
Google Drive serve, e qualquer host que devolva o arquivo também. **Confirmado na prática no
mesmo dia:** foi assim que as 21 capturas do #24 entraram no repositório — um `.zip` de 20 MB
no Drive, baixado e distribuído em uma rodada. Duas regras:

1. **Link de ARQUIVO (um `.zip`), não de pasta.** Pasta do Drive não dá para baixar sem
   credencial. Compacte, suba o `.zip`, compartilhe o `.zip`.
2. **Compartilhamento em "qualquer pessoa com o link".** Sem isso o Drive devolve a página de
   login, e o que chega é HTML em vez de arquivo.

O `manuais/cardapio-digital-tablet-modo-kiosk/copiar-imagens.py` já aceita URL como origem:
baixa, confere que é zip de verdade, extrai e alimenta `imagens-puras/` — as tratadas ficam por
conta do `annotate.py`. Link de compartilhamento do Drive é convertido sozinho para o endpoint de
download direto (`drive.usercontent.google.com/download?id=…&confirm=t`), porque o link normal
devolve a página de visualização, não o arquivo. **Vale copiar essa função em qualquer manual
cujas capturas venham de fora.**

**O que resolve de verdade, para capturas que moram em outro repositório:** dar ao ambiente
acesso a esse repositório, para o agente pegar os arquivos na origem em vez de depender de
anexo. É o caso do #24: as capturas estão em `beetechbr/beetech-appgarcom-android`, em
`docs/images/kiosk/`. O `.cursor/install.sh` já lista o repositório e já aceita vários tokens
(`TOKENS_BITBUCKET`); falta apenas cadastrar o secret `BITBUCKET_TOKEN_APPGARCOM`, porque um
Repository Access Token é escopado a **um** repositório e o `BITBUCKET_TOKEN` atual só alcança
o `beetech-server-node-2.0` (a API responde **404** para o repo do app). Lembrando que
**secret novo só entra em VM nova**.

**Enquanto isso, o caminho mais curto é o dono commitar os arquivos.** Foi assim que 13 das
14 pastas de imagens deste repositório nasceram — só a do `campanhas-inteligentes` foi
capturada por agente, e porque aquele manual é do painel web, que o agente alcança com o
Playwright. Manual de aplicativo Android não tem esse atalho.

**Como mandar material para o Cloud Agent, em ordem de preferência:**

1. **Commitar no repositório** (numa branch) e citar o caminho no pedido. Funciona para texto
   e imagem, e ainda deixa o material versionado.
2. **Colar o texto no corpo da mensagem.** Resolve o `.md`, não resolve as imagens.
3. **Liberar o repositório de origem:** GitHub via `repositoryDependencies` + GitHub App;
   Bitbucket via Repository Access Token em secret + entrada em `REFERENCIAS_BITBUCKET`
   (lembrando que **secret só entra em VM nova**).

> O `BITBUCKET_TOKEN` de hoje é **escopo de repositório**: alcança apenas
> `beetechbr/beetech-server-node-2.0`. Listar o workspace `beetechbr` pela API retorna
> `size: 1`. Qualquer outro repositório do Bitbucket (app Android, totem, servidores) está
> fora do alcance.
>
> Detalhe útil: a API do Bitbucket **exige `Authorization: Bearer <token>`** com esse tipo de
> token. `curl -u x-token-auth:<token>` devolve **401** na API, embora funcione no `git`.

---

## 7. Regras de segurança em produção

- Decisão vigente: o ambiente "BeeFood3 - Manual" é **sandbox** → pode-se executar fluxos reais
  (abrir caixa, criar venda baixa, pagar) para o manual ficar fiel.
- Em contas que NÃO sejam sandbox: **não** finalizar vendas/pagamentos reais sem autorização.
- Nunca fazer ações destrutivas/irreversíveis sem confirmar com o usuário.

### Técnica do ensaio (para passos irreversíveis)

Muitas telas só gravam no clique final (fechar caixa, conferir, confirmar). Nesses casos,
**execute o fluxo inteiro uma vez sem o clique final**, capture tudo, revise as imagens e só
então repita para valer. Foi assim nos manuais de fechar caixa e de segunda conferência, e
evitou queimar cenários que não têm volta. Ao automatizar, mantenha o passo irreversível num
script separado dos idempotentes.

**Antes de capturar, leia no código o que grava.** Vale conferir três coisas: se a tela tem
auto-save (Parâmetros e a configuração do Cashback têm; o editor de campanha inteligente não
tem), em que linha o `handleSave` realmente chama a API, e o que um switch faz de fato. No
editor de campanha inteligente, por exemplo, o switch do card apenas abre um diálogo de
confirmação e o salvamento com a proteção anti-spam desligada retorna antes da API — o que
permitiu fotografar até o alerta vermelho de banimento sem alterar nada. Cinco minutos de
leitura de código evitam capturas em ambiente sujo ou cenários queimados.

### Dado pessoal em captura

O repositório é **público**. Quando a tela mostra nome, telefone ou e-mail de cliente, cubra na
imagem **pura**, não só na tratada — a pura também é versionada. No manual de segmentação isso
foi feito com borrão via `annotate.py`; no de campanhas inteligentes, com uma tarja e um
telefone fictício aplicados na pura antes do primeiro commit.

---

## 8. Stack do projeto (código) — referência

React 18 + TypeScript + Vite + Tailwind + shadcn/ui; react-router-dom v6; Supabase + API DataSnap
(`/datasnap/rest/...`); @tanstack/react-query; react-hook-form + zod. Versão em produção: `v3.190826.x`
(conferida em 19/08/2026 no rodapé do menu lateral).
Estrutura: `src/pages`, `src/components`, `src/hooks`, `src/contexts`, `src/integrations`.
Obs.: ainda **não existe `spec.md`** no projeto (a regra do projeto pede criar — pendente).

### Onde fica o código (por máquina)

| Máquina | Caminho do `beefood-web-react` |
|---------|--------------------------------|
| Windows (dono) | `C:\projetos\beefood-web-react` |
| Cloud Agent | `~/refs/beefood-web-react` (clone raso, **somente leitura**) |

No Cloud Agent o clone é feito pelo `.cursor/install.sh`. Para o clone funcionar são
necessárias **duas** liberações: o repositório precisa estar selecionado no **GitHub App do
Cursor** (configurações da org) **e** listado em `repositoryDependencies` no
`.cursor/environment.json` — esse campo não clona nada, ele só inclui o repositório no token
gerado para o ambiente. Faltando qualquer uma das duas, o clone falha com
`Repository not found`.

**O acesso vale durante a sessão inteira** (verificado em 2026-08-19). Dentro da sessão o
`git fetch origin main` em `~/refs/beefood-web-react` funciona normalmente, e `gh` também
enxerga o repositório. Ou seja: **dá para atualizar o código no meio do trabalho**, sem
precisar de uma sessão nova.

> Correção: até 2026-08-04 esta seção afirmava que o escopo valia só durante o install e que
> o código ficava congelado. Não é mais o caso.

Para conferir o que o token alcança: `gh api /installation/repositories -q '.total_count,
(.repositories[].full_name)'`. Hoje retorna **2**: `beefood-web-react` e
`beefood-web-react-manual`. Qualquer outro repositório (ex.: os de servidor, usados para
importar manuais de integração) responde **404** — e 404 aqui é ambíguo: significa "não
existe" **ou** "não liberado". Para liberar, são necessárias as duas coisas descritas acima
(GitHub App + `repositoryDependencies`).

### Referências no Bitbucket (backend)

`repositoryDependencies` **não serve** para Bitbucket: ele só amplia o token do GitHub. Para
clonar um repositório do Bitbucket no Cloud Agent:

1. No Bitbucket, em **Repository settings → Security → Access tokens**, criar um
   **Repository Access Token** com escopo **Repositories: Read** (só leitura, e limitado
   àquele repositório).
2. No **Cursor Dashboard → Cloud Agents → Secrets**, guardar o valor como `BITBUCKET_TOKEN`.
3. Adicionar a entrada em `REFERENCIAS_BITBUCKET`, no `.cursor/install.sh`, no formato
   `workspace/repositorio#branch` (o `#branch` é opcional). O clone tenta os dois usuários
   possíveis (`x-token-auth` para Access Token, `x-bitbucket-api-token-auth` para Atlassian
   API token) e depois **regrava o remote sem o token**.

Sem o secret, o bloco é ignorado e o setup segue normalmente.

| Máquina | Caminho do backend |
|---------|--------------------|
| Cloud Agent | `~/refs/beetech-server-node-2.0` (branch `beefood-web-react`, clone raso, só leitura) |

> **Secret só entra em VM nova.** O `BITBUCKET_TOKEN` é injetado no boot do ambiente. Criar o
> secret no meio de uma sessão não o disponibiliza para a sessão em andamento — o clone só
> acontece no install da **próxima** sessão.

> **Funcionou.** Desde 2026-08-19 o backend está clonado e disponível em
> `~/refs/beetech-server-node-2.0` (branch `beefood-web-react`). Ele tem um `spec.md` próprio
> na raiz. Foi o que permitiu fechar o estudo do manual #13: só o código do servidor explicou
> por que o parâmetro "Caixa por Usuário" não fazia o que a tela promete.

> **Cuidado com repositório público.** Este repositório de manuais é público. Secret de
> ambiente em repositório público é risco real: quem puder abrir um Cloud Agent nele recebe a
> variável injetada — e o Cursor pode até bloquear a injeção por padrão nesse caso. Antes de
> cadastrar um token do backend, **torne este repositório privado**. A decisão de deixá-lo
> público (seção 11) valia para credenciais descartáveis de teste, não para acesso ao
> código-fonte do servidor.

---

## 9. Índice de manuais

| Manual | Pasta | Status |
|--------|-------|--------|
| Caixa (abrir, receber, consultar) | `manuais\caixa\` | ✅ Concluído |
| Fechar caixa (vendas pendentes, 1ª conferência, quebra) | `manuais\caixa-fechar\` | ✅ Concluído |
| Segunda conferência (dupla checagem, resolve a quebra) | `manuais\caixa-conferencia-2\` | ✅ Concluído |
| Restrições de caixa (grupo de acesso) | `manuais\caixa-restricoes\` | ✅ Concluído |
| Segmentação de clientes (Food Marketing) | `manuais\segmentacao-clientes\` | ✅ Concluído |
| Reforma Tributária (IBS/CBS) | `manuais\reforma-tributaria-ibscbs\` | ✅ Concluído |
| Ativação Aiqfome V2 | `manuais\ativacao-aiqfome\` | ✅ Concluído |
| Integração Machine | `manuais\integracao-machine\` | ✅ Concluído |
| Integração 99 Entrega | `manuais\integracao-99-entrega\` | ✅ Concluído |
| Integração Repediu | `manuais\integracao-repediu\` | ✅ Concluído |
| Integração FoodCRM | `manuais\integracao-foodcrm\` | ✅ Concluído |
| Integração Uber Direct | `manuais\integracao-uber-direct\` | ✅ Concluído |
| Segmentação de clientes | `manuais\segmentacao-clientes\` | ✅ Concluído |
| Campanhas Inteligentes | `manuais\campanhas-inteligentes\` | ✅ Concluído |
| Avisos do cardápio digital | `manuais\cardapio-digital-avisos\` | ✅ Concluído |
| Capas e Destaques | `manuais\cardapio-digital-capas-destaques\` | ✅ Concluído |
| Pixel Meta + API de Conversões | `manuais/pixel-meta-api/` | ✅ Concluído |
| Pixel Meta somente | `manuais/pixel-meta-somente/` | ✅ Concluído |
| Mapas do Google | `manuais/mapas-google/` | ✅ Concluído |
| Domínio próprio | `manuais/dominio-proprio/` | ✅ Concluído |
| TEF Stone (AutoTEF) | `manuais/tef-stone/` | ✅ Concluído |
| TEF PayGo | `manuais/tef-paygo/` | ✅ Concluído |
| Gaveta de dinheiro | `manuais/gaveta-dinheiro/` | ✅ Concluído |
| Mercado Pago | `manuais/mercado-pago/` | ✅ Concluído |
| BeeFood Entregador (app motoboy) | `manuais/app-entregadores/` | ✅ Concluído |
| IA ChatGPT no WhatsApp | `manuais/ia-chatgpt-whatsapp/` | ✅ Concluído |
| Campanhas SMS | `manuais/campanhas-sms/` | ✅ Concluído |
| Cupom de Desconto | `manuais/cupom-desconto/` | ✅ Concluído |
| Entrega Fácil iFood | `manuais/entrega-facil-ifood/` | ✅ Concluído |
| Let's Express | `manuais/integracao-lets-express/` | ✅ Concluído |
| Foody Delivery | `manuais/integracao-foody-delivery/` | ✅ Concluído |
| Pick n Go! | `manuais/integracao-pick-n-go/` | ✅ Concluído |
| Uai Rango | `manuais/integracao-uai-rango/` | ✅ Concluído |
| Desconto nas formas de recebimento | `manuais/cardapio-digital-desconto-formas/` | ✅ Concluído (#64) |
| Taxas das formas de recebimento | `manuais/taxas-formas-pagamento/` | ✅ Concluído (#65) |
| Lançamentos: contas a pagar | `manuais/lancamentos-contas-pagar/` | ✅ Concluído (#66) |
| Lançamentos: contas a receber | `manuais/lancamentos-contas-receber/` | ✅ Concluído (#67) |
| Exibir / Ocultar | `manuais/exibir-ocultar/` | ✅ Concluído (#68) |
| Preço Programado | `manuais/preco-programado/` | ✅ Concluído (#69) |
| Agendamento do cardápio digital | `manuais/cardapio-digital-agendamento/` | ✅ Concluído (#70) |
| Aparência e layout do cardápio digital | `manuais/cardapio-digital-aparencia-layout/` | ✅ Concluído (#71) |

### Exibir/Ocultar e Preço Programado — #68 e #69

Mesmo modal (`ModalTabelaPreco`). **Exibir / Ocultar** força
`ocultar=0` (Ocultar Item). **Preço Programado** manda `?preco=1` e
força `ocultar=1` (Alterar Preço), sem produto de rodízio. Permissão
do Preço Programado no menu é `rodizio`. Rodízio de verdade é
`/rodizio` (só presencial + produto vinculado).

Canal **Cardápio Digital** = `beeshop`. Sem ele o menu público não
muda. Dias vazios = tabela `0d` e não vale. Aba Produtos numa tabela
nova **salva a config sozinha**. Desconto em massa só depois de
selecionar o produto. Cache do cardápio público: até **5 minutos**.

No card da lista do Preço Programado o front esconde Delivery e
Cardápio Digital (`!isRodizio`) — só o Presencial aparece; os três
canais estão no modal.

Sandbox (30/08/2026): **Ocultar Brownie (manual)** ativa; **Happy
hour milk-shake (manual)** ativa (Milk Shake 18,90 → 15,12).

---

### Agendamento do cardápio digital — #70

Aba `tab=agendamento`, auto-save 800 ms (unmount sem flush). Campo
inválido não grava. O cardápio Vue (`menu.beefood.com.br`) abre
**AGENDAR PEDIDO** depois de Entrega/Retirada: faixa **Dia** + lista
**Hora Aproximada** (faixas de 30 min; `agendaInterM` é o passo entre
inícios). `agendaAgoraM` só mexe no dia de hoje. `agendaMinAntes` =
minutos **depois** de abrir. Preencher vários `input` via Playwright
e sair perde o save — gravar pelo POST autenticado e recarregar.

---

### Aparência e layout do cardápio digital — #71

Card **Aparência** em `/cardapio-digital?tab=configuracoes`. Auto-save
800 ms (POST do snapshot inteiro). Capa fixa = `fotoCapa`; logo =
`logotipoS3Link`; tema = `corPrimaria`; capa vazia = `corAcao`.
`layoutSetor` / `layoutStepCarrinho` boolean. Vitrine =
`exibirPromocoes` + `abrirPromocoesAuto`. Capa/logo: clique no
preview, máx 1 MB, sem recorte. **Não** é o modal de banners (#48).
O preview sticky (xl) reflete na hora; o Vue público pode atrasar
o cache. Clique “só para ver” já grava.

---

### Lançamentos (Financeiro) — #66 e #67

Rota `/contas-pagar-receber`. Uma tela, 3 abas: **Contas a pagar** /
**Contas a receber** / **Todos**. **+ Novo (F1)** → **Despesa** (−) ou
**Receita** (+). Formas do lançamento = topo de Formas Pagamento.

Venda **paga** já vira conta a receber (categoria **Receita de Pedidos**,
valor = **líquido** da taxa do #65). Receita extra: categoria fixa
**Outras Receitas**. Sem contas bancárias no sandbox — deixar Conta
vazia.

Sandbox (30/08/2026): **Aluguel do ponto** R$ 800 Pix pago; **Máquina
de café** 2× R$ 150 Boleto (1/2 no mês); **Patrocínio da festa junina**
R$ 200 Pix recebido; venda **#915** no receber (14,00 → 13,69).

Fora deste par: Recebimentos/Pagamentos agregados, DRE, cadastros,
Fluxo Caixa (*Em breve!*).

---

## 10. Como retomar o trabalho (checklist de início de sessão)

1. Ler este `MEMORIA-GERAL.md`.
2. Se a sessão for da fila do ajuda.beefood, ler `PLANO-MIGRACAO-AJUDA.md`. A fila **#49–#56** já foi produzida. O **#57** (app Entregador) e o **#58** (IA ChatGPT no WhatsApp) foram pedidos depois e também já estão prontos.
3. Ler a `MEMORIA.md` do manual em andamento (se houver).
4. Logar em `contato@beefood.com.br` e ativar tema claro.
5. Conferir estado da funcionalidade no sistema antes de capturar.

---

## 11. Versionamento (Git/GitHub) — REGRA DE COMMIT POR AÇÃO

- Repositório remoto: `git@github.com:BeeFood-Sistema-para-Restaurantes/beefood-web-react-manual.git` (branch `main`).
- **REGRA DE OURO:** após **cada ação relevante** (criar/editar manual, gerar imagens,
  ajustar `annotate.py`, atualizar memórias, etc.), fazer **`commit` + `push` automaticamente**
  (sempre os dois!) — sem precisar pedir autorização. Mensagens claras e descritivas em português.
- **Sempre subir tudo:** todo commit deve ser seguido de `git push origin main`. Não deixar
  commits acumulados só localmente.
- Padrão de mensagem: verbo no presente + escopo. Ex.:
  `docs(caixa): adiciona etapa de consulta do valor em caixa`,
  `chore(anotacao): setas em verde e mais sutis`,
  `feat(manual): inicia manual de delivery`.
- Não versionar segredos novos: usar `.gitignore` (ex.: `credenciais.local.md`, `.env`).
  > **Decisão do dono:** as contas usadas são de uma **empresa de TESTES** (credenciais
  > descartáveis). Portanto as senhas PODEM ficar versionadas e o repositório PODE ser
  > **público** sem problema. Não tratar essas credenciais como segredo crítico.

---

## 12. `texto-documentation.ia.md` — PROMPT pronto por manual (OBRIGATÓRIO)

Para o dono **publicar** um manual, ele cola um **texto de criação** no construtor de documentação do
app (que gera a página dentro do BeeFood). Por isso, **todo manual concluído DEVE ter** um arquivo
`texto-documentation.ia.md` na sua pasta, contendo esse texto **pronto para copiar e colar**.

**Princípio:** o projeto do manual **já vem anexo no contexto**. O prompt deve ser **direto e listar os
arquivos EXATOS a ler** (o `<nome>.md` + os caminhos das imagens em `imagens-tratadas/`) e dizer
explicitamente **"NÃO varra/leia o resto do projeto"** (nada de `fluxo-codigo.md`, `MEMORIA*.md`,
`annotate.py`, `imagens-puras/`). Isso evita que a IA leia o projeto inteiro.

**O que o arquivo deve conter:**
1. Um bloco **PROMPT (copiar e colar)** com:
   - **Onde criar o menu** (ex.: "Em **Fiscal**, crie um novo item por último chamado **\<Nome\>**").
   - **Lista explícita dos arquivos a ler** (somente esses): o **`<nome>.md`** (conteúdo na íntegra) e os **caminhos de cada imagem** em `imagens-tratadas/` (na ordem).
   - Frase clara de **"NÃO ler outros arquivos do projeto"**.
   - A instrução: **"faça a apresentação das imagens igual ao menu 'Abrir Caixa'"** (padrão de referência).
2. **Estrutura da página** (seções, na ordem do `<nome>.md`).
3. **Tabela de imagens** na ordem, com tipo (contexto / com setas) e legenda.
4. **Observações de conteúdo** (idioma, destaques obrigatórios, o que NÃO publicar — ex.: `fluxo-codigo.md`).

**Modelo mínimo:**

```md
# texto-documentation.ia.md — <Nome do Manual>

## PROMPT (copiar e colar)
Em <Seção>, adicione um item de menu por último chamado "<Nome>".

Leia APENAS os arquivos abaixo (não varra o resto do projeto):
1. Conteúdo (use na íntegra): beefood-web-react-manual/manuais/<pasta>/<nome>.md
2. Imagens (nesta ordem): beefood-web-react-manual/manuais/<pasta>/imagens-tratadas/<arquivos...>

NÃO leia outros arquivos (fluxo-codigo.md, MEMORIA*.md, annotate.py, imagens-puras/).

- Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa".
- pt-BR, didático; destacar obrigatórios; não publicar o rodapé "Referências internas".

## Anexo — legendas das imagens (na ordem)
| Ordem | Arquivo (em imagens-tratadas/) | Tipo | Legenda |
| ... |
```

> Referência viva: `manuais\reforma-tributaria-ibscbs\texto-documentation.ia.md`.
