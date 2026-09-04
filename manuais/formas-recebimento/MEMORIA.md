# MEMÓRIA — Cadastrar forma de recebimento (#82)

Manual **de cadastro**, produzido na mesma sessão dos manuais **#80** (mesas) e **#81**
(comandas). O pedido do dono foi *"como cadastrar forma de recebimento para delivery, presencial e
PDV"* — e a resposta principal do manual é que **PDV não tem switch próprio**: ele está dentro de
**Presencial**.

Estado: ✅ **Concluído** em 03/09/2026. 11 imagens (10 com setas, 1 de contexto), 25 setas.

---
    10|
## 1. O que o manual afirma, e com que prova

| Afirmação | Prova |
|-----------|-------|
| **Presencial** cobre PDV, mesa e comanda; não existe switch de PDV | Filtro do código (`tipo === 'DELIVERY' ? delivery : presencial`) e a forma nova aparecendo no recebimento de uma **mesa** |
| A forma nova entra na tela de recebimento com atalho de teclado | Capturado: *Vale Refeição Sodexo* em **CTRL+1** |
| A aba **Taxas e Bandeiras** não existe para todo tipo | Reproduzido ao vivo: com o tipo padrão `Dinheiro` a aba fica desabilitada, com o aviso *"Não disponível para este tipo de pagamento"* |
| **Taxa (%)** e **Desconto Fixo (R$)** são alternativas | Preencher um desabilita o outro (código + tela) |
| Trocar de aba **salva** a forma | Toast *"Forma de recebimento salva!"* — foi como a captura gravou antes das taxas |
    20|| O que o cliente vê vem de **outra tela** | As duas listagens capturadas lado a lado (21 formas no cadastro × 18 no cardápio digital) |
| O ajuste da forma aparece na hora de receber | Etiquetas `-1,00%`, `+3,00%` e `+R$ 5,00` visíveis na tela de pagamento |
| A listagem de Cadastros **não** tem excluir | Só os switches; a exclusão existe no financeiro e no cardápio |

Detalhe técnico, rotas e campos em `fluxo-codigo.md`.

---

## 2. Cenário no sandbox

    30|Exemplo escolhido: **um vale novo com taxa e prazo**, que é o caso real de quem fecha com uma
bandeira de benefícios.

| Campo | Valor usado |
|-------|-------------|
| Título | **Vale Refeição Sodexo** |
| Tipo | **Vale Refeição** (habilita a aba de taxas) |
| Canais | **Delivery/Retirada** e **Presencial** ligados |
| Ajuste no pagamento | **Sem ajuste** (o dropdown foi aberto só para fotografar as cinco opções) |
| Taxa (%) | **4,5** |
| Dias para Recebimento | **30** |
    40|
A base já tinha *Vale Alimentação* e *Vale Refeição* genéricos — o nome com a bandeira
(*Sodexo*) reforça o conselho do manual de ser específico no título.

Para o canal do cliente, o modal de **Cardápio Digital → Formas Recebimento** foi aberto e
preenchido com `Vale Sodexo`, mas **não** foi salvo: a imagem mostra o formulário, e o texto
explica o vínculo. Assim o cardápio público continuou como estava.

---

## 3. Armadilhas de captura
    50|
- **Clicar no texto do tipo não marca o radio.** `text=Vale Refeição` acha um `span`; o clique não
  troca o tipo — e a aba de taxas continua desabilitada (foi o que quebrou a primeira tentativa).
  O que funciona é o `id` do radio: `#tipo-Vale\\ Refeição`.
- **ESC fecha o modal inteiro.** Depois de abrir o select de *Ajuste no pagamento*, apertar ESC
  fechou o cadastro. Para sair do dropdown, clique numa opção (**Sem ajuste**, se não quer mudar).
- **A aba de taxas depende do tipo.** Se ela estiver cinza, o tipo é `Dinheiro`, `Fiado` ou
  `PIX Online`.
- **O modal do cardápio digital é um painel lateral** (sheet à direita), não um diálogo
    60|  centralizado — o recorte da imagem 10 pega só a faixa `x` de 0,635 a 1,0.
- **A tela de pagamento da mesa mostra dado do cliente.** O documento (CPF) foi **borrado no
  `annotate.py`** (parâmetro `borrao`, aplicado antes do recorte) porque o repositório é público.

---

## 4. Imagens

| Arquivo | Setas | Onde entra |
|---------|------:|------------|
| `01-menu-cadastros.png` | 1 | Onde fica |
    70|| `02-listagem.png` | 6 | A tela: é aqui que se liga o canal |
| `03-nova-forma.png` | 6 | Cadastrar uma forma |
| `04-ajuste-pagamento.png` | 2 | Desconto ou acréscimo na forma |
| `05-aba-taxas.png` | 4 | Aba Taxas e Bandeiras |
| `06-aba-tef.png` | 1 | Aba TEF |
| `07-forma-criada.png` | 2 | Conferindo o resultado |
| `08-pagamento-presencial.png` | 1 | Conferindo o resultado (com borrão no documento) |
| `09-cardapio-digital-formas.png` | 3 | Para o cliente ver na sacola |
| `10-cardapio-adicionar.png` | 3 | Para o cliente ver na sacola |
| `11-financeiro-formas.png` | contexto | E a terceira tela? |
    80|
---

## 5. Estado do ambiente ao terminar

- **21 formas** no cadastro de vendas (a nova é *Vale Refeição Sodexo*, ativa nos dois canais,
  taxa 4,5% e 30 dias).
- **18 formas** no cardápio digital — nenhuma criada por este manual.
- Nenhum recebimento registrado: a tela de pagamento da mesa 2 foi aberta e fechada sem confirmar.
