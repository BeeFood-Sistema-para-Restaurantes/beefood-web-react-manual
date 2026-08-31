# MEMORIA.md — #72 Produto só com agendamento (encomenda)

## Escopo
O interruptor **Somente agendamento** do **produto**: onde fica
(cadastro e **Editar em Lote**), como conferir na lista (ícone de
calendário) e como o produto aparece no cardápio digital (etiqueta
**Encomenda** + tela **AGENDAR PEDIDO** forçada no Continuar).

Não cobre: os prazos e switches da aba Agendamento (#70), grade
semanal (#32), pausa (#33), filtro de agendados no Delivery,
Exibir/Ocultar (#68) e Preço Programado (#69).

## Origem
Pedido do dono (31/08/2026): o #70 documentou a aba, mas ficou de fora
a parte do **produto** que só aceita agendamento — e o pedido incluía
mostrar o **Editar em Lote** como caminho e o efeito no cardápio
digital. O próprio #70 já avisava, no rodapé, que esse switch era
"outro interruptor, item a item".

## Cenário montado no sandbox
Setor **Sobremesas**: os três pudins (Brigadeiro, Leite Condensado,
Zero Açúcar) marcados **em lote** como Somente Agendamento; o
**Brownie** ficou de fora, para servir de contraste na mesma tela
(card sem o ícone de calendário).

Estado da aba Agendamento durante as capturas (o mesmo que o #70
deixou): ON / ON / OFF, dias 2 e 7, 60 / 60 / 90 / 60, 5 pedidos.

## Imagens
| Arquivo | Tipo | O que mostra |
|---------|------|----------------|
| `01-lista-antes.png` | setas | Aba Produtos filtrada em Sobremesas + botão Editar em Lote |
| `02-lote-selecao.png` | setas | Etapa 1: Brownie desmarcado, 3 de 4 |
| `03-lote-campo.png` | setas | Etapa 2: Somente Agendamento = Sim + PROCESSAR |
| `04-lote-resultado.png` | setas | Etapa 3: 3 de 3, 3 sucesso |
| `05-lista-depois.png` | setas | Ícone de calendário nos pudins; Brownie sem |
| `06-produto-switch.png` | setas | Cadastro: Opções avançadas + switch + SALVAR E SAIR |
| `07-par-encomenda.png` | par | Painel (Sim) → cardápio (etiqueta Encomenda) |
| `08-cardapio-digital.png` | setas | Tira: etiqueta / Mais informações / AGENDAR PEDIDO |
| `07-cel-lista.png`, `08-cel-produto.png`, `09-cel-ajuda.png`, `10-cel-retirada.png`, `11-cel-agendar.png` | puras | Fontes do par e da tira |

## Descobertas (testes de campo)
- No cardápio a marca do produto se chama **Encomenda** (etiqueta
  vermelha com calendário), não "agendamento". O **?** ao lado abre
  *Mais informações → Produto disponível apenas por agendamento*.
- Com o item de encomenda na sacola, **Hoje** continua na tela e pode
  ficar marcado — mas o **Continuar** abre a tela **AGENDAR PEDIDO**.
  Produto normal (testado com Coca Zero) vai direto ao pagamento.
- **Sem o Agendamento geral ligado a marca não segura nada:**
  desliguei o switch da aba, esperei o cache e o pedido do pudim foi
  até as formas de pagamento sem agendar (o botão **Agendar**
  desaparece). Religado e conferido pelo GET: valores do #70 intactos.
- O campo da API é `importadoMatriz` — nome legado, sem relação com
  matriz.
- No lote, o valor do ToggleField nasce em **Não**: marcar o campo e
  processar **desliga** a flag. É o caminho para desfazer.
- O campo aparece também no lote de **Complementos**, mas o cadastro
  do complemento não tem o switch (e complemento não é vendido
  sozinho).
- O ícone de calendário na lista usa `title` nativo (shim de Tooltip
  no grid virtualizado): **hover não rende tooltip em screenshot**.
  Documentado por texto, sem imagem de tooltip.

## Decisões
- Exemplo de encomenda com **sobremesa** em vez de criar produto novo:
  a base do sandbox não tem bolo/torta e a regra é não montar cenário
  sem limpeza combinada.
- Três pudins (não quatro produtos) para o Brownie servir de contraste
  na mesma captura.
- Tira de 3 aparelhos (390×844, dsf 2) no padrão do #19/#20/#64/#70.
- Par painel → cardápio no padrão do #70/#71, com o recorte do painel
  incluindo o **PROCESSAR** para dar contexto.
- **Não** foi finalizado nenhum pedido de teste. O cashback de R$ 5,00
  do Teste Manual continua intacto.

## Estado deixado no sandbox
- Pudins Brigadeiro / Leite Condensado / Zero Açúcar: **Somente
  agendamento ON**
- Brownie: **OFF**
- Aba Agendamento: ON / ON / OFF, 2 e 7 dias, 60 / 60 / 90 / 60, 5
- Nenhum pedido finalizado; tabelas #68/#69 e descontos #64 intactos

## Status
Concluído — aguardando publicação.
