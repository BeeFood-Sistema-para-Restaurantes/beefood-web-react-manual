#!/usr/bin/env python3
"""Captura o cardápio digital público com a nossa mídia dentro dele.

O problema: capa em vídeo, vitrine e avisos são recurso novo, e o cardápio
modelo (`menu.beefood.com.br/oneburger`) não tem nada disso configurado —
`bannersJson` e `avisosJson` vêm nulos. Configurar na loja de um cliente está
fora de questão, e desenhar a tela em CSS jogaria fora justamente o que o
slide precisa provar: que é o aplicativo de verdade que toca o vídeo.

A saída é a mesma do totem: **interceptar a resposta da API** e devolver a
configuração com a nossa mídia. Quem renderiza é o cardápio de produção — com o
layout, as cores, a fonte e os produtos reais da loja. Nada é gravado em lugar
nenhum: a injeção vive só dentro deste Chromium.

Duas interceptações:

1. `validaDelivery` — o corpo é uma string base64 de um JSON comprimido com
   zlib. Decodifica, escreve `bannersJson` e `avisosJson`, comprime de volta.
2. a mídia — as URLs injetadas apontam para um caminho de exemplo no host de
   imagens, e este script responde com o arquivo de `assets/midia/`. O MP4 pede
   faixa (`Range`), então a resposta sabe devolver 206; sem isso o Chromium não
   toca o vídeo e a captura sai preta.

Uso:
    python capturar-cardapio.py --saida carrosseis/<slug>/imagens-puras \\
        --conteudo carrosseis/<slug>/midias.json
    python capturar-cardapio.py --saida ... --limpo      # antes, sem mídia
    python capturar-cardapio.py --listar-tomadas

Entrada : --conteudo, um JSON com as mídias (ver `midias.json` do carrossel de
          capas e destaques) e --biblioteca, a pasta dos arquivos.
Saída   : PNG em --saida, um por tomada.
"""

from __future__ import annotations

import argparse
import base64
import json
import re
import sys
import zlib
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
RAIZ = SKILL.parents[2]
MIDIA = SKILL / "assets" / "midia"

URL_PADRAO = "https://menu.beefood.com.br/oneburger/"
# Caminho de exemplo no host de imagens do cardápio: não existe no servidor, é
# só um endereço estável para o interceptador reconhecer e responder com o
# arquivo local. Sai igual a uma URL de mídia de verdade dentro do aplicativo.
PASTA_FALSA = "exemplo-beefood-midia"

APARELHOS = {
    "pc": {"viewport": {"width": 1440, "height": 900}, "device_scale_factor": 2},
    "cel": {"viewport": {"width": 390, "height": 844}, "device_scale_factor": 3,
            "is_mobile": True, "has_touch": True},
}

TIPOS = {".mp4": "video/mp4", ".webm": "video/webm", ".jpg": "image/jpeg",
         ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp",
         ".gif": "image/gif"}

# Tomadas: aparelho, o que fazer antes do clique no disparador, e o recorte.
# `midia` é (qual carrossel, número da mídia) — 1 é sempre a capa fixa da loja.
TOMADAS: dict[str, dict] = {
    "pc-capa-imagem": {"aparelho": "pc", "midia": ("capa", 2),
                       "nota": "capa no banner de imagem, computador"},
    "pc-capa-video": {"aparelho": "pc", "midia": ("capa", 3), "video": 2.4,
                      "nota": "capa no vídeo, computador"},
    "pc-vitrine": {"aparelho": "pc", "midia": ("vitrine", 1), "video": 2.0,
                   "rolar": "vitrine",
                   "nota": "vitrine no vídeo, computador"},
    "pc-avisos": {"aparelho": "pc", "rolar": "avisos",
                  "nota": "fileira de avisos, computador"},
    "cel-capa-video": {"aparelho": "cel", "midia": ("capa", 3), "video": 2.4,
                       "nota": "capa no vídeo, celular"},
    "cel-vitrine": {"aparelho": "cel", "midia": ("vitrine", 1), "video": 2.0,
                    "rolar": "vitrine", "nota": "vitrine no vídeo, celular"},
    "cel-avisos": {"aparelho": "cel", "rolar": "avisos",
                   "nota": "fileira de avisos, celular"},
    "cel-aviso-aberto": {"aparelho": "cel", "rolar": "avisos", "abrir_aviso": True,
                         "nota": "aviso aberto, com título e descrição"},
    # Sem mídia nenhuma: é o "antes" do mesmo cardápio, para a comparação.
    "pc-capa-limpa": {"aparelho": "pc", "limpo": True,
                      "nota": "capa parada, sem banner (antes)"},
    "cel-capa-limpa": {"aparelho": "cel", "limpo": True,
                       "nota": "capa parada, sem banner (antes), celular"},
}


