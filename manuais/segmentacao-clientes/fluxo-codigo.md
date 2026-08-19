# fluxo-codigo.md — Segmentação de Clientes

Mapeamento técnico da funcionalidade, no front (`beefood-web-react`) e no backend
(`beetech-server-node-2.0`, branch `beefood-web-react`). Documento interno — **não publicar**.

Levantado em 19/08/2026, com o código das duas pontas e conferência na API de produção.

---

## 1. Visão geral

```
Food Marketing -> Segmentação de Cliente        (itemID 292, formularioID 165)
   /food-marketing/segmentacao-cliente
        |
        +-- GET  /cliente2/segmentacao/campos/{empresaID}/{usuarioID}   catálogo (37 campos)
        +-- GET  /cliente2/segmentacao/publicos/{empresaID}/{usuarioID} lista
        +-- GET  /cliente2/segmentacao/modelos/{empresaID}/{usuarioID}  9 modelos
        +-- POST /cliente2/segmentacao/publico                          criar
        +-- PUT  /cliente2/segmentacao/publico                          editar
        +-- POST /cliente2/segmentacao/publico/duplicar
        +-- POST /cliente2/segmentacao/publico/ativo
        +-- DELETE /cliente2/segmentacao/publico/{empresaID}/{usuarioID}/{id}
        +-- POST /cliente2/segmentacao/modelo/aplicar                   modelo -> público
        +-- POST /cliente2/segmentacao/processar                        calcula o público
```

Rotas em `src/api/routes/clienteRouter2.js` (linhas 80-90), todas com `authMiddleware`.

**O motor roda em JavaScript, não em SQL.** O banco só faz `SELECT` das fontes; a árvore de
regras é avaliada em memória por `src/models/segmentacao/engine/avaliador.js`.

---

## 2. Modelo de dados

Tabela `dbo.segmentacao`, no banco de cache (`docs/segmentacao/schema.sql` e `schema_v2.sql`):

| Coluna | Papel |
|--------|-------|
| `id`, `empresaID` | identificação |
| `nome`, `descricao` | metadados |
| **`regraJson`** | **a árvore de filtros — é isto que define o público** |
| `ativo` | entra ou não nas campanhas |
| `excluido` | soft delete |
| `sistema` | `1` = público fixo BeeFood (só leitura) |
| `chaveModelo` | `fixo-novos`, `fixo-sumidos`, `fixo-cashback`, `fixo-aniversario` |
| `criadoPorID`, `criadoPor`, `criadoEm`, `atualizadoEm` | auditoria |

**Não existe tabela de "clientes do público".** O resultado só é materializado quando vira
participante de campanha (`wppofCampanhaParticipante`, `smsCampanhaParticipante`, no MySQL).

Formato da regra:

```json
{ "operadorLogico": "and", "negar": false,
  "condicoes": [ { "campo": "qtdPedidos", "operador": "maiorOuIgual", "valor": 2 } ] }
```

Um nó com `condicoes` é grupo; sem, é condição. O motor aceita aninhamento sem limite e `negar`,
mas **o construtor visual só produz uma lista plana com E/OU** — sem subgrupos e sem NÃO.

---

## 3. O filtro primário

Aplicado sempre, antes de qualquer regra (`src/models/segmentacao/dataSources.js`):

```sql
select clienteID, dataAbertura as dataNascimento, tipoCliente
from _cliente (nolock)
where empresaID = @empresaID
  and isnull(ativo, 0) = 1
  and isnull(aceitaWhatsapp, 0) = 1
  and len(isnull(telefonePrincipal, '')) >= 10
```

O `totalBase` e o `percentual` mostrados na tela são sobre **essa** base. Condições nos campos
`aceitaWhatsApp`, `clienteAtivo` e `telefoneValido` são ignoradas pelo avaliador
(`CAMPOS_PRIMARIOS_IGNORADOS` em `processarSegmentacao.js`).

