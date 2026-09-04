# MEMÓRIA — Cadastrar mesas e gerar o QR Code (#80)

Manual **de cadastro**: percorre a tela inteira de Cadastros → Mesas e os três tipos de QR Code,
terminando com um exemplo prático de montagem do salão.

Estado: ✅ **Concluído** em 03/09/2026. 17 imagens (15 com setas, 2 de contexto), 41 setas.

Manual irmão: **#81** (`manuais/cadastro-comandas/`). Os dois foram produzidos na mesma sessão,
com o **#82** (`manuais/formas-recebimento/`).

---
    10|

## 1. O que o manual afirma, e com que prova

| Afirmação | Prova |
|-----------|-------|
| O cadastro sugere o próximo código livre e a descrição `Mesa N` | Criada a **Mesa 1** com o modal aberto do zero |
| O lote avisa quando a faixa esbarra em mesas existentes | Pedido 4 mesas a partir da 5: *"As mesas 5, 6, 7, 8 já existem."*, com o botão bloqueado |
| O lote cria a faixa inteira | 4 mesas criadas de uma vez (16 a 19); contador foi de 15 para 19 |
| São três tipos de QR Code, com conteúdos diferentes | Os três gerados na tela: URL do cardápio, `38311_1` e EAN-13 `2 003831 100015` |
| O QR do cardápio gera pela **faixa**, sem conferir o cadastro | Está no código (`ModalQRCode`) e vale como aviso no texto |
| Existe um gate que recomenda QR de comanda | Reproduzido: pergunta → comparativo → *CONTINUAR COM QR CODE DE MESA (ENTER)* |
    20|| A folha de impressão sai em grade de 3 com logo e nome da mesa | Capturada de verdade (ver seção 3) |
| Mesa cadastrada vira card no mapa do salão | Mapa capturado com as 19 mesas, incluindo *Livre*, *Ocupado* e *Fechado* |

Detalhe técnico, rotas e limites em `fluxo-codigo.md`.

---

## 2. Cenário no sandbox

A base já tinha **14 mesas (códigos 2 a 15)** e o código **1 estava vago** — sorte, porque deu o
exemplo perfeito para o cadastro individual sem inventar nome estranho. O lote entrou na sequência
    30|(16 a 19), fechando a faixa 1–19.

| Passo do manual | O que foi feito |
|-----------------|-----------------|
| Cadastro individual | **Mesa 1** (código 1, descrição `Mesa 1`) |
| Conflito do lote | 4 mesas a partir da **5** — só para fotografar o aviso, sem criar |
| Lote válido | 4 mesas a partir da **16** → Mesa 16 a Mesa 19 |
| QR Codes | Faixa **1 a 4** nos três tipos |
| Mapa do salão | Aba **Mesas**, 19 cards |

Nada foi excluído: o diálogo de exclusão foi fotografado e **cancelado**.
    40|

---

## 3. A folha de impressão (o truque do iframe)

O **Imprimir Todos** não abre janela nova: usa `imprimirViaIframe`, que escreve o HTML num iframe
oculto de id **`beefood-print-frame`** — o mesmo caminho do cupom no #74. Para fotografar a folha:

1. Antes do clique, instalar um `setInterval` de 40 ms que lê
   `document.getElementById('beefood-print-frame').contentDocument.documentElement.outerHTML`.
2. Clicar em **Imprimir Todos**.
    50|3. Renderizar o HTML capturado numa aba limpa com `set_content`, viewport de 900 px, e tirar o
   screenshot com `full_page=True`.

Funcionou na primeira tentativa e rendeu a melhor imagem do manual (a folha pronta para recortar).

---

## 4. Armadilhas de captura

- **O item do menu não é `<a>`.** O submenu Cadastros é montado com `button`; `a[href=...]` não
  acha nada. O que funciona é `page.locator("button", has_text="Mesas").first` **depois** de
    60|  clicar em `text=Cadastros`.
- **O modal individual não tem atalho.** Não existe ENTER/ESC no *Nova Mesa* — clique em
  **Salvar**.
- **Só o lote valida código repetido.** O cadastro individual aceita e o backend resolve; para
  fotografar o conflito, use o lote.
- **O gate de comanda só aparece em mesas** e só na opção *Cardápio Digital Presencial*.
- **Feche os modais de QR com dois ESC**: o modal do QR fica sobre o seletor de tipo.
- **O cardápio presencial não mostra o número da mesa na home.** A imagem 18 é só o cardápio
  abrindo no celular; o número viaja no link (`?tipo=p&mesa=1`). Tentar provar o "Mesa 1" na tela
  exigiria montar a sacola, e os cliques no cardápio (Vuetify) falham por elemento fora da
    70|  viewport — não vale o esforço para este manual.

---

## 5. Imagens

| Arquivo | Setas | Onde entra |
|---------|------:|------------|
| `01-menu-cadastros.png` | 2 | Onde fica |
| `02-tela-mesas.png` | 5 | A tela de mesas |
| `03-nova-mesa.png` | 4 | Cadastrar uma mesa |
    80|| `05-editar-mesa.png` | 2 | Editar e excluir |
| `06-excluir-mesa.png` | 2 | Editar e excluir |
| `07-lote-conflito.png` | 3 | Criar o salão de uma vez |
| `08-lote-previsao.png` | 2 | Criar o salão de uma vez |
| `09-lote-resultado.png` | 2 | Criar o salão de uma vez |
| `10-qr-tipos.png` | 3 | Os três tipos de QR Code |
| `11-qr-gate-comanda.png` | 2 | Cardápio Digital Presencial |
| `12-qr-recomendacao.png` | contexto | Cardápio Digital Presencial |
| `13-qr-cardapio-presencial.png` | 4 | Cardápio Digital Presencial |
| `14-qr-codigo-mesa.png` | 2 | Código da Mesa |
    90|| `15-codigo-barras.png` | 1 | Código de Barras |
| `16-mapa-salao.png` | 3 | O que o cadastro habilita |
| `17-folha-impressa.png` | contexto | Exemplo prático |
| `18-cardapio-celular.png` | contexto | Exemplo prático |

A pura `04-mesa-criada.png` ficou na pasta como registro do passo, mas **não entra no manual**
(a imagem 09 já mostra a lista depois de gravar).

O `annotate.py` recebe as coordenadas em frações da **imagem cheia** e converte para o recorte
sozinho, com recortes reaproveitados (`BARRA`, `MODAL_P`, `MODAL_M`, `MODAL_QR`) — os modais desta
tela repetem a mesma geometria.
   100|
---

## 6. Estado do ambiente ao terminar

- **19 mesas** cadastradas (códigos 1 a 19), todas ativas.
- Nenhuma mesa excluída; nenhuma venda criada.
- O cache `mesaComanda_cache` é limpo pela própria tela ao entrar — não há nada a restaurar.
