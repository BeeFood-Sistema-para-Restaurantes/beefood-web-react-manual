# Cardápio Digital no Tablet — Modo Kiosk

> **RASCUNHO — não publicar.** O material que o dono anexou ao pedido (`manual-modo-kiosk.md`
> e a pasta `images`) **não chegou ao ambiente do Cloud Agent**. Este texto foi escrito a
> partir do que dá para comprovar no código do painel, no servidor e nas fontes oficiais da
> BeeFood. As partes que dependem do anexo estão marcadas com **[PENDENTE — ANEXO]**, e as
> imagens ainda não existem em `imagens-tratadas/`. Detalhes em `MEMORIA.md`.

Este manual ensina, passo a passo, a deixar o tablet **preso no cardápio**: o cliente pede
sozinho na mesa e não consegue sair do aplicativo, abrir o navegador nem mexer nas
configurações do aparelho.

O que você vai fazer:

1. **Preparar o cardápio** que o tablet vai exibir (aba Layout)
2. **Conferir o tablet** na listagem (status, bateria, versão e limite contratado)
3. **Fixar a mesa** no tablet, para dispensar a leitura do QR Code
4. **Travar o tablet**, bloqueando a saída do aplicativo
5. **Confirmar** que o comando chegou (aba Eventos)
6. **Destravar** quando precisar dar manutenção

> As imagens têm **setas com números** (1, 2, 3...). No texto, cada número indica exatamente
> o campo ou botão correspondente na tela.

---

## O que é o modo kiosk e por que usar

Um tablet no salão é um computador completo na mão do cliente. Sem nenhuma trava, qualquer
pessoa sentada na mesa pode sair do cardápio, abrir o navegador, mexer no Wi-Fi, desinstalar
o aplicativo ou simplesmente deixar o aparelho numa tela que o próximo cliente não entende.

Modo kiosk é o nome que se dá a deixar o aparelho **dedicado a uma única função**. No
Cardápio Digital no Tablet, isso significa três coisas somadas:

- **O aplicativo não deixa sair.** O botão *voltar* fica bloqueado, então o cliente não
  consegue abandonar o cardápio.
- **A mesa fica fixa no aparelho.** O tablet já sabe em qual mesa está, e o cliente não
  precisa apontar a câmera para o QR Code a cada pedido.
- **O tablet volta sozinho para o início.** Depois de **5 minutos** sem ninguém tocar, o app
  retorna à tela de destaques, pronto para o próximo cliente. Se houver itens no carrinho,
  ele pergunta antes por **60 segundos**, para não descartar um pedido de quem só se
  distraiu.

O ganho é operacional: o aparelho está sempre na tela certa, na mesa certa, e a equipe não
perde tempo reconfigurando tablet no meio do serviço.

---

## Pré-requisitos

- **Tablets contratados** no plano. A quantidade aparece no card *Contratados*; passar do
  limite faz o sistema **deslogar os tablets excedentes sozinho**.
- **Cardápio habilitado para tablet.** Se o cardápio aparecer esmaecido na aba Layout, com o
  botão *Chame o Suporte para Habilitar*, a liberação é feita pelo suporte BeeFood.
- **Mesas (ou comandas) já cadastradas** em Cadastros. Sem mesa cadastrada, o tablet não
  consegue lançar pedido.
- **Aplicativo instalado** no tablet: *Cardápio Digital Mesa/Comanda*, na Google Play.
- **Aparelho dentro dos requisitos:** Android 11 e 2 GB de RAM no mínimo; Android 14 e 4 GB
  recomendados.
- **Tablet logado e online** — o comando de travar é entregue no próximo contato do aparelho
  com o servidor.

---

## Etapa 1 — Preparar o cardápio que o tablet vai exibir

Antes de travar o aparelho, deixe pronto o que ele vai mostrar. Depois de travado, mexer no
tablet dá trabalho.

1. No menu lateral, clique em **Cardápio Digital Tablet**.
2. Abra a aba **Layout**.
3. Localize o cardápio (cada filial tem o seu) e clique em **Configurar**.

> 🖼️ **[PENDENTE — ANEXO]** imagem `01-aba-layout.png` — a listagem de cardápios com os selos
> (Light/Dark, Grade/Lista, PIX Online, Chamar Garçom, Fechar Conta) e o botão **Configurar**.

Na aba **Configurações** do modal, ajuste:

| Campo | O que faz |
|-------|-----------|
| **Tema** | *Light* (tons de branco) ou *Dark* (tons de preto). Escolha pensando na luz do salão. |
| **Tipo de Layout** | *Lista Completa* mostra setores e produtos numa lista só. *Por Etapas* pede o setor primeiro, depois o subsetor e por fim os produtos. |
| **Pix online** | Permite o fechamento da conta com Pix pelo próprio tablet. |
| **Chamar Garçom e Opções** | Libera o botão de chamar o garçom e pedir cortesias (talher, sal, copo). Imprime um cupom com a solicitação. |
| **Solicitar Fechamento de Conta** | Exibe no tablet o botão para o cliente pedir a conta. |

