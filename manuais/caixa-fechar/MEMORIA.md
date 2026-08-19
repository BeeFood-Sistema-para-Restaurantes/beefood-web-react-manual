# MEMÓRIA — Manual de Fechar Caixa

> Memória detalhada deste manual (fluxo, uso, decisões e estado), para retomar a qualquer momento.
> Ver também a memória geral: `../../MEMORIA-GERAL.md`.

Status: ✅ **Concluído** — Última atualização: 2026-08-19

---

## ⚠️ NÃO FAÇA A 2ª CONFERÊNCIA NESTE CAIXA

O **caixa1 fechado em 19/08/2026 10:18** (quebra de **R$ 2,55**) foi deixado de propósito
**sem a segunda conferência**, porque ele é o cenário do **próximo manual** (dupla checagem).

Se alguém clicar em **Adicionar 2ª Conferência** nesse caixa, o cenário é perdido: o caixa
ganha o cadeado, a conferência trava e não há como refazer sem reabrir e fechar de novo.

---

## 1. Escopo do manual

Ensinar o usuário final a:

1. Abrir a tela de fechamento (**Caixa → Ver Caixa → FECHAR CAIXA**).
2. Resolver as **vendas sem pagamento total** antes de fechar.
3. Conferir os valores forma por forma (**1ª conferência**), usando a **calculadora**.
4. Entender a **quebra de caixa** (falta/sobra).
5. **Salvar sem fechar** ou **fechar** o caixa e imprimir o resumo.
6. Confirmar o resultado na listagem.

Fora do escopo, por decisão do dono:

- **Segunda conferência** → vira manual próprio, usando este mesmo caixa.
- **Versão mobile** → não coberta.

Arquivo final: `caixa-fechar.md`. Mapa técnico: `fluxo-codigo.md`.

---

## 2. Descoberta que mudou o escopo

Não existe modal separado de conferência. O `CaixaFecharModal` **é** a tela de conferência
(título em tela: *Conferência de Valores - 1ª Conferência*) e é o mesmo componente usado
pelo **Ver Conferência**, apenas com `readOnly={true}`.

Por isso o manual deixou de ser "fechar, depois conferir" e passou a ser um percurso único.
Consequência para o backlog: a ideia **"Ver conferência (caixa fechado)"** não precisa de
manual próprio — cabe no manual da segunda conferência.

---

## 3. Fluxo executado (passo a passo real)

Ambiente: conta **BeeFood3 - Manual** (`contato@beefood.com.br`), tema claro, produção.
Caixa usado: **caixa1**, aberto em **17/07/2026 11:59**.

1. **Vendas pendentes:** ao clicar em FECHAR CAIXA, o sistema listou **74 vendas sem
   pagamento total**.
2. **Quitada uma venda como exemplo:** venda **#723** (2× Sprite Zero 350ml, **R$ 17,80**),
   paga em **Cartão de Débito**. A linha virou **PAGA** com Faltante R$ 0,00 e o aviso
   seguinte passou a falar de **73 vendas pendentes**.
3. **Seguiu com FECHAR CAIXA MESMO ASSIM (F2)** → **FECHAR ASSIM MESMO (ENTER)**.
4. **1ª conferência** com 6 formas de pagamento:

   | Forma | Entrada | Conferido | Diferença |
   |-------|---------|-----------|-----------|
   | Dinheiro | R$ 102,55 | R$ 100,00 | **-R$ 2,55** |
   | Cartão de Débito | R$ 1.277,26 | R$ 1.277,26 | R$ 0,00 |
   | Cartão de Crédito | R$ 306,05 | R$ 306,05 | R$ 0,00 |
   | Vale Alimentação | R$ 114,20 | R$ 114,20 | R$ 0,00 |
   | Vale Refeição | R$ 33,33 | R$ 33,33 | R$ 0,00 |
   | PIX Beetech | R$ 78,59 | R$ 78,59 | R$ 0,00 |

   O dinheiro foi contado pela **calculadora**: R$ 50 + R$ 20 + R$ 20 + R$ 10 = **R$ 100,00**.
   A quebra leve de **R$ 2,55** foi criada de propósito (pedido do dono), para ser resolvida
   no manual da segunda conferência.

5. **Resultado:** Total Entrada **R$ 1.911,98**, Entrada Conferida **R$ 1.909,43**,
   **Quebra de Caixa R$ 2,55 (Falta)**.
6. **Fechado de verdade** (`Confirma fechamento do caixa?` → **Fechar caixa**).
7. **Impressão:** respondida **Não** na pergunta *Deseja imprimir a conferência?* — a captura
   da pergunta bastou para o manual e evitou disparar a impressora.
8. **Listagem:** caixa1 com fechamento em **19/08/2026 10:18**, Conf. Saldo Final
   **R$ 1.909,43** e Quebra de Caixa **R$ 2,55**.

