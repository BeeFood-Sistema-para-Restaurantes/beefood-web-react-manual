# Estudo — manual "Vínculo Marketplace"

> Estudo pedido pelo dono em **02/09/2026** ("estude vínculo marketplace e crie um plano"),
> antes de produzir o manual.
> Responde à pergunta: *"há informação e ambiente suficientes para escrever o manual?"*
>
> **Resposta curta: sim.** O recurso está inteiro em produção (conferido no bundle
> `index-BkZot3Tx.js`), e o sandbox **BeeFood3 - Manual** já tem tudo o que o manual precisa
> fotografar: **786 vínculos** (69 feitos, 717 pendentes) e **22 vendas de marketplace**, entre
> elas uma com produto pendente e uma com opção pendente. Apareceram **sete achados** fora do
> pedido; dois deles são candidatos a correção de produto, não de manual.

Status: ✅ **aprovado e executado** em 02/09/2026 — manual em `manuais/vinculo-marketplace/`.
As respostas do dono estão na seção 15.

---

## 1. Resumo em cinco linhas

Quando um pedido entra por marketplace (iFood, Aiqfome, 99Food, Keeta, Rappi, Uai Rango,
Delivery Much), o item chega com **o nome que está no cardápio do marketplace**, não com o
produto do BeeFood. O **Vínculo Marketplace** é a tela onde se diz, uma única vez, que
"Refrigerante Pepsi 350 Ml" (nome de lá) é o "Coca Cola 350ml" (produto de cá). Feito o
vínculo, o item passa a ter setor, impressora, ficha técnica e código — e a venda deixa de
travar a nota fiscal. Sem vínculo, o pedido entra e é entregue normalmente, mas o item fica
"solto": aparece um aviso na venda, a nota fiscal não sai, e a via da cozinha depende de uma
impressora de emergência.

---

## 2. O que é o vínculo — e o que ele não é

| É | Não é |
|---|-------|
| Uma tradução **nome do marketplace → produto (ou opção) do BeeFood** | Não é sincronização de cardápio: não cria, não altera e não publica nada no marketplace |
| Feito **uma vez por nome**: o próximo pedido com aquele nome já entra vinculado | Não é por pedido — o modo "por venda" só é o atalho para resolver um pedido específico |
| **N para 1**: vários nomes de marketplace podem apontar para o mesmo produto (provado no sandbox) | Não é 1 para 1, e não existe validação de duplicidade |
| Um cadastro **por filial** (o `filialID` viaja em toda operação) | Não é global da empresa |

Não confundir com **Copiar do iFood** (importar o cardápio do iFood para dentro do BeeFood),
que é outra função, liberada pelo switch **Gerente** do cadastro do usuário — o #75 já tratou
dela na seção 7.1.

---

## 3. Os quatro caminhos até o vínculo

O manual precisa mostrar todos, porque cada um aparece num momento diferente do dia:

| # | Onde | Como se chega | Para que serve |
|---|------|---------------|----------------|
| 1 | **Delivery** (a lista inteira) | `/delivery` → botão **⋮** do topo → **Vínculo Marketplace** | Trabalho de mesa: vincular em lote, ver quanto falta |
| 2 | **Dentro da venda** | Abrir o pedido → botão **^** (ao lado de PAGAMENTO) → **Vínculo Marketplace** | Resolver só os itens daquele pedido; aparece somente em venda de marketplace |
| 3 | **Aviso no item da venda** | Abrir o pedido → faixa **"Produto não associado no pedido - sem vínculo marketplace"** no produto | Atalho de um clique: já abre a seleção com o item preenchido |
| 4 | **Bloqueio da nota fiscal** | Emitir NFC-e numa venda com produto pendente → modal **"Produtos sem vínculo marketplace"** | Não deixa emitir; obriga a vincular e emite pelo **EMITIR FISCAL (F2)** |

Os caminhos 1 e 2 existem também no celular (`MobileDeliveryPage`), no mesmo modal.

---

## 4. O modal em modo listagem (caminho 1)

Cabeçalho **Vínculo Marketplace**, tabela paginada e dois contadores no topo direito
(verde = vinculados, vermelho = pendentes).

