# MEMÓRIA — Manual de Restrições de Caixa (por grupo de acesso)

> Memória detalhada deste manual. **O estudo está concluído**; falta produzir.
> Ver também: `../../MEMORIA-GERAL.md`, `../caixa-fechar/` e `../caixa-conferencia-2/`.

Status: 🔨 **Em execução** — estudo concluído em 2026-08-19 (incluindo a leitura do backend,
que fechou a última pendência); produção aguardando aprovação do plano.

---

## 1. Escopo aprovado pelo dono

Manual **único** explicando **todas** as restrições de caixa que podem ser aplicadas a um
usuário, como configurar cada uma e como o caixa fica depois.

Decisões dele, já fechadas:

- **Formato:** dividido por restrição, em pares — *como fazer 1 e como fica*, *como fazer 2 e
  como fica*, e assim por diante. Não é por perfil de usuário.
- **Escopo completo:** inclui o que não está no grupo de acesso (Função Gerente, parâmetro
  Caixa por Usuário, Cadastro de Caixas).
- **Numeração `1, 2, 3`** no texto (nunca `①②③`).
- Autorizado **criar usuário de teste** e **mexer nos switches** do grupo "Acesso Funcionário".
- Mobile fora do escopo (padrão dos manuais anteriores).

---

## 2. Onde se configura

**Configuração → Usuários → aba Grupos de Acesso → clicar no grupo** abre o modal
*Editar Grupo: \<nome\>*, com as permissões agrupadas por recurso, busca e filtro.

Dois comportamentos da tela que precisam entrar no manual:

1. **Cada switch salva na hora**, individualmente. O botão **Salvar** do rodapé serve apenas
   para o campo **Descrição** do grupo.
2. A **busca esconde os sub-itens** quando o texto não casa com eles. Buscar "Abrir e Fechar"
   não mostra as sub-permissões; buscar "caixa" mostra. Isso engana quem procura.

API por trás: `GET /api/empresa2/grupoAcesso/{empresaID}/{usuarioID}/{grupoAcessoID}` lista os
itens; `POST /api/empresa2/grupoAcessoItem` grava cada toggle.

---

## 3. As restrições e o efeito de cada uma (TESTADO)

Todos os efeitos abaixo foram comprovados ao vivo em 19/08/2026, desligando uma permissão por
vez e observando o caixa do usuário restrito. Tudo foi religado depois.

| # | Restrição | Onde | Efeito ao DESLIGAR | Flag na API de caixa |
|---|-----------|------|--------------------|----------------------|
| 1 | **Abrir e Fechar Caixa** | Grupo → Venda | O menu **Caixa** desaparece e o acesso direto a `/caixa` redireciona para a home | `sidebar.menu.caixa` (itemID 42) |
| 2 | **Visualizar Valores de Referência** | sub-item de 1 | Somem as colunas **Saldo Final**, **Conf. Saldo Final** e **Quebra de Caixa** na listagem; o painel **Resumo** fica "Nenhum resumo disponível"; na conferência somem **Entrada, Saída, Saldo e Diferença**; somem os botões **Reabrir Caixa** e **Ver Conferência** | `itemID136` |
| 3 | **Visualizar Caixas Fechados** | sub-item de 1 | A listagem passa a mostrar **só o caixa aberto** (no teste: de 10 linhas para 1) | `itemID212` |
| 4 | **Transferência de Operações** | sub-item de 1 | Somem o botão **TRANSFERIR** e, dentro do modal do caixa, os botões **Cancelamentos** e **Excluídos** | `itemID227` |
| 5 | **Cadastro de Caixas** | Grupo → Empresa | Esconde **Configuração → Caixa** (cadastro dos terminais) | `submenus.configuracao.items.caixa` (itemID 34) |
| 6 | **Função Gerente** | Cadastro do **usuário** | Sem ela, a aba **Cancelamentos** não aparece | flag `gerente` do cache |
| 7 | **Usuário Fixo** | Cadastro do **caixa** | Vinculado a um usuário, ele passa a ver **só os caixas que ele mesmo abriu** (ver seção 4) | `_sat.UsuarioID` |

