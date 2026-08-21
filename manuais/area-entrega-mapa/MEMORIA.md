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

Prova no cardápio: o cliente busca o CEP **18035-490**, confirma o número **13** e vê
a taxa do círculo (**R$ 5,99**). Sem tela de *Calculando…* / fora da área.

Capturas do menu em viewport 390×844, DPR 3. Não documentar o telefone de teste.
Propagação: 1 a 2 minutos.

`04-desenhando-circulo.png` ficou nas puras; o manual usa `04b` (campos preenchidos).
