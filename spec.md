# BeeFood — Manuais (spec)

Repositório de manuais de usuário final do BeeFood (`https://beefood.app`).

## Stack

- Markdown + imagens PNG (puras + tratadas com `annotate.py`)
- Python 3.10+ e Pillow para anotações
- Playwright para capturas no Cloud Agent
- Código de referência: `beefood-web-react` e `beetech-server-node-2.0` (somente leitura)

## Estrutura

```
manuais/<nome>/
├── <nome>.md
├── fluxo-codigo.md
├── MEMORIA.md
├── texto-documentation.ia.md
├── annotate.py
├── imagens-puras/
└── imagens-tratadas/
```

## Conta sandbox

**BeeFood3 - Manual** — `contato@beefood.com.br`

## Planos executados

| Plano | Manuais | Documento |
|-------|---------|-----------|
| Cardápio por segmento | #27–#31 (concluídos) | [`PLANO-CARDAPIO.md`](PLANO-CARDAPIO.md) |
| Área de entrega | #34–#38 (refação 21/08/2026) | `manuais/endereco-restaurante/` + `manuais/area-entrega-*` |
| Parâmetros (Configuração) | #39–#46 concluídos (Opção B — 8 manuais) | [`PLANO-PARAMETROS.md`](PLANO-PARAMETROS.md) |

Endereço da loja no sandbox (BeeFood3): **R. Caramuru, 108 — Vila Leão, Sorocaba – SP,
18040-370**. Endereço de entrega de teste nos quatro tipos: **R. Arthur Gomes, 13 — Centro,
Sorocaba – SP, 18035-490**. No cardápio, os manuais #35–#38 mostram a **busca** (CEP ou
bairro), o formulário depois da busca e o endereço confirmado com a taxa — sem tela de
*Calculando…*.

Regras que valem para qualquer manual com cenário montado no sandbox: limpar a base **antes de
cada manual** (o dono faz e avisa) e inserir **foto em todos os produtos e opções** dos exemplos,
sem documentar isso no texto.

## Validação

```bash
python validar-imagens.py
python validar-imagens.py fiado
```
