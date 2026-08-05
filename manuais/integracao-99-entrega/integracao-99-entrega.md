# BeeFood + 99 Entrega — Guia de integração

Siga este passo a passo para obter as credenciais no painel da 99 e conectar a **99 Entrega** ao seu restaurante, via BeeFood.

---

## O que é a 99 Entrega?

Com a 99 Entrega, seu restaurante pode cotar, despachar, acompanhar e cancelar entregas diretamente pelo BeeFood, usando a rede de entregadores da 99.

**Forma de pagamento da integração:** nas entregas despachadas pela 99 Entrega via BeeFood, o único método de pagamento aceito é o **boleto**. Cartão de crédito e outras formas **não** se aplicam a esse fluxo de integração.

Antes de começar a chamar entregadores, você vai precisar: **(1)** ter a 99 Entrega habilitada para o estabelecimento, **(2)** solicitar o **boleto** nas configurações de pagamento (único método da integração; análise da 99), **(3)** pedir o **ambiente de produção** no modo de desenvolvedor (também com análise da 99), **(4)** copiar as credenciais de API no painel da 99, **(5)** colar os dados no BeeFood e salvar.

---

## Passo a passo — configurar a integração

### 1. Solicite o boleto nas configurações de pagamento

Nas entregas via integração BeeFood + 99 Entrega, o **boleto** é o **único** método de pagamento. Não use cartão para configurar o pagamento dessa integração.

No painel da 99 Entrega (https://entrega.99app.com/v2/), acesse a guia **Configurações de pagamento**.

![Configurações de pagamento — solicitar boleto](imagens-tratadas/99-entrega-05.png)

Na opção de seleção, escolha **Boleto** — é a opção correta e a única usada pela integração.

![Selecionar Boleto](imagens-tratadas/99-entrega-06.png)

Clique em **Confirmar**.

![Confirmar solicitação de boleto](imagens-tratadas/99-entrega-07.png)

A solicitação fica **pendente de análise pela 99**. Aguarde a aprovação antes de seguir — a liberação depende da análise da 99 e pode levar algum tempo. **Para agilizar o processo, entre em contato com o suporte BeeFood.**

![Boleto pendente de análise](imagens-tratadas/99-entrega-08.png)

---

### 2. Após a aprovação do boleto, peça o ambiente de produção

Quando a 99 **aprovar o boleto**, o painel passa a refletir essa liberação. Em seguida, clique em **Modo de desenvolvedor**.

![Painel após aprovação do boleto — Modo de desenvolvedor](imagens-tratadas/99-entrega-09.png)

Clique em **Ambiente de produção**.

![Ambiente de produção](imagens-tratadas/99-entrega-10.png)

Role até a parte inferior da tela e clique em **Enviar**.

![Enviar solicitação de produção](imagens-tratadas/99-entrega-11.png)

Confirme o envio clicando novamente em **Enviar**, conforme a tela.

![Confirmar envio](imagens-tratadas/99-entrega-12.png)

Assim como no boleto, a solicitação de **ambiente de produção** fica **pendente de análise pela 99**. Só depois dessa aprovação você terá o acesso completo para copiar as credenciais de API usadas no BeeFood. **Para agilizar o processo, entre em contato com o suporte BeeFood.**

![Ambiente de produção pendente de análise](imagens-tratadas/99-entrega-13.png)

---

### 3. Configure o webhook e obtenha as credenciais no painel da 99

Após a aprovação do ambiente de produção, no painel da 99 Entrega (https://entrega.99app.com/v2/), acesse a guia **Modo de desenvolvedor**.

![Modo de desenvolvedor no painel 99](imagens-tratadas/99-entrega-14.png)

Agora, copie o link `https://entregas.beetechapi.be/api/99Entrega/webhook` e cole no campo URL (Insira o webhook), conforme destacado na imagem abaixo.

![Cadastro do webhook na 99](imagens-tratadas/99-entrega-15.png)

Após isso, você terá acesso aos 3 campos que deverão ser inseridos diretamente via BeeFood.

- **ID do cliente**
- **Segredo do cliente**
- **Chave de assinatura**

![Credenciais no painel 99](imagens-tratadas/99-entrega-16.png)

Guarde esses valores com cuidado — você vai colá-los no BeeFood na próxima etapa.

---

### 4. Acesse a 99 Entrega no BeeFood

No menu lateral do BeeFood, clique em **Aplicativos**.

![Menu lateral — Aplicativos](imagens-tratadas/99-entrega-17.png)

Na seção **Entregas**, selecione **99 Entrega**.

![Aplicativos → Entregas → 99 Entrega](imagens-tratadas/99-entrega-18.png)

Você verá a tela de configuração da 99 Entrega.

---

### 5. Cole as credenciais no BeeFood e salve

- **ID do cliente** — cole o **ID do cliente** da 99 Entrega.
- **Segredo do cliente** — cole o **Segredo do cliente** da 99 Entrega.
- **Chave de assinatura** — cole a **Chave de assinatura** da 99 Entrega.

Deixe a integração **ativa** e clique em **Salvar**.

![Tela de credenciais 99 Entrega no BeeFood](imagens-tratadas/99-entrega-19.png)

Parabéns! A partir de agora a integração BeeFood e 99 Entrega está ativa e você já pode começar a enviar os seus pedidos.

---

### 6. Despache o primeiro pedido

Abra a tela de delivery e localize um pedido do tipo **entrega** (DELIVERY).

![Buscar o pedido na lista](imagens-tratadas/99-entrega-20.png)

Clique em **Adicionar Entregador**.

![Adicionar entregador](imagens-tratadas/99-entrega-21.png)

Selecione a opção **99 Entrega**.
O sistema realizará automaticamente uma cotação com a distância, tempo estimado de entrega e valor do frete.

![Selecionar 99 Entrega](imagens-tratadas/99-entrega-22.png)

Para prosseguir, basta clicar no botão **Confirmar**, conforme destacado na imagem abaixo.

![Visualizar cotação](imagens-tratadas/99-entrega-23.png)

O pedido é enviado à 99 com endereço e cliente já preenchidos.

![Pedido vinculado à 99 Entrega](imagens-tratadas/99-entrega-24.png)

---

### 7. Acompanhe e, se precisar, cancele

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
