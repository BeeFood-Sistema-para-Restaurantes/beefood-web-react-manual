# fluxo-codigo.md — Cardápio Digital Tablet (mapeamento técnico do painel)

> **Não publicar** — material interno.
>
> **Atenção ao escopo.** O manual `cardapio-digital-tablet-modo-kiosk.md` é **só do aplicativo
> Android**: a trava é configurada no próprio tablet, pela tela de Administração do app. Este
> arquivo mapeia o **painel web**, que é o lado complementar — é lá que o gestor acompanha os
> tablets e envia eventos remotos, entre eles um `TRAVAR`/`DESTRAVAR` que **não é** o modo
> kiosk do app (bloqueia apenas o botão *voltar* dentro do aplicativo).
>
> Serve para: (a) não confundir as duas travas no suporte; (b) documentar o painel quando o
> manual da aba Tablets/Layout/Eventos for produzido. O código do app Android fica em
> `beetech-appgarcom-android`, fora do alcance deste ambiente.
>
> Base: `beefood-web-react` (commit `dbfa088`, 19/08/2026) e `beetech-server-node-2.0`
> (branch `beefood-web-react`, commit `b7f37f5`, 19/08/2026).

## 0. As três travas, para não confundir

| Trava | Onde se configura | O que bloqueia |
|-------|-------------------|----------------|
| **Modo Kiosk (trava avançada)** — assunto do manual | No tablet, em Administração → *Configurar Trava Avançada* / *Travar* | Saída do app por botão Início, notificações, recentes e Configurações. Exige as permissões de Acessibilidade e Launcher padrão. Não bloqueia volume e power. |
| **Trava básica** | No tablet, no mesmo assistente, em *Pular e usar trava básica agora* | Só o *screen pinning* do Android. Sai segurando Voltar + Recentes. |
| **Evento `TRAVAR` do painel** | No painel web, em Cardápio Digital Tablet → Tablets → Enviar evento | Apenas os botões de *voltar* dentro do aplicativo. |

---

## 1. Onde fica a tela

| Item | Valor |
|------|-------|
| Rota | `/cardapio-digital-tablet` |
| Página (desktop) | `src/pages/CardapioDigitalTablet.tsx` |
| Página (mobile) | `src/components/mobile/cardapio-digital-tablet/MobileCardapioDigitalTabletPage.tsx` |
| Chave de permissão | `menuKey="cardapioDigitalTablet"` (em `src/App.tsx`) |
| Rótulo no menu lateral | **Cardápio Digital Tablet** — vira **Cardápio no Tablet** quando o menu está com rolagem vertical, e **Cardápio Tablet** no menu mobile |
| Ícone | `TabletSmartphone` (lucide) |

A página é montada por `ResponsivePage`, então o desktop e o mobile são componentes
diferentes. No mobile, o modal de enviar evento e o de layout viram páginas próprias
(`/cardapio-digital-tablet/enviar-evento` e `/cardapio-digital-tablet/configuracao/:filialID`).

Quando a empresa não tem o módulo liberado, o item do menu aparece esmaecido, com cadeado e
tooltip **Acesso restrito** (`isMenuItemEnabled('/cardapio-digital-tablet')`).

## 2. As três abas

Estado local `activeTab: 'tablets' | 'layout' | 'eventos'`. Cada troca de aba dispara o
fetch correspondente:

| Aba | Hook | Endpoint |
|-----|------|----------|
| Tablets | `useTabletAparelhos` | `GET /api/tablet2/aparelhos/{empresaID}/{usuarioID}` |
| Layout | `useTabletConfiguracoes` | configuração por filial (`TabletConfiguracao`) |
| Eventos | `useTabletEventos` | histórico de eventos enviados |

## 3. Aba Tablets — status, bateria e limite

### 3.1 Como o status é calculado

`src/components/cardapio-digital-tablet/tablet-helpers.tsx`, função `getTabletStatus`.
A conta é feita **no navegador**, sobre o campo `ping2` do aparelho:

| Status | Regra | Cor |
|--------|-------|-----|
| Online | último ping há **menos de 1 hora** | verde (`bg-green-500`) |
| Ausente | último ping entre **1 e 6 horas** | âmbar (`bg-amber-400`) |
| Offline | último ping há **6 horas ou mais**, ou sem `ping2` | vermelho (`bg-red-400`) |

Consequência prática para o manual: um tablet **desligado há 2 horas** aparece como
*Ausente*, não como *Offline*. E um tablet que acabou de ser tirado do modo kiosk continua
*Online* pelas próximas horas — o status não prova que o app está aberto, só que o aparelho
deu sinal de vida.

### 3.2 Ícone de bateria

`BatteryIcon` usa o campo `bateria` (string convertida para float):

| Faixa | Ícone | Cor |
|-------|-------|-----|
| ≤ 20% | `BatteryWarning` | vermelho |
| ≤ 50% | `BatteryLow` | âmbar |
| ≤ 80% | `BatteryMedium` | verde |
| > 80% | `BatteryFull` | verde |

