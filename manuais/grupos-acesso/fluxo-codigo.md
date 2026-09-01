# fluxo-codigo.md — Grupos de acesso (estudo completo)

Mapeamento técnico do sistema de permissões do BeeFood: as **93 permissões** da tela de Grupos
de Acesso, a chave que cada uma acende no `grupoAcessoUsuario` e o que o front faz com ela.
Documento interno — **não publicar**.

Levantado em 01/09/2026 no sandbox "BeeFood3 - Manual" (empresaID 38311), com o código do front
(`beefood-web-react`) e do hub de relatórios (`beefood-reports-hub`) em mãos. O backend
(`beetech-server-node-2.0`) **não estava clonado nesta sessão**, então o efeito de cada permissão
foi levantado por **experimento em produção**, não por leitura do servidor.

---

## 1. Como uma permissão vira comportamento

```
_grupoAcessoItem (banco)
    └─ GET /api/empresa2/grupoAcesso/{empresaID}/{usuarioID}/{grupoAcessoID}
         → árvore da tela (acessos[] com recurso, descricao, nivelAcesso, subAcessos[])
    └─ cache do grupo no servidor (TTL ~1 min)
         └─ GET /api/empresa2/empresaConfig/{empresaID}/{usuarioID}/1
              → campo grupoAcessoUsuario (base64 + zlib)
                   └─ front: localStorage.config_cache
                        ├─ ProtectedRoute            → redireciona para "/"
                        ├─ AppSidebar                → esconde ou põe cadeado
                        ├─ usePermissions            → esconde botões/campos
                        └─ beefood-reports-hub       → filtra os relatórios no iframe
```

Escrita: `POST /api/empresa2/grupoAcessoItem`, **um POST por switch**, sem botão Salvar
(`ModalEditarGrupoAcesso.tsx`). O corpo leva `nivelAcesso`, `campoLogico` e um `log` com os
valores anteriores.

Dois detalhes explicam quase todo comportamento estranho ao testar:

- **Permissão ausente é permissão concedida.** `usePermissions` devolve `true` quando a chave não
  existe no JSON (`return permissions.sidebar.menu[key]?.visible ?? true`). Vale para o objeto
  inteiro: se `grupoAcessoUsuario` for `null`, tudo libera.
- **São dois caches em série.** O servidor guarda o grupo por ~1 min; o navegador guarda o
  `config_cache`. Depois de mexer num switch é preciso esperar ~85 s **e** relogar.

Medido nesta sessão: com espera de **85 s** entre o POST e a leitura, oito rodadas seguidas
devolveram resultado **estável** (duas leituras espaçadas de 12 s sempre iguais). Com menos que
isso a resposta oscila entre o valor antigo e o novo.

---

## 2. Método do levantamento (codificação binária)

Mapear 93 permissões uma a uma custaria 93 × ~100 s. Em vez disso, cada permissão recebeu um
código de 7 bits (1 a 93) e foram feitas **7 rodadas**: na rodada *b*, desligamos todas as
permissões cujo bit *b* vale 1 e ligamos as demais; depois lemos o `grupoAcessoUsuario` do
usuário de teste. A assinatura de 7 bits em que uma chave ficou `false` identifica a permissão
que a controla.

- Grupo usado: **Acesso Funcionário** (71880) — nunca o grupo do próprio operador.
- Usuário de teste: **caixa.manual** (122583), não gerente.
- Rodada extra de **baseline** com as 93 ligadas, para separar o que não depende do grupo.
- Ao final, o estado original do grupo foi restaurado a partir do dump feito antes de começar.

**Limite do método:** uma chave que dependa de *duas* permissões ao mesmo tempo produz uma
assinatura combinada, que pode coincidir com o código de uma terceira permissão. Foi o que
aconteceu com três chaves, todas do Desempenho, e cada uma foi reconferida por **teste
individual** (desligar só aquela permissão). O resultado está na seção 6.

Total observado: **352 chaves** no `grupoAcessoUsuario` do sandbox.

---

## 3. Estrutura do `grupoAcessoUsuario`

```ts
interface GrupoAcessoUsuario {
  version: string;
  updatedAt: string;
  sidebar: {
    menu: Record<string, { visible, enabled }>;
    submenus: Record<string, { visible, enabled, items, acoes? }>;
    footer: Record<string, { visible, enabled }>;
  };
  aplicativos: Record<string, { visible, items }>;
}
```