A restrição **2** é a mais interessante do manual: ela cria uma **conferência cega** — o
operador digita o que contou sem ver quanto o sistema esperava.

### Duas dúvidas que já foram respondidas por teste

- **Usuário Principal NÃO tem bypass.** Desligamos "Transferência de Operações" no grupo
  Administrador2 e o botão TRANSFERIR desapareceu para o `contato@beefood.com.br`
  (`itemID227: false`). Ou seja: dá para testar no próprio login — mas **nunca desligar
  "Usuários"**, senão o próprio acesso à tela de permissões é perdido e não há como religar.
- **Sangria e Acréscimo não têm permissão própria.** O usuário restrito lançou um acréscimo e
  o servidor respondeu **200**. Quem tem "Abrir e Fechar Caixa" opera o caixa. O erro
  *"Usuário sem permissão para realizar operações no caixa"* que existe no front é defensivo,
  para outro cenário.

### Refinamentos que só o backend revelou (19/08/2026)

O código confirmou os efeitos acima e acrescentou três coisas que o teste de tela não mostrou:

1. **A checagem de permissão da sangria/acréscimo existe, mas está desativada.** Em
   `caixa2/operacaoManual.js` o bloco que devolveria 403 está **comentado**:

   ```js
   /*let checkAcesso = await checkAcessoItemID(empresaID, usuarioID, 136);
   if (!checkAcesso) {
       return res.status(403).json({ ... "Usuário sem permissão para realizar operações no caixa" });
   }*/
   ```

   É a origem exata da mensagem que aparece no front e a explicação do 200 que observamos.
   Vale a mesma conclusão de antes — **não existe permissão de sangria/acréscimo hoje** — mas
   agora sabemos que a intenção era amarrá-la ao mesmo item da restrição 2.

2. **"Transferência de Operações" também esconde os Cancelamentos e os Excluídos do modal do
   caixa.** No front, `CaixaVerModal.tsx` faz `const showTabs = data?.itemID227;` e usa esse
   mesmo `showTabs` para os botões de **Cancelamentos** e **Excluídos** dentro do modal. No
   teste de tela só tínhamos notado o TRANSFERIR; a linha 4 da tabela acima já está corrigida.

3. **A aba Cancelamentos da tela `/caixa` exige três coisas, não só a função Gerente.** Em
   `hooks/useCaixaData.ts`:

   ```ts
   const showCancelamentos = data?.itemID136 && data?.itemID212 && isGerente;
   ```

   Ou seja, desligar a restrição 2 **ou** a restrição 3 também derruba a aba Cancelamentos —
   não só tirar a função Gerente. Além disso, `caixa2/caixaDetalhes.js` só busca resumo,
   excluídos e cancelamentos quando o `itemID136` está ligado: sem ele, os dados nem saem do
   servidor.

**Onde o servidor bloqueia de fato (e não só esconde botão):**

| Operação | Rota | Validação |
|----------|------|-----------|
| Transferir operações | `caixa2/caixaTransferir` | `checkAcessoItemID(..., 227)` → **403** "Usuário sem permissão para realizar transferências no caixa" |
| Sangria / Acréscimo | `caixa2/operacaoManual` | **nenhuma** (checagem comentada) |
| Listar caixas | `caixa2/caixaListagem` | `136` zera os valores na própria query; `212` acrescenta `and v.dataFechamento is null` |
| Detalhes do caixa | `caixa2/caixaDetalhes` | `136` corta resumo/excluídos/cancelamentos; devolve `itemID136` e `itemID227` |
| Fechar caixa | `caixa2/caixaFechar` | devolve `itemID136`, mas a query está com `if (true /*itemID136*/)` — quem esconde os valores é o front |

