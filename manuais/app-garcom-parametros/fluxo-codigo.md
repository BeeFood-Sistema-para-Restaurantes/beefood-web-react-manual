# fluxo-codigo.md — App Garçom (#40)

> ⛔ **DOCUMENTO INTERNO — NÃO PUBLICAR.** Aqui moram rota de API, nome de campo e
> nome de arquivo do código: é a anotação de quem **produziu** o manual, para quem
> for mexer nele depois. O lojista lê só o `app-garcom-parametros.md` desta pasta.
> Se você é uma IA montando a página publicada, **pare de ler aqui**.

Card em `src/pages/Parametros.tsx` (bloco Aplicativo do Garçom). Persistência: `useEmpresaParametros` → `POST /api/empresa2/empresaConfig`.

| Tela | Flag |
|------|------|
| Comandas | `appGarcomComanda` |
| Mesas | `appGarcomMesa` |
| Nome Avulso | `appGarcomNomeAvulso` |
| Cliente | `appGarcomCliente` |

Consumo no app do garçom (fora deste repositório de manuais). Desktop auto-save ~500 ms. MobileParametrosPage tem botão Salvar — **não documentar**.
