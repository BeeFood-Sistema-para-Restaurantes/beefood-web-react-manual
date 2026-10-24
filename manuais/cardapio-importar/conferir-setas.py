"""Confere, neste manual, se o texto e as setas falam a mesma coisa.

Duas perguntas, que a revisão no olho erra com dezoito imagens e cinquenta setas:

* toda seta **desenhada** pelo `annotate.py` é **citada** no `.md`?
* todo número **citado** no `.md` existe como seta **naquela** imagem?

A convenção da casa diz que o número aparece em duas posições, e só nessas: `(N)` no parágrafo
imediatamente **antes** da imagem, ou na tabela imediatamente **depois** dela.

Diferença em relação ao conferidor do #129: aqui as coordenadas são **frações** (`0.345`), não
pixels, e há duas imagens de contexto, sem seta nenhuma, entrando por `passthrough()` — elas
passam quando o texto também não cita número.

Rodar dentro da pasta do manual:

    python3 conferir-setas.py

Sai com código 1 quando acha divergência.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PASTA = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
APOIO = ("fluxo-codigo.md", "MEMORIA.md", "texto-documentation.ia.md")

manual = next(p for p in sorted(PASTA.glob("*.md")) if p.name not in APOIO)
texto = manual.read_text(encoding="utf-8")
script = (PASTA / "annotate.py").read_text(encoding="utf-8")

# --- o que o annotate.py desenha ---------------------------------------------------------
desenhadas: dict[str, set[int]] = {}
for bloco in re.split(r"\n(?=annotate\(|passthrough\()", script):
    m = re.search(r'^(?:annotate|passthrough)\(\s*\n?\s*"([^"]+)"', bloco)
    if not m:
        continue
    saida = re.search(r'saida="([^"]+)"', bloco)
    nome = saida.group(1) if saida else m.group(1)
    desenhadas[nome] = {int(n) for n in
                        re.findall(r"\(\s*(\d+),\s*[\d.]+,\s*[\d.]+,", bloco)}

# --- o que o manual cita ------------------------------------------------------------------
citadas: dict[str, set[int]] = {}
partes = re.split(r"!\[[^\]]*\]\((imagens-tratadas/[^)]+)\)", texto)
for i in range(1, len(partes), 2):
    arquivo = Path(partes[i]).name
    antes = partes[i - 1].split("\n#")[-1]           # só o trecho depois do último título
    depois = partes[i + 1] if i + 1 < len(partes) else ""
    tabela: list[str] = []
    for linha in depois.splitlines():                # a tabela imediatamente depois
        if linha.startswith("|"):
            tabela.append(linha)
        elif tabela:
            break
    numeros = {int(n) for n in re.findall(r"\((\d+)\)", antes)}
    numeros |= {int(m.group(1)) for m in
                (re.match(r"\|\s*(\d+)\s*\|", l) for l in tabela) if m}
    citadas[arquivo] = numeros

# --- comparação ---------------------------------------------------------------------------
falhas = 0
for nome in sorted(set(desenhadas) | set(citadas)):
    d, c = desenhadas.get(nome, set()), citadas.get(nome, set())
    if d == c:
        print(f"ok    {nome}: {sorted(d) or 'contexto, sem seta'}")
        continue
    falhas += 1
    print(f"ERRO  {nome}: sem citação no texto={sorted(d - c)}"
          f" | citado sem seta na imagem={sorted(c - d)}")

print(f"\nimagens: {len(desenhadas)} | setas: {sum(len(v) for v in desenhadas.values())}"
      f" | falhas: {falhas}")
sys.exit(1 if falhas else 0)