---

## 4. Mapa das imagens (número da seta → alvo)

| Arquivo | Etapa | Setas |
|---------|-------|-------|
| `01-listagem-caixa-aberto.png` | 1 | 1 Em aberto · 2 Ver Caixa (lupa) |
| `02-ver-caixa-fechar.png` | 1 | 1 FECHAR CAIXA · 2 VALOR EM CAIXA |
| `03-vendas-pendentes.png` | 2 | 1 botão verde (pagar) · 2 Faltante · 3 FECHAR CAIXA MESMO ASSIM |
| `04-pagamento-venda.png` | 2 | 1 Pagamentos realizados/Pago · 2 Pagamento completo |
| `05-venda-paga.png` | 2 | 1 botão virou check · 2 badge PAGA |
| `06-aviso-fechar-mesmo-assim.png` | 2 | 1 motivos · 2 NÃO, REVISAR · 3 FECHAR ASSIM MESMO |
| `07-conferencia-em-branco.png` | 3 | 1 Entrada · 2 campo 1ª Conferência · 3 calculadora · 4 seta do detalhe do Dinheiro |
| `08-calculadora-dinheiro.png` | 3 | 1 campo de valor · 2 Valores Adicionados · 3 Total · 4 Incluir Conferência |
| `09-conferencia-com-quebra.png` | 4 | 1 Diferença -R$ 2,55 · 2 Quebra de Caixa · 3 Saldo Final Conferido |
| `10-confirmar-fechamento.png` | 5 | 1 Fechar caixa |
| `11-imprimir-conferencia.png` | 5 | 1 Sim, imprimir · 2 Não |
| `12-listagem-fechado.png` | 6 | 1 Data/Hora Fechamento · 2 Conf. Saldo Final · 3 Quebra de Caixa |

> Coordenadas das setas estão no `annotate.py` (frações 0..1). Para reanotar: `python annotate.py`.
> Nos modais os badges ficam na margem escurecida do overlay e as setas apontam para dentro,
> encostando na **borda** do elemento — assim nenhum número cobre valor ou rótulo.

---

## 5. Decisões de produção

- **Numeração `1, 2, 3`** no texto (não `①②③`): pedido do dono, porque o `③` fica ilegível.
  Os badges das imagens já eram números normais desenhados pelo `annotate.py`.
- **Cenário real, não montado:** o caixa1 tinha movimento em 6 formas de pagamento, o que
  deixa a tabela de conferência representativa. Nenhum valor foi inventado.
- **Quitar uma venda de exemplo** em vez de só mostrar a tela de pendências: assim o manual
  ensina o caminho recomendado, e não apenas o "fechar mesmo assim".
- **`annotate.py` com fallback de fonte:** Arial no Windows do dono, Arimo/DejaVu no Cloud
  Agent. O script roda nas duas máquinas sem edição.
- **Imagem 08 (calculadora):** a lista de valores rola e o primeiro lançamento (R$ 50,00)
  ficou fora da área visível. O texto do manual explica isso. Não foi possível recapturar
  porque, com o caixa fechado, a calculadora fica desabilitada (`readOnly`).
- **CPF desfocado na imagem 04:** a tela de pagamento mostra o campo **Documento** do cliente
  (dado pessoal, ainda que de um cliente de teste). A região é desfocada pelo `annotate.py`,
  via parâmetro `blur=` da função `annotate`, antes de desenhar as setas — o rótulo
  "Documento" continua visível, só o número fica ilegível. Se outras telas trouxerem dado
  pessoal, use o mesmo parâmetro.

---

## 6. Estado deixado no sistema

- **caixa1 FECHADO** em 19/08/2026 10:18, com quebra de **R$ 2,55 (Falta)** e **sem** segunda
  conferência — reservado para o próximo manual (ver aviso no topo).
- **Vendas #720, #722 e #723 quitadas** durante os testes e a produção (R$ 13,34 e R$ 28,16 nos
  ensaios, R$ 17,80 na captura final). As demais pendências foram mantidas.
- **Nenhum caixa aberto** na conta ao final. Para voltar a usar o PDV é preciso abrir um caixa
  novo (**Caixa → Abrir Caixa**) ou reabrir o caixa1 — mas **reabrir o caixa1 estraga o
  cenário do próximo manual**, então prefira abrir um novo.

---

## 7. Possíveis próximos incrementos

- Manual da **2ª conferência** usando este caixa (já aprovado pelo dono).
- Cobrir a **versão mobile** do fechamento.
- Recapturar a calculadora com a lista rolada para o topo, num caixa com movimento em dinheiro.
- Mostrar o **Resumo Conferência de Caixa** impresso (respondemos "Não" na impressão).
