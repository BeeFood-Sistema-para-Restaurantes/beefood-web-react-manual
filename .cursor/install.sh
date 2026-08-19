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

# Referencias hospedadas no Bitbucket (backend). "repositoryDependencies" nao
# funciona aqui: ele so amplia o token do GitHub. Por isso o clone usa um
# Repository Access Token do proprio Bitbucket, com escopo Repositories: Read,
# exposto ao ambiente como o secret BITBUCKET_TOKEN (Cursor Dashboard ->
# Cloud Agents -> Secrets).
#
# Sem o secret configurado o bloco e ignorado: o setup continua e os manuais
# seguem sendo escritos so com o front.
REFERENCIAS_BITBUCKET=(
  # "workspace/repositorio"
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

clonar_bitbucket() {
  local slug="$1"
  local destino="${REFS_DIR}/$(basename "${slug}")"
  local url_limpa="https://bitbucket.org/${slug}.git"
  local url_auth="https://x-token-auth:${BITBUCKET_TOKEN}@bitbucket.org/${slug}.git"

  if [ -d "${destino}/.git" ]; then
    echo "--> atualizando (bitbucket) ${slug}"
    git -C "${destino}" fetch --depth 1 "${url_auth}" HEAD
    git -C "${destino}" reset --hard FETCH_HEAD
  else
    echo "--> clonando (bitbucket) ${slug}"
    git clone --depth 1 "${url_auth}" "${destino}"
  fi
  # O token nunca fica gravado no remote: ele expira e ainda vaza em qualquer
  # "git remote -v" dentro da sessao.
  git -C "${destino}" remote set-url origin "${url_limpa}"
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
  destino="${REFS_DIR}/$(basename "${slug}")"
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
