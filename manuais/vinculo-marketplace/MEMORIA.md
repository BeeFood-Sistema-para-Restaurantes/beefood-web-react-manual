# MEMÓRIA — Vínculo Marketplace (#79)

Manual **de operação**: ensina a traduzir o nome que o marketplace manda para o produto do
cardápio. Estudo que o originou:
[`PLANO-VINCULO-MARKETPLACE.md`](../../PLANO-VINCULO-MARKETPLACE.md).

Estado: ✅ **Concluído** em 02/09/2026. 14 imagens, 39 setas + 2 molduras.

---

    10|## 1. O que o manual afirma, e com que prova

| Afirmação | Prova |
|-----------|-------|
| O vínculo é por **nome do marketplace**, e vale para os próximos pedidos | 69 vínculos já existiam na base antes do manual; os 5 criados aqui funcionaram na primeira tentativa |
| Vários nomes podem apontar para **um** produto | Feito ao vivo: *Sachê Maionese* + *Sachê Maionese Temperada* → **Maionese Grill (Defumada/Tasty)** |
| Item **Grupo Opção** pode ir para produto **ou** opção; item **Produto**, só para produto | Regra no código (`tiposPermitidos`) e vista na tela: com a opção selecionada aparecem os dois chips *Produtos* e *Opções de Grupo* |
| **Criar produto e vincular** cria produto **sem preço**, no setor **Vínculo Marketplace** | Criado o `Salada Caesar`: `venda: null`, setor novo `Vínculo Marketplace`, ativo em delivery e presencial |
| Produto sem vínculo **trava a NFC-e** | Modal *Produtos sem vínculo marketplace* fotografada na venda **769**, com **EMITIR FISCAL (F2)** desabilitado |
| **Opção** pendente não trava nada e não avisa | Venda **871**: 4 opções pendentes, nenhuma faixa na tela do pedido e nenhum bloqueio |
| O setor vem do produto vinculado | Nas 717 linhas pendentes o setor é vazio; depois do vínculo apareceu *Sobremesas* / *Molhos adicionais* |
    20|| Vincular por dentro do pedido também alimenta a lista | Testado com *Complemento 1 - Segundo Nível* (ver seção 3) |

Detalhe técnico, rotas e medições em `fluxo-codigo.md`.

---

## 2. Cenário montado no sandbox (02/09/2026)