`src/utils/configCache.ts`. Onze submenus no sandbox: `fiscal`, `whatsapp`, `foodMarketing`,
`cardapio`, `cardapioDigital`, `cadastros`, `configuracao`, `estoque`, `desempenho`, `crm`,
`financeiro`.

### `visible` versus `enabled`

| Campo | Efeito no front |
|-------|-----------------|
| `visible: false` | `return null` — o item **não é renderizado** (`AppSidebar.tsx:428-431`, `:514`, `:558-562`) |
| `visible: true, enabled: false` | renderiza com `opacity-40`, ícone `Lock` e tooltip **"Acesso restrito"** |
| qualquer um `false` numa rota protegida | `<Navigate to="/" state={{ reason: 'access_denied' }} replace />` — redireciona sem mensagem |

O grupo de acesso mexe quase sempre no **`visible`**. Das 130 chaves `.enabled` do sandbox,
apenas 12 responderam a algum switch — e todas por tabela (seção 5). O `enabled` é o canal do
**plano/contratação**: `fluxoCaixa.enabled` é `false` mesmo com tudo ligado, porque a tela é
"Em breve!".

### `acoes` — o único bloco que não é menu

Só `sidebar.submenus.cardapio` tem `acoes`, e é um booleano direto (sem `visible`/`enabled`):

```json
"acoes": { "adicionarNovo": true, "editar": true, "editarPreco": true,
           "editarAtivo": true, "editarLote": true, "excluir": true }
```

Lido por `canSubmenuAcao` → `canCardapioAcao` (`src/hooks/usePermissions.ts:324-332`).

---

## 4. As 93 permissões da tela

Os `grupoAcessoItem` são **por grupo** (são o id da linha de vínculo, não um itemID global):
os números abaixo valem para o grupo 71880 do sandbox e servem só como referência do
experimento. A tela agrupa por `acesso.recurso`, que o backend devolve.

| Recurso | Itens pai | Sub-itens |
|---------|----------:|----------:|
| Empresa | 8 | 0 |
| Gestão | 6 | 22 |
| Venda | 6 | 3 |
| Fiscal | 5 | 0 |
| Cliente | 3 | 0 |
| Cadastros Básicos | 3 | 0 |
| Configurações | 3 | 1 |
| Cadastros | 2 | 6 |
| Relatórios | 1 | 20 |
| Marketing | 1 | 3 |
| **Total** | **38** | **55** |

O catálogo com o efeito de cada uma está no manual (`grupos-acesso.md`, seção "Catálogo").
Aqui ficam apenas os casos que exigem explicação técnica.

---

## 5. Permissões que controlam mais de uma tela

Resultado do experimento — cada linha foi observada na resposta da API, não deduzida.

| Permissão | Chaves que ela apaga |
|-----------|----------------------|
| **Cadastro de Cardápio** | `cardapio.visible` + `items.produtos`, `items.grupoOpcoes`, `items.complementos`, `items.reordenar` |
| **Cardápio - Exibir / Ocultar Produtos** | `cardapio.items.exibirOcultar` **e** `cardapio.items.rodizio` (que é Rodízio **e** Preço Programado) |
| **Dados da Empresa** | `configuracao.items.empresa` **e** `configuracao.items.parametros` |
| **Cadastro de Impressoras** | `configuracao.items.impressao` + `aplicativos.cozinha.items.impressaoCupom.enabled` |
| **Cardápio Digital** | `cardapioDigital.visible` + 7 `enabled` de Aplicativos (Cardápio Digital, Cashback, Cupom Desconto, Facebook Pixel, Google Analytics, Google Tag, Cardápio QR Code) |
| **Inteligência Artificial (ChatGPT)** | `whatsapp.items.ia.visible` + `aplicativos.marketing.items.ia.enabled` |
| **Cardápio Digital Tablet** | `menu.cardapioDigitalTablet` + `aplicativos.presencial.items.cardapioTablet.visible` |
| **WhatsApp** | `whatsapp.visible` + `whatsapp.items.conexao` + `aplicativos.marketing.items.whatsapp.enabled` |
| **Campanhas** (sub de WhatsApp) | `whatsapp.items.enviosMassa` + `foodMarketing.items.campanhaWhatsApp` + `foodMarketing.items.campanhaInteligente` |
| **PIX** | `menu.pix` + `aplicativos.pagamentoOnline.items.pix.visible` |
| **KDS** | `menu.kds` + `aplicativos.cozinha.items.kds.enabled` |
| **Estoque** | `estoque.visible` + `estoque.items.meuEstoque` |
| **Multilojas** (sub de Cardápio Digital) | `cardapioDigital.items.multilojas.enabled` + `aplicativos.delivery.items.multilojas.enabled` |

