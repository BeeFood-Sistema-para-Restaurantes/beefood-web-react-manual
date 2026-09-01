"""Anota os screenshots do manual "Criar usuario e montar grupo de acesso".

Mesmo estilo dos demais manuais: setas finas em VERDE + badges numerados.
Coordenadas em fracoes (0..1) da largura/altura da imagem.
Cada marcador: (numero, alvo_x, alvo_y, badge_x, badge_y)

A funcao `comparar` (copiada do manual #72) recorta a MESMA regiao de duas
capturas e monta as duas lado a lado, com titulo — e o manual usa isso para
mostrar o menu de quem tem grupo x de quem nao tem.
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

SRC = "imagens-puras"
OUT = "imagens-tratadas"
os.makedirs(OUT, exist_ok=True)

GREEN = (22, 150, 78)
WHITE = (255, 255, 255)
CINZA = (244, 244, 245)
TEXTO = (40, 40, 45)
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
        d.line([(x1, y1), (x1 - L * math.cos(ang - s), y1 - L * math.sin(ang - s))],
               fill=col, width=w)


def badge(d, cx, cy, r, num, fnt):
    d.ellipse([cx - r - 2, cy - r - 2, cx + r + 2, cy + r + 2], fill=WHITE + (235,))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREEN + (A_BADGE,))
    t = str(num)
    bb = d.textbbox((0, 0), t, font=fnt)
    d.text((cx - (bb[2] - bb[0]) / 2 - bb[0], cy - (bb[3] - bb[1]) / 2 - bb[1]),
           t, fill=WHITE, font=fnt)


def _marcar(img, markers, ring=None):
    W, H = img.size
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    r = int(W * 0.0125)
    fnt = font(int(r * 1.2))
    w = max(2, int(W * 0.0022))
    for (fx, fy, fw, fh) in (ring or []):
        x0, y0 = fx * W, fy * H
        d.rectangle([x0, y0, x0 + fw * W, y0 + fh * H], outline=GREEN + (A_LINE,), width=w)
    for (num, tx, ty, bx, by) in markers:
        TX, TY, BX, BY = tx * W, ty * H, bx * W, by * H
        ang = math.atan2(TY - BY, TX - BX)
        draw_arrow(d, BX + (r + 5) * math.cos(ang), BY + (r + 5) * math.sin(ang), TX, TY, w)
        badge(d, BX, BY, r, num, fnt)
    return Image.alpha_composite(img, overlay).convert("RGB")


def passthrough(name, saida=None):
    img = Image.open(os.path.join(SRC, name)).convert("RGB")
    img.save(os.path.join(OUT, saida or name))
    print("OK (contexto)", saida or name)


def annotate(name, markers, ring=None, saida=None, crop=None):
    img = Image.open(os.path.join(SRC, name)).convert("RGBA")
    if crop:
        W, H = img.size
        fx, fy, fw, fh = crop
        img = img.crop((int(fx * W), int(fy * H), int((fx + fw) * W), int((fy + fh) * H)))
    _marcar(img, markers, ring).save(os.path.join(OUT, saida or name))
    print("OK", saida or name)


def comparar(saida, painel_esq, painel_dir, crop, markers_esq=None, markers_dir=None,
             ring_esq=None, ring_dir=None, largura=760):
    GAP, PAD, CAP_H = 18, 22, 46
    partes = []
    for arq, titulo, mk, rg in ((painel_esq[0], painel_esq[1], markers_esq, ring_esq),
                                (painel_dir[0], painel_dir[1], markers_dir, ring_dir)):
        img = Image.open(os.path.join(SRC, arq)).convert("RGBA")
        W, H = img.size
        fx, fy, fw, fh = crop
        img = img.crop((int(fx * W), int(fy * H), int((fx + fw) * W), int((fy + fh) * H)))
        img = _marcar(img, mk or [], rg).convert("RGBA")
        esc = largura / img.size[0]
        img = img.resize((largura, int(img.size[1] * esc)), Image.LANCZOS)
        partes.append((img, titulo))

    alt = max(p[0].size[1] for p in partes)
    canvas = Image.new("RGB", (PAD * 2 + largura * 2 + GAP, PAD * 2 + CAP_H + alt), CINZA)
    d = ImageDraw.Draw(canvas)
    fnt = font(24)
    for i, (img, titulo) in enumerate(partes):
        x = PAD + i * (largura + GAP)
        bb = d.textbbox((0, 0), titulo, font=fnt)
        d.text((x + (largura - (bb[2] - bb[0])) / 2, PAD + (CAP_H - (bb[3] - bb[1])) / 2 - bb[1]),
               titulo, fill=TEXTO, font=fnt)
        canvas.paste(img.convert("RGB"), (x, PAD + CAP_H))
        d.rectangle([x, PAD + CAP_H, x + largura - 1, PAD + CAP_H + img.size[1] - 1],
                    outline=(210, 210, 214), width=1)
    canvas.save(os.path.join(OUT, saida))
    print("OK (comparativo)", saida)


# =====================================================================
# A tela de usuarios
# =====================================================================

annotate("01-aba-usuarios-limite-do-plano.png", [
    (1, 0.290, 0.180, 0.255, 0.470),   # Novo Usuario (F1)
    (2, 0.858, 0.132, 0.700, 0.072),   # contador do plano
    (3, 0.665, 0.240, 0.620, 0.470),   # coluna Funcao
    (4, 0.800, 0.240, 0.790, 0.470),   # coluna Grupo de Acesso
    (5, 0.898, 0.290, 0.945, 0.400),   # icones de senha e edicao
])

# =====================================================================
# Passo 1 — criar o grupo
# =====================================================================

annotate("05-modal-novo-grupo-vazio.png", [
    (1, 0.400, 0.262, 0.180, 0.230),   # campo do nome do grupo
    (2, 0.660, 0.360, 0.830, 0.330),   # aviso de que as permissoes vem depois
])

annotate("07-grupo-novo-permissoes-iniciais.png", [
    (1, 0.400, 0.253, 0.180, 0.210),   # nome do grupo salvo
    (2, 0.712, 0.443, 0.860, 0.420),   # todos os switches ligados
    (3, 0.712, 0.535, 0.870, 0.560),
])

# =====================================================================
# Passo 2 — criar o usuario
# =====================================================================

annotate("02-modal-novo-usuario-vazio.png", [
    (1, 0.288, 0.315, 0.180, 0.290),   # Login
    (2, 0.288, 0.418, 0.180, 0.400),   # Senha
    (3, 0.722, 0.418, 0.840, 0.395),   # olho da senha
    (4, 0.288, 0.522, 0.180, 0.520),   # Funcionario
    (5, 0.288, 0.623, 0.180, 0.640),   # Grupo de Acesso
    (6, 0.722, 0.700, 0.830, 0.680),   # switches
    (7, 0.720, 0.800, 0.840, 0.820),   # SALVAR (F2)
])

annotate("10-escolher-grupo-de-acesso.png", [
    (1, 0.288, 0.593, 0.180, 0.560),   # Grupo de Acesso
    (2, 0.320, 0.658, 0.180, 0.700),   # a opcao Nenhum, marcada
    (3, 0.340, 0.700, 0.820, 0.720),   # os grupos da empresa
])

# =====================================================================
# Senha e usuario principal
# =====================================================================

annotate("13-modal-alterar-senha.png", [
    (1, 0.320, 0.400, 0.180, 0.370),   # Nova Senha
    (2, 0.320, 0.500, 0.180, 0.530),   # Confirmar Senha
])

annotate("14-usuario-principal-login-bloqueado.png", [
    (1, 0.320, 0.270, 0.180, 0.230),   # aviso Usuario principal
    (2, 0.288, 0.390, 0.180, 0.420),   # Login travado
    (3, 0.330, 0.763, 0.180, 0.800),   # ALTERAR SENHA continua disponivel
])

# Usuario desativado: badge Inativo e o contador do plano, que nao muda
annotate("17-usuario-inativo-na-lista.png", [
    (1, 0.508, 0.456, 0.450, 0.560),   # badge Inativo
    (2, 0.858, 0.132, 0.700, 0.072),   # contador continua o mesmo
])

# =====================================================================
# O comparativo: com grupo x sem grupo
# =====================================================================

comparar(
    "15-comparativo-com-e-sem-grupo.png",
    ("09-menu-usuario-com-grupo.png", "Com grupo restrito"),
    ("08-menu-usuario-sem-grupo.png", "Grupo de Acesso: Nenhum"),
    crop=(0.0, 0.125, 0.145, 0.70),
    largura=420,
)

print("done")
