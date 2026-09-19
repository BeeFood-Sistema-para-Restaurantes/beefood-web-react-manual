# Relatório das capturas

## O que foi capturado

| | |
|---|---|
| **App** | BeeFood Entregador `3.3.0` (build Android `versionName 1.0.1.2`, `versionCode 24`), build de desenvolvimento rodando com o Metro |
| **Data** | 19/09/2026, entre 02h e 04h |
| **Aparelho** | emulador `Pixel_7_Pro` (AVD), Android 15, `sdk_gphone64_x86_64`, locale pt-BR |
| **Ambiente** | empresa 38311 / filial 39202 / entregador 194115 (`BeeFood3 - Manual`), GPS fixado na loja (`-23.5061438, -47.4657927`) |
| **Cenários** | `2-scripts/smoke-app.js` e `2-scripts/cenario.js`, um caso por foto, com `limpar` entre eles |

**24 dos 26 prints saíram.** Os dois que faltam são os de iPhone.

## Os prints que saíram diferentes do pedido

### `19-sem-internet/01-lista-sem-carregar.png`

O pedido era a lista sem carregar. O app **não mostra mensagem de erro** nesse estado: com a rede
desligada, a lista de Entregas fica congelada no que já tinha em cache e o pull-to-refresh não
muda nada. O print é essa tela, com os ícones de sem sinal na barra de status. Vale como está —
é o que o entregador vê —, mas o manual precisa descrever o comportamento assim, e não como um
aviso na tela.

Não dá para fotografar o app abrindo *do zero* sem rede neste build: sem Metro ele não carrega o
bundle JavaScript. Num APK de produção esse caminho existe e vale uma captura futura.

### `20-permissao-e-presenca/01-localizacao-recusada.png`

Em vez de `pm clear` (que derrubaria o login e o token de push do cenário inteiro), a permissão
foi **revogada pelo sistema** (`adb shell pm revoke ... ACCESS_FINE_LOCATION` e as duas irmãs). O
app reabriu, pediu a permissão, e a resposta foi **Não permitir** na caixa do Android — mesmo
caminho do entregador que recusa. A foto é a tela **Permissões** do app com *Localização* e
*Localização em segundo plano* em **Inativa**, e Câmera e Notificações em **Ativa**. As permissões
foram devolvidas logo depois.

### `22-erros-de-cobranca/04-falta-finalizar.png`

Saiu — e sem depender de sorte com o relógio. Em vez de tentar cortar a rede no meio de dois
pedidos HTTP, a rota foi **excluída no painel** com a folha *Confirmar cobrança?* já aberta no
celular. O pagamento entrou (a rota não tem nada com o caixa) e a baixa falhou, porque o app
mandou o `rotaID` de uma rota que não existia mais. É exatamente o estado que o FAQ descreve:
dinheiro no caixa, entrega ainda aberta.

Duas telas extras dessa sequência ficaram em `_triagem/prints/` e podem entrar no manual se você
quiser contar a história inteira: o alerta **Pagamento registrado — Finalize a entrega** que
aparece ao voltar (`pos22.png`) e o **Não foi possível dar baixa** que o FINALIZAR dá enquanto o
app ainda carrega o `rotaID` velho (`pos22d.png`). O caminho de saída é atualizar a lista: sem a
rota, o FINALIZAR passa.

### `23-rota-com-problema/02-falha-melhor-rota.png`

**A mensagem é outra, e isso é um achado, não um erro de captura.** Com o wifi desligado, tocar em
MELHOR ROTA não mostra *Ocorreu uma falha ao gerar a melhor rota* — mostra **Permissão
necessária · Permissão de localização é necessária para continuar**. O `try/catch` de
`src/components/Rota/ModalApp.js` embrulha a leitura do GPS **e** a chamada HTTP no mesmo `catch`,
então qualquer falha de rede sai com o texto de permissão.

O texto pedido só apareceria se o servidor respondesse 200 com um corpo sem `resultado`. Testando
o `tutils/entregadorMelhorRota` direto, as falhas reais dele vêm como `{resultado:false, msg:...}`
— e nesse caminho o app mostra *Falha* com a mensagem do servidor (`Ocorreu um erro ao cálcular a
melhor rota`, ou `Falha ao cálcular a latitude e longitude dos endereços`). Ou seja: o manual do
#113 deve responder a pergunta com **duas** mensagens possíveis, e vale abrir um ajuste no app
para o `catch` não chamar de permissão o que é rede.

### `18-ciclo-completo` — as seis fotos da janela do #117

A janela rodou inteira, as sete fases, no mesmo lote de pedidos (`59587920`, `59587921`,
`59587923`, vendas #1105 a #1107, rota `A` id 131). Duas observações:

- **As três baixas vieram do celular**, não do painel — que era a opção que o roteiro chama de
  "mais verdadeira". A primeira foi dinheiro com troco para R$ 50,00 (troco R$ 30,10), a segunda
  Débito · Visa e a terceira PIX Manual.
- `05-lista-sem-a-rota.png` ficou sendo a **lista vazia**: com as três paradas entregues e nada
  mais atribuído, não sobrou item nenhum na tela. É a mesma imagem de estado que
  `21-listas-vazias/01`, só que no contexto do ciclo. Se o manual precisar da rota sumindo *com
  outros pedidos ainda na lista*, é refazer a janela com um pedido solto a mais.

As fotos do painel (fila, rota criada, despacho, pin andando, parada entregue, relatório) **não
estão aqui** — são da sua metade da janela, como o roteiro previa.

## Os prints que não saíram

### `25-ios/01-lista-entregas.png` e `25-ios/02-detalhes-entrega.png`

**Não há iPhone nem simulador iOS nesta máquina** (ambiente Windows; o projeto tem a pasta `ios/`,
mas compilar exige macOS). A pasta ficou vazia.

Como o kit manda: enquanto essas duas não existirem, o manual deve falar **só de Android** e não
prometer que a tela do iPhone é igual.

## Detalhes que ajudam a ler as imagens

- **O marcador `[SEED-ENTREGAS]` não aparece em nenhuma foto.** Ele mora agora em
  `_cliente.Observacao`, que o app não mostra, e a observação da venda recebeu um texto de vida
  real (*Portão azul, chamar no interfone.*). A limpeza pelos scripts continua funcionando.
- **Todos os pedidos têm o mesmo formato de itens** (combo + acompanhamento + bebida, ou o item
  único do gerador), para as telas não mudarem de assunto entre um capítulo e outro.
- **A pílula de disponibilidade** aparece ONLINE na maioria das fotos; onde ela está com a nuvem
  cortada (`20/02`) é o print do estado sem sincronia, que é o assunto daquele capítulo.
- Nas fotos de erro de rede, os ícones da barra de status mostram wifi e dados desligados — é o
  jeito de o leitor saber que não é falha do servidor.

## Depois das capturas

Cenário desmontado: `smoke-app.js limpar` rodou no fim, a lista do app está vazia, nenhuma rota
ficou aberta e nenhuma entrega ficou pendente. O pedido usado no `22/04` — que tinha pagamento e
não tinha baixa — foi finalizado pela mesma porta do botão FINALIZAR, para não sobrar entrega
aberta na sandbox. As permissões de localização do emulador foram devolvidas e o GPS voltou para a
loja.