> Repare no padrão: quando a permissão apaga um `enabled` de Aplicativos, o app não desaparece
> da tela — ele fica com **cadeado**. É o único lugar em que o grupo de acesso produz cadeado
> em vez de sumiço.

---

## 6. Os grupos do Desempenho são derivados

`sidebar.submenus.desempenho.items.vendas`, `.produtos` e `.clientes` são **cabeçalhos**, não
permissões. Não existe switch para eles na tela, e o experimento binário atribuiu cada um a uma
permissão que não fazia sentido (`vendas` → "Configuração Fiscal - Regra Fiscal";
`produtos` → "Vendas - Cancelamentos"; `clientes` → "Clientes - Base de clientes").

Teste individual desligando **apenas** "Configuração Fiscal - Regra Fiscal": a única chave que
caiu foi `sidebar.submenus.fiscal.items.configuracao.visible`. Ou seja, o cabeçalho do grupo é
`false` só quando **todos** os relatórios daquele grupo estão desligados — foi a coincidência de
as cinco permissões de Vendas estarem desligadas nas mesmas rodadas que produziu a assinatura
enganosa.

O hub de relatórios já trata os dois níveis (`beefood-reports-hub/src/lib/accessControl.ts`):

```ts
const leaf = readPath(desempenho.items, path);
if (!leaf) return false;
if (leaf.visible === false) return false;
if (path.length > 1) {
  const parent = readPath(desempenho.items, [path[0]]);
  if (parent?.visible === false) return false;
}
```

Três relatórios existem no cache mas **não têm switch** na tela de grupos:
`delivery.items.entregador` (Entregador — Taxa / KM), `delivery.items.acessoCardapioDigital` e
`presencial.items.acessoCardapioDigital`. Os dois de "Acesso Cardápio Digital" estão escondidos
em produção pelo próprio hub (`isProduction`); o de Entregador aparece para qualquer um que
alcance o Desempenho.

`delivery.items.mapaCalor` governa **dois** itens do menu de relatórios: *Mapa de Calor* e
*Top Bairros*.

---

## 7. O que a tela de produto faz com as seis ações

`src/components/ModalEditarProduto.tsx:118-125`:

```ts
const { canCardapioAcao, isSubmenuItemEnabled } = usePermissions();
const podeDesligarEstoqueNegativo = isSubmenuItemEnabled('estoque', 'estoqueNegativo');
const podeEditar = canCardapioAcao('editar');
const podeEditarPreco = canCardapioAcao('editarPreco');
const podeEditarAtivo = canCardapioAcao('editarAtivo');
const podeExcluir = canCardapioAcao('excluir');
const algoEditavel = podeEditar || podeEditarPreco || podeEditarAtivo;
```

| Ação | Campos/controles atingidos no modal |
|------|--------------------------------------|
| `editar` | Nome (408, 453), Setor (471), Subsetor (922), Código (626), Código de Barras (635), Unidade (674), Descrição + botão de IA (778-799), Observações internas (993), Sem taxa de serviço (897), Somente agendamento (972), Enviar para balança (1009), Setor de produção (1058), Nome de produção (1128-1140), **aba Restrições inteira** (`<fieldset disabled>` em 1425) |
| `editarPreco` | Preço de Venda (604), Custo (712), preços de Delivery e Presencial por filial (848, 877, 1348, 1367, 1390) |
| `editarAtivo` | switches Ativo / Delivery / Presencial / Totem (817-877, 1325-1408) e os `handleToggle*` (216, 221) |
| `excluir` | item **Excluir Produto** no menu OPÇÕES (1637) |
| as três de edição | botão **SALVAR E SAIR (F2)** fica desabilitado quando `!algoEditavel` (1661) |
| `adicionarNovo` | botão **+ NOVO PRODUTO** no cabeçalho (`Cardapio.tsx:474`) e criar setor (`CardapioProdutosTab.tsx:762`) |
| `editarLote` | botão de edição em lote (`CardapioProdutosTab.tsx:851`) e busca avançada (`ModalBuscaAvancada.tsx:61`) |

