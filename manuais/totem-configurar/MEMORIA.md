# MEMORIA.md — #121 Totem de Autoatendimento: pôr no ar e configurar

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `totem-configurar.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

## Pedido do dono

> "estude para fazer manuais do totem de autoatendimento, me traga as ideias que
> chegou" (21/09/2026) e, no dia seguinte, o recorte: *"crm no totem: cupom de
> desconto e cashback; fotos do setor → aparece setor com fotos, sem foto aparece
> listagem pura (vale no layout). tbm acho que criamos manuais de mais. precisamos
> ser mais diretos… refaça o pensamento"* → três manuais, aprovados com
    10|*"pode fazer, sem parar"*.

Plano do bloco: [`PLANO-TOTEM.md`](../../.cursor/skills/manual-sistema/references/planos/PLANO-TOTEM.md).
Medições brutas do estudo: `estudo-totem-medicoes.log` (artefato da sessão).

## Escopo

O manual que faltava: onde o totem é contratado, o que cada aba do painel
decide, **o efeito de cada decisão na tela do cliente** e a regra da foto do
setor. Não é inventário de campo — Aparência, Cardápios e Download entram com
uma imagem cada.

    20|Fica fora: cupom e cashback (#122) e a venda no painel (#123).

## A descoberta que destravou o bloco

A `MEMORIA-GERAL` dizia que totem e tablet não são fotografáveis no Cloud Agent,
porque são aplicativo Android. **Vale para o tablet, não para o totem**: o totem
é uma página web (PWA) e a aba *Download* entrega a URL. Com viewport de
**1080×1920** o Chromium desenha o aparelho inteiro.

```
https://totem.beefood.app/?empresaID=38311&filialID=39202&token=<aaToken>
```

    30|O `aaToken` sai do `config_cache` do painel ou do botão **Copiar** da aba
Download. Sandbox descartável, então a URL fica versionada no `capturar.py`.

Duas manhas do aparelho, que valem para os três manuais (e já estão na
`MEMORIA-GERAL`):

- os botões respondem a `click()` por JavaScript, mas **o teclado numérico não**
  (ele escuta evento de ponteiro) — ali é preciso
  `get_by_role("button", name=c).click(force=True)`;
- os seletores não são estáveis: o que funciona é achar botão **pelo texto** e
  filtrar pela **altura/posição** quando o texto repete (cartão e cabeçalho).

    40|## Estado do sandbox (BeeFood3 - Manual, empresa 38311, filial 39202)

`qtdAA = 5` → o card abre a configuração, e o cabeçalho diz **5 TOTENS
CONTRATADOS**.

| Aba | Estado fotografado |
|-----|--------------------|
| Configuração | consumo nos dois; cupom e senha impressos (`EPSON TM-T20 Receipt5`); **NFC-e desligada**; obs. de produto e de pedido ligadas; tradução ligada (herança do #100); *Nome e Telefone Opcional* + *Informar Número da Mesa*; senha `123`; sem produto de acréscimo; mensagem final padrão |
| Pagamentos | **os seis meios ligados** — é o que permite fechar pedido em Dinheiro, sem pinpad |
| Aparência | tema Branco, cor `#EF3F37`, logotipo e capa cadastrados, **nenhum slide** |
    50|| Cardápios | uma filial só → *Nenhum outro cardápio disponível* (virou texto, não imagem: regra 0) |
| Download | URL + os dois `.cmd` |

**Nada foi alterado na configuração do totem.** A única mudança de cenário foi a
foto dos setores (abaixo).

## O cenário montado: foto nos sete setores

Antes, os 7 setores estavam sem foto e os 67 produtos com foto. Para o par
"sem foto / com foto" ser prova e não montagem:

1. capturamos o cardápio do aparelho **antes** (imagem 10, coluna de texto);
    60|2. subimos foto nos **sete** setores pelo **Banco de imagens** do próprio
   sistema (`capturar.py fotos`, um termo de busca por setor);
3. capturamos o cardápio **depois** (imagem 13, tira de miniaturas).

Aprendizado de captura: foto recém-subida chega do S3 **depois** do texto. Sem
esperar `document.images` completarem, a miniatura sai como ícone de imagem
quebrada — por isso o `esperar_imagens()` no `capturar.py`.

A medição por interceptação (injetar/remover `s3Link` nas respostas) ficou só
no `fluxo-codigo.md`: ela provou a regra, mas não vira imagem publicável.

## Imagens (14)
    70|
Painel em 2160×1350 (1440×900 com DPR 1.5); aparelho em 1080×1920.