| Coluna | O que traz |
|--------|-----------|
| **Status** | `Vinculado` (verde) ou `Pendente` (vermelho) |
| **Tipo** | `Produto` (azul) ou `Grupo Opção` (roxo) — decide o que pode ser escolhido no vínculo |
| **Descrição Marketplace** | O nome exatamente como o marketplace mandou |
| **Vínculo** | O produto do BeeFood, ou `Sem vínculo` |
| **Setor** | Vem do produto vinculado. **Fica `-` enquanto não há vínculo** — é a evidência de que o roteamento da cozinha depende do vínculo |

Filtros: busca por descrição (procura no nome do marketplace, no nome vinculado e no setor),
seletor **Todos / Vinculados / Pendentes**, botão de recarregar e **Itens por página**
(15/30/50/100). A linha pendente sai com fundo âmbar.

Marcando qualquer caixa, o rodapé abre o painel de ações em lote.

---

## 5. O modal em modo venda (caminho 2)

Mesmo modal com o título **Vínculo Marketplace - Pedido #871** e duas diferenças que valem
uma seção do manual:

- A coluna **Setor** dá lugar a **Nível**: `1º` é o produto e `2º` é a opção dentro dele. É
  assim que se enxerga que o combo veio vinculado mas os complementos não.
- O painel de ações em lote só mostra **Vincular**. **Criar produto e vincular** e **Excluir**
  não aparecem aqui.

---

## 6. As três ações — e a regra de tipo

| Ação | O que faz | Confirmação |
|------|-----------|-------------|
| **Vincular** | Abre **Selecionar Vínculo**, você escolhe **um** item do cardápio e todos os selecionados passam a apontar para ele | Não tem diálogo: o `Confirmar Vínculo` já grava |
| **Criar produto e vincular** | Cria um produto novo **com o nome que veio do marketplace** e já vincula | Diálogo `Sim, criar (ENTER)` |
| **Excluir** | Apaga a linha do vínculo (a tradução), não o produto do cardápio | Diálogo `Sim, excluir (ENTER)`, com o aviso de que não há como desfazer |

**A regra de tipo é a parte que o usuário erra.** No modal **Selecionar Vínculo**:

- se **algum** item selecionado for do tipo **Produto**, a lista mostra **só produtos**;
- se **todos** forem **Grupo Opção**, a lista mostra **produtos e opções de grupo**.

A lista vem agrupada por **setor** (acordeão aberto), com filtro de setor, preço embaixo de
cada item e uma busca que captura qualquer tecla digitada dentro do modal — inclusive fora do
campo. Detalhe prático: **o cardápio do sandbox tem 21 nomes repetidos** (existem dois
"Batata frita", dois "One Burger"), então o manual precisa ensinar a distinguir pelo **setor e
pelo preço**, senão o vínculo vai para o produto errado.

---

## 7. O que acontece quando ninguém vincula

| Consequência | Situação | Prova |
|--------------|----------|-------|
| **A nota fiscal não sai** | ✅ Provado no código, nos dois caminhos de emissão | `VendaDetalhes` e `useModalPagamentosLogic` filtram `produtoID === null` antes de emitir e abrem o modal de bloqueio |
| **Só produto bloqueia; opção não** | ✅ Provado | O filtro olha os produtos da venda. Na venda 871, as **4 opções pendentes** não geram aviso nem bloqueio |
| **A via da cozinha depende de uma impressora de emergência** | ✅ Provado no código | Impressão → Cozinha tem o card **Local de Impressão padrão para Marketplace** com os modos *Imprimir todos* e *somente o que não conseguir imprimir*, criado porque "esses itens não imprimiriam" nos modos por setor e por produto |
| **O item não tem setor** | ✅ Provado no dado | Nas 717 linhas pendentes o `setorProduto` é nulo; nas 69 vinculadas ele vem preenchido |
| **Sem baixa de estoque e sem custo (ficha técnica)** | 🔜 A confirmar na execução | O item sem `produtoID` não é produto do cadastro, logo não tem ficha; falta comprovar em venda real, como o #72 fez |
| **Relatório de produtos não conta o item** | 🔜 A confirmar na execução | Mesma lógica; medir em Desempenho antes de afirmar |

---

## 8. Estado do sandbox — dá para produzir o manual?

