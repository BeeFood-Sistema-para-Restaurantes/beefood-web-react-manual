"""Anota os screenshots do manual BeeFood - Modo Kiosk (Cardapio Digital Tablet).
Mesmo estilo dos demais manuais: setas finas/sutis em VERDE + badges numerados.
Coordenadas em fracoes (0..1) da largura/altura da imagem.
Cada marcador: (numero, alvo_x, alvo_y, badge_x, badge_y)
- alvo = ponta da seta (campo/botao)
- badge = posicao do circulo numerado (origem da seta)

As capturas sao do aplicativo Android num tablet, em 2560x1600. Quase toda tela
do app e um dialogo centralizado com o cardapio escurecido em volta, entao os
badges ficam nessa margem escura e as setas entram no dialogo. Nas telas de
Configuracoes do Android, que tem fundo claro, o badge vai no espaco vazio da
propria lista.

As duas telas sem seta usam passthrough(): a que mostra o cardapio intacto
depois do teste da trava (o ponto e justamente nada ter mudado) e a que mostra o
painel de volta ao estado destravado.

Nada de borrao aqui: a unica tela com dado identificavel era o login, que saiu do
manual junto com a Parte 1.
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


def annotate(name, markers, ring=None, borrao=None, raio=0.0125):
    """ring   = retangulos (x, y, largura, altura) em fracoes, para cercar uma area.
    borrao = retangulos (x, y, largura, altura) em fracoes, para tornar dados
             pessoais ilegiveis. Aplicado ANTES das setas."""
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
    out_img.save(os.path.join(OUT, name))
    print("OK", name)


# ---------- Parte 1: abrir a tela de Administracao ----------

# 03) O logo e a unica porta de entrada da Administracao
annotate("03-home-logo.png", [
    (1, 0.043, 0.037, 0.135, 0.115),   # logo do estabelecimento
])

# 04) Senha da Administracao (a mesma do login)
annotate("04-senha-administracao.png", [
    (1, 0.445, 0.163, 0.235, 0.130),   # campo Senha (a direita do rotulo)
    (2, 0.430, 0.232, 0.235, 0.260),   # ACESSAR
])

# 05) Os dois botoes que interessam no painel
annotate("05-painel-administracao.png", [
    (1, 0.645, 0.393, 0.785, 0.340),   # TRAVAR
    (2, 0.645, 0.457, 0.800, 0.510),   # CONFIGURAR TRAVA AVANCADA
])

# ---------- Parte 2: conceder as duas permissoes ----------

# 06) Assistente com as duas permissoes pendentes
# As setas dos CONCEDER miram a BORDA INFERIOR do botao, nao o meio: a ponta no
# meio cobria a palavra "CONCEDER".
annotate("06-assistente-inicio.png", [
    (1, 0.505, 0.295, 0.505, 0.185),   # contador "0 de 2 permissoes concedidas"
    (2, 0.220, 0.658, 0.220, 0.830),   # CONCEDER da Acessibilidade
    (3, 0.780, 0.658, 0.780, 0.830),   # CONCEDER do Launcher padrao
    (4, 0.170, 0.712, 0.075, 0.790),   # observacao sobre Volume e Power
])

# 07) Consentimento do servico de acessibilidade
annotate("07-aviso-acessibilidade.png", [
    (1, 0.775, 0.822, 0.870, 0.870),   # CONCORDAR E CONTINUAR
    (2, 0.250, 0.822, 0.140, 0.870),   # AGORA NAO
])

# 08) Lista de Acessibilidade do Android
annotate("08-android-acessibilidade.png", [
    (1, 0.700, 0.235, 0.800, 0.325),   # servico em "Apps baixados"
])

# 09) Chave do servico ainda desativada
annotate("09-android-servico-kiosk.png", [
    (1, 0.930, 0.330, 0.820, 0.440),   # chave "Usar ... Modo Kiosk"
])

# 10) Confirmacao do Android
annotate("10-android-confirmar-servico.png", [
    (1, 0.555, 0.692, 0.760, 0.620),   # Permitir
])

# 11) Chave azul: servico ativo
annotate("11-android-servico-ativo.png", [
    (1, 0.930, 0.330, 0.820, 0.440),   # chave ligada
])

# 12) Assistente reconhecendo a primeira permissao
annotate("12-assistente-1de2.png", [
    (1, 0.505, 0.295, 0.505, 0.185),   # contador "1 de 2"
    (2, 0.295, 0.571, 0.065, 0.600),   # selo "concedida" na Acessibilidade
    (3, 0.780, 0.658, 0.780, 0.830),   # CONCEDER do Launcher padrao
])

# 13) Android perguntando qual sera a tela inicial
annotate("13-android-launcher.png", [
    (1, 0.683, 0.488, 0.820, 0.440),   # opcao Cardapio Mesa/Comanda, desmarcada
])

# 14) Opcao marcada e confirmacao
annotate("14-android-launcher-selecionado.png", [
    (1, 0.683, 0.487, 0.820, 0.430),   # opcao marcada
    (2, 0.665, 0.657, 0.800, 0.730),   # Definir como padrao
])

# ---------- Parte 3: ativar a trava ----------

# 15) Assistente pronto
annotate("15-assistente-pronto.png", [
    (1, 0.505, 0.310, 0.505, 0.205),   # contador "2 de 2"
    (2, 0.673, 0.700, 0.750, 0.830),   # ATIVAR MODO KIOSK
])

# 16) Confirmacao do app e aviso do Android atras
annotate("16-kiosk-ativado.png", [
    (1, 0.700, 0.562, 0.830, 0.490),   # OK do aviso do aplicativo
    (2, 0.375, 0.790, 0.200, 0.720),   # painel "O app esta fixado", do Android
])

# 17) O aviso rapido do Android
annotate("17-app-fixado.png", [
    (1, 0.470, 0.895, 0.330, 0.840),   # aviso "App fixado"
])

# ---------- Parte 4: conferir se travou ----------

# 19) O cardapio segue na tela: nada a apontar, a prova e a tela inteira
passthrough("19-home-travada.png")

# ---------- Parte 5: destravar ----------

# 18) Com o tablet travado, TRAVAR da lugar a DESTRAVAR
annotate("18-painel-destravar.png", [
    (1, 0.645, 0.425, 0.790, 0.370),   # DESTRAVAR
])

# 20) Painel de volta ao estado destravado (contexto)
passthrough("20-destravado.png")

# ---------- Alternativa: trava basica ----------

# 21) A saida sem permissao, e o aviso de que ela e mais fraca
annotate("21-trava-basica.png", [
    (1, 0.170, 0.702, 0.060, 0.650),   # borda do aviso laranja com a limitacao
    (2, 0.505, 0.790, 0.505, 0.890),   # PULAR E USAR TRAVA BASICA AGORA
])

print("done")
