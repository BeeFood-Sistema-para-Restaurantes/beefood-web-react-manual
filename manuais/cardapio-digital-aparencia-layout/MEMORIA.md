# MEMORIA.md — #71 Aparência e layout do cardápio digital

## Escopo
Aba **Cardápio Digital → Configurações**, card **Aparência**: trocar
capa e logo no preview, identidade, cores e os três layouts
(lista × setores, rolagem × passos, vitrine de promoções). Cada
opção aparece **lado a lado** com o resultado no cardápio público
(`montar_par`, padrão do #70).

Não cobre: Capas e Destaques / banners (#48), avisos (#47),
agendamento (#70), horário, link de acesso, domínio.

## Origem
Pedido do dono (30/08/2026): novo manual de layout do cardápio
digital — foto, capa e configurações; cada uma com o resultado no
cardápio ao lado.

## Imagens (planejado)
| Arquivo | Tipo | O que mostra |
|---------|------|----------------|
| `01-aparencia.png` | setas | Card Aparência: preview (capa/logo), identidade, cores |
| `02-par-capa-logo.png` | recorte | Painel: clicar capa/logo → cardápio: topo |
| `03-par-cores.png` | recorte | Painel: Cor do Tema / Cor da Capa → tema no cardápio |
| `04-par-lista-setores.png` | recorte | Lista completa × Navegação por setores |
| `05-par-opcoes.png` | recorte | Em Rolagem × Em Passos no produto |
| `06-par-vitrine.png` | recorte | Vitrine → aba Promoções (ou ausência) |

Fontes de celular ficam só em `imagens-puras/`.

## Decisões
- Número **#71** (#70 já é Agendamento).
- Auto-save 800 ms. Não clicar opção “só para ver”.
- Capa/logo: ensinar o clique no preview (máx 1 MB). **Não** trocar
  a foto da loja no sandbox — só mostrar o alvo.
- Cores: capturar o estado atual + o efeito no cardápio. Não deixar
  cor diferente no ar.
- Layouts: capturar os dois lados (mudar, esperar cache, print,
  **restaurar** o valor original).
- Vitrine: as três opções no texto; no recorte, o estado que o
  sandbox tiver + o contraste (com aba / sem aba) se der para
  fotografar sem quebrar o #69 (Milk Shake em promoção).
- Tira/par: painel à esquerda, cardápio à direita, seta no meio.
- Viewport celular 390×844 dsf 2. Não clicar Retirada na home.
- Cache: até 1 min (texto do produto); folga de até 5 min.

## Estado deixado no sandbox
(a preencher depois das capturas — restaurar capa, logo, cores e
layouts ao valor original)

## Status
Em execução.
