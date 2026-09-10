# MEMORIA.md — #95 Autorizar o contador

Manual do lojista: aba **Contadores** em Fiscal → Fechamento Fiscal. Inserir,
permissões, e-mail, encerrar, reativar, reset de senha.

Última atualização: 10/09/2026 (CNPJ embassado nas tratadas).

---

## 1. O pedido

Segundo dos três manuais de fechamento fiscal. O dono pediu: como adicionar o
contador, remover o acesso e o e-mail que ele recebe.

---

## 2. Imagens

| Arquivo | Tipo | Uso |
|---------|------|-----|
| `01-aba-contadores.png` | setas | Lista (Aguardando + Ativo) |
| `02-dialog-autorizar.png` | setas | Formulário preenchido (CNPJ de exemplo) |
| `03-menu-acoes.png` | setas | Menu da linha Ativo (inclui reset) |
| `04-dialog-permissoes.png` | setas | Três switches |
| `05-confirmar-encerrar.png` | setas | Confirmação — **não confirmamos** |
| `06-email-primeiro-acesso.png` | setas | MAGA: CRIAR MINHA SENHA |
| `07-email-conta-existente.png` | setas | Nippon: ACESSAR O PORTAL + 2 CNPJs |

Os e-mails vieram dos anexos Gmail do dono (`contato@beefood.com.br`).

---

## 3. Decisões e achados

- Acesso é da **empresa inteira**, não de um CNPJ. Filial nova entra sozinha.
- O lojista **não escolhe a senha**. Uma conta por CPF/CNPJ.
- Dois status na mesma lista para o mesmo escritório (BeeFood Testes):
  `23.641.947/0001-50` *Aguardando primeiro acesso* e `23.641.847/0001-50`
  *Ativo*. São dois documentos (um dígito diferente) — não é bug de UI.
- Primeiro acesso **não exige clicar no e-mail**. Quem souber o documento e
  chegar antes assume a conta. Mitigação: e-mail com data/IP + status na lista.
- `PENDENTE` é da **conta** (sem senha), não do vínculo. Conta com senha já
  nasce `ATIVO` (`sql/011`).
- Confirmação de conta existente mostra nome + e-mail mascarado. O e-mail
  digitado na segunda autorização **não substitui** o cadastrado.
- Encerrar nesta sessão: só abriu o diálogo; **CANCELAR**. Nada revogado.
- Formulário de autorizar: CNPJ `12.345.678/0001-90` de exemplo, não enviado.
- Aba Contadores ainda atrás de `isDevelopment` no front de produção.
- CNPJ do escritório e da empresa saem **embassados** nas `imagens-tratadas/`.

---

## 4. Código

Ver `fluxo-codigo.md`.
