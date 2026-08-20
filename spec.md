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

## Planos aprovados (aguardando execução)

| Plano | Manuais | Documento |
|-------|---------|-----------|
| Cardápio por segmento | #27–#31 | [`PLANO-CARDAPIO.md`](PLANO-CARDAPIO.md) |

Regras: limpar base sandbox **antes de cada manual**; fotos em todos produtos/opções dos exemplos (não documentar no texto).

## Validação

```bash
python validar-imagens.py
python validar-imagens.py fiado
```
