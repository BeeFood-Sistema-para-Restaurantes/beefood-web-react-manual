# MEMÓRIA — #110 Avisos de WhatsApp da entrega

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `gestao-entregas-avisos-whatsapp.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

## O que este manual é

O quarto bloco do plano da Gestão de Entregas: a tela de notificações automáticas vista pelo
recorte da entrega. Não substitui o [#87](../whatsapp-notificacoes/), que é sobre os oito avisos
do pedido do cliente; aqui são os **quatro** avisos que a entrega dispara, três deles para o
entregador.

## A descoberta que virou a espinha do manual

O plano do bloco já suspeitava disso, e a medição confirmou com número: **o raio do aviso de
proximidade está NULL em 56.654 das 56.661 filiais**, e o padrão global também está NULL. O
`sql/010` previa `filiaisSemRaio = 0` — o passo das colunas rodou, o do back-fill não.

O que torna isso pior que um campo vazio é que **a tela mostra 2 km**: o React cai em
`raioProximidadeMetros ?? raioDefault ?? 2000` para não exibir caixinha vazia. Então o lojista
vê um aviso ligado, com texto pronto e distância configurada — e ele nunca saiu.

Conferi os dois lados na sandbox, e é a prova que sustenta a seção 4:

```
antes de salvar:  raioProximidadeMetros = null
depois de SALVAR: raioProximidadeMetros = 2000
```

Salvar funciona porque o modal sempre manda o campo quando o tipo é o da proximidade, e o valor
que ele manda é o que está na tela — o padrão. **Isso virou seção, não nota de rodapé**, porque
é a diferença entre o recurso funcionar e não funcionar.

## O que eu esperava e não era assim

| Eu esperava | O que é |
|---|---|
| Os quatro avisos no mesmo grupo | Três no grupo **Entregador**, um no grupo **Delivery** — a tela agrupa por destinatário |
| A paleta de variáveis oferecer os marcadores das mensagens novas | Ela é fixa (MEU / CLIENTE / VENDA). `**ENTREGADOR_NOME**`, `**DETALHE_ENTREGAS**`, `**LINHA_TAXAS**`, `**DATA_REFERENCIA**` e `**QTD_ENTREGAS**` funcionam mas **não** aparecem |
| "Entrega cancelada" ser o cancelamento do pedido | É "este pedido não é mais seu" — troca de entregador, parada removida, rota excluída |
| O campo de km aceitar metros | Recusa acima de 50, de propósito: é o erro de quem digita 2000 |
| A distância valer na hora | Até 30 min (cache do servidor de entregas). O liga/desliga, sim, vale na hora |

## Decisões de captura

- **As duas conversas são mockup, e o texto não foi escrito à mão.** O `/tmp/ge/mock110.py` lê o
  `msgPadrao` do banco, substitui os marcadores pelos dados do cenário de hoje (rota 125,
  pedidos 1048 a 1050) e resolve o `{a|b}` na primeira opção. Se o texto de fábrica mudar, a
  imagem mente — e é por isso que o script fica registrado aqui e no `fluxo-codigo.md`.
- **Salvei o aviso de proximidade na sandbox** e deixei salvo: é o estado correto, e o print de
  `2000` no banco é a prova da seção 4. Não é mudança que precise ser desfeita.
- **`07-km-recusado.png` foi capturado de propósito com erro**: digitei 2000, cliquei em SALVAR
  e fotografei a recusa. É a única imagem do manual que mostra o sistema dizendo não.
- **O recorte do cadastro de funcionário** (`10a`) nasceu porque a imagem inteira tem a lista
  atrás do modal e as duas caixinhas de telefone ficavam pequenas no meio de um formulário de
  dez campos.
- **A etiqueta ficou dentro das caixinhas de Telefone e Celular**: elas estão vazias, e qualquer
  lado de fora cobria o rótulo do campo de cima (E-mail) ou de baixo (Data de Admissão).

## O que não entrou

- **Prova de mensagem enviada de verdade.** O sandbox não tem número conectado, e conectar um
  número é decisão do dono. O manual assume o funcionamento, como autorizado.
- **A lacuna do pedido transferido entre rotas**: quando a rota de origem não fica vazia, o
  entregador de origem não recebe *Entrega cancelada*. Está no doc 20 como pendência conhecida;
  não entra no manual do usuário porque ele não tem o que fazer a respeito.
- **A vazão de 5 mensagens por filial por minuto** ficou no `fluxo-codigo.md`, não no manual: o
  lojista não configura isso, e a informação levaria a conclusões erradas ("o sistema está
  lento").

## Scripts

| Script | O que faz |
|---|---|
| `/tmp/ge/cap110.py` | lista, grupo Entregador e os modais 30, 32 e 33 |
| `/tmp/ge/cap110b.py` | salva o raio (a prova da seção 4) e captura a recusa de 2000 |
| `/tmp/ge/cap110c.py` | o campo Celular do cadastro de funcionário |
| `/tmp/ge/mock110.py` | as duas conversas, a partir do texto gravado no banco |
| `/tmp/dbcheck/rel110.js` | a medição dos quatro tipos na base |
