# MEMÓRIA — Manual #35 Configuração por mapa

Última atualização: 2026-08-21 (refação do zero)

Pré-requisito: #34. Tipo ativo: `tipoEntregaMapa`.

Sandbox, três regiões criadas do zero:

| Região | Forma | Taxa | Frete grátis | Tempo+ | Entregador |
|--------|-------|------|--------------|--------|------------|
| Até 2 km | Círculo 2 km na loja | R$ 5,99 | R$ 40,00 | 5 min | R$ 3,00 |
| Campolim | Polígono ao sul | R$ 7,90 | R$ 50,00 | 10 min | R$ 4,00 |
| Zona industrial | Círculo, `naoEntrega` | — | — | — | — |

O círculo de 2 km cobre **R. Arthur Gomes, 13** (Centro). Campolim e a zona industrial
ficam fora desse ponto, para o teste do cardápio cair só no círculo.

Prova no cardápio: CEP 18035-490 nº 13 → taxa do círculo; Av. Paulista 1000 → fora.

Capturas do menu em viewport 390×844, DPR 3. Não documentar o telefone de teste.
Propagação: 1 a 2 minutos.

Imagens de contexto do fluxo de CEP (06, 06b, 06c, 08) nas puras não entram no manual.
`04-desenhando-circulo.png` ficou nas puras; o manual usa `04b` (campos preenchidos).