Fora do modal, as mesmas ações valem no card da lista (`VirtualizedProductGrid.tsx:702-703`:
switch Ativo, itens *Em falta*, *Desativar Delivery*, *Desativar Presencial*, *Excluir*) e nos
modais de opção, complemento, grupo de opções e edição em lote — 22 arquivos chamam
`canCardapioAcao`.

**Não existe** permissão separada para *ver* custo: `Custo`, `Custo Ficha Técnica` e `Custo
Total` aparecem para qualquer um que abra o produto. `editarPreco` só decide se o campo é
editável (`readOnly`). Quem não pode ver custo não pode entrar no cadastro do produto.

**`estoqueNegativo`** é a única permissão de fora do Cardápio que atua dentro do modal do
produto (switch *Aceita Estoque Negativo*, linha 1202) — e ela **não responde a nenhum switch**
da tela de grupos: `estoque.items.estoqueNegativo.enabled` ficou `true` nas oito rodadas.

---

## 8. O que não passa pelo grupo de acesso

### 8.1 Depende da Função Gerente (`_usuario.gerente`)

Estas três ficaram `false` na rodada de baseline (93 permissões **ligadas**), porque o usuário
de teste não é gerente:

| Chave | Item |
|-------|------|
| `cardapio.items.copiarIfood` | Cardápio → Copiar do iFood |
| `cardapio.items.copiarImagem` | Cardápio → Copiar de Imagem |
| `configuracao.items.migrarDados` | Configuração → Migrar Dados |

A flag `gerente` também governa, no front: layout da Home (`HomeGerente` × `HomeNaoGerente`),
cards de resumo do NFe/NFCe, linha **Taxa de Serviço** no resumo do caixa, a aba
**Cancelamentos** do caixa (junto de `itemID136` e `itemID212`) e o bypass do
`ModalValidarSenhaGerente`.

### 8.2 Depende de Parâmetros (senha de gerente)

`geCai`, `gePag`, `geVen`, `gePro`, `geEst`, `geDesc` + `geDescMax`, `motivoCancelamento`,
`operadorPDV`, `operadorPDVObrigar` — todos em Configuração → Parâmetros, não no grupo.
Definem **quais ações pedem senha de gerente**, não quem vê o quê.

### 8.3 Depende do cadastro do caixa

`_sat.UsuarioID` (**Usuário Fixo**) — cada um vê só o próprio caixa. Documentado no manual #13.

### 8.4 Nunca é controlável pelo grupo

75 chaves `.visible` não responderam a nenhum switch nas oito rodadas:

- **Todos os 44 aplicativos de integração** e as 6 categorias da tela Aplicativos (iFood, Keeta,
  99Food, Rappi, UaiRango, Aiqfome, Delivery Much, Google Business, Uber Direct, Machine, Lets
  Express, Foody, Pick n Go, Agilizone, Husky, Open Delivery, Mapas Google, BeeFood Entregador,
  Gestão de Entregas, App Garçom, Totem, Balança, Pesagem Automática, Mercado Pago, TEF PayGo,
  AutoTEF Stone, Repediu, Domínio Próprio, Super Avaliações…). Só a permissão **Aplicativos**
  (que esconde o menu inteiro) e os `enabled` da seção 5 têm efeito.
- **`sidebar.menu.inicio`** — Início não sai do menu. E a rota `/` não tem `ProtectedRoute`.
- **Footer**: Meus Links, Manual, Suporte.
- **Cabeçalhos dos submenus Cadastros, Configuração e Fiscal** — o cabeçalho fica; o que
  desaparece são os itens dentro dele.
