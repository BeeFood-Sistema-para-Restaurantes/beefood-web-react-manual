# MEMÓRIA — #46 PDV balança

Status: ✅ 21/08/2026. Fluxo 100% no PDV **digitando** o EAN-13 (sem hardware).

## Produto

**Queijo Mussarela**, código **199**, unidade **KG**, R$ 39,90 / kg, foto (queijo). Setor Balcão.

## Layout

Balança ON, dígitos **2–6 / 7–12** (não o default 1–5 / 6–11).

Parser: `src/utils/balancaParser.ts`. 13 dígitos, começa com `2`. Zeros à esquerda do código caem (`00199` → `199`).

## Contas e códigos

| Tipo | EAN-13 | Conta | Resultado no PDV |
|------|--------|-------|------------------|
| Peso (0) | `2001990003501` | 000350/1000 = 0,350 kg × 39,90 | **0,350 KG / R$ 13,97** + toast *Produto adicionado via balança* |
| Valor (1) | `2001990019957` | 001995/100 = 19,95 / 39,90 | **0,500 KG / R$ 19,95** + toast 0.500 kg |

O 13º dígito do peso (`1`) não é o checksum EAN-13 canônico (`5`); o parser **não valida** o verificador. O do valor (`7`) bate com `calcularChecksumEAN13`.

Auto-insert ~180 ms no campo `Digite algo para buscar...`. Código interno `199` + Enter **não** pesa — é busca comum.

Não confundir com Aplicativos → Balança (PLU/serial).
