# Reforma Tributária (IBS/CBS) — Mapeamento técnico

> Fontes:
> - Front: `C:\projetos\beefood-web-react\src` (tela Edição Fiscal e modal de produto da nota).
> - Docs/Backend: `C:\projetos\beetech-server-node-3.0\docs\reforma-tributaria` (schema + APIs).
> - Emissão (Delphi): `C:\projetos\beetecherp\NFE\cNFe.pas` (`preencheIBSCBS`).
> Base para escrever o manual do usuário final. Labels = textos exatos da UI.

---

## 1. Contexto

Reforma tributária **NT 2025.002 / LC 214/2025** cria os tributos **IBS** (Imposto sobre Bens e
Serviços) e **CBS** (Contribuição sobre Bens e Serviços). Fase de transição **2026**: o sistema
apenas **configura e exibe** os campos por produto; o **cálculo e o XML** são feitos no servidor de
emissão (Delphi/ACBr). Atende **Simples Nacional** e **Regime Normal** (regra por produto).

---

## 2. Os 6 campos (por produto)

| Campo (coluna física) | Rótulo na tela | Tipo | Exemplo | Observação |
|---|---|---|---|---|
| `IBSCBS_CST` | **CST IBS/CBS** | select | `000` | CST (3 díg.). Catálogo `_IBSCBSCST` |
| `IBSCBS_cClassTrib` | **cClassTrib** | select | `000001` | Class. Tributária (6 díg.). **Filtra pelo CST**. Catálogo `_IBSCBSClassTrib` |
| `IBSCBS_pRedAliq` | **% Red. Alíquota** | número | `0` | % de redução (grupo gRed) |
| `IBSUF_pIBSUF` | **Alíq. IBS UF (%)** | número | `0,1` | Alíquota IBS estadual |
| `IBSMun_pIBSMun` | **Alíq. IBS Mun. (%)** | número | `0` | Alíquota IBS municipal |
| `CBS_pCBS` | **Alíq. CBS (%)** | número | `0,9` | Alíquota CBS |

Produtos com `IBSCBS_CST` **nulo NÃO emitem** o grupo IBS/CBS (o Delphi ignora — evita assumir
tributação errada).

### Catálogo de CST (principais — `_IBSCBSCST`)
`000` Tributação integral · `010/011` Alíquotas uniformes · `200` Alíquota reduzida ·
`220/221` Alíquota fixa · `222` Redução de BC · `400` Isenção · `410` Imunidade/não incidência ·
`510/515` Diferimento · `550` Suspensão · `620` Monofásica · `800` Transferência de crédito ·
`810/811` Ajuste ZFM/Ajustes · `820` Regimes específicos · `830` Exclusão da BC.

### cClassTrib (exemplos — `_IBSCBSClassTrib`, ligado ao CST)
`000001` Tributação integral (CST 000) · `000004` Integral c/ crédito presumido ·
`400001` Isenção (CST 400) · `410001` Imunidade (CST 410).

---

## 3. Onde editar no front

### A) Tela Edição Fiscal (edição em massa) — FOCO DO MANUAL
| Item | Valor |
|---|---|
| Menu | **Fiscal → Edição Fiscal** (sidebar) |
| Rota | `/edicao-fiscal` (`src/pages/EdicaoFiscal.tsx`) — **só desktop** (`MobileBlockedRoute`) |
| Grupo de colunas | **"IBS/CBS (Reforma)"** (`COLUMN_GROUPS` id `IBSCBS`) — ativar no seletor de grupos (`ModalGruposColunasEdicaoFiscal`) |
| Colunas | CST IBS/CBS, cClassTrib, % Red. Alíquota, Alíq. IBS UF (%), Alíq. IBS Mun. (%), Alíq. CBS (%) |
| Edição em lote | `ModalEditarImpostosBatch.tsx` (seção IBS/CBS) |
| Hook produtos | `src/hooks/useEdicaoFiscalProdutos.ts` (`ProdutoFiscal`) |
| Catálogos | `useFiscalCache` (`dados.ibscbsCST`, `dados.ibscbsClassTrib`) |

APIs (já prontas no backend — não foram criadas no manual):
- Produtos: `GET /api/fiscal2/edicaoFiscal/produtos/:empresaID/:usuarioID/1`
- Catálogos: `GET /api/fiscal2/edicaoFiscal/dados/:empresaID/:usuarioID`
- Salvar célula: `POST /api/fiscal2/edicaoFiscal/produto`
  body `{ produtoID, produtoImpostosID, usuarioID, empresaID, ckFiscal: true, fiscalColuna, fiscalValor }`

### B) Modal de produto dentro da nota (fora do escopo deste manual)
`src/components/fiscal/ModalEditarProdutoNF.tsx` → aba **"IBS/CBS (Reforma)"**, nas telas `/nfe` e
`/nfce` (detalhe). Edita `_NFeConfigProduto` via `GET/POST /api/fiscal2/notasFiscais/detalhes/produto`.

---

## 4. Como chega na NOTA (fluxo real)

```
_produtoImpostos (config por produto)
   -> proc de processamento copia as 6 colunas -> _NFeConfigProduto (snapshot por NOTA)
   -> funcSelect_NFe_Produtos / funcSelect_NFCe_Produtos (leem _NFeConfigProduto)
   -> Delphi cNFe.preencheIBSCBS: calcula valores e monta o grupo <IBSCBS> no XML (ACBr)
```

### Cálculo em `cNFe.pas` (`preencheIBSCBS`)
- Base: `vBC = vProd` (valor do produto do item).
- Alíquota efetiva (se `% Red.>0`): `pEfet = p × (1 - pRed/100)`.
- `vIBSUF = vBC × pIBSUFEfet%` · `vIBSMun = vBC × pIBSMunEfet%` · `vCBS = vBC × pCBSEfet%`.
- `vIBS = vIBSUF + vIBSMun`.
- Monta `Imposto.IBSCBS`: `CST`, `cClassTrib`, `gIBSCBS{ vBC, vIBS, gIBSUF{pIBSUF,vIBSUF[,gRed]},
  gIBSMun{pIBSMun,vIBSMun[,gRed]}, gCBS{pCBS,vCBS[,gRed]} }`.
- Totais da nota: `IBSCBSTot{ vBCIBSCBS, gIBS{ gIBSUFTot.vIBSUF, gIBSMunTot.vIBSMun, vIBS },
  gCBS.vCBS }`.

> A camada de regra fiscal (ICMS/PIS/COFINS) NÃO toca IBS/CBS — não há cálculo lá.

---

## 5. Observações para o manual

1. A tela Edição Fiscal é **somente desktop**.
2. Editar a config **grava de verdade** no produto, mas **não emite nota** — é reversível.
3. CST e cClassTrib são **selects**; cClassTrib **filtra** pelo CST escolhido.
4. Alíquotas aceitam vírgula/ponto.
5. O exemplo de "como sai na nota" no manual é **fictício/ilustrativo** — NÃO geramos XML nem
   emitimos NFC-e/NF-e.
6. Valores típicos da fase de teste 2026 (ilustrativos): IBS ~`0,1%`, CBS ~`0,9%`.
