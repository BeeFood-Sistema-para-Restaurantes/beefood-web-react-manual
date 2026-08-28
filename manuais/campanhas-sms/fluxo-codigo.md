# fluxo-codigo.md — Campanhas SMS

Mapeamento técnico da funcionalidade no front (`beefood-web-react`). Documento interno —
**não publicar**.

Levantado em 28/08/2026 a partir do código do front e das telas ao vivo na conta
**BeeFood3 - Manual** (produção). O clone do backend (`beetech-server-node-2.0`) não estava
disponível neste ambiente; os endpoints abaixo saem de `src/lib/api/sms.ts`.

---

## 1. Visão geral

```
Food Marketing -> Campanhas SMS
   /food-marketing/campanhas-sms
        |
        +-- aba campanhas   (tab=campanhas, padrão)
        +-- aba saldo       (tab=saldo)          "Saldo & Extrato"
        +-- aba blacklist   (tab=blacklist)      "Blacklist / Opt-out"
        |
        +-- GET    /sms2/saldo/{empresaID}/{usuarioID}
        +-- GET    /sms2/pacotes/{empresaID}/{usuarioID}
        +-- POST   /sms2/saldo/comprar
        +-- GET    /sms2/saldo/extrato/{empresaID}/{usuarioID}/{limite}
        +-- GET    /sms2/saldo/pedidos/{empresaID}/{usuarioID}
        +-- GET    /sms2/variaveis/{empresaID}/{usuarioID}
        +-- GET    /sms2/campanhas/{empresaID}/{usuarioID}
        +-- GET    /sms2/campanha/{empresaID}/{usuarioID}/{id}
        +-- POST   /sms2/campanha
        +-- PUT    /sms2/campanha
        +-- POST   /sms2/campanha/preview
        +-- POST   /sms2/campanha/enviar
        +-- DELETE /sms2/campanha/{empresaID}/{usuarioID}/{id}
        +-- GET    /sms2/campanha/participantes/{empresaID}/{usuarioID}/{id}
        +-- POST   /sms2/campanha/segmentacao
        +-- POST   /sms2/campanha/participante
        +-- DELETE /sms2/campanha/participante/{empresaID}/{usuarioID}/{id}/{participanteID}
        +-- POST   /sms2/campanha/participantes/limpar
        +-- GET    /sms2/campanha/envios/{empresaID}/{usuarioID}/{id}
        +-- GET    /sms2/blacklist/{empresaID}/{usuarioID}
        +-- POST   /sms2/blacklist
        +-- DELETE /sms2/blacklist/{empresaID}/{usuarioID}/{id}
```

No código do front o prefixo é `/datasnap/rest/...`. Em produção, em 28/08/2026, as
chamadas saíram em `https://app3.beetechapi.be/api/sms2/...` (empresa 38311). Mocks em
`sms.mocks.ts` existem só como fixture — `USE_MOCK = false` em todos os ambientes.

Há versão **mobile** (`MobileSmsPage`) com as mesmas abas. Este manual documenta o **desktop**.

---

## 2. Componentes do front

| Arquivo | Papel |
|---------|-------|
| `src/pages/FoodMarketingCampanhasSms.tsx` | Casca desktop/mobile |
| `FoodMarketingCampanhasSms.desktop.tsx` | Três abas + modal de compra |
| `SmsCampanhasTab.tsx` | Lista, landing vazia, ações, abre editor/detalhe |
| `SmsEmptyLanding.tsx` | Landing quando não há campanha (presets com `{nome}`, não `{{nome}}`) |
| `ModalCampanha.tsx` | Editor em 3 passos (Sheet lateral). **Sem auto-save** |
| `campanha/Step2Publico.tsx` | Destinatários: segmentação, telefone avulso, Excel |
| `SmsPhonePreview.tsx` | Prévia do celular |
| `SmsExtratoTab.tsx` | Saldo, PIX pendentes, movimentações |
| `SmsBlacklistTab.tsx` | Lista + texto de opt-out + status de entrega |
| `ModalComprarCreditos.tsx` | Slider, pacotes, GERAR PIX (Asaas) |
| `ModalVerPix.tsx` | Reabre o PIX de um pedido pendente |
| `ModalDetalheCampanha.tsx` | Resultado + tabela de envios + CSV |
| `ModalAdicionarBlacklist.tsx` | Inclusão manual de telefone |
| `ModalImportarParticipantesExcel.tsx` | Importação .xlsx/.xls/.csv |
| `SmsSaldoBadge.tsx` | Saldo + COMPRAR CRÉDITOS |
| `src/utils/smsSegments.ts` | GSM-7 / UCS-2, segmentos, pior caso, preço por faixa |
| `src/utils/smsVariaveis.ts` | Extração, renderização de exemplo, flags de cashback/link |
| `src/utils/smsBlacklist.ts` | Rótulos de motivo/origem |

---

## 3. Permissão

| Camada | Identificador |
|--------|---------------|
| Chave no JSON de permissões | `campanhaSMS` |
| Item do menu / rota | `campanhas-sms` / `submenuKey="foodMarketing"` |
| Rota | `/food-marketing/campanhas-sms` |

O itemID/formularioID mora no backend (`grupoAcesso.js`), que não estava clonado nesta sessão.
A chave de tela é **distinta** das Campanhas WhatsApp (`campanhaWhatsApp` / item 167).

---

## 4. Editor — 3 passos, sem auto-save

