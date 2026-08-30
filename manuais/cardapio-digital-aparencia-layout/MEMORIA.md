# MEMORIA.md — #71 Aparência e layout do cardápio digital

## Escopo
Aba **Cardápio Digital → Configurações**, card **Aparência**: trocar
capa e logo no preview, identidade, cores e os três layouts
(lista × setores, rolagem × passos, vitrine de promoções). Cada
opção aparece **lado a lado** com o resultado no cardápio
(`montar_par` / `montar_dois_pares`, padrão do #70).

Não cobre: Capas e Destaques / banners (#48), avisos (#47),
agendamento (#70), horário, link de acesso, domínio.

## Origem
Pedido do dono (30/08/2026): novo manual de layout do cardápio
digital — foto, capa e configurações; cada uma com o resultado no
cardápio ao lado.

## Imagens
| Arquivo | Tipo | O que mostra |
|---------|------|----------------|
| `01-onde-fica.png` | setas | Sidebar + preview (capa/logo) + cores |
| `02-par-capa-logo.png` | recorte | Preview (câmeras) → topo do cardápio |
| `03-cor-tema.png` | setas | Modal da cor + prévia Ver sacola / Adicionar |
| `04-par-lista-setores.png` | recorte | Lista → filtro; setores → grid |
| `05-par-opcoes.png` | recorte | Rolagem → Combo One Burger; passos → 1-2-3 |
| `06-par-vitrine.png` | recorte | Dropdown → aba Promoções |
| `00-admin-full.png` | pura | Fonte do 01 |
| `02-preview.png` | pura | Fonte do 02 |
| `03b-modal-cor-tema.png` | pura | Fonte do 03 |
| `04b-layout-setor.png` | pura | Fonte do 04 |
| `04c-layout-opcoes.png` | pura | Fonte do 05 |
| `05b-vitrine-aberta.png` | pura | Fonte do 06 |
| `11-cel-produto-rolagem.png` | pura | Combo One Burger em rolagem |
| `12-cel-promocoes.png` | pura | Aba Promoções |
| `13-cel-home-setores.png` | pura | Home lista (nome histórico) |
| `21-preview-setores.png` | pura | Preview sticky com grid de setores |

## Decisões
- Número **#71** (#70 já é Agendamento).
- Auto-save 800 ms. Não clicar opção “só para ver”.
- Capa/logo: ensinar o clique no preview. **Não** trocamos a foto
  da loja no sandbox.
- Cores: modal da cor já traz a prévia lado a lado — usamos ele
  como figura 03.
- Layouts: POST autenticado confirmou `layoutSetor=true` no GET.
  O Vue `menu.beefood.com.br/beefood3` **não** virou o grid na
  sessão (cache ou app público atrasado). O resultado de setores
  saiu do **preview sticky** do painel (`Escolha um setor`).
  Passos: miniatura do próprio card (1-2-3 + Avançar). Rolagem:
  Combo One Burger real.
- Vitrine do sandbox: **Deixar a aba disponível**. Milk Shake e
  burgers em promoção (#69) sustentam a aba.
- Clique no banner verde de cupom **abre** ADICIONAR CUPOM — não
  usar esse texto para fechar.
- Viewport celular 390×844 dsf 2. Não clicar Retirada na home.

## Estado deixado no sandbox
- `layoutSetor=false` (Lista completa)
- `layoutStepCarrinho=false` (Em Rolagem)
- `exibirPromocoes=true`, `abrirPromocoesAuto=false` (Deixar a aba)
- Capa, logo, cores e nome **não** foram alterados
- Agendamento #70, tabelas #68/#69 e descontos #64 intactos

## Status
Concluído — aguardando publicação.