### 3.3 Cards de estatística

Cinco cards, nesta ordem: **Contratados**, **Total**, **Online**, **Ausentes**, **Offline**.

- **Contratados** vem de `getConfigValue('qtdTablet')` — é o que a loja pagou, não o que está
  ligado.
- Os outros quatro respeitam os filtros da tela (filial, busca e versão).

### 3.4 Estouro do limite contratado

```tsx
const isOverLimit = qtdTablet > 0 && globalStats.activeCount > qtdTablet;
```

`activeCount` = **online + ausente**, contando **todos** os aparelhos (ignora o filtro de
filial de propósito). Quando estoura, aparece a faixa vermelha:

> **Quantidade de tablets ultrapassa o limite contratado.**
> Os tablets excedentes serão deslogados automaticamente.

com o botão **Contratar tablet**, que abre o WhatsApp do financeiro
(`WHATSAPP_FINANCEIRO`, em `src/config/contatos.ts`) com a mensagem já escrita.

Isso importa para o manual do modo kiosk: **um tablet excedente é deslogado sozinho**, e um
tablet deslogado sai do cardápio e volta para a tela de login — ou seja, o kiosk "cai" por
motivo de contrato, não por defeito.

### 3.5 Atualização automática

`REFRESH_INTERVAL = 60` segundos. Um `setInterval` de 1 s incrementa a barrinha de progresso
dentro do botão de atualizar e, ao chegar a 100%, chama `fetchAparelhos()`. O botão manual
zera o progresso.

### 3.6 Seleção e filtros

- Clicar no card do tablet alterna a seleção (`toggleTabletSelection`).
- **Selecionar todos** marca só os aparelhos **filtrados**; **Limpar (n)** desmarca.
- **Enviar evento** só aparece com pelo menos um tablet selecionado.
- A busca casa com `mesa`, `model`, `brand` e `uniqueId`.
- Os chips de versão vêm de `agruparPorVersao`: a maior versão fica verde (`isLatest`), as
  demais em âmbar, e os sem versão em cinza (**Sem versão**). Servem de filtro clicável.

## 4. O modal Enviar Evento — o coração do modo kiosk pelo painel

`src/components/cardapio-digital-tablet/ModalEnviarEvento.tsx`. Os seis eventos são fixos,
nesta ordem:

| Ordem | `evento` | Rótulo na tela | Ícone |
|-------|----------|----------------|-------|
| 1 | `ATUALIZAR` | Atualizar Cardápio e Layout | `RefreshCw` |
| 2 | `TRAVAR` | Travar | `Lock` |
| 3 | `DESTRAVAR` | Destravar | `Unlock` |
| 4 | `MESA` | Vincular Mesa/Comanda | `TableProperties` |
| 5 | `MESA_REMOVER` | Remover Vínculo de Mesa/Comanda | `Unlink` |
| 6 | `DESLOGAR` | Deslogar Usuário | `LogOut` |

Regras do modal:

- **Um POST por tablet**, em série (laço `for`), com barra de progresso `Enviando x/y...`.
- Só o evento `MESA` exige campo adicional (o combobox de mesa/comanda, com busca por código
  ou descrição). `canEnviar` bloqueia o envio sem mesa escolhida.
- Atalhos: **F1** (ou `Enter`) envia; **ESC** cancela. O `Enter` é ignorado enquanto o
  combobox de mesa está aberto.
- Enquanto envia, o modal não pode ser fechado (`onOpenChange` vira `undefined`).
- No fim: toast de sucesso, de aviso (parcial) ou de erro, e a seleção é limpa.

Corpo enviado:

```json
{
  "empresaID": 0,
  "usuarioID": 0,
  "aparelhoId": 0,
  "evento": "TRAVAR",
  "json": null
}
```

Para o evento `MESA`, o `json` carrega a mesa e **fixa** o vínculo:

```json
{
  "codigo": "10",
  "descricao": "Mesa 10",
  "mesa": { "codigo": "10" },
  "mesaFixa": true,
  "mesaID": 10
}
```

O `mesaFixa: true` é o que dispensa a leitura do QR Code no tablet — sem ele, o cliente
precisa apontar a câmera para o QR Code da mesa a cada pedido.

## 5. O lado do servidor

`POST /api/tablet2/criarEvento` → `src/api/controllers/tablet2/criarEventoPOST.js`
(rota registrada em `src/api/routes/tabletRouter2.js`, com `authMiddleware`).

O controller faz duas coisas:

1. Se o evento for `ATUALIZAR`, dispara `processarCacheSetorProdutoGrupo(empresaID,
   "produto,setor,grupo,grupoOpcao")` — em segundo plano, sem travar a resposta.
2. Enfileira o evento: `call autoatendimento.procInsertEvento(aparelhoId, evento, json)`.

