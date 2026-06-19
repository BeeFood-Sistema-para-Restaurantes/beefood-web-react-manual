# MEMÓRIA — Manual Reforma Tributária (IBS/CBS)

> Memória detalhada deste manual (escopo, fluxo, decisões e estado), para retomar a qualquer momento.
> Ver também a memória geral: `..\..\MEMORIA-GERAL.md`.

Status: ✅ **Concluído** — Última atualização: 2026-06-19

---

## 1. Escopo do manual

Ensinar o responsável fiscal a:
1. Entender os **6 campos** novos da Reforma Tributária (IBS/CBS) por produto.
2. **Preencher/editar** esses campos no menu **Fiscal → Edição Fiscal** (edição em lote).
3. Entender **como esses campos aparecem na nota** — via **exemplo fictício** (sem emitir XML/NFC-e).

Arquivo final: `reforma-tributaria.md`. Mapa técnico: `fluxo-codigo.md`.
Texto pronto p/ construir no app: `texto-documentation.ia.md`.

---

## 2. Conteúdo da pasta

```
manuais\reforma-tributaria-ibscbs\
├─ MEMORIA.md                 (este arquivo)
├─ reforma-tributaria.md      (manual final)
├─ fluxo-codigo.md            (mapeamento do código: campos, rotas, API, cálculo no emissor)
├─ texto-documentation.ia.md  (prompt pronto p/ criar o manual no app)
├─ annotate.py                (gera imagens-tratadas a partir de imagens-puras)
├─ imagens-puras\             (01,02,03,04,05,07,08,09,10 originais — backup)
└─ imagens-tratadas\          (04,07,08,09 com setas verdes — usadas no manual)
```

---

## 3. Fluxo executado (passo a passo real)

Ambiente: conta **BeeFood3 - Manual** (`contato@beefood.com.br`), tema claro, produto **"10 mini churros"**.

1. **Edição Fiscal** (`/edicao-fiscal`, só desktop): grupo de colunas **"IBS/CBS (Reforma)"** ativo.
2. Marcar o produto → **EDITAR IMPOSTOS** → modal **"Editar Impostos em Lote"**.
3. Seção **IBS/CBS (Reforma Tributária)**:
   - **CST IBS/CBS** = `000 – Tributação integral`.
   - **cClassTrib** = `000001` (o select **filtra pelo CST**: para 000 vêm 000001–000004).
   - **Alíq. IBS UF (%)** = `0,10` · **Alíq. CBS (%)** = `0,90`.
4. **PRÓXIMO** → revisão → **CONFIRMAR (F2)** → **"Concluído! 1 produto atualizado"**.

---

## 4. Mapa das imagens (número da seta → alvo)

| Arquivo | Etapa | Setas |
|---------|-------|-------|
| `01-edicao-fiscal-grade.png` | (contexto) tela Edição Fiscal | — |
| `02-grupos-colunas-ibscbs.png` | (contexto) ativar grupo IBS/CBS | — |
| `03-colunas-ibscbs-grade.png` | (contexto) colunas IBS/CBS na grade | — |
| `04-produto-selecionado-editar-impostos.png` | Editar | ① checkbox do produto ② EDITAR IMPOSTOS |
| `07-cst-catalogo-carregado.png` | Editar | ① busca de CST ② opção 000 – Tributação integral |
| `08-modal-preenchido.png` | Editar | ① CST IBS/CBS ② cClassTrib ③ Alíq. IBS UF ④ Alíq. CBS ⑤ PRÓXIMO |
| `09-revisar-alteracoes.png` | Revisar | ① alterações a aplicar ② CONFIRMAR (F2) |
| `10-concluido.png` | (contexto) "Concluído!" | — |

> Coordenadas no `annotate.py` (frações 0..1). Reanotar: `python annotate.py`.
> Coords da grade (04) medidas via bounding box real; coords do modal (07/08/09) estimadas e conferidas visualmente.

---

## 5. Resumo técnico (ver `fluxo-codigo.md`)

- 6 colunas em `_produtoImpostos`; editáveis em `ModalEditarImpostosBatch.tsx` (Edição Fiscal).
- Catálogos `_IBSCBSCST` e `_IBSCBSClassTrib` (cClassTrib filtra pelo CST).
- Salvar: `POST /api/fiscal2/edicaoFiscal/produto`.
- Na nota: `_produtoImpostos` → snapshot `_NFeConfigProduto` → Delphi `cNFe.preencheIBSCBS` monta o grupo `<IBSCBS>` no XML (ACBr). Sem CST, o grupo não é emitido.

---

## 6. Decisões / observações

- **Bloqueio resolvido:** catálogos vinham vazios por **cache de localStorage** desatualizado;
  **logout + login** atualizou os dados (API de produção já corrigida).
- Edição **grava de verdade** (reversível) mas **não emite nota**.
- Exemplo da nota é **fictício** — nada de XML/NFC-e real no manual.

---

## 7. Estado deixado no sistema

- Produto **"10 mini churros"** ficou com a config IBS/CBS aplicada (CST 000 / cClassTrib 000001 / IBS UF 0,10 / CBS 0,90). Reversível pela própria tela, se quiser limpar.

---

## 8. Possíveis próximos incrementos

- Documentar a **aba IBS/CBS no modal de produto dentro da nota** (`ModalEditarProdutoNF.tsx`, telas `/nfe` e `/nfce`).
- Exemplos de outros CSTs (isenção 400, redução 200) e o efeito no grupo da nota.