- **As 11 abas do Cardápio Digital** (Configurações, Agendamento, Marketing, Pagamento Online,
  Formas Recebimento, Horário Atendimento, Pausa Programada, Área de Entrega, Cupom de Desconto,
  Cashback, Link Multilojas): só a permissão-pai **Cardápio Digital** age, escondendo o submenu
  inteiro. A aba **Avisos** nem existe como chave — `canViewSubmenuItem` devolve `true` por
  ausência.
- **`estoque.items.estoqueNegativo`**.

### 8.5 Rotas sem `ProtectedRoute`

`/` (Home), `/notas-recebidas`, `/sugestoes`, `/estrategias`, `/manual`, `/ajuda-videos`,
`/certificado-a1`, `/admin` (guard próprio), `/bridge` (guard próprio). Em `/notas-recebidas` o
menu respeita a permissão **NFe - Recebidas**, mas a URL digitada à mão abre.

---

## 9. Restrições que não têm chave no JSON

As três sub-permissões de **Abrir e Fechar Caixa** (Visualizar Valores de Referência,
Visualizar Caixas Fechados, Transferência de Operações) não produziram **nenhuma** chave no
`grupoAcessoUsuario` em nenhuma das oito rodadas. Elas agem no servidor, dentro das rotas de
caixa (`itemID136`, `itemID212`, `itemID227`), e chegam ao front como flags da própria resposta
de `caixaListagem`/`caixaDetalhes`. É o mecanismo documentado no manual #13
(`manuais/caixa-restricoes/fluxo-codigo.md`).

Consequência prática para o estudo: o grupo de acesso tem **dois canais** de efeito — o
`grupoAcessoUsuario` (menus, telas, ações do cardápio) e a **filtragem direta na API** (caixa).
Só o primeiro é visível no `config_cache`.

---

## 10. Onde configurar (rotas e APIs)

| Tela | Rota do front | API |
|------|---------------|-----|
| Grupos de acesso | `/usuarios` (aba Grupos de Acesso) | `GET /api/empresa2/gruposAcesso/{empresaID}/{usuarioID}`; `GET /api/empresa2/grupoAcesso/{empresaID}/{usuarioID}/{grupoAcessoID}`; `POST /api/empresa2/grupoAcesso`; `POST /api/empresa2/grupoAcessoItem` |
| Cadastro do usuário (grupo + Gerente) | `/usuarios` (aba Usuários) | `GET /api/empresa2/usuarios/{empresaID}/{usuarioID}`; `POST /api/empresa2/usuario` |
| Permissões efetivas do usuário | — | `GET /api/empresa2/empresaConfig/{empresaID}/{usuarioID}/1` (o `usuarioID` tem de ser o do próprio token: com token de outro usuário a rota devolve **401**) |
| Parâmetros (senha de gerente) | `/parametros` | `GET`/`POST /api/empresa2/empresaConfig` |

`campoLogico` existe no payload e no retorno da API, mas **não tem switch na interface** — o
modal só repassa o valor que veio. No sandbox, 6 dos 93 itens têm `campoLogico: false`
(Funcionários, Usuários, Clientes, Cadastro de Cardápio, Estoque, Financeiro) sem diferença
observável de comportamento.

---

## 11. Arquivos de referência

| Papel | Caminho (em `beefood-web-react`) |
|-------|----------------------------------|
| Tipos e leitura do cache | `src/utils/configCache.ts` |
| Hook de permissões | `src/hooks/usePermissions.ts` |
| Guard de rota | `src/components/ProtectedRoute.tsx` |
| Menu lateral | `src/components/AppSidebar.tsx` |
| Tela de grupos | `src/pages/Usuarios.tsx`, `src/components/ModalEditarGrupoAcesso.tsx` |
| APIs de grupo | `src/hooks/useGruposAcesso.ts`, `src/hooks/useGrupoAcessoDetalhes.ts` |
| Modal de produto | `src/components/ModalEditarProduto.tsx` |
| Lista de produtos | `src/components/cardapio/CardapioProdutosTab.tsx`, `src/components/cardapio/VirtualizedProductGrid.tsx` |
| Senha de gerente | `src/components/ModalValidarSenhaGerente.tsx`, `src/hooks/useDescontoGuard.ts` |
| Relatórios (iframe) | `beefood-reports-hub/src/lib/accessControl.ts`, `src/pages/Reports.tsx` |