As abas **Slides** e **Garçom Opções** completam a configuração: os slides são as imagens da
tela inicial, e as opções de garçom são a lista de cortesias que o cliente pode pedir.

> **Dica:** deixe o *Chamar Garçom* ligado quando for travar o tablet. Com o aparelho preso no
> cardápio, esse botão passa a ser o caminho natural do cliente para pedir ajuda.

---

## Etapa 2 — Conferir o tablet na listagem

Volte para a aba **Tablets**. Cada aparelho aparece como um card, e a faixa colorida no topo
indica o estado dele.

> 🖼️ **[PENDENTE — ANEXO]** imagem `02-aba-tablets.png` — os cinco cards de estatística, a
> busca, os filtros de versão e a grade de tablets.

Os cinco cards do topo:

| Card | O que significa |
|------|-----------------|
| **Contratados** | Quantos tablets o plano cobre. |
| **Total** | Quantos aparelhos aparecem com os filtros atuais. |
| **Online** | Deram sinal há **menos de 1 hora**. |
| **Ausentes** | Deram sinal entre **1 e 6 horas** atrás. |
| **Offline** | Sem sinal há **6 horas ou mais**. |

Cada card de tablet mostra o número do aparelho (`#id`), a mesa vinculada, marca e modelo, a
bateria, há quanto tempo foi o último sinal e a versão do aplicativo.

**Antes de travar, confira três coisas:**

- **O tablet está Online.** Um aparelho *Ausente* ou *Offline* só vai receber o comando
  quando voltar a se comunicar.
- **A bateria está boa.** O ícone fica vermelho abaixo de 20%. Tablet travado que descarrega
  no meio do almoço vira mesa sem cardápio.
- **A versão está atualizada.** Os selos de versão logo abaixo da busca ficam **verdes** na
  versão mais nova e **âmbar** nas antigas. Clique num selo para filtrar só aqueles
  aparelhos.

> **Atenção ao limite contratado.** Se a soma de tablets *Online* + *Ausentes* passar do
> número de contratados, aparece a faixa vermelha *"Quantidade de tablets ultrapassa o limite
> contratado"* e **os excedentes são deslogados automaticamente**. Um tablet deslogado sai do
> cardápio e volta para a tela de login — nenhuma trava segura isso. O botão **Contratar
> tablet** abre o WhatsApp do financeiro com a mensagem pronta.

A lista se atualiza sozinha a cada **60 segundos** (a barrinha dentro do botão de atualizar
mostra o tempo). Para atualizar na hora, clique no botão.

---

## Etapa 3 — Fixar a mesa no tablet

Fixar a mesa é o que faz o tablet "pertencer" àquela mesa. Sem isso, o cliente precisa ler o
QR Code da mesa toda vez que fecha um pedido.

1. Clique nos cards dos tablets que você quer configurar. O card selecionado ganha borda
   destacada e o quadradinho marcado. Para pegar todos os filtrados de uma vez, use
   **Selecionar todos**.
2. Clique em **Enviar evento**.
3. Escolha **Vincular Mesa/Comanda**.
4. No campo **Selecione a Mesa**, busque pelo código ou pelo nome e escolha a mesa.
5. Clique em **ENVIAR EVENTO** (ou tecle **F1**).

> 🖼️ **[PENDENTE — ANEXO]** imagem `03-evento-vincular-mesa.png` — o modal *Enviar Evento* com
> a opção **Vincular Mesa/Comanda** marcada e o seletor de mesa aberto.

> **Um tablet por mesa.** O vínculo é por aparelho. Se você selecionar cinco tablets e
> escolher a Mesa 10, os cinco vão ficar na Mesa 10. Para mesas diferentes, envie um evento
> para cada tablet.

Para desfazer, envie o evento **Remover Vínculo de Mesa/Comanda**. O tablet volta a pedir a
leitura do QR Code.

---

## Etapa 4 — Travar o tablet

Este é o passo que fecha o modo kiosk pelo painel.

1. Selecione os tablets.
2. Clique em **Enviar evento**.
3. Escolha **Travar**.
4. Clique em **ENVIAR EVENTO** (ou tecle **F1**).

> 🖼️ **[PENDENTE — ANEXO]** imagem `04-evento-travar.png` — o modal *Enviar Evento* com a
> opção **Travar** marcada, mostrando também a contagem *Tablets selecionados*.

