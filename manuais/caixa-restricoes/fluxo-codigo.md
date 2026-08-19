# fluxo-codigo.md — Restrições de caixa

Mapeamento técnico das sete restrições, no front (`beefood-web-react`) e no backend
(`beetech-server-node-2.0`, branch `beefood-web-react`). Documento interno — **não publicar**.

Levantado em 19/08/2026, com o código das duas pontas em mãos e confirmação por teste ao vivo
em produção (sandbox "BeeFood3 - Manual").

---

## 1. Como uma permissão vira comportamento

```
_grupoAcessoItem (banco)
    └─ funcSelect_GrupoAcesso_react(empresaID)
         └─ cacheGrupoAcesso.getGrupoAcesso()        TTL 1 min, por instância
              └─ checkAcessoItemID(empresaID, usuarioID, itemID) -> bool
                   ├─ rotas de caixa: filtram a query e/ou devolvem a flag
                   └─ empresa2/empresaConfigGET -> grupoAcessoUsuario (menus)
                        └─ front: config_cache no localStorage (base64 + zlib)
                             ├─ ProtectedRoute (redireciona)
                             └─ hooks/usePermissions, useCaixaData (esconde)
```

Dois detalhes que explicam quase todo comportamento estranho ao testar:

- **`checkAcessoItemID` devolve `true` por padrão.** Se o item não existe no grupo, o acesso é
  liberado. Permissão ausente é permissão concedida.
- **São dois caches em série.** O servidor guarda o grupo por 1 minuto; o navegador guarda o
  `config_cache`. Depois de mexer num switch, é preciso esperar ~1 min **e** relogar para ver o
  efeito completo.

---

## 2. Tabela de referência

| # | Restrição | itemID | Onde é lido | Efeito |
|---|-----------|--------|-------------|--------|
| 1 | Abrir e Fechar Caixa | **42** | `models/empresa/grupoAcesso.js` → `sidebar.menu.caixa` | esconde o menu; `ProtectedRoute` redireciona `/caixa` |
| 2 | Visualizar Valores de Referência | **136** | `caixa2/caixaListagem`, `caixa2/caixaDetalhes`, `caixa2/caixaFechar` | zera os valores na query e corta resumo/excluídos/cancelamentos |
| 3 | Visualizar Caixas Fechados | **212** | `caixa2/caixaListagem` | `and v.dataFechamento is null` |
| 4 | Transferência de Operações | **227** | `caixa2/caixaTransferir`, `caixa2/caixaDetalhes` | **403** na transferência; esconde TRANSFERIR, Cancelamentos e Excluídos |
| 5 | Cadastro de Caixas | **34** | `models/empresa/grupoAcesso.js` → `submenus.configuracao.items.caixa` | esconde Configuração → Caixa |
| 6 | Função Gerente | — | `_usuario.gerente` → `config_cache.gerente` | condição da aba Cancelamentos |
| 7 | Usuário Fixo | — | `_sat.UsuarioID` → `checkSatUsuarioID` | `and v.usuarioIDAbertura = @usuarioID` |

> Os itemIDs 136, 212 e 227 foram identificados por teste: desligar cada sub-item e observar
> qual flag virava `false` na resposta de `caixaListagem`/`caixaDetalhes`. A rota
> `empresa2/grupoAcesso` devolve os rótulos (da tabela `_item`) mas **não** devolve o itemID.

---

## 3. Restrição 1 — Abrir e Fechar Caixa (itemID 42)

`src/models/empresa/grupoAcesso.js`:

```js
"caixa": {
    "visible": await checkAcessoItemID(empresaID, usuarioID, 42),
    "enabled": true
},
```

O resultado vai no `grupoAcessoUsuario` devolvido por `empresa2/empresaConfigGET` e é gravado no
`config_cache`. No front, `ProtectedRoute` usa a chave para decidir a rota, e o menu lateral usa
a mesma chave para renderizar (ou não) o item.

---

## 4. Restrição 2 — Visualizar Valores de Referência (itemID 136)

O servidor **reescreve a query** — os valores não chegam ao navegador. Em
`caixa2/caixaListagem.js`:

```js
let itemID136 = await checkAcessoItemID(empresaID, usuarioID, 136);
if (!itemID136) {
    query = `select
                 convert(float, 0) as saldoDinheiroInicial
                ,convert(float, 0) as conferenciaDinheiro
                ,convert(float, 0) as saldoFinal
                ,convert(float, 0) as conferenciaSaldoFinal
                ,convert(float, 0) as quebraDeCaixa
                ...
                ,convert(varchar(1000), null) as conferidoObs
