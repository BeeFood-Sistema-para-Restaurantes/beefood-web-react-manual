# O que a tela faz de verdade — #109 Despacho automático

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `gestao-entregas-despacho-automatico.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

Lido em `beetech-server-node-2.0/docs/gestao-entrega-2.0/13-despacho-automatico.md` e
conferido na sandbox ligando, agrupando e associando de verdade.

## Onde ele roda

O agrupamento e a associação rodam num **cron de um minuto**, fora do painel. O que o painel
faz é bater um **heartbeat**: o cron só trabalha em filial que deu sinal de tela aberta. É por
isso que o manual avisa, com destaque, que painel fechado é despacho parado — não é
recomendação de uso, é requisito.

## Ele agrupa e associa. Não despacha

Decisão de produto, e a mais importante do manual. Despachar grava a situação no ERP e passa
pelo orquestrador que avisa cliente e marketplace, imprime e baixa estoque. Rota despachada
sozinha avisaria o cliente de algo que não aconteceu — o entregador ainda precisa pegar as
sacolas.

Consequência técnica: **nada nesta fase toca na situação do pedido**. Por isso ela pôde viver
num servidor que não tem WhatsApp, impressão nem integração de marketplace.

## As duas fases são separadas de propósito

| Fase | Quando | Resultado |
|---|---|---|
| Agrupamento | assim que os pedidos entram, sem esperar entregador | rota criada, sem dono — o painel mostra **Montando** |
| Associação | quando as regras de entregador fecham | rota com entregador — o painel mostra **Pronta para sair** |

O motivo de separar é o que o manual explora na seção 4: o lojista vê a rota se formando antes
de ela ganhar dono, e pode intervir. Num passo único ele só veria o resultado.

Rotas criadas na mesma rodada já entram na associação — não se perde um minuto esperando a
rodada seguinte.

## As sete regras, e de onde vêm

| Campo | Origem | Efeito |
|---|---|---|
| máximo de entregas por viagem | do concorrente | teto de pedidos por rota |
| distância máxima para agrupar | do concorrente | distância entre pedidos; vazio desliga |
| tempo máximo para agrupar | do concorrente | diferença de espera; vazio desliga |
| liberar entregador quando | do concorrente | `FINALIZADOS` ou `EM_TRANSITO` |
| raio do restaurante | nossa | entregador a ≤N m da loja |
| considerar a posição do entregador | nossa | associa ao mais próximo da 1ª parada |
| tolerância de GPS | nossa | posição velha = entregador ignorado |

O algoritmo é **guloso**, não ótimo: com grupos de 2 ou 3 pedidos a diferença prática é quase
nula, e o ótimo seria um problema de particionamento por minuto e por filial.

Três detalhes que o manual repassa em palavras simples:

1. **A semente é o pedido mais antigo sem rota** — quem espera mais sai primeiro.
2. **A distância é conferida contra todos os pedidos já no grupo**, não só contra a semente.
   Comparar só com a semente produziria a rota em ziguezague.
3. **A ordem das paradas é refeita depois** de o grupo fechar, pelo trajeto mais curto saindo
   da loja — o mesmo cálculo do botão *Otimizar ordem*. Antiguidade decide quem sai primeiro
   da loja, não a sequência de entrega.

## O freio de 2 horas é constante, não campo

`IDADE_MAXIMA_PEDIDO_MINUTOS = 120`. Ele não está no formulário de propósito: expor
convidaria alguém a aumentá-lo "para pegar os antigos também", que é exatamente o que ele
evita. A janela do ERP já limita a ±6 h; 2 h é o que sobra de razoável para um delivery ainda
sem rota.

A janela **explica** o limite mesmo sem oferecer o campo, e o manual repete a explicação.

## O que impede a associação — medido, não suposto

Na sandbox a rota ficou **em *Montando* por mais de dez minutos** com tudo aparentemente
pronto: três pedidos `PRONTO`, entregador `DISPONIVEL` a 0 m da loja, raio de 500 m.

O que segurava era a **tolerância de GPS de 5 minutos**: a última posição gravada tinha mais
de cinco minutos de idade, e entregador com posição velha sai da lista. Uma gravação de posição
nova (o que o app faz sozinho quando está aberto) e a associação aconteceu na rodada seguinte.

É a experiência que virou a tabela de quatro causas e o aviso da seção 5 — e ela não estava em
documento nenhum: só apareceu porque o cenário foi rodado de verdade.

## Pedido sem coordenada

Com a regra de distância **preenchida** ele fica fora do agrupamento (não há como avaliar se
cabe na viagem). Com a regra **desligada** ele entra, porque o lojista declarou que distância
não importa.

## Como o cenário foi montado

1. Regras afrouxadas (máximo 3, distância 6.000 m) e interruptor ligado pela tela.
2. `cenario.js semear --qtd 3` criou pedidos **novos** — os que sobraram do #108 tinham mais de
   4 h e o freio de 2 h os ignorava.
3. `cenario.js presenca` + `andar --para` a coordenada da loja puseram o entregador disponível
   na porta.
4. `cenario.js rota-prontos` marcou os três prontos, para a regra *Finalizados* liberar.
5. Renovar a posição a cada tentativa foi o que destravou a associação.
6. No fim, as regras voltaram ao original (máximo 2, distância 3.000 m) e o interruptor voltou
   a **desligado** — a sandbox ficou como estava antes.
