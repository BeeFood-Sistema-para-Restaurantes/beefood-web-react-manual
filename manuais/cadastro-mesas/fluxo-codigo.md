# Fluxo de código — Cadastro de mesas e QR Code (#80)

Mapeamento levantado em 03/09/2026 a partir de `beefood-web-react` (clone de leitura em
`~/refs/beefood-web-react`) e de uso real no sandbox. **Não publicar nada daqui no manual.**

---

## 1. Rota, menu e arquivos

| Item | Valor |
|------|-------|
| Rota | `/cadastro-mesas` |
    10|| Menu | **Cadastros → Mesas** (`AppSidebar.tsx`, `cadastrosSubItems`) |
| Permissão | `submenuKey="cadastros"`, `submenuItemKey="mesas"` (`ProtectedRoute`) |
| Página desktop | `src/pages/CadastroMesas.tsx` |
| Página mobile | `src/components/mobile/cadastro-mesas/MobileCadastroMesasPage.tsx` |
| Modal individual | `src/components/ModalEditarMesa.tsx` |
| Modal em lote | `src/components/ModalCriarMesasEmLote.tsx` |
| Seletor de QR | `src/components/ModalSelecionarTipoQRCode.tsx` |
| Gate de comanda | `src/components/qrcode/UsaComandaGate.tsx` |
| QR do cardápio | `src/components/cardapio-digital/ModalQRCode.tsx` |
| QR interno / código de barras | `src/components/ModalQRCodeMesa.tsx`, `src/components/ModalCodigoBarrasComanda.tsx` |
    20|| Hook | `src/hooks/useCadastroMesas.ts` |
| Operação | `src/pages/Mesas.tsx` + `useMesasData` |

A página **limpa o `mesaComanda_cache` do `localStorage`** ao montar, para a tela de operação
recarregar o catálogo na próxima visita.

---

## 2. Rotas de API

| Operação | Método | Caminho |
|----------|--------|---------|
    30|| Listar | GET | `/api/empresa2/mesas/{empresaID}/{filialID}/{usuarioID}` |
| Detalhe | GET | `/api/empresa2/mesa/{empresaID}/{usuarioID}/{mesaID}` |
| Criar / atualizar | POST | `/api/empresa2/mesa` |
| Criar em lote | POST | `/api/empresa2/mesa` (array) |
| Excluir | DELETE | `/api/empresa2/mesa` |
| Catálogo da operação | GET | `/datasnap/rest/empresa2/mesaComanda/{empresaID}/{usuarioID}/1` |

Payload de criação: `{ mesaID: null, empresaID, filialID, usuarioID, descricao, codigo, ativo,
usuario, nomeFantasia, log: { acao, observacao } }`. O `log.acao` muda conforme a ação
(`Inserir mesa`, `Atualizar mesa`, `Criar mesa em lote`).
    40|
---

## 3. Regras que estão no front

1. **Próximo código** = maior `codigo` existente + 1 (ou 1). A descrição nasce `Mesa {código}`.
2. **Salvar exige código e descrição** — sem mensagem inline: o `handleSave` simplesmente não
   conclui.
3. **Não há validação de código duplicado no cadastro individual.** Só o lote confere.
4. **Lote:** 1 a 100 por vez; compara a faixa com os códigos existentes e monta a mensagem
   *"As mesas X, Y já existem."*, bloqueando o botão.
    50|5. **Atalhos:** `F1` abre Nova Mesa (só quando não há modal aberto), `F5` atualiza sempre.
6. **Ordenação** por código crescente; a busca filtra por `descricao` ou `codigo`.
7. **Não existe** duplicar, editar em lote, ativar/desativar em massa nem exportar PDF.

---

## 4. Os três QR Codes

| Tipo | Componente | Conteúdo do código |
|------|------------|--------------------|
| Cardápio Digital Presencial | `ModalQRCode` (`tipo="presencial-mesa"`) | `https://menu.beefood.com.br/{linkAcesso}/?tipo=p&mesa={codigo}` |
    60|| Código da Mesa | `ModalQRCodeMesa` (`tipo="mesa"`) | `{empresaID}_{codigo}` — ex.: `38311_1` |
| Código de Barras | `ModalCodigoBarrasComanda` (`tipo="mesa"`) | EAN-13 `2` + `0` + empresa(6) + código(4) + dígito |

- QR desenhado com **`qrcode.react`** (`QRCodeSVG`, nível H); código de barras com
  **`react-barcode`** (EAN-13). Geração em `src/utils/barcodegen.ts`.
- **O QR do cardápio gera pela faixa informada, sem consultar o cadastro.** Os outros dois só
  geram para mesas que existem.
- Limite de **100 QR Codes** por geração; código de barras limitado à mesa **9999**.
- **Impressão via iframe oculto** (`imprimirViaIframe`, `#beefood-print-frame`), grade de 3
  colunas com logo e marca d'água *Sistema BeeFood*. **Não há PDF** — só PNG (um por mesa) e a
    70|  folha HTML.
- No sandbox, o EAN-13 da Mesa 1 saiu **`2 003831 100015`** (empresa 38311, tipo 0, código 0001).

### O gate "Você usa Comanda?"

Só aparece **no cadastro de mesas** e **só** ao escolher *Cardápio Digital Presencial*
(`CadastroMesas.tsx`). O botão **QUERO GERAR DE COMANDA** navega para
`/cadastro-comandas?openQRCode=1`, e o cadastro de comandas abre o seletor de QR automaticamente
por causa desse parâmetro.

---
    80|
## 5. Relação com a operação (`/mesas`)

- O card do mapa vem do catálogo `mesaComanda`, que **não traz o campo `ativo`** — mesa inativa
  simplesmente não é devolvida para a operação.
- Status operacional (`useMesasData.getItemStatus`): `livre` (sem venda), `ocupado` (venda
  aberta), `fechado` (`fechamentoSolicitado === true`).
- O PDV lê o QR interno no formato `{empresaID}_{codigo}` (`PDV.tsx`).

---

    90|## 6. Medições no sandbox (03/09/2026, empresa 38311 / filial 39202)

- Antes: **14 mesas** (códigos 2 a 15) — o código **1 não existia**, o que deixou o exemplo do
  cadastro individual pronto de graça.
- Criada a **Mesa 1** pelo modal individual e as mesas **16 a 19** pelo lote → **19 mesas**.
- O conflito de numeração foi reproduzido pedindo 4 mesas a partir da 5: *"As mesas 5, 6, 7, 8 já
  existem."*
- Comandas na mesma base: 25 (depois 30, no manual #81).
