# MEMORIA.md — #58 IA ChatGPT no WhatsApp

## Escopo
Manual de usuário final migrado do ajuda.beefood
([artigo antigo](https://ajuda.beefood.com.br/baseconhecimento/como-configurar-a-inteligencia-artificial-do-chatgpt-no-whatsapp-do-seu-restaurante/)).
Prints da **OpenAI** e dos **exemplos de WhatsApp** reaproveitados e **copiados**
para o repositório. Telas em que o BeeFood **salva** usam print **novo** (tema
claro, Playwright 1440×900 DPR 1.5).

## Origem
Pedido avulso depois da fila #49–#56 e do #57. Produzido em 28/08/2026 na conta
sandbox BeeFood3 (`contato@beefood.com.br`).

## Imagens
| Arquivo | Tipo | O que mostra |
|---------|------|----------------|
| `01`–`11` OpenAI | contexto | Login, telefone, API Keys, billing, usage |
| `12`–`15` WhatsApp | contexto | Exemplos de conversa do artigo antigo |
| `16-aplicativos-ia.png` | setas | Aplicativos (1) → card Inteligência Artificial (2) |
| `17-ia-boas-vindas.png` | setas | INICIAR CONFIGURAÇÃO |
| `18-ia-chave-secreta.png` | setas | Campo Chave Secreta |
| `19-ia-configuracoes.png` | setas | Ativar, modelo, nome, tipo Inteligente, SALVAR |

## Decisões
- **Não** migrar o print do BeeFood Windows nem o atalho ChatGPT da barra do
  BeeBot Windows. No web o liga/desliga é o switch **Ativar IA no WhatsApp**.
- **Não** colar chave OpenAI real no sandbox. O print do passo 3 usou intercept
  só do GET `/chatGPT/token/` (assistant_id fake `asst_…`) para abrir a tela;
  o GET de config (`empresaDelivery2/chatGPT`) veio real (nome BeeBot, tipo
  Inteligente). O switch foi ligado **só no estado local** — **SALVAR não foi
  clicado**.
- **Conhecimento extra** existe no produto (título + texto). Entra no manual
  como menção, sem tutorial do modal.
- Custos por modelo: mantidos do artigo antigo (estimativa).

## Status
Concluído — aguardando publicação do dono.
