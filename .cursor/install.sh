#!/usr/bin/env bash
# Prepara o ambiente do Cloud Agent para escrever os manuais.
# Precisa ser idempotente: roda de novo sobre um ambiente ja preparado.
set -euo pipefail

REFS_DIR="${HOME}/refs"

# Repositorios de referencia, usados somente para LEITURA do codigo ao escrever
# os manuais (rotas, labels, validacoes -> fluxo-codigo.md).
#
# Toda entrada aqui precisa estar tambem em "repositoryDependencies" no
# environment.json. Esse campo NAO clona nada: ele apenas inclui o repositorio
# no token do GitHub gerado para o ambiente. Sem isso o clone abaixo falha com
# "Repository not found", mesmo que o GitHub App tenha acesso.
#
# ATENCAO: esse escopo extra so vale DURANTE o install. O token que o agente usa
# depois, ja em sessao, volta a enxergar apenas o repositorio de manuais. Ou seja,
# este script e a unica janela em que da para baixar o codigo de referencia -- por
# isso o clone precisa acontecer aqui, e nao sob demanda no meio do trabalho.
REFERENCIAS=(
  "BeeFood-Sistema-para-Restaurantes/beefood-web-react"
)

# Referencias hospedadas no Bitbucket (backend e apps). "repositoryDependencies"
# nao funciona aqui: ele so amplia o token do GitHub. Por isso o clone usa um
# token do proprio Bitbucket, exposto ao ambiente como secret
# (Cursor Dashboard -> Cloud Agents -> Secrets).
#
# Formato de cada entrada: "workspace/repositorio#branch" (o "#branch" e
# opcional; sem ele o clone traz a branch default).
#
# Sem nenhum secret configurado o bloco e ignorado: o setup continua e os
# manuais seguem sendo escritos so com o front.
REFERENCIAS_BITBUCKET=(
  "beetechbr/beetech-server-node-2.0#beefood-web-react"
  # App Android do cardapio no tablet. Traz "docs/manual-modo-kiosk.md" e
  # "docs/images", que o manual do modo kiosk precisa. Um Repository Access
  # Token e escopado a UM repositorio: se o BITBUCKET_TOKEN atual so alcanca o
  # beetech-server-node-2.0, cadastre um segundo secret para este (veja
  # TOKENS_BITBUCKET, abaixo) ou troque por um token de workspace/projeto.
  "beetechbr/beetech-appgarcom-android"
)

# Nomes das variaveis de ambiente que podem trazer um token do Bitbucket. Cada
# repositorio tenta todas, na ordem, o que permite um token por repositorio sem
# precisar ampliar o escopo de um token existente. Adicionar um secret novo aqui
# NAO quebra nada: variavel vazia e simplesmente ignorada.
TOKENS_BITBUCKET=(
  "BITBUCKET_TOKEN"
  "BITBUCKET_TOKEN_APPGARCOM"
)

# O usuario da URL depende do tipo de token: "x-token-auth" para Access Token de
# repositorio/projeto/workspace, "x-bitbucket-api-token-auth" para os novos
# Atlassian API tokens. Tentamos os dois, na ordem.
USUARIOS_BITBUCKET=(
  "x-token-auth"
  "x-bitbucket-api-token-auth"
)

clonar_ou_atualizar() {
  local slug="$1"
  local destino="${REFS_DIR}/$(basename "${slug}")"

  if [ -d "${destino}/.git" ]; then
    echo "--> atualizando ${slug}"
    git -C "${destino}" fetch --depth 1 origin HEAD
    git -C "${destino}" reset --hard FETCH_HEAD
  else
    echo "--> clonando ${slug}"
    git clone --depth 1 "https://github.com/${slug}.git" "${destino}"
    # Grava a URL limpa: se o token do momento ficar embutido no remote, ele
    # expira e trava qualquer atualizacao futura deste clone.
    git -C "${destino}" remote set-url origin "https://github.com/${slug}.git"
  fi
}

# Valores dos tokens do Bitbucket que existem neste ambiente, na ordem de
# TOKENS_BITBUCKET. Variavel nao definida ou vazia fica de fora.
valores_tokens_bitbucket() {
  local nome valor
  for nome in "${TOKENS_BITBUCKET[@]}"; do
    valor="${!nome:-}"
    [ -n "${valor}" ] && printf '%s\n' "${valor}"
  done
}

# Roda o git escondendo QUALQUER token conhecido das mensagens impressas.
git_sem_vazar() {
  local saida status=0 token
  saida=$("$@" 2>&1) || status=$?
  while IFS= read -r token; do
    saida="${saida//${token}/***}"
  done < <(valores_tokens_bitbucket)
  printf '%s\n' "${saida}"
  return "${status}"
}

bitbucket_slug() { printf '%s' "${1%%#*}"; }

bitbucket_branch() {
  local entrada="$1"
  [ "${entrada}" = "${entrada%%#*}" ] || printf '%s' "${entrada#*#}"
}

bitbucket_destino() { printf '%s' "${REFS_DIR}/$(basename "$(bitbucket_slug "$1")")"; }

