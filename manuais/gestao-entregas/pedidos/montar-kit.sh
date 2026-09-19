#!/usr/bin/env bash
#
# Monta o zip que vai para quem tira os prints do app — a IA que opera o emulador, ou o dono.
#
# O kit é auto-suficiente de propósito: quem recebe não tem este repositório, não tem o painel e
# não deveria precisar de nenhum dos dois para fotografar uma tela de celular. Por isso ele leva o
# pedido, os scripts de cenário, os manuais já publicados como referência e a árvore de pastas de
# saída com os nomes exatos.
#
# O zip fica **versionado**, nesta mesma pasta, a pedido do dono: assim ele baixa direto do GitHub
# pelo botão de download do arquivo e repassa sem depender de WeTransfer nem de link que expira. São
# 24 MB num repositório que já tem 669 MB de imagem de manual, e o conteúdo é o mesmo que está
# versionado ao lado — o zip existe pela conveniência de ser um arquivo só.
#
# Uso:
#   bash montar-kit.sh [rodada] [destino]     # rodada padrão: 3 · destino padrão: esta pasta
#
# A **rodada** muda quatro coisas e nada mais: o nome do zip, o arquivo de pedido que é a tarefa, o
# `LEIA-PRIMEIRO` e a árvore de pastas de saída. O resto — scripts, manuais de referência, material
# original, ferramentas de emulador — é igual nas duas, porque é igual o trabalho.
#
# A rodada 2 continua aqui porque é a mesma maquinaria, com outra lista — mas o **zip** dela está
# congelado como foi entregue. Regravá-lo hoje o deixaria com 404 arquivos em vez de 323: a referência
# passou a incluir as 24 fotos que aquele pedido pede, e um kit que já traz a resposta do próprio
# pedido confunde quem o abre. Se precisar montá-la, mande para outro destino:
#   bash montar-kit.sh 2 /tmp
#
set -euo pipefail

AQUI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GE="$(dirname "$AQUI")"
MANUAIS="$(dirname "$GE")"
RODADA="${1:-3}"
DESTINO="${2:-$AQUI}"

case "$RODADA" in
  2)
    NOME="kit-teste-app-entregador"
    LEIA="instrucoes-ia-app.md"
    ARVORE="arvore-de-entrega.md"
    PEDIDOS=(README.md capturas-app.md janela-117.md)
    SAIDA_NOME="capturas-2"
    SAIDA_PASTAS=(16-notificacoes 17-troca-de-entregador 18-ciclo-completo 19-sem-internet
                  20-permissao-e-presenca 21-listas-vazias 22-erros-de-cobranca
                  23-rota-com-problema 24-plataforma-sem-confirmacao)
    ;;
  3)
    NOME="kit-teste-app-entregador-2"
    LEIA="instrucoes-ia-app-2.md"
    ARVORE="arvore-de-entrega-2.md"
    # O pedido da rodada 2 viaja junto como histórico: o da 3 se refere a ele, e o `README.md` da
    # pasta linka os dois. Link para arquivo que não está no zip é o defeito que este kit não tem.
    PEDIDOS=(README.md capturas-app-2.md capturas-app.md janela-117.md)
    SAIDA_NOME="capturas-3"
    SAIDA_PASTAS=(26-codigo-de-barras 27-historico-vazio 28-abrir-sem-rede)
    ;;
  *)
    echo "rodada desconhecida: $RODADA (use 2 ou 3)" >&2
    exit 1
    ;;
esac

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
KIT="$TMP/$NOME"

# --- 1. o pedido -----------------------------------------------------------------------------
mkdir -p "$KIT/1-pedido"
for arquivo in "${PEDIDOS[@]}"; do
  cp "$AQUI/$arquivo" "$KIT/1-pedido/"
done
cp "$AQUI/$LEIA" "$KIT/LEIA-PRIMEIRO.md"

# A última seção do README é a maquinaria do kit — os arquivos que não viajam nele. Cortada aqui
# para o kit não ficar com link apontando para arquivo que não existe lá dentro.
sed -i '/^## Quando quem fotografa não é você$/,$d' "$KIT/1-pedido/README.md"

# --- 2. os scripts ---------------------------------------------------------------------------
mkdir -p "$KIT/2-scripts"
cp "$GE/scripts/README.md" "$GE/scripts/cenario.js" "$GE/scripts/smoke-app.js" \
   "$GE/scripts/relogio.py" "$KIT/2-scripts/"