Levantamento de **02/09/2026** na conta **BeeFood3 - Manual** (empresa 38311, filial 39202),
lido pela API autenticada com a técnica do #74. **Nada foi alterado: só leitura** (o único POST
foi a consulta do histórico de vendas, que é uma busca).

### 8.1 A lista de vínculos

| Medida | Valor |
|--------|------:|
| Linhas em `vinculoMarketplace` | **786** |
| Vinculadas | **69** |
| Pendentes | **717** |
| Tipo `Produto` | 525 |
| Tipo `Grupo Opção` | 261 |
| Todas na filial 39202 | sim |

Os 69 vínculos existentes são **todos produto → produto**; **nenhum** aponta para opção de
grupo. Ou seja: o caminho "vincular uma opção" nunca foi usado nessa base e vai ser
fotografado pela primeira vez no manual.

### 8.2 Os itens disponíveis para vincular

351 linhas: **7 setores, 67 produtos, 64 grupos e 213 opções de grupo**. Distribuição dos
produtos: Burgers Avulsos 18, Molhos adicionais 17, Bebidas 11, Combos 9, Acompanhamentos 6,
Sobremesas 4, Milk Shakes 2.

### 8.3 As vendas de marketplace

De **936 vendas** de 2026, a origem é: Manual 676, Cardápio Digital 206, Totem 32,
**AIQFome 21** e **iFood 1**. As 22 de marketplace se distribuem assim:

| Grupo | Quantas | Serve para |
|-------|--------:|-----------|
| Canceladas (o modal devolve lista vazia) | 5 | Nota de rodapé |
| Com **1 produto pendente** | 11 | O aviso na venda e o bloqueio fiscal |
| Com produto vinculado | 5 | O "depois" |
| **Venda 871 (iFood)** — 2 produtos vinculados + 4 opções pendentes | 1 | A imagem-chave do modo venda |

**As duas vendas de exemplo já estão prontas:**

- **Venda 865** (AIQFome, 27/08, R$ 36,03): o item `sorvete 1 medio` está com `produtoID` nulo
  e a faixa **"Produto não associado no pedido - sem vínculo marketplace"** aparece na tela.
- **Venda 871** (iFood, pedido de teste de integração, 28/08): `PRODUTO 1` e `PRODUTO 2 (COMBO)`
  já vinculados a *Batata frita* e *Molho Cheddar*, e `Complemento 1` a `Complemento 4`
  pendentes no nível 2º.

---

## 9. Sete achados fora do pedido

1. **A lista tem linhas repetidas e indistinguíveis.** São 403 nomes distintos em 786 linhas:
   **196 nomes aparecem mais de uma vez** (579 linhas em duplicidade), e há nome com **6
   linhas** — "Ovo Perdomo Pistache", por exemplo, ocupa seis linhas idênticas na tela.
2. **A tela não diz de qual marketplace veio a linha.** A rota de listagem não devolve nenhum
   campo de marketplace; a rota por venda devolve todos (`ifoodShortReference`, `aiqfomeId`,
   `rappiOrderID`, `uaiRangoID`, `muchDeliveryCode`, `uberEatsDisplayId`,
   `americanasOrderID`). Junto com o achado 1, é a maior dificuldade do usuário: ele não tem
   como saber qual das seis linhas iguais é a do iFood.
3. **A mesma descrição existe nos dois tipos.** "Batata frita" aparece como `Produto` e como
   `Grupo Opção` na mesma lista — e a coluna **Tipo** é a única pista de qual usar.
4. **"Criar produto e vincular" duplica cardápio com facilidade.** Entre os pendentes,
   **59 produtos e 122 opções já têm nome idêntico** a algo que existe no cardápio. Se o
   usuário selecionar tudo e mandar criar, ganha 181 duplicatas. O manual tem de inverter a
   ordem: **procurar primeiro, criar só o que realmente não existe**.
5. **Opção pendente é silenciosa.** Nenhum aviso na venda, nenhum bloqueio fiscal — some no
   relatório e cai na impressora de emergência sem ninguém perceber. É o principal motivo
   para o manual existir.