clonar_bitbucket() {
  local entrada="$1"
  local slug branch destino url_limpa
  slug="$(bitbucket_slug "${entrada}")"
  branch="$(bitbucket_branch "${entrada}")"
  destino="$(bitbucket_destino "${entrada}")"
  url_limpa="https://bitbucket.org/${slug}.git"

  # Um Access Token e escopado a um repositorio, entao tentamos todos os tokens
  # do ambiente; e o tipo do token define o usuario da URL, entao tentamos as
  # duas formas de usuario para cada um.
  local token usuario url_auth
  while IFS= read -r token; do
    for usuario in "${USUARIOS_BITBUCKET[@]}"; do
      url_auth="https://${usuario}:${token}@bitbucket.org/${slug}.git"

      if [ -d "${destino}/.git" ]; then
        echo "--> atualizando (bitbucket) ${slug}${branch:+ [${branch}]} como ${usuario}"
        if git_sem_vazar git -C "${destino}" fetch --depth 1 "${url_auth}" "${branch:-HEAD}" \
          && git -C "${destino}" reset --hard FETCH_HEAD >/dev/null; then
          git -C "${destino}" remote set-url origin "${url_limpa}"
          return 0
        fi
      else
        echo "--> clonando (bitbucket) ${slug}${branch:+ [${branch}]} como ${usuario}"
        if git_sem_vazar git clone --depth 1 ${branch:+--branch "${branch}"} \
          "${url_auth}" "${destino}"; then
          # O token nunca fica gravado no remote: ele expira e ainda vaza em
          # qualquer "git remote -v" dentro da sessao.
          git -C "${destino}" remote set-url origin "${url_limpa}"
          return 0
        fi
        # Um clone parcial atrapalha a proxima tentativa.
        rm -rf "${destino}"
      fi
    done
  done < <(valores_tokens_bitbucket)

  echo "    nenhuma forma de autenticacao funcionou para ${slug}"
  return 1
}

mkdir -p "${REFS_DIR}"

# Um repositorio de referencia inacessivel nao impede trabalhar nos manuais,
# entao registramos a falha e seguimos em vez de abortar o setup inteiro.
falhas=()
for slug in "${REFERENCIAS[@]}"; do
  if ! clonar_ou_atualizar "${slug}"; then
    falhas+=("${slug}")
  fi
done

for slug in "${REFERENCIAS_BITBUCKET[@]:-}"; do
  [ -n "${slug}" ] || continue
  if [ -z "${BITBUCKET_TOKEN:-}" ]; then
    echo "--> ${slug} ignorado: secret BITBUCKET_TOKEN nao configurado"
    falhas+=("${slug}")
    continue
  fi
  if ! clonar_bitbucket "${slug}"; then
    falhas+=("${slug}")
  fi
done

# Pillow: usado pelos annotate.py para desenhar as setas verdes numeradas.
# Playwright: captura as telas do sistema em producao.
echo "--> instalando Pillow e Playwright"
pip_instalar() {
  python3 -m pip install --quiet --upgrade "$@" \
    || python3 -m pip install --quiet --upgrade --break-system-packages "$@"
}
pip_instalar pillow playwright
python3 -m playwright install chromium

echo
echo "===== resumo do setup ====="
python3 -c 'import PIL; print("Pillow", PIL.__version__)'
python3 -c 'import playwright; from importlib.metadata import version; print("Playwright", version("playwright"))'
sem_acesso=0
for slug in "${REFERENCIAS[@]}" "${REFERENCIAS_BITBUCKET[@]:-}"; do
  [ -n "${slug}" ] || continue
  # Entradas do Bitbucket podem trazer "#branch", que nao faz parte do caminho.
  destino="${REFS_DIR}/$(basename "${slug%%#*}")"
  if [ ! -d "${destino}/.git" ]; then
    echo "FALHA ${slug} (sem acesso)"
    sem_acesso=$((sem_acesso + 1))
    continue
  fi

  total=$(find "${destino}" -type f | wc -l)
  # Um clone que ja existe continua servindo mesmo se o fetch falhar: o codigo
  # esta em disco. So avisamos que ele pode estar atrasado.
  if printf '%s\n' "${falhas[@]:-}" | grep -qxF "${slug}"; then
    echo "OK    ${slug} -> ${destino} (${total} arquivos, NAO atualizado nesta rodada)"
  else
    echo "OK    ${slug} -> ${destino} (${total} arquivos)"
  fi
done

if [ "${sem_acesso}" -gt 0 ]; then
  echo
  echo "AVISO: sem acesso a ${sem_acesso} repositorio(s) de referencia."
  echo "GitHub: confira se o GitHub App do Cursor tem o repositorio selecionado E"
  echo "se ele esta listado em repositoryDependencies no .cursor/environment.json."
  echo "Bitbucket: confira o secret BITBUCKET_TOKEN (Repository Access Token com"
  echo "escopo Repositories: Read) e o slug workspace/repositorio no install.sh."
fi