def endereco(arquivo: str) -> str:
    return (f"https://beetech-imagens.s3-sa-east-1.amazonaws.com/"
            f"{PASTA_FALSA}/{arquivo}")


def agenda() -> dict:
    """Agenda de mídia no ar todo dia, 24 h, nos dois canais.

    A novidade também vende agendamento, mas print de mídia fora do ar é print
    de tela vazia: o que entra na captura fica sempre ligado.
    """
    return {"dias": [1, 2, 3, 4, 5, 6, 7], "todoDia": True, "hIni": None,
            "hFim": None, "ctx": ["D", "P"], "on": True}


def montar_banners(conteudo: dict) -> str:
    grupos: dict[str, list] = {}
    for grupo in ("capas", "lojas"):
        itens = []
        for i, item in enumerate(conteudo.get(grupo, []), start=1):
            arquivo = item["arquivo"]
            itens.append({"id": f"{grupo[:1]}{i:07d}", "url": endereco(arquivo),
                          "tipo": "V" if arquivo.endswith((".mp4", ".webm")) else "I",
                          "ordem": i, **agenda()})
        grupos[grupo] = itens
    return json.dumps({"v": 1, **grupos}, ensure_ascii=False)


def montar_avisos(conteudo: dict) -> str:
    itens = []
    for i, item in enumerate(conteudo.get("avisos", []), start=1):
        itens.append({"id": f"a{i:07d}", "url": endereco(item["arquivo"]),
                      "titulo": item["titulo"], "descricao": item["descricao"],
                      "ordem": i, **agenda()})
    return json.dumps({"v": 1, "avisos": itens}, ensure_ascii=False)


def remendar_config(corpo: str, banners: str | None, avisos: str | None) -> str:
    """Escreve `bannersJson`/`avisosJson` no corpo do `validaDelivery`.

    O corpo é uma string JSON com base64 de zlib. Mantém o mesmo embrulho: o
    aplicativo só sabe ler nesse formato.
    """
    b64 = json.loads(corpo)
    config = json.loads(zlib.decompress(base64.b64decode(b64)).decode("utf-8"))
    config["bannersJson"] = banners
    config["avisosJson"] = avisos
    cru = json.dumps(config, ensure_ascii=False).encode("utf-8")
    return json.dumps(base64.b64encode(zlib.compress(cru, 9)).decode("ascii"))


def responder_midia(rota, biblioteca: Path) -> None:
    """Devolve o arquivo local, com 206 quando o Chromium pede faixa.

    Vídeo em `<video>` não é baixado inteiro: o Chromium pede `Range`. Se a
    resposta ignorar isso e mandar 200 com tudo, o elemento fica sem duração e
    a captura sai num quadro preto.
    """
    nome = rota.request.url.rsplit("/", 1)[-1].split("?")[0]
    arquivo = biblioteca / nome
    if not arquivo.is_file():
        rota.fulfill(status=404, body=f"sem {nome}")
        return
    dados = arquivo.read_bytes()
    tipo = TIPOS.get(arquivo.suffix.lower(), "application/octet-stream")
    faixa = rota.request.headers.get("range")
    if faixa and (m := re.match(r"bytes=(\d+)-(\d*)", faixa)):
        ini = int(m.group(1))
        fim = int(m.group(2)) if m.group(2) else len(dados) - 1
        pedaco = dados[ini:fim + 1]
        rota.fulfill(status=206, body=pedaco, headers={
            "Content-Type": tipo,
            "Content-Length": str(len(pedaco)),
            "Content-Range": f"bytes {ini}-{fim}/{len(dados)}",
            "Accept-Ranges": "bytes",
            "Cache-Control": "no-store",
        })
        return
    rota.fulfill(status=200, body=dados, headers={
        "Content-Type": tipo,
        "Content-Length": str(len(dados)),
        "Accept-Ranges": "bytes",
        "Cache-Control": "no-store",
    })