O `ModalCampanha` só grava ao **avançar do passo 1 para o 2** (`persistirMensagem` →
`POST/PUT /sms2/campanha`). Fechar por **FECHAR (ESC)** no passo 1, sem ter avançado, **não
cria rascunho**. Isso permite fotografar avisos (UCS-2, link, variável inválida) e sair sem
sujar o ambiente.

Passo 1 válido: nome preenchido, mensagem preenchida, nenhuma variável desconhecida, e
cardápio selecionado se a mensagem usa `{{meu_link}}`.

Passo 2 válido: campanha já persistida e `totalParticipantes > 0`.

Passo 3 / envio: saldo suficiente; se a mensagem tem link (URL ou `{{meu_link}}`), o usuário
precisa confirmar o risco de spam (`cienteLink` / diálogo **ENVIAR COM LINK**).

O envio é `POST /sms2/campanha/enviar` com `{ smsCampanhaID, confirmaLink }`. Irreversível.
Campanha enviada ou em envio **não pode ser excluída**.

---

## 5. Segmentos e créditos (regra que o manual precisa acertar)

`calcularSegmentos` em `smsSegments.ts`:

| Codificação | Quando | 1 segmento | Multi-segmento |
|-------------|--------|------------|----------------|
| GSM-7 (`"0"`) | só caracteres do alfabeto GSM | 160 chars | 153 chars/seg |
| UCS-2 (`"8"`) | qualquer acento fora do GSM, emoji, etc. | 70 chars | 67 chars/seg |

Cada **segmento = 1 crédito por destinatário**. O custo da campanha usa o **pior caso**
(`piorCasoCreditos`): substitui `{{nome}}` / `{{primeiro_nome}}` pelos nomes reais da lista,
`{{saldo_cashback}}` por `R$ 9.999,99` e `{{meu_link}}` pelo link com `?sms={id}`. Se algum
nome tiver acento e o switch estiver desligado, a campanha inteira cai em UCS-2.

O switch **Enviar sem acento e emoji** (`removerAcento`, **ligado por padrão** em campanha
nova) passa o texto por `semAcentoEmoji` (NFD + descarte de não-GSM) **no envio**, inclusive
nos nomes. A prévia já mostra o texto limpo.

`{{meu_link}}` vira `menu.beefood.com.br/{slug}?sms={id}` (sem `https://`). Domínios medidos
para clique/conversão: `menu.beefood.com.br` e `shop.beetech.com.br`. Link de outro domínio
dispara aviso de que **não será medido**.

Clientes **sem saldo de cashback** são ignorados (não consomem crédito) se a mensagem usa
`{{saldo_cashback}}`.

---

## 6. Destinatários

Três origens no passo 2:

1. **Por segmentação** — `POST /sms2/campanha/segmentacao`. Só públicos **ativos**. O backend
   devolve `adicionados` / `ignorados` (duplicados ou blacklist).
2. **Telefone avulso** — `POST /sms2/campanha/participante`, validado por
   `telefoneValidoWhatsApp`.
3. **Planilha** — Excel/CSV via `ModalImportarParticipantesExcel`.

A tela avisa: a segmentação já traz só clientes com telefone válido, ativos e que aceitam
mensagem; blacklist/opt-out é removida automaticamente.

Origem na tabela: `manual` ou `segmentacao`.

---

## 7. Compra de créditos (PIX / Asaas)

Faixas **fixas no front** (`ModalComprarCreditos.tsx`):

| Até | Preço / crédito |
|-----|-----------------|
| 1.000 | R$ 0,16 |
| 10.000 | R$ 0,14 |
| acima | R$ 0,12 |

Mínimo de compra: **R$ 5,00** (piso de 32 créditos a R$ 0,16). Máximo por pedido: **R$ 10.000**.
Slider até 50.000 créditos. Pacotes sugeridos vêm de `GET /sms2/pacotes`.

`POST /sms2/saldo/comprar` devolve pedido Asaas com `pixCopiaCola`, `pixQrCode` e
`linkPagamento`. O pedido fica em **Saldo & Extrato → Pagamentos pendentes** até confirmar.
O saldo só sobe depois do PIX.

---

## 8. Blacklist / opt-out

Entra por:

| Origem | Motivo típico |
|--------|----------------|
| `MO` | Cliente respondeu `SAIR`, `PARAR`, `STOP`, `CANCELAR` ou `DESCADASTRAR` |
| `DLR` | Erro permanente: número inválido, rejeitado, Anatel/operadora, internacional, expirado |
| `MANUAL` | Inclusão na tela |
| `BACKFILL` | Histórico importado |

**Conteúdo bloqueado não coloca o número na blacklist** — o problema é da mensagem. SMS com
erro de entrega **não é reembolsado**. Número na blacklist é pulado no próximo disparo.

---

## 9. Status

Campanha: `RASCUNHO` · `ENVIANDO` · `ENVIADA` · `ABORTADA` · `ERRO`.

Envio: `PENDENTE` · `ACCEPTED` · `SENT` · `DELIVERED` · `FALHA` · `SEM_CASHBACK` · `BLACKLIST`.

---

## 10. Variáveis

Catálogo vem de `GET /sms2/variaveis` (não está hardcoded no front). O editor só aceita as
chaves devolvidas. Variável desconhecida trava o passo 1.

A landing vazia usa placeholders **errados** (`{nome}`, `{valor}`) nos presets — o editor
correto usa `{{chave}}`. O manual ensina o formato com chave dupla.
