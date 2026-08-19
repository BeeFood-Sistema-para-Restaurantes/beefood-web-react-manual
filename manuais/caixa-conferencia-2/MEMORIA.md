# MEMÓRIA — Manual da Segunda Conferência

> Memória detalhada deste manual (fluxo, uso, decisões e estado), para retomar a qualquer momento.
> Ver também a memória geral: `../../MEMORIA-GERAL.md` e o manual anterior: `../caixa-fechar/`.

Status: ✅ **Concluído** — Última atualização: 2026-08-19

---

## 1. Escopo do manual

Continuação direta do manual **#2 (Fechar caixa)**. Ensina o usuário final a:

1. Abrir a conferência de um caixa já fechado (**Ver Conferência**).
2. Iniciar a **2ª conferência** (dupla checagem).
3. Recontar os valores, com a **calculadora**.
4. Comparar as duas contagens e resolver a **quebra de caixa**.
5. Registrar a **observação**, marcar a declaração e **Conferir**.
6. Entender o que muda depois (cadeado, travamento, saldo conferido atualizado).

O manual abre com uma seção sobre **por que a dupla checagem importa** (pedido do dono),
com três argumentos: protege a equipe de suspeita injusta, deixa registro auditável e faz o
saldo conferido refletir a recontagem.

Fora do escopo: versão mobile.

Arquivo final: `caixa-conferencia-2.md`. Mapa técnico: `fluxo-codigo.md`.

---

## 2. Como este manual se encaixa no #2

O #2 fechou o **caixa1** de propósito com uma **quebra leve de R$ 2,55 (Falta)**: o dinheiro
apurado era R$ 102,55 e a contagem deu R$ 100,00. Este manual resolve exatamente essa quebra,
o que dá uma narrativa contínua entre os dois:

| Manual | O que acontece com o dinheiro |
|--------|-------------------------------|
| #2 Fechar caixa | Contagem dá **R$ 100,00** contra R$ 102,55 → quebra de **R$ 2,55 (Falta)** |
| #12 Segunda conferência | Recontagem acha **R$ 2,55 em moedas** → total **R$ 102,55** → quebra **resolvida** |

A recontagem foi lançada na calculadora como **R$ 100,00 + R$ 2,55**, o que rende uma imagem
melhor que a do #2: com só dois lançamentos, a lista **Valores Adicionados** aparece inteira,
sem rolagem.

---

## 3. Fluxo executado (passo a passo real)

Ambiente: conta **BeeFood3 - Manual** (`contato@beefood.com.br`), tema claro, produção.
Caixa: **caixa1**, aberto em 17/07/2026 11:59 e fechado em 19/08/2026 10:18.

1. **Listagem** → caixa1 com Conf. Saldo Final R$ 1.909,43 e Quebra de Caixa R$ 2,55.
2. **Ver Conferência** (botão verde) → 1ª conferência em modo leitura, campos em cinza, com o
   botão **Adicionar 2ª Conferência** ao lado do título.
3. **Adicionar 2ª Conferência** → título vira *2ª Conferência*, colunas em branco, aparece a
   coluna **1ª Conferência** e a seção de observações.
4. **Recontagem** das 6 formas:

   | Forma | Entrada | 2ª Conferência | 1ª Conferência | Diferença |
   |-------|---------|----------------|----------------|-----------|
   | Dinheiro | R$ 102,55 | **R$ 102,55** | R$ 100,00 | R$ 0,00 |
   | Cartão de Débito | R$ 1.277,26 | R$ 1.277,26 | R$ 1.277,26 | R$ 0,00 |
   | Cartão de Crédito | R$ 306,05 | R$ 306,05 | R$ 306,05 | R$ 0,00 |
   | Vale Alimentação | R$ 114,20 | R$ 114,20 | R$ 114,20 | R$ 0,00 |
   | Vale Refeição | R$ 33,33 | R$ 33,33 | R$ 33,33 | R$ 0,00 |
   | PIX Beetech | R$ 78,59 | R$ 78,59 | R$ 78,59 | R$ 0,00 |

5. **Totais:** Entrada Conferida **R$ 1.911,98**, **Quebra de Caixa: Correto**,
   **Quebra 1ª Conf.: R$ 2,55 (Falta)**, Saldo Final Conferido **R$ 1.911,98**.
6. **Observação registrada:** *"Recontagem feita pela gerência: localizados R$ 2,55 em moedas
   que não haviam sido contados. Valores conferem."*
