# fluxo-codigo.md — #121 Totem de Autoatendimento: pôr no ar e configurar

Leitura do `beefood-web-react` em 22/09/2026 (`fcb00ac`). O **front do totem não
está em nenhum repositório clonado** — o que se afirma sobre a tela do cliente foi
**medido no aparelho em produção** (o totem é web e abre no Cloud Agent), não lido
em código.

## Onde a tela mora

| Arquivo | Papel |
|---------|-------|
    10|| `src/pages/Aplicativos.tsx` | o card. `app.id === 'totem'` → se `getConfigCache()?.qtdAA > 0` abre `TotemConfigModal`; **senão abre `TotemModal`**, que é a modal informativa de venda |
| `src/components/tef/TotemConfigModal.tsx` (1.568 linhas) | as abas Configuração, Pagamentos e Download, e o gerador dos `.cmd` |
| `src/components/tef/totem-aparencia/TotemAparenciaTab.tsx` + `src/hooks/useTotemAparencia.ts` | aba Aparência |
| `src/components/tef/totem-cardapios/TotemCardapiosTab.tsx` + `src/hooks/useTotemCardapios.ts` | aba Cardápios |
| `src/data/appCategories.ts` | o card: `{ id: 'totem', name: 'Totem', description: 'Autoatendimento presencial' }`, na faixa **Presencial** |

É o `qtdAA` do contrato que decide qual modal abre — é a primeira linha dos
problemas comuns do manual.

## Não existe Salvar: `update()` chama `persist()`
    20|
```ts
const update = (patch) => setData(prev => { const next = {...prev, ...patch};
                                           persist(next); return next; });
```

`persist()` faz `POST /api/totem2/configuracao` com o estado inteiro mais `log`
(o snapshot anterior) e mostra o toast *"Configuração salva"*. Em erro, ele
devolve `originalRef` para o valor antigo, para o próximo salvamento mandar o log
certo.

    30|Campo de texto usa `updateDebounced()`, com **800 ms** depois da última tecla —
vale para `aaSenha` e `aaMsgFinal`. Ao fechar o modal com salvamento pendente
(`pendingSaveRef`), ele dispara o `persist` final antes de zerar o estado: fechar
no ESC **não perde** o que foi digitado.

## Aba Configuração — campo por campo

`GET /api/totem2/configuracao/{empresa}/{filial}/{usuario}` traz tudo.

| Grupo na tela | Campo | O que o manual diz |
|---------------|-------|--------------------|
    40|| Meio de Consumo | `aaComerAqui`, `aaViagem` | com os dois ligados o totem pergunta; com um só, não pergunta |
| Impressão | `aaImp` (cupom), `aaImpSenha` (senha) | e a impressora, que é registro próprio |
| Emissão Fiscal | `aaNFCe`, `aaCPF` | NFC-e emitida pelo próprio totem |
| Observação | `aaObsProd`, `aaObsPed` | o campo de recado no produto e no pedido |
| Idiomas | `aaTraducao` | as bandeiras — é o interruptor do #100 |
| Identificação | `aaNomeT` (0 a 4) | `NOME_T_OPTIONS`: Nenhum, Nome Opcional, **Nome e Telefone Opcional**, Nome Obrigatório, Nome e Telefone Obrigatório |
| Identificação | `aaPager` / `aaMesa` | um `Select` de três estados que grava os dois campos juntos: `Desativado`, `Informar Número do Pager`, `Informar Número da Mesa` |
| Senha Administrador | `aaSenha` | só dígitos (`replace(/\D/g, '')`), com debounce |
| Acréscimo | `aaProdutoIDComer`, `aaProdutoIDViagem` | produto somado ao pedido por meio de consumo |
| Mensagem Final | `aaMsgFinal` | com debounce |
    50|
Dois valores que a tela **sugere sem gravar**, no `GET`:

- `aaSenha` vazia → o formulário mostra o `empresaID`, e isso só vai para o
  servidor quando o usuário digita (o comentário no código é explícito);
- `aaMsgFinal` vazia → o formulário mostra `"Pedido feito com sucesso!\nMuito
  obrigado!"`, que é exatamente o texto que apareceu na tela do aparelho.

**Impressora do totem** é outro par de rotas:
`GET/POST /api/totem2/configuracao/impressora/...`, com os campos do ACBr
(`impressoraDefault`, `acbrModelo`, `acbrPorta`, `acbrColunas`, bordas). A lista
    60|vem do BeeImpressão — no sandbox, `EPSON TM-T20 Receipt5`.

## Aba Pagamentos

`GET/POST /api/totem2/configuracao/formaRecebimento/...`, seis pares
liga/forma:

| Meio | Flag | Forma | Engrenagem |
|------|------|-------|------------|
| Dinheiro | `aaDinheiro` | `aaDinheiroFP` | não |
| Pix BeeFood | `aaPix` | — (não tem forma) | não |
    70|| Pix TEF | `aaPixTef` | `aaPixTefFP` | sim |
| Crédito TEF | `aaCC` | `aaCCFP` | sim |
| Débito TEF | `aaCD` | `aaCDFP` | sim |
| Vale Refeição TEF | `aaRef` | `aaRefFP` | sim |