Detalhe relevante: `checkAcessoItemID` devolve **`true` por padrão** quando não encontra o item
no grupo. Permissão que não existe na base é permissão liberada.

---

## 4. RESOLVIDO — o que "Caixa por Usuário" faz de verdade

> Fechado em 19/08/2026 com o backend (`~/refs/beetech-server-node-2.0`) em mãos, e confirmado
> por teste ao vivo. **Esta era a única pendência do estudo.**

### 4.1. O parâmetro não tem nada a ver com o caixa

Varredura por `caixaPorUsuario` no backend inteiro: aparece em **quatro** arquivos, e nenhum
deles é de caixa.

| Arquivo | Papel |
|---------|-------|
| `empresa2/empresaConfigGET.js` | lê o valor para a tela de Parâmetros |
| `empresa2/empresaConfigPOST.js` | grava o `UPDATE _EmpresaConfig` |
| `models/cache/cacheOthers.js` | carrega o campo no cache da empresa |
| **`venda2/historicoVendas.js`** | **único consumidor real** |

Nenhuma das rotas de caixa (`caixa2/caixaListagem`, `caixa2/caixaDetalhes`,
`caixa2/abrirCaixa`, `caixa2/operacaoManual`, `caixa2/caixaTransferir`) sequer importa o
parâmetro. No front é igual: `caixaPorUsuario` só aparece em `pages/Parametros.tsx`,
`hooks/useEmpresaParametros.ts` e no tipo de `utils/configCache.ts` — nunca em componente de
caixa.

Ou seja: **a descrição em tela ("Cada usuário tem e só consegue ver seu próprio caixa") não
corresponde ao que o código faz.** O comportamento observado no produto não era um bug do
teste — o parâmetro realmente não filtra caixa nenhum.

O único uso, em `historicoVendas.js`, é este:

```js
const caixaPorUsuario = empresaConfig && empresaConfig.caixaPorUsuario === true;
let usuarioIDParam = null;
if (caixaPorUsuario && body.usuarioID) usuarioIDParam = parseInt(body.usuarioID);
```

O `usuarioIDParam` vai para a função SQL `funcSelect_Vendas_WebFim`. Testamos os dois estados
(desligado e ligado) chamando `venda2/historicoVendas` com o token do usuário restrito: as
**62 vendas** do período vieram iguais nos dois casos, repetido 4 vezes. Ou seja, mesmo no
Histórico de Vendas o efeito prático não apareceu nesta base. **Para efeito de manual, o
parâmetro é inócuo no caixa.**

### 4.2. O que realmente faz "cada usuário vê só o seu caixa"

É o campo **Usuário Fixo** do **Cadastro de Caixas** (Configuração → Caixa), que grava
`_sat.UsuarioID`. Em `caixa2/caixaListagem.js`:

```js
let satUsuarioID = await checkSatUsuarioID(empresaID, filialID, usuarioID);
if (satUsuarioID) {
    query += ` and v.usuarioIDAbertura = @usuarioIDAbertura`;
}
```

`checkSatUsuarioID` responde "existe algum caixa desta filial com Usuário Fixo = este
usuário?". Se **sim**, a listagem passa a mostrar **só os caixas que ele mesmo abriu**.

**A lógica é invertida em relação ao que se espera** — e é isso que explica tudo o que tínhamos
observado:

- O `contato@beefood.com.br` **tem** os dois caixas do sandbox no nome dele, então a listagem
  dele **já vinha filtrada** o tempo todo. Ninguém percebeu porque todos os 10 caixas do
  histórico foram abertos por ele.
- O `caixa.manual` **não tinha** caixa nenhum no nome dele → **nenhum filtro** → via os 10.

Quem não tem Usuário Fixo em lugar nenhum vê **todos** os caixas. A restrição só nasce quando
se dá um caixa ao usuário.

