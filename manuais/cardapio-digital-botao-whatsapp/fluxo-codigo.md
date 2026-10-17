# Fluxo de código — Botão de WhatsApp do Cardápio Digital (#128)

O que a tela faz de verdade, lido no `beefood-web-react` (painel) e no **bundle publicado** do
cardápio do cliente (`menu.beefood.com.br`, Nuxt, repositório que não se clona — a técnica é a
do #125). Não é conteúdo de manual: serve para o texto do manual não prometer o que o código
não faz.

## Onde a aba mora

| Peça | Arquivo |
|------|---------|
| Aba no painel | `src/pages/CardapioDigital.tsx` — `{ id: 'whatsapp', label: 'Botão WhatsApp', icon: MessageCircle }`, a **última** da lista |
| Mesma aba no celular | `src/components/mobile/cardapio-digital/MobileCardapioDigitalPage.tsx` — mesmo componente, com `mobile` |
| Formulário | `src/components/cardapio-digital/WhatsappTab.tsx` |
| Prévia | `src/components/cardapio-digital/preview/PreviewBotaoWhatsapp.tsx` e `PreviewCardapioDigital.tsx` |
| Regras e validação | `src/utils/whatsappBotao.ts` |
| Carga e gravação | `src/hooks/useCardapioDigitalWhatsapp.ts` |
| Liberação por empresa | `src/utils/whatsappBotaoAcesso.ts` |

Rota: `/cardapio-digital?tab=whatsapp`.

## Quem vê a aba — e por que ela pode não aparecer

Duas travas, e as duas precisam passar:

1. **Grupo de acesso.** `usePermissions.ts` mapeia o item `whatsapp` do submenu
   `cardapioDigital` para a permissão **`botaoWhatsApp`**.
2. **Lista de empresas.** `WHATSAPP_BOTAO_EMPRESAS = [107, 38311]` em `whatsappBotaoAcesso.ts`,
   conferida dentro do próprio `usePermissions`. O comentário do arquivo diz que é
   *"trava temporária até o grupo de acesso normalizar para todos"*.

O sandbox dos manuais (**empresaID 38311**) está na lista, e é por isso que este manual
existe agora. **Em conta fora dessas duas a aba não aparece**, mesmo com a permissão ligada —
é a primeira coisa a dizer no manual e a primeira linha da tabela de defeitos.

## O que grava, e quando

**Não há botão Salvar.** `useAutoSave` grava sozinho, e o aviso é um toast
*"Salvo automaticamente"*:

```ts
useAutoSave({ data: form, enabled: carregado && !bloqueado, onSave: async (snap) => ... });
```

`bloqueado` reúne as quatro recusas — e enquanto uma delas vale, **nada é gravado**:

| Recusa | Função | Mensagem na tela |
|--------|--------|------------------|
| Horário invertido | `horarioInvalido` | *O horário inicial precisa ser menor que o final.* |
| Ligado sem telefone nenhum | `semTelefone` | *Informe um telefone: a filial não tem WhatsApp no cadastro.* |
| Telefone incompleto | `foneInvalido` | *Informe o número completo: DDD e telefone.* |
| Mensagem acima do limite | `form.msg.length > regras.maxMsg` | contador fica vermelho |

Com DDI 55 o número tem de ter **10 ou 11 dígitos** depois do DDI; com outro DDI, de **10 a
15** no total.

### As duas rotas

```
GET  /api/empresaDelivery2/cardapioDigital/whatsapp/{empresaID}/{filialID}/{usuarioID}
POST /api/empresaDelivery2/cardapioDigital/whatsapp
     { empresaID, filialID, usuarioID, usuario, whatsapp: <documento> }
```

A configuração é **por filial** — o `filialID` entra na URL. Loja com mais de uma filial
configura uma por uma.

### O GET traz as regras, não só a configuração

Medido na conta do sandbox: `maxMsg 300`, `maxRotulo 30`, `maxSub 60`, `tamMin 80`,
`tamMax 140`, `tamPasso 5`, `layoutsTamanhoFixo {"fabMini": 75}`, mais `layoutsPorPosicao`,
`layoutsSemFundo`, `layoutsComSub` e o `telefoneCadastro` da filial. O
`src/utils/whatsappBotao.ts` tem os mesmos valores, **mas só como fallback** — o
`AGENTS.md` da pasta explica o motivo: formato novo no servidor aparece no painel **sem novo
deploy**. Consequência para o manual: **não vale afirmar "existem 14 formatos"** como número
de produto, porque a lista é do servidor. O texto fala de "oito formatos flutuantes" só onde
a própria tela escreve isso.

### O que o painel limpa antes de mandar (`paraPayload`)

- `lay` é **corrigido para a posição**: trocar de posição mantém o formato se ele valer ali, e
  cai no primeiro da lista se não valer (`ajustarLayout`).
- `rot` vazio volta para **"Falar no WhatsApp"**; `sub` só sobrevive nos formatos da lista
  `layoutsComSub` (`card`, `cardLogo`, `selo`).
- `pulsar` é forçado a `false` nos formatos sem fundo preenchido.
- `hIni`/`hFim` viram `null` quando *Dia inteiro* está ligado.
- `tam` é arredondado para o passo de 5 e preso entre 80 e 140 — e ignorado nos formatos de
  tamanho fixo.

Ou seja: **meia configuração não chega ao cardápio**. O que o cliente vê é sempre um
documento coerente.

## A decisão de aparecer, nos dois lados

`botaoNoAr()` (painel) e a `visivel()` do bundle do cardápio aplicam a mesma lista:

1. `on` ligado;
2. telefone (próprio ou do cadastro) com **10 dígitos ou mais**;
3. o canal da visita está em `ctx` (Delivery / Presencial);
4. o aparelho está em `disp` (`M` celular e tablet, `D` computador);
5. `quando` combina com a loja estar aberta (`sempre` / `aberta` / `fechada`);
6. o dia da semana está em `dias` (domingo = 1);
7. estando fora de *Dia inteiro*, a hora está em `[hIni, hFim)`.

O relógio é o **do aparelho do cliente**, como nos banners e nos avisos — a própria tela
escreve isso.

### O que a prévia **não** respeita, de propósito

A prévia desenha o botão mesmo quando a configuração o esconderia, e marca o desenho com um
contorno tracejado. Enquanto o controle de **Tamanho** está com foco, ela também ignora a
regra de loja aberta e abre o espaço da sacola, para o tamanho que está sendo arrastado não
desaparecer da tela. É o que o `AGENTS.md` da pasta chama de *"previews always render the
selected button independently of publication conditions"*. No manual isso virou uma frase: a
prévia mostra **o desenho**, não a decisão de publicar.

## O lado do cliente (bundle publicado)

O cardápio lê **`whatsappJson`** e **`telefoneWhatsApp`** do payload da loja
(`listaBeeshopDetalhe/.../empresa/...`) e normaliza com guardas próprias:

- `v > 1` → devolve `null`. **Versão futura do documento desliga o botão em cardápio
  antigo**, em vez de desenhar errado.
- `on !== true` → `null`; telefone com menos de 10 dígitos → `null`.
- `pos` e `lay` são conferidos contra as mesmas listas do painel; `tam` é preso entre 80 e
  140, e `fabMini` vira 75.
- `rot` vazio cai em **"Fale no WhatsApp"** (o padrão do cardápio; o do painel é *Falar no
  WhatsApp*).

O link é montado na hora do clique:

```js
montarLink() { return "https://wa.me/" + cfg.fone + "?text=" + encodeURIComponent(mensagem()) }
mensagem()   { return cfg.msg.replace(/\{loja\}/g, nomeLoja).replace(/\{link\}/g, location.href) }
```

Dois fatos que vieram daí e entraram no manual:

- **`{link}` é o endereço da página em que o cliente clicou**, não a home do cardápio: quem
  clica dentro de um produto manda o link daquele produto.
- O elemento é um `<a>` com classe `be-wa__alvo` — é por ele que o `capturar.py` confere se o
  botão está no ar antes de gravar o print.

### Folgas do flutuante, medidas no bundle

| Onde | Distância da lateral | Distância do rodapé |
|------|---------------------|---------------------|
| Computador | 24 px | 24 px |
| Celular, sacola vazia | 16 px | 68 px |
| Celular, com itens na sacola | 16 px | 118 px + `safe-area-inset-bottom` |

É isso que sustenta a frase *"fica acima da barra da sacola, sem cobrir o botão de
finalizar"*. O formato **Pílula que recolhe** só recolhe no celular, e a partir de 56 px de
rolagem.

### Cada clique vira evento no Pixel

`trackWhatsappContact` dispara o evento **`contato_whatsapp`** com `posicao`, `layout`,
`tamanho`, `loja_aberta` e `dispositivo`. O dado é gravado, mas **não há tela no painel que
mostre esse número separado** — a busca por `contato_whatsapp` no `beefood-web-react` não
devolve nada. No manual isso virou uma pergunta de FAQ respondida com o limite, não com
promessa.

## O outro WhatsApp da mesma tela

O ícone de WhatsApp que já aparecia entre as redes sociais do cabeçalho é a configuração
**Exibir WhatsApp**, da aba *Configurações*, e continua valendo em paralelo — a própria aba
avisa isso num quadro azul. São dois recursos diferentes com o mesmo logo, e é a confusão
mais provável no suporte: por isso a observação aparece no manual **e** no FAQ, escrita das
duas maneiras que o lojista perguntaria.

## O que este manual não documenta, e por quê

O pedido do dono foi explícito: *"existem muitas configurações e muitas possibilidades, não
vamos documentar tudo… a tela é autoexplicativa 100%"*. Então ficou de fora, de propósito:

- as outras quatro posições (topo, destaques, rodapé, sacola) e os formatos do corpo do
  cardápio — citados em uma linha, sem captura;
- a agenda completa (dias, faixa de horário, canais Delivery/Presencial) — uma seção curta
  sem imagem;
- subtítulo, pulsar, tamanho fora dos 100% e cor fora do verde.

Tudo isso **existe e funciona**; o manual mostra o caminho mais curto até um botão no ar e
diz onde o resto mora.
