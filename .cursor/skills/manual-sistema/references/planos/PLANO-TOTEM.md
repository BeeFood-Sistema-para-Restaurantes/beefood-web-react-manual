# Plano — Totem de Autoatendimento (#121, #122, #123)

> Estudo pedido pelo dono em **21/09/2026** (*"estude para fazer manuais do totem de
> autoatendimento"*) e **recortado por ele em 22/09/2026**: CRM no totem (cupom e cashback)
> e a regra da foto do setor entram; a lista de seis manuais sai. O pedido foi
> *"precisamos ser mais diretos… podemos agrupar, falar menos, ser mais objetivos"*.

Status: ☑️ **aprovado — três manuais** (`pode fazer, sem parar`, 22/09/2026).

Tudo abaixo foi **medido no sandbox BeeFood3 - Manual** (empresa 38311, filial 39202) com
Playwright, e o registro bruto das medições está em `estudo-totem-medicoes.log` (artefato da
sessão). O que importa para quem for escrever está resumido aqui.

---

## 1. A descoberta que destrava o bloco: o totem abre no Cloud Agent

A memória dizia que totem e tablet não são fotografáveis aqui, porque são aplicativo Android.
**Vale para o tablet, não para o totem.** O totem é uma página web (PWA), e a própria aba
*Download* do painel entrega a URL:

```
https://totem.beefood.app/?empresaID=38311&filialID=39202&token=D3590976-63A1-4FDF-9721-0E054CBF3BB5
```

O `token` é o `aaToken` da filial — dá para lê-lo no `config_cache` do `localStorage` do painel,
ou simplesmente copiar pelo botão **Copiar** da aba *Download*. Com viewport de **1080×1920** o
Chromium desenha o aparelho inteiro, e o pé da tela mostra a versão (`v1.170926.1226`).

Consequência prática: **cada configuração do painel pode ser fotografada em par** — a chave no
painel e o efeito na tela do cliente. É isso que os três manuais fazem.

Duas manhas de automação, aprendidas no ensaio:

- Os botões do aplicativo respondem a `click()` por JavaScript, mas **o teclado numérico não**
  (ele escuta evento de ponteiro). Para digitar telefone e mesa, é preciso o clique real do
  Playwright: `get_by_role("button", name=c, exact=True).first.click(force=True)`.
- Os seletores não são estáveis; o que funciona é procurar botão **pelo texto**, e filtrar pela
  altura do elemento quando o texto aparece em mais de um lugar (cartão e cabeçalho).

---

## 2. O que o painel tem — cinco abas, e nenhum botão Salvar

**Aplicativos → Autoatendimento presencial → Totem de Autoatendimento.** O cabeçalho do modal
mostra **5 TOTENS CONTRATADOS** (o `qtdAA` do contrato) e o rodapé só tem **FECHAR (ESC)**:
cada campo grava sozinho, como nas telas de auto-save do #32.

| Aba | O que decide |
|-----|--------------|
| **Configuração** | meio de consumo (Comer aqui / Para viagem), impressão do cupom e da senha, emissão de NFC-e, observação de produto e de pedido, tradução, identificação do cliente (nome/telefone e mesa), senha do administrador, produto de acréscimo por meio de consumo e mensagem final |
| **Pagamentos** | os seis meios: Dinheiro, Pix BeeFood, Pix TEF, Crédito TEF, Débito TEF, Vale Refeição TEF — cada um amarrado a uma forma de pagamento do sistema |
| **Aparência** | tema (branco/preto) e cor principal, logotipo, capa e os slides/vídeos da tela de espera (com a regra escrita na tela: MP4 H.264, até 1080×1920, 4–6 Mbps; HEVC/H.265 e 4K não funcionam) |
| **Cardápios** | quais cardápios de outras lojas ficam disponíveis; o da loja principal está sempre ativo |
| **Download** | a URL do totem (com **Copiar**) e os dois `.cmd` de modo kiosk, para Edge e para Chrome |

Estado do sandbox hoje: consumo nos dois, impressão de cupom e senha ligadas (impressora
`EPSON TM-T20 Receipt5`), **NFC-e desligada**, observação de produto e de pedido ligadas,
tradução ligada (herança do #100), identificação em *Nome e Telefone Opcional* + *Informar Número
da Mesa*, e **todos os seis pagamentos ligados**. Com Dinheiro ligado, dá para fechar pedido no
totem **sem pinpad nenhum** — é o que permite gerar a venda de hoje para o #123.

---

## 3. CRM no totem — o recorte novo pedido pelo dono

O totem **não tem configuração de cupom nem de cashback**: ele lê o que o CRM já tem. As duas
chamadas que provam isso, feitas pelo próprio aparelho ao abrir:

```
GET /api/venda2/cupomDescontoAtivo/38311/0?tipo=totem
GET /api/totem2/filial/38311/39202/0
```

**Cupom.** A resposta traz os cupons cujo canal *Totem* está ligado no cadastro do CRM — 7 no
sandbox — e o aparelho desenha o cadastro inteiro: título, benefício, e **uma linha de texto por
regra**. Medido:

| Código | Benefício | Selos e regras que o totem escreve |
|--------|-----------|------------------------------------|
| `FIRST` | 15% | selo **LOGIN** • *Válido apenas para a primeira compra* |
| `SMS` | 5% | *O pedido precisa ter: Combos…, Bacon* • *Não vale para itens em promoção* • *Válido apenas para retirada ou consumo no local* • *Válido apenas para pagamento em: PIX Bee, PIX Online, Dinheiro* • *É preciso confirmar seu telefone por SMS* |
| `PIX15%` | 15% | *Válido apenas para pagamento em: PIX Bee, PIX Online* • *É preciso confirmar seu telefone por SMS* |

Ou seja: **a regra que o operador escreve no CRM vira frase na tela do cliente**, e regra que
exige login ou SMS transforma a identificação em obrigatória. É o eixo do #122.

**Cashback.** Vem da filial: `cashBackAtivo`, `cashBackDeliveryTotem` (a modalidade *Pedidos via
Totem*), `cashBackPorReal = 0,03` e validade de 35 dias. O efeito aparece em três lugares do
aparelho, todos medidos:

1. tela de identificação — *"Insira seu telefone e ganhe 3% de cashback"*;
2. confirmação, com o telefone informado — *"Cashback disponível R$ 1,19"* + botão **USAR R$ 1,19**;
3. barra do total — *"Você ganhará de cashback R$ 0,84"* (3% de R$ 28,00).

O aparelho também reconhece o cliente pelo telefone (mostra o nome e um botão **Sair**).

---

## 4. A regra da foto — medida por interceptação, e o que ela muda

Hoje o sandbox está com os **7 setores sem foto** e os **67 produtos com foto**. Interceptando as
respostas da API para simular o contrário, o comportamento ficou claro — e é diferente do que a
intuição diz:

| Onde está a foto | O que muda no totem |
|------------------|---------------------|
| **Setor** (`s3Link` em `/api/totem2/setores`) | **muda o layout da coluna da esquerda**: com foto, cada setor vira miniatura com o nome embaixo; sem foto, a coluna é listagem pura de texto — que é o que está no ar hoje |
| **Produto** (`s3Link` em `/api/totem2/produtos`) | **não muda layout nenhum**: a grade de três colunas continua igual e o cartão exibe o ícone de **imagem quebrada** |

A conclusão que o manual precisa passar: *ou todos os setores têm foto, ou nenhum* — e **produto
sem foto no totem não é "listagem simples", é cartão com imagem quebrada**. A medição por
interceptação serve para nós; a prova publicável exige subir foto de verdade (Cardápio → setor →
**ADICIONAR FOTO**).

---

## 5. Os três manuais

### #121 — Totem de Autoatendimento: pôr no ar e configurar

`manuais/totem-configurar/`

O manual que faltava: onde o totem é contratado, como se abre a URL no aparelho, as cinco abas e
— o que nenhum manual diz hoje — **o que cada chave faz na tela do cliente**, em par de imagens.
Entra também a regra da foto do setor, porque é decisão de cadastro que só aparece no totem.

Não é inventário de campo: as abas *Aparência*, *Cardápios* e *Download* entram com uma imagem
cada, pelo que o leitor decide nelas.

### #122 — Cupom e cashback no totem

`manuais/totem-cupom-cashback/`

Onde se liga o canal *Totem* no cupom e a modalidade *Pedidos via Totem* no cashback, e o que o
cliente vê: o selo de cupons disponíveis, a lista de regras em texto, o cupom que exige login ou
SMS, o saldo de cashback e o "você ganhará" da barra do total. Fecha com a pergunta que o
suporte recebe: *"por que o cupom não apareceu no totem?"*.

### #123 — O pedido do totem no painel

`manuais/totem-venda-no-painel/`

O outro lado do balcão: o pedido do totem chegando no **Delivery**, no **Histórico de Vendas**
(com o filtro de origem), na ficha da cozinha e no **Desempenho** por origem. O sandbox já tem
32 vendas de totem antigas; o manual usa **uma venda nova, feita por nós, paga em Dinheiro**,
para o leitor ver a venda do dia.

---

## 6. Decisões de produção

- **Um pedido real no totem, pago em Dinheiro**, com a técnica do ensaio: o roteiro roda inteiro
  até a tela de pagamento sem confirmar, é revisado, e só então repete para valer. Sem NFC-e
  (está desligada) e sem impressora física.
- **Foto de setor subida de verdade** em um setor, para o par "sem foto / com foto" do #121 ser
  prova e não montagem. O estado anterior (todos sem foto) fica fotografado antes.
- **Nada de tela vazia** (regra 0 da memória): a aba *Cardápios* do sandbox diz "Nenhum outro
  cardápio disponível", e isso entra como frase no texto, não como imagem.
- O que for aprendizado de **captura** vai para a `MEMORIA-GERAL.md`; o que for de **cenário**
  (como escrever no sandbox) vai para a `cenario-sandbox`.