### 4.3. Prova ao vivo (19/08/2026)

| Passo | Usuário Fixo do "caixa 2" | O que `caixa.manual` via em `/caixa` |
|-------|---------------------------|--------------------------------------|
| antes | `contato@beefood.com.br` | **10 caixas** ("Mostrando 1-10 de 10") |
| durante | `caixa.manual` | **0 caixas** ("Nenhum caixa encontrado") |
| depois (restaurado) | `contato@beefood.com.br` | **10 caixas** |

Foi para zero porque o `caixa.manual` nunca abriu um caixa. Estado devolvido ao original ao
final.

### 4.4. Duas armadilhas de cache (importantes para testar e para o manual)

- **Cadastro de Caixas:** `caixaPOST` chama `resetCacheSat`, mas isso limpa o cache **só da
  instância do servidor que atendeu o POST**. Logo depois de restaurar o vínculo, uma das
  chamadas ainda devolveu a listagem filtrada; nas 5 seguintes já veio certa. O TTL do
  `cacheSat` é de **30 minutos** — então a mudança pode demorar a valer em todas as instâncias.
- **Grupo de acesso:** o `cacheGrupoAcesso` tem TTL de **1 minuto**. Ao ligar/desligar um
  switch, esperar ~1 minuto antes de concluir que "não funcionou".

### 4.5. Consequência para o manual

O parâmetro "Caixa por Usuário" **entra no manual, mas com o papel corrigido**: a tela promete
uma coisa e quem entrega é o Cadastro de Caixas. O manual precisa dizer isso com todas as
letras, senão o leitor liga o parâmetro e acha que restringiu o caixa.

---

## 5. Ambiente de teste já preparado

| Item | Valor |
|------|-------|
| Usuário restrito | **`caixa.manual`** / senha **`manual123`** |
| Grupo dele | **Acesso Funcionário** (`grupoAcessoID` 71880) |
| Função Gerente | **não** marcada (de propósito — é o que esconde Cancelamentos) |
| Usuário admin | `contato@beefood.com.br` / `1q2w3e4r` — **Principal**, Gerente, grupo **Administrador2** (`grupoAcessoID` 71879) |
| Estado dos switches | **tudo religado** ao final do estudo |
| Sujeira conhecida | um acréscimo de **R$ 0,01** com observação "teste de permissao - manual" no caixa aberto |
| IDs úteis | `empresaID` 38311, `filialID` 39202, usuário admin **88711**, usuário restrito **122583** |
| Caixas cadastrados | **caixa1** (satID 6193, ativo) e **caixa 2** (satID 39516, inativo) — os dois com Usuário Fixo `contato@beefood.com.br` |
| Parâmetro Caixa por Usuário | **ligado** (estado original, restaurado ao final) |

No grupo **Acesso Funcionário**, "Cadastro de Caixas" já vem **desligado** — é o cenário da
restrição 5 sem precisar mexer em nada.

### Técnica de teste que funcionou

Dois contextos de navegador no mesmo script Playwright: um logado como **admin** (que liga e
desliga o switch) e outro como **restrito** (que recarrega `/caixa` e observa). Entre cada
teste, religar a permissão para isolar as variáveis.

Para localizar o switch de um sub-item: buscar **"caixa"** no campo *Buscar permissão...*,
expandir o item "Abrir e Fechar Caixa" pelo chevron e mapear switch → rótulo via
`page.evaluate`, porque os switches não têm rótulo acessível próprio.

Ler as flags do resultado direto das respostas de `caixaListagem` e `caixaDetalhes`, em vez de
inferir pela tela — é mais confiável e mostra a causa, não só o efeito.

### Ajustes descobertos na sessão de 19/08 (Cloud Agent)

- **A tela de login mudou.** Não existe mais o campo "Login de acesso": agora é
  `input#emailOrWhatsapp` ("Digite seu e-mail ou WhatsApp") + `input#password`, botão
  **ENTRAR**. O login `caixa.manual` continua entrando por esse mesmo campo.