---

## 4. Catálogo de campos (37 em 9 grupos)

Definido em `src/models/segmentacao/engine/campos.js`, servido por `camposGET.js`.

| Grupo | Chaves |
|-------|--------|
| Cliente | `filialID`, `origem`, `tipoCliente` |
| Indicadores | `qtdPedidos`, `totalVenda`, `ticketMedio`, `notaMedia`, `notaUltima`, `diasUltimaVenda`, `diasPrimeiraVenda`, `dataPrimeiraVenda`, `dataUltimaVenda` |
| RFV | `classificacao`, `recencia`, `frequencia`, `valorMonetario` |
| Aniversário | `mesAniversario`, `diasAteAniversario`, `dataNascimento` |
| Cashback | `saldoCashback`, `temCashback` |
| Cupom | `usouCupom`, `qtdCuponsUsados`, `cupons` |
| Endereço | `bairro`, `cidade`, `sigla`, `cep`, `km` |
| Vendas | `venda_setores`, `venda_produtos`, `categoriaFavorita`, `produtoFavorito`, `venda_diasSemana`, `periodosCompra`, `cadenciaMediaDias` |
| Canais | `canaisComprados` |

### Fontes e carregamento preguiçoso

`coletarFontes` inspeciona a regra e carrega só o necessário:

| Fonte | Tabela | Cache |
|-------|--------|-------|
| `cliente` (sempre) | `_cliente` + `_clienteProcessado` + RFV | 60 min / RFV 1× por dia |
| `endereco` | `_clienteEndereco` + `_Cidade` + `_Estado` | 60 min |
| `venda` | `_pvspProcessado` | até 06:00 do dia seguinte |
| `cashback` | cache em memória de cashback | 5 min |
| `cupom` | `_deliveryCupomUso` | 60 min |

Por isso o modal de teste mostra "Fontes: cliente" ou "Fontes: cliente, cashback": é a lista de
fontes que a regra obrigou a carregar.

---

## 5. Semântica que o manual precisa acertar

| Campo | O que realmente é |
|-------|-------------------|
| `diasUltimaVenda`, `diasPrimeiraVenda` | calculados no processamento: `floor((agora - data) / 86400000)`, com o relógio do servidor Node (não o fuso da empresa) |
| `temCashback` | derivado de `saldoCashback > 0` — qualquer centavo conta |
| `usouCupom` / `qtdCuponsUsados` | histórico vitalício, sem recorte de período |
| `mesAniversario`, `diasAteAniversario` | de `_cliente.dataAbertura`, em UTC; `0` = aniversário hoje |
| `categoriaFavorita`, `produtoFavorito` | maior soma de `qtd`; empate resolve pelo primeiro do Map |
| `cadenciaMediaDias` | média dos intervalos entre datas distintas de pedido; `null` com menos de 2 pedidos |
| `canaisComprados`, `periodosCompra`, `venda_*` | união de tudo o que o cliente já fez |
| `km` | guardado como **array** de distâncias, mas declarado `numero`; os operadores numéricos não tratam array — **comportamento indefinido com vários endereços** |

Operadores (`engine/operadores.js`):

- texto compara **sem acento e sem caixa**;
- `em` em campo de lista é **interseção** ("algum item do cliente está na lista do filtro");
- `entre` e `entreDatas` são **inclusivos**;
- campo nulo faz a comparação numérica **falhar** (cliente fica de fora);
- **operador desconhecido faz a condição ser ignorada** (`avaliador.js` retorna `true`) — falha
  silenciosa.

### Duas lacunas — não afirmar no manual

1. `qtdPedidos`, `totalVenda`, `ticketMedio`, `notaMedia` e as datas vêm prontos de
   `_clienteProcessado`, preenchido por um ETL **fora deste repositório**. Não dá para dizer se
   vendas canceladas entram nem como o ticket é ponderado.
