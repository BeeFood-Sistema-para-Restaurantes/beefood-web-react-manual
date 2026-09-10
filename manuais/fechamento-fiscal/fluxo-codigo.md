# fluxo-codigo.md — #94 Fechamento Fiscal (uso interno, NÃO publicar)

Mesma apuração do portal do contador. Dois prefixos só por causa da autorização.

```
Painel (token do lojista)
  GET /api/fiscal2/fechamento/:empresaID/:usuarioID/:cnpj/:competencia
  GET .../:competencia/produtos
  GET .../:competencia/documentos
  GET .../:competencia/zip
  GET .../documento/:documentoID/download
  GET .../documento/:documentoID/itens
  GET .../:cnpj/competencias

Model compartilhado: src/models/fiscal/fechamento.js
Front: pages/FiscalFechamentoHub.tsx + pages/FechamentoFiscal.tsx
       lib/api/fechamentoFiscal.ts
       components/fechamento/*
       utils/pdfExportFechamentoFiscal.ts  (cliente)
       utils/excelExportFechamentoFiscal.ts (cliente)
```

O ZIP é montado no servidor. PDF e Excel nascem no navegador.

---

## Permissão (item 301)

`sql/012-item-fechamento-fiscal.sql` cria o item `actFechamentoFiscal` (Recurso
Fiscal, `beefood3 = 1`) e cobre **todos** os grupos: nível 1 se a descrição
contém `adm`, nível 0 no resto. Sem linha = liberado (`checkAcessoItemID`
começa em `true`).

`grupoAcesso.js`:

```
sidebar.menu.fiscal.items.fechamentoFiscal.visible  → item 301
fechamentoFiscal.enabled                           → form 102 (NFC-e) OU 35 (NF-e)
submenus.fiscal.visible                            → 192, 25, 208, 207, 294, 301
```

Front: `AppSidebar.tsx` `permissionKey: "fechamentoFiscal"`, selo Novo.
Rota: `ProtectedRoute submenuItemKey="fechamentoFiscal"` → `FiscalFechamentoHub`.

Grupo criado depois do script nasce **liberado** (trigger). Cache ~1 min +
relógio. Recarregar a página não basta.

---

## Recorte de período

Query `?de=` e `?ate=` (YYYY-MM-DD). `de=` vazio dá 400 — o front só manda o
que tem valor (`aplicarPeriodo` em `fechamentoFiscal.ts`).

---

## Hub de abas

`FiscalFechamentoHub.tsx`: aba Fechamento sempre; aba Contadores só se
`isDevelopment` (`localhost` / Lovable). Em produção a URL
`/fechamento-fiscal?aba=contadores` cai na aba Fechamento.

`/contadores` redireciona para `?aba=contadores`.
