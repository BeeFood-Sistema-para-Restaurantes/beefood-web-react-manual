# Liberar o entregador: cadastro, acesso ao app e código de barras

Antes de qualquer entrega sair pelo painel, o motoboy precisa existir em **dois lugares**
do BeeFood:

1. como **funcionário** com a função *Entregador* — é isso que o coloca na lista de quem
   pode receber rota;
2. como **usuário** com os *Aplicativos* ligados — é isso que faz o login funcionar no
   celular dele.

Faltando um dos dois, o sintoma é confuso: o entregador aparece no painel mas nunca recebe
entrega, ou o app diz "usuário ou senha inválidos" com a senha certa. Este manual faz os
dois cadastros na ordem e, no fim, liga o **código de barras no cupom**, que é como o
motoboy confirma o pedido pelo celular.

## Para que serve

- Deixar um entregador novo pronto para trabalhar, do zero.
- Entender por que o app recusa o login de um usuário que existe.
- Registrar quanto o entregador recebe por diária e por quilômetro.
- Imprimir no cupom o código de barras que o aplicativo lê.

## Antes de começar

- Você precisa de acesso a **Cadastros → Funcionários** e a **Configuração → Usuários**.
- Tenha em mãos o nome do motoboy e o login e a senha que ele vai usar no celular.
- Para o código de barras, a impressora do **cupom de pedido** já precisa estar
  funcionando.

O aplicativo se chama **BeeFood Entregador** e é gratuito:

- Android — [Google Play](https://play.google.com/store/apps/details?id=com.beetechentregador&hl=pt_BR)
- iPhone — [App Store](https://apps.apple.com/br/app/beefood-para-entregadores/id6736578030)

> **O login do app não é o seu.** Cada motoboy entra com o usuário que você criar para ele.
> Um login por pessoa: é assim que o painel sabe quem está na rua e quem entregou o quê.

---

## 1. Cadastrar o funcionário

Abra **Cadastros → Funcionários**.

![A lista de funcionários](imagens-tratadas/01-lista-funcionarios.png)

| Nº | Onde | O que faz |
|----|------|-----------|
| 1. | **Novo Funcionário (F1)** | Abre a ficha em branco. Use para quem ainda não existe. |
| 2. | **Buscar por nome, CPF ou e-mail** | Ache quem já está cadastrado em vez de duplicar. |
| 3. | **Entregadores** | Quantos funcionários têm a função *Entregador* hoje. É o número que precisa subir quando você terminar. |
| 4. | **Função** | A coluna mostra o que cada um é. Quem está sem nada nessa coluna não entra no painel de entregas. |
| 5. | **Ações** | O lápis abre a ficha de quem já existe. |

Clique em **Novo Funcionário (F1)** (ou no lápis, para aproveitar um cadastro que já
existe).

![A ficha do funcionário, aba Dados](imagens-tratadas/02-funcionario-dados.png)

| Nº | Campo | O que preencher |
|----|-------|-----------------|
| 1. | **Nome** | Único campo obrigatório. Use um nome que dê para reconhecer no painel — *João Moto*, e não *Funcionário 3*. |
| 2. | **Função** | A aba do próximo passo. **É ela que cria o entregador**; a aba *Dados*, sozinha, só cria um funcionário comum. |
| 3. | **Funcionário Ativo** | Deixe ligado. Desligado, ele sai das listas — é o que se usa quando alguém deixa a equipe. |
| 4. | **SALVAR (F2)** | Grava. |

Os outros campos (CPF, RG, telefone, datas) são opcionais e servem ao seu controle. O
**Código Operador** é o número curto usado no PDV, não tem relação com o app.

---

## 2. Marcar a função Entregador

Ainda na ficha, abra a aba **Função**.

![A aba Função, com Entregador marcado](imagens-tratadas/03-funcionario-funcao.png)

| Nº | Onde | O que faz |
|----|------|-----------|
| 1. | **Entregador** | *Atua como entregador no delivery.* **Este é o passo que importa.** Sem ele, o nome não aparece na Gestão de Entregas. |
| 2. | **Valor Diária (R$)** | Valor fixo pago por diária trabalhada. Opcional. |
| 3. | **Valor por KM (R$)** | Valor pago por quilômetro rodado. Opcional. |
| 4. | **Garçom** | A função é **uma só**: marcar *Garçom* desmarca *Entregador*. Quem faz as duas coisas precisa de dois cadastros. |
| 5. | **SALVAR (F2)** | Grava a função. |

Diária e valor por KM não mudam nada no funcionamento do app nem no painel: eles alimentam
o relatório de quanto pagar ao entregador no fim do período. Se você ainda não sabe os
valores, deixe em zero e volte depois —
[Quanto o entregador recebe](../entregador-quanto-recebe/entregador-quanto-recebe.md)
explica onde cada número aparece.

> **Um nome por pessoa.** Dois entregadores com o mesmo nome ficam indistinguíveis no mapa,
> na lista de rotas e no relatório. Se houver dois Josés, use sobrenome.

---

## 3. Criar o usuário do celular

O funcionário do passo anterior **não tem senha**. O login é outro cadastro:
**Configuração → Usuários**.

![A lista de usuários](imagens-tratadas/04-usuarios-lista.png)

| Nº | Onde | O que faz |
|----|------|-----------|
| 1. | **Novo Usuário (F1)** | Abre a ficha do login. |
| 2. | **Função** | Mostra a função do funcionário vinculado ao usuário. É a conferência rápida: usuário de motoboy tem que mostrar *Entregador* aqui. |
| 3. | **Entregador** | O selo que você quer ver na linha do login do motoboy depois de salvar. |

No canto de cima aparece **quantos usuários o seu plano permite** (por exemplo, *7/99
usuários*). Cada motoboy consome um.

Clique em **Novo Usuário (F1)**.

![A ficha do usuário novo](imagens-tratadas/05-usuario-novo.png)

| Nº | Campo | O que preencher |
|----|-------|-----------------|
| 1. | **Login** | O que o motoboy digita no app. Sem espaço e sem acento — `joao.moto` funciona bem. |
| 2. | **Senha** | Combine com ele. Pode ser trocada depois. |
| 3. | **Funcionário** | **Escolha o entregador do passo 1.** É este vínculo que diz ao sistema de quem é aquele login. Ficando em *Nenhum*, o app entra e não mostra entrega nenhuma. |
| 4. | **Grupo de Acesso** | Pode ficar em *Nenhum*: quem só usa o celular não precisa de permissão no sistema. |
| 5. | **Aplicativos** | **Ligue.** Desligado, o app recusa o login mesmo com login e senha certos. É o erro mais comum deste manual. |
| 6. | **SALVAR (F2)** | Grava o login. |

Deixe **Gerente** desligado — ele dá poderes no sistema que o motoboy não usa.

> **Os dois cadastros têm nomes diferentes de propósito.** *Funcionário* é a pessoa;
> *usuário* é a chave que ela usa para entrar. O painel de entregas lê a pessoa; o app lê a
> chave. É por isso que faltar um dos dois dá sintoma em lugares diferentes.

### Conferir se deu certo

Abra a **Gestão de Entregas** e veja a lista de entregadores. O nome novo aparece em
**Offline**, com o aviso **Nunca usou o app** ao lado. É o estado correto de quem está
liberado e ainda não entrou.

Quando o motoboy fizer o primeiro login e se colocar disponível, ele muda de grupo sozinho.
Ler essa lista está em
[Ler o mapa e o painel de entregas](../gestao-entregas-mapa-painel/gestao-entregas-mapa-painel.md).

---

## 4. Ligar o código de barras no cupom

O aplicativo tem um leitor de código de barras: o motoboy aponta a câmera para a etiqueta
do cupom e o pedido é confirmado ali, sem procurar na lista. Para a etiqueta existir, é
preciso ligá-la no layout do cupom.

Abra **Configuração → Impressão**.

![A aba Layout, com os layouts do restaurante](imagens-tratadas/06-impressao-layout.png)

| Nº | Onde | O que faz |
|----|------|-----------|
| 1. | **Layout** | A aba dos desenhos de cupom. As outras abas são das impressoras. |
| 2. | **Cupom Pedido** | O cupom que sai no delivery. É neste, e só neste, que o código de barras existe. |
| 3. | **Lápis** | Abre o layout para edição. |

Dentro do layout, vá para a aba **Texto Padrão**.

![A caixinha Código de Barras App Entrega](imagens-tratadas/07-cupom-texto-padrao.png)

| Nº | Onde | O que faz |
|----|------|-----------|
| 1. | **Texto Padrão** | A terceira aba do layout. A caixinha não está na primeira aba — é onde a maioria procura e não acha. |
| 2. | **Código de Barras App Entrega** | Marque. É o que imprime a etiqueta que o app lê. |
| 3. | **QR Code Cardápio Digital** | Outra coisa: é o QR do cardápio para o cliente. Não confunda. |
| 4. | **SALVAR E FECHAR** | Grava o layout. |

A partir do próximo pedido impresso, o código sai no pé do cupom, **depois do endereço de
entrega**:

![O cupom com o código de barras do aplicativo](imagens-tratadas/08-cupom-impresso.png)

O código só sai em pedido de **delivery com entrega** — não sai em retirada no balcão nem
em venda presencial, porque nesses casos não há motoboy para ler.

### O que acontece quando o motoboy lê o código

Ler o código **não é conferir o pedido: é despachar**. No mesmo instante o BeeFood:

- marca o pedido como **saiu para entrega**;
- atrela o pedido **àquele** entregador;
- avisa o **marketplace**, quando o pedido vem de um (iFood, 99Food e afins);
- dispara o **aviso ao cliente** no WhatsApp, se os avisos estiverem configurados.

Ou seja, é o mesmo efeito do botão de despachar no painel, disparado do celular. Isso tem
duas consequências práticas:

- **Não peça para o motoboy "testar o leitor" com um pedido de cliente.** O cliente recebe
  aviso e o marketplace registra a saída.
- **Ler é irreversível pelo app.** Para corrigir, o acerto é no painel.

Ler o código pelo celular está em
[App do entregador: confirmar a entrega pelo código de barras](../app-entregador-codigo-barras/app-entregador-codigo-barras.md).

> Se você usa a Gestão de Entregas com rotas, o código de barras é um **atalho**, não o
> caminho principal: quem monta a viagem é o painel. O leitor resolve bem o restaurante que
> manda um pedido por vez, sem agrupar.

---

## Problemas comuns

| Sintoma | O que verificar |
|---------|-----------------|
| O app diz que o login é inválido, mas login e senha estão certos | O switch **Aplicativos** no usuário está ligado? É a causa em quase todos os casos. |
| O motoboy entra no app e não vê entrega nenhuma | O campo **Funcionário** do usuário está preenchido com o entregador, e não em *Nenhum*? |
| O nome não aparece na Gestão de Entregas | A aba **Função** do funcionário está com **Entregador** marcado? |
| Aparece na lista, mas nunca recebe rota | Ele está **Offline**. Quem muda isso é o próprio motoboy, no app. Se estiver com **Nunca usou o app**, ele ainda não entrou. |
| O cupom sai sem código de barras | **Código de Barras App Entrega** marcado no layout do **Cupom Pedido**, aba *Texto Padrão*? O pedido é delivery **com entrega**? |
| Dois motoboys se confundem no mapa | Nomes iguais ou parecidos. Renomeie em **Cadastros → Funcionários**. |
| O funcionário sumiu das listas | O switch **Funcionário Ativo** foi desligado. |

---

## Onde continuar

| Manual | O que cobre |
|--------|-------------|
| [Ler o mapa e o painel de entregas](../gestao-entregas-mapa-painel/gestao-entregas-mapa-painel.md) | A tela onde o entregador cadastrado aparece |
| [Montar a rota](../gestao-entregas-montar-rota/gestao-entregas-montar-rota.md) | Juntar pedidos numa viagem e escolher quem leva |
| [Quanto o entregador recebe](../entregador-quanto-recebe/entregador-quanto-recebe.md) | Diária, valor por KM e o relatório de fechamento |
| [App do entregador: instalar, entrar e ficar disponível](../app-entregador-entrar/app-entregador-entrar.md) | O primeiro acesso, do lado do motoboy |
