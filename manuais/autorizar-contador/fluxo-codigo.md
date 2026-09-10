# fluxo-codigo.md — #95 Autorizar o contador (uso interno, NÃO publicar)

```
Lojista (token do painel)
  GET  /api/fiscal2/contadores/:empresaID/:usuarioID
  POST /api/fiscal2/contador/:empresaID/:usuarioID
  POST .../:vinculoID/revogar
  POST .../:vinculoID/reativar
  POST .../:vinculoID/resetar-senha
  POST .../:vinculoID/permissoes

Front: pages/ContadoresAutorizados.tsx
       components/contador-gestao/ListaContadores.tsx
       components/contador-gestao/DialogAutorizarContador.tsx
       components/contador-gestao/DialogConfirmarContadorExistente.tsx
       lib/api/contadorGestao.ts
```

---

## Identidade

Uma linha em `fiscal.contador` por documento. N linhas em
`fiscal.contador_vinculo` (uma por empresa). Navegação do portal continua por CNPJ.

409 `CONTADOR_JA_EXISTE` **não é erro**: a tela pede confirmação
(`ContadorJaExisteError`).

Permissões do vínculo: `podeBaixarXml`, `podeVerFechamento`, `podeEditarImposto`
(esta última nasce desligada).

---

## E-mail

`src/models/fiscal/contadorEmail.js`

- Remetente `BeeFood Fiscal <integracao@beefood.com.br>`
- Portal no link: `https://beefood.app/contador` — **sem token**
- Templates: `contador_convite.hbs`, `contador_ativado.hbs`,
  `contador_revogado.hbs`, recuperação de senha
- SMTP que falha **não** derruba o vínculo

Dois textos no convite: `primeiroAcesso` → CRIAR MINHA SENHA; senha já existe →
ACESSAR O PORTAL (+ “N CNPJs” quando `totalCnpjs > 1`).

---

## Status na lista

O front mostra *Aguardando primeiro acesso* quando a conta ainda não tem
`senhaHash`, mesmo com vínculo criado. *Ativo* = senha existe e vínculo válido.
*Revogado* = `status = REVOGADO`. Reset de senha só na linha ativa.

Revogação é imediata na próxima requisição (`exigirVinculo` filtra ATIVO).
O JWT do contador dura 12 h, mas cada clique reconsulta o vínculo.