def limpar(pagina) -> None:
    """Fecha a faixa verde de cupom, que não é assunto de nenhum slide.

    Pelo texto da faixa e não pela posição: no topo da página moram o logotipo
    e a busca, e clicar no botão errado leva a captura para outra tela. A
    memória dos manuais registra esta faixa como a que não fechou por seletor.
    """
    pagina.evaluate("""() => {
        const faixa = document.querySelector('.promo-banner')
            || [...document.querySelectorAll('div')].find(e =>
                /cupom/i.test(e.textContent || '') && e.clientHeight < 90
                && e.getBoundingClientRect().top < 60 && e.querySelector('.mdi-close'));
        if (!faixa) return;
        const x = faixa.querySelector('.mdi-close, button');
        (x?.closest('button') || x)?.click();
    }""")
    pagina.wait_for_timeout(700)


def carrosseis(pagina) -> list:
    """Os `.midia-carrossel` da página, de cima para baixo: capa e vitrine."""
    return pagina.evaluate("""() => [...document.querySelectorAll('.midia-carrossel')]
        .map((c, i) => ({i, y: Math.round(c.getBoundingClientRect().top + scrollY)}))
        .sort((a, b) => a.y - b.y)""")


def ir_para_midia(pagina, qual: str, numero: int) -> None:
    """Clica no ponto da mídia pedida, no carrossel da capa ou da vitrine.

    Pelo ponto, e não pela seta: o ponto tem `aria-label` com o número, então a
    tomada não depende de quantas vezes a seta foi clicada nem de o carrossel
    ter girado sozinho no meio do caminho.
    """
    indice = 0 if qual == "capa" else 1
    pagina.evaluate("""([indice, numero]) => {
        const cs = [...document.querySelectorAll('.midia-carrossel')]
            .sort((a, b) => a.getBoundingClientRect().top - b.getBoundingClientRect().top);
        const c = cs[indice];
        if (!c) return;
        const pontos = [...c.querySelectorAll('.midia-carrossel__ponto')];
        const alvo = pontos.find(p =>
            (p.getAttribute('aria-label') || '').startsWith(`Ir para a mídia ${numero} `));
        (alvo || pontos[numero - 1])?.click();
    }""", [indice, numero])
    pagina.wait_for_timeout(1400)


def congelar_video(pagina, segundo: float) -> None:
    """Pausa o vídeo num segundo fixo, para a captura não sair sempre diferente."""
    pagina.evaluate("""async (segundo) => {
        const vs = [...document.querySelectorAll('video')];
        for (const v of vs) {
            v.pause();
            if (Number.isFinite(v.duration) && v.duration > 0) {
                v.currentTime = Math.min(segundo, v.duration - 0.1);
                await new Promise(ok => {
                    if (v.readyState >= 2 && Math.abs(v.currentTime - segundo) < 0.3) return ok();
                    v.addEventListener('seeked', ok, {once: true});
                    setTimeout(ok, 2500);
                });
            }
        }
    }""", segundo)
    pagina.wait_for_timeout(500)