| Arquivo | Conteúdo |
|---------|----------|
| `01-aplicativos-card-totem.png` | Aplicativos → faixa Presencial → card **Totem** |
| `02-modal-configuracao-topo.png` | Totens contratados, abas, Meio de Consumo e Impressão |
| `03-modal-configuracao-meio.png` | Emissão Fiscal, Observação, Idiomas e Identificação do Cliente |
| `04-modal-configuracao-fim.png` | Senha Administrador, Acréscimo e Mensagem Final |
| `05-modal-pagamentos.png` | Os seis meios, a forma de recebimento e a engrenagem do TEF |
| `06-totem-pagamento.png` | Tela de pagamento do cliente, com 1% no Dinheiro e 5% no Pix |
    80|| `07-modal-aparencia.png` | Tema e cor, logotipo, capa e Adicionar slide |
| `08-totem-espera.png` | Tela de espera: FAÇA SEU PEDIDO e as bandeiras |
| `09-modal-download.png` | URL do totem, Copiar e os dois `.cmd` de modo kiosk |
| `10-totem-cardapio-sem-foto-setor.png` | Coluna da esquerda em **texto** (setor sem foto) |
| `11-painel-setor-foto.png` | Cadastro do setor: ADICIONAR FOTO, chave Presencial, Cardápios |
| `12-painel-foto-setor-banco.png` | A janela da foto: arrastar imagem ou Banco de imagens |
| `13-totem-cardapio-com-foto-setor.png` | A mesma coluna com **miniaturas** (setor com foto) |
| `14-totem-pedido-feito.png` | Pedido concluído: erro de impressão, mensagem final e a senha |

Recortes do `annotate.py`:

    90|- `MODAL` — o modal do totem vai de x=410 a x=1755 e de y=95 a y=1250; faixa
  branca de 150 px à esquerda para as etiquetas;
- `TOTEM_SEM_BARRA` — o aparelho sem a barra de cima, porque o logotipo
  retangular (350×112) sai cortado no espaço quadrado dela;
- as duas capturas do cardápio inteiro (10 e 13) ficam **sem recorte**: a coluna
  e a grade precisam aparecer juntas para o par funcionar.

As imagens 6 e 14 nasceram no `capturar.py` do **#123** (é ele que fecha o
pedido de verdade) e foram copiadas para cá.

## Decisões de texto
   100|
- **Par painel → cliente** em três seções (Pagamentos, Aparência, pedido
  concluído). É o que diferencia este manual de um inventário de campos.
- O desconto de 1% e 5% da tela de pagamento **não é do totem**. Conferido nas
  duas telas do sandbox: *Dinheiro* 1% em **Cadastros → Formas Recebimento** e
  *PIX Online* 5% em **Cardápio Digital → Pagamento Online**. A mesma forma
  *Dinheiro* em **Cardápio Digital → Formas Recebimento** está com 5% e **não**
  foi o valor aplicado — por isso o manual cita os dois caminhos exatos.
- O **erro de impressão** da imagem 14 ficou na foto e virou explicação: a loja
  de teste não tem impressora no aparelho, e o pedido vai para a cozinha do
   110|  mesmo jeito. Esconder o erro daria uma imagem mais bonita e um manual pior.
- A regra da foto foi escrita como **decisão de conjunto** ("ou todos os setores
  têm foto, ou nenhum") e com o aviso de que **produto** sem foto não vira lista:
  vira cartão com imagem quebrada.
- A URL é tratada como senha, porque ela carrega o `aaToken` da filial.
- A aba *Cardápios* não tem imagem (o sandbox mostraria "Nenhum outro cardápio
  disponível" — tela vazia, regra 0 das boas práticas).

## Scripts

- `capturar.py` — etapas `aplicativos`, `configuracao`, `pagamentos`,
   120|  `aparencia`, `cardapios`, `download`, `setor`, `fotos` (sobe as fotos) e
  `aparelho` / `aparelho-com-foto`. O painel usa `storage_state` em
  `/tmp/bf3-auth.json`; o aparelho abre em contexto próprio, 1080×1920, com
  `service_workers="block"` (sem isso o PWA serve tela cacheada).
- `annotate.py` — setas e números em pixels da imagem já recortada.

As abas do modal **não são `role=tab`**: são elementos com o texto da aba, e o
que funcionou foi clicar por JavaScript filtrando altura < 60 px.

## Status

   130|Concluído — 14 imagens, manual, fluxo de código e prompt de publicação.
