# O que o app faz hoje — inventário de telas, textos e APIs

Levantamento por leitura de código em `src/`, em 17/09. Serve de espinha dorsal dos manuais: é
daqui que sai a lista de prints a tirar e o texto literal que cada print tem de mostrar.

Os textos entre **negrito** são literais da interface, copiados do código. Se um print divergir
de algo escrito aqui, o print manda — e a linha é corrigida.

---

## 0. Correções ao `spec.md`

Duas divergências encontradas entre o `spec.md` da raiz e o código atual. Registro para não
tropeçar depois:

| `spec.md` diz | Código diz |
|---|---|
| `views/barras/` com resíduos de merge `index_BACKUP_459.js`, `index_BASE_459.js`, `index_REMOTE_459.js` | a pasta `src/views/barras/` **não existe mais**; o scanner é só o modal `components/Barras/BarcodeScannerModal.js` |
| detalhes da entrega em `components/Entregas/Detalhes` | o arquivo é `components/Rota/Detalhes.js`; em `components/Entregas/` moram `ItemEntrega`, `CabecalhoRota`, `AcoesEntrega` e as duas folhas de confirmação |

---

## 1. Navegação

`src/Navigation.js`. Chrome escuro `#212121` no header, gaveta e barra de abas.

```
NavigationContainer
├── EntregadorLocationReportingHost   (GPS, global)
├── EntregadorPushHost                (push, global)
├── Drawer  (rota inicial: Load)
│   ├── Login
│   ├── MainTabs
│   │   ├── Entregas        → aba inicial
│   │   ├── Historico
│   │   ├── Barcode         → placeholder: abre o modal do scanner
│   │   └── Configuracoes   → placeholder: abre a gaveta
│   ├── Load
│   └── Permissoes
└── BarcodeScannerModal               (overlay global)
```

Abas, com o rótulo literal: **Entregas**, **Histórico**, **Código barras**, **Ajustes**.
Gaveta: **Entregas**, **Histórico**, **Código barras**, **Permissões**, **Sair**.

Fluxo de entrada: `Login` → `Load` (3 s de animação) → `MainTabs`.

---

## 2. Telas, uma a uma

### 2.1 Login — `src/views/login/index.js`

Campos com placeholder **Usuário** e **Senha** (com ícone de olho), botão **ENTRAR**.
Erro: **Usuário e/ou Senha inválidos.**, visível 3 s. Sucesso mostra animação e vai para `Load`.

Antes do formulário o app pede permissões; negada, aparece o alerta **Permissão necessária** com
o texto *A permissão de {localização / localização em segundo plano / câmera} foi negada.
Habilite manualmente nas configurações do dispositivo para continuar utilizando o aplicativo.* e
os botões **Cancelar** / **Abrir configurações**.

Não há validação de campo vazio: o app envia o POST de qualquer forma.

API: `POST tusuario/validaBeeEntregador` (`apiN`, servidor 2.0). A resposta inteira vai para
`AsyncStorage['dadosFuncionario']` como array; o app consome sempre o `[0]`.

**Prints do manual 01:** formulário vazio, senha visível/oculta, erro de credencial, os diálogos
de permissão, a animação de sucesso.

### 2.2 Load — `src/views/load/index.js`

Animação, logo e spinner. **Sem texto.** É a porta única: entra por login novo e por sessão
restaurada. Aqui o app carrega entregas e histórico, reafirma a presença e registra o token de
push. Sessão inválida → volta para `Login`.

### 2.3 Permissões — `src/views/permissoes/index.js`

Título **Permissões**. Texto de apoio: *Toque em uma permissão para abrir as configurações do
dispositivo e habilitar ou desabilitar o acesso.* Quatro cartões, cada um com etiqueta **Ativa**
ou **Inativa**:

| Cartão | Descrição na tela |
|---|---|
| **Localização** | *Usada para acompanhar a entrega em tempo real e gerar rotas.* |
| **Localização em segundo plano** | *Permite enviar sua posição à central quando o app está minimizado.* |
| **Câmera** | *Usada para leitura de códigos de barras dos pedidos.* |
| **Notificações** | *Avisa quando um pedido ou uma rota é atribuída a você.* |

### 2.4 Presença — `PresencaSwitch.js`, `SwitchPresenca.js`, `ModalPresenca.js`

Pílula no canto direito do header, nas telas Entregas e Histórico, com três rótulos: **ONLINE**,
**PAUSA**, **OFFLINE**. Enquanto salva, spinner; se o servidor não confirmou, ícone de nuvem
cortada em amarelo.

O toque abre a folha **Sua disponibilidade** com as três opções e a consequência de cada uma:

- **Online** — *Você está trabalhando e o restaurante te vê disponível.*
- **Em pausa** — *O restaurante te vê em intervalo, sem encerrar seu turno.*
- **Offline** — *Turno encerrado. O restaurante te vê fora de serviço.*

Rodapé: *Isto avisa o restaurante sobre sua intenção de trabalho — a decisão de te enviar uma
entrega continua sendo dele. Fora do online, o app economiza bateria enviando sua posição com
menos frequência.* E **CANCELAR**.

Tocar no estado já ativo fecha sem requisição. API: `POST entrega2/gestao/presenca` (`apiN3`).

**Prints do manual 02:** pílula nos três estados, folha aberta, pílula com o aviso de não
sincronizado.

### 2.5 Lista de Entregas — `src/views/entregas/index.js`

Recarrega ao ganhar foco, no arrastar para baixo, no botão **ATUALIZAR** e quando o entregador
toca numa notificação push.

Vazia: **Nenhuma entrega agora** + *Quando o restaurante te enviar um pedido, ele aparece aqui.*
+ *Arraste a tela para baixo para atualizar.* + **ATUALIZAR**.

Com conteúdo, a tela tem **N grupos de rota e uma lista solta**, e qualquer um dos dois pode
estar vazio. A faixa **OUTRAS ENTREGAS ({N})** só aparece quando existem as duas coisas ao mesmo
tempo.

**Cartão do pedido** (`ItemEntrega.js`): número da parada (a `ordem` da rota, ou a posição na
lista quando avulso), etiqueta **#{numeroPedido}**, etiquetas de marketplace quando houver,
**Previsão Entrega** com a hora (em vermelho se atrasado), endereço completo e, quando há saldo,
**Cobrar R$ {valor}** em verde. Toque abre os detalhes. **Não há botão de cobrança na lista** —
ele vive nos detalhes.

**Cabeçalho de rota** (`CabecalhoRota.js`): **ROTA {código}** num círculo amarelo,
**{n} de {N} entregues**, a marca **em rota** quando já despachada, e o botão: **INICIAR ROTA**
(verde) enquanto não despachada, **ABRIR NO MAPS** (azul) depois.

**Melhor rota:** com mais de um pedido avulso, aparece o botão flutuante
**MELHOR ROTA GOOGLE MAPS ({N})**, que abre a janela **ABRIR ROTA** com o ícone do Google Maps e
**FECHAR**. Ele reordena as paradas por distância da loja — por isso vale só para os avulsos, e
cada rota tem o próprio botão.

API: `GET entrega2/gestao/entregador/{empresaID}/{filialID}/{usuarioID}/{funcionarioID}`
(`apiN3`), com fallback para o 2.0 em caso de falha.

**Prints dos manuais 03, 06 e 07.**

### 2.6 Detalhes da entrega — `src/components/Rota/Detalhes.js`

Abre como tela cheia sobre a lista. Header **DETALHES DA ENTREGA**.

**Bloco fixo no topo** (não rola): **Endereço de entrega** com o endereço, o **complemento** em
pílula vermelha com texto branco quando existir, **Observações** com o texto da venda em
laranja, e o botão **VER NO MAPA**, que abre a folha com **GOOGLE MAPS** e **WAZE**.

**Corpo:** **Realizado às {hora}**, **#{numeroPedido}**, etiquetas de iFood/Uber/99/Keeta quando
houver, e a lista de produtos — carregada sob demanda, com esqueleto de carregamento. Quantidade
sempre como **`Nx`**, tanto no produto quanto nas opções. Item marcado como destaque de impressão
sai em preto: linha a linha quando só o produto ou só algumas opções estão marcados, e como
cartão preto inteiro quando produto e todas as opções estão.

**Rodapé:** **FORMA DE PAGAMENTO** com o `tipoPagStr`, ou **não informado**; e as colunas
**TOTAL**, **TROCO** (quando o texto do pedido traz "troco para") e **COBRAR** em verde quando há
saldo. Abaixo, os botões de marketplace quando aplicável (**CONFIRMAR ENTREGA IFOOD** /
**CONFIRMAR ENTREGA 99FOOD**) e as ações da entrega.

**Ações** (`AcoesEntrega.js`):

| Situação | Botões |
|---|---|
| Há saldo a cobrar | **INICIAR COBRANÇA** e, abaixo, **FINALIZAR SEM COBRAR** (cinza) |
| Não há saldo | **FINALIZAR** |
| O pagamento já foi registrado nesta sessão | só **FINALIZAR** |

Duas folhas se intrometem antes, por decisão de produto:

1. Se algum produto ou opção está marcado como destaque, aparece
   **CONFIRMA E ENTREGA DESSES PRODUTOS CORRETAMENTE?** com a lista e **CONFIRMAR** / **CANCELAR**.
2. Se for finalizar com saldo em aberto, **Finalizar sem cobrar?** com o valor e
   **CONTINUAR** / **CANCELAR**.

No modo histórico a tela muda: mostra **VALOR TOTAL DO PEDIDO** e a linha do tempo
**REALIZADO** / **COLETADO** / **ENTREGUE**, e nenhum botão de ação.

API dos produtos: `GET entrega2/gestao/entregador/historico/produto/{empresaID}/{usuarioID}/{preVendaID}`.

**Prints dos manuais 04, 05 e parte do 13.**

### 2.7 Cobrança — `src/components/Rota/Cobranca.js` e vizinhos

Abre de dentro dos detalhes, deslizando da direita. Header **PAGAMENTO** com o botão de
atualizar formas.

Ao abrir: **Consultando saldo…**, enquanto busca em paralelo o saldo da venda e as formas de
pagamento (as formas têm cache de 24 h em disco).

**Formulário:** nome do cliente, etiqueta **PEDIDO #{numero}**, **A RECEBER** com o valor,
**TOTAL** e **JÁ PAGO**, o bloco **JÁ REGISTRADO** quando houver pagamento anterior,
**DIVIDIR CONTA** com o seletor de 1 a 10 pessoas, e um cartão **Pessoa N** por pessoa
(`CobrancaPessoa.js`) com valor editável, **FORMA DE PAGAMENTO** / **Selecione a forma** e, em
dinheiro, **Troco para**. Aviso em vermelho quando a conta não fecha:
**A soma precisa ser R$ {saldo}**. Campo de observação com o placeholder
**Deseja adicionar alguma observaçao?** e contador de 200 caracteres. Rodapé escuro com
**CONFIRMAR PAGAMENTO**.

Com **uma** pessoa, o campo de forma não aparece na tela: o **CONFIRMAR PAGAMENTO** abre primeiro
a folha de formas.

**Folhas do fluxo:**

| Folha | Título e conteúdo |
|---|---|
| Formas | **FORMA DE PAGAMENTO** (+ **Pessoa N** na divisão), lista de formas, **CANCELAR** |
| Bandeira | **BANDEIRA**, *Opcional — a taxa resolve pela forma se você pular*, **CONTINUAR SEM BANDEIRA** |
| Troco | **Troco para quanto?**, *Digite quanto vai ser pago em dinheiro.*, **CONFIRMAR** / **SEM TROCO** |
| Confirmação | **Confirmar cobrança?**, *Vai registrar R$ {saldo} nesta entrega. Confira as formas antes de enviar.*, resumo linha a linha, **CONFIRMAR** / **CANCELAR** |

**Resultados:**

| Estado | O que a tela diz |
|---|---|
| Enviando | **Registrando pagamento…** |
| Já pago | **Pedido já pago** — *Não há saldo a receber. Finalize a entrega se ainda não estiver encerrada.* → **FECHAR** |
| Bloqueado | **Não foi possível cobrar** + a mensagem do servidor → **TENTAR NOVAMENTE** / **ATUALIZAR FORMAS** / **VOLTAR** |
| Sucesso | **Pagamento Confirmado!** — *O pagamento de R$ {saldo} foi registrado com sucesso.* → **VOLTAR PARA ENTREGAS** |
| Pago sem baixa | **Pagamento Confirmado!** — *O pagamento foi registrado. Finalize a entrega — o dinheiro já está no caixa.* |
| Erro | **Erro no Pagamento** → **TENTAR NOVAMENTE** / **VOLTAR PARA ENTREGAS** |

APIs: `GET .../pagamentos/...` e `GET .../formasPagamento/...` na abertura;
`POST entrega2/gestao/entregador/pagamento` no envio — e é este POST que **também finaliza a
entrega**, quando o pedido não está em rota ou quando o `rotaID` vai no corpo.

**Prints dos manuais 11 e 12.** É o fluxo com mais telas do app: contando folhas e resultados,
são 12 a 15 capturas.

### 2.8 Finalizar — `src/components/Rota/Finalizar.js`

Folha que sobe de baixo. Título **Finalizar Entrega** com o valor em verde quando há saldo.
Campo de observação de 200 caracteres, com placeholder **Deseja adicionar alguma observaçao?** —
ou **Por que não houve cobrança?** no caminho sem cobrança, onde aparece também a dica *Você está
encerrando com saldo em aberto. A observação (até 200 caracteres) explica no histórico por que
não houve cobrança.*