A engrenagem do `PagamentoRow` tem `title="Configurar bandeiras e taxas"` e só
aparece quando há forma escolhida. **Pix BeeFood não tem combo de forma** —
é o Pix da operadora BeeFood.

### De onde vem o desconto que o totem mostra

    80|Medido no sandbox em 22/09/2026, com pedido de R$ 28,00:

| Cartão no totem | Desconto | Onde está configurado |
|-----------------|----------|------------------------|
| Dinheiro → R$ 27,72 | 1% | **Cadastros → Formas Recebimento**, forma *Dinheiro* = `1,00%` |
| Pix → R$ 26,60 | 5% | **Cardápio Digital → Pagamento Online → PIX Online** = *Desconto de 5,00%* |

O changelog do produto (`src/data/changelog.ts`, *"Desconto ou acréscimo por
forma de pagamento"*) confirma a regra: o ajuste é cadastrado na forma e o
**Totem de Autoatendimento** aplica "a mesma regra na finalização do pedido".
    90|Cuidado com a pegadinha: o mesmo *Dinheiro* em **Cardápio Digital → Formas
Recebimento** está com 5% no sandbox, e **não** é esse o valor que o totem usou.

## Aba Aparência

`useTotemAparencia.ts`:

- `GET/POST /api/totem2/configuracao/aparencia/{empresa}/{filial}/{usuario}` — tema, cor principal;
- `GET/POST/DELETE /api/totem2/configuracao/imagem/...` — logotipo, capa e slides (`tipo` na rota);
- o texto do formato de vídeo é literal do componente: *"Para vídeos: MP4 H.264,
  até 1080×1920, 4–6 Mbps. HEVC/H.265 e 4K não funcionam no totem."*
   100|
## Aba Cardápios

`GET/POST /api/totem2/configuracao/cardapios/...`. A loja principal vem com
`disabled` no switch (etiqueta *Principal*) e filial com `cardapioAdicional ===
false` aparece opaca, com o selo *Cardápio Digital não habilitado*.

## Aba Download

`totemUrl` é montada no componente:

   110|```ts
const aaToken = matriz?.aaToken ?? '';
const totemUrl = `https://totem.beefood.app/?empresaID=${empresaID}&filialID=${filialID}&token=${aaToken}`;
```

O `aaToken` mora no `config_cache` (`src/utils/configCache.ts`) — é por isso que
o manual trata a URL como senha.

Os dois `.cmd` (`BEEFOOD_TOTEM_<loja>_EDGE.cmd` e `..._CHROME.cmd`) são gerados
no próprio front, como string. Além de abrir `--kiosk`, eles:

   120|- liberam `LocalNetworkAccessAllowedForUrls` para `https://totem.beefood.app`
  (acesso ao pinpad/impressora na rede local);
- escrevem `C:\Beefood\Totem\beefood-totem-close.cmd` e registram o protocolo
  `beefoodtotem:` — é o que permite **fechar** o totem pela tela de
  administração, já que `window.close()` é bloqueado no modo kiosk.

O manual não detalha o registro do Windows: para o lojista, o que importa é
salvar no Desktop e dar duplo clique.

## A foto do setor

   130|`src/components/ModalEditarSetor.tsx` — o botão **ADICIONAR FOTO** tem a legenda
*"(Foto para exibição no AutoAtendimento em Tablet)"*, e é o mesmo `s3Link` que a
rota do totem devolve.

Medido por interceptação das respostas no próprio aparelho (21/09/2026):

| Foto em… | Efeito no totem |
|----------|-----------------|
| **Setor** (`s3Link` de `/api/totem2/setores`) | injetando foto, a coluna da esquerda deixa de ser texto e vira miniatura + nome |
| **Produto** (`s3Link` de `/api/totem2/produtos`) | tirando a foto, a grade de três colunas **não muda** e o cartão exibe o ícone de imagem quebrada |

   140|A prova publicável não é a interceptação: as fotos dos **sete setores** foram
subidas de verdade pelo Banco de imagens, e o par de capturas (10 e 13) é o
mesmo cardápio antes e depois.

**Correção de 22/09/2026 (feita no #124).** A regra completa do trilho é
`const p = setores.some(s => !!s.s3Link)` e, quando `p` é verdadeiro,
`src = setor.s3Link || logotipoDaLoja`. Ou seja: **basta um** setor com foto para
a coluna inteira virar miniatura, e o setor sem foto entra com o **logotipo da
loja** — não com espaço vazio, como este manual afirmava. A prova está na captura
03 do #124, em que os setores próprios do cardápio adicional saem todos com o
mesmo logotipo.

## O que o aparelho pede ao abrir

Capturado no navegador, para quem for mexer nisso depois:

```
GET /api/totem2/filial/{empresa}/{filial}/0
GET /api/totem2/setores/...      GET /api/totem2/produtos/...
GET /api/totem2/imagens/{empresa,slides}/...
   150|GET /api/totem2/bandeiras/...    GET /api/totem2/tef/{empresa}/0
GET /api/venda2/cupomDescontoAtivo/{empresa}/0?tipo=totem
POST marketing.beetechapi.be/api/rest/pixel/session
```

A configuração é lida **na abertura** — daí a linha dos problemas comuns: o
aparelho com configuração antiga precisa ser reaberto. O Pixel também roda no
totem (o changelog do BeeFood Pixel Analytics lista o totem entre os canais).