```

Em `caixa2/caixaDetalhes.js`, a flag decide se três consultas chegam a rodar:

```js
if (checkAcesso136) {
    // funcSelect_Caixa_SomaOperacoes2DetalhesWeb3 (resumo)
    // _CaixaOperacao where Ativo = 0        (excluídos)
    // beetech.log                            (cancelamentos)
}
```

No fechamento é diferente: `caixa2/caixaFechar.js` calcula tudo e **devolve** `itemID136`; quem
esconde é o front. Repare que a condição está neutralizada:

```js
let itemID136 = await checkAcessoItemID(empresaID, usuarioID, 136);
...
if (true /*itemID136*/) {
```

`components/CaixaFecharModal.tsx` usa a flag para aplicar `invisible` nas colunas Entrada,
Saída, Saldo e Diferença — é daí que vem a **conferência cega**.

---

## 5. Restrição 3 — Visualizar Caixas Fechados (itemID 212)

`caixa2/caixaListagem.js`, na query e na contagem da paginação:

```js
let acessoItemID212 = await checkAcessoItemID(empresaID, usuarioID, 212);
if (!acessoItemID212) {
    query += ` and v.dataFechamento is null`;
}
```

---

## 6. Restrição 4 — Transferência de Operações (itemID 227)

Único ponto do caixa com bloqueio real de escrita. `caixa2/caixaTransferir.js`:

```js
let checkAcesso = await checkAcessoItemID(empresaID, usuarioID, 227);
if (!checkAcesso) {
    return res.status(403).json({
        resultado: false,
        mensagem: "Usuário sem permissão para realizar transferências no caixa"
    });
}
```

No front, a mesma flag esconde mais do que o botão. `components/CaixaVerModal.tsx`:

```ts
const showTabs = data?.itemID227;
```

`showTabs` governa o botão **TRANSFERIR**, o de **Cancelamentos** e o de **Excluídos**.

---

## 7. Sangria e acréscimo — a permissão que existe mas está desligada

`caixa2/operacaoManual.js` tem a checagem escrita e **comentada**:

```js
/*let checkAcesso = await checkAcessoItemID(empresaID, usuarioID, 136);
if (!checkAcesso) {
    return res.status(403).json({
        resultado: false,
        mensagem: "Usuário sem permissão para realizar operações no caixa"
    });
}*/
```

É a origem da mensagem que aparece no front e a explicação do **200** observado no teste: o
usuário restrito lançou um acréscimo sem nenhuma barreira. A intenção original era amarrar
sangria/acréscimo ao mesmo item da restrição 2.

---

## 8. Restrição 5 — Cadastro de Caixas (itemID 34)

`src/models/empresa/grupoAcesso.js`, dentro de `submenus.configuracao.items`:

```js
"caixa": {
    "visible": await checkAcessoItemID(empresaID, usuarioID, 34),
    "enabled": await checkAcessoFormularioID(empresaID, 21)
},
```

Rota do front: `/configuracao-caixa` (com hífen), protegida por
`<ProtectedRoute submenuKey="configuracao" submenuItemKey="caixa">`.

---

## 9. Restrição 6 — Função Gerente

A flag vem de `_usuario.gerente`, é devolvida por `empresa2/empresaConfigGET` e gravada no
`config_cache`. No front, `hooks/useCaixaData.ts`:

```ts
const isGerente = getConfigValue('gerente') === true;
const showCancelamentos = data?.itemID136 && data?.itemID212 && isGerente;
```

Ou seja, a aba **Cancelamentos** depende de **três** condições. Desligar a restrição 2 ou a 3
também a derruba.

No backend, `gerente` entra em `getGrupoAcessoUsuario(empresaID, usuarioID, gerente, ...)` e
governa alguns outros itens fora do caixa (`copiarIfood`, `copiarImagem`, `migrarDados`).

---

## 10. Restrição 7 — Usuário Fixo (`_sat.UsuarioID`)

O mecanismo real do "cada usuário vê só o seu caixa". `caixa2/caixaListagem.js`:

```js
let satUsuarioID = await checkSatUsuarioID(empresaID, filialID, usuarioID);
if (satUsuarioID) {
    query += ` and v.usuarioIDAbertura = @usuarioIDAbertura`;
    parameters.push({ name: "usuarioIDAbertura", sqltype: sql.Int, value: usuarioID });
}
```

`models/cache/cacheSat.js`:

```js
const checkSatUsuarioID = async (empresaID, filialID, usuarioID) => {
    let sat = await getSat(empresaID);
    return sat.filter(f => f.empresaID == empresaID
                        && f.filialID == filialID
                        && f.usuarioID == usuarioID).length > 0;
}
```

**A lógica é invertida em relação à expectativa:** o filtro nasce da *existência* de um vínculo.
Quem não tem terminal no próprio nome não é filtrado e vê todos os caixas — inclusive o gerente,
que também é filtrado se tiver um terminal no nome dele.

O campo é gravado pela tela `pages/ConfiguracaoCaixa.desktop.tsx` (coluna **Usuário Fixo**) e
pelo modal `components/caixa/ModalEditarCaixaConfig.tsx`, que envia `usuarioFixoID` para
`POST /api/empresa2/caixa`. Esse controller chama `resetCacheSat(empresaID)` — mas o
`cacheSat` é **por instância** e tem TTL de **30 minutos**, então o efeito não é uniforme logo
após salvar.

`caixa2/abrirCaixa.js` **não** consulta o Usuário Fixo: a única trava na abertura é um caixa já
aberto para o mesmo `satID` (HTTP 409).

---

## 11. O parâmetro "Caixa por Usuário" (`caixaPorUsuario`)

Varredura completa no backend — quatro ocorrências, **nenhuma** em rota de caixa:

| Arquivo | Papel |
|---------|-------|
| `empresa2/empresaConfigGET.js` | lê para a tela de Parâmetros |
| `empresa2/empresaConfigPOST.js` | `UPDATE _EmpresaConfig` |
| `models/cache/cacheOthers.js` | carrega no cache da empresa |
| `venda2/historicoVendas.js` | único consumidor |

```js
const empresaConfig = getEmpresaConfig(empresaID);
const caixaPorUsuario = empresaConfig && empresaConfig.caixaPorUsuario === true;

let usuarioIDParam = null;
if (caixaPorUsuario && body.usuarioID) {
    usuarioIDParam = parseInt(body.usuarioID);
}
```

O `usuarioIDParam` vai para `funcSelect_Vendas_WebFim`. Testado nos dois estados com o token do
usuário restrito: **62 vendas nos dois casos**, em quatro repetições — o filtro não se
manifestou nesta base.

No front, `caixaPorUsuario` aparece só em `pages/Parametros.tsx`,
`components/mobile/parametros/MobileParametrosPage.tsx`, `hooks/useEmpresaParametros.ts` e no
tipo de `utils/configCache.ts`. Nenhum componente de caixa o consulta.

**Conclusão: a descrição em tela ("Cada usuário tem e só consegue ver seu próprio caixa") não
corresponde ao código.** Quem entrega esse comportamento é o Usuário Fixo (seção 10).

Detalhe da tela: `pages/Parametros.tsx` não tem botão Salvar. `updateField` chama
`scheduleAutoSave`, que grava 500 ms depois do clique.

---

## 12. Onde configurar (rotas e APIs)

| Tela | Rota do front | API |
|------|---------------|-----|
| Grupos de acesso | `/usuarios` (aba Grupos de Acesso) | `GET /api/empresa2/grupoAcesso/{empresaID}/{usuarioID}/{grupoAcessoID}`; `POST /api/empresa2/grupoAcessoItem` (um por switch) |
| Cadastro do usuário | `/usuarios` (aba Usuários) | `POST /api/empresa2/usuario` |
| Cadastro de caixas | `/configuracao-caixa` | `GET /api/empresa2/caixas/{empresaID}/{filialID}/{usuarioID}`; `POST /api/empresa2/caixa` |
| Parâmetros | `/parametros` | `GET`/`POST /api/empresa2/empresaConfig` |
| Listagem de caixa | `/caixa` | `GET /api/caixa2/caixaListagem/{empresaID}/{filialID}/{usuarioID}` |

A montagem da árvore de permissões da tela está em `empresa2/grupoAcessoGET.js`: os rótulos vêm
de `_item.descricao`, a hierarquia de `_item.NomeFormPai` / `_item.FormularioPai`, e só entram
itens com `beefood3 = 1`.
