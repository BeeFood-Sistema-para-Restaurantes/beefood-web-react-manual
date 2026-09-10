# MEMORIA.md — #96 Portal do contador

Manual do escritório contábil: e-mail, login, clientes, competências, XML,
NFe recebidas e edição fiscal.

Última atualização: 10/09/2026 (valores fiscais embassados nas tratadas).

---

## 1. O pedido

Terceiro dos três manuais. Visão do contador: e-mail, ver/baixar fechamento,
analisar dados, edição fiscal.

Conta: documento `23641847000150` (BeeFood Testes). Clientes na lista: MAGA
(`00.616.579/0001-11`), Nippon - Matriz e Hey Sushi Fortaleza (empresa 31049,
2 CNPJs).

---

## 2. Imagens

| Arquivo | Tipo | Uso |
|---------|------|-----|
| `01-email-criar-senha.png` | setas | Mesmo e-mail MAGA do #95 |
| `02-email-acessar-portal.png` | setas | Mesmo e-mail Nippon do #95 |
| `03-login-identificar.png` | setas | CPF/CNPJ |
| `05-login-senha.png` | setas | Senha da conta já ativada |
| `06-meus-clientes.png` | setas | MAGA + rede Nippon |
| `07-competencias.png` | setas | Meses da matriz |
| `08-fechamento.png` | setas | Resumo set/2026 |
| `09-produtos.png` | setas | Mesmos itens do #94 |
| `10-documentos.png` | setas | Lista de NFC-e |
| `11-nfe-recebidas.png` | setas | Entradas + aviso mar/2026 |
| `12-edicao-fiscal.png` | setas | Filtro Sem NCM |

Não publicada: `04-login-documento-preenchido.png` (passo intermediário; a 03
já mostra o campo).

---

## 3. Decisões e achados

- Totais iguais aos do lojista (R$ 97.808,04 / 1.992 NFC-e em set/2026).
- NFe recebidas: recorte por **período**, não competência. Histórico a partir de
  **março de 2026**. Chip SEM XML (31) > NOTAS (29) no print — XML ainda não
  baixado da SEFAZ em várias linhas.
- Edição fiscal: mesma tela do lojista. **Não corrige XML já emitido.** Produto
  é cadastro da empresa: editar num CNPJ alcança as filiais.
- Rotas `/contador/*` ainda atrás de `isDevelopment`. Captura no Vite local.
  Em `beefood.app/contador` o front de produção redireciona para `/login`.
- E-mails já apontam para `https://beefood.app/contador`.
- Senha da conta de teste **não** entra no repositório.
- Valores em R$, CNPJ, chave, número da nota e dados de fornecedor saem
  **embassados** nas `imagens-tratadas/` (`blur=` no `annotate.py`).

---

## 4. Código

Ver `fluxo-codigo.md`.
