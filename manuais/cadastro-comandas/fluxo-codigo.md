# Fluxo de código — Cadastro de comandas e QR Code (#81)

Levantado em 03/09/2026 em `~/refs/beefood-web-react` (leitura) e no sandbox.
**Não publicar nada daqui no manual.** O irmão deste arquivo é
[`../cadastro-mesas/fluxo-codigo.md`](../cadastro-mesas/fluxo-codigo.md) — a tela é a mesma, com
as diferenças abaixo.

---

## 1. Rota, menu e arquivos
    10|
| Item | Valor |
|------|-------|
| Rota | `/cadastro-comandas` |
| Menu | **Cadastros → Comandas** |
| Permissão | `submenuKey="cadastros"`, `submenuItemKey="comandas"` |
| Página desktop | `src/pages/CadastroComandas.tsx` |
| Página mobile | `src/components/mobile/cadastro-comandas/MobileCadastroComandasPage.tsx` |
| Modal individual | `src/components/ModalEditarComanda.tsx` |
| Modal em lote | `src/components/ModalCriarComandasEmLote.tsx` |
| Hook | `src/hooks/useCadastroComandas.ts` |
    20|
---

## 2. Rotas de API

| Operação | Método | Caminho |
|----------|--------|---------|
| Listar | GET | `/api/empresa2/comandas/{empresaID}/{filialID}/{usuarioID}` |
| Detalhe | GET | `/api/empresa2/comanda/{empresaID}/{usuarioID}/{comandaID}` |
| Criar / atualizar / lote | POST | `/api/empresa2/comanda` |
| Excluir | DELETE | `/api/empresa2/comanda` |
    30|
**Atenção:** o campo de identificação no payload é **`id`**, não `comandaID` (nas mesas é
`mesaID`). O resto do corpo é igual ao das mesas (`descricao`, `codigo`, `ativo`, `usuario`,
`nomeFantasia`, `log`).

---

## 3. Diferenças em relação às mesas

| Aspecto | Mesas | Comandas |
|---------|-------|----------|
    40|| Campo de ID no payload | `mesaID` | **`id`** |
| Descrição padrão | `Mesa N` | `Comanda N` |
| QR do cardápio | `?tipo=p&mesa={codigo}` | **`?tipo=p&comanda={codigo}`** |
| QR interno | `{empresaID}_{codigo}` | **`{empresaID}_c{codigo}`** |
| EAN-13 (2º dígito = tipo) | `0` | **`1`** |
| Gate "você usa comanda?" | Sim | **Não** |
| Deep link | — | **`?openQRCode=1`** abre o seletor de QR automaticamente |

O deep link é o destino do botão **QUERO GERAR DE COMANDA** do gate exibido no cadastro de mesas.

    50|No sandbox, o EAN-13 da Comanda 1 saiu **`2 103831 100012`** (tipo 1, empresa 38311, código
0001) — contra `2 003831 100015` da Mesa 1. É a prova de que o sistema distingue mesa de comanda
pelo próprio código lido.

---

## 4. Medições no sandbox (03/09/2026, empresa 38311 / filial 39202)

- Antes: **25 comandas** (códigos 1 a 25), todas ativas.
- Criada a **Comanda 26** pelo modal individual e as **27 a 30** pelo lote → **30 comandas**.
    60|- Diálogo de exclusão fotografado na Comanda 26 e **cancelado**.
- QR Codes gerados na faixa **1 a 4** nos três tipos; folha de impressão capturada pelo iframe
  oculto (mesmo truque descrito no `MEMORIA.md` do #80).
- Mapa do salão: aba **Comandas** com 30 cards (27 livres, 3 ocupados no momento da captura).
