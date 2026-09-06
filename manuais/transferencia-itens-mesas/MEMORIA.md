# MEMORIA.md — Transferir item entre mesas e comandas

Manual **#94**. Produzido em 06/09/2026. Sandbox BeeFood3.

Última atualização: 2026-09-06.

## O que o manual afirma

| Afirmação | Prova |
|-----------|-------|
| Move a **linha inteira** para outra conta **ABERTO** | Chicken Deluxe saiu da Mesa 16 (#941) e entrou na Comanda 1 (#942) |
| Destino não é mesa Livre | Lista = `venda2/mesa` com `situacao === "ABERTO"`; Comanda 1 estava aberta (R$ 0,00) |
| Não é o chip de mesa/comanda | Texto; código em `ModalSelecionarMesaComanda` |
| Taxa acompanha o item | Origem: R$ 35,15 → R$ 19,20; destino: R$ 0,00 → R$ 15,95 (14,50 + 1,45) |

## Cenário

| Conta | Venda | Antes | Depois |
|-------|-------|-------|--------|
| Mesa 16 | **#941** | Chicken Deluxe R$ 14,50 + Anéis R$ 19,20 + taxa R$ 1,45 = **R$ 35,15** | Só Anéis **R$ 19,20** (anel sem taxa, #85) |
| Comanda 1 | **#942** | Aberta, R$ 0,00 | Chicken Deluxe + taxa **R$ 15,95** |

Caixa `caixa1` em aberto desde 01/09/2026. Login `contato@beefood.com.br`.

A Comanda 1 foi salva sem item (busca *Coxinha* vazia) — destino vazio é válido.
Não ensinar “salvar conta vazia” como procedimento; o texto diz só que a conta
já estava aberta.

## Armadilhas

- Lista de destino mistura contas avulsas antigas (ex.: venda #938 “felipe”).
  A captura do passo 2 filtrou a busca **Comanda** para não publicar nome.
- `get_by_role(name=lambda)` e `filter(has_text=lambda)` quebram no Playwright
  Python desta VM.
- Anéis continuam **Sem taxa de serviço** (#85): a origem depois fica com taxa
  R$ 0,00 mesmo com o switch ligado — não transformar isso em lição deste manual.
- Botão Transferir **não** existe em delivery.

## Imagens

6 no `.md` (01–06). Extras nas puras (`01-mapa-mesas`, `04b`, `04-passo-destino`
sem filtro) não entram no manual.

## Help

`/mesas` → slug `transferencia-itens-mesas` (anotar em `help-manuais.ts` no front).
