# Fluxo de código — Comida japonesa: contagem exata e preço fechado

> Mapeamento técnico do que o manual **#31 Cardápio — comida japonesa** documenta.
> Fonte: `beefood-web-react`, somente leitura. Levantado em 20/08/2026, versão
> **v3.200826.2046** em produção.
> O cadastro básico está em `manuais/cardapio-fundamentos/fluxo-codigo.md`; as fórmulas de preço
> em `manuais/cardapio-pizza/fluxo-codigo.md`; Brinde e Obrigatório em
> `manuais/cardapio-hamburguer/fluxo-codigo.md`; limite de grupo em
> `manuais/cardapio-acai/fluxo-codigo.md`. Aqui só o que é específico deste manual.

---

## 1. Contagem exata: `qtdMin` igual a `qtdMax`

Não há campo de "quantidade fixa". O que existe é o par **Mínimo / Máximo** do grupo, e igualar
os dois produz o efeito:

| Configuração | Comportamento |
|--------------|---------------|
| `qtdMin: 4`, `qtdMax: 4` | o cliente **precisa** escolher 4 e **não consegue** escolher 5 |
| `obrigatorio: true` | reforça o mínimo com a validação no clique (toast) |

O mínimo já bloqueia o envio por si (o grupo com `qtdMin > 0` exige seleção). Marcar
**Obrigatório** faz o selo vermelho aparecer no PDV e deixa a exigência visível para o operador.

---

## 2. Repetir a mesma opção depende do máximo DA OPÇÃO

Dois limites diferentes, que o manual precisa separar:

| Campo | Onde | Efeito |
|-------|------|--------|
| Máximo do **grupo** | aba Detalhes do Grupo | total de escolhas no grupo |
| Máximo da **opção** | linha da opção, expandida (`input[type=number]` índice 3) | quantas vezes **aquele** item pode ser repetido |

Com máximo da opção `1`, o PDV renderiza **caixa de seleção**; acima de 1, renderiza **contador
`− n +`** (`ModalCombo.tsx`, ~1489 a 1526). É o que permite `2x Hot Roll`.

**O botão "+" do contador está `disabled` fixo no código** (achado do #29): quem aumenta é o
clique na linha da opção; o "−" funciona.

---

## 3. Com o grupo cheio, o clique é ignorado sem aviso

Testado no sandbox com o grupo em 4/4:

| Ação | Resultado |
|------|-----------|
| Clicar numa opção ainda não escolhida | **nada acontece** — quantidade segue 0 |
| Clicar numa opção já escolhida (para repetir) | **nada acontece** — quantidade não sobe |
| Total no botão | inalterado |
| Mensagem | **nenhuma** |

`canSelectOption` compara o total selecionado com o `qtdMax` do grupo e o `increaseOption`
simplesmente não executa. Diferente do grupo **Obrigatório** pendente, que emite toast ao tentar
adicionar ao carrinho.

Para trocar uma escolha, é preciso **diminuir** no botão "−" e escolher outra. O manual avisa,
porque a ausência de retorno visual pode parecer defeito.

---

## 4. Preço fechado = Brinde no grupo de montagem

O preço do combinado fica no **produto** (`venda`), e o grupo de montagem usa **Brinde**
(`agregaValor: false`, opções com valor zero). Assim:

```
total = preço do produto + Σ (valor das opções × quantidade)
      = 89,00 + (0 × 2) + (0 × 1) + (0 × 1)
      = 89,00
```

Como visto no manual do hambúrguer, **o que garante o zero é o valor da opção**, não a formação.
Aqui os quatro complementos de peça foram cadastrados sem preço.

O grupo de **Extras** é `normal`, então soma normalmente: R$ 89,00 + R$ 2,00 = **R$ 91,00**.

---

## 5. Quantidade de peças não existe como campo

O sistema não tem "quantas peças esta opção representa". A informação vive **no nome do
complemento** (`Hot Roll (5 peças)`), que aparece:

- na listagem de complementos;
- na opção dentro do grupo;
- no modal do PDV;
- **no item do carrinho, com o multiplicador** (`2x Hot Roll (5 peças)`).

É por isso que o manual insiste em colocar a quantidade no nome: é o único lugar onde ela existe,
e é o que a cozinha lê.

---

## 6. Cenário conferido no PDV

**Combinado 20 peças**, R$ 89,00, dois grupos.

| Passo | Total no botão |
|-------|----------------|
| Modal aberto | R$ 89,00 |
| Hot Roll ×2 + Uramaki + Niguiri (4/4, grupo Brinde) | **R$ 89,00** |
| Clicar em Sashimi (5ª escolha) | **R$ 89,00** — ignorado |
| Clicar em Hot Roll de novo | **R$ 89,00** — ignorado |
| + Shoyu extra R$ 2,00 (grupo Normal) | **R$ 91,00** |

**Temaki Salmão**, R$ 24,00: com Cream cheese R$ 4,00 → **R$ 28,00**.

No carrinho, o combinado sai com `2x Hot Roll (5 peças)`, `1x Uramaki Salmão (5 peças)`,
`1x Niguiri Salmão (5 peças)` e `1x Shoyu extra`.

---

## 7. Grupo compartilhado entre produtos diferentes

O grupo **Extras** (shoyu e wasabi) foi vinculado ao **combinado** e ao **temaki** — produtos de
naturezas distintas. Nada no código restringe isso: o vínculo é por produto, e o grupo não sabe
que tipo de produto o usa.

Efeito colateral a considerar no cadastro: alterar o preço do shoyu vale para os dois. É o
comportamento desejado neste caso.

---

## 8. Rodízio é outra tela

O menu **Cardápio** tem um item **Rodízio** próprio, fora do escopo deste manual e dos outros
quatro do bloco. Não se resolve com grupo de opções.

---

## 9. Endpoints

Os mesmos do manual de fundamentos. Nada específico deste manual. Ver
`manuais/cardapio-fundamentos/fluxo-codigo.md`, seção 7.