Ou seja: **o evento é uma fila, não um comando direto**. O painel grava a linha e responde
`{ resultado: true }` na hora; quem executa é o tablet, quando faz o próximo ping. É por isso
que a aba Eventos tem os estados *Pendente* e *Processado* — e por isso um tablet offline
recebe o `TRAVAR` só quando voltar.

## 6. Aba Eventos

Tabela com paginação (10/25/50/100 por página) e as colunas:

| Coluna | Origem |
|--------|--------|
| Status | *Processado* quando existe `dataHoraProcessado`; senão *Pendente* |
| Evento | `evento` (`TRAVAR`, `DESTRAVAR`, ...) — mostra o código, não o rótulo amigável |
| Data Criação | `dataHoraCriado` |
| Data Processado | `dataHoraProcessado` ou `-` |
| Dispositivo (ID) | `uniqueId` |
| Mesa | `mesa` ou `-` |

## 7. Aba Layout

Lista um card por cardápio (filial). Sem configuração, o card fica esmaecido, com o texto
*Cardápio não habilitado para tablet* e o botão desabilitado **Chame o Suporte para
Habilitar**. Com configuração, mostra os selos e o botão **Configurar**.

Selos do card:

| Selo | Campo |
|------|-------|
| Light / Dark | `temaLight` |
| Grade / Lista | `tipoLayout` (1 → *Grade*, 2 → *Lista*) |
| PIX Online | `pixOnline` |
| Chamar Garçom | `opcGarcom` |
| Fechar Conta | `fecharMesa` |

> **Divergência de rótulo (atenção ao escrever o manual):** o card da listagem chama o
> `tipoLayout` de **Grade** (1) e **Lista** (2), mas o modal de configuração chama os mesmos
> valores de **Lista Completa** (1) e **Por Etapas** (2). São os mesmos dois valores com
> nomes diferentes em telas diferentes.

O modal `ModalConfiguracaoLayout.tsx` tem três abas — **Configurações**, **Slides** e
**Garçom Opções** — e, na primeira, os controles:

| Controle | Opções / descrição em tela |
|----------|----------------------------|
| Tema | Light / Dark |
| Tipo de Layout | Lista Completa / Por Etapas |
| Pix online | *Permite o fechamento da conta com Pix* |
| Chamar Garçom e Opções | *Imprime cupom com a solicitação* |
| Solicitar Fechamento de Conta | *Exibe no tablet o botão para o cliente pedir o fechamento da conta* |
| Gerar QR Code | gera os QR Codes de mesa/comanda |

## 8. O aplicativo Android

| Item | Valor |
|------|-------|
| Pacote | `com.cardapiodigitalmesacomanda` |
| Loja | `ANDROID_APP_URL` em `tablet-helpers.tsx` → Google Play |
| Botão no painel | **Baixar App Android** (estado vazio) e **Baixar App** (rodapé da lista) |
| Vídeo do estado vazio | YouTube `A8SjHJmOG_k`, embutido em `renderEmptyState()` |

> O pacote **antigo** é `com.beegarcom` (app *BeeGarçom — Cardápio Digital Tablet*). A base de
> conhecimento pública ainda documenta o app antigo; o painel atual aponta para o pacote novo.
> Não misturar os dois ao escrever o manual.

## 9. Campos que o tablet reporta

`TabletAparelho` (`src/hooks/useTabletAparelhos.ts`) — útil para explicar a listagem:

`id`, `empresaID`, `filialID`, `usuarioID`, `usuario`, `funcionarioID`, `funcionario`,
`mesa`, `mesaID`, `uniqueId`, `serialNumber`, `systemVersion`, `apiLevel`, `brand`, `model`,
`batteryLevel`, `versao`, `ultimaAtualizacao2`, `ping2`, `pingDif`, `ultimaAtualizacaoDif`,
`eventos`, `memoria`, `hd`, `bateria`.

O card do tablet mostra só: seleção, status, `#id`, logo da filial, `mesa`,
`brand + model`, bateria, `pingDif` e `v{versao}`.

## 10. APIs do tablet usadas durante o atendimento

Documentadas em `beetech-server-node-2.0/docs/tablet/historico-cardapio-digital-tablet/API.md`
(prefixo `/api/tablet2`, Basic Auth global, fora do fluxo de eventos):

`GET /historico/...`, `POST /cashback/aplicar`, `POST /cashback/remover`,
`POST /cliente/consultarTelefone`, `POST /cliente/cadastrar`, `POST /cliente/alterar`,
`POST /cliente/vincular`, `POST /cliente/sms/enviar`, `POST /cliente/sms/validar`,
`POST /mesa/qtdPessoas`.

Não fazem parte do modo kiosk, mas explicam o que o tablet consegue fazer sozinho na mesa
(identificar o cliente, aplicar cashback, mudar a quantidade de pessoas e pedir o
fechamento).
