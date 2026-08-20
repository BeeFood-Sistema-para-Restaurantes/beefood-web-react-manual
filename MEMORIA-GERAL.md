# MEMÓRIA GERAL — Boas práticas para criação de manuais BeeFood

> Memória mestre do projeto de manuais. **Ler SEMPRE no início de cada sessão.**
> Cada manual tem ainda sua própria `MEMORIA.md` dentro da sua pasta.

Última atualização: 2026-08-20 (ler no código o que grava antes de capturar; dado pessoal
coberto na imagem pura; widget flutuante escondido por CSS; diagnóstico do ambiente pela API;
anexo do chat não chega ao Cloud Agent; escopo real do `BITBUCKET_TOKEN`; backend clonado no
Cloud Agent; tela de login mudou; telas com auto-save; captura com Playwright)

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
6. As imagens em produção saem em **1508×1274** (DPR alto). `annotate.py` usa coordenadas
   em **frações 0..1**, então independe da resolução.
7. **Dados pessoais de clientes precisam sair ilegíveis.** Telas que listam clientes (nome,
   telefone, e-mail) não podem ir para o repositório como estão — ele é **público**. A decisão
   da seção 11 vale para as *credenciais* de teste, não para dados de terceiros. O `annotate.py`
   de `manuais\segmentacao-clientes\` tem o parâmetro `borrao` (regiões em frações, aplicadas
   com `GaussianBlur` antes das setas); copie de lá quando precisar.

### Como anotar (Pillow)
- Requisitos: Python 3.10+ e Pillow (já instalados nesta máquina).
- `annotate.py` lê de `imagens-puras\` e escreve em `imagens-tratadas\`.
- Config por imagem: lista de marcadores `(numero, alvo_x, alvo_y, badge_x, badge_y)` em frações.
- Rodar dentro da pasta do manual: `python annotate.py`.
- **Sempre conferir visualmente** as imagens tratadas e ajustar coordenadas se necessário.

---

## 4. Padrão de escrita do manual (.md)

- Idioma: **português do Brasil**, tom didático para usuário final.
- Estrutura: Título → objetivo → pré-requisitos → etapas numeradas → dicas.
- Cada etapa: passos numerados + imagem tratada + **tabela** relacionando **nº da seta** (`1.`, `2.`, `3.` — números normais, nunca ①②③) → campo → o que fazer.
- Sinalizar claramente o que é **obrigatório**.
- Caminhos de imagem no `.md` são **relativos** à pasta do manual: `imagens-tratadas/arquivo.png`.

---

## 5. Contas de acesso (produção https://beefood.app)

| Conta | Login | Senha | Observação |
|-------|-------|-------|------------|
| beefood1 | `beefood1` | `beefood123` | Conta de teste inicial (tem caixas históricos). |
| **BeeFood3 - Manual** | `contato@beefood.com.br` | `1q2w3e4r` | **Sandbox dedicado aos manuais.** Usar esta. Usuário **Principal**, Gerente, grupo **Administrador2**. |
| caixa.manual | `caixa.manual` | `manual123` | Usuário **restrito** criado em 19/08/2026 para o manual de restrições de caixa. Grupo **Acesso Funcionário**, **sem** função Gerente. Serve para ver o produto com permissões reduzidas. |

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
- **Esperar bastante:** os modais de caixa levam de 8 a 13 segundos para carregar os dados.
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

### Arquivo anexado no chat NÃO chega ao Cloud Agent (comprovado em 2026-08-20)

Ao pedir o manual do **modo kiosk** (#24), o dono anexou um `manual-modo-kiosk.md` e uma
pasta `images`. **Nenhum dos dois existia no VM.** Foi procurado no repositório, em todo o
histórico do Git, em todas as branches remotas, nos dois repositórios de referência, nas 81
branches do backend no Bitbucket e no sistema de arquivos inteiro (`find /`).

O anexo fica no contexto da conversa. Se o conteúdo não vier **inline no texto da mensagem**,
o agente não tem como abri-lo — e imagem nunca vem inline.

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

---

## 10. Como retomar o trabalho (checklist de início de sessão)

1. Ler este `MEMORIA-GERAL.md`.
2. Ler a `MEMORIA.md` do manual em andamento (se houver).
3. Logar em `contato@beefood.com.br` e ativar tema claro.
4. Conferir estado da funcionalidade no sistema antes de capturar.

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
