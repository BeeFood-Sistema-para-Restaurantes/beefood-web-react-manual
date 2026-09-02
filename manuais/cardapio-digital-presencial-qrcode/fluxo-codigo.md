# Fluxo de código — Cardápio digital presencial e QR Code (#77)

> Uso interno. **Não publicar.** Fonte: `beefood-web-react`, somente leitura.
> Levantado em 02/09/2026.

---

## 1. Telas

| Tela | Arquivo | Rota |
|------|---------|------|
| Card **Presencial (Mesas/Comandas)** | `src/components/cardapio-digital/ConfiguracoesTab.tsx` | `/cardapio-digital?tab=configuracoes&scrollTo=presencial` |
| Mobile do mesmo card | `src/components/mobile/cardapio-digital/MobileConfiguracoesTab.tsx` | idem |
| Modal dos 3 QRs | `src/components/cardapio-digital/ModalQRCode.tsx` | — |
| Meus Links (desktop) | `src/components/ModalMeusLinks.tsx` | rodapé da sidebar |
| Meus Links (mobile) | `src/components/mobile/MobileMeusLinks.tsx` | idem |
| Card de um link | `src/components/meus-links/LinkCard.tsx` | — |
| QR de um link (um só) | `src/components/meus-links/ModalQRCodeLink.tsx` | — |
| Passo 1 do gerador | `src/components/meus-links/ModalSelecionarMesaOuComanda.tsx` | — |
| Passo 2 do gerador | `src/components/ModalSelecionarTipoQRCode.tsx` | — |
| Gate “usa comanda?” | `src/components/qrcode/UsaComandaGate.tsx` | só Meus Links / Cadastro Mesas |
| QR “Código da Mesa” | `src/components/ModalQRCodeMesa.tsx` | outro produto (PDV/tablet) |
| Bloqueio de canal | `src/components/cardapio-digital/CanalBlocker.tsx` | menu `/mesas` |

---

## 2. API das configurações

```
GET  /datasnap/rest/empresaDelivery2/cardapioDigital/configuracoes/{empresa}/{filial}/{usuario}
POST /api/empresaDelivery2/cardapioDigital/configuracoes
```

O POST manda o **snapshot inteiro** (Delivery + Presencial + redes). Auto-save
`useAutoSave` com delay **800 ms**. Toast *Salvo automaticamente*.

| Tela | Estado | Campo POST | Default |
|------|--------|------------|---------|
| Presencial Ativo | `qrCodePresencial` | `qrCodePresencial` | `true` |
| Opções do Garçom | `garcomOpcoes` | `presencialGarcomOpcoes` | `true` |
| Fechar conta | `botaoFechamento` | `pFechaConta` | `true` |
| Cadastro (3 modos) | `cadastroPresencialIndex` | `pedSemCadPSimp` + `pedidoSemCadastroPresencial` | rápido |
| E-mail presencial | `emailPresencialIndex` | `solicitaEmailP` (0/1/2) | depende do modo |
| Nascimento presencial | `nascimentoPresencialIndex` | `solicitaNascimentoP` (0/1/2) | depende do modo |

Índice do cadastro:

| Índice | Texto | Flags |
|--------|-------|-------|
| 0 | Cadastro rápido com nome e telefone | `pedSemCadPSimp=true` |
| 1 | Sem cadastro (venda única por mesa/comanda) | `pedidoSemCadastroPresencial=true` |
| 2 | Cadastro completo com login e senha | os dois `false` |

No modo 1 os selects de e-mail/nascimento ficam `disabled`.

O card **só renderiza** se `linkAcesso` existe. Sem slug, o alerta pede
para configurar o link.

`CanalBlocker canal="presencial"` deriva de `canViewMenuItem('/mesas')` e
`isMenuItemEnabled('/mesas')`. Motivo: *"Presencial (Mesas) não está
habilitado no seu plano/grupo de acesso."*

---

## 3. URLs do presencial

Três hosts, o mesmo slug (`linkAcesso`):

| Onde | URL | Quem lê |
|------|-----|---------|
| Configurações / `ModalQRCode` | `https://menu.beefood.com.br/{slug}/?tipo=p` | câmera do cliente |
| + mesa | `...?tipo=p&mesa={N}` | idem |
| + comanda | `...?tipo=p&comanda={N}` | idem |
| Meus Links — pedidos | `https://presencial.beefood.com.br/{slug}` | idem |
| + selects | `.../?mesa={N}&comanda={M}` | idem |
| Meus Links — visualização | `https://cardapio.beefood.com.br/{slug}` | só ver, **não pede** |
| Backend `linkAcessoP` | vem no cabecalho | popover / lista |

O gerador de Configurações **não consulta** o cadastro de mesas: o
intervalo 1–10 é só número. Teto: **100** QRs por vez.

`ModalQRCodeMesa` (Código da Mesa) grava `empresaID_N` / `empresaID_cN`
e **filtra** as mesas que existem. É outro QR.

---

## 4. Meus Links — bloco presencial

Rodapé da sidebar (`AppSidebar`): item **Meus Links**. Some/cadeado se
`semLink` ou permissão `meusLinks` off.

Grupo **Cardápios Presencial** (só se `presencialLiberado`):

1. **Link para pedidos de mesa e comanda** — `presencial.beefood.com.br`.
   Dois `<Select>`: Sem mesa / Mesa N e Sem comanda / Comanda N (lista
   `useMesaComanda`). Ações do `LinkCard`: olho, copiar, WhatsApp
   (`Olá! Acesse nosso cardápio digital: {url}`), QR (`ModalQRCodeLink`).
   Se o usuário escolhe **só mesa** e já existem comandas, o clique no QR
   passa pelo `UsaComandaGate`.
2. **Cardápio de visualização** — `cardapio.beefood.com.br`. Sem pedido.
3. **Gerador de QR Codes** — botão *Abrir Gerador de QR Codes*:
   Mesa/Comanda → Cardápio Digital Presencial **ou** Código da Mesa →
   (se Digital) `ModalQRCode` no modo range.

O grupo **Cardápios Delivery** (origem `?s=`, balcão, multilojas) fica
**fora** deste manual.

---

## 5. Opções do Garçom

```
GET  /api/tablet2/garcomOpc/{empresa}/{filial}/{usuario}
POST /api/tablet2/garcomOpc
```

Switch ligado ⇔ `garcomOpcEmpresaID !== null`. Cada toque grava na hora
(não passa pelo auto-save das configurações). Mesmo catálogo do tablet.

---

## 6. O que este manual não cobre

| Assunto | Onde |
|---------|------|
| Grade semanal presencial | #32 |
| Pausa / switch do popover | #33 |
| Menus do app do garçom | #40 |
| Taxa / obrigatoriedade de mesa | #41 |
| Kiosk do tablet | #24 |
| Cadastrar mesa/comanda | backlog Cadastros |
| Operar o salão | backlog Mesas |

**Consumo no Local** (`consumoLocal`) é switch do card **Delivery**.
O preview sticky só mostra o alternador Delivery/Presencial se esse
switch estiver ligado — por isso a prova do cliente é o cardápio
público, não o preview.