O modal envia **um comando por tablet**, com uma barra de progresso *Enviando x/y...*.
Enquanto envia, não é possível fechar a janela. No fim aparece um aviso dizendo para quantos
aparelhos o evento foi enviado.

**O que o Travar faz:** bloqueia os botões de voltar do aplicativo, para que o cliente não
consiga sair do cardápio.

> **Importante:** o comando entra numa **fila**. O painel confirma o envio na hora, mas quem
> executa é o tablet, no próximo contato dele com o servidor. Em aparelho *Ausente* ou
> *Offline*, o travamento acontece quando ele voltar.

Os seis eventos disponíveis, para referência:

| Evento | O que faz |
|--------|-----------|
| **Atualizar Cardápio e Layout** | Puxa as alterações de cardápio e de layout para o tablet. |
| **Travar** | Bloqueia a saída do aplicativo. |
| **Destravar** | Libera a saída do aplicativo. |
| **Vincular Mesa/Comanda** | Fixa uma mesa no aparelho (dispensa o QR Code). |
| **Remover Vínculo de Mesa/Comanda** | Desfaz o vínculo. |
| **Deslogar Usuário** | Faz logout e volta o tablet para a tela de login. |

---

## Etapa 5 — Conferir se o comando chegou

1. Abra a aba **Eventos**.
2. Procure a linha do evento que você acabou de enviar.

> 🖼️ **[PENDENTE — ANEXO]** imagem `05-aba-eventos.png` — o histórico com uma linha
> *Processado* e uma *Pendente*.

| Coluna | O que mostra |
|--------|--------------|
| **Status** | *Pendente* (ainda não chegou ao tablet) ou *Processado* (o tablet executou). |
| **Evento** | O código do comando: `TRAVAR`, `DESTRAVAR`, `MESA`, `MESA_REMOVER`, `ATUALIZAR`, `DESLOGAR`. |
| **Data Criação** | Quando você enviou. |
| **Data Processado** | Quando o tablet executou. |
| **Dispositivo (ID)** | O identificador do aparelho. |
| **Mesa** | A mesa vinculada, quando houver. |

Só considere o tablet travado depois que a linha ficar **Processado**. Se continuar
*Pendente* por muito tempo, o aparelho provavelmente está sem rede — confira o status na aba
Tablets.

---

## Etapa 6 — Destravar para dar manutenção

Para atualizar o aplicativo, trocar de rede Wi-Fi ou mexer nas configurações do Android, o
tablet precisa sair do modo kiosk:

1. Selecione o tablet.
2. **Enviar evento** → **Destravar** → **ENVIAR EVENTO**.
3. Faça a manutenção.
4. Envie **Travar** de novo ao terminar.

> Lembre-se de mandar **Atualizar Cardápio e Layout** sempre que mexer em produtos, preços ou
> no layout — assim o tablet pega as mudanças sem precisar reiniciar nada.

---

## Etapa 7 — Travar o aparelho pelo Android

**[PENDENTE — ANEXO]**

O *Travar* do painel bloqueia a saída **pelo aplicativo**. Fechar o aparelho por completo —
barra de navegação, notificações, botão de início, acesso às configurações do Android e
retorno automático ao app depois de reiniciar — é configuração do próprio Android, feita uma
vez em cada tablet.

Esta seção precisa do material anexado ao pedido (`manual-modo-kiosk.md` e as imagens), que
não chegou ao ambiente. Não escrevi o procedimento por conta própria para não publicar um
caminho diferente do que a BeeFood recomenda.

---

## Dicas e problemas comuns

| Situação | O que costuma ser | O que fazer |
|----------|-------------------|-------------|
| O evento fica *Pendente* | Tablet sem rede ou desligado | Conferir o status na aba Tablets; o comando é entregue quando o aparelho voltar |
| O tablet caiu para a tela de login sozinho | Limite de tablets contratados estourado | Conferir a faixa vermelha na aba Tablets e o card *Contratados* |
| O tablet pede QR Code a cada pedido | A mesa não está fixada | Enviar o evento **Vincular Mesa/Comanda** |
| Mudei o cardápio e o tablet não mostrou | Falta sincronizar | Enviar o evento **Atualizar Cardápio e Layout** |
| O cardápio nem aparece na aba Layout | Cardápio não habilitado para tablet | Acionar o suporte BeeFood (botão *Chame o Suporte para Habilitar*) |
| Um tablet some da lista | Sem sinal há mais de 6 horas ele conta como *Offline*, mas continua listado | Se sumiu mesmo, foi deslogado — verificar o limite contratado |
| A versão do app está em âmbar | Aparelho desatualizado | Destravar, atualizar pela Google Play e travar de novo |

---

## Referências internas (não publicar)

- Mapeamento técnico: `fluxo-codigo.md` desta pasta.
- Memória do manual, com o que ficou pendente: `MEMORIA.md`.
