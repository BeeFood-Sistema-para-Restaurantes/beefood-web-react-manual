# Ativar integração Uai Rango

Ligue a loja do **Uai Rango** ao BeeFood: os pedidos do marketplace entram no
Delivery e cada forma de pagamento chega associada a uma forma do sistema.

O processo tem três partes:

1. Gerar o **Token de Acesso** no painel do Uai Rango
2. Colar o token em **Aplicativos → UaiRango** no BeeFood
3. Associar as **formas de recebimento**

> Nas telas do BeeFood, as **setas verdes** mostram onde clicar.
> O print do Uai Rango já vem com os passos numerados do painel deles.

---

## Antes de começar

1. Loja ativa no **Uai Rango**, com login no gestor
   (`uairango.com/estabelecimento/estabelecimento`).
2. Acesso a **Aplicativos** no BeeFood.
3. Formas de recebimento já cadastradas no BeeFood (Dinheiro, Crédito, Débito,
   e a forma que você usa para pagamento online). Se faltar alguma, cadastre em
   **Cadastro → Formas Recebimento** antes de associar.

---

## Parte 1 — Uai Rango: gerar o Token de Acesso

### Passo 1. Abrir o estabelecimento e copiar o token

No gestor do Uai Rango:

1. Acesse `uairango.com/estabelecimento/estabelecimento`.
2. Clique em **Estabelecimento** no menu central.
3. Abra a aba **Integração**.
4. Marque **Sim** em *Deseja habilitar a API de integração com outros sistemas?*
5. Copie o **Token de acesso** gerado.

![Painel Uai Rango — token de acesso](imagens-tratadas/01-uairango-painel-token.png)

Guarde o token — ele entra no BeeFood no passo seguinte. Não publique o valor
inteiro em grupo ou rede social.

---

## Parte 2 — BeeFood: colar o token

### Passo 2. Abrir Aplicativos → UaiRango

No BeeFood, clique em **Aplicativos** (1) no menu. Na busca, digite **UaiRango**
(ou role até a seção **Delivery**) e abra o card **UaiRango** (2).

![BeeFood → Aplicativos → UaiRango](imagens-tratadas/02-beefood-aplicativos.png)

| Nº | O que fazer |
|----|-------------|
| 1. | Menu **Aplicativos**. |
| 2. | Card **UaiRango** (*Marketplace*). |

### Passo 3. Novo Cardápio

Na aba **Credenciais**, clique em **+ Novo Cardápio** (1).

Se ainda não houver token, a tela mostra *Nenhuma credencial configurada* — é
normal.

![Modal UaiRango — Credenciais](imagens-tratadas/03-beefood-modal-credenciais.png)

| Nº | O que fazer |
|----|-------------|
| 1. | **+ Novo Cardápio** — abre o formulário do token. |
| 2. | Aviso: depois de salvar, fale com o **Suporte BeeFood** para ativar a integração. |

### Passo 4. Colar o token e salvar

Na janela **Nova Credencial UaiRango**:

![Nova credencial — Token e cardápio](imagens-tratadas/04-beefood-modal-token.png)

| Nº | Campo | O que fazer |
|----|-------|-------------|
| 1. | **Token** \* | Cole o Token de acesso copiado no Uai Rango. |
| 2. | **Cardápio de Origem** | Selecione o cardápio BeeFood que recebe os pedidos. Na loja única, deixe o cardápio principal. |
| 3. | **SALVAR (F2)** | Grava a credencial. |

Depois de salvar, o cadastro aparece na lista com o status **Aguardando
comunicação**. Quando o Uai Rango confirmar, o status passa a **Ativo** e o
token **não pode mais ser alterado**.

A sincronização pode levar **até 1 hora** depois de o token entrar no BeeFood.
Enquanto isso, fale com o **suporte** (aviso da seta 2 da imagem do Passo 3)
para liberar a integração.

---

## Parte 3 — Formas de recebimento

### Passo 5. Associar cada forma do Uai Rango

Ainda no modal **UaiRango**, abra a aba **Formas Recebimento** (1). Para cada
linha da esquerda, escolha na direita a forma equivalente do BeeFood (2).

A associação grava sozinha, no momento em que você escolhe a forma.

![Formas de recebimento Uai Rango](imagens-tratadas/05-beefood-formas-recebimento.png)

| Nº | O que fazer |
|----|-------------|
| 1. | Aba **Formas Recebimento**. |
| 2. | **Forma do Sistema** — uma para cada linha do Uai Rango. |

Combine o tipo certo:

| Forma UaiRango | Forma do Sistema (exemplo) |
|----------------|----------------------------|
| Pago Online | a forma de pagamento **online** da loja |
| Dinheiro | **Dinheiro** |
| Mastercard Crédito / Visa Crédito | **Crédito** |
| Mastercard Débito / Visa Débito | **Débito** |

Se a lista da direita não tiver a forma que você precisa, cadastre em
**Cadastro → Formas Recebimento** e volte nesta aba.

> A lista só aparece depois que o Uai Rango já enviou as formas. Se estiver
> vazia, confira se o token foi salvo e aguarde a primeira comunicação.

---

## Problemas comuns

| Sintoma | O que verificar |
|---------|-----------------|
| Pedidos não chegam | O token foi salvo? Já passou **até 1 hora**? O suporte já ativou a integração? |
| Status **Aguardando comunicação** | Normal logo após salvar. Só vira **Ativo** quando o Uai Rango responde. |
| Token não edita | A integração já está **Ativa** — o campo trava de propósito. |
| Forma sem vínculo | Abra a aba **Formas Recebimento** e escolha a forma do sistema em cada linha. |
| Falta uma forma no seletor | Cadastre em **Cadastro → Formas Recebimento** e recarregue a aba. |

---

## Precisa de ajuda?

Fale com o **suporte BeeFood** informando: nome da loja, **CNPJ** e um print
do modal (sem expor o token inteiro em canais públicos).

---

*Última atualização: agosto/2026 — BeeFood · Uai Rango*
