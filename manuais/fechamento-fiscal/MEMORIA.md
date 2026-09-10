# MEMORIA.md — #94 Fechamento Fiscal

Manual do lojista: tela **Fiscal → Fechamento Fiscal** (aba Fechamento) e a
permissão **item 301** no grupo de acesso.

Última atualização: 10/09/2026.

---

## 1. O pedido

O dono pediu três manuais de fechamento fiscal. Este é o **#94** (visão do
restaurante: conferir o mês, XML, PDF/Excel, grupo de acesso). Os outros dois
são **#95** (autorizar o contador) e **#96** (portal do contador).

Conta de captura: Nippon - Matriz, empresa **31049**, CNPJ `30.436.379/0001-48`.
Setembro/2026: R$ 97.808,04, 1.992 NFC-e.

---

## 2. Imagens

| Arquivo | Tipo | Uso |
|---------|------|-----|
| `01-tela-resumo.png` | setas | Resumo da competência |
| `02-exportar-pdf-excel.png` | setas | Menu PDF / Excel |
| `03-filtro-periodo.png` | setas | Recorte de dias |
| `04-aba-produtos.png` | setas | Tabela de itens |
| `05-produtos-por-cfop.png` | setas | Agrupamento por CFOP |
| `06-aba-documentos.png` | setas | Lista de notas |
| `07-dialog-itens.png` | setas | Itens de uma NFC-e |
| `08-ajuda-acesso.png` | setas | Quem tem acesso |
| `10-permissao-fechamento-fiscal.png` | setas | Switch no grupo Administrador |

Não publicadas (ficam só em `imagens-puras/`): `07-dialog-xml.png` (erro
*Não encontramos esta competência* na primeira captura) e `09-aba-grupos.png`
(contexto da lista de grupos; a permissão já aparece na 10).

---

## 3. Decisões

- **Não existe botão de fechar o mês.** O fechamento é calculado na hora.
- Uma permissão só (`fechamentoFiscal` / item 301) libera as duas abas.
- Grupo novo nasce **com a permissão ligada** (trigger `trg_CriaGrupoAcessoItem`).
- O lojista **não** tem limite de ZIP por hora; o portal do contador tem.
- Captura no Vite local (`127.0.0.1:5173`) com API de produção: a aba Contadores
  e o portal `/contador` ainda estão atrás de `isDevelopment` no front. Em
  `beefood.app` o fechamento do lojista já abre; a aba Contadores some.
- Calendário do recorte saiu em inglês no Chromium da VM (`September 2026`).
  Os rótulos da UI (Mês inteiro, quinzenas, APLICAR) estão em pt-BR.
- Widget flutuante e banner promocional escondidos por CSS na recaptura.
- Credenciais da Nippon **não** entram no repositório.

---

## 4. Código

Ver `fluxo-codigo.md`.