7. **Checkbox** *Conferência realizada e valores conferidos* marcado → botão **Conferir** ficou
   verde e habilitado.
8. **Confirmado** em *Confirma a conferência do caixa?* → **Conferir**.
9. **Resultado:** cadeado na listagem, Conf. Saldo Final atualizado para **R$ 1.911,98** e
   Quebra de Caixa **R$ 0,00** com check verde. Ao reabrir, a tela vem travada e o botão
   *Adicionar 2ª Conferência* não existe mais.

> **Ensaio antes de valer:** todo o fluxo foi executado uma vez sem clicar em **Conferir**
> (nada é gravado até a confirmação), as imagens foram revisadas e só então a ação real foi
> disparada. Vale repetir essa técnica em qualquer manual com passo irreversível.

---

## 4. Mapa das imagens (número da seta → alvo)

| Arquivo | Etapa | Setas |
|---------|-------|-------|
| `01-listagem-caixa-fechado.png` | 1 | 1 Quebra de Caixa R$ 2,55 · 2 Ver Conferência (botão verde) |
| `02-primeira-conferencia-leitura.png` | 1 | 1 Adicionar 2ª Conferência · 2 campos travados · 3 Quebra de Caixa (Falta) |
| `03-segunda-conferencia-em-branco.png` | 2 | 1 coluna 2ª Conferência · 2 coluna 1ª Conferência · 3 Observações |
| `04-calculadora-recontagem.png` | 3 | 1 campo de valor · 2 Valores Adicionados (100,00 + 2,55) · 3 Total R$ 102,55 · 4 Incluir Conferência |
| `05-segunda-conferencia-conferida.png` | 4 | 1 valor recontado com check · 2 1ª Conferência ao lado · 3 Quebra de Caixa: Correto · 4 Quebra 1ª Conf. |
| `06-observacoes-conferido.png` | 5 | 1 Observações · 2 checkbox marcado · 3 Conferir habilitado |
| `07-confirmar-conferencia.png` | 5 | 1 botão Conferir na confirmação |
| `08-listagem-conferido.png` | 6 | 1 cadeado · 2 Conf. Saldo Final atualizado · 3 Quebra zerada |
| `09-conferencia-travada.png` | 6 | 1 campos travados · 2 as duas contagens registradas · 3 Conferir desabilitado |

> Coordenadas no `annotate.py` (frações 0..1). Para reanotar: `python annotate.py`.
> A imagem `08` foi capturada com viewport mais largo (1680 px) para caber o **cadeado**
> (à esquerda) e as colunas **Conf. Saldo Final** e **Quebra de Caixa** (à direita) na mesma
> foto. Como o `annotate.py` usa frações, a diferença de tamanho não afeta as setas.

---

## 5. Decisões de produção

- **Numeração `1, 2, 3`** no texto, como no #2.
- **Recontagem em dois lançamentos** (R$ 100,00 + R$ 2,55) em vez de recontar cédula por
  cédula: mantém a lista da calculadora visível por inteiro e conta uma história clara
  ("apareceram R$ 2,55 em moedas").
- **Observação escrita de verdade** no campo, para o manual mostrar um exemplo real de registro
  em vez de um campo vazio.
- **Seção de abertura sobre a importância** da dupla checagem, a pedido do dono, antes das
  etapas operacionais.

---

## 6. Estado deixado no sistema

- **caixa1**: fechado **e conferido** (cadeado). Conf. Saldo Final R$ 1.911,98, Quebra de Caixa
  R$ 0,00. Não é possível fazer outra conferência nele.
- **Data/Hora Fechamento mudou** de 19/08/2026 10:18 para **10:54** — o `tipo: "CONFERIR"`
  regrava esse campo. Por isso o manual #2 (capturado antes) mostra 10:18 e este mostra 10:54.
  Não é erro de captura.
- Existe um **caixa aberto** (19/08/2026 10:35, saldo inicial R$ 0,00) para o PDV seguir
  utilizável. Ele não foi usado neste manual.
- Para produzir um manual novo que precise de caixa fechado **sem** conferência, será preciso
  fechar outro caixa — o caixa1 já está conferido.

---

## 7. Possíveis próximos incrementos

- Cobrir a **versão mobile** da conferência.
- Mostrar o **Resumo Conferência de Caixa** impresso (o botão **Imprimir** existe também aqui,
  no canto inferior esquerdo, e não foi explorado).
- Um exemplo em que a recontagem **também** não bate, para ensinar o que fazer quando a quebra
  é real.
