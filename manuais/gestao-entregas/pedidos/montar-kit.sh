#!/usr/bin/env bash
#
# Monta o zip que vai para quem tira os prints do app — a IA que opera o emulador, ou o dono.
#
# O kit é auto-suficiente de propósito: quem recebe não tem este repositório, não tem o painel e
# não deveria precisar de nenhum dos dois para fotografar uma tela de celular. Por isso ele leva o
# pedido, os scripts de cenário, os manuais já publicados como referência e a árvore de pastas de
# saída com os nomes exatos.
#
# Uso:
#   bash montar-kit.sh [destino]        # destino padrão: /opt/cursor/artifacts
#
set -euo pipefail

AQUI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GE="$(dirname "$AQUI")"
MANUAIS="$(dirname "$GE")"
DESTINO="${1:-/opt/cursor/artifacts}"
NOME="kit-teste-app-entregador"

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
KIT="$TMP/$NOME"

# --- 1. o pedido -----------------------------------------------------------------------------
mkdir -p "$KIT/1-pedido"
cp "$AQUI/README.md" "$AQUI/capturas-app.md" "$AQUI/janela-117.md" "$KIT/1-pedido/"
cp "$AQUI/instrucoes-ia-app.md" "$KIT/LEIA-PRIMEIRO.md"

# A última seção do README é a maquinaria do kit — os arquivos que não viajam nele. Cortada aqui
# para o kit não ficar com link apontando para arquivo que não existe lá dentro.
sed -i '/^## Quando quem fotografa não é você$/,$d' "$KIT/1-pedido/README.md"

# --- 2. os scripts ---------------------------------------------------------------------------
mkdir -p "$KIT/2-scripts"
cp "$GE/scripts/README.md" "$GE/scripts/cenario.js" "$GE/scripts/smoke-app.js" "$KIT/2-scripts/"

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
SAIDA="$KIT/4-entrega/capturas-2"
for pasta in 16-notificacoes 17-troca-de-entregador 18-ciclo-completo 19-sem-internet \
             20-permissao-e-presenca 21-listas-vazias 22-erros-de-cobranca \
             23-rota-com-problema 24-plataforma-sem-confirmacao 25-ios; do
  mkdir -p "$SAIDA/$pasta/prints"
done

# O `capturar.ps1` grava dois níveis acima de si mesmo. Posto aqui, sem nenhuma alteração, ele
# resolve para a raiz de `capturas-2/` — e `-Capitulo 16-notificacoes` cai no lugar certo.
mkdir -p "$SAIDA/_ferramentas/emulador"
cp "$ORIG/smoketests/emulador/"*.ps1 "$SAIDA/_ferramentas/emulador/"

cp "$AQUI/arvore-de-entrega.md" "$SAIDA/LEIA.md"

# --- 5. os links internos, ajustados para a árvore do kit ------------------------------------
sed -i 's#\.\./scripts/#../2-scripts/#g' "$KIT/1-pedido/"*.md
sed -i 's#\.\./pedidos/#../1-pedido/#g'  "$KIT/2-scripts/README.md" "$KIT/2-scripts/"*.js

# Os manuais de referência apontam para a pasta do repositório; no kit, o mesmo arquivo está três
# níveis acima. Os links que sobram quebrados são os manuais do painel, que o kit não leva.
sed -i -e 's#\.\./gestao-entregas/pedidos/#../../../1-pedido/#g' \
       -e 's#\.\./gestao-entregas/scripts/#../../../2-scripts/#g' \
       "$PUB"/*/*.md

# O zip nasce em disco local e só depois é copiado: o destino pode ser um ponto de montagem que
# não aceita escrita incremental de arquivo grande.
(cd "$TMP" && zip -qr "$TMP/$NOME.zip" "$NOME")

mkdir -p "$DESTINO"
rm -f "$DESTINO/$NOME.zip"
cp "$TMP/$NOME.zip" "$DESTINO/$NOME.zip"

echo "$DESTINO/$NOME.zip"
unzip -l "$DESTINO/$NOME.zip" | tail -1
