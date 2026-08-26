# MEMORIA.md — #57 BeeFood Entregador (aplicativo para motoboy)

## Escopo
Migração do artigo [BeeFood Aplicativo para Entregadores](https://ajuda.beefood.com.br/baseconhecimento/beefood-aplicativo-para-entregadores/).
Mesma mentalidade da fila #49–#56: prints do **app** e do cupom antigo **copiados** para o repo; telas em que o BeeFood **salva** (funcionário, usuário, layout do cupom) com print **novo** (tema claro, Playwright 1440×900 DPR 1.5).

## Origem
Pedido do dono em 26/08/2026. Não estava nos oito itens da fila `PLANO-MIGRACAO-AJUDA.md`. Sandbox BeeFood3 (`contato@beefood.com.br`).

## Imagens
| Arquivo | Tipo | O quê |
|---------|------|-------|
| `01-play-store.png` | contexto | Badge Google Play (artigo 2024) |
| `02-app-store.png` | contexto | Badge App Store (artigo 2024) |
| `03-app-ler-barcode.png` | contexto | App: LER CÓDIGO BARRAS + câmera + cupom |
| `04-app-entregas.png` | contexto | App: lista Entregas + detalhes |
| `05-app-rotas.png` | contexto | App: ABRIR ROTA → Maps / Waze |
| `06-app-finalizar.png` | contexto | App: FINALIZAR entrega |
| `07-app-ifood-confirmar.png` | contexto | App: CONFIRMAR ENTREGA IFOOD |
| `08-app-ifood-localizador.png` | contexto | App: colar localizador |
| `09-app-ifood-codigo.png` | contexto | App: código do cliente iFood |
| `10-cupom-barcode-resultado.png` | contexto | Cupom com código de barras (artigo) |
| `11-aplicativos-entregador.png` | setas | Aplicativos → card BeeFood Entregador |
| `12-modal-app-entregador.png` | setas | Modal: links de cadastro + lojas |
| `13-modal-funcionario-funcao.png` | setas | Função **Entregador** + SALVAR |
| `14-modal-usuario.png` | setas | Funcionário + switch **Aplicativos** |
| `15-modal-layout-barcode.png` | setas | **Código de Barras App Entrega** |

## Decisões
- “Acesso Aplicativos” do Windows virou o switch **Aplicativos** (`webAcesso`) no modal de usuário.
- Layout do cupom: caminho novo é **Configuração → Impressão → Layout → Cupom Pedido → Texto Padrão**, não “Layout Impressão Cupom” do Windows.
- Modal de Aplicativos não salva nada — entra porque é a tela nova do card e aponta os dois cadastros.
- Prints do app: sem recaptura (emulador Android não sobe neste ambiente).
- Ensaio: modal **Novo Usuário** preenchido só para o print; **não gravado**. Funcionário usado na captura: **Funcionário 1** (já era entregador).
- Checkbox `beeEntregaCodigoBarras` já estava ligado no sandbox; não mexi no layout.

## Status
Concluído — aguardando publicação do dono.
