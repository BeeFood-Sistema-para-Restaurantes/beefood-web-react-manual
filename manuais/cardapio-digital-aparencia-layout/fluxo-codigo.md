# fluxo-codigo.md — #71 Aparência e layout do cardápio digital (uso interno, NÃO publicar)

- Página: `src/pages/CardapioDigital.tsx` — rota `/cardapio-digital?tab=configuracoes`.
- Card: `src/components/cardapio-digital/ConfiguracoesTab.tsx` (desktop).
- Mobile: `src/components/mobile/cardapio-digital/MobileConfiguracoesTab.tsx`.
- Preview sticky (xl+): `src/components/cardapio-digital/preview/PreviewCardapioDigital.tsx`.
- Seletores: `LayoutSetorSelector.tsx`, `LayoutCarrinhoSelector.tsx`,
  `VitrinePromocoesSelector.tsx`.
- Cores: `ModalAlterarCorTema.tsx` (tema) + `<input type="color">` (capa).
- Upload: `useUploadImageS3` + `otimizarImagemUpload` (máx 1600 px / 1 MB).
- Hook: `useCardapioDigitalConfiguracoes` + `useCardapioDigitalConfiguracaoLogic`.
- Auto-save: `useAutoSave` delay **800 ms**. Toast *Salvo automaticamente*.
  Mobile **não tem** botão Salvar. Modal da cor só confirma no estado local;
  o POST sai no debounce.
- **Capas e Destaques** (banners) é **outra** API (`/banners`) e outro
  manual (#48). A capa fixa daqui é `fotoCapa` (só imagem).

## API

```
GET  /datasnap/rest/empresaDelivery2/cardapioDigital/configuracoes/{empresa}/{filial}/{usuario}
POST /api/empresaDelivery2/cardapioDigital/configuracoes
```

POST manda o **snapshot inteiro** (delivery, presencial, redes…), não só
Aparência. `log` = payload anterior do GET.

| Tela | Estado | GET / POST | Default |
|------|--------|------------|---------|
| Nome Fantasia | `nomeFantasia` | `nomeFantasia` | `''` |
| Categoria | `categoriaID` | `deliveryCategoriaID` | `1` se null |
| ID | só leitura | `id` (não envia) | UUID |
| Cor do Tema | `corTema` | `corPrimaria` | `#dc2626` |
| Cor da Capa | `corCapa` | `corAcao` | `#000000` |
| Logo | `logoUrl` | `logotipoS3Link` | `''` |
| Capa | `capaUrl` | `fotoCapa` | `''` |
| Lista completa | `layoutSetor=false` | `layoutSetor` boolean | `false` |
| Navegação por setores | `layoutSetor=true` | idem | |
| Em Rolagem | `layoutStepCarrinho=false` | `layoutStepCarrinho` | `false` |
| Em Passos | `layoutStepCarrinho=true` | idem | |
| Destacar promoções | `destacar` | `exibirPromocoes=true` + `abrirPromocoesAuto=true` | `destacar` |
| Deixar a aba disponível | `disponivel` | `true` + `false` | |
| Não mostrar promoções | `desligado` | `false` + `false` | |

`lerVitrinePromocoes`: `exibirPromocoes===false` → desligado;
`abrirPromocoesAuto===false` → disponivel; senão destacar.

## Efeito no cardápio público (`menu.beefood.com.br/{link}`)

Fonte Vue **não** está neste repo. Mapeamento pelo painel + prova no
sandbox `beefood3`:

- `fotoCapa` = capa fixa do carrossel do topo (antes dos banners do #48).
- `logotipoS3Link` = logo sobre a capa.
- `corPrimaria` = faixa do topo, “Aberto agora”, botões, aba ativa.
- `corAcao` = fundo da capa quando não há imagem.
- `nomeFantasia` = nome no cabeçalho.
- `layoutSetor=false`: uma página com filtro de setores.
- `layoutSetor=true`: grid de setores primeiro. Setor sem foto = card cinza
  (alerta no painel). Foto do setor é em **Cardápio → Setores**.
- `layoutStepCarrinho=false`: todos os grupos de opção na mesma tela.
- `layoutStepCarrinho=true`: um grupo por passo + **Avançar** (loja inteira).
- Vitrine: aba **Promoções** no rodapé só existe se houver produto com
  preço promocional valendo. `desligado` some a aba; o preço riscado
  continua no produto. `destacar` abre a vitrine sozinha na primeira
  visita do dia.

Upload aceita PNG / JPEG / WEBP. Sem recorte. Ícone de câmera no preview
abre o seletor. Cache do menu público: até **1 minuto** (novidades do
produto; na prática o #70 usou até 5 min — esperar e recarregar).

IDs sandbox (BeeFood3): empresa 38311, filial 39202, usuário 88711.
Link: `https://menu.beefood.com.br/beefood3`.
