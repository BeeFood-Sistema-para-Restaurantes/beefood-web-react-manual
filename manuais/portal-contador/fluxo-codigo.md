# fluxo-codigo.md — #96 Portal do contador (uso interno, NÃO publicar)

Sessão **separada** do painel. Token assinado com outro segredo, 12 h.
`contadorAuthMiddleware` + `exigirVinculo` em cada CNPJ.

```
Públicas
  POST /api/contador/identificar
  POST /api/contador/login
  POST /api/contador/definir-senha
  POST /api/contador/senha/recuperar
  POST /api/contador/senha/redefinir

Autenticadas (router + exigirVinculo)
  GET  /api/contador/clientes
  GET  /api/contador/cliente/:cnpj/competencias
  GET  /api/contador/cliente/:cnpj/fechamento/:competencia
  GET  .../produtos  .../documentos  .../zip
  GET  .../documento/:id/download|xml|itens
  GET  /api/contador/cliente/:cnpj/entradas[ /zip /resumo ]
  GET  /api/contador/cliente/:cnpj/entrada/:id/xml|download
  GET/POST /api/contador/cliente/:cnpj/produtos-fiscais | produto-fiscal
  GET/POST/DELETE .../taxa-servico
  GET  /api/contador/catalogos-fiscais   (sem :cnpj, sem exigirVinculo)
```

Front: `pages/contador/*`, `components/contador/*`, `lib/api/contador.ts`,
`lib/contadorSessao.ts`. Rotas em `App.tsx` **somente se** `isDevelopment`.

O fechamento usa o **mesmo model** `fiscal/fechamento.js` do painel.

---

## Identificar

`identificar` responde se a conta existe e se já tem senha. Sem isso o portal
não distingue primeiro acesso de login. Mensagem de “nenhum cliente autorizou”
é a mesma se a conta não existe — de propósito.

---

## NFe recebidas

Índice `fiscal.documento_entrada`, XML no prefixo `entrada/`. Recorte `?de=&ate=`.
Distribuição DFe da SEFAZ: últimos 3 meses. Corte de histórico: março/2026.

---

## Edição fiscal

Exige `podeEditarImposto`. Alcance de **empresa**, não do CNPJ da rota.
Logs no painel do lojista com o nome do contador. Sem e-mail automático.

ZIP do portal tem limite por hora; o do lojista não.
