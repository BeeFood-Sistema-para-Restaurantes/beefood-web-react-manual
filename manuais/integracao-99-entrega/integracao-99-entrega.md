# BeeFood + 99 Entrega — Guia de integração

Siga este passo a passo para obter as credenciais no painel da 99 e conectar a **99 Entrega** ao seu restaurante, via BeeFood.

---

## O que é a 99 Entrega?

Com a 99 Entrega, seu restaurante pode cotar, despachar, acompanhar e cancelar entregas diretamente pelo BeeFood, usando a rede de entregadores da 99.

Antes de começar a chamar entregadores, você vai precisar: **(1)** ter a 99 Entrega habilitada para o estabelecimento, **(2)** copiar as credenciais de API no painel da 99, **(3)** colar os dados no BeeFood e salvar.

---

## Passo a passo — configurar a integração

### 1. Cadastre seu cartão para pagamentos no painel da 99

No painel da 99 Entrega (https://entrega.99app.com/v2/), acesse a guia **Configurações de pagamento**.

![Configurações de pagamento](imagens-tratadas/99-entrega-01.png)

Na tela de **Configurações de pagamento**, clique em **Gerenciar** para que você possa preencher as informações do seu cartão de crédito.

![Gerenciar método de pagamento](imagens-tratadas/99-entrega-02.png)

Clique na opção **Adicionar cartão**.

![Adicionar cartão no 99Pay](imagens-tratadas/99-entrega-03.png)

Preencha com os dados do seu cartão os campos destacados na imagem abaixo. Após isso, clique em **Adicionar**.

![Preencher dados do cartão](imagens-tratadas/99-entrega-04.png)

---

### 2. Obtenha as credenciais no painel da 99

No painel da 99 Entrega (https://entrega.99app.com/v2/), acesse a guia **Modo de desenvolvedor**.

![Modo de desenvolvedor no painel 99](imagens-tratadas/99-entrega-05.png)

Agora, copie o link `https://entregas.beetechapi.be/api/99Entrega/webhook` e cole no campo URL (Insira o webhook), conforme destacado na imagem abaixo.

![Cadastro do webhook na 99](imagens-tratadas/99-entrega-06.png)

Após isso, você terá acesso aos 3 campos que deverão ser inseridos diretamente via BeeFood.

- **ID do cliente**
- **Segredo do cliente**
- **Chave de assinatura**

![Credenciais no painel 99](imagens-tratadas/99-entrega-07.png)

Guarde esses valores com cuidado — você vai colá-los no BeeFood na próxima etapa.

---

### 3. Acesse a 99 Entrega no BeeFood

No menu lateral do BeeFood, clique em **Aplicativos**.

![Menu lateral — Aplicativos](imagens-tratadas/99-entrega-08.png)

Na seção **Entregas**, selecione **99 Entrega**.

![Aplicativos → Entregas → 99 Entrega](imagens-tratadas/99-entrega-09.png)

Você verá a tela de configuração da 99 Entrega.

---

### 4. Cole as credenciais no BeeFood e salve

- **ID do cliente** — cole o **ID do cliente** da 99 Entrega.
- **Segredo do cliente** — cole o **Segredo do cliente** da 99 Entrega.
- **Chave de assinatura** — cole a **Chave de assinatura** da 99 Entrega.

Deixe a integração **ativa** e clique em **Salvar**.

![Tela de credenciais 99 Entrega no BeeFood](imagens-tratadas/99-entrega-10.png)

Parabéns! A partir de agora a integração BeeFood e 99 Entrega está ativa e você já pode começar a enviar os seus pedidos.

---

### 5. Despache o primeiro pedido

Abra a tela de delivery e localize um pedido do tipo **entrega** (DELIVERY).

![Buscar o pedido na lista](imagens-tratadas/99-entrega-11.png)

Clique em **Adicionar Entregador**.

![Adicionar entregador](imagens-tratadas/99-entrega-12.png)

Selecione a opção **99 Entrega**.
O sistema realizará automaticamente uma cotação com a distância, tempo estimado de entrega e valor do frete.

![Selecionar 99 Entrega](imagens-tratadas/99-entrega-13.png)

Para prosseguir, basta clicar no botão **Confirmar**, conforme destacado na imagem abaixo.

![Visualizar cotação](imagens-tratadas/99-entrega-14.png)

O pedido é enviado à 99 com endereço e cliente já preenchidos.

![Pedido vinculado à 99 Entrega](imagens-tratadas/99-entrega-15.png)

---

### 6. Acompanhe e, se precisar, cancele

Depois do despacho, o pedido fica vinculado à 99 Entrega. O status no BeeFood acompanha a operação via webhook.

Para cancelar, clique no botão de lixeira existente no campo **Entregador** — o cancelamento é enviado à 99 e a associação com a integração é desfeita.

**Nota:** o cancelamento só pode ser feito antes do entregador retirar o pedido no restaurante.

---

## Pronto! O que você pode fazer agora

Com tudo configurado, seu restaurante pode:

- **Despachar** entregadores da 99 pelos pedidos do BeeFood.
- **Acompanhar** o status (e consultar detalhes da corrida quando precisar).
- **Cancelar** uma entrega, quando necessário e antes do entregador retirar o pedido.

---

## Como funciona no dia a dia

1. O pedido entra no BeeFood (site, iFood, balcão ou outro canal).
2. Você avança o pedido no fluxo normal da cozinha.
3. Na hora da entrega, o BeeFood solicita a **cotação** à 99 e, em seguida, cria a corrida.
4. A 99 aloca um entregador.
5. As mudanças de status voltam sozinhas para o BeeFood e atualizam o pedido, WhatsApp e marketplaces quando aplicável.

---

## Status — o que você vê no BeeFood

| Situação na 99 | O que você vê no BeeFood |
|----------------|--------------------------|
| Entregador saiu para entrega | Pedido em **Entrega** |
| Entrega concluída | Pedido **Entregue** |

---
