# MEMÓRIA — Cadastrar comandas e gerar o QR Code (#81)

Manual **de cadastro**, par do **#80** (`manuais/cadastro-mesas/`). A tela é a mesma; o manual
existe separado porque o fluxo do cliente é diferente — a comanda anda com a pessoa.

Estado: ✅ **Concluído** em 03/09/2026. 12 imagens (11 com setas, 1 de contexto), 27 setas.

---

## 1. O que o manual afirma, e com que prova

    10|| Afirmação | Prova |
|-----------|-------|
| O cadastro sugere o próximo código e a descrição `Comanda N` | Criada a **Comanda 26** com o modal aberto do zero |
| O lote cria a faixa inteira, até 100 por vez | 4 comandas criadas de uma vez (27 a 30); contador foi de 26 para 30 |
| A exclusão repete a descrição e avisa que não tem volta | Diálogo fotografado na Comanda 26 e cancelado |
| São três tipos de QR Code | Os três gerados: URL do cardápio, `38311_c1` e EAN-13 `2 103831 100012` |
| Mesa e comanda têm códigos diferentes de propósito | EAN-13 da Comanda 1 (`2 103831 …`) contra o da Mesa 1 (`2 003831 …`) — o segundo dígito é o tipo |
| **Não** existe o gate "você usa comanda?" aqui | Escolher *Cardápio Digital Presencial* vai direto para a faixa |
| Comanda cadastrada vira card na aba Comandas | Mapa capturado com as 30 comandas |

Detalhe técnico e diferenças em relação às mesas em `fluxo-codigo.md`.
    20|
---

## 2. Cenário no sandbox

A base já tinha **25 comandas (1 a 25)**. O manual criou a 26 individualmente e as 27 a 30 em
lote, fechando a faixa 1–30 — número redondo, que serviu de exemplo prático ("30 comandas em
circulação").

| Passo do manual | O que foi feito |
|-----------------|-----------------|
    30|| Cadastro individual | **Comanda 26** (código e descrição sugeridos) |
| Exclusão | Diálogo aberto na Comanda 26 e **cancelado** |
| Lote | 4 comandas a partir da **27** → Comanda 27 a Comanda 30 |
| QR Codes | Faixa **1 a 4** nos três tipos |
| Mapa | Aba **Comandas** |

O conflito de numeração **não** foi fotografado aqui (a imagem existe no #80); o texto explica o
aviso em uma frase.

---
    40|

## 3. Armadilhas de captura

Valem as mesmas do #80, com um detalhe a mais:

- **O menu é `button`, não `<a>`** — clicar em `text=Cadastros` e depois em
  `page.locator("button", has_text="Comandas").first`.
- **A folha de impressão sai pelo iframe oculto `#beefood-print-frame`**: instale o poll de 40 ms
  antes de clicar em *Imprimir Todos* e renderize o HTML capturado numa aba limpa (receita
  completa no `MEMORIA.md` do #80).
    50|- **Dois ESC para sair dos modais de QR** (o modal do QR fica sobre o seletor de tipo).
- **A aba do mapa é ambígua:** `text=Comandas` casa com vários elementos. No mapa do salão,
  `page.locator("text=Comandas").first` resolve; no cadastro, prefira o `button` do submenu.

---

## 4. Imagens

| Arquivo | Setas | Onde entra |
|---------|------:|------------|
    60|| `01-menu-cadastros.png` | 1 | Onde fica |
| `02-tela-comandas.png` | 5 | A tela de comandas |
| `03-nova-comanda.png` | 4 | Cadastrar uma comanda |
| `04-excluir-comanda.png` | 2 | Editar e excluir |
| `05-lote-previsao.png` | 3 | Criar a faixa inteira |
| `06-lote-resultado.png` | 1 | Criar a faixa inteira |
| `07-qr-tipos.png` | 3 | Os três tipos de QR Code |
| `08-qr-cardapio-presencial.png` | 4 | Cardápio Digital Presencial |
| `09-folha-impressa.png` | contexto | Cardápio Digital Presencial |
| `10-qr-codigo-comanda.png` | 2 | Código da Comanda |
    70|| `11-codigo-barras.png` | 1 | Código de Barras |
| `12-mapa-comandas.png` | 3 | O que o cadastro habilita |

O `annotate.py` é o mesmo do #80 com as coordenadas ajustadas (os rótulos são mais largos:
*Nova Comanda (F1)*, *25 comandas*).

---

## 5. Estado do ambiente ao terminar

    80|- **30 comandas** cadastradas (códigos 1 a 30), todas ativas.
- Nenhuma comanda excluída; nenhuma venda criada.
- 19 mesas cadastradas pelo manual #80, na mesma sessão.
