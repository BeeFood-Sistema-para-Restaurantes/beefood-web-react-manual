# MEMÓRIA — Manual Ativação Aiqfome V2

> Memória detalhada deste manual (escopo, origem, decisões e estado).
> Ver também a memória geral: `..\..\MEMORIA-GERAL.md`.

Status: ✅ **Concluído** — Última atualização: 2026-06-26

---

## 1. Escopo do manual

Ensinar o restaurante a **ativar a integração Aiqfome V2** no BeeFood, em 3 partes:
1. Obter o **Store ID** da loja no painel **Geraldo** do Aiqfome.
2. Cadastrar a filial no BeeFood (**Aplicativos → Aiqfome V2 → Credenciais → + Novo Cadastro**).
3. Autorizar via **ID Magalu** (OAuth) até o status ficar **Conectado**.

Arquivo final: `ativacao-aiqfome.md`.

---

## 2. Origem (import)

- Importado de `C:\projetos\beefood-server-aiqfome\docs` (arquivo `ativacao-aiqfome.md` + `images/`).
- **As imagens já vieram prontas/corretas** (com marcações verdes). Por isso **não há `annotate.py`**
  neste manual — as imagens em `imagens-tratadas/` são as definitivas.
- Não há `fluxo-codigo.md`: o manual é de **ativação/configuração** (não mapeia código do front).

---

## 3. Conteúdo da pasta

```
manuais\ativacao-aiqfome\
├─ MEMORIA.md                 (este arquivo)
├─ ativacao-aiqfome.md        (manual final)
├─ texto-documentation.ia.md  (prompt pronto p/ criar o manual no app)
├─ imagens-puras\             (11 originais — BACKUP, nunca referenciado)
└─ imagens-tratadas\          (11 imagens — usadas no manual; já vieram com marcações verdes)
```

---

## 4. Imagens (ordem e conteúdo)

| Arquivo | Tela | Destaque (verde) |
|---------|------|------------------|
| `01-configuracoes-loja-aiqfome.png` | Painel Geraldo — menu lateral | "Seu Restaurante" → **configurações da loja** |
| `02-codigo-loja-na-url.png` | Barra de endereço | **Store ID** no fim da URL (`142114`) |
| `03-menu-aplicativos-beefood.png` | Sidebar BeeFood | **Aplicativos** |
| `04-selecionar-aiqfome-v2.png` | Aplicativos → Delivery | card **Aiqfome V2** (seta) |
| `05-novo-cadastro.png` | Aiqfome V2 → Credenciais | **+ Novo Cadastro** |
| `06-salvar-cadastro.png` | Modal Novo Cadastro | ① Filial ② Store ID ③ **SALVAR (F2)** |
| `07-botao-conectar.png` | Lista de credenciais | **Conectar** (status Não conectado) |
| `08-login-magalu-email.png` | ID Magalu | campo **Email** + **Continuar** |
| `09-senha-magalu.png` | ID Magalu | campo **Senha** + **Entrar** |
| `10-selecionar-conta-pj.png` | Escolha uma conta | **Pessoa jurídica** |
| `11-confirmacao-conectado.png` | Aiqfome V2 → Credenciais | status **Conectado** (verde) |

---

## 5. Melhorias aplicadas (vs. original) — conforme imagens

- Rótulos exatos dos botões: **SALVAR (F2)**, **CANCELAR (ESC)**; menção a **Atualizar status**.
- Texto do Status do modal igual à tela: *"O status é gerenciado automaticamente pela integração"*.
- Citado o painel **Geraldo** e o item de menu **"Seu Restaurante"**.
- Dicas extras vistas nas telas do Magalu: **Não é você? Usar outro email**, **Entrar sem senha**.
- Caminhos de imagem padronizados para `imagens-tratadas/` (único diretório referenciado).
- Tabela do Passo 6 numerada (①②③) alinhada às marcações da imagem.

---

## 6. Estado / pendências

- Manual pronto. **Aguardando publicação** pelo dono.
- Não há ambiente de teste executado aqui (manual veio com imagens prontas).
