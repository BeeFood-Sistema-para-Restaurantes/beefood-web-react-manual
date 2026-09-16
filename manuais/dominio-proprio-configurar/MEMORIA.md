# MEMORIA.md — #101 Configurar domínio próprio e subdomínio

## Pedido do dono (16/09/2026)

> "em /aplicativos -> domínio próprio agora é possível configurar o seu próprio
> domínio diretamente pela tela e iremos criar um manual de configuração de:
> 1. 1.1 domínio próprio / 1.2 alterar zona DNS / 1.3 excluir domínio
> 2. 2.1 subdomínio — são 2 fluxos diferentes.
> (…) 1.1 → tu faz a configuração com o domínio cardapioteste.com.br → me passa o
> DNS e espera eu te retornar. Assim que eu retornar tu mostra o domínio com
> sucesso configurado e depois segue para 1.2. depois faz 1.3 e conclui. depois já
> pode seguir pro 2.1, me passa o CNAME, eu te retorno e você finaliza tudo."

## Escopo

A tela **nova** de Aplicativos → **Domínio Próprio**, em que o próprio lojista
cadastra o endereço sem passar pelo suporte. Dois fluxos:

1. **Domínio próprio (APEX)** — `cardapioteste.com.br`: cadastro, troca dos
   servidores DNS, domínio no ar, **aba DNS** (a "zona DNS") e **exclusão**.
2. **Subdomínio** — `cardapio.cardapioteste.com.br`: cadastro e registro **CNAME**.

**Não é o #52.** O manual `manuais/dominio-proprio/` documenta o modal antigo
(*Domínio Personalizado* → falar com o suporte) e a verificação na Meta, e continua
valendo para quem ainda não foi liberado: `dominioAcesso.ts` libera a tela nova em
produção **só para a empresa 38311**, que por sorte é o sandbox dos manuais.

## Ambiente

- Capturas em **produção** (`https://beefood.app`), sandbox BeeFood3
  (`contato@beefood.com.br`), empresa **38311**, filial **39202**, tema claro,
  1440×900 DPR 1.5 → puras 2160×1350.
- O domínio de teste é do dono: **`cardapioteste.com.br`**. Em 16/09 ele ainda não
  resolvia no DNS (sem NS, sem SOA), o que fez a tela mostrar o aviso amarelo
  *"Não encontramos … no DNS"* — o cadastro é liberado mesmo assim.
- Antes deste trabalho havia um cadastro de ensaio do mesmo domínio, removido às
  13:58 de 16/09 (aparece em *Domínios removidos anteriormente*, `dominioID 13`).
  O cadastro que vale é o **`dominioID 14`**, criado 16/09 14:30.

## Cronologia (o manual precisa parar para o dono trocar o DNS)

| Etapa | Quando | Situação |
|-------|--------|----------|
| 1.1 cadastro do APEX + instrução NS | 16/09 14:30 | ✅ capturado (imagens 01–06) |
| 1.1 domínio **No ar** | depende do dono trocar os NS | ⏸ aguardando |
| 1.2 aba **DNS** (zona) | depois do domínio no ar | ⏸ aguardando |
| 1.3 excluir domínio | depois de 1.2 | ⏸ aguardando |
| 2.1 subdomínio + CNAME | depois de 1.3 | ⏸ aguardando |

**Servidores DNS entregues ao dono em 16/09 14:31** (é o que ele precisa colocar no
registrador de `cardapioteste.com.br`):

```
ns-991.awsdns-59.net
ns-62.awsdns-07.com
ns-1150.awsdns-15.org
ns-1648.awsdns-14.co.uk
```

## Imagens

| Arquivo | Tipo | Conteúdo |
|---------|------|----------|
| `01-aplicativos-dominio.png` | setas 1–2 | Aplicativos → card **Domínio Próprio** |
| `02-escolher-cardapio.png` | seta 1 | passo 1: escolher o cardápio |
| `03-escolher-tipo.png` | contexto | passo 2: os dois cartões (domínio próprio × subdomínio) |
| `04-endereco-conferido.png` | setas 1–4 | passo 3: endereço conferido, aviso e **CADASTRAR DOMÍNIO** |
| `05-cadastrado-preparando.png` | seta 1 | *Estamos preparando os dados do seu DNS* (~1 min) |
| `06-instrucao-ns.png` | setas 1–3 + moldura | os quatro servidores DNS e o **Já configurei, verificar agora** |

A imagem **03** ficou de **contexto** de propósito: a tela inteira são os dois
cartões, cada um com título próprio, e o manual os compara numa tabela. Seta ali só
cobriria o texto de um dos dois (o cartão do APEX tem o aviso do e-mail, que é
justamente o que precisa ser lido).

## Decisões

- **Recortar o painel lateral (pedido do dono, 16/09).** A captura inteira tem
  2160 px e o painel começa exatamente em **x = 1154**: mais da metade da imagem era
  tela escurecida sem uso, e o texto do painel ficava pequeno na página publicada.
  Agora o `annotate.py` recorta em `PAINEL = (1154, 0, 2160, 1350)` e cola uma
  **faixa branca de 150 px à esquerda**, que é onde ficam as etiquetas — as setas
  entram na horizontal e nenhuma cruza texto. Cada imagem também é cortada na altura
  (`ate(y)`) para não sobrar branco embaixo. As **coordenadas continuam sendo medidas
  na captura pura de 2160 px**; a função converte. Só a `01`, que é a tela de
  Aplicativos, fica inteira.
- Etiqueta e traço mantêm o tamanho da captura inteira (`RAIO = 27`, `TRACO = 4`)
  passados na mão: o recorte não redimensiona o painel, então a proporção
  etiqueta × texto continua igual à dos outros manuais.
- Captura da instrução de DNS precisa **rolar até o botão** *Já configurei,
  verificar agora* (`scroll_into_view_if_needed`), senão o 4º servidor fica cortado
  — foi o que aconteceu na primeira tentativa. Etapa própria no script:
  `python3 capturar.py instrucao`.
- O script grava de verdade. `DRY=1` percorre o caminho inteiro e para antes do
  clique que grava (regra da `MEMORIA-GERAL.md`, seção 7) — usado antes do cadastro
  e será usado antes da exclusão.

## Status

Em andamento — parte 1.1 capturada até a entrega dos servidores DNS; o resto depende
do retorno do dono.
