"""Anota os screenshots do manual BeeFood - Horario de atendimento (#32).

Mesmo estilo dos demais manuais: setas finas/sutis em VERDE + badges numerados.
Coordenadas em fracoes (0..1) da largura/altura da imagem.
Cada marcador: (numero, alvo_x, alvo_y, badge_x, badge_y)

Capturas do painel web em 2160x1350 (viewport 1440x900, DPR 1.5).

ATENCAO ao ambiente de captura: esta tela tem `input type="time"`, que o Chromium
renderiza em AM/PM quando o navegador esta em en-US. As capturas deste manual
foram feitas com a variavel de ambiente LANG=pt_BR.UTF-8 no processo do Chromium
- nem o `locale` do contexto nem o argumento `--lang` mudam o formato do campo.
Sem isso, as imagens mostram "02:30 AM" em vez de "02:30".

A tela nao tem modal centralizado na maior parte do tempo, entao os badges ficam
na area vazia ao lado do conteudo (a direita da lista, abaixo da timeline) ou na
faixa da sidebar. Nos modais do Assistente, na margem escura em volta.

Tres imagens de contexto (passthrough): as duas do estado desorganizado, que
abrem o manual, e a grade Presencial zerada - nelas o ponto e o conjunto.
Sem borrao: nenhuma captura tem dado de cliente.
"""
import os, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(OUT, exist_ok=True)

GREEN = (22, 150, 78)
WHITE = (255, 255, 255)
A_LINE = 220
A_BADGE = 235

FONT_CANDIDATES = [
    r"C:\Windows\Fonts\arialbd.ttf",
    "/usr/share/fonts/truetype/croscore/Arimo-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]


def font(sz):
    for caminho in FONT_CANDIDATES:
        if os.path.exists(caminho):
            return ImageFont.truetype(caminho, sz)
    raise RuntimeError("nenhuma fonte bold encontrada: " + ", ".join(FONT_CANDIDATES))


def draw_arrow(d, x0, y0, x1, y1, w):
    col = GREEN + (A_LINE,)
    d.line([(x0, y0), (x1, y1)], fill=col, width=w)
    ang = math.atan2(y1 - y0, x1 - x0)
    L = w * 3.6
    for s in (0.45, -0.45):
        xa = x1 - L * math.cos(ang - s)
        ya = y1 - L * math.sin(ang - s)
        d.line([(x1, y1), (xa, ya)], fill=col, width=w)


def badge(d, cx, cy, r, num, fnt):
    d.ellipse([cx - r - 2, cy - r - 2, cx + r + 2, cy + r + 2], fill=WHITE + (235,))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREEN + (A_BADGE,))
    t = str(num)
    bb = d.textbbox((0, 0), t, font=fnt)
    tw, th = bb[2] - bb[0], bb[3] - bb[1]
    d.text((cx - tw / 2 - bb[0], cy - th / 2 - bb[1]), t, fill=WHITE, font=fnt)


def passthrough(name):
    """Copia uma imagem de CONTEXTO (sem setas) para imagens-tratadas/."""
    img = Image.open(os.path.join(SRC, name)).convert("RGB")
    img.save(os.path.join(OUT, name))
    print("OK (contexto)", name)