6. **O vínculo gravado na venda sobrevive à limpeza da base.** As vendas 619 e 629–632 apontam
   para o `produtoID 2252703`, que **não está mais** entre os 67 produtos do cardápio atual. A
   venda antiga guarda o vínculo de quando foi feita.
7. **Pode existir permissão por marketplace que o #75 não catalogou.** O Delivery tem o
   diálogo *"Aplicativo sem permissão — acesse Configurações → Grupos de Acesso → Aplicativos
   e habilite este marketplace"*, que impede até abrir o pedido, enquanto o #75 concluiu que
   "todas as integrações da tela de Aplicativos" não têm permissão própria. Vale reconferir
   antes de publicar — pode virar correção do #75.

---

## 10. Rotas usadas (base do futuro `fluxo-codigo.md`)

Base em produção: `https://app3.beetechapi.be`.

| Método | Rota | Para que |
|--------|------|----------|
| GET | `/api/venda2/vinculoMarketplace/{empresaID}/{usuarioID}` | Lista completa (modo listagem) |
| GET | `/api/venda2/vinculoMarketplace/{empresaID}/{usuarioID}?numeroPreVenda=N` | Itens de uma venda (modo venda) |
| GET | `/api/venda2/vinculoMarketplace/vincular/{empresaID}/{filialID}/{usuarioID}` | Itens do cardápio disponíveis (setor / produto / grupo / opção) |
| POST | `/api/venda2/vinculoMarketplace/vincular` | Grava o vínculo (lote) |
| POST | `/api/venda2/vinculoMarketplace/criarProdutoVincular` | Cria o produto e vincula (lote) |
| DELETE | `/api/venda2/vinculoMarketplace` | Apaga vínculos (lote) |

Arquivos do front: `src/components/ModalVinculoMarketplace.tsx`,
`src/components/ModalSelecionarVinculoProduto.tsx`,
`src/components/fiscal/ModalVinculoPendenteFiscal.tsx`,
`src/hooks/useVinculoMarketplace.ts`, `src/hooks/useVinculoMarketplaceVincular.ts`; pontos de
entrada em `src/pages/Delivery.tsx`, `src/components/VendaDetalhes.tsx`,
`src/hooks/useModalPagamentosLogic.ts` e `src/components/mobile/delivery/MobileDeliveryPage.tsx`.

---

## 11. Riscos da captura em produção

O estudo foi todo em leitura, mas o **manual** precisa gravar. Três cuidados:

1. **`Vincular` não tem diálogo de confirmação.** O `Confirmar Vínculo` grava na hora. Escolher
   um item de teste combinado com o dono antes de clicar.
2. **`Excluir` é declaradamente irreversível.** Só apagar um vínculo que o próprio manual tenha
   criado, e na ordem: criar → fotografar → apagar.
3. **`Criar produto e vincular` mexe no cardápio.** Cria produto de verdade. Fotografar com
   **um** item selecionado e combinar se o produto criado fica ou é apagado depois.

Para o caminho 4 (bloqueio fiscal) é preciso uma venda de marketplace **paga e não emitida** —
nenhuma das 22 está nesse estado hoje (a 865 está *Não pago*). Duas saídas: registrar o
pagamento de uma delas com autorização do dono, ou lançar um pedido de marketplace novo. Isso
precisa de decisão antes da produção.

---

## 12. Proposta do manual (#78)

Pasta `manuais/vinculo-marketplace/`, **8 seções** e **10 a 12 imagens** — mesmo porte do #75.

| Seção | Conteúdo | Imagens |
|-------|----------|--------:|
| 1 | O que é o vínculo, com o antes/depois do mesmo item | 1 |
| 2 | Abrir a tela pelo Delivery: colunas, contadores, filtro Pendentes | 2 |
| 3 | Vincular um item: selecionar → **Selecionar Vínculo** → confirmar, e a leitura do resultado | 3 |
| 4 | Vincular **em lote** (vários nomes para o mesmo produto) e a regra de tipo Produto × Grupo Opção | 2 |
| 5 | **Criar produto e vincular** — quando usar e por que procurar antes (o achado 4) | 1 |
| 6 | Resolver **pelo pedido**: o aviso no item, o modo venda e a coluna Nível | 2 |
| 7 | O **bloqueio da nota fiscal** e o EMITIR FISCAL (F2) | 1 |
| 8 | Excluir vínculo, o que não vincular quebra (cozinha e fiscal) e as perguntas frequentes | — |