A base **não** foi limpa para este manual: a lista de vínculos é histórica e não dá para
reconstruí-la. O que se fez foi escolher itens pendentes cujo nome fosse **único na busca**, para
    30|as capturas não exibirem a duplicidade da base de testes (decisão do dono: *"duplicidade de base
de testes, evite mostrar"*).

| Seção | Item do marketplace | Destino | Por que esse |
|-------|--------------------|---------|--------------|
| Vincular um item | **Pudim - Tradicional** | produto **Pudim - Leite Condensado** (R$ 19,90, Sobremesas) | Nome único na busca dos dois lados; na janela de escolha aparecem só os 3 pudins do setor Sobremesas, sem repetição |
| Lote | **Sachê Maionese** + **Sachê Maionese Temperada** | produto **Maionese Grill (Defumada/Tasty)** | A busca por *Sachê Maionese* devolve exatamente essas duas linhas, e o produto de destino tem nome único no cardápio |
| Opção | **Adicionar queijo cheddar** | opção **Fatia de queijo cheddar** (grupo Adicionais) | Único item *Adicionar…* que tem correspondente óbvio; mostra o agrupamento setor → grupo (produto) |
| Criar produto | **Salada Caesar** | produto novo | O cardápio (hamburgueria) não tem salada nenhuma — é o caso legítimo de criar |
| Aviso no pedido | venda **865** (AIQFome) | — | Produto `sorvete 1 medio` sem vínculo desde 27/08 |
| Modo venda | venda **871** (iFood) | — | Pedido de teste da integração: 2 produtos vinculados + 4 opções pendentes |
    40|| Bloqueio fiscal | venda **769** (AIQFome) | — | A única faixa de vendas pendentes que já estava **recebida** (`valorPago = valorTotal`), o que é pré-requisito da emissão |

**Evite nomes duplicados nos dois lados.** A primeira tentativa foi *Molhão Cheddar* → *Molho
Cheddar*, e a janela de escolha mostrou **dois** "Molho Cheddar" idênticos (R$ 4,90 cada) —
imagem ruim para manual. Trocar para o pudim resolveu. O cardápio do sandbox tem **21 nomes de
produto repetidos**; vale sempre rodar um ensaio (`DRY=1`) e ler o que a janela devolve antes de
capturar.

---

## 3. O teste que virou frase no manual

   50|Pergunta: vincular por dentro do pedido resolve só aquele pedido, ou também ensina o sistema?

Medido em três passos, com o item *Complemento 1 - Segundo Nível* (pedido 871):

1. **Antes**, na lista geral: `Pendente | Grupo Opção | Sem vínculo | -`
2. Vinculado **por dentro do pedido** (modo venda) a *Batata frita com cheddar e bacon*
3. **Depois**, na lista geral: `Vinculado | Grupo Opção | Batata frita com cheddar e bacon | Acompanhamentos`

Ou seja: o vínculo feito no pedido **vale para os próximos**. Ficou como quadro na seção
*Resolver pelo próprio pedido*.

    60|> Esse vínculo de teste ficou no ambiente e o destino escolhido é sem sentido comercial
> (o script pegou o primeiro resultado da busca por "Bacon"). É item de **pedido de teste do
> iFood**, então não afeta operação — mas pode ser apagado à vontade.

---

## 4. Armadilhas de captura

- **O `⋮` do topo do Delivery não é o `⋮` do card do pedido.** O do card abre *Alterar Situação*.
  O certo é `button.h-10.w-10:has(svg.lucide-ellipsis-vertical)`.
- **Dentro do pedido o menu é o `^`** (`svg.lucide-chevron-up`), no rodapé ao lado de PAGAMENTO —
    70|  não existe `⋮` ali.
- **A venda demora ~12 s para montar.** A faixa *Produto não associado* só entra no DOM depois
  disso; com os 5 s de praxe a captura sai sem ela (aconteceu duas vezes). Para essa tela, espere
  **14 s** e role até o elemento (`scroll_into_view_if_needed`).
- **Deep link do pedido:** `https://beefood.app/pedido=<preVendaID>` (865 = 57938276,
  871 = 58014871, 769 = 56112787). Poupa navegar pelo Histórico.
- **O diálogo de confirmação não é filho do modal.** `[role="dialog"]` filtrado pelo texto
  *Criar produto e vincular* casa com o modal de trás; clicar no `Sim, criar` exige
  `page.locator("button:has-text('Sim, criar')")` na página, não dentro do modal.
- **A janela Selecionar Vínculo captura qualquer tecla** e joga na busca. `fill()` no input
    80|  funciona; digitar com `keyboard.type` fora do campo também cai na busca.
- **Ensaiar antes de gravar.** Os scripts de captura ganharam um `DRY=1` que faz tudo menos o
  `Confirmar Vínculo`. Foi o que evitou gravar o vínculo errado no caso do *Molho Cheddar*.

### Dado pessoal coberto na imagem PURA

O repositório é público. Nas capturas de venda (imagens 12 e 14) o cliente é real, então o borrão
foi aplicado **no navegador, antes do screenshot** (`filter: blur(7px)` via `page.evaluate` nos
elementos que casam com nome/telefone/CEP) — a pura já nasce sem dado legível. A captura
intermediária que mostrava o cliente sem borrão foi **apagada antes do commit**.

    90|---

## 5. Decisões do dono (02/09/2026)

| Pergunta do estudo | Decisão |
|--------------------|---------|
| De onde vêm as 786 linhas e por que repetem | **Duplicidade da base de testes** — não mostrar, não explicar no manual |
| Mostrar de qual marketplace é cada linha | **Não dá para saber** — não tocar no assunto |
| Pode vincular / criar produto / excluir no sandbox | **Pode, à vontade** — o produto criado fica |
| Registrar pagamento para fotografar o bloqueio fiscal | **Autorizado** |
| Existe permissão por marketplace (achado 7 do estudo) | **Não existe** — o #75 continua correto, nada a corrigir |
   100|
Reflexos no texto: nenhuma seção fala de linhas repetidas ou de "de qual marketplace veio"; a
única menção é uma pergunta frequente que orienta a vincular todas as linhas pendentes do mesmo
nome de uma vez.

---

## 6. Imagens

| Arquivo | Setas | Onde entra |
|---------|------:|------------|
   110|| `01-delivery-menu.png` | 2 | Onde fica a tela |
| `02-listagem.png` | 5 | Entendendo a tela |
| `03-selecionar-item.png` | 3 | Vincular um item |
| `04-selecionar-vinculo.png` | 4 | Vincular um item (janela de escolha) |
| `05-vinculado.png` | 4 | Vincular um item (resultado) |
| `06-lote-selecao.png` | 3 | Vários nomes no mesmo produto |
| `07-lote-resultado.png` | 1 + moldura | Vários nomes no mesmo produto (resultado) |
| `08-opcao-selecionar.png` | 3 | Vincular uma opção |
| `09-criar-produto.png` | 2 | Criar produto e vincular |
| `10-cardapio-produto-criado.png` | 3 | Criar produto e vincular (o produto no Cardápio) |
   120|| `11-excluir-dialogo.png` | 2 | Excluir um vínculo |
| `12-venda-aviso.png` | 2 | Resolver pelo próprio pedido |
| `13-modo-venda.png` | 3 + moldura | Resolver pelo próprio pedido (modo venda) |
| `14-bloqueio-fiscal.png` | 2 | O bloqueio da nota fiscal |

O `annotate.py` recebe as coordenadas em frações da **imagem inteira** e converte para o recorte
sozinho (`converter()`). Isso importa porque quase toda tela do manual é o mesmo modal
centralizado: medir uma vez na captura cheia serve para todos os recortes. Recortes padrão:
`MODAL` (o modal do Vínculo Marketplace) e `SELECIONAR` (a janela Selecionar Vínculo, que é menor
e fica por cima).
   130|
---

## 7. Estado do ambiente ao terminar

Cinco vínculos novos, um produto novo e um setor novo:

| O que | Detalhe |
|-------|---------|
| Vínculos criados | *Pudim - Tradicional* → Pudim - Leite Condensado; *Sachê Maionese* e *Sachê Maionese Temperada* → Maionese Grill (Defumada/Tasty); *Adicionar queijo cheddar* → Fatia de queijo cheddar; *Complemento 1 - Segundo Nível* → Batata frita com cheddar e bacon (teste) |
| Produto criado | **Salada Caesar** (`produtoID 2540502`), sem preço, no setor **Vínculo Marketplace** — o dono autorizou deixar |
   140|| Contadores | Saíram de **69 / 717** para **75 / 711** (as capturas do manual param em 74 / 712; o 75º é o vínculo de teste do *Complemento 1*) |
| Venda 865 | Ficou com o pagamento **marcado como pago** (Dinheiro R$ 36,03). O `valorPago` da venda continua 0, ou seja, ela **não** foi recebida no caixa; o botão *Marcar como não pago* não reverteu |
| Nenhuma nota fiscal foi emitida | O bloqueio foi fotografado e fechado com **FECHAR (ESC)**; o **EMITIR FISCAL** nunca foi clicado |