2. Os limiares do RFV (scores 1-5 e as 12 classificações) estão em
   `funcSelect_Cliente_RFV` / `procInsert_RFV`, procedures **não versionadas aqui**.

---

## 6. Rótulos: a API e a tela divergem

O front reescreve os rótulos em `src/components/segmentacao/labels.ts`. **Vale o da tela.**

| API | Tela |
|-----|------|
| está em / não está em | **é um de** / **não é nenhum de** |
| maior que / menor que | **é maior que** / **é menor que** |
| entre | **está entre** |
| antes de / depois de | **é antes de** / **é depois de** |
| não está vazio | **está preenchido** |
| verdadeiro / falso | **sim** / **não** |

Campos: `filialID` → **Cardápio**, `recencia` → **Recência (R) — 1 a 5**, `tipoCliente` →
**Tipo de pessoa (PF/PJ)**.

---

## 7. Processamento

`POST /cliente2/segmentacao/processar`, corpo:

```json
{ "empresaID": 38311, "usuarioID": 88711,
  "id": 7, "regra": { ... }, "periodoVenda": {}, "somenteContagem": true }
```

- `regra` inline tem prioridade sobre `id` (é o que o botão **TESTAR PÚBLICO** usa).
- `usuarioID` **é obrigatório no corpo** — o middleware recusa sem ele ("Parâmetros empresaID e
  usuarioID são obrigatórios"), embora o controller só use `empresaID`.
- `somenteContagem: true` devolve só `total`, `totalBase`, `percentual` e `fontesUsadas`.
- **Sob demanda**, sem job agendado, sem timeout explícito e sem limite de tamanho.

---

## 8. Modelos e públicos fixos

`src/models/segmentacao/modelosTop.js` — 9 modelos, viram cópia editável por
`POST /modelo/aplicar` (`sistema = 0`).

`src/models/segmentacao/publicosFixos.js` — 4 públicos com `sistema = 1`, criados automaticamente
na primeira listagem e mantidos em dia pelos scripts `docs/segmentacao/update_regras_fixos_v1.sql`
e `v2.sql`. As janelas de `fixo-novos` (6-30 dias) e `fixo-sumidos` (31-90 dias) não se sobrepõem
de propósito.

> **No sandbox os 4 fixos aparecem duplicados** (8 linhas). É característica do ambiente de
> teste, não do produto.

---

## 9. Front — arquivos principais

| Papel | Arquivo |
|-------|---------|
| Lista | `src/pages/FoodMarketingSegmentacaoLista.desktop.tsx` |
| Editor | `src/components/segmentacao/SegmentacaoEditorModal.tsx` |
| Construtor de regras | `ConstrutorRegra.tsx`, `CondicaoLinha.tsx` |
| Entrada de valor | `ValorInput.tsx` — máscara BRL nos campos monetários |
| Seletor de campo | `SeletorCampoModal.tsx` |
| Rótulos | `labels.ts` |
| Teste | `TestarSegmentacaoModal.tsx`, `VerClientesSheet.tsx` |
| Exportação | `excelExportSegmentacao.ts` |
| Hooks | `useSegmentacoes.ts`, `useCamposCatalogoSegmentacao.ts`, `useModelosSegmentacao.ts` |

> `src/lib/api/segmentacao.mocks.ts` existe e **diverge da API real** em rótulos e modelos. Não
> usar como fonte: conferir sempre na API de produção.

> A máscara dos campos em R$ preenche da direita: digitar `50` resulta em **R$ 0,50**. Essa
> pegadinha está avisada no manual.

---

## 10. Permissões

```js
"segmentacaoCliente": {
    "visible": await checkAcessoItemID(empresaID, usuarioID, 292),
    "enabled": await checkAcessoFormularioID(empresaID, 165)
},
```

`src/models/empresa/grupoAcesso.js`. Os endpoints **não revalidam** o itemID 292 — a restrição é
de interface.