Duas decisões de escopo que sugiro **fora** deste manual, para não engordá-lo: a configuração
do **Local de Impressão padrão para Marketplace** (é da tela de Impressão, rende um manual do
bloco *Impressão*, já no backlog) e a ativação de cada marketplace (já são os manuais #6, #59
a #63).

---

## 13. Roteiro de captura

Vale a regra permanente da `MEMORIA-GERAL.md` (esperar o spinner sumir + 5 s). Três notas
específicas medidas neste estudo:

- **A venda demora a montar.** O aviso "Produto não associado" só entra no DOM cerca de
  **12 s** depois de abrir `/pedido=<preVendaID>`; com 5 s a captura sai sem a faixa. Foi o que
  aconteceu nas duas primeiras tentativas deste estudo.
- **O ⋮ do topo do Delivery não é o ⋮ do card.** O do card abre *Alterar Situação*. O correto é
  `button.h-10.w-10:has(svg.lucide-ellipsis-vertical)`. Dentro da venda, o menu é o
  **^** do rodapé (`svg.lucide-chevron-up`), não um ⋮.
- **Deep link direto para a venda:** `https://beefood.app/pedido=<preVendaID>` (865 = 57938276,
  871 = 58014871). Poupa navegar pelo Histórico.

---

## 14. Perguntas em aberto (para o dono)

1. **De onde vêm as 786 linhas** e por que o mesmo nome repete até 6 vezes? Uma linha por
   marketplace, por importação, ou por item do cardápio de lá? A resposta muda o texto da
   seção 2 do manual.
2. **Dá para mostrar de qual marketplace é cada linha?** Se não dá hoje, o manual precisa
   ensinar a conviver com isso (usar o modo venda, que identifica o pedido).
3. **O manual pode gravar vínculo, criar produto e excluir vínculo no sandbox?** E o produto
   criado na seção 5 fica ou é apagado depois?
4. **Autoriza registrar pagamento numa venda de marketplace** (ou lançar um pedido novo) para
   fotografar o bloqueio fiscal?
5. **Confirma o achado 7** (permissão por marketplace)? Se existir, o #75 precisa de correção.

---

## 15. Respostas do dono (02/09/2026) e o que mudou no manual

| # | Resposta | Efeito no manual |
|---|----------|------------------|
| 1 | **Duplicidade de base de testes — evite mostrar** | Nenhuma seção fala de linhas repetidas. Todos os exemplos foram escolhidos com **nome único na busca**, para as capturas não exibirem linhas iguais. A única menção é uma pergunta frequente que orienta a marcar todas as linhas pendentes do mesmo nome e vincular de uma vez |
| 2 | **Não dá para saber de qual marketplace é a linha — não focar no assunto** | Assunto fora do texto. O manual trata a lista como uma lista de nomes; quando o operador precisa saber de qual pedido veio, o caminho ensinado é o **modo venda** |
| 3 | **Pode vincular, criar produto e excluir à vontade** | Cinco vínculos criados ao vivo e o produto **Salada Caesar** criado e mantido. O diálogo de exclusão foi fotografado e cancelado (nenhum vínculo foi apagado) |
| 4 | **Pode gerar venda de marketplace e pagar** | Não foi preciso fabricar venda: a **769** já estava recebida e serviu para fotografar o bloqueio fiscal. A tentativa na **865** revelou que *marcar como pago* na linha do pagamento **não** alimenta o `valorPago` — registrado no `fluxo-codigo.md` |
| 5 | **A permissão por marketplace não existe** | O achado 7 fica registrado como hipótese descartada. O **#75 não precisa de correção** |

### O que o manual acrescentou ao estudo

Duas descobertas só apareceram na execução, e as duas viraram destaque no texto:

- **O produto do "Criar produto e vincular" nasce cru**: sem preço, num setor novo chamado
  **Vínculo Marketplace**, e já **ativo** em delivery e presencial.
- **Vincular por dentro do pedido também alimenta a lista geral** (testado com o
  *Complemento 1 - Segundo Nível* do pedido 871), o que responde se o trabalho feito no pedido
  vale para os próximos.