- **Configuração → Caixa fica em `/configuracao-caixa`** (com hífen), não em
  `/configuracao/caixa` — a rota errada só redireciona para a home, sem erro.
- **A tela de Parâmetros não tem botão Salvar: ela grava sozinha**, com auto-save de 500 ms
  depois do clique (`scheduleAutoSave` em `pages/Parametros.tsx`). Ou seja, clicar no switch
  para "só olhar" já altera o ambiente. Isso precisa entrar no manual.
- Para chegar ao switch de um parâmetro, os seletores por texto não funcionam bem (o `<p>` da
  descrição fica dois níveis abaixo do container). O que funciona é achar o texto e subir os
  pais até encontrar `[role="switch"]`.
- O usuário `caixa.manual` **não tem acesso ao menu Histórico**; para testar rotas que ele não
  enxerga, capture o header `Authorization` de outra requisição dele e chame a API direto.
  O token é amarrado ao usuário: usar o token do admin com outro `usuarioID` devolve
  *"Token inválido ou não autorizado para este usuário/empresa"*.

---

## 6. Onde está o código

| Camada | Caminho |
|--------|---------|
| Front (tela de grupos) | `~/refs/beefood-web-react/src/components/ModalEditarGrupoAcesso.tsx`, `src/pages/Usuarios.tsx`, `src/hooks/useGrupoAcessoDetalhes.ts` |
| Front (consumo) | `src/hooks/usePermissions.ts`, `src/utils/configCache.ts`, `src/components/ProtectedRoute.tsx` |
| Front (caixa) | `src/pages/Caixa.tsx`, `src/components/CaixaVerModal.tsx`, `src/components/CaixaFecharModal.tsx`, `src/hooks/useCaixaData.ts` |
| Parâmetro | `src/pages/Parametros.tsx` (rótulo "Caixa por Usuário") |
| Front (cadastro de caixas) | `src/pages/ConfiguracaoCaixa.desktop.tsx` (rota `/configuracao-caixa`), `src/components/caixa/ModalEditarCaixaConfig.tsx` (campo **Usuário Fixo**) |
| **Backend** | `~/refs/beetech-server-node-2.0` (branch `beefood-web-react`) — disponível desde 19/08/2026 |

### Arquivos do backend que importam para este manual

| Arquivo | Por quê |
|---------|---------|
| `src/api/controllers/caixa2/caixaListagem.js` | filtros do `136`, do `212` e do Usuário Fixo |
| `src/api/controllers/caixa2/caixaDetalhes.js` | `136` corta resumo/excluídos/cancelamentos; devolve `136` e `227` |
| `src/api/controllers/caixa2/caixaTransferir.js` | único 403 real, pelo `227` |
| `src/api/controllers/caixa2/operacaoManual.js` | checagem de sangria/acréscimo **comentada** |
| `src/models/cache/cacheSat.js` | `checkSatUsuarioID` — o mecanismo do "caixa por usuário" |
| `src/models/cache/cacheGrupoAcesso.js` | `checkAcessoItemID`, TTL de 1 min, default `true` |
| `src/models/empresa/grupoAcesso.js` | menus por itemID (Caixa = 42, Configuração → Caixa = 34) |
| `src/api/controllers/venda2/historicoVendas.js` | único consumidor de `caixaPorUsuario` |
| `src/api/controllers/empresa2/grupoAcessoGET.js` | monta a árvore de permissões da tela (tabela `_item`) |

O cache de permissões do usuário logado fica no `localStorage`, chave `config_cache`, em
**base64 + zlib**. Para inspecionar: `base64 -d` e descomprimir (em Python,
`zlib.decompress(base64.b64decode(valor))`).

---

## 7. Plano de produção (proposto em 19/08/2026 — aguardando aprovação)

