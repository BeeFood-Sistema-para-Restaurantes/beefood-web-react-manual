# MEMORIA.md — #63 Ativar integração Uai Rango

## Escopo
Migração do artigo [Ativar integração Uai Rango](https://ajuda.beefood.com.br/baseconhecimento/ativar-integracao-uai-rango/).
Mesma mentalidade da fila #49–#57: print do **painel Uai Rango** copiado do artigo;
telas em que o BeeFood **salva** (token e formas) com print **novo** (tema claro,
Playwright 1440×900 DPR 1.5).

## Origem
Pedido do dono em 28/08/2026. Não estava nos oito itens da fila `PLANO-MIGRACAO-AJUDA.md`.
Sandbox BeeFood3 (`contato@beefood.com.br`).

## Imagens
| Arquivo | Tipo | O quê |
|---------|------|-------|
| `01-uairango-painel-token.png` | contexto | Uai Rango admin: Estabelecimento → Integração → Sim → Token (artigo 2023) |
| `02-beefood-aplicativos.png` | setas | Aplicativos (1) → card UaiRango (2) |
| `03-beefood-modal-credenciais.png` | setas | **+ Novo Cardápio** (1) + aviso de suporte (2) |
| `04-beefood-modal-token.png` | setas | Token (1), Cardápio de Origem (2), SALVAR (3) |
| `05-beefood-formas-recebimento.png` | setas | Aba Formas Recebimento (1) + select (2) |

## Decisões
- Prints do Windows (`fffe.png`, `regeh.png`, `jjj.png`, `fvafesd.png`) **não** entram:
  a tela nova é o modal web com abas **Credenciais** e **Formas Recebimento**.
- O botão antigo *Configurar credenciais* virou **+ Novo Cardápio**. O campo é **Token**
  (não “ID”). Grava com **SALVAR (F2)**.
- Não existe mais o botão *Cadastro Forma Recebimento* dentro da janela do marketplace.
  Se faltar forma, o texto manda para **Cadastro → Formas Recebimento**.
- Banner azul do produto: *Entre em contato com o Suporte para ativar a integração.*
  Mantido no manual, junto com a espera de até 1 h do artigo antigo.
- Token de ensaio `cole-aqui-o-token-do-uai-rango` só para o print; **CANCELAR**, não gravou.
  API `GET /uairango/restaurante/38311/88711` = `[]`.
- Formas já existiam no sandbox com crédito/débito invertidos. Corrigi no print
  (Mastercard/Visa Crédito → Crédito; Débito → Débito) e deixei assim — sem credencial
  ativa, não há pedido Uai Rango nesta conta.
- *UaiRango Online (inativa)* no seletor é o cadastro da loja; o texto do manual não
  trata como obrigatório.

## Status
Concluído — aguardando publicação do dono.
