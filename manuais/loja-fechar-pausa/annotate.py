"""Anota os screenshots do manual BeeFood - Fechar a loja fora do horario (#33).

Mesmo estilo dos demais manuais: setas finas/sutis em VERDE + badges numerados.
Coordenadas em fracoes (0..1) da largura/altura da imagem.
Cada marcador: (numero, alvo_x, alvo_y, badge_x, badge_y)

Capturas do painel web em 2160x1350 (viewport 1440x900, DPR 1.5), com
LANG=pt_BR.UTF-8 no processo do Chromium para os campos de data e hora sairem no
formato brasileiro (ver o annotate.py do manual de horario).

Duas telas deste manual sao popovers ancorados no topo da pagina (o menu de
cardapios e o submenu de pausa), entao os badges ficam a direita deles, sobre a
area do preview - que nao e o assunto.

Uma imagem de contexto (passthrough): a pausa desativada, onde o ponto e o
switch cinza no meio da lista.
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


# ---------- Parte 1: o atalho do topo ----------

# 01) O menu de cardapios, com o status e os switches de canal
annotate("01-header-popover.png", [
    (1, 0.222, 0.024, 0.400, 0.024),   # nome do cardapio no topo abre o menu
    (2, 0.240, 0.130, 0.420, 0.130),   # Pausa Temporaria
    (3, 0.283, 0.192, 0.430, 0.192),   # badge do status do canal
    (4, 0.330, 0.248, 0.470, 0.290),   # switches Entrega / Retirada / Consumo Local
])

# 02) O submenu com as pausas rapidas
annotate("02-pausa-temporaria-menu.png", [
    (1, 0.430, 0.130, 0.620, 0.100),   # Pausas ativas
    (2, 0.410, 0.190, 0.620, 0.190),   # Pausar por 15 / 30 / 45 minutos
    (3, 0.400, 0.378, 0.620, 0.378),   # Pausar por hoje
])

# ---------- Parte 2: pausa com data marcada ----------

# 03) A aba Pausa Programada
annotate("03-pausa-aba.png", [
    (1, 0.348, 0.141, 0.520, 0.100),   # Adicionar Pausa Programada
    (2, 0.295, 0.290, 0.180, 0.380),   # switch Ativo de uma pausa antiga
    (3, 0.470, 0.290, 0.560, 0.380),   # periodo e motivo
])

# 04) O modal, ainda em branco
annotate("04-pausa-modal.png", [
    (1, 0.405, 0.220, 0.240, 0.180),   # presets de duracao
    (2, 0.405, 0.343, 0.240, 0.310),   # HOJE e AMANHA
    (3, 0.458, 0.438, 0.240, 0.470),   # Inicio e Fim
    (4, 0.399, 0.673, 0.240, 0.700),   # switches de canal
    (5, 0.500, 0.757, 0.240, 0.790),   # Motivo
])

# 05) Preset de 30 minutos aplicado
annotate("05-pausa-preenchida.png", [
    (1, 0.500, 0.220, 0.760, 0.180),   # 30 MINUTOS selecionado
    (2, 0.458, 0.438, 0.760, 0.440),   # Inicio e Fim preenchidos sozinhos
    (3, 0.566, 0.829, 0.760, 0.870),   # CONFIRMAR PAUSA (F2)
])

# 06) A confirmacao, com a duracao
annotate("06-pausa-confirmacao.png", [
    (1, 0.430, 0.480, 0.240, 0.440),   # duracao, inicio e fim
    (2, 0.596, 0.565, 0.780, 0.610),   # CONFIRMAR (ENTER)
])

# 07) A pausa criada e valendo
annotate("07-pausa-criada.png", [
    (1, 0.295, 0.288, 0.180, 0.380),   # switch Ativo ligado
    (2, 0.345, 0.288, 0.420, 0.380),   # canais afetados
    (3, 0.470, 0.288, 0.560, 0.380),   # periodo da pausa
])

# 08) Desligar o switch encerra a pausa (contexto)
passthrough("08-pausa-desativada.png")

# ---------- Parte 3: desligar o canal por tempo indeterminado ----------

# 09) Os switches da aba Configuracoes
annotate("09-configuracoes-switches.png", [
    (1, 0.663, 0.549, 0.520, 0.500),   # Delivery Ativo
    (2, 0.330, 0.782, 0.200, 0.840),   # Entrega / Retirada / Consumo no Local
])

# ---------- Parte 4: continuar vendendo com a loja fechada ----------

# 10) A aba Agendamento
annotate("10-agendamento.png", [
    (1, 0.838, 0.348, 0.700, 0.300),   # Agendamento
    (2, 0.838, 0.454, 0.700, 0.520),   # Agendamento com o Cardapio Digital fechado
    (3, 0.838, 0.561, 0.700, 0.620),   # So aceita agendamento
])

print("done")