# --- 3. referência: os manuais publicados, com as imagens ------------------------------------
#
# As pastas vão com o nome que têm no repositório, sem prefixo de número, para os links que os
# manuais fazem entre si (`../app-entregador-rota/app-entregador-rota.md`) continuarem resolvendo
# dentro do kit. O número de cada um fica no `INDICE.md`.
PUB="$KIT/3-referencia/manuais-publicados"
for pasta in app-entregador-entrar app-entregador-entregas-do-dia app-entregador-rota \
             app-entregador-codigo-barras app-entregador-marketplace app-entregador-cobranca \
             gestao-entregas-ciclo-completo; do
  mkdir -p "$PUB/$pasta"
  cp "$MANUAIS/$pasta/$pasta.md" "$PUB/$pasta/"
  for extra in MEMORIA.md fluxo-codigo.md; do
    [ -f "$MANUAIS/$pasta/$extra" ] && cp "$MANUAIS/$pasta/$extra" "$PUB/$pasta/"
  done
  [ -d "$MANUAIS/$pasta/imagens-tratadas" ] && cp -r "$MANUAIS/$pasta/imagens-tratadas" "$PUB/$pasta/"
done
cp "$AQUI/indice-referencia.md" "$PUB/INDICE.md"

# --- 3b. referência: o material original do app, como veio -----------------------------------
ORIG="$GE/material-recebido/app-entregador"
mkdir -p "$KIT/3-referencia"
cp -r "$ORIG" "$KIT/3-referencia/material-original"

# --- 4. a árvore de saída --------------------------------------------------------------------
SAIDA="$KIT/4-entrega/$SAIDA_NOME"
for pasta in "${SAIDA_PASTAS[@]}"; do
  mkdir -p "$SAIDA/$pasta/prints"
done

# O `capturar.ps1` grava dois níveis acima de si mesmo. Posto aqui, sem nenhuma alteração, ele
# resolve para a raiz de `$SAIDA_NOME/` — e `-Capitulo <pasta>` cai no lugar certo.
mkdir -p "$SAIDA/_ferramentas/emulador"
cp "$ORIG/smoketests/emulador/"*.ps1 "$SAIDA/_ferramentas/emulador/"

cp "$AQUI/$ARVORE" "$SAIDA/LEIA.md"

# --- 5. os links internos, ajustados para a árvore do kit ------------------------------------
sed -i -e 's#\.\./scripts/#../2-scripts/#g' \
       -e 's#\.\./material-recebido/app-entregador/#../3-referencia/material-original/#g' \
       -e 's#\.\./material-recebido/#../3-referencia/#g' \
       "$KIT/1-pedido/"*.md
sed -i 's#\.\./pedidos/#../1-pedido/#g'  "$KIT/2-scripts/README.md" "$KIT/2-scripts/"*.js

# Os manuais de referência apontam para a pasta do repositório; no kit, o mesmo arquivo está três
# níveis acima. Os links que sobram quebrados são os dos manuais do painel, que o kit não leva — e é
# de propósito: o kit é sobre o aplicativo, e carregar os onze do painel dobraria o zip.
sed -i -e 's#\.\./gestao-entregas/pedidos/#../../../1-pedido/#g' \
       -e 's#\.\./gestao-entregas/scripts/#../../../2-scripts/#g' \
       -e 's#\.\./gestao-entregas/material-recebido/app-entregador/#../../material-original/#g' \
       -e 's#\.\./gestao-entregas/material-recebido/#../../material-original/#g' \
       "$PUB"/*/*.md

# O material original tem README próprio, e ele aponta para a pasta de pedidos do repositório.
# `-maxdepth 2` porque os arquivos dos 15 capítulos ficam um nível abaixo e não têm esses links.
#
# O link para o próprio zip perde o destino aqui — nenhum kit carrega uma cópia de si mesmo —, então
# ele vira texto simples em vez de link morto.
find "$KIT/3-referencia/material-original" -maxdepth 2 -name '*.md' -print0 \
  | xargs -0 sed -i -e 's#\[`\(kit-teste-app-entregador[^`]*\.zip\)`\](\.\./\.\./\.\./pedidos/[^)]*)#`\1`#g' \
                    -e 's#\.\./\.\./\.\./pedidos/#../../../1-pedido/#g'

# O zip nasce em disco local e só depois é copiado: o destino pode ser um ponto de montagem que
# não aceita escrita incremental de arquivo grande.
(cd "$TMP" && zip -qr "$TMP/$NOME.zip" "$NOME")

mkdir -p "$DESTINO"
rm -f "$DESTINO/$NOME.zip"
cp "$TMP/$NOME.zip" "$DESTINO/$NOME.zip"

echo "$DESTINO/$NOME.zip"
unzip -l "$DESTINO/$NOME.zip" | tail -1
