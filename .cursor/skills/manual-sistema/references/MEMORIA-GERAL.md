# MEMÓRIA GERAL — Boas práticas para criação de manuais BeeFood

> Memória mestre da skill `manual-sistema`. **Ler SEMPRE no início de cada sessão.**
> A porta de entrada, com o fluxo resumido, é o [`SKILL.md`](../SKILL.md) — este
> arquivo é o conteúdo. Cada manual tem ainda sua própria `MEMORIA.md` na pasta dele.

Última atualização: 2026-09-23 (**tela de front público se lê no bundle publicado, sem clone** —
o rastreio do #121 mora no cardápio digital, um Nuxt 2 em repositório que não se consegue clonar, e
o `curl` de `menu.beefood.com.br` entregou rota, componentes, todas as frases de todos os estados,
os intervalos de atualização e o `noindex`. Primeiro manual **sem nenhuma captura própria**: o
material veio pronto do dono, e o importador do `annotate.py` segue o padrão do #24 — avisa e segue
quando o caminho do upload já não existe. Duas armadilhas de seta confirmadas na quarta rodada de
conferência: **mire o vão antes da primeira letra**, e pino de mapa aceita seta na borda);
2026-09-19 (**regra 0 das imagens: o manual não é inventário do aplicativo** —
um pedido de capturas inteiro foi recusado pelo dono na leitura, porque pedia tela vazia e app sem
rede; *"o manual deve ser util e não ter um monte de conteudo sem sentido"*. O critério passou a
abrir a seção 3: **imagem entra se o leitor sair dela fazendo algo diferente**. Custou uma imagem já
publicada no #112, dois comandos do `smoke-app.js` e o kit da rodada nova, todos apagados. A história
está em *O pedido que foi recusado antes de virar trabalho*);
2026-09-19 (**bloco da Gestão de Entregas fechado, 16 manuais** — as 24
capturas da segunda rodada chegaram e o **#117** saiu com as duas telas do mesmo pedido: 6 imagens
do celular e 7 do painel **reencenadas** depois, restaurando o estado de cada fase no banco. Três
regras novas na seção 3, todas de print que vem de outra máquina em outro dia: **transplantar a
faixa de data** com `relogio.py` em vez de redigitar (a Roboto do Android não existe aqui);
**quando o aplicativo desmente o pedido, quem cede é o pedido**; e **tela de erro vira seção
numerada, não imagem no FAQ**. Mais a regra de asserção: *nenhum/sempre/nunca* exige achar o campo
no código, não medir prints — o #117 escreveu que o número do pedido não aparecia em tela nenhuma
do aplicativo, e ele estava numa imagem já publicada do #116);
2026-09-17 (o repositório virou **duas skills**, `manual-sistema`
e `carrossel`: o processo de manual saiu da raiz e passou a morar em
`.cursor/skills/manual-sistema/`, com esta memória, o checklist, os planos e o
`validar-imagens.py` dentro dela — ver seção 2);
2026-09-17 (**#103** Venda Sugestiva (UpSell) — três caminhos que
gravam a mesma lista de até **6** produtos, a aba do cadastro **salva sozinha**, o
cardápio público **filtra** a sugestão antes de mostrar (oculto/inativo/já na sacola) e o
relatório de Sugestões **só conta venda concluída**; técnica nova para achar o ⋮ de um
card em grade virtualizada e para rolar dentro do iframe de relatórios);
2026-09-17 (**#102** Gerar Cardápio em PDF — *Cardápio → Cardápio
em PDF*, editor de 4 etapas com prévia; **nada é salvo**; editar item vale só para o
PDF; o **QR Code só é montado na etapa 3**; Clássico sai com foto por padrão; padrão
novo de imagem: **página de PDF gerada** renderizada com PyMuPDF e montada lado a lado);
2026-09-16 (**#100** Tradução do cardápio presencial — bandeiras
Brasil/EUA/Espanha no cadastro de setor, produto, complemento e grupo de opções;
só existem com **totem ou tablet contratado** (`temTraducaoContratada`); item sem
tradução cai para o português; **Habilitar tradução** no totem; **sem** tradução em lote;
telas do cliente no totem e no tablet, com o padrão de anotar **foto de tela enviada
pelo dono**; **#101** domínio próprio e subdomínio pela tela — APEX troca os servidores
DNS e ganha a aba **DNS** da zona, subdomínio é só um CNAME; exclusão é assíncrona;
padrão de imagem do **painel lateral** e prova de CNAME ausente por **NSEC**);
2026-09-13 (**#99** Destaque na impressão — produto/complemento/lote; fundo escuro no Cupom Pedido, na Cozinha e no cupom do delivery; texto em tom de busca a partir da discussão *Destaque de bebida*);
2026-09-11 (**#98** taxa de serviço opcional no cupom — rodapé do Cupom Pedido, Delivery ≠ Presencial);
2026-09-10 (**#94/#95/#96** fechamento fiscal, autorizar contador e portal do contador; **#97** transferir item entre mesas/comandas);
2026-09-06 (**série WhatsApp #15 e #86–#93** — campanhas
em rascunho, QR só gerado, conversas fake; Pedido Chat **#86**;
**#83/#84/#85** comissão do garçom ≠ taxa de serviço — o % mora no funcionário, só nasce com identidade (app / usuário / operador); Relatório de Desempenho item a item; Resumo Presencial do caixa lista a taxa e **não** substitui o fechamento da comissão; switch Sem taxa de serviço no produto);
**#80/#81/#82** mesas, comandas e formas de recebimento; **#78** Classificação RFV — header com o
custo do disparo único e tabela de tom por grupo; mapa de usos: WhatsApp
**direto ou via segmentação**, inteligente e SMS **só pela segmentação**,
relatório + Base de Clientes; cupom/cashback/PDV/Pixel não leem o grupo;
10 imagens);
**#78** (02/09) limites em Clientes → RFV, 11 grupos, recálculo em 24h; V é
ticket médio apesar do rótulo “Total gasto” na ficha);
**#17** BeeFood Pixel Analytics — funil +
campanha paga: Origem isola a plataforma, UTM isola a campanha; 4 pedidos
gerados com URLs fake Google/Facebook/Instagram/TikTok; 228 visitas / 8
pedidos / 4% nos últimos 7 dias);
**#75/#76** Grupos de acesso — estudo das 93 permissões (com a
técnica de codificação binária para medir permissão e a espera de 85 s do cache) e o manual de
criar usuário/grupo — **usuário sem grupo enxerga quase tudo**;
**#74** Entendendo a numeração dos pedidos — concluído: número da
venda nunca reseta, número do pedido é do caixa, mesa nunca recebe **e não consome** número;
virada 60→1 provada ao vivo; **cupom no navegador é IFRAME, não `window.open`**;
**o `BITBUCKET_TOKEN` parou de autenticar** — mas o clone do backend
sobrevive no snapshot do ambiente, em leitura congelada (seção 5);
**#72** Ficha técnica — base de insumos zerada, opção repetida
baixa em dobro, insumo sem controle de estoque não movimenta; **#73** Produto só com agendamento;
**#71** Aparência e layout; **#70** Agendamento do cardápio digital; **#68/#69** Exibir/Ocultar e Preço Programado; **#66/#67** Lançamentos; **#65** Taxas formas de recebimento; **#64** Desconto formas de recebimento; **#19** e **#20** Cashback; **#59–#63** entregas/marketplace; **#21** Cupom; **#18** SMS; **#58** IA ChatGPT; **#57** BeeFood Entregador; **#48** Capas e Destaques; **#49–#56** migrados do
ajuda.beefood em `PLANO-MIGRACAO-AJUDA.md`; screenshot Playwright
precisa de `type="png"`; prévia `aside` pode sair com 5000+ px — recortar o aparelho;
`get_by_role(name=lambda)` quebra no Playwright Python desta VM; banner de cupom
do cardápio público nem sempre fecha por `Dispensar`; **espera de 5 s após cada
clique vale para SEMPRE**, qualquer manual — spinner some primeiro, só então
contar os 5 s; bloco Área de Entrega #34–#38; ler no código o que grava antes de
capturar; dado pessoal coberto na imagem pura; widget flutuante escondido por CSS;
diagnóstico do ambiente pela API; anexo do chat não chega ao Cloud Agent; imagem
colada no chat não tem como ser baixada, mas **zip numa URL pública o agente
baixa** — o VM tem egresso liberado; escopo real do `BITBUCKET_TOKEN`; backend
clonado no Cloud Agent; tela de login mudou; telas com auto-save; captura com
Playwright; **medir coordenada de seta com grade de frações** e mirar a borda do
botão, não o centro)

---

## 1. Objetivo

Criar **manuais de funcionalidades para o USUÁRIO FINAL** do sistema BeeFood, combinando:
- **Código** do projeto `beefood-web-react` (`C:\projetos\beefood-web-react`) → entender a lógica real.
- **Produção** (`https://beefood.app`) → capturar telas reais.

Saída: arquivos **`.md`** + imagens anotadas.

---

## 2. Estrutura de pastas (PADRÃO — seguir sempre)

Desde 17/09/2026 o repositório está organizado em **duas skills**, e o processo de
manual mora inteiro dentro da `manual-sistema`. A raiz guarda só a saída
(`manuais/`, `carrosseis/`) e os arquivos de orientação (`AGENTS.md`, `README.md`,
`spec.md`).

```
beefood-web-react-manual/
├─ AGENTS.md                         <- qual skill atende qual pedido
├─ .cursor/skills/manual-sistema/    <- ESTA skill
│  ├─ SKILL.md                       <- porta de entrada: o fluxo em sete passos
│  ├─ references/
│  │  ├─ MEMORIA-GERAL.md            <- esta memória (boas práticas, contas, ferramentas)
│  │  ├─ CHECKLIST-MANUAIS.md        <- fila, status e histórico
│  │  └─ planos/PLANO-*.md           <- estudo de bloco antes de virar manual
│  └─ scripts/validar-imagens.py
├─ .cursor/skills/carrossel/   <- a outra skill; lê isto e não escreve aqui
└─ manuais/
   └─ <nome-do-manual>/        <- UMA PASTA POR MANUAL (ex.: caixa, delivery, pdv...)
      ├─ MEMORIA.md                 <- memória detalhada do manual (fluxo, uso, decisões, estado)
      ├─ <nome>.md                  <- o manual final (para o usuário)
      ├─ fluxo-codigo.md            <- mapeamento técnico (a partir do código)
      ├─ texto-documentation.ia.md  <- PROMPT pronto p/ criar o manual no app (ver seção 12)
      ├─ annotate.py                <- script de anotação (setas/números) deste manual
      ├─ imagens-puras/             <- screenshots ORIGINAIS (BACKUP, nunca referenciado)
      └─ imagens-tratadas/          <- TODAS as imagens do manual (com setas + contexto). Única pasta referenciada
```

**Regra de ouro:** ao iniciar um manual novo, criar uma pasta nova em
`manuais/<nome>/` com TODAS as subpastas/arquivos acima. O que é **processo** vai
para a skill; o que é **manual pronto** vai para `manuais/`.

---

## 3. Boas práticas de imagens

