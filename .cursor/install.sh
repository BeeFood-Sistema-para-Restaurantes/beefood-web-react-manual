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

mkdir -p "${REFS_DIR}"

# Um repositorio de referencia inacessivel nao impede trabalhar nos manuais,
# entao registramos a falha e seguimos em vez de abortar o setup inteiro.
falhas=()
for slug in "${REFERENCIAS[@]}"; do
  if ! clonar_ou_atualizar "${slug}"; then
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
for slug in "${REFERENCIAS[@]}"; do
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
  echo "Confira se o GitHub App do Cursor tem o repositorio selecionado E se ele"
  echo "esta listado em repositoryDependencies no .cursor/environment.json."
fi
