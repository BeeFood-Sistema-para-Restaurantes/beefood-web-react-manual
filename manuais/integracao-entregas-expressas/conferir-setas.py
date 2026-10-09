"""Confere, neste manual, se o texto e as setas falam a mesma coisa.

Duas perguntas, que a revisão no olho erra com onze imagens e 36 setas:

* toda seta **desenhada** pelo `annotate.py` é **citada** no `.md`?
* todo número **citado** no `.md` existe como seta **naquela** imagem?

A convenção da casa diz que o número aparece em duas posições, e só nessas: `(N)` no parágrafo
imediatamente **antes** da imagem, ou na tabela imediatamente **depois** dela. Quando a ação
está numa imagem anterior, o texto escreve *"a seta N da imagem acima"* — e esse caso é
conferido à parte, contra a imagem **anterior**, porque é dela que o número é.

Rodar dentro da pasta do manual:

    python3 conferir-setas.py

Sai com código 1 quando acha divergência. Ele é **deste manual**: lê os marcadores no formato
`(numero, alvo_x, alvo_y, etiqueta_x, etiqueta_y)` e as funções `annotate`, `painel` e
`dialogo` do `annotate.py` daqui. Passá-lo nos 119 manuais da pasta mostrou que só 22 têm o
texto e o script arrumados desta forma — generalizar exigiria ler cada estilo antigo, e não é
o que este manual precisa.
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
for bloco in re.split(r"\n(?=annotate\(|painel\(|dialogo\()", script):
    m = re.search(r'^(?:annotate|painel|dialogo)\(\s*\n?\s*"([^"]+)"', bloco)
    if not m:
        continue
    saida = re.search(r'saida="([^"]+)"', bloco)
    nome = saida.group(1) if saida else m.group(1)
    numeros = {int(n) for n in re.findall(r"\(\s*(\d+),\s*\d+,\s*\d+,", bloco)}
    if numeros:
        desenhadas[nome] = numeros

# --- o que o manual cita ------------------------------------------------------------------
citadas: dict[str, set[int]] = {}
retro: dict[str, list[int]] = {}
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
    anteriores = [int(n) for n in re.findall(r"setas? (\d+) da imagem", antes)]
    citadas[arquivo] = numeros - set(anteriores)
    retro[arquivo] = anteriores

# --- comparação ---------------------------------------------------------------------------
falhas = 0
for nome in sorted(set(desenhadas) | set(citadas)):
    d, c = desenhadas.get(nome, set()), citadas.get(nome, set())
    if d == c:
        print(f"ok    {nome}: {sorted(d)}")
        continue
    falhas += 1
    print(f"ERRO  {nome}: sem citação no texto={sorted(d - c)}"
          f" | citado sem seta na imagem={sorted(c - d)}")

ordem = list(citadas)
for i, nome in enumerate(ordem):
    for n in retro.get(nome, []):
        anterior = ordem[i - 1] if i else None
        if anterior and n in desenhadas.get(anterior, set()):
            print(f"ok    {nome}: cita a seta {n} de {anterior}")
        else:
            falhas += 1
            print(f"ERRO  {nome}: cita a seta {n} da imagem acima, que é {anterior} e tem"
                  f" {sorted(desenhadas.get(anterior, set()))}")

print(f"\nimagens: {len(desenhadas)} | setas: {sum(len(v) for v in desenhadas.values())}"
      f" | falhas: {falhas}")
sys.exit(1 if falhas else 0)
