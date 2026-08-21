# MEMÓRIA — Manual #31 Cardápio: comida japonesa

> Memória detalhada deste manual: decisões, cenário montado, descobertas e estado do ambiente.
> **Último manual do bloco de cardápio (#27 a #31).**

Última atualização: 2026-08-20 (manual concluído, aguardando publicação do dono)

---

## 1. Escopo

Assunto novo: **combinado de preço fechado com contagem exata de peças**. Três configurações
combinadas, que nenhum manual anterior juntou:

| Exigência | Como se resolve |
|-----------|-----------------|
| As escolhas não podem mexer no preço | formação **Brinde** |
| O cliente escolhe exatamente a quantidade certa | **Mínimo = Máximo** no grupo |
| Ele pode querer duas porções do mesmo item | **Máximo da opção** maior que 1 |

O manual também traz, de propósito, um **produto simples** (temaki) ao lado do complexo, para
mostrar os dois extremos no mesmo cardápio.

**Fora do escopo:** rodízio (tela própria no menu Cardápio), peças com preços diferentes dentro
da montagem (só citado na FAQ).

---

## 2. A decisão de cadastro que faz o manual funcionar

**Cada opção é um bloco de 5 peças**, não uma peça.

Com mínimo e máximo 20, o atendente precisaria de vinte cliques por combinado — inviável no
balcão. Com blocos de 5, são **quatro cliques** e a conta fecha igual: 4 × 5 = 20 peças.

Essa escolha não é do produto, é de modelagem — e é o que transforma um cadastro teoricamente
possível em um cadastro utilizável. O manual explica o raciocínio, não só o passo a passo.

**A quantidade de peças não existe como campo no sistema.** Ela vive **no nome do complemento**
(`Hot Roll (5 peças)`), que aparece na opção, no PDV e no carrinho com o multiplicador
(`2x Hot Roll (5 peças)`). Daí a insistência do manual em colocar a quantidade no nome.

---

## 3. Cenário montado no sandbox

Base **limpa pelo dono** em 20/08/2026, confirmado pela API antes de começar.

| Item | Valor |
|------|-------|
| Setor | **Comida Japonesa** |
| Blocos de peças | Hot Roll · Uramaki Salmão · Niguiri Salmão · Sashimi Salmão — *(5 peças)* no nome, **R$ 0,00** |
| Extras | Shoyu extra R$ 2,00 · Wasabi extra R$ 2,00 |
| Adicionais do temaki | Cream cheese R$ 4,00 · Cebolinha R$ 2,00 |
| Grupos | **Escolha 4 opções de 5 peças** (Brinde + Obrigatório, **4/4**, cada opção máx **4**) · **Extras** (Normal, 0/3) · **Adicionais do temaki** (Normal, 0/3) |
| Produtos | **Combinado 20 peças** R$ 89,00 (montagem + Extras) e **Temaki Salmão** R$ 24,00 (Adicionais + Extras) |

**Contas conferidas no PDV:** combinado fecha em **R$ 89,00** com 2× Hot Roll + Uramaki +
Niguiri; sobe para **R$ 91,00** com o shoyu; temaki vai de R$ 24,00 para **R$ 28,00** com cream
cheese.

**Estado em que o ambiente ficou:** cenário completo, com um Combinado de R$ 91,00 no carrinho do
PDV (não finalizado).

### Fotos

10 imagens: 4 blocos de peças, 2 extras, 2 adicionais e 2 produtos.

---

## 4. Descoberta: com o grupo cheio, o clique é ignorado em silêncio

Testado com o grupo em **4/4**:

| Ação | Resultado |
|------|-----------|
| Clicar numa opção ainda em 0 | nada acontece |
| Clicar numa opção já escolhida, para repetir | nada acontece |
| Total | inalterado |
| Mensagem | **nenhuma** |

É o mesmo mecanismo do limite visto no #30, mas aqui o efeito é mais confuso: as opções mostram
**contador** (porque o máximo da opção é 4), então o operador vê um controle que parece
disponível e não responde. Para trocar uma escolha é preciso **diminuir no "−"** e então escolher
outra — o manual explica isso em destaque.

Somado ao fato, já conhecido do #29, de que **o botão "+" está `disabled` fixo no código**, o
contador do PDV fica com os dois botões pouco úteis: o "+" nunca funciona e o "−" é o único
caminho para corrigir. Vale reportar ao time como um conjunto.

---

## 5. Automação

A função `marcar_por_texto` (nascida da correção do #30) funcionou nas três marcações deste
manual — grupos com 4, 2 e 2 opções, mais os vínculos de grupo nos produtos. **Nenhuma opção
faltou**, ao contrário do que aconteceu no #30 com marcação por índice.

Outro ponto que se confirmou: **abrir o produto no PDV antes de capturar** é a verificação mais
rápida do cadastro. Aqui o PDV mostrou de primeira os quatro blocos, os dois extras e os
contadores no lugar das caixas de seleção — sinal de que o máximo da opção pegou.

Tempo de execução do cadastro completo (8 complementos com foto, 3 grupos com ajuste de máximo
por opção, 2 produtos com foto e vínculo): ~12 minutos.

---

## 6. Marcação das imagens

14 imagens, **31 setas** em 13 delas. Uma de contexto (`passthrough`): o cardápio com os dois
produtos.

A imagem **10** é a mais carregada do bloco inteiro, com quatro setas, porque precisa mostrar
quatro coisas ao mesmo tempo: o contador cheio, a opção repetida (`2`), a que ficou de fora (`0`)
e o total inalterado. São exatamente as quatro evidências da contagem exata com preço fechado.

**Detalhe da imagem 01:** a listagem de complementos sai em **ordem alfabética**, então na
primeira coluna a linha 1 é um extra (*Cebolinha*) e a linha 2 é um bloco de peças (*Sashimi*).
A numeração das setas segue a tela, e o texto do manual foi escrito nessa ordem — extra primeiro,
peça depois. Não inverter só para "ficar didático": o leitor confere pela tela.

Conferência automática (`annotate.py` × `.md`): **14 imagens, 0 divergência**.

---

## 7. Fechamento do bloco de cardápio

Com o #31, os cinco manuais cobrem as quatro formações de preço e os principais padrões de
montagem:

| Manual | Formações demonstradas | Padrão que ensina |
|--------|------------------------|-------------------|
| #27 fundamentos | Normal (+ tabela das quatro) | o fluxo completo e a edição em lote |
| #29 pizza | Valor da Maior, Proporcional | preço de sabor e meio a meio |
| #28 hambúrguer | Brinde, Normal | escolha que informa vs escolha que cobra |
| #30 açaí | Brinde com limite, Normal | inclusos + pagos, e tamanhos |
| #31 japonesa | Brinde com contagem exata, Normal | preço fechado com montagem |

**O que sobrou para manuais futuros:** Rodízio, importar do iFood, Exibir/Ocultar em massa,
Estoque e Ficha Técnica do produto, Cardápio Digital.

Todos os cinco terminam com a mesma **Dica extra** apontando para a Parte 8 do #27, como o dono
pediu.
