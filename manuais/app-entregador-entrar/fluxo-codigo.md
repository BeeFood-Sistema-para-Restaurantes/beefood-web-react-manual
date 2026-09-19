# O que o aplicativo faz de verdade — #111

Fonte: o estudo do código do aplicativo que veio no material do dono
(`manuais/gestao-entregas/material-recebido/app-entregador/estudo/01-o-que-o-app-faz-hoje.md`),
mais o estudo do backend em `manuais/gestao-entregas/estudo/01-como-o-sistema-funciona.md`.
**Nada aqui vai para o manual do usuário**: rota de API e nome de arquivo ficam nesta página.

## 1. A ordem das telas não é a ordem das permissões

O aplicativo pede **localização**, **localização em segundo plano** e **câmera** *antes* do
formulário de login, e **notificações** *depois* do login aceito. Não é descuido: as três
primeiras são o que o aplicativo precisa já na primeira conversa com o servidor, e a de
notificações depende de um token que só existe com sessão.

```
Login  →  Load (animação, ~3 s)  →  MainTabs (Entregas)
```

A tela `Load` é a **porta única**: entra por login novo e por sessão restaurada. É lá que o
aplicativo carrega entregas e histórico, reafirma a presença e registra o token de push. Sessão
inválida volta para `Login` — é isto que o usuário percebe como "abriu e voltou para o login".

## 2. Login

| Item | Como é |
|---|---|
| Endpoint | `POST tusuario/validaBeeEntregador`, no servidor 2.0 |
| Resposta | vai inteira para `AsyncStorage['dadosFuncionario']`, como array; o aplicativo consome sempre o `[0]` |
| Validação local | **não existe.** Campo vazio também vira POST |
| Erro | **Usuário e/ou Senha inválidos.**, visível ~3 s |

A mensagem de erro é **única** para senha errada, usuário inexistente e acesso desativado. Quem
decide é o servidor; o aplicativo só exibe. Daí a frase do manual: se veio *Usuário e/ou Senha
inválidos*, o aplicativo **falou** com o servidor — falha de rede tem outra mensagem.

O login não tem recuperação de senha porque o acesso não é do entregador: é um usuário do painel,
com os *Aplicativos* ligados. Quem cria e reseta é o restaurante, na tela de Usuários.

## 3. Sessão

A sessão vive no `AsyncStorage`, sem prazo de validade do lado do aplicativo. Só três coisas a
derrubam:

1. o **Sair** do menu;
2. o servidor recusar a sessão na passagem pela `Load`;
3. limpar os dados do aplicativo pelo Android.

O logout faz mais do que apagar a sessão: **marca presença offline no servidor**, desativa o
dispositivo de push, para o GPS, limpa filas e o cache de formas de pagamento. É por isso que o
manual diz que sair é diferente de ficar offline — sair faz as duas coisas.

## 4. Presença

| Item | Como é |
|---|---|
| Componentes | `PresencaSwitch.js`, `SwitchPresenca.js`, `ModalPresenca.js` |
| Endpoint | `POST entrega2/gestao/presenca` (servidor 3.0) |
| Estados | `ONLINE`, `PAUSA`, `OFFLINE` |
| Tocar no estado já ativo | fecha a folha **sem requisição** |
| Sem confirmação do servidor | ícone de nuvem cortada, em amarelo, na própria pílula |

A pílula aparece só nas telas **Entregas** e **Histórico**.

**A presença não filtra despacho.** O painel usa o estado para ordenar e sugerir entregador, e o
aplicativo usa para espaçar o envio de GPS, mas nada no servidor impede despachar para quem está
OFFLINE. O texto da própria folha admite isso (*a decisão de te enviar uma entrega continua sendo
dele*), e o manual repete a frase em vez de suavizar: entregador que entende a pílula como tranca
vai brigar com o restaurante por um pedido que chegou depois do "acabei".

## 5. GPS

O envio de posição é global, montado no `EntregadorLocationReportingHost` — fora das telas, para
continuar rodando enquanto o entregador navega no aplicativo.

- manda a posição a cada ~10 segundos, e **só quando há deslocamento**: celular parado não fica
  repetindo a mesma coordenada;
- fora do ONLINE, o intervalo aumenta;
- sem a permissão de segundo plano, o envio para quando o aplicativo sai da tela — e o pino do
  entregador **congela** no painel, o que o operador lê como "o entregador parou".