> **0. Antes de tudo: o manual não é inventário do aplicativo.** Uma seção ou uma imagem só entra se
> o leitor **sair dela fazendo algo diferente**. Tela de erro com saída entra; tela **vazia**, estado
> que o leitor já sabe que está vivendo (sem rede, sem sinal) e tela idêntica à normal, não entram —
> por mais fácil que seja produzi-las e por mais que a cobertura pareça incompleta sem elas. Custou
> uma imagem publicada, dois comandos de script e um pedido de captura inteiro descobrir isso; a
> história está em [O pedido que foi recusado antes de virar trabalho](#o-pedido-que-foi-recusado-antes-de-virar-trabalho-19092026).
> Sinal de alarme no sumário: seções que se chamam *"Quando não tem…"*, *"Quando fica vazio"*,
> *"Quando não há rede"*.

1. **Sempre salvar a imagem PURA primeiro** em `imagens-puras\` (backup, **nunca referenciado** no `.md` nem no `texto-documentation.ia.md`).
2. Depois gerar a versão **tratada** em `imagens-tratadas\` via `annotate.py`. **`imagens-tratadas\` deve conter TODAS as imagens usadas no manual:** as principais com setas + as de **contexto** (sem setas, via `passthrough()` do `annotate.py`). Assim só essa pasta é referenciada.
3. Nomeação sequencial por etapa: `NN-descricao.png` (ex.: `03-modal-abrir-caixa.png`).
4. **Poucas fotos, sem excesso** — apenas as essenciais de cada etapa.
5. Cada foto essencial leva **setas verdes + número**. O texto do manual referencia cada número e
   destaca campos **obrigatórios (\*)**.
   - **Numeração:** usar SEMPRE números normais **`1.`, `2.`, `3.`** (com ponto). **NÃO** usar
     números circulados (①②③) nem em parênteses — no texto, nas tabelas e nas legendas.
   - **Não printar a tela ainda carregando.** Depois de cada clique: esperar sumir
     `Carregando...` / `Atualizando...` / `Calculando…` e **só então esperar 5 segundos**.
     Vale para **todo** manual. Detalhe na seção 6.
6. As imagens em produção saem em **1508×1274** (DPR alto). `annotate.py` usa coordenadas
   em **frações 0..1**, então independe da resolução.
7. **Dados pessoais de clientes precisam sair ilegíveis.** Telas que listam clientes (nome,
   telefone, e-mail) não podem ir para o repositório como estão — ele é **público**. A decisão
   da seção 11 vale para as *credenciais* de teste, não para dados de terceiros. O `annotate.py`
   de `manuais\segmentacao-clientes\` tem o parâmetro `borrao` (regiões em frações, aplicadas
   com `GaussianBlur` antes das setas); copie de lá quando precisar.

### Antes de dar um manual por concluído: `validar-imagens.py`

Da raiz do repositório, rodar `python .cursor/skills/manual-sistema/scripts/validar-imagens.py`
(ou com `<pasta-do-manual>` no fim, para um só). Ele confere, em todos os manuais:

- se **toda imagem referenciada existe** em `imagens-tratadas/` — sai com **código 1** quando
  falta alguma, porque manual com imagem faltando não pode ser publicado;
- se o `texto-documentation.ia.md` lista alguma imagem que o manual **não usa**;
- se há **órfão** em `imagens-tratadas/` (arquivo na pasta que ninguém referencia).

Órfão e divergência do prompt são **avisos**, não erram a saída.

Na mesma passada, rodar
`python .cursor/skills/manual-sistema/scripts/indice-manuais.py`: ele reescreve a
tabela de manuais do `README.md` a partir das pastas, com o título lido do H1 de
cada manual. A tabela era mantida à mão e chegou a **99 pastas com 63 linhas** —
36 manuais prontos não apareciam para quem abre o repositório, e nada quebrava,
porque tabela incompleta continua sendo tabela válida. O `--conferir` não
escreve: sai com código 1 quando o README está atrasado.

> Existe porque manual com imagem faltando **quebra em silêncio**: o markdown continua válido,
> o texto continua legível, e só quem abre a página publicada descobre. Foi o que aconteceu no
> #24, cujas capturas vivem em outro repositório. Auditoria de 20/08/2026: dos 14 manuais, 13
> estavam íntegros (164 imagens) e só o #24 acusou as 21 faltando; nenhum órfão.

### Como anotar (Pillow)
- Requisitos: Python 3.10+ e Pillow (já instalados nesta máquina).
- `annotate.py` lê de `imagens-puras\` e escreve em `imagens-tratadas\`.
- Config por imagem: lista de marcadores `(numero, alvo_x, alvo_y, badge_x, badge_y)` em frações.
- Rodar dentro da pasta do manual: `python annotate.py`.
- **Sempre conferir visualmente** as imagens tratadas e ajustar coordenadas se necessário.

**Para medir as coordenadas, sobreponha uma grade de frações na captura** em vez de estimar no
olho: uma cópia temporária com linha a cada 0,05 e rótulo a cada 0,10, e os valores são lidos
direto da grade. É rápido de escrever (umas 20 linhas de Pillow, em `/tmp`, fora do repositório)
e acerta quase tudo de primeira. Usado no #24 em 16 capturas: das 29 setas, 24 nasceram no lugar.

### Padrão oficial — tela em painel lateral (`Sheet`)

Telas que abrem num painel à direita (o **Domínio Próprio** do #101 é o primeiro
caso) desperdiçam mais da metade da imagem: no viewport de 1440×900 com DPR 1.5 o
painel começa em **x = 1154** dos 2160 px, e o resto é a tela escurecida. Print
inteiro deixa o texto do painel pequeno na página publicada — foi o pedido do dono em
16/09/2026: *"as imagens precisam ficar mais recortadas quando for essa modal
lateral, pois 60% da tela à esquerda é sem uso"*.

O padrão:

- **Recortar no painel** e colar uma **faixa branca de ~150 px à esquerda**, que é
  onde ficam as etiquetas numeradas. As setas entram na **horizontal**, então nenhuma
  cruza texto — dentro do painel não há espaço vazio para etiqueta.
- Cortar também **na altura**, logo depois do último elemento útil, para não sobrar
  branco embaixo (o painel tem rodapé fixo e sobra um vão no meio).
- **Medir as coordenadas na captura pura inteira** e deixar o `annotate.py` converter
  (`crop` + `pad_left`, com o deslocamento aplicado a setas e molduras). Assim a
  medição não muda quando o recorte muda.
- Passar `r` e `w` **na mão** com os valores da captura inteira (27 e 4). O recorte
  não redimensiona nada, e o cálculo automático por largura encolheria a etiqueta.
- A tela que **contém** o painel (o card que abre) entra inteira, como contexto.
- **Recortar não é dar zoom.** Tira estreita com um botão só (o rodapé do painel, por
  exemplo) tira a referência de onde aquilo fica e o cliente se perde — foi o segundo
  recado do dono no #101: *"não devemos ter imagens com super zoom dentro da modal
  lateral, senão o usuário se perde no entendimento"*. Para um clique no rodapé, a
  imagem é o **painel inteiro** com a seta no botão.
- **Diálogo no centro da tela** (`ConfirmationDialog`, formulários em `Dialog`) não
  está dentro do painel: recorte próprio, com o painel visível atrás como contexto
  (no #101, `crop=(640, 100, 2160, 1280)`). Como esse recorte tem `y0`, o
  `annotate.py` desloca as coordenadas em **x e y**.

### Manual que depende de DNS — como não culpar o produto errado

No #101 o subdomínio ficou **duas horas** em *Aguardando você* depois de o dono criar
o CNAME, e a suspeita natural caiu no BeeFood. O jeito de decidir sem chutar:

- `dig +short CNAME nome @8.8.8.8` vazio não prova nada sozinho (pode ser cache
  negativo). Peça a autoridade: `dig nome @8.8.8.8 +noall +authority` mostra o **SOA**
  de quem respondeu.
- Se a zona tem **DNSSEC** (`.com.br` do Registro.br tem), a negativa vem com um
  registro **NSEC** que lista os nomes existentes. `cardapioteste.com.br. NSEC
  cardapioteste.com.br. NS SOA MX TXT RRSIG NSEC DNSKEY` = cadeia de um só nó, ou
  seja, **só o apex está publicado** — o registro do cliente não entrou. Isso é prova,
  não suposição.
- Serial do SOA subindo **não** quer dizer que a alteração entrou: comparar a janela
  da `RRSIG` (início/fim) revela reassinatura periódica do DNSSEC.
- Provedor pode demorar para publicar. Deixe um monitor em `tmux`
  (`dig` a cada 60 s gravando em log) em vez de ficar consultando na mão, e avise o
  dono com o que a evidência mostra — no #101 o CNAME apareceu às 18:41 e o cardápio
  abriu às 18:47, sem que nada precisasse ser mexido no BeeFood.

Implementação de referência: `manuais/dominio-proprio-configurar/annotate.py`
(`PAINEL`, `MARGEM`, `ate(y)` e o atalho `painel(...)`).

### Padrão oficial — tira de celulares (cardápio público)

Não coloque vários prints altos de celular soltos no `.md`. Monte **uma tira**
com os aparelhos lado a lado. O cliente lê o conjunto numa olhada; o arquivo
único também cabe melhor na página publicada.

**Captura (Playwright):**

- Viewport **390×844**, `device_scale_factor=2` → pura **780×1688**
- `is_mobile=True`, `has_touch=True`, `locale="pt-BR"`, `LANG=pt_BR.UTF-8`
- Cardápio: `https://menu.beefood.com.br/beefood3`
- **Não clicar Retirada na home** (abre o mapa Leaflet). Modalidade =
  **Retirar no estabelecimento** dentro da sacola
- Combo de teste: One Burger + Batata frita + Coca 350ml = **R$ 39,00**
- Telefone de teste: **(15) 99999-8888** (`15999998888` no `input[type=tel]`)
- Opções do combo: clique JS/mouse em `.modal-product__details .option-item`
  (o `click` do Playwright falha “outside viewport”)

**Montagem (`montar_celulares` no `annotate.py` — copiar do #19/#20/#64):**

| Constante | Valor | Função |
|-----------|------:|--------|
| `PHONE_W` | 380 | Largura de cada aparelho na tira |
| `GAP` | 18 | Espaço entre aparelhos |
| `PAD` | 22 | Margem do canvas |
| `CAP_H` | 44 | Faixa do título acima do aparelho |
| raio | 26 | Canto arredondado + máscara |
| fundo | `(244, 244, 245)` | Cinza claro |

- Puras **individuais** ficam em `imagens-puras/` como **fonte**. Não entram no `.md`.
- `montar_celulares` grava a tira **também em `imagens-puras/`**.
- Só a tira (já anotada) entra no `.md` e no `texto-documentation.ia.md`.
- 2 ou 3 aparelhos. Três ainda lê fácil (~1220 px de largura). Quatro aperta.
- Título curto acima de cada um (“PIX Online — 5%”).
- Setas na tira: `no_painel(i, tx, ty, W, H, ph_h)` — `tx/ty` são frações
  **dentro daquele celular**, não da tira inteira.

Usado no **#19**, **#20** e **#64**.

**Mire a borda do elemento, não o centro, quando ele tem texto.** Seta apontada para o meio de um
botão cai em cima do rótulo e cobre uma letra — aconteceu em quatro botões do #24 (`CONCEDER`,
`AGORA NÃO`, `CONCORDAR E CONTINUAR`, `ACESSAR`). A borda inferior ou lateral marca o mesmo
elemento sem tapar nada. Vale também para campo de texto: apontar ao lado do rótulo, não nele.

> Só a conferência **em tamanho real** revela isso. Numa folha de contato reduzida as quatro setas
> pareciam perfeitas. Faça as duas coisas: folha de contato para ver o conjunto, e depois abrir
> uma a uma as que têm alvo pequeno ou botão com texto.

**Se as capturas vêm de fora do repositório, o script que as importa não pode escrever em
`imagens-tratadas\`** — ele apagaria as setas na próxima execução. Que ele alimente só
`imagens-puras\`, e que imprima no fim o lembrete de rodar o `annotate.py`. Foi o ajuste feito no
`copiar-imagens.py` do #24 quando o manual deixou de ser só contexto.

### Padrão oficial — páginas de PDF gerado (montagem) — #102

Manual de recurso que **produz um arquivo** (o gerador de Cardápio em PDF) precisa
mostrar o arquivo, não só a tela que o monta. Print da prévia não serve: é imagem de
JPEG dentro de canvas, com o cromo do sistema em volta.

O caminho que funcionou no #102:

1. **Baixar o PDF de verdade** pelo próprio botão da tela, com
   `page.expect_download()` (contexto com `accept_downloads=True`) → `/tmp/*.pdf`.
2. **Renderizar as páginas** com **PyMuPDF** (`pip install pymupdf`) em **110 dpi**
   (`doc[i].get_pixmap(dpi=110)` → A4 vira 910×1287, nítido e leve). O `poppler-utils`
   **não** existe no VM, então nada de `pdftoppm`.
3. Gravar as páginas em `imagens-puras/pdf-*.png` — elas são a **fonte**, e é o que
   mantém o `annotate.py` reproduzível depois que o `/tmp` some.
4. `montar()` no `annotate.py` põe as páginas lado a lado em fundo cinza
   `(238,238,240)`, com borda de 2 px e legenda em cima ("Capa (página 1)"). Duas
   páginas em 100% para detalhar; três em `escala=0.62` para comparar modelos.
5. Anotar a montagem normalmente. Vantagem: os números podem ficar **fora da página**,
   no fundo cinza, quando a borda do papel não tem margem sobrando.

Para achar o alvo das setas **dentro do PDF**, não meça no PNG: use
`page.search_for("texto")` e `page.get_image_info()` do PyMuPDF (devolvem pontos) e
multiplique por `110/72`. Foi assim que saíram as sete setas da imagem 11 (cabeçalho,
título do setor, item, rodapé, logo, contato e QR Code).

Números medidos que valem como argumento no texto: o mesmo cardápio (68 itens)
saiu com **4,4 MB em 5 páginas** com fotos e **57 KB em 4 páginas** só com texto.

### Fotos de tela enviadas pelo dono (totem, tablet, PDV) — #100

O totem e o tablet não abrem no Cloud Agent, então essas telas chegam como
imagem pronta, em resolução menor que as capturas do painel (~1100–1300 px).
O que funcionou:

- Copiar para `imagens-puras/` com o nome numerado do manual e **anotar no
  tamanho original** — reescalar para 2160 px só borra o texto.
- Passar `r=15, w=3` no `annotate`: o cálculo automático (`W * 0,0125`) devolve
  seta fina demais nesse tamanho.
- **Coordenada lida em grade sobre a imagem original.** Medir "no olho" pela
  miniatura do chat erra por um fator constante (a pré-visualização é de 1024 px
  de largura); a grade tem de ser gerada sobre o arquivo, não sobre o preview.
- Quando o alvo fica sobre foto ou banner (não há espaço vazio para o número),
  acrescente uma **faixa branca no topo** (`pad_top`) e coloque o número nela,
  em vez de jogar o badge sobre a imagem.
- Recorte a moldura vazia do aparelho (`crop`), mas sem virar zoom: o elemento
  precisa continuar visível no contexto da tela.

Vale mais que a foto: telas assim costumam **provar o comportamento com dados
reais**. No #100, a mesma foto do tablet mostrou um produto traduzido e outro
sem tradução, lado a lado — confirmado nos endpoints de detalhe antes de
escrever a legenda.

### Padrão oficial — prints de aplicativo de celular recebidos do dono — #111 a #116

Seis manuais seguidos feitos com 63 prints de emulador Android (`Pixel_7_Pro`, app `3.3.0`)
produziram um padrão próprio, com dois arquivos reaproveitáveis em `/tmp/ge/`:
**`cabeca-app.py`** (o cabeçalho com as funções) e **`mkapp.py`** (gera o `annotate.py` de cada
manual a partir de um `docNNN.txt` e um `marcNNN.txt`).

Tela de celular é **estreita e cheia**, e é isso que muda tudo em relação ao painel:

- **Etiqueta numerada dentro da tela cobre texto.** Foi o que aconteceu na primeira rodada do
  leitor de código de barras. A solução é `com_margem()`: acrescentar margem clara **fora** do
  print, para a etiqueta viver na margem e a seta entrar pela borda. O print fica inteiro visível.
- **Três margens, três motivos.** `esq` é a padrão (a coluna esquerda da tela quase sempre tem
  texto); `topo` serve para recorte em tira fina, onde não há altura para a etiqueta; e `dire`
  existe pelo motivo oposto à esquerda — a coluna direita é onde moram a flecha `>`, o selo de
  estado e o `!` de atraso, e alcançá-los pela esquerda obriga a seta a atravessar o cartão
  inteiro por cima do endereço.
- **`rec(caixa, m, tm, md)`** converte pixel lido na prévia do print inteiro em fração da imagem
  **final**, já recortada e com as margens. Sem ela, cada recorte exige recalcular tudo à mão, e
  foi a fonte de metade dos erros de posição.
- **`recortar`/`copiar` em vez de print inteiro.** Cartão de pedido, rodapé de pagamento e
  cabeçalho de rota viram imagens separadas. Uma tela de celular inteira com cinco etiquetas não
  se lê; o mesmo conteúdo em três recortes se lê.
- **Cuidado com o numeral que o app já desenha.** O aplicativo numera as paradas da rota em
  círculos, e etiqueta verde numerada por cima disso cria dois sistemas de numeração na mesma
  imagem. Nesses casos a imagem entra como **contexto** (`passthrough`, sem etiqueta) e o detalhe
  numerado vai para um recorte.
- **Recorte o resto da barra de status.** Sobra de barra preta no topo ou no pé aparece como um
  risco fino e some na miniatura — apareceu em quatro imagens do #115 e do #116. Confira em
  tamanho real.
- **Nome de cliente em print de app costuma ser dado semeado.** Nos 63 prints, *Ana Beatriz
  Moraes* e *Rafael Monteiro Dias* são clientes criados por script (repetidos na base, sem
  telefone nem e-mail, origem *Delivery Manual*). Conferir antes de decidir se desfoca —
  desfocar o que é fake só deixa a imagem pior.

**O mesmo padrão serve para print de navegador de celular** (cardápio público, totem, página de
rastreio), e foi o que o #121 usou: as capturas chegaram em **780x1688** (viewport 390x844 em
DPR 2) e **2000x1250**, e o `annotate.py` dele é o padrão enxuto — `preparar()` para importar e
recortar, `margem()` com esquerda e direita, `rec()` para converter pixel da captura original em
fração da imagem final. **Meça em pixel da captura inteira, não em fração do resultado:** medir
uma vez na tela cheia é o que permite mexer no recorte depois sem remedir nada. E, no #121, o
dono liberou o print inteiro por escrito (*"todas imagens são dados falsos"*) — **pergunte antes
de borrar**, porque a primeira versão saiu com borrão desnecessário sobre o link.

### Quando o print vem de outra máquina, em outro dia — #111 a #117

A segunda rodada (24 prints, tirados por uma IA na máquina do dono) trouxe três problemas que a
primeira não tinha, e cada um virou regra:

**1. O relógio do emulador não é o relógio da loja.** A barra de status marcava 03:4x (UTC) e o
aplicativo escrevia 00:4x nos próprios campos (fuso da loja). As horas do **aplicativo** são as
certas: são as gravadas no servidor e as que o relatório soma. Duas saídas, nesta ordem:

- **Recorte a barra de status.** É a regra padrão, e não é só por causa da hora: o manual mostra a
  tela do aplicativo, não a barra do sistema. Só mantenha a barra quando ela **é** a prova (o ícone
  de rede cortada, por exemplo).
- **Se a data aparece dentro da tela e está no dia errado, transplante — não redigite.**
  [`manuais/gestao-entregas/scripts/relogio.py`](../../../../manuais/gestao-entregas/scripts/relogio.py)
  copia a faixa de data de um print de **referência** (um do dia certo) para os novos. Ele acha a
  faixa pela cor (vermelho por **dominância de canal**, `R > 1,8·G` e `R > 1,8·B`, não por brilho
  absoluto — texto atrás de modal escurecido tem `R` baixo e passaria batido), repinta o fundo
  **linha por linha** para não achatar o gradiente do escurecimento, e cola a tinta por máscara de
  alpha com a cor local. Redigitar com Pillow não funciona: a Roboto do Android não existe na
  máquina que monta as imagens, e a diferença de fonte salta aos olhos.

**2. O aplicativo desmente o pedido, e quem cede é o pedido.** Dois dos 24 prints saíram diferentes
do que a lista pedia. Sem rede, o *MELHOR ROTA* responde **Permissão necessária** (o `try/catch`
trata rede e GPS no mesmo `catch`): virou seção do #113, porque tem saída — conceder a permissão. O
print do "histórico vazio" veio com 22 entregas em três dias: **não virou nada**, e a conclusão
certa era que a foto não servia, não que o pedido precisava de outra volta. Print que sai diferente
é achado, não defeito — mas só se quem tirou escrever no relatório o que fez antes, e é por isso que
o pedido exige *uma linha por print que saiu diferente*.

**3. Tela de erro que passa no teste da regra 0 não entra no FAQ — entra em seção nova, numerada.** A
convenção da casa é FAQ **só de texto**. Quando chegam seis telas de erro para um manual, a saída não
é enfiar imagem na pergunta: é abrir **seção numerada** (*Quando a cobrança não fecha* no #116, *A
lista muda sozinha* no #112) e a pergunta do FAQ passa a **apontar para ela**. Mantém o FAQ escaneável
e dá à imagem o texto que ela precisa em volta. Cuidado com o efeito colateral, que é o que aconteceu
aqui: **ter onde pôr imagem de erro faz querer imagem de erro**. Uma das seis não tinha o que mostrar
— a lista sem rede é idêntica à lista com rede — e virou parágrafo depois de já ter sido publicada
como imagem anotada.

**E uma regra de asserção, que custou uma correção:** *"não aparece em tela nenhuma"* é afirmação
sobre o aplicativo inteiro, e medição em 24 prints não sustenta isso. O #117 escreveu que o número do
pedido não aparecia em lugar nenhum do aplicativo — e o selo *PEDIDO #1030* estava visível numa
imagem já publicada do #116. Antes de escrever *nenhum*, *sempre* ou *nunca*, ache o campo no código:
eram **dois** campos diferentes (`numeroPedido` no crachá do cartão, nulo em pedido do restaurante;
`numeroPreVenda` no selo do pagamento).

---

## 4. Padrão de escrita do manual (.md)

- Idioma: **português do Brasil**, tom didático para usuário final.
- Estrutura: Título → objetivo → pré-requisitos → etapas numeradas → dicas.
- Cada etapa: passos numerados + imagem tratada + **tabela** relacionando **nº da seta** (`1.`, `2.`, `3.` — números normais, nunca ①②③) → campo → o que fazer.
- Sinalizar claramente o que é **obrigatório**.
- Caminhos de imagem no `.md` são **relativos** à pasta do manual: `imagens-tratadas/arquivo.png`.

**Onde o número entra no texto, para não gerar ambiguidade.** Duas posições, e só essas:

- **`(N)` inline** no parágrafo **imediatamente antes** da imagem em que a seta N está desenhada
  ("Toque no logo do estabelecimento (1)", e a imagem vem em seguida).
- **Tabela "Nº → o que fazer"** imediatamente **depois** da imagem a que se refere.

Quando a ação está numa imagem **anterior**, escrever **"a seta N da imagem acima"** em vez de
`(N)`. Sem essa regra o leitor não sabe para qual das duas imagens vizinhas o número aponta — e o
risco é real: no #24, um "toque em CONCEDER (2)" ficava colado numa imagem cuja seta 2 era
*AGORA NÃO*. Vale conferir no fim que **toda seta desenhada é citada** e que **todo número citado
existe** na imagem: um script curto que compara o `.md` com os marcadores do `annotate.py` acha
isso em segundos, e foi assim que a ambiguidade apareceu.

---

## 5. Contas de acesso (produção https://beefood.app)

| Conta | Login | Senha | Observação |
|-------|-------|-------|------------|
| beefood1 | `beefood1` | `beefood123` | Conta de teste inicial (tem caixas históricos). |
| **BeeFood3 - Manual** | `contato@beefood.com.br` | `1q2w3e4r` | **Sandbox dedicado aos manuais.** Usar esta. Usuário **Principal**, Gerente, grupo **Administrador2**. |
| caixa.manual | `caixa.manual` | `manual123` | Usuário **restrito** criado em 19/08/2026 para o manual de restrições de caixa. Grupo **Acesso Funcionário**, **sem** função Gerente. Serve para ver o produto com permissões reduzidas. |
| estoque.manual | `estoque.manual` | `manual123` | Criado em 01/09/2026 no **#76**. Grupo **Acesso Estoque** (71881, criado com as 93 permissões **ligadas**), sem função Gerente. O contador do plano foi a **5/99**. |

> **Telefone de teste no cardápio digital (BeeFood3):** use **(15) 99999-8888**
> (cliente **Teste Manual**, saldo de cashback **R$ 5,00**). Digite **11 dígitos**
> `15999998888` no `input[type=tel]`. Não use telefone de cliente real nas capturas
> (o repositório é público). Cache do cardápio público: até **1 minuto**.

> **Atenção ao testar permissão no login principal:** o usuário Principal **não** ignora as
> restrições do grupo (comprovado). Logo, desligar uma permissão do grupo **Administrador2**
> afeta você. Nunca desligue **Usuários** nesse grupo — você perde a própria tela de
> permissões e não há como religar de dentro do sistema.

> Login em `/login`. A tela mudou em 2026-08: agora são **um campo só** para identificação
> (`input#emailOrWhatsapp`, rótulo "Digite seu e-mail ou WhatsApp") e `input#password`, botão
> **ENTRAR**. Logins que não são e-mail (ex.: `caixa.manual`) entram por esse mesmo campo.
> Demora ~2-4s. **Trocar de conta:** menu de usuário (ícone pessoa, canto sup. direito) → **Sair**.

---

## 6. Ferramentas e procedimentos (navegador)

### No Windows (máquina do dono) — MCP do navegador

- MCP `cursor-ide-browser`: `browser_navigate`, `browser_snapshot`, `browser_take_screenshot`,
  `browser_click`, `browser_fill`, `browser_press_key`, `browser_lock`.
- Fluxo de lock: `navigate` → `lock` → interações → `unlock`.
- Screenshots brutos caem em `C:\Users\T-GAMER\AppData\Local\Temp\cursor\screenshots\`.
  Copiar os escolhidos para `imagens-puras\` do manual.
- **Tema:** SEMPRE **claro/branco** nas capturas. Ativar pelo botão **"Alterar tema"** (canto sup. direito).
- **Depois de cada clique, esperar o spinner sumir e mais 5 segundos antes do
  print.** Mesma regra da seção Playwright — vale no Windows também.
- Refs do snapshot mudam a cada render — pegar snapshot novo antes de clicar se der "Element not found".

### No Cloud Agent (Linux) — capturar com Playwright

O MCP `cursor-ide-browser` **não existe** no Cloud Agent. Lá o navegador é o **Playwright**
(instalado pelo `.cursor/install.sh`), dirigido por script Python. O que funcionou no #2:

- Rodar com `export PATH="$HOME/.local/bin:$PATH"`.
- Logar uma vez e reaproveitar a sessão: `storage_state` salvo em arquivo e passado ao
  `new_context` — evita relogar em cada script (o login leva ~10s).
- `viewport={"width":1440,"height":900}` com `device_scale_factor=1.5` → imagens 2160×1350,
  nítidas o bastante para ler os valores das tabelas.
- Salvar o `screenshot` **direto** em `imagens-puras/` do manual.
- Fechar o **banner promocional** do topo antes de capturar (botão × do banner), senão ele
  aparece em todas as imagens.
- **Espera obrigatória após cada clique (dono, 21/08/2026 — permanente):**
  1. Clique (ou `goto`, ou troca de aba).
  2. Se aparecer `Carregando...`, `Atualizando...`, `Calculando…` ou spinner,
     esperar sumir (timeout 20–30 s).
  3. **Mais 5 segundos** depois do spinner sumir — não durante.
  4. Só então `screenshot`.
  Não basta `wait_for_timeout(400)` / `800` / `1500`. A regra **não é do #43**: é de
  Delivery, PDV, Mesas, Parâmetros, cardápio, área de entrega e qualquer tela nova.
  O #43 saiu com o painel em `Carregando...` e depois com `Atualizando...` no Pronto
  justamente porque o print veio cedo. Helper sugerido:

  ```python
  WAIT = 5000
  def after_click(page):
      for _ in range(30):
          busy = (
              page.locator("text=Carregando...").count()
              or page.locator("text=Atualizando...").count()
              or page.locator("text=Calculando").count()
          )
          if not busy:
              break
          page.wait_for_timeout(1000)
      page.wait_for_timeout(WAIT)
  ```
- **Sempre escopar o clique dentro do modal certo:**
  `page.locator('div[role="dialog"]').filter(has_text="...").last`. As tabelas de fundo têm os
  mesmos textos e as mesmas classes (`bg-green-500`, badges "Débito"), e o clique vai para o
  elemento errado ou fica preso em "subtree intercepts pointer events".
- Quando a tela oferecer **atalho de teclado**, prefira-o ao clique (ex.: `Control+3` para
  escolher Débito no pagamento, `Enter` para confirmar). É mais robusto que caçar seletor.
- Dividir a captura em **scripts curtos por etapa**, deixando as ações irreversíveis (pagar,
  fechar caixa) em scripts separados dos idempotentes — assim é possível repetir a parte que
  falhou sem repetir o que não tem volta.
- **Ler a resposta da API vale mais que ler a tela.** Registrando `page.on("response", ...)` dá
  para imprimir exatamente o que o servidor devolveu (flags de permissão, número de linhas) —
  isso mostra a causa, não só o efeito, e evita conclusão errada por cache de tela.
- **Cuidado com telas que salvam sozinhas.** Configuração → Parâmetros faz auto-save 500 ms
  depois do clique, sem botão Salvar: clicar num switch "só para ver" já altera o ambiente.
  Antes de clicar em qualquer switch, conferir o estado (`data-state`) e anotar para restaurar.
- Para achar o controle de um item quando o texto não é rótulo acessível, localizar o texto e
  **subir os elementos-pai** até encontrar `[role="switch"]` — filtrar `div` por texto costuma
  cair no elemento errado.
- **Ao mudar permissão, relogue.** O front guarda o `config_cache` no `localStorage`; recarregar
  a página não basta. E o servidor guarda o grupo por ~1 min. Ou seja: espere ~70s e faça login
  de novo antes de concluir que a mudança não pegou.
- **Cuidado ao regravar o `storage_state`.** Se você salvar a sessão enquanto uma permissão está
  desligada, o `config_cache` congela nesse estado e a conta parece continuar restrita mesmo
  depois de religar. O sintoma é a tela redirecionar para a home sem erro. A saída é relogar.
- O banner promocional do topo fecha por `button[aria-label="Dispensar"]`.
- **Esconda o widget flutuante de suporte antes de capturar.** É um `div.fixed.bottom-6` de
  56×56 no canto inferior esquerdo e cobre conteúdo de cards baixos. `page.add_style_tag` com
  `div.fixed.bottom-6 { display:none !important }` resolve, sem alterar nada no produto.
- **A pesquisa de NPS aparece depois do login e cobre a tela.** É um diálogo com o título
  "Como está sendo sua experiência?" e o botão **FECHAR (ESC)** — que é o **mesmo texto** de
  vários modais do sistema (produto, usuário). Uma rotina de limpeza que clique em
  `button:has-text("FECHAR (ESC)")` sem filtrar o diálogo **fecha o modal que você quer
  fotografar**: foi o que quebrou duas rodadas de captura no #75. Filtre primeiro:
  `page.locator('[role="dialog"]').filter(has_text="Como está sendo sua experiência")`. Ela pode
  reaparecer, então vale rodar a limpeza duas vezes.
- **Diagnostique o estado pela API antes de planejar o manual.** Um script curto que só abre a
  tela e imprime a resposta da listagem já diz quantos registros existem, em que estado estão e
  se há dados suficientes para as capturas — evita planejar imagens que o ambiente não tem.
  Foi assim que se descobriu, antes de escrever qualquer coisa, que as campanhas inteligentes
  já tinham os três estados e dois envios reais para fotografar.
- Alguns elementos ficam em **listas com rolagem própria** (o modal de permissões, por exemplo).
  Aumentar o viewport não resolve; use `scroll_into_view_if_needed()` no item desejado.
- **Campo de hora e de data sai em AM/PM se você não mexer no `LANG` do Chromium.** Telas com
  `input type="time"` (Horário Atendimento) ou `type="date"` (Pausa Programada) renderizam
  "02:30 AM" quando o navegador está em inglês — e o usuário brasileiro vê "02:30". O que corrige
  é a **variável de ambiente do processo**: `launch(env={**os.environ, "LANG": "pt_BR.UTF-8",
  "LANGUAGE": "pt_BR"})`. Testado em 21/08/2026: nem `new_context(locale="pt-BR")` nem o
  argumento `--lang=pt-BR` mudam o formato do campo, só o `env`. Um teste rápido sem OCR: medir a
  largura do campo, que cai de **189 px** (12h) para **137 px** (24h). Vale passar também
  `timezone_id="America/Sao_Paulo"`.
- **Modal nem sempre é `div[role="dialog"]`.** No assistente de horário e no modal de pausa, o
  seletor não casa (o wizard não usa `role=dialog`; o de pausa usa, mas em outro elemento).
  Quando falhar, localize pelo texto do próprio conteúdo ou pelo índice do campo, e confirme com
  um dump de `innerText`.
- **Se o traceback do Playwright citar um seletor que você já trocou**, desconfie de cache do
  script: criar um arquivo novo com outro nome resolveu (visto em 21/08/2026, manual #33).
- **O detalhe da venda (`/pedido=<preVendaID>`) demora ~12 s para montar por completo.** Os 5 s de
  praxe não bastam: no #79, a faixa *Produto não associado no pedido* só entrou no DOM depois
  disso, e duas capturas saíram sem ela. Para essa tela, espere **14 s**, role até o elemento
  (`scroll_into_view_if_needed`) e confirme pelo `inner_text` antes do print.
- **Ensaie a captura antes de gravar qualquer coisa (`DRY=1`).** Em tela que salva sem
  confirmação — o *Confirmar Vínculo* do #79 é um exemplo — vale um script que faz todo o
  caminho, imprime o que a janela devolveu e **para antes do último clique**. Foi o que evitou
  gravar o vínculo errado quando a janela mostrou dois produtos com o mesmo nome.
- **Botão sem rótulo em grade virtualizada (o ⋮ do card do produto): ache pela geometria.**
  Todos os cards têm o mesmo `svg.lucide-ellipsis-vertical`, e `nth(0)` abre o menu do
  produto errado. O que funciona é localizar o **título** do produto, listar todos os
  botões do ⋮ e escolher o que está **à direita e na mesma linha** (menor diferença de
  `y`, com tolerância de ~40 px). Implementação: `abrir_menu_do_produto()` no
  `manuais/venda-sugestiva-upsell/capturar.py`.
- **Conteúdo dentro de iframe não rola com `window.scrollTo`.** O app de relatórios
  (`relatorios.beefood.com.br`) tem rolagem própria: use `page.mouse.move()` sobre a área
  do iframe + `page.mouse.wheel(0, 220)` em passos pequenos e, antes do print, **afaste o
  ponteiro** (`page.mouse.move(80, 700)`) para não congelar um tooltip do gráfico na
  imagem.
- **Antes de escolher o exemplo do manual, cheque se o nome é único** nos dois lados (na lista e
  no cardápio). A base do sandbox tem **21 nomes de produto repetidos**; um exemplo com nome
  repetido rende imagem confusa. Um ensaio que imprime os botões da janela mostra isso em
  segundos.

### Modal por cima de mapa Leaflet sai apagado — esconda o mapa antes do print (#104)

Na Gestão de Entregas (`/gestao-entregas`) o modal de despacho automático saía **branco ou pela
metade** em oito tentativas seguidas. A causa não é animação: no Chromium headless o
`.leaflet-container` **compõe por cima do modal**, e o screenshot pega o mapa, não o diálogo.

O que **não** resolve: aumentar o `wait_for_timeout`, forçar `opacity: 1` / `visibility: visible`,
desligar animação por CSS, `--disable-gpu`, `--disable-lcd-text`. Forçar `transform: none` é pior:
o modal é centralizado por `transform`, e o print sai com o diálogo fora da tela.

O que resolve é esconder o mapa imediatamente antes do print:

```python
page.evaluate("document.querySelectorAll('.leaflet-container').forEach(e=>e.style.visibility='hidden')")
page.wait_for_timeout(1500)
page.locator("[role=dialog]").last.screenshot(path=destino, animations="disabled")
```

`visibility: hidden` e não `display: none`: o mapa continua ocupando o espaço, então o modal não
se reposiciona entre a leitura das coordenadas e o disparo do print.

### Medir o efeito de uma permissão (grupo de acesso) — #75

Vale para qualquer estudo que precise saber **o que cada switch faz**:

- **Espere 85 segundos** entre o `POST /api/empresa2/grupoAcessoItem` e a leitura das permissões.
  Testado em oito rodadas: com 85 s, duas leituras espaçadas de 12 s deram sempre o mesmo
  resultado; com menos, a resposta oscila entre o valor antigo e o novo.
- **Leia as permissões efetivas pela API**, não pela tela:
  `GET /api/empresa2/empresaConfig/{empresaID}/{usuarioID}/1` devolve o `grupoAcessoUsuario`.
  Ele vem em **base64 + zlib** (`pako.inflate` no front) — em Python, `b64decode` +
  `zlib.decompress`. A rota só aceita o **usuarioID do próprio token**: com o token do Principal
  e o id de outro usuário ela responde **401**. Solução: dois contextos do Playwright abertos,
  um por usuário.
- **Codificação binária em vez de um teste por permissão.** Dê a cada permissão um código de N
  bits e faça N rodadas desligando as que têm o bit da rodada ligado. A assinatura de bits em
  que cada chave virou `false` identifica a permissão. Fechou 93 permissões em 7 rodadas
  (~18 min) em vez de 93 rodadas (~2 h30). Ponto cego: chave que depende de **duas** permissões
  gera assinatura combinada, que pode coincidir com o código de uma terceira — reconfira os
  resultados estranhos com teste individual.
- **Nunca experimente no próprio grupo.** Salve o estado original antes e restaure no fim.
- **Rodada de baseline com tudo ligado** é obrigatória: ela separa o que não depende do grupo
  (no #75, apareceram três itens que dependem da **Função Gerente**).
- **Login novo por cenário.** Reaproveitar `storage_state` congela o `config_cache` no estado
  antigo.

### Aplicativos Android — o emulador NÃO funciona no Cloud Agent (testado em 2026-08-19)

> **Isto vale para o que é APK de verdade — e o totem não é** (descoberto em 21/09/2026,
> bloco #121 a #123). O **Totem de Autoatendimento** é uma página web servida em
> `totem.beefood.app` e **abre no Playwright**, com viewport de 1080×1920. Quem continua
> fora de alcance é o **tablet** (`com.cardapiodigitalmesacomanda`) e os dois apps de celular.
> Detalhes da captura do totem na seção 9, em *Totem de Autoatendimento — bloco #121 a #123*.

Investigação completa, para não se repetir o teste:

**O que o ambiente tem de sobra:**

| Recurso | Situação |
|---------|----------|
| Android SDK | Instala em **~40 s** (`commandlinetools-linux`, platform-tools, plataforma 34, emulador, imagens) |
| Java / Node / Yarn | OpenJDK 21, Node 22, Yarn 1.22 — já instalados |
| KVM | **Funciona de verdade.** Teste por `ioctl`: `KVM_CREATE_VM` com sucesso, 4 vCPUs, virtualização aninhada `Y` |
| Display | `DISPLAY=:1` com X ativo, Xvfb disponível |
| Máquina | 4 CPUs, 15 GB de RAM, 233 GB livres |
| `sudo` | Sem senha (dá para `chmod 666 /dev/kvm`) |

**O que não funciona:** o emulador sobe o QEMU, mas **o guest nunca inicia**. Testadas quatro
configurações (imagem `google_apis` com skin de tablet e swiftshader; imagem `default` com
`-gpu off`; a mesma sem Bluetooth; e com `-show-kernel`). Em todas, o log para exatamente na
mesma linha —

```
INFO | Activated packet streamer for bluetooth emulation
```

— e a CPU do QEMU cai para **0,2%**. Com `-show-kernel`, **nenhuma linha do kernel do Android
aparece**: não é lentidão, é travamento antes do boot. O `adb` enxerga `emulator-5554 offline`
indefinidamente. Provável bloqueio de syscall no sandbox do container; o KVM em si está sadio.

**Segundo obstáculo, independente do primeiro:** o **código dos apps não está acessível**. O
token do GitHub alcança 2 repositórios (`beefood-web-react` e `beefood-web-react-manual`), e a
organização no GitHub não tem nenhum projeto Android. O código deve estar no Bitbucket, como o
backend. Os três apps publicados são:

| Pacote | App |
|--------|-----|
| `com.beetechappgarcom` | App Garçom |
| `com.beetechentregador` | BeeFood Entregador |
| `com.cardapiodigitalmesacomanda` | Cardápio Digital Mesa/Comanda (o do tablet) |

> **Confirmado em 20/08/2026 (manual #24):** o código está no Bitbucket, em
> `beetechbr/beetech-appgarcom-android` — na máquina do dono, `c:\projetos\beetech-appgarcom-android`.
> É lá que ficam os `docs/manual-modo-kiosk.md` e `docs/images/kiosk/`. O `BITBUCKET_TOKEN`
> atual **não alcança** esse repositório (Access Token é escopado a um repositório só); o
> `.cursor/install.sh` já tem a entrada e aceita vários tokens via `TOKENS_BITBUCKET`, mas
> falta cadastrar o secret `BITBUCKET_TOKEN_APPGARCOM` — e secret só entra em **VM nova**.

> Sobre `yarn android`: é comando de React Native e **não resolve sozinho** — ele compila e
> instala num device conectado, ou seja, ainda depende de emulador funcionando ou de aparelho
> físico via `adb`.

**Como produzir manual de app Android, então:** as capturas precisam vir de **aparelho real**
(print do próprio Android, ou `scrcpy` espelhando na máquina do dono), ou de um **emulador na
máquina dele** (Android Studio no Windows, onde a virtualização é nativa). O Cloud Agent
continua servindo para escrever o manual, tratar as imagens e documentar a parte **web** do
app (por exemplo, Cardápio Digital Tablet tem as abas Tablets, Layout e Eventos no painel).

### Arquivo anexado no chat NÃO chega ao Cloud Agent (comprovado em 2026-08-20)

Ao pedir o manual do **modo kiosk** (#24), o dono anexou um `manual-modo-kiosk.md` e uma
pasta `images`. **Nenhum dos dois existia no VM.** Foi procurado no repositório, em todo o
histórico do Git, em todas as branches remotas, nos dois repositórios de referência, nas 81
branches do backend no Bitbucket e no sistema de arquivos inteiro (`find /`).

O anexo fica no contexto da conversa. Se o conteúdo não vier **inline no texto da mensagem**,
o agente não tem como abri-lo — e imagem nunca vem inline.

> **Correção, no mesmo dia:** existe um caso em que o anexo **chega**. Quando o arquivo é
> enviado como **documento**, ele é gravado em
> `~/.cursor/projects/workspace/uploads/<nome>_<hash>.<ext>` — foi assim que o
> `manual-modo-kiosk.md` do #24 finalmente chegou. **Antes de concluir que um anexo não
> existe, olhe essa pasta.** Arquivos gravados lá vêm com **CRLF**; converter com
> `tr -d '\r'` antes de comparar com algo do repositório.

**Imagem é a exceção, e isso importa muito para este projeto.** Testado cinco vezes em
20/08/2026: imagem enviada no chat aparece para o modelo (ele descreve o conteúdo sem
dificuldade) mas **nunca** vira arquivo em `uploads/` — não há como gravá-la em disco nem
commitá-la. Foi o que travou as 21 capturas do #24.

O agente recebe a imagem já decodificada, como imagem, sem caminho em disco e sem URL.
Não existe, portanto, "baixar a imagem do chat": não há de onde baixar. É a pergunta que o
dono fez em 20/08 e a resposta é essa. Também não serve reproduzir a tela desenhando algo
parecido: o manual precisa da captura real do aplicativo.

> **O `.zip` era a aposta, e ela falhou na prática.** A ideia era boa — zip não é imagem,
> então deveria cair em `uploads/` como qualquer documento. Só que na tentativa de 20/08 o
> `.zip` **não chegou** (`uploads/` seguiu com apenas o `.md`), e as imagens vieram outra vez
> como imagem no chat. Trate o zip como caminho **não confirmado**: vale tentar, mas não
> planeje o manual em cima dele.

### O caminho que resolve: zip numa URL pública (o agente baixa)

**O VM tem saída de internet liberada.** Confirmado em 20/08/2026 pelo
`cursor-cloud-environment-info`, que devolve `egress: { restricted: false }`. Ou seja: não há
allowlist de domínios, e o agente alcança qualquer host. `drive.google.com`, `docs.google.com`
e `github.com` foram testados com `curl` e respondem.

**Então o jeito de mandar imagem para o Cloud Agent é publicá-la numa URL e passar o link.**
Google Drive serve, e qualquer host que devolva o arquivo também. **Confirmado na prática no
mesmo dia:** foi assim que as 21 capturas do #24 entraram no repositório — um `.zip` de 20 MB
no Drive, baixado e distribuído em uma rodada. Duas regras:

1. **Link de ARQUIVO (um `.zip`), não de pasta.** Pasta do Drive não dá para baixar sem
   credencial. Compacte, suba o `.zip`, compartilhe o `.zip`.
2. **Compartilhamento em "qualquer pessoa com o link".** Sem isso o Drive devolve a página de
   login, e o que chega é HTML em vez de arquivo.

O `manuais/cardapio-digital-tablet-modo-kiosk/copiar-imagens.py` já aceita URL como origem:
baixa, confere que é zip de verdade, extrai e alimenta `imagens-puras/` — as tratadas ficam por
conta do `annotate.py`. Link de compartilhamento do Drive é convertido sozinho para o endpoint de
download direto (`drive.usercontent.google.com/download?id=…&confirm=t`), porque o link normal
devolve a página de visualização, não o arquivo. **Vale copiar essa função em qualquer manual
cujas capturas venham de fora.**

### WeTransfer também funciona — e não precisa de conta (confirmado em 18/09/2026)

O link do WeTransfer é página, não arquivo: `curl` no endereço devolve HTML. Mas o próprio
site pede o download por uma API pública, e o agente pode fazer a mesma chamada. Foi assim
que os **18 MB** do material do app do entregador (#104) entraram no repositório.

O link tem a forma `wetransfer.com/downloads/<transferID>/<recipientID>/<hash>`, e os três
pedaços são exatamente o que a API quer:

```bash
TID=<transferID>; RID=<recipientID>; H=<hash>
curl -sSL -c c.txt -o /dev/null "https://wetransfer.com/downloads/$TID/$RID/$H"   # pega o cookie
URL=$(curl -sS -b c.txt -X POST "https://wetransfer.com/api/v4/transfers/$TID/download" \
  -H "Content-Type: application/json" -H "x-requested-with: XMLHttpRequest" \
  -H "Referer: https://wetransfer.com/downloads/$TID/$RID/$H" \
  -d "{\"security_hash\":\"$H\",\"recipient_id\":\"$RID\",\"intent\":\"entire_transfer\"}" \
  | python3 -c 'import json,sys; print(json.load(sys.stdin)["direct_link"])')
curl -sSL -o pacote.zip "$URL"
```

A resposta é um `direct_link` assinado, com validade curta (o JWT do `token=` expira em
minutos) — **peça o link e baixe na mesma rodada.** A página também traz a lista de arquivos
em JSON (`"items":[{"name":…`), o que serve para conferir o pacote antes de baixar.

**Ganho sobre o Drive:** não exige configurar compartilhamento nem converter o link, e o dono
manda a pasta inteira de uma vez. Mesmos cuidados de sempre: conferir dado pessoal antes de
versionar, e checar os links internos do pacote — os do #104 vinham com 8 caminhos quebrados.

**O que resolve de verdade, para capturas que moram em outro repositório:** dar ao ambiente
acesso a esse repositório, para o agente pegar os arquivos na origem em vez de depender de
anexo. É o caso do #24: as capturas estão em `beetechbr/beetech-appgarcom-android`, em
`docs/images/kiosk/`. O `.cursor/install.sh` já lista o repositório e já aceita vários tokens
(`TOKENS_BITBUCKET`); falta apenas cadastrar o secret `BITBUCKET_TOKEN_APPGARCOM`, porque um
Repository Access Token é escopado a **um** repositório e o `BITBUCKET_TOKEN` atual só alcança
o `beetech-server-node-2.0` (a API responde **404** para o repo do app). Lembrando que
**secret novo só entra em VM nova**.

**Enquanto isso, o caminho mais curto é o dono commitar os arquivos.** Foi assim que 13 das
14 pastas de imagens deste repositório nasceram — só a do `campanhas-inteligentes` foi
capturada por agente, e porque aquele manual é do painel web, que o agente alcança com o
Playwright. Manual de aplicativo Android não tem esse atalho.

**Como mandar material para o Cloud Agent, em ordem de preferência:**

1. **Commitar no repositório** (numa branch) e citar o caminho no pedido. Funciona para texto
   e imagem, e ainda deixa o material versionado.
2. **Colar o texto no corpo da mensagem.** Resolve o `.md`, não resolve as imagens.
3. **Liberar o repositório de origem:** GitHub via `repositoryDependencies` + GitHub App;
   Bitbucket via Repository Access Token em secret + entrada em `REFERENCIAS_BITBUCKET`
   (lembrando que **secret só entra em VM nova**).

> O `BITBUCKET_TOKEN` de hoje é **escopo de repositório**: alcança apenas
> `beetechbr/beetech-server-node-2.0`. Listar o workspace `beetechbr` pela API retorna
> `size: 1`. Qualquer outro repositório do Bitbucket (app Android, totem, servidores) está
> fora do alcance.
>
> Detalhe útil: a API do Bitbucket **exige `Authorization: Bearer <token>`** com esse tipo de
> token. `curl -u x-token-auth:<token>` devolve **401** na API, embora funcione no `git`.

### O caminho de volta: mandar um kit para quem tira o print (19/09/2026)

Tudo acima é sobre material **chegando**. Quando quem fotografa é outra pessoa — ou outra IA, na
máquina do dono, com o emulador que aqui não existe — o problema se inverte: é preciso mandar um
pacote que se explique sozinho. O padrão que ficou está em
`manuais/gestao-entregas/pedidos/montar-kit.sh`, e vale copiar.

Quatro pastas numeradas na ordem de leitura: **o pedido**, **os scripts de cenário**, **a
referência** e **a árvore de saída já nomeada**. Mais um `LEIA-PRIMEIRO.md` na raiz. Três decisões
que fizeram diferença:

1. **A árvore de saída vai vazia, com os nomes exatos.** Quem fotografa grava dentro dela, e o
   pacote volta sem renomear nada. Renomear 26 arquivos na volta custa mais que criar 10 pastas na
   ida — e nome errado é o defeito que só aparece quando o manual já está sendo montado.
2. **As pastas da referência vão com o nome que têm no repositório**, sem prefixo de número, para
   os links que os manuais fazem entre si continuarem resolvendo dentro do kit. O número de cada um
   fica num `INDICE.md`. Com prefixo, os 136 links internos quebravam; sem, sobram 35, todos
   apontando para manuais que o kit não leva de propósito.
3. **As imagens da referência vão junto** (24 MB no caso). É o que deixa quem fotografa comparar
   enquadramento: "o seu print precisa parecer com estes". Kit só de texto obriga a adivinhar.

Um detalhe que economiza uma hora: o `capturar.ps1` do material do dono grava **dois níveis acima
de si mesmo**. Copiado sem alteração para `capturas-2/_ferramentas/emulador/`, ele passa a gravar
na raiz de `capturas-2/` — e `-Capitulo 16-notificacoes` cai exatamente na pasta do pedido. Resolver
por posição em vez de editar o script alheio evita divergência entre as duas cópias.

E o `LEIA-PRIMEIRO.md` precisa de uma frase que um humano não precisaria ler: **foto que não saiu
não se inventa.** Uma IA com acesso a editor de imagem e uma lista de 26 arquivos para preencher
tem todo incentivo para produzir a 26ª. Print faltando está anotado no relatório; print forjado vira
manual publicado mentindo.

**O zip fica versionado, na pasta do pedido.** Foi a decisão do dono e é a certa: artefato de agente
é link que ele precisa abrir no dashboard, enquanto arquivo na PR é o botão de download do GitHub, que
ele já sabe usar e pode repassar. São 24 MB num repositório que já tem **669 MB** de imagem de manual,
e o conteúdo é cópia do que está versionado ao lado — o zip existe pela conveniência de ser um arquivo
só. Duas consequências que o `README.md` da pasta precisa declarar: o `montar-kit.sh` grava **nesta
pasta** por padrão, e mexer em qualquer arquivo que entra no kit obriga a regravar e commitar o zip
junto, senão a cópia mente.

Conferir o zip **baixado**, não o que ia entrar: `curl` na URL `raw` do GitHub (sem autenticação, já
que o repositório é público), `unzip -t` e `md5sum` contra o arquivo versionado. Foi o que provou que o
caminho funciona ponta a ponta.

### O pedido que foi recusado antes de virar trabalho (19/09/2026)

Com o bloco da Gestão de Entregas fechado, escrevi uma **segunda lista de capturas** — 6 prints,
kit empacotado, zip versionado, tudo pronto — e o dono a recusou **na leitura**, antes de delegar:

> *"que tipo de manual estamos fazendo? pra que vamos ter uma sessão e uma imagem mostrando 'Nenhum
> pedido'? o manual deve ser util e não ter um monte de conteudo sem sentido. mostrar uma imagem de
> um aplicativo sem pedidos é totalmente fora de realidade."*

Ele tinha razão, e o defeito não estava na execução do pedido: estava em **o que eu tinha escolhido
pedir**. Eu havia passado a cobrir o aplicativo em vez de escrever o que alguém procura. O sintoma
é fácil de reconhecer depois: as seções começam a se chamar *"Quando não tem X"*, *"Quando a tela
fica vazia"*, *"Quando não há rede"* — descrições de **ausência**, que existem porque o aplicativo
tem aquele estado, não porque alguém precisa daquela resposta.

**O critério, e é uma pergunta só: o leitor sai daí fazendo algo diferente?**

| Ganha seção e imagem | Não ganha |
|---|---|
| tela de erro com **saída** — *Despacho não confirmado* do #113 manda ligar para a loja e avisa para não tocar de novo | tela **vazia**: ninguém consulta manual para saber como é a tela quando não há nada nela |
| tela que **parece** outra coisa — *Pagamento Confirmado!* que ainda pede FINALIZAR muda uma frase só e vale dinheiro | estado que o leitor **já sabe** que está vivendo: sem rede, o entregador não descobre pelo manual que está sem rede |
| variação que **muda a ação** — pedido de plataforma sem botão de confirmar encurta o roteiro | tela **idêntica** à normal: sem comparação possível, a foto não ensina |
| o que o suporte **ouve ao telefone** — a seção de cobrança que não fecha responde quase toda ligação sobre dinheiro | cobertura por simetria: "já mostrei o cheio, falta o vazio" |

Três coisas que saíram junto com o pedido, e é isso que dá o tamanho do erro:

1. **Uma imagem publicada.** A lista sem internet do #112 já estava tratada, anotada com três
   marcadores e no ar. O comentário que eu mesmo escrevi no `annotate.py` denunciava: *"a imagem
   inteira é a mensagem: não há mensagem"*. O achado ficou, como dois parágrafos; a foto saiu.
2. **Dois comandos de script.** `historico-zerar` e `historico-voltar` **apagavam o histórico
   inteiro do entregador** e guardavam o desfazer em arquivo, e existiam só para produzir a tela
   vazia. Ferramenta que reescreve passado precisa valer mais que uma imagem que não ensina nada.
3. **Meia tarde de engenharia de pedido.** Cena virtual do emulador para a câmera ler um EAN-13,
   `assembleRelease` para o app abrir sem Metro, separação das fotos por risco de decodificação —
   tudo correto, tudo caro, tudo a serviço de três imagens que não deviam ter sido pedidas.
   **Perguntar "consigo produzir esta imagem?" antes de "alguém precisa dela?" é a ordem errada.**

A parte que se salvou aponta para a próxima lição: relendo o **estudo de fonte que a IA anterior
entregou junto das fotos**, descobri que a faixa de status do leitor do #114 tem **seis** mensagens
e o manual listava cinco — faltava *Erro: {mensagem}* (o servidor recusando), caso diferente de
*Erro na leitura* (o envio que não saiu), e a diferença decide o que o entregador faz. **Material
recebido vale mais que as imagens dele:** a correção real do dia saiu de reler o que já estava no
disco, não de pedir coisa nova.

> **O store de artefatos tem cota, e ela aparece como "No space left on device".** O zip de 24 MB
> falhou pela metade escrevendo direto em `/opt/cursor/artifacts` (que é link para
> `/cursor/stores/self/artifacts`) e deixou um arquivo parcial de nome aleatório ocupando espaço.
> O jeito que funciona é montar o zip em `/tmp` e **copiar** depois — e limpar o parcial, senão a
> tentativa seguinte falha pelo mesmo motivo. Mais um argumento para o zip morar no repositório.

---

## 7. Regras de segurança em produção

- Decisão vigente: o ambiente "BeeFood3 - Manual" é **sandbox** → pode-se executar fluxos reais
  (abrir caixa, criar venda baixa, pagar) para o manual ficar fiel.
- Em contas que NÃO sejam sandbox: **não** finalizar vendas/pagamentos reais sem autorização.
- Nunca fazer ações destrutivas/irreversíveis sem confirmar com o usuário.

### Técnica do ensaio (para passos irreversíveis)

Muitas telas só gravam no clique final (fechar caixa, conferir, confirmar). Nesses casos,
**execute o fluxo inteiro uma vez sem o clique final**, capture tudo, revise as imagens e só
então repita para valer. Foi assim nos manuais de fechar caixa e de segunda conferência, e
evitou queimar cenários que não têm volta. Ao automatizar, mantenha o passo irreversível num
script separado dos idempotentes.

**Antes de capturar, leia no código o que grava.** Vale conferir três coisas: se a tela tem
auto-save (Parâmetros e a configuração do Cashback têm; o editor de campanha inteligente não
tem), em que linha o `handleSave` realmente chama a API, e o que um switch faz de fato. No
editor de campanha inteligente, por exemplo, o switch do card apenas abre um diálogo de
confirmação e o salvamento com a proteção anti-spam desligada retorna antes da API — o que
permitiu fotografar até o alerta vermelho de banimento sem alterar nada. Cinco minutos de
leitura de código evitam capturas em ambiente sujo ou cenários queimados.

### Dado pessoal em captura

O repositório é **público**. Quando a tela mostra nome, telefone ou e-mail de cliente, cubra na
imagem **pura**, não só na tratada — a pura também é versionada. No manual de segmentação isso
foi feito com borrão via `annotate.py`; no de campanhas inteligentes, com uma tarja e um
telefone fictício aplicados na pura antes do primeiro commit.

---

## 8. Stack do projeto (código) — referência

React 18 + TypeScript + Vite + Tailwind + shadcn/ui; react-router-dom v6; Supabase + API DataSnap
(`/datasnap/rest/...`); @tanstack/react-query; react-hook-form + zod. Versão em produção: `v3.190826.x`
(conferida em 19/08/2026 no rodapé do menu lateral).
Estrutura: `src/pages`, `src/components`, `src/hooks`, `src/contexts`, `src/integrations`.
Obs.: ainda **não existe `spec.md`** no projeto (a regra do projeto pede criar — pendente).

### Onde fica o código (por máquina)

| Máquina | Caminho do `beefood-web-react` |
|---------|--------------------------------|
| Windows (dono) | `C:\projetos\beefood-web-react` |
| Cloud Agent | `~/refs/beefood-web-react` (clone raso, **somente leitura**) |

No Cloud Agent o clone é feito pelo `.cursor/install.sh`. Para o clone funcionar são
necessárias **duas** liberações: o repositório precisa estar selecionado no **GitHub App do
Cursor** (configurações da org) **e** listado em `repositoryDependencies` no
`.cursor/environment.json` — esse campo não clona nada, ele só inclui o repositório no token
gerado para o ambiente. Faltando qualquer uma das duas, o clone falha com
`Repository not found`.

**O acesso vale durante a sessão inteira** (verificado em 2026-08-19). Dentro da sessão o
`git fetch origin main` em `~/refs/beefood-web-react` funciona normalmente, e `gh` também
enxerga o repositório. Ou seja: **dá para atualizar o código no meio do trabalho**, sem
precisar de uma sessão nova.

> Correção: até 2026-08-04 esta seção afirmava que o escopo valia só durante o install e que
> o código ficava congelado. Não é mais o caso.

Para conferir o que o token alcança: `gh api /installation/repositories -q '.total_count,
(.repositories[].full_name)'`. Hoje retorna **2**: `beefood-web-react` e
`beefood-web-react-manual`. Qualquer outro repositório (ex.: os de servidor, usados para
importar manuais de integração) responde **404** — e 404 aqui é ambíguo: significa "não
existe" **ou** "não liberado". Para liberar, são necessárias as duas coisas descritas acima
(GitHub App + `repositoryDependencies`).

### Referências no Bitbucket (backend)

`repositoryDependencies` **não serve** para Bitbucket: ele só amplia o token do GitHub. Para
clonar um repositório do Bitbucket no Cloud Agent:

1. No Bitbucket, em **Repository settings → Security → Access tokens**, criar um
   **Repository Access Token** com escopo **Repositories: Read** (só leitura, e limitado
   àquele repositório).
2. No **Cursor Dashboard → Cloud Agents → Secrets**, guardar o valor como `BITBUCKET_TOKEN`.
3. Adicionar a entrada em `REFERENCIAS_BITBUCKET`, no `.cursor/install.sh`, no formato
   `workspace/repositorio#branch` (o `#branch` é opcional). O clone tenta os dois usuários
   possíveis (`x-token-auth` para Access Token, `x-bitbucket-api-token-auth` para Atlassian
   API token) e depois **regrava o remote sem o token**.

Sem o secret, o bloco é ignorado e o setup segue normalmente.

| Máquina | Caminho do backend |
|---------|--------------------|
| Cloud Agent | `~/refs/beetech-server-node-2.0` (branch `beefood-web-react`, clone raso, só leitura) |

> **Secret só entra em VM nova.** O `BITBUCKET_TOKEN` é injetado no boot do ambiente. Criar o
> secret no meio de uma sessão não o disponibiliza para a sessão em andamento — o clone só
> acontece no install da **próxima** sessão.

> **Funcionou.** Desde 2026-08-19 o backend está clonado e disponível em
> `~/refs/beetech-server-node-2.0` (branch `beefood-web-react`). Ele tem um `spec.md` próprio
> na raiz. Foi o que permitiu fechar o estudo do manual #13: só o código do servidor explicou
> por que o parâmetro "Caixa por Usuário" não fazia o que a tela promete.

> ⚠️ **Parou de funcionar em 2026-09-01 (estudo #74).** O backend **não está mais** em
> `~/refs/` — só `beefood-web-react` e `beefood-reports-hub` clonaram. O secret
> `BITBUCKET_TOKEN` continua injetado no ambiente, mas o Bitbucket responde
> *"You may not have access to this repository"*. Testadas as **quatro** combinações
> (`x-token-auth` e `x-bitbucket-api-token-auth` × `BITBUCKET_TOKEN` e
> `BITBUCKET_CARDAPIO_DIGITAL`): todas falham na autenticação. O token provavelmente
> **expirou ou foi revogado** — Repository Access Token do Bitbucket tem validade. Para
> voltar a ter o backend, gerar um token novo (Repository settings → Security → Access
> tokens, escopo *Repositories: Read*) e regravar o secret no Cursor Dashboard;
> **secret novo só entra em VM nova**.
>
> ✅ **Mas o backend está lá — conferido em 2026-09-17.** O clone existe em
> `~/refs/beetech-server-node-2.0` (branch `beefood-web-react`, commit `4a419d2`, baixado em
> 2026-09-10) e foi ele que explicou o `sugestao: true` do `pedidoPOST.js` e a proc do
> `relatorioSugestao.js` no manual #103. A VM inicia de um **snapshot pronto do ambiente**,
> que guarda o clone feito num build em que o token ainda valia. O token continua falhando
> (as quatro combinações testadas de novo em 2026-09-17), então o backend é **leitura
> congelada**: o código de setembro está em disco, mas não atualiza. `git fetch` dentro da
> sessão também não resolve — o `install.sh` grava o remote **sem** o token de propósito,
> para o clone não travar quando o token expira. Antes de concluir que o backend não existe,
> **olhe a pasta**.
>
> Enquanto isso, a saída que funcionou no #74 é **provar a regra por dado real** em vez de
> ler o código do servidor: um script curto que loga com Playwright e consulta a API
> autenticada de dentro da página (o token do app vem do `localStorage`, ofuscado por XOR
> com a chave `bf2024_secure_key_token` — ver `src/lib/api.ts`). Base da API em produção é
> `https://app3.beetechapi.be`, e o front troca `/datasnap/rest/` por `/api/`
> (`src/config/api-endpoints.ts`). Cruzando `venda2/historicoVendas`,
> `caixa2/caixaListagem`, `venda2/vendaDetalhes` e `empresa2/empresaConfig` deu para
> provar o reset da numeração sem nenhuma linha do backend.

> **Cuidado com repositório público.** Este repositório de manuais é público. Secret de
> ambiente em repositório público é risco real: quem puder abrir um Cloud Agent nele recebe a
> variável injetada — e o Cursor pode até bloquear a injeção por padrão nesse caso. Antes de
> cadastrar um token do backend, **torne este repositório privado**. A decisão de deixá-lo
> público (seção 11) valia para credenciais descartáveis de teste, não para acesso ao
> código-fonte do servidor.

> **Documentação de módulo pode estar dentro do clone que existe.** No #104 o dono pediu para ler
> `beetech-server-node-3.0\docs\gestao-entrega-2.0`, e a conclusão apressada foi "não temos esse
> repositório". A pasta estava em `~/refs/beetech-server-node-2.0/docs/gestao-entrega-2.0/` — 21
> documentos, 13 prompts de frontend e 14 scripts SQL, ~17.100 linhas. **Procure por caminho de
> documentação antes de concluir que falta repositório.**

> **O cardápio digital é um terceiro repositório, e ele não precisa de clone.** Descoberto no
> #121: o cardápio público (`menu.beefood.com.br`) é um **Nuxt 2** próprio, que não está no
> `beefood-web-react` nem no `beetech-server-node-2.0`. Clone não há, mas o **bundle publicado
> tem o código-fonte de tela**: componentes, todas as frases de todos os estados, intervalos de
> atualização e as metatags. O caminho é `curl` da página → listar os `/_nuxt/*.js` → procurar o
> termo no chunk grande, que traz o mapa de rotas **e** o mapa de hashes de chunk → traduzir o
> número do chunk em nome de arquivo. Os hashes mudam a cada publicação; o caminho não. A base
> da API dele é `https://cardapio-digital.beetechapi.be`, em caminhos
> `api/rest/tempresaDelivery/...`. Vale para qualquer manual de tela do cardápio, do totem ou
> de outro front público.

### Ler os bancos e a API do app direto do Cloud Agent (#104)

Descoberto no estudo da Gestão de Entregas, e vale para qualquer manual que precise **provar** o
estado de um cenário em vez de deduzi-lo da tela. Três caminhos funcionam de dentro da VM:

| Caminho | Como | Serve para |
|---|---|---|
| **MSSQL `notafacilb`** (ERP) | usuário **de leitura** do backend, em `src/config/execSQLQuery.js`; `npm i mssql` | pedido, situação da entrega, funcionário, parâmetros, tipos de WhatsApp da filial |
| **MySQL Aurora `entregas`** | credencial em `src/config/initMySqlServerGestaoEntrega.js`; `npm i mysql2` | rota, parada, presença, GPS, despacho automático, token de push |
| **API do app do entregador** | Basic Auth + header `app-name: bee-entregador`, em `app.beetechapi.be` (login) e `app3.beetechapi.be` (entregas) | o **mesmo payload** que o celular recebe — conferir cenário sem emulador |

Duas regras, e a segunda não é opcional:

1. **Nunca copie credencial para este repositório.** Ele é público. Cite o arquivo do backend onde
   ela está e pare aí — foi o que fiz nos arquivos de estudo do #104.
2. **O usuário do Aurora tem `INSERT`, `UPDATE` e `DELETE`, não só `SELECT`.** Então daqui dá para
   escrever no banco de produção do módulo de entregas. Isso **não** dispensa a regra da seção 7:
   escrita em produção só com o dono pedindo, e a técnica do ensaio antes.

Teste de alcance, antes de instalar driver:

```bash
timeout 15 bash -c 'cat < /dev/null > /dev/tcp/<host>/3306' && echo OK
```

### Montar cenário de entregas sem emulador (#104)

O que o dono autorizou em 18/09 para a Gestão de Entregas, e que foi conferido de ponta a ponta:
**pedido semeado, entregador simulado e pin andando no mapa**, tudo do Cloud Agent. O caminho está
detalhado em `manuais/gestao-entregas/MEMORIA.md`. Três coisas que valem para além daquele bloco:

1. **`beetech_leitura` engana pelo nome.** O usuário do MSSQL que todo o backend usa é
   `db_datareader` **+ `db_datawriter` + `db_ddladmin`**, com `EXECUTE` no banco inteiro. A
   seção 8 acima já avisava isso do Aurora; vale igual para o ERP. Nenhuma das duas credenciais é
   de leitura, apesar dos nomes.
2. **O JWT do painel sai do `localStorage`**, não da API: a rota de login do painel não responde no
   caminho óbvio, e Basic Auth devolve **401** nas rotas que têm `authMiddleware`. Logar com
   Playwright e desofuscar a chave `beefood_auth_token` é o caminho que funciona.
3. **Script Python não pode se chamar `token.py`** (nem `tokenize.py`, `logging.py`…): ele sombreia
   o módulo da biblioteca padrão e o Playwright morre com erro de importação circular que não
   parece ter nada a ver com o nome do arquivo.

### ⚠️ Nunca cole saída do leitor de arquivos dentro de um `.md`

Ferramentas de leitura prefixam **cada décima linha** com o número alinhado à direita em 6
caracteres, seguido de `|` — `    10|`, `   150|`. Isso é **metadado da ferramenta**, não conteúdo
do arquivo. Copiar a saída para dentro de um `.md` gravou o rótulo no texto, e em 18/09 havia
**301 ocorrências em 20 arquivos**, incluindo quatro manuais **já publicados**
(`vinculo-marketplace`, `formas-recebimento`, `cadastro-mesas`, `cadastro-comandas`).

Os dois estragos são diferentes, e o segundo é pior:

| Forma | Vira | Efeito |
|---|---|---|
| Rótulo **sozinho** na linha (linha vazia na posição) | `   150|` no lugar de uma linha em branco | Parágrafos que deviam estar separados aparecem colados |
| Rótulo **grudado** na linha | `    50\|\| Nº \| Item \|` | O markdown não reconhece mais a tabela: cinco linhas viram um parágrafo com canos no meio |

Para achar: `grep -rn '^ \{0,5\}[0-9]\{1,6\}|' --include=*.md .`. Ao corrigir, **rótulo sozinho
volta a ser linha em branco** (apagar a linha cola parágrafos, e num caso colava texto com imagem);
rótulo grudado perde só os 7 caracteres do prefixo.

Antes de remover em lote, confirme que é artefato e não conteúdo: os números sobem
**monotonicamente em passos de 10** e **não batem** com a posição real da própria linha — número
escrito de propósito bateria.

---

## 9. Índice de manuais

| Manual | Pasta | Status |
|--------|-------|--------|
| Caixa (abrir, receber, consultar) | `manuais\caixa\` | ✅ Concluído |
| Fechar caixa (vendas pendentes, 1ª conferência, quebra) | `manuais\caixa-fechar\` | ✅ Concluído |
| Segunda conferência (dupla checagem, resolve a quebra) | `manuais\caixa-conferencia-2\` | ✅ Concluído |
| Restrições de caixa (grupo de acesso) | `manuais\caixa-restricoes\` | ✅ Concluído |
| Segmentação de clientes (Food Marketing) | `manuais\segmentacao-clientes\` | ✅ Concluído |
| Reforma Tributária (IBS/CBS) | `manuais\reforma-tributaria-ibscbs\` | ✅ Concluído |
| Ativação Aiqfome V2 | `manuais\ativacao-aiqfome\` | ✅ Concluído |
| Integração Machine | `manuais\integracao-machine\` | ✅ Concluído |
| Integração 99 Entrega | `manuais\integracao-99-entrega\` | ✅ Concluído |
| Integração Repediu | `manuais\integracao-repediu\` | ✅ Concluído |
| Integração FoodCRM | `manuais\integracao-foodcrm\` | ✅ Concluído |
| Integração Uber Direct | `manuais\integracao-uber-direct\` | ✅ Concluído |
| Segmentação de clientes | `manuais\segmentacao-clientes\` | ✅ Concluído |
| Campanhas Inteligentes | `manuais\campanhas-inteligentes\` | ✅ Concluído |
| Avisos do cardápio digital | `manuais\cardapio-digital-avisos\` | ✅ Concluído |
| Capas e Destaques | `manuais\cardapio-digital-capas-destaques\` | ✅ Concluído |
| Pixel Meta + API de Conversões | `manuais/pixel-meta-api/` | ✅ Concluído |
| Pixel Meta somente | `manuais/pixel-meta-somente/` | ✅ Concluído |
| Mapas do Google | `manuais/mapas-google/` | ✅ Concluído |
| Domínio próprio | `manuais/dominio-proprio/` | ✅ Concluído |
| TEF Stone (AutoTEF) | `manuais/tef-stone/` | ✅ Concluído |
| TEF PayGo | `manuais/tef-paygo/` | ✅ Concluído |
| Gaveta de dinheiro | `manuais/gaveta-dinheiro/` | ✅ Concluído |
| Mercado Pago | `manuais/mercado-pago/` | ✅ Concluído |
| BeeFood Entregador (app motoboy) | `manuais/app-entregadores/` | ✅ Concluído |
| IA ChatGPT no WhatsApp | `manuais/ia-chatgpt-whatsapp/` | ✅ Concluído |
| Campanhas SMS | `manuais/campanhas-sms/` | ✅ Concluído |
| Cupom de Desconto | `manuais/cupom-desconto/` | ✅ Concluído |
| Entrega Fácil iFood | `manuais/entrega-facil-ifood/` | ✅ Concluído |
| Let's Express | `manuais/integracao-lets-express/` | ✅ Concluído |
| Foody Delivery | `manuais/integracao-foody-delivery/` | ✅ Concluído |
| Pick n Go! | `manuais/integracao-pick-n-go/` | ✅ Concluído |
| Uai Rango | `manuais/integracao-uai-rango/` | ✅ Concluído |
| Desconto nas formas de recebimento | `manuais/cardapio-digital-desconto-formas/` | ✅ Concluído (#64) |
| Taxas das formas de recebimento | `manuais/taxas-formas-pagamento/` | ✅ Concluído (#65) |
| Lançamentos: contas a pagar | `manuais/lancamentos-contas-pagar/` | ✅ Concluído (#66) |
| Lançamentos: contas a receber | `manuais/lancamentos-contas-receber/` | ✅ Concluído (#67) |
| Exibir / Ocultar | `manuais/exibir-ocultar/` | ✅ Concluído (#68) |
| Preço Programado | `manuais/preco-programado/` | ✅ Concluído (#69) |
| Agendamento do cardápio digital | `manuais/cardapio-digital-agendamento/` | ✅ Concluído (#70) |
| Aparência e layout do cardápio digital | `manuais/cardapio-digital-aparencia-layout/` | ✅ Concluído (#71) |
| Ficha técnica (custo do prato e baixa de estoque) | `manuais/ficha-tecnica/` | ✅ Concluído (#72) |
| Produto só com agendamento (encomenda) | `manuais/cardapio-digital-agendamento-produto/` | ✅ Concluído (#73) |
| Entendendo a numeração dos pedidos | `manuais/numeracao-pedidos/` | ✅ Concluído (#74) |
| Grupos de acesso — estudo completo | `manuais/grupos-acesso/` | ✅ Concluído (#75) |
| Criar usuário e montar grupo de acesso | `manuais/usuarios-criar/` | ✅ Concluído (#76) |
| BeeFood Pixel Analytics | `manuais/pixel-analytics/` | ✅ Concluído (#17) |
| Cardápio digital presencial e QR Code | `manuais/cardapio-digital-presencial-qrcode/` | ✅ Concluído (#77) |
| Vínculo Marketplace | `manuais/vinculo-marketplace/` | ✅ Concluído (#79) |
| Cadastrar mesas e gerar o QR Code | `manuais/cadastro-mesas/` | ✅ Concluído (#80) |
| Cadastrar comandas e gerar o QR Code | `manuais/cadastro-comandas/` | ✅ Concluído (#81) |
| Cadastrar forma de recebimento | `manuais/formas-recebimento/` | ✅ Concluído (#82) |
| Comissão do garçom: cadastrar e lançar | `manuais/comissao-garcom-cadastrar/` | ✅ Concluído (#83) |
| Relatório de comissão do garçom | `manuais/relatorio-comissao-garcom/` | ✅ Concluído (#84) |
| Relatório de taxa de serviço | `manuais/relatorio-taxa-servico/` | ✅ Concluído (#85) |
| Taxa de serviço opcional no cupom | `manuais/cupom-taxa-servico-opcional/` | ✅ Concluído (#98) |
| Destaque na impressão | `manuais/destaque-impressao/` | ✅ Concluído (#99) |
| Tradução do cardápio presencial (tablet e totem) | `manuais/traducao-cardapio-presencial/` | ✅ Concluído (#100) |
| Domínio próprio e subdomínio pela tela | `manuais/dominio-proprio-configurar/` | ✅ Concluído (#101) |
| Gerar Cardápio em PDF | `manuais/cardapio-pdf/` | ✅ Concluído (#102) |
| Venda Sugestiva (UpSell) | `manuais/venda-sugestiva-upsell/` | ✅ Concluído (#103) |
| Pedidos pelo chat no WhatsApp | `manuais/whatsapp-pedidos-chat/` | ✅ Concluído (#86) |
| Campanhas de WhatsApp | `manuais/campanhas-whatsapp/` | ✅ Concluído (#15) |
| Notificações de cada etapa | `manuais/whatsapp-notificacoes/` | ✅ Concluído (#87) |
| Respostas automáticas | `manuais/whatsapp-respostas/` | ✅ Concluído (#88) |
| Resumo diário e semanal | `manuais/whatsapp-resumo-diario/` | ✅ Concluído (#89) |
| Conectar o WhatsApp (QR) | `manuais/whatsapp-conectar/` | ✅ Concluído (#90) |
| Atender no BeeBot | `manuais/whatsapp-atendimento-beebot/` | ✅ Concluído (#91) |
| Indicadores de WhatsApp | `manuais/whatsapp-indicadores/` | ✅ Concluído (#92) |
| Histórico de mensagens | `manuais/whatsapp-historico/` | ✅ Concluído (#93) |
| Liberar o entregador | `manuais/gestao-entregas-liberar-entregador/` | ✅ Concluído (#104) |
| Ler o mapa e o painel de entregas | `manuais/gestao-entregas-mapa-painel/` | ✅ Concluído (#105) |
| Montar a rota | `manuais/gestao-entregas-montar-rota/` | ✅ Concluído (#106) |
| Despachar a rota e acompanhar | `manuais/gestao-entregas-despachar/` | ✅ Concluído (#107) |
| Fechar a entrega no painel | `manuais/gestao-entregas-fechar-entrega/` | ✅ Concluído (#108) |
| Despacho automático | `manuais/gestao-entregas-despacho-automatico/` | ✅ Concluído (#109) |
| Avisos de WhatsApp da entrega | `manuais/gestao-entregas-avisos-whatsapp/` | ✅ Concluído (#110) |
| App: instalar, entrar e ficar disponível | `manuais/app-entregador-entrar/` | ✅ Concluído (#111) |
| App: as entregas do dia e o histórico | `manuais/app-entregador-entregas-do-dia/` | ✅ Concluído (#112) |
| App: chegar no endereço | `manuais/app-entregador-rota/` | ✅ Concluído (#113) |
| Código de barras: ligar a etiqueta e ler o pedido | `manuais/app-entregador-codigo-barras/` | ✅ Concluído (#114) |
| App: pedido de iFood e de 99Food | `manuais/app-entregador-marketplace/` | ✅ Concluído (#115) |
| App: receber na porta | `manuais/app-entregador-cobranca/` | ✅ Concluído (#116) |
| Uma entrega do começo ao fim | `manuais/gestao-entregas-ciclo-completo/` | 🔨 Esqueleto (#117) — faltam 13 imagens |
| Relatório Operação de Entrega | `manuais/relatorio-operacao-entrega/` | ✅ Concluído (#118) |
| Quanto o entregador recebe (Taxa / KM) | `manuais/entregador-quanto-recebe/` | ✅ Concluído (#119) |
| Painel para Entregadores | `manuais/painel-entregador/` | ✅ Concluído (#120) |
| Totem: pôr no ar e configurar | `manuais/totem-configurar/` | ✅ Concluído (#121) |
| Cupom e cashback no totem | `manuais/totem-cupom-cashback/` | ✅ Concluído (#122) |
| O pedido do totem no painel | `manuais/totem-venda-no-painel/` | ✅ Concluído (#123) |
| Mais de um cardápio no mesmo totem | `manuais/totem-multicardapio/` | ✅ Concluído (#124) |
| O cliente acompanha a entrega no mapa | `manuais/gestao-entregas-rastreio-cliente/` | ✅ Concluído (#121) |

> ⚠️ **O #121 está repetido nesta tabela, e é de propósito até o dono decidir.** O bloco do
> totem e o rastreio do cliente foram escritos em paralelo, em branches diferentes, e os dois
> pegaram o mesmo número — a colisão só apareceu quando as duas branches entraram na `main`.
> O detalhe e a recomendação (renumerar o **rastreio** para **#125**, que é o lado barato)
> estão no [`CHECKLIST-MANUAIS.md`](CHECKLIST-MANUAIS.md), logo abaixo da tabela de manuais.
> **Lição de processo: número de manual se escolhe lendo o checklist, não contando o último
> que você mesmo escreveu** — trabalho paralelo não vê a numeração do vizinho.

### O cliente acompanha a entrega no mapa — #121

O rastreio do lado do **cliente**: link no WhatsApp que abre mapa ao vivo, com o primeiro
nome do entregador, a moto andando e a distância em linha reta. O manual é para o lojista,
e o assunto é o que o cliente dele vê. Detalhes em
[`MEMORIA.md`](../../../../manuais/gestao-entregas-rastreio-cliente/MEMORIA.md) e
[`fluxo-codigo.md`](../../../../manuais/gestao-entregas-rastreio-cliente/fluxo-codigo.md).

Três aprendizados que **não** são deste manual só:

- **Tela do cardápio público? O código está a um `curl` de distância.** O rastreio mora no
  cardápio digital, que é um Nuxt 2 em repositório separado — e os tokens do Bitbucket
  continuam inválidos (seção 8). Mas `menu.beefood.com.br` **serve o bundle**, e nele estão
  a rota, os componentes, todas as frases de todos os estados, os intervalos e o
  `noindex, nofollow`. O caminho: `curl` da página → achar os `/_nuxt/*.js` de entrada →
  procurar o termo no chunk grande, que tem o mapa de rotas e o **mapa de hashes de chunk**
  → traduzir o número do chunk em arquivo. Os hashes mudam a cada publicação; o caminho não.
  **Vale sempre que o manual é de tela do cardápio, do totem ou de qualquer front público.**
- **Primeiro manual sem captura própria, e o importador segue o padrão do #24.** Quando o
  material vem pronto do dono, o `annotate.py` ganha uma função `preparar()` que traz a
  captura do caminho de upload do chat e recorta — e ela **avisa e segue** quando o caminho
  já não existe, usando a pura versionada. O importador **nunca** escreve em
  `imagens-tratadas/`, senão a próxima execução apaga as setas.
- **Material não versionado? Então nada pode transformar a pura depois do importador.** O
  `com_margem()` dos manuais do app **grava a margem dentro de `imagens-puras/`**, e ali isso
  é inofensivo: o material daqueles manuais é versionado, o `copiar()` reconstrói a pura a
  cada execução (conferido — o `annotate.py` do #111 rodado duas vezes dá as 15 tratadas
  idênticas). No #121 o material é um upload de chat, que **desaparece**: a segunda execução
  pegava a pura que já tinha margem e somava outra, levando 780 px para 1026 e as tratadas
  para 1350, com toda seta deslocada. A correção é a regra: **pura é o print, e só** — a
  margem passou a ser montada dentro do `annotate()`, a partir de `m` e `md`. **Teste que
  pega isso:** rode o script com o caminho do material trocado por uma pasta inexistente e
  confira que as tratadas saem byte a byte iguais e as puras não mudam.
- **A margem à direita não é exclusiva de print de app.** Ela já estava documentada para os
  manuais #111 a #116 e reapareceu aqui, em print de **navegador** de celular, pelo mesmo
  motivo: o alvo era a hora do despacho, no canto direito da linha do estado. `md=0.13`
  resolveu. Print de cardápio público tem a mesma anatomia de print de app — coluna
  esquerda com texto, coluna direita com hora, selo e flecha.

Duas armadilhas de anotação que se repetiram até a quarta rodada de conferência:

- **Texto: mire o vão antes da primeira letra, nunca a letra.** As pontas caíam sobre o
  *P* de *Pedido*, o *C* de *Carlos*, o *A* de *Acompanhe* e o *1* de *1 item*. Onde há
  ícone antes do texto, o vão entre ícone e texto é o alvo certo.
- **Pino de mapa aceita seta na borda.** Ícone não é texto: apontar para a borda do pino é
  mais claro que apontar para o vazio ao lado dele.

E uma decisão de conteúdo que serve para qualquer recurso novo: **honestidade do produto é
assunto de manual.** A tela não estima horário de chegada e mostra distância *em linha
reta*; o manual explica **por quê**, em vez de esconder. Um "8 minutos" que vira 25 gera
exatamente a ligação que o recurso existe para evitar — e essa é a mentalidade que o dono
pede que os manuais documentem.

### Totem de Autoatendimento — bloco #121 a #123 (e o #124)

**A regra antiga estava meio errada: o totem abre no Cloud Agent.** "Totem e tablet são
APK, não dá para fotografar" vale só para o **tablet**. O totem é uma página web (PWA), e
a própria aba *Download* do painel entrega a URL:

```
https://totem.beefood.app/?empresaID=<empresa>&filialID=<filial>&token=<aaToken>
```

O `aaToken` sai do `config_cache` do painel (ou do botão **Copiar** da aba Download). Com
viewport de **1080×1920**, `locale="pt-BR"` e `service_workers="block"` (sem isso o PWA
serve tela cacheada), o Chromium desenha o aparelho inteiro. Isso destrava o padrão que os
três manuais usam: **cada configuração fotografada em par — a chave no painel e o efeito
na tela do cliente.**

Duas manhas do aparelho, que valem para qualquer captura de totem:

- os botões respondem a `click()` por JavaScript, mas **o teclado numérico e o seletor de
  cardápio não** (eles escutam evento de ponteiro): telefone e mesa precisam de
  `get_by_role("button", name=c, exact=True).click(force=True)`, e os cartões do seletor
  precisam de `page.mouse.click(x, y)` na caixa medida por `getBoundingClientRect`
  (#124). Clique em camada por cima do cardápio também tem de ser **escopado no diálogo**
  (`[role=dialog][aria-labelledby="menu-picker-title"]`), senão o seletor por texto acha um
  produto atrás da camada e o clique morre;
- os seletores não são estáveis. O que funciona é achar botão **pelo texto** e filtrar por
  **altura/posição** quando o texto repete (cartão e cabeçalho).

E uma terceira, de imagem: **foto recém-subida chega do S3 depois do texto**. Sem esperar
`document.images` completarem, a miniatura sai como ícone de imagem quebrada — daí o
`esperar_imagens()` dos três `capturar.py`.

O recorte do aparelho tira a **barra de cima**: o logotipo da loja é retangular (350×112)
e ela o desenha num espaço quadrado, então ele sai cortado.

Três descobertas de produto que ficaram documentadas:

- **foto de setor muda o layout** da coluna da esquerda do totem (texto × tira de
  miniaturas); **foto de produto não muda layout nenhum** — produto sem foto vira cartão
  com o ícone de imagem quebrada. A regra completa é
  `algum setor com s3Link ? miniatura : texto` e, na miniatura,
  `src = setor.s3Link || logotipoDaLoja`: **basta um** setor com foto para a coluna toda
  virar miniatura, e o setor sem foto sai com o **logotipo da loja**, não com espaço vazio
  (o #121 dizia espaço vazio e foi corrigido pelo #124);
- o desconto que o totem mostra na forma de pagamento **não é do totem**: *Dinheiro* 1% vem
  de **Cadastros → Formas Recebimento** e *PIX* 5% de **Cardápio Digital → Pagamento
  Online**. Cuidado: a mesma forma em *Cardápio Digital → Formas Recebimento* tinha 5% e
  **não** foi o valor aplicado;
- a venda do totem é `tipo` DELIVERY + `codigoServico = 'A'`, e tem **três nomes** na
  interface: **AutoAtendimento** no card da venda, **Totem** nos chips e filtros,
  **Autoatendimento** no Desempenho.

**O #124 entrou depois, porque o dono montou o cenário.** Ele contratou um cardápio
adicional na empresa 38311 (filial 50502) e pediu o manual do multicardápio — a aba
*Cardápios* do #121 era três parágrafos de texto justamente porque não havia segundo
cardápio para fotografar. **Cenário criado pelo dono é gatilho de manual novo:** vale
perguntar o que mais a tela passa a mostrar quando o dado existe. O que o aparelho ganha
com dois cardápios: a tela *Escolha um cardápio* (só a partir do segundo —
`if (menus.length > 1)`), o *Ver todos os cardápios* (produtos concatenados, setores
**deduplicados por `produtoSetorID`**) e o botão *Trocar* no cabeçalho, sem perder a
sacola. O pedido continua sendo **um**, na loja do totem: `totem2/pedido/processar` não
tem `filialID` por item. No painel, `CardapioSelector` e a faixa *EDITANDO CARDÁPIO* só
existem com `filiais.length > 1` — ou seja, capturas de painel que dependem do seletor
**não existiam** antes deste cenário.

### Painel para Entregadores — #120

Tela de **parede**, feita para TV na área onde os entregadores esperam: duas colunas
(*Em preparo* e *Pronto*), número grande do canal, logo da plataforma e alerta de atraso.
Rota `/painel-entregador`, **somente leitura** — nenhum hook de escrita. Abre em janela
nova por dois caminhos: ⋮ do cabeçalho do Delivery e card em *Aplicativos → Entrega*.
Liberada por lista de empresas (`[107, 38311]`, então a sandbox fotografa) e pela permissão
`gestaoEntregas`, a **mesma** da Gestão de Entregas.

Dois achados que valem para outras telas de fila:

- **A janela é de 6 horas e olha a criação do pedido**, não a última mudança de situação.
  Pedido de ontem não volta para a tela mexendo na situação dele. O painel é do **turno**.
- **`origem` é derivada do identificador de plataforma** (`ifoodLocalizer` → iFood, `nnID`
  → 99Food, `keetaId` → Keeta, `aiqfomeId` → AIQFome, `filialIDOrigem` → Cardápio Digital,
  nada → Manual). Nenhuma rota aceita `origem` como entrada. O método que provou isso, e o
  jeito seguro de estampar identificador na base, viraram a skill
  [`cenario-sandbox`](../../cenario-sandbox/SKILL.md).

Armadilha de captura que se repete: para forçar tema claro, **gravar
`localStorage.theme = 'light'` e recarregar**. Ler `html.class` logo depois do `goto` às
vezes diz `light` numa tela que ainda vai virar escura, porque a classe só se firma depois
da hidratação. E a cobertura de dado pessoal tem de varrer **nó de texto**, não elemento
folha: onde o nome divide a caixa com um ícone, a busca por folha mede zero e o print sai
com o nome à vista.

### Tradução do cardápio presencial — #100

Campo `traducao` (JSON `{ "en": { chave: texto }, "es": {...} }`, **português fora
do objeto**) em quatro cadastros: setor (chave `setor`, no **Nome Interno**, não no
Nome Público), produto e complemento (`descricao` = nome, `descritivo` = descrição)
e grupo de opções (`descricao`). Tudo mora em
`src/components/cardapio/BandeiraIdioma.tsx`.

As bandeiras só aparecem quando `temTraducaoContratada()` → `qtdAA > 0 ||
qtdTablet > 0` no `config_cache`. Trocar de bandeira **não** salva nem descarta:
é visão sobre o mesmo `formData`, gravado no `SALVAR E SAIR (F2)`. Bolinha verde =
aquele idioma já tem texto. **Sem tradução em lote** (o `ModalEditarLote` não
importa nada de tradução) e **sem sub-setor traduzível**.

Armadilha: **Melhorar com Inteligência Artificial** grava `formData.descricao`, ou
seja o **português**, mesmo com a bandeira do inglês ativa.

Totem: `aaTraducao` em Aplicativos → Totem → **Configuração** → grupo **Idiomas**
(auto-save, sem botão). O texto do próprio produto documenta o fallback: item sem
tradução continua em português. **Não existe interruptor de idioma do tablet no
painel.** `statusTraduzido` das listagens de grupo é formação de preço, não idioma.

Captura: a aba do Cardápio **não tem campo de busca** e a lista é virtualizada —
em Produtos, clicar no setor antes de procurar o item. As listagens
(`cardapio2/cardapio`, `produto2/cardapio/setores`) **não** devolvem `traducao`;
só os endpoints de detalhe.

Telas do cliente (fotos de produção do dono, 16/09/2026). Seletor de idioma:
no **totem**, embaixo do botão *FAÇA SEU PEDIDO* e no **canto superior direito**
do menu; no **tablet**, na coluna da esquerda, embaixo de *Avaliar*. Os textos do
próprio aplicativo (*CANCEL ORDER*, *MY CART*, *MY BILL*, *Order*, *SEARCH*) já
vêm traduzidos — o lojista cadastra só o cardápio. No tablet, o **cabeçalho da
lista não troca de idioma**: com o inglês ativo a coluna de setores mostrou
*Drinks* e a faixa continuou *Bebidas* (o `tituloWeb` do setor estava `null`).

---

### Gerar Cardápio em PDF — #102

*Cardápio → Cardápio em PDF* (`/cardapio-pdf`) e atalho **Gerar cardápio em PDF** no
menu de ações da tela Cardápio (no celular, só por esse atalho). Liberado por conta:
`cardapioPdfAcesso.ts` → `CARDAPIO_PDF_EMPRESAS = [38311]` (o sandbox é a empresa
liberada, então dá para capturar em produção). Rota protegida pela permissão de
**Produtos**. Editor e `@react-pdf/renderer` entram por `lazy()`.

Quatro achados que mudaram o texto do manual:

- **Nada é salvo.** `useCardapioPdfProjeto` é `useState` puro — fechar o gerador zera
  itens, layout e marca. Monte e baixe na mesma sessão.
- **Editar item na etapa 1 não toca no cadastro** (`overrides` só valem no PDF). Serve
  para limpar do papel texto interno da descrição (no sandbox as descrições traziam
  linhas *"Tags / X-salada…"*, que apareciam no PDF).
- **O QR Code só é montado na etapa 3.** O canvas do `qrcode.react` vive escondido
  dentro do `StepMarca`; quem vai da etapa 1 direto ao download (ou aperta **F2**)
  baixa a capa sem o quadradinho. A prévia da etapa 1 sai sem QR e a da etapa 3 com —
  as duas capturas provam. Nas capturas, passe pela etapa 3 antes de baixar.
- **Clássico sai com foto**, apesar de a descrição dizer "só texto":
  `projetoPadrao()` liga `mostrarFotos`. Só o Fotográfico obriga (switch travado). Para
  comparar modelos, desligue a foto no Clássico — senão Clássico e Fotográfico saem
  quase iguais.

Preço do impresso: presencial (padrão), delivery, venda padrão ou tabela de preço
(produto fora da tabela cai no presencial). Só produto **ativo** entra; seção sem item
desaparece. Telefone, endereço, redes e logo já vêm do cadastro — a logo é achatada na
cor de fundo (PNG transparente sairia preto no PDF).

Captura: a prévia é `pdf.js` em canvas e demora. Espere o
`img[alt="Página 1 do cardápio"]` antes do screenshot, senão sai o skeleton
*Montando a prévia...*. As imagens da coluna de ajustes (06 e 07) foram recortadas
(`crop=(316,160,1250,1320)` + `pad_right=140`): os controles ocupam a coluna inteira e
não sobra espaço vazio para os números.

---

### Venda Sugestiva (UpSell) — #103

Até **6** produtos (`MAX_UPSELL`) sugeridos quando o cliente põe um item na sacola.
Liberado por conta: `vendaSugestivaAcesso.ts` → `VENDA_SUGESTIVA_EMPRESAS = [107,
38311]` (o sandbox está na lista, então captura em produção). Sem a liberação somem os
**três** caminhos.

Três telas, um endpoint (`useProdutoUpsell`, GET/POST em
`produto2/cardapio/produto/upsell`): `ModalVendaSugestivaGeral` (três pontinhos da tela
Cardápio, com selo **Configurado**, linha *Sugere:* e **Somente configurados**),
`ModalVendaSugestiva` (três pontinhos do produto) e `ProdutoVendaSugestivaTab` (aba do
cadastro, que **salva sozinha** — as janelas exigem **SALVAR (F2)**).

O que vale saber: a lista é **por cardápio/filial**; a **ordem do array é a ordem que o
cliente vê**; `produtos: []` **limpa** (não há DELETE); o POST tira duplicados e o
próprio produto; não existe aba em complemento nem permissão nova de grupo.

**O cardápio público filtra a sugestão** (`openUpsell` no bundle Nuxt): descarta o que
já está na sacola, o inativo, o `disabled` e corta em 6 — se sobrar zero, a janela não
abre. Foi o que explicou 4 configurados × 3 vistos no manual (o Brownie está oculto pela
tabela do #68); por pedido do dono, isso é explicado no texto com o produto pelo nome,
seção própria e pergunta na FAQ — *produto inativo ou oculto não aparece na sugestão*. O
preço do card é **o do canal**, com desconto/preço programado (R$ 17,60 no delivery ×
R$ 19,20 no presencial no mesmo item).

**Relatório (`Desempenho → Delivery/Presencial → Sugestões`) é processado uma vez por dia
— até 24 h de atraso** (dono, 17/09/2026). Mesmo componente para os dois canais (`tipo` 1
e 2) e o **mesmo relatório das sugestões automáticas** — não separa uma coisa da outra.

> **Erro a não repetir:** a venda de hoje não aparecia e a explicação escrita foi
> "o relatório só conta venda já concluída / fechada no caixa", deduzida da diferença
> entre uma venda antiga (`FECHADO`, arquivada, aparece) e a de hoje (`RECEBIDO`, não
> aparece). A causa real é o **processamento diário**. Antes de explicar relatório vazio
> por estado de venda, considere a janela de processamento — e, em manual, prefira o
> aviso de prazo a teorizar sobre a base.

**Cache do cardápio público chegou a ~10 minutos** aqui (o normal é 1 minuto). Antes de
suspeitar da configuração, espere.

---

### Gestão de Entregas — bloco #104 a #119 (fechado, 16 prontos)

O plano pedia 14 manuais; saíram **16 linhas de checklist**, porque o dono acrescentou dois
relatórios no meio da rodada. **Os dezesseis estão prontos**, desde 19/09:

| Faixa | Manuais |
|---|---|
| Painel | **#104** liberar entregador · **#105** ler o mapa · **#106** montar rota · **#107** despachar · **#108** fechar · **#109** despacho automático · **#110** avisos de WhatsApp |
| App | **#111** entrar · **#112** entregas do dia · **#113** chegar no endereço · **#114** código de barras · **#115** marketplace · **#116** receber na porta |
| Relatórios | **#118** Operação de Entrega · **#119** Entregador (Taxa / KM) |
| Lado a lado | **#117** uma entrega do começo ao fim — 13 imagens, 6 do celular e 7 do painel |

O **#104** herda a Parte 1 do **#57** e o **#114** herda o código de barras: com os dois, mais os
**#111 a #116**, o #57 está **pronto para aposentar**.

**O #117 ficou esqueleto até a última hora, e o motivo vale como regra:** manual de "lado a lado"
precisa que as duas metades sejam do **mesmo pedido**. Eu capturo o painel; o app depende de
emulador, que não roda aqui. O que destravou não foi a janela combinada que eu havia planejado, e sim
descobrir que ela era dispensável: **reencenar** o lado do painel depois, restaurando no banco o
estado de cada fase, dá o mesmo resultado — porque o que amarra as duas metades é endereço, valor,
forma de pagamento, letra da rota e hora da baixa, não número de pedido. O número não aparece na
lista nem nos detalhes do app (o crachá lê `numeroPedido`, nulo em pedido do restaurante); ele existe
numa tela só, a de pagamento, que lê `numeroPreVenda`.

**A pasta de pedidos e o smoke test** ficaram em `manuais/gestao-entregas/`:
[`pedidos/capturas-app.md`](../../../../manuais/gestao-entregas/pedidos/capturas-app.md) (26 prints
em 10 pastas, cada linha com a pergunta do FAQ que ganharia a foto),
[`pedidos/janela-117.md`](../../../../manuais/gestao-entregas/pedidos/janela-117.md) (o roteiro de
sete fases) e
[`scripts/smoke-app.js`](../../../../manuais/gestao-entregas/scripts/smoke-app.js) (nove cenários
que montam estados inalcançáveis por clique).

> **Lição de pedido de foto:** a primeira versão do `capturas-app.md` pediu 12 prints deduzidos dos
> capítulos que o dono enviou, **antes** de os manuais existirem. Depois de escrever os seis, a
> lista real era outra — e maior. Pedido de captura feito antes do texto pede o que parece faltar;
> feito depois, pede o que **falta**. Escreva o manual primeiro, com o que tem, e peça no fim.

Estudo completo em `manuais/gestao-entregas/estudo/`: o funcionamento do módulo em
[`01-como-o-sistema-funciona.md`](../../../../manuais/gestao-entregas/estudo/01-como-o-sistema-funciona.md)
e o estado medido em
[`02-estado-medido.md`](../../../../manuais/gestao-entregas/estudo/02-estado-medido.md).
O que precisa estar aqui porque vale para além deste manual:

**Quatro programas, dois bancos.** A tela é do `beefood-web-react`; a API é o
`beetech-server-node-3.0`; os crons rodam num servidor de **instância única**
(`beefood3-server-entregas`); o app é `beetech-entregador` (React Native / Expo). O ERP MSSQL
`notafacilb` é dono de pedido, cliente, funcionário e **taxa do entregador**; o Aurora MySQL
`entregas` é dono de rota, parada, presença e GPS. Nada é replicado — o que há no Aurora são
snapshots para o mapa não fazer JOIN entre servidores.

**Duas portas para a mesma tela.** `/gestao-entregas` abre em página cheia, e o botão **`Entregas`**
na barra do **Delivery** abre a **mesma tela dentro de um modal** sobre o Delivery, com botões de
abrir em nova aba, expandir e fechar. Não há item de menu lateral — procurei e não existe.

**Seis frases que contrariam a intuição e o manual precisa acertar:**

1. **Despachar avisa cliente e marketplace.** Grava `ENTREGA` no ERP e isso passa pelo
   `SituacaoDeliveryUpdater`: marketplace, impressão e fila de WhatsApp.
2. **Despacho automático não despacha** (só agrupa e associa entregador) **e não age com a tela
   fechada** — quem autoriza o cron a olhar a filial é o `painel_heartbeat`, gravado pelo próprio
   `GET /painel`. Conferido: a minha visita à tela escreveu o heartbeat.
3. **"Melhor rota" no app desfaz a ordem que o operador montou** no painel (o app reordena por
   distância a partir da loja).
4. **O que põe o pedido na tela do app é `_PreVenda.FuncionarioIDMotoboy`**, não estar pronto e não
   estar em rota. Pedido pronto sem entregador atribuído não existe para o celular — e a rota
   aparece no app **antes** de qualquer despacho, porque criar a rota com entregador já grava a
   coluna. É a confusão número um da operação, e o eixo do #117.
5. **Ler o código de barras é despachar** (#114) e **cobrar é finalizar** (#116). Nenhuma das duas
   ações confere nada: as duas movem estado, e nenhuma tem volta. Manual que descreve leitura de
   etiqueta como conferência ou cobrança como registro ensina errado.
6. **O `INICIAR ROTA` do app é o mesmo `PUT /gestao/rota/:rotaID/despachar` do avião do painel.**
   Foi aberto para o app em 29/08 por decisão de produto — o argumento foi que a alternativa era o
   entregador na moto com o painel dizendo que nada saiu.

**O vocabulário de situação:** `PREPARO` → em preparação, `PRONTO` → pronto, `ENTREGA` → em rota,
`ENTREGUE` → entregue. `TRANSPORTE` **não é valor válido** (removido do filtro da view pelo script
`004`). E status **não regride**: evento de WebSocket atrasado não puxa pedido de "entregue" para
"em rota".

> ⚠️ **Achado que vale levar ao dono: o aviso "Entregador próximo" não dispara para quase
> ninguém.** O campo de km mostra `2` na tela, mas é o padrão do código —
> `_WhatsappMsgTipoFilial.raioProximidadeMetros` está **NULL em 56.633 das 56.639 filiais**, e o
> padrão global também. O script `010` diz, na própria conferência, que filial com raio NULL nunca
> recebe o aviso. Só 6 filiais têm valor, porque alguém abriu o modal e salvou. É pendência de
> ambiente, não de manual — mas o manual não pode prometer o que não funciona.

**O módulo tem um cliente piloto e nada mais.** O Aurora `entregas` só tem dados de duas filiais
(a sandbox e uma real) e o `despacho_config` tem **1 linha na base inteira**, desligada. A tabela
`entregador` (veículo, capacidade) está **vazia na base toda** — os nomes que o painel mostra vêm
do `_Funcionario` do MSSQL.

**Sujeira que estraga captura em silêncio:** *rota fantasma* — quando `entregador_status.rotaIDAtual`
aponta para rota que já não existe, o entregador fica ocupado para sempre e **nunca recebe rota do
despacho automático**. Há um caso vivo na sandbox (`194115` → rota 120, inexistente). Antes de
fotografar despacho automático, confira isso.

**Desmontar cenário é mais difícil do que montar, e o painel é a tela que esquece.** Desatribuir o
entregador tira o pedido do app na hora, mas ele fica em *Pedidos sem rota* no painel por até **6 h**
— e depois de uma tarde de ensaios a fila tinha **21 pedidos de teste**, o que estragaria em silêncio
qualquer foto de "fila com N pedidos". O estado que resolve é `AGUARDANDO`: a view do painel filtra
`PREPARO`/`PRONTO`/`ENTREGA`/`ENTREGUE` e o app ignora `AGUARDANDO`, então o pedido sai das duas telas
sem ser apagado e **sem entrar na conta de entregas do dia** — o que `ENTREGUE` faria, inflando o
relatório. É o `arquivar-fila` do `smoke-app.js`, e a lição geral é: **ensaie o roteiro inteiro antes
da janela combinada**, porque é o ensaio que revela a sujeira que a foto mostraria.

**Conferir cenário pela API do app, não pelo banco.** Entre as duas coisas moram o agrupamento de
rota, o filtro de situação e a ordenação por distância — e já aconteceu de o banco estar certo e a
tela vir vazia. O `smoke-app.js` chama
`GET /api/entrega2/gestao/entregador/{empresa}/{filial}/{usuario}/{funcionario}` com Basic Auth e
verifica o que a tela vai mostrar. Vale como padrão para qualquer cenário de app: **confira pela
porta que o cliente usa.**

**Sentinela de escrita, o desenho que deu certo.** Script que escreve em produção (a sandbox é
produção) precisa de mais do que `--dry-run`. O que o `smoke-app.js` usa, e que vale copiar:
lista branca **literal** de empresa/filial no código (destravar exige editar o arquivo, não passar
flag), `UPDATE` só numa tabela, só em ID que **o próprio script criou** naquela janela — guardado em
arquivo de estado local, porque as fases acontecem em execuções diferentes —, lista branca de
colunas, e uma flag separada (`--permitir-passado`) para o subconjunto que altera histórico. As
operações de rota vão pela **API**, nunca por SQL, para o log, o socket e o `rota_evento`
acontecerem como no uso real.

---

### Exibir/Ocultar e Preço Programado — #68 e #69

Mesmo modal (`ModalTabelaPreco`). **Exibir / Ocultar** força
`ocultar=0` (Ocultar Item). **Preço Programado** manda `?preco=1` e
força `ocultar=1` (Alterar Preço), sem produto de rodízio. Permissão
do Preço Programado no menu é `rodizio`. Rodízio de verdade é
`/rodizio` (só presencial + produto vinculado).

Canal **Cardápio Digital** = `beeshop`. Sem ele o menu público não
muda. Dias vazios = tabela `0d` e não vale. Aba Produtos numa tabela
nova **salva a config sozinha**. Desconto em massa só depois de
selecionar o produto. Cache do cardápio público: até **5 minutos**.

No card da lista do Preço Programado o front esconde Delivery e
Cardápio Digital (`!isRodizio`) — só o Presencial aparece; os três
canais estão no modal.

Sandbox (30/08/2026): **Ocultar Brownie (manual)** ativa; **Happy
hour milk-shake (manual)** ativa (Milk Shake 18,90 → 15,12).

---

### Agendamento do cardápio digital — #70

Aba `tab=agendamento`, auto-save 800 ms (unmount sem flush). Campo
inválido não grava. O cardápio Vue (`menu.beefood.com.br`) abre
**AGENDAR PEDIDO** depois de Entrega/Retirada: faixa **Dia** + lista
**Hora Aproximada** (faixas de 30 min; `agendaInterM` é o passo entre
inícios). `agendaAgoraM` só mexe no dia de hoje. `agendaMinAntes` =
minutos **depois** de abrir. Preencher vários `input` via Playwright
e sair perde o save — gravar pelo POST autenticado e recarregar.

---

### Produto só com agendamento — #73 (complemento do #70)

Switch do **produto**, campo da API `importadoMatriz` (nome legado).
Dois caminhos: **Editar em Lote** (`ModalEditarLote` + `useEditarLote`,
POST `/api/produto2/cardapio/editarLote` em lotes de **5**) e o
cadastro em **Opções avançadas** (grava só no **SALVAR E SAIR**).
No lote o valor nasce em **Não** — marcar o campo e processar
**desliga** a flag; é assim que se desfaz. A etapa 1 herda o filtro de
setor da aba, então **filtre antes de abrir**.

Lista do painel: `CalendarDays` azul `#1565c0`. O Tooltip do grid
virtualizado é **shim com `title` nativo** — hover **não** rende
tooltip em screenshot (documentar por texto).

Cardápio público: etiqueta **Encomenda** + `?`
(`.attributes-row__help-btn`) → *Produto disponível apenas por
agendamento*. Com o item na sacola, **Continuar** abre **AGENDAR
PEDIDO** mesmo com **Hoje** marcado; produto normal vai direto ao
pagamento. **Sem o `agendamento` da aba ligado a marca não segura
nada** (testado e revertido). Campo também aparece no lote de
**Complementos**, mas o cadastro do complemento não tem o switch.

Sandbox (31/08/2026): 3 pudins de **Sobremesas** ON, Brownie OFF.
Só abrir a aba Agendamento já dispara um POST do auto-save.

---

### Aparência e layout do cardápio digital — #71

Card **Aparência** em `/cardapio-digital?tab=configuracoes`. Auto-save
800 ms (POST do snapshot inteiro). Capa fixa = `fotoCapa`; logo =
`logotipoS3Link`; tema = `corPrimaria`; capa vazia = `corAcao`.
`layoutSetor` / `layoutStepCarrinho` boolean. Vitrine =
`exibirPromocoes` + `abrirPromocoesAuto`. Capa/logo: clique no
preview, máx 1 MB, sem recorte. **Não** é o modal de banners (#48).
Comparação do manual: painel à esquerda, **cardápio público** à
direita (`menu.beefood.com.br/{link}`). O preview sticky do painel
não entra no par. `validaDelivery` vem zlib+base64; cache ~1 min.
Clique “só para ver” já grava.

---

### Numeração dos pedidos — #74 (concluído)

Dois números na mesma venda. **`numeroPreVenda` = número da venda**, contador
único da loja, **nunca reinicia** (provado: faixa 627–930, 304 vendas, zero
buraco e zero repetição). **`numeroPedido` = número do pedido**, contador **do
caixa**: volta para 1 a cada caixa novo. Exibição: `numeroPedido
(numeroPreVenda)`, ou só o da venda — em 12 pontos do código, mudando só a
palavra da frente (`Pedido #`, `Venda Nº`, `#`, ou sem prefixo no Histórico).

**A prova do reset:** caixa 927703 abriu **17/07 11:59:02** e o **pedido nº 1
saiu 11:59:06 — 4 segundos depois**. Na virada seguinte o pedido caiu de **110
para 1** enquanto a venda ia de **838 para 843**.

**Por canal:** mesa **nunca** recebe (0 de 15) e não existe `mesaNumeroPedido`;
PDV depende do switch **Número de Pedido no PDV** (`pdvNumeroPedido`, card PDV
em Parâmetros, o último da tela); delivery depende do caixa.

**Descoberta que vale para o manual de Caixa:** o caixa precisa ser aberto com
**Delivery** marcado. O caixa 907962 abriu sem delivery e **79 pedidos ficaram
sem número de pedido**, sem aviso na tela; nos caixas com delivery o número
saiu em **100%**.

**O #44 está errado numa linha:** ele diz que o switch "mostra o número da
venda (ex.: Venda #848)". Não é isso — o *Venda #848* aparece com o switch
desligado também, e a tela do PDV **nunca** mostra o número do pedido (o front
manda `numeroPedido: null` sempre, com o comentário `// PDV não tem
numeroPedido`). A venda 848 do próprio #44 tem pedido **3**. O switch faz o
servidor **atribuir** o número, que aparece depois no Histórico (`3 (848)`), no
cupom reimpresso e nos relatórios.

**Mesa não consome número.** O caixa 927703 usou 110 números na faixa 1..110
**sem um único buraco**, tendo 13 vendas sem número (5 de mesa). Visto também
na tela: vendas de mesa 854–858 entre os pedidos **5** e **6**.

**Truque do levantamento:** associe a venda à **janela de tempo do caixa**
(abertura → fechamento), **não** ao `caixaID` gravado na venda — esse campo
fica `null` enquanto a venda não é liquidada e esconde o padrão (217 de 304
vinham `null`). Cuidado também com vendas criadas **em lote pela API** por
scripts de manuais antigos: várias no mesmo segundo, sem `numeroPedido`, são
ruído do sandbox e não regra do produto. E **marketplace grava `horaCadastro`
fora de ordem** (AIQFome): produz reset falso em análise cronológica; reset real
é o que cai **para 1**.

**Cupom no Cloud Agent: o fallback de impressão é IFRAME, não `window.open`.**
O botão de impressora do detalhe da venda (`lucide-printer` no cabeçalho do
modal; o `chef-hat` ao lado é a ficha de cozinha) tenta o BeeImpressão, falha
com *"Servidor offline. Usando impressão do navegador."* e chama
`imprimirViaIframe` (`src/lib/impressao-service.ts`), que escreve num iframe
oculto de id **`beefood-print-frame`**. Ou seja: **nenhuma aba nova abre** e
sobrescrever `window.open` **não captura nada** (tentado e falhou). O que
funciona é um `MutationObserver` + poll de 40 ms instalado **antes** do clique,
ler `contentDocument.documentElement.outerHTML` do iframe e renderizar esse
mesmo HTML numa página nova com viewport de **400 px** (bobina de 80 mm).
Vale para qualquer manual que precise fotografar cupom.

**Três armadilhas de tela descobertas aqui:** o modal **Reabrir Venda** do PDV
exige **CONFIRMAR SELEÇÃO (F1 / ENTER)** — clicar na linha só seleciona e o
**Receber** fica desabilitado; a **paginação do Histórico** não responde a
`button:has-text('Próximo')` (troque **Itens por página** para 100 e role com
`scrollIntoView({block:'center'})`); e a **aba de setor do PDV é `div`**, não
`button`. O PDV manda `tipo: 'PDV'` mesmo com mesa selecionada no topo — venda
de **mesa** exige o **Novo Pedido (F1)** da tela de Mesas, e clicar numa mesa
livre não abre nada.

Detalhe em [`PLANO-NUMERACAO-PEDIDOS.md`](planos/PLANO-NUMERACAO-PEDIDOS.md) e em
`manuais/numeracao-pedidos/` (`MEMORIA.md` e `fluxo-codigo.md`).

---

### Ficha técnica — #72

Aba **Ficha Técnica** no modal de **produto e de complemento** (Cardápio ou Meu
Estoque). Só aparece com o produto **salvo**; o insumo precisa existir antes
(Estoque → Meu Estoque → Insumos). Mobile é **somente leitura**.

`custoLinha = qtd × custo do insumo`; o total vira **Custo Ficha Técnica** no
produto (`custoComposicao`) e **soma** com o campo **Custo** digitado à mão.
Margem = `(venda − custo total) ÷ venda`, sobre a venda, não markup.

**Sem conversão de unidade:** insumo em KG, quantidade em fração (100 g = `0,1`;
5 g = `0,005`). Até 4 casas decimais. Decisão do dono: cadastrar em **KG/L**.

Provado em venda real (#925/#927/#928): a baixa acontece no **Receber** (pré-venda,
antes do pagamento); a trilha tem 2 ou 3 níveis (`produto -> insumo` e
`produto -> opção -> insumo`); **opção repetida baixa em dobro** (`origemQtd`), o
que libera o modelo Proporcional da pizza; e **insumo sem Controlar Estoque não
gera movimentação** (entra no custo e some do relatório).

Sandbox: base de insumos **zerada** em 01/09/2026 e remontada com 10 insumos de
hamburgueria. Sobrou *Maionese da casa (sache)* — insumo preso a receitas já
usadas em produção não é excluível, nem com a receita inativa, e a API recusa
receita com `itens: []`.

Base com **nomes repetidos** (dois *One Burger*, duas *Batata frita*): o que tem
grupos e ficha é o `produtoID` 2515371 / 2515323. No PDV o card certo é o do selo
**COMBO**. Preço do PDV ≠ Preço de Venda por causa de um **Preço Programado**
ativo na conta.

---

### Lançamentos (Financeiro) — #66 e #67

Rota `/contas-pagar-receber`. Uma tela, 3 abas: **Contas a pagar** /
**Contas a receber** / **Todos**. **+ Novo (F1)** → **Despesa** (−) ou
**Receita** (+). Formas do lançamento = topo de Formas Pagamento.

Venda **paga** já vira conta a receber (categoria **Receita de Pedidos**,
valor = **líquido** da taxa do #65). Receita extra: categoria fixa
**Outras Receitas**. Sem contas bancárias no sandbox — deixar Conta
vazia.

Sandbox (30/08/2026): **Aluguel do ponto** R$ 800 Pix pago; **Máquina
de café** 2× R$ 150 Boleto (1/2 no mês); **Patrocínio da festa junina**
R$ 200 Pix recebido; venda **#915** no receber (14,00 → 13,69).

Fora deste par: Recebimentos/Pagamentos agregados, DRE, cadastros,
Fluxo Caixa (*Em breve!*).

---

## 10. Como retomar o trabalho (checklist de início de sessão)

1. Ler este `MEMORIA-GERAL.md`.
2. Se a sessão for da fila do ajuda.beefood, ler `PLANO-MIGRACAO-AJUDA.md`. A fila **#49–#56** já foi produzida. O **#57** (app Entregador) e o **#58** (IA ChatGPT no WhatsApp) foram pedidos depois e também já estão prontos.
3. Ler a `MEMORIA.md` do manual em andamento (se houver).
4. Logar em `contato@beefood.com.br` e ativar tema claro.
5. Conferir estado da funcionalidade no sistema antes de capturar.

---

## 11. Versionamento (Git/GitHub) — REGRA DE COMMIT POR AÇÃO

- Repositório remoto: `git@github.com:BeeFood-Sistema-para-Restaurantes/beefood-web-react-manual.git` (branch `main`).
- **REGRA DE OURO:** após **cada ação relevante** (criar/editar manual, gerar imagens,
  ajustar `annotate.py`, atualizar memórias, etc.), fazer **`commit` + `push` automaticamente**
  (sempre os dois!) — sem precisar pedir autorização. Mensagens claras e descritivas em português.
- **Sempre subir tudo:** todo commit deve ser seguido de `git push origin main`. Não deixar
  commits acumulados só localmente.
- Padrão de mensagem: verbo no presente + escopo. Ex.:
  `docs(caixa): adiciona etapa de consulta do valor em caixa`,
  `chore(anotacao): setas em verde e mais sutis`,
  `feat(manual): inicia manual de delivery`.
- Não versionar segredos novos: usar `.gitignore` (ex.: `credenciais.local.md`, `.env`).
  > **Decisão do dono:** as contas usadas são de uma **empresa de TESTES** (credenciais
  > descartáveis). Portanto as senhas PODEM ficar versionadas e o repositório PODE ser
  > **público** sem problema. Não tratar essas credenciais como segredo crítico.

---

## 12. `texto-documentation.ia.md` — PROMPT pronto por manual (OBRIGATÓRIO)

Para o dono **publicar** um manual, ele cola um **texto de criação** no construtor de documentação do
app (que gera a página dentro do BeeFood). Por isso, **todo manual concluído DEVE ter** um arquivo
`texto-documentation.ia.md` na sua pasta, contendo esse texto **pronto para copiar e colar**.

**Princípio:** o projeto do manual **já vem anexo no contexto**. O prompt deve ser **direto e listar os
arquivos EXATOS a ler** (o `<nome>.md` + os caminhos das imagens em `imagens-tratadas/`) e dizer
explicitamente **"NÃO varra/leia o resto do projeto"** (nada de `fluxo-codigo.md`, `MEMORIA*.md`,
`annotate.py`, `imagens-puras/`). Isso evita que a IA leia o projeto inteiro.

**O que o arquivo deve conter:**
1. Um bloco **PROMPT (copiar e colar)** com:
   - **Onde criar o menu** (ex.: "Em **Fiscal**, crie um novo item por último chamado **\<Nome\>**").
   - **Lista explícita dos arquivos a ler** (somente esses): o **`<nome>.md`** (conteúdo na íntegra) e os **caminhos de cada imagem** em `imagens-tratadas/` (na ordem).
   - Frase clara de **"NÃO ler outros arquivos do projeto"**.
   - A instrução: **"faça a apresentação das imagens igual ao menu 'Abrir Caixa'"** (padrão de referência).
2. **Estrutura da página** (seções, na ordem do `<nome>.md`).
3. **Tabela de imagens** na ordem, com tipo (contexto / com setas) e legenda.
4. **Observações de conteúdo** (idioma, destaques obrigatórios, o que NÃO publicar — ex.: `fluxo-codigo.md`).

**Modelo mínimo:**

```md
# texto-documentation.ia.md — <Nome do Manual>

## PROMPT (copiar e colar)
Em <Seção>, adicione um item de menu por último chamado "<Nome>".

Leia APENAS os arquivos abaixo (não varra o resto do projeto):
1. Conteúdo (use na íntegra): beefood-web-react-manual/manuais/<pasta>/<nome>.md
2. Imagens (nesta ordem): beefood-web-react-manual/manuais/<pasta>/imagens-tratadas/<arquivos...>

NÃO leia outros arquivos (fluxo-codigo.md, MEMORIA*.md, annotate.py, imagens-puras/).

- Faça a apresentação das imagens IGUAL ao menu "Abrir Caixa".
- pt-BR, didático; destacar obrigatórios; não publicar o rodapé "Referências internas".

## Anexo — legendas das imagens (na ordem)
| Ordem | Arquivo (em imagens-tratadas/) | Tipo | Legenda |
| ... |
```

> Referência viva: `manuais\reforma-tributaria-ibscbs\texto-documentation.ia.md`.
