# fluxo-codigo.md — App Garçom (#40)

Card em `src/pages/Parametros.tsx` (bloco Aplicativo do Garçom). Persistência: `useEmpresaParametros` → `POST /api/empresa2/empresaConfig`.

| Tela | Flag |
|------|------|
| Comandas | `appGarcomComanda` |
| Mesas | `appGarcomMesa` |
| Nome Avulso | `appGarcomNomeAvulso` |
| Cliente | `appGarcomCliente` |

Consumo no app do garçom (fora deste repositório de manuais). Desktop auto-save ~500 ms. MobileParametrosPage tem botão Salvar — **não documentar**.
