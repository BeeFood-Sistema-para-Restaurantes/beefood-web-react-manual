#!/usr/bin/env python3
"""Procura conteudo tecnico nos arquivos publicaveis dos manuais.

O manual do lojista e "como eu uso", nunca "como o sistema faz": rota de API, nome de
campo, nome de arquivo do codigo e jargao de programador sao anotacao interna e moram
no fluxo-codigo.md. Em 23/09/2026 uma pagina publicada saiu com a rota da API do cupom
e dois nomes de campo do cashback, porque nada conferia isso.

O que este script NAO acusa, de proposito:

- URL completa de webhook (`https://.../api/...`): o lojista copia e cola no painel do
  parceiro, entao e conteudo dele.
- bloco de codigo com o "Resumo do caminho" ou um desenho de layout: e texto de tela,
  nao codigo. Bloco com `const`, `import`, `=>`, `{`, `;` ou JSON, sim, e acusado.
- jargao dentro de **negrito** ou `monoespacado`: ali ele e o nome literal de um campo
  ou de uma janela que o lojista ve (a Uber chama a janela de "Crie um endpoint").

Uso, de qualquer pasta:
    python .cursor/skills/manual-sistema/scripts/conferir-vazamento.py
    python .cursor/skills/manual-sistema/scripts/conferir-vazamento.py totem-

Codigo de saida: 0 se tudo limpo, 1 se houver achado.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# .cursor/skills/manual-sistema/scripts/ -> raiz do repositorio
RAIZ = Path(__file__).resolve().parents[4]
MANUAIS = RAIZ / "manuais"

# Padroes que valem na linha crua: aqui o backtick nao salva ninguem.
ESTRUTURAIS = [
    (r"(?<!\w)/api/[a-zA-Z0-9]", "rota de API"),
    (r"\b(?:GET|POST|PUT|PATCH|DELETE)\s+[/`]", "verbo HTTP com rota"),
    (r"\b[a-zA-Z][\w-]*\.(?:tsx|ts|jsx|js|py)\b", "nome de arquivo de codigo"),
    (r"\b\w+\[\]", "nome de campo de lista"),
    (r"\b\w+\s*=\s*(?:true|false)\b", "campo booleano"),
    (r"n[ãa]o publicar", "secao interna dentro do arquivo publicavel"),
]

# Palavras que so fazem sentido para quem programa.
JARGAO = ["backend", "endpoint", "payload", "array", "bundle", "front-end", "frontend"]

# Endereco que o lojista precisa copiar para configurar uma integracao.
LIBERADOS = re.compile(r"https?://[^\s`]*/api/", re.I)

# Dentro de um bloco cercado, o que denuncia codigo de verdade.
CODIGO_DE_VERDADE = re.compile(
    r"(?:\bconst\b|\blet\b|\bimport\b|\bfunction\b|=>|;\s*$|^\s*[{}]|\"\w+\":)"
)

SEM_NEGRITO_NEM_MONO = re.compile(r"\*\*[^*]*\*\*|`[^`]*`")


def achados_do_bloco(linhas: list[str], inicio: int) -> list[str]:
    if any(CODIGO_DE_VERDADE.search(linha) for linha in linhas):
        return [f"{inicio}: bloco de codigo"]
    return []


def conferir(caminho: Path) -> list[str]:
    achados: list[str] = []
    bloco: list[str] | None = None
    abertura = 0

    for numero, linha in enumerate(caminho.read_text(encoding="utf-8").split("\n"), 1):
        if linha.lstrip().startswith("```"):
            if bloco is None:
                bloco, abertura = [], numero
            else:
                achados += achados_do_bloco(bloco, abertura)
                bloco = None
            continue
        if bloco is not None:
            bloco.append(linha)
            continue

        liberada = bool(LIBERADOS.search(linha))
        for padrao, motivo in ESTRUTURAIS:
            for achado in re.finditer(padrao, linha):
                if liberada:
                    continue
                achados.append(f"{numero}: {motivo} — {achado.group(0)!r}")

        prosa = SEM_NEGRITO_NEM_MONO.sub("", linha)
        for palavra in JARGAO:
            if re.search(rf"\b{palavra}\b", prosa, re.I):
                achados.append(f"{numero}: jargao — {palavra!r}")

    return achados


def main() -> int:
    prefixo = sys.argv[1] if len(sys.argv) > 1 else ""
    total = 0
    pastas = sorted(
        p for p in MANUAIS.iterdir() if p.is_dir() and p.name.startswith(prefixo)
    )
    for pasta in pastas:
        publicavel = pasta / f"{pasta.name}.md"
        if not publicavel.exists():
            print(f"AVISO: {pasta.name} nao tem {pasta.name}.md")
            continue
        achados = conferir(publicavel)
        marca = "LIMPO" if not achados else f"{len(achados)} ACHADO(S)"
        print(f"{marca:>12}  {publicavel.relative_to(RAIZ)}")
        for achado in achados:
            print(f"               {achado}")
        total += len(achados)
    print(f"\n{len(pastas)} manuais conferidos, {total} achado(s).")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