def rolar_para(pagina, alvo: str) -> None:
    seletor = {"vitrine": ".midia-carrossel", "avisos": ".aviso-card"}[alvo]
    pagina.evaluate("""(seletor) => {
        const es = [...document.querySelectorAll(seletor)];
        const e = seletor === '.midia-carrossel' ? es[es.length - 1] : es[0];
        if (!e) return;
        const c = e.getBoundingClientRect();
        // Um respiro acima do elemento: encostar o banner no topo da tela deixa
        // a captura sem contexto nenhum do cardápio em volta.
        scrollTo({top: c.top + scrollY - (innerHeight * 0.22), behavior: 'instant'});
    }""", seletor)
    pagina.wait_for_timeout(1200)


def abrir_aviso(pagina) -> None:
    pagina.evaluate("() => document.querySelector('.aviso-card')?.click()")
    pagina.wait_for_timeout(1200)


def capturar(args: argparse.Namespace, nomes: list[str]) -> None:
    from playwright.sync_api import sync_playwright

    saida = Path(args.saida)
    saida.mkdir(parents=True, exist_ok=True)
    biblioteca = Path(args.biblioteca)
    conteudo = json.loads(Path(args.conteudo).read_text(encoding="utf-8")) \
        if args.conteudo else {}
    banners = montar_banners(conteudo) if conteudo else None
    avisos = montar_avisos(conteudo) if conteudo else None

    with sync_playwright() as p:
        navegador = p.chromium.launch(args=["--autoplay-policy=no-user-gesture-required"])
        for nome in nomes:
            receita = TOMADAS[nome]
            limpo = receita.get("limpo") or args.limpo
            ctx = navegador.new_context(
                locale="pt-BR", timezone_id="America/Sao_Paulo",
                # O cardápio é PWA: sem bloquear o service worker, ele responde
                # do cache e a interceptação não vê a chamada da API.
                service_workers="block",
                **APARELHOS[receita["aparelho"]],
            )
            ctx.route(
                "**/validaDelivery**",
                lambda rota: rota.fulfill(
                    status=200,
                    content_type="application/json",
                    body=remendar_config(rota.fetch().text(),
                                         None if limpo else banners,
                                         None if limpo else avisos),
                ),
            )
            ctx.route(f"**/{PASTA_FALSA}/*",
                      lambda rota: responder_midia(rota, biblioteca))
            pagina = ctx.new_page()
            pagina.goto(args.url, wait_until="networkidle", timeout=120_000)
            pagina.wait_for_timeout(6000)
            limpar(pagina)

            if receita.get("rolar"):
                rolar_para(pagina, receita["rolar"])
            if receita.get("midia"):
                ir_para_midia(pagina, *receita["midia"])
            if receita.get("video") is not None:
                congelar_video(pagina, receita["video"])
            if receita.get("abrir_aviso"):
                abrir_aviso(pagina)

            destino = saida / f"{nome}.png"
            pagina.screenshot(path=str(destino), type="png")
            print(f"OK  {destino}  ({receita['nota']})")
            ctx.close()
        navegador.close()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--saida", help="pasta imagens-puras do carrossel")
    ap.add_argument("--conteudo", help="JSON com capas, lojas e avisos")
    ap.add_argument("--biblioteca", default=str(MIDIA),
                    help=f"pasta dos arquivos de mídia (padrão: {MIDIA})")
    ap.add_argument("--url", default=URL_PADRAO)
    ap.add_argument("--tomada", action="append", choices=sorted(TOMADAS),
                    help="só esta tomada (pode repetir)")
    ap.add_argument("--limpo", action="store_true",
                    help="captura sem injetar mídia nenhuma")
    ap.add_argument("--listar-tomadas", action="store_true")
    args = ap.parse_args()

    if args.listar_tomadas:
        for nome, receita in TOMADAS.items():
            print(f"{nome:20} {receita['aparelho']:4} {receita['nota']}")
        return 0

    if not args.saida:
        sys.exit("ERRO: --saida é obrigatório")
    if not args.conteudo and not args.limpo:
        sys.exit("ERRO: sem --conteudo só faz sentido com --limpo")

    capturar(args, args.tomada or list(TOMADAS))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