Botões empilhados, **FINALIZAR** acima de **CANCELAR** — nesta ordem de propósito: o FINALIZAR
move o pedido no ERP, avisa o cliente e o marketplace, então quem fica na zona de esbarrão do
polegar é o CANCELAR.

Falha: **Não foi possível dar baixa** — *O servidor não confirmou a entrega. Verifique a conexão e
tente novamente.*

API: `POST entrega2/gestao/entregador/entregar`, com `rotaID` e `obsEntrega` quando houver.

### 2.9 iFood e 99Food — `src/components/Rota/IfoodView.js`

O botão aparece no rodapé dos detalhes: **CONFIRMAR ENTREGA IFOOD** quando o pedido tem
`ifoodLocalizer`, **CONFIRMAR ENTREGA 99FOOD** quando tem `nnID`.

Abre uma WebView com o site do parceiro. No topo, o app mostra **LOCALIZADOR** com o número
espaçado (iFood) e um botão de copiar, que confirma com **Localizador copiado com sucesso!** ou
**Código copiado com sucesso!**. Enquanto carrega, **Carregando...**

| Parceiro | Endereço aberto |
|---|---|
| iFood | `confirmacao-entrega-propria.ifood.com.br/numero-pedido` |
| 99Food | `food-b-h5.99app.com/pt-BR/v2/confirmation-entrega` |

O app **não preenche o site**: ele copia o código e o entregador cola. Keeta aparece só como
etiqueta, sem botão.

**Prints dos manuais 09 e 10.**

### 2.10 Código de barras — `src/components/Barras/BarcodeScannerModal.js`

Abre pela aba **Código barras**, pelo item da gaveta, ou por chamada de outra tela. Título
**LEITURA DE CÓDIGO**, faixa de status com as mensagens **Aguardando Leitura**,
**Lendo código...**, **Pedido lido com sucesso!**, **Pedido já lido.**,
**Erro na leitura, tente novamente** e **Erro: {mensagem}**. Dica sob a faixa da câmera:
**Posicione o código de barras na faixa da câmera**. Botão **VOLTAR**, que fecha e recarrega a
lista de entregas.

Sem permissão: **Permissão de câmera necessária**, com **Solicitar Permissão**,
**Abrir Configurações** e **FECHAR**.

O código lido é um EAN-13; o app descarta o último dígito e usa o resto como `preVendaID`.
API: `POST tentrega/lerCodigoBarras`.

**Prints do manual 08.**

### 2.11 Histórico — `src/views/historico/index.js`

Cabeçalho com **{N} Entregas** e o período. Lista agrupada por dia (`ItemGrpHistorico.js`): dia
da semana, data e **{n} entrega(s)**. Vazio: **Nenhuma entrega no período** + *As entregas que
você concluir aparecem aqui.*

Tocar num dia abre a lista daquele dia (`ItemHistorico.js`): pedido, **Entregue às {hora}**,
endereço e um **!** vermelho quando houve atraso. Tocar num item abre os detalhes em modo
somente leitura.

API: `GET entrega2/gestao/entregador/historico/{empresaID}/{usuarioID}/{funcionarioID}/{data}/{data}`
— hoje o app manda a data de hoje nos dois campos.

**Prints do manual 14.**

### 2.12 Sair — `src/components/Navigation/ConfirmarSair.js`

Folha **Sair do aplicativo?** — *Você vai encerrar a sessão neste aparelho. Para voltar a receber
entregas, será preciso entrar de novo.* — **SAIR** / **CANCELAR**.

O logout marca presença offline no servidor, desativa o dispositivo de push, para o GPS, limpa
filas e cache de formas de pagamento e apaga a sessão.

---

## 3. O que existe no código e não tem porta de entrada na tela

Vai para o apêndice `o-que-nao-existe-na-tela.md` do manual:

| Item | Situação |
|---|---|
| `ModalWhatsApp` — cinco mensagens prontas ao cliente (**Não encontrei o endereço**, **Estou a caminho**, **Cheguei no local**, **Tentei entregar, sem resposta**, **Atraso na entrega**) | componente completo, **não montado em nenhuma tela** |
| Confirmação de entrega Keeta | só a etiqueta **#{keetaId}**; sem WebView, ao contrário de iFood e 99Food |
| `MainTabsHeader.js`, `ModalDesconectado.js` | código morto, não montados |
| Rota de navegação `'Rota'` | referenciada, **não registrada** no navigator |
| Linha de quilometragem no histórico | existe na tela com opacidade zero — invisível de propósito |