Do lado do servidor, a posição cai em `entregas.posicao` e atualiza `entregador_status`, que é o
que o painel lê para desenhar o pino e calcular `posicaoIdadeMinutos`.

## 6. Permissões

`src/views/permissoes/index.js`. Quatro cartões, cada um com etiqueta **Ativa** ou **Inativa**, e
o texto literal que o manual reproduz. Duas coisas que a tela deixa claras e o manual precisa
repetir:

- **o aplicativo não concede permissão nenhuma.** Tocar no cartão abre as configurações do
  Android. É regra do sistema;
- o **ícone de recarregar** do cabeçalho relê o estado — sem ele, quem acabou de conceder no
  Android continuaria vendo *Inativa*.

Quando o pedido é negado no fluxo de entrada, o aplicativo mostra o alerta **Permissão
necessária** com os botões **Cancelar** / **Abrir configurações**.

## 7. O que existe no código e não tem porta na tela

Levantado no estudo do material, e **fora do manual** de propósito — manual de coisa que não
existe nasce errado:

| Item | Situação |
|---|---|
| `ModalWhatsApp`, com cinco mensagens prontas ao cliente | componente completo, **não montado em tela nenhuma** |
| `MainTabsHeader.js`, `ModalDesconectado.js` | código morto |
| rota de navegação `'Rota'` | referenciada, não registrada |

## 8. Onde o manual escolheu ser mais direto que a tela

| Tela diz | Manual diz | Por quê |
|---|---|---|
| **Apenas esta vez** é uma opção como as outras | "evite" | ela funciona hoje e volta a perguntar no próximo turno; quem escolhe isso fica invisível no painel até responder de novo |
| a folha de disponibilidade explica a consequência em letra cinza | o aviso ganhou número de seta e parágrafo próprio | é a linha que separa "avisei" de "bloqueei", e ela está justamente no texto que ninguém lê |
| **Permissões** é um item de menu entre cinco | o manual manda conferir no começo do turno | o Android revoga por inatividade e não avisa; a falha aparece como defeito do aplicativo |

## 9. O que a pílula amarela e o selo vermelho dizem por baixo

**A nuvem cortada é estado local sem confirmação do servidor.** A presença muda primeiro no
aparelho e a tela responde na hora, mesmo sem rede — esperar o servidor faria o entregador achar
que o aplicativo travou. Quando o `POST` de presença não volta, o estado fica marcado como não
sincronizado e a pílula ganha o ícone.

A retentativa pega carona no tick de 10 s do relato de posição, com **piso de 60 s** entre
tentativas, e acontece também quando o aplicativo volta ao primeiro plano. `HTTP 400` é tratado
como definitivo: insistir num corpo que o servidor nunca vai aceitar só gera tráfego. O manual
traduz isso como *o aplicativo tenta de novo sozinho* — o entregador não tem botão para forçar, e
não precisa de um.

**O selo da tela de Permissões é leitura, não interruptor.** A tela é de conferência: mostra estado
e abre as configurações do sistema. Quem pede a permissão de notificação é o
`registrarDispositivoPush()`, no `Load`, e não esta tela — o plano original pedia ali, e mudou
porque a maioria dos entregadores nunca abre a tela de Permissões. O cartão de status existe
justamente para o caminho de volta: quem nega uma vez não é perguntado de novo pelo sistema
(`canAskAgain` falso), e as configurações do aparelho passam a ser o único caminho.

## 10. Procedência das imagens

As treze primeiras vêm do material que o dono enviou — emulador `Pixel_7_Pro`, Android 15, contra
a filial de teste. **Não há como capturar tela de app daqui**: o Cloud Agent não roda emulador.

O `annotate.py` recorta, reamostra para largura fixa e acrescenta a margem clara onde a etiqueta
vive. Nenhuma imagem é montagem: a de três pílulas é a justaposição de três recortes reais, e
está declarada como tal na legenda.

As duas últimas (`14` e `15`) vieram da segunda rodada de capturas. A `14` segue a mesma
justaposição da `10` — duas pílulas PAUSA reais, coladas — e a `15` reusa o recorte da `12` para
as duas telas de Permissões ficarem sobreponíveis. Nenhuma das duas mostra data, então nenhuma
passou pelo `relogio.py`.