def annotate(name, markers, ring=None, borrao=None, raio=0.0125, out_name=None):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    W, H = img.size

    for (fx, fy, fw, fh) in (borrao or []):
        caixa = (int(fx * W), int(fy * H), int((fx + fw) * W), int((fy + fh) * H))
        trecho = img.crop(caixa).filter(ImageFilter.GaussianBlur(radius=max(6, W // 140)))
        img.paste(trecho, caixa)

    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    r = int(W * raio)
    fnt = font(int(r * 1.2))
    w = max(2, int(W * 0.0022))
    for (fx, fy, fw, fh) in (ring or []):
        x0, y0 = fx * W, fy * H
        d.rectangle([x0, y0, x0 + fw * W, y0 + fh * H], outline=GREEN + (A_LINE,), width=w)
    for (num, tx, ty, bx, by) in markers:
        TX, TY = tx * W, ty * H
        BX, BY = bx * W, by * H
        ang = math.atan2(TY - BY, TX - BX)
        sx = BX + (r + 5) * math.cos(ang)
        sy = BY + (r + 5) * math.sin(ang)
        draw_arrow(d, sx, sy, TX, TY, w)
        badge(d, BX, BY, r, num, fnt)
    out_img = Image.alpha_composite(img, overlay).convert("RGB")
    out_img.save(os.path.join(OUT, out_name or name))
    print("OK", out_name or name)


# ---------- Parte 1: onde fica e as duas visoes ----------

# 01) Timeline: a semana inteira num relance (grade desorganizada, o "antes")
annotate("01-timeline-antes.png", [
    (1, 0.240, 0.093, 0.300, 0.230),   # sub-abas Delivery / Presencial
    (2, 0.860, 0.105, 0.880, 0.230),   # botoes Timeline / Lista
    (3, 0.757, 0.095, 0.700, 0.230),   # botao Assistente
])

# 02) A mesma grade na visao Lista (contexto: e o "antes" do manual)
passthrough("02-lista-antes.png")

# 03) A grade Presencial, que e independente (contexto)
passthrough("03-presencial-antes.png")

# ---------- Parte 2: comecar do zero ----------

# 04) O menu de tres pontos
annotate("04-menu-resetar.png", [
    (1, 0.932, 0.155, 0.870, 0.290),   # Resetar horarios
])

# 05) O aviso do reset
annotate("05-reset-confirmacao.png", [
    (1, 0.617, 0.545, 0.760, 0.620),   # OK! (ENTER)
])

# 06) A grade zerada depois do reset
annotate("06-apos-reset.png", [
    (1, 0.240, 0.290, 0.130, 0.420),   # todos os dias como Fechado
])

# ---------- Parte 3: o Assistente ----------

# 07) O aviso de que o Assistente substitui tudo
annotate("07-assistente-aviso.png", [
    (1, 0.617, 0.545, 0.760, 0.620),   # OK! (ENTER)
])

# 08) Passo 1: os dias
annotate("08-assistente-passo1.png", [
    (1, 0.492, 0.530, 0.250, 0.480),   # os botoes de dia (Dom desmarcado)
    (2, 0.430, 0.601, 0.250, 0.660),   # atalhos Todos / Dias uteis / Fim de semana
    (3, 0.618, 0.660, 0.790, 0.710),   # Avancar
])

# 09) Passo 2: o modelo pronto e os horarios
annotate("09-assistente-passo2.png", [
    (1, 0.418, 0.365, 0.230, 0.330),   # os quatro modelos prontos
    (2, 0.417, 0.570, 0.230, 0.620),   # Abertura e Fechamento
    (3, 0.344, 0.618, 0.230, 0.690),   # segundo turno
    (4, 0.417, 0.784, 0.230, 0.830),   # Tempo de entrega e de retirada
])

# 10) Passo 3: a revisao antes de aplicar
annotate("10-assistente-passo3.png", [
    (1, 0.500, 0.545, 0.250, 0.500),   # a semana como vai ficar
    (2, 0.418, 0.688, 0.250, 0.730),   # os tempos aplicados
    (3, 0.621, 0.731, 0.800, 0.780),   # Aplicar
])

# ---------- Parte 4: o resultado ----------

# 11) Timeline com os dois turnos por dia
annotate("11-timeline-depois.png", [
    (1, 0.473, 0.668, 0.300, 0.720),   # bloco do almoco
    (2, 0.473, 0.875, 0.300, 0.930),   # bloco do jantar
    (3, 0.898, 0.248, 0.960, 0.330),   # Domingo Fechada
])

# 12) A mesma coisa na Lista, com o segundo turno e o botao de remover
annotate("12-lista-dois-turnos.png", [
    (1, 0.330, 0.348, 0.180, 0.300),   # primeiro turno
    (2, 0.330, 0.393, 0.180, 0.440),   # segundo turno
    (3, 0.477, 0.393, 0.560, 0.440),   # remover o segundo turno
    (4, 0.640, 0.348, 0.700, 0.290),   # tempo de entrega e de retirada
])

# 13) O resumo de horas da semana
annotate("13-resumo-desempenho.png", [
    (1, 0.300, 0.420, 0.180, 0.520),   # horas totais e por faixa
])

# ---------- Parte 5: ajustar na mao ----------

# 14) O popover de um bloco na timeline
annotate("14-popover-bloco.png", [
    (1, 0.404, 0.797, 0.250, 0.760),   # Inicio e Fim
    (2, 0.404, 0.878, 0.250, 0.920),   # Entrega e Retirada
    (3, 0.581, 0.941, 0.700, 0.900),   # Aplicar
])

# ---------- Parte 6: quem fecha depois da meia-noite ----------

# 15) O aviso do turno dividido
annotate("15-meia-noite-toast.png", [
    (1, 0.890, 0.075, 0.740, 0.160),   # aviso "Turno dividido"
    (2, 0.421, 0.980, 0.560, 0.930),   # o campo virou 23:59
])

# 16) Dia fechado e o turno da madrugada no dia seguinte
annotate("16-dia-fechado.png", [
    (1, 0.262, 0.254, 0.140, 0.300),   # switch desligado = Fechado
    (2, 0.330, 0.810, 0.180, 0.870),   # o turno 00:00 - 02:00 no domingo
])

# ---------- Parte 7: o que o sistema recusa ----------

# 17) Inicio igual ao fim nao salva
annotate("17-validacao-igual.png", [
    (1, 0.890, 0.075, 0.700, 0.170),   # a mensagem de erro
    (2, 0.328, 0.121, 0.180, 0.180),   # o campo com inicio igual ao fim
])

# ---------- Parte 8: a grade Presencial ----------

# 18) Depois do reset, o Presencial tambem ficou fechado (contexto)
passthrough("18-presencial-fechado.png")

# 19) O Assistente no Presencial nao pede tempo de entrega
annotate("19-presencial-passo2.png", [
    (1, 0.470, 0.174, 0.250, 0.130),   # "horarios de Presencial"
    (2, 0.417, 0.737, 0.250, 0.800),   # aqui termina: nao ha tempo de entrega
])

# 20) A grade Presencial configurada
annotate("20-presencial-configurado.png", [
    (1, 0.328, 0.145, 0.250, 0.230),   # sub-aba Presencial ativa
])

print("done")