Estudo fechado. O plano abaixo foi apresentado ao dono; **nada é produzido antes do "pode ir"**.

### 7.1. Estrutura do `caixa-restricoes.md`

Sete blocos, cada um no par *como configurar* + *como fica o caixa*, na ordem do mais amplo
para o mais específico:

| Bloco | Restrição | Onde se configura |
|-------|-----------|-------------------|
| Abertura | O que é um grupo de acesso, onde fica, e os dois avisos da tela (salva a cada switch; a busca esconde sub-itens) | — |
| 1 | Abrir e Fechar Caixa | Grupo → Venda |
| 2 | Visualizar Valores de Referência | sub-item de 1 |
| 3 | Visualizar Caixas Fechados | sub-item de 1 |
| 4 | Transferência de Operações | sub-item de 1 |
| 5 | Cadastro de Caixas | Grupo → Empresa |
| 6 | Função Gerente | cadastro do usuário |
| 7 | Cada usuário só vê o seu caixa | cadastro do caixa (Usuário Fixo) + a verdade sobre o parâmetro |
| Fecho | Tabela-resumo "quero que ele não consiga X → desligue Y" | — |

Decisões de conteúdo:

- O bloco 7 **desmente a descrição da tela** com cuidado: explica que ligar "Caixa por Usuário"
  não restringe o caixa, e que quem restringe é o **Usuário Fixo**. Inclui o aviso de que a
  regra é invertida (só é restrito quem **tem** um caixa no nome) e o de que a mudança pode
  levar alguns minutos para valer.
- O bloco 2 ganha destaque de **conferência cega** — é o caso de uso mais forte do manual.
- Os blocos 2, 3 e 6 avisam, cada um, que derrubam a aba **Cancelamentos**.
- O manual **não** promete permissão para sangria/acréscimo (não existe hoje).
- Avisos de segurança que entram em caixa de destaque: nunca desligar **Usuários** no próprio
  grupo; a tela de Parâmetros salva sozinha; o Principal não tem bypass.

### 7.2. Imagens (12, com folga para 14)

| # | Imagem | Tipo |
|---|--------|------|
| 01 | Configuração → Usuários → aba Grupos de Acesso | contexto |
| 02 | Modal *Editar Grupo* com os itens de caixa expandidos | setas |
| 03 | Caixa completo (referência para todos os "depois") | contexto |
| 04 | Switch "Abrir e Fechar Caixa" desligado | setas |
| 05 | Menu lateral sem o item Caixa | setas |
| 06 | Switch "Visualizar Valores de Referência" desligado | setas |
| 07 | Listagem sem as colunas de valor + Resumo vazio | setas |
| 08 | Conferência cega (fechamento sem Entrada/Saída/Saldo/Diferença) | setas |
| 09 | Listagem só com o caixa aberto (sem "Visualizar Caixas Fechados") | setas |
| 10 | Modal do caixa sem TRANSFERIR/Cancelamentos/Excluídos | setas |
| 11 | Configuração → Caixa com o campo **Usuário Fixo** | setas |
| 12 | Caixa do usuário restrito mostrando só o dele | setas |

### 7.3. Ordem de execução

1. Capturar tudo com o ambiente **intacto** (imagens 01, 02, 03, 11).
2. Para cada restrição: desligar → capturar → **religar** → conferir que voltou.
3. O bloco 7 exige abrir um caixa com o `caixa.manual` antes de vincular o Usuário Fixo, senão
   a tela dele fica vazia em vez de mostrar "só o dele" (foi o que aconteceu no teste).
4. Anotar com `annotate.py` copiado de `../caixa-conferencia-2/`.
5. Escrever `caixa-restricoes.md`, `fluxo-codigo.md` e `texto-documentation.ia.md`.
6. Fechar o item **#13** no `CHECKLIST-MANUAIS.md` e atualizar o índice da `MEMORIA-GERAL.md`.
