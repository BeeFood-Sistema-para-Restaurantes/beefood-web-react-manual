"""Confere, neste manual, se o texto e as setas falam a mesma coisa.

Duas perguntas, que a revisão no olho erra com catorze imagens e 40 setas:

* toda seta **desenhada** pelo `annotate.py` é **citada** no `.md`?
* todo número **citado** no `.md` existe como seta **naquela** imagem?

A convenção da casa diz que o número aparece em duas posições, e só nessas: `(N)` no parágrafo
imediatamente **antes** da imagem, ou na tabela imediatamente **depois** dela.

Aqui apareceu um terceiro caso, que o #127 não tinha: o leitor vai e volta entre as duas pontas
da integração, e o texto precisa apontar para uma seta **de um passo anterior qualquer** — *"o
valor da seta 1 do Passo 5"*, *"a seta 3 do Passo 10"*. No #127 bastava *"da imagem acima"*,
porque a referência era sempre à imagem anterior. Essas citações são conferidas à parte, contra
a imagem do passo citado, e para isso o script mapeia cada imagem ao seu `### Passo N`.

Rodar dentro da pasta do manual:

    python3 conferir-setas.py

Sai com código 1 quando acha divergência. Ele é **deste manual**: lê os marcadores no formato
`(numero, alvo_x, alvo_y, etiqueta_x, etiqueta_y)` e as quatro funções de geometria do
`annotate.py` daqui (`annotate`, `painel`, `dialogo`, `faixa`, `lado`).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PASTA = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
APOIO = ("fluxo-codigo.md", "MEMORIA.md", "texto-documentation.ia.md")
GEOMETRIAS = ("annotate", "painel", "dialogo", "faixa", "lado")

manual = next(p for p in sorted(PASTA.glob("*.md")) if p.name not in APOIO)
texto = manual.read_text(encoding="utf-8")
script = (PASTA / "annotate.py").read_text(encoding="utf-8")

# --- o que o annotate.py desenha ---------------------------------------------------------
abre = "|".join(f"{g}\\(" for g in GEOMETRIAS)
desenhadas: dict[str, set[int]] = {}
for bloco in re.split(rf"\n(?={abre})", script):
    m = re.search(rf'^(?:{"|".join(GEOMETRIAS)})\(\s*\n?\s*"([^"]+)"', bloco)
    if not m:
        continue
    saida = re.search(r'saida="([^"]+)"', bloco)
    nome = saida.group(1) if saida else m.group(1)
    numeros = {int(n) for n in re.findall(r"\(\s*(\d+),\s*-?\d+,\s*-?\d+,", bloco)}
    if numeros:
        desenhadas[nome] = numeros

# --- de que passo é cada imagem ------------------------------------------------------------
passo_da_imagem: dict[str, int] = {}
imagens_do_passo: dict[int, list[str]] = {}
passo = 0
for linha in texto.splitlines():
    cab = re.match(r"###\s*Passo\s*(\d+)", linha)
    if cab:
        passo = int(cab.group(1))
    img = re.search(r"!\[[^\]]*\]\(imagens-tratadas/([^)]+)\)", linha)
    if img:
        passo_da_imagem[img.group(1)] = passo
        imagens_do_passo.setdefault(passo, []).append(img.group(1))

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

# --- as citações a setas de passos anteriores, onde quer que estejam -----------------------
retro = [(int(n), int(p)) for n, p in
         re.findall(r"setas? (\d+)(?: da imagem)? do Passo (\d+)", texto)]

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

for numero, destino in retro:
    alvos = imagens_do_passo.get(destino, [])
    achou = [a for a in alvos if numero in desenhadas.get(a, set())]
    if achou:
        print(f"ok    texto cita a seta {numero} do Passo {destino} ({achou[0]})")
    else:
        falhas += 1
        print(f"ERRO  texto cita a seta {numero} do Passo {destino}, e as imagens de lá"
              f" ({alvos or 'nenhuma'}) não têm essa seta")

print(f"\nimagens: {len(desenhadas)} | setas: {sum(len(v) for v in desenhadas.values())}"
      f" | falhas: {falhas}")
sys.exit(1 if falhas else 0)
