#!/usr/bin/env python3
"""
"Intense" carousel theme for @civic.sense.india — 1080x1350, dark, high contrast.

Replaces the paper/teal look. Near-black with film grain and vignette,
saffron for India, crimson for the comparison country, white Anton headlines.

Each slide is a list of blocks rendered top-down; see SLIDES in a post file.
"""
import os
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1080, 1350
MARGIN = 84

BG = (17, 16, 16)
BG2 = (28, 26, 25)
WHITE = (248, 244, 238)
GREY = (196, 188, 178)
DIM = (128, 120, 112)
SAFFRON = (255, 122, 26)     # India
CRIMSON = (226, 48, 58)      # comparison country
GOLD = (255, 196, 46)        # highlights

FDIR = os.environ.get("CIVIC_FONTS") or "/home/claude/fonts"
ANTON = os.path.join(FDIR, "Anton-Regular.ttf")
BOLD = os.path.join(FDIR, "BarlowCondensed-Bold.ttf")
SEMI = os.path.join(FDIR, "BarlowCondensed-SemiBold.ttf")
MED = os.path.join(FDIR, "BarlowCondensed-Medium.ttf")

HANDLE = "@civic.sense.india"


def font(path, size):
    return ImageFont.truetype(path, size)


def tw(draw, text, f):
    b = draw.textbbox((0, 0), text, font=f)
    return b[2] - b[0], b[3] - b[1], b[0], b[1]


def fit(draw, text, path, max_w, start, floor=40):
    s = start
    while s > floor:
        f = font(path, s)
        if tw(draw, text, f)[0] <= max_w:
            return f
        s -= 2
    return font(path, floor)


def wrap(draw, text, f, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if tw(draw, t, f)[0] <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def base():
    im = Image.new("RGB", (W, H), BG)
    # vertical warm gradient
    top = Image.new("RGB", (W, H), BG2)
    mask = Image.linear_gradient("L").resize((W, H)).point(lambda v: int(v * 0.55))
    im = Image.composite(im, top, mask)  # lighter at the top, darker below
    # vignette
    vig = Image.new("L", (W, H), 0)
    vd = ImageDraw.Draw(vig)
    vd.ellipse([-W * 0.35, -H * 0.25, W * 1.35, H * 1.25], fill=255)
    vig = vig.filter(ImageFilter.GaussianBlur(160))
    dark = Image.new("RGB", (W, H), (6, 6, 6))
    im = Image.composite(im, dark, vig)
    # film grain
    rnd = random.Random(7)
    noise = Image.effect_noise((W, H), 22).convert("L")
    grain = Image.merge("RGB", (noise, noise, noise))
    im = Image.blend(im, grain, 0.055)
    return im


def chip(d, x, y, text, fill, fg=BG, size=38):
    f = font(BOLD, size)
    w, h, ox, oy = tw(d, text, f)
    px, py = 22, 12
    d.rounded_rectangle([x, y, x + w + 2 * px, y + h + 2 * py], radius=8, fill=fill)
    d.text((x + px - ox, y + py - oy), text, font=f, fill=fg)
    return x + w + 2 * px, y + h + 2 * py


def wordmark(d):
    """Brand lockup, top right of every slide: saffron bar + CIVIC SENSE INDIA."""
    f1 = font(ANTON, 30)
    f2 = font(ANTON, 30)
    t1, t2 = "CIVIC SENSE ", "INDIA"
    w1, h1, ox1, oy1 = tw(d, t1, f1)
    w2, h2, ox2, oy2 = tw(d, t2, f2)
    x = W - MARGIN - w1 - w2
    y = 52
    d.rectangle([x - 22, y + 2, x - 12, y + h1 + 2], fill=SAFFRON)
    d.text((x - ox1, y - oy1), t1, font=f1, fill=WHITE)
    d.text((x + w1 - ox2, y - oy2), t2, font=f2, fill=SAFFRON)


def footer(d, n, total):
    wordmark(d)
    f = font(BOLD, 38)
    w, h, ox, oy = tw(d, HANDLE, f)
    d.text((MARGIN - ox, H - 96 - oy), HANDLE, font=f, fill=WHITE)
    d.rectangle([MARGIN, H - 96 + h + 10, MARGIN + w, H - 96 + h + 14], fill=SAFFRON)
    f2 = font(SEMI, 34)
    label = f"{n}/{total}"
    w, h, ox, oy = tw(d, label, f2)
    d.text((W - MARGIN - w - ox, H - 94 - oy), label, font=f2, fill=DIM)


def rule(d, x, y, w, col, h=10):
    d.rectangle([x, y, x + w, y + h], fill=col)


def headline_stack(d, y, lines, max_w=None, start=170, gap=18):
    """lines: list of (text, colour). Each line auto-fits to the width."""
    max_w = max_w or (W - 2 * MARGIN)
    for text, col in lines:
        f = fit(d, text, ANTON, max_w, start)
        w, h, ox, oy = tw(d, text, f)
        d.text((MARGIN - ox, y - oy), text, font=f, fill=col)
        y += h + gap
    return y


def body(d, y, text, col=GREY, size=50, max_w=None, gap=14, path=MED):
    max_w = max_w or (W - 2 * MARGIN)
    f = font(path, size)
    for ln in wrap(d, text, f, max_w):
        w, h, ox, oy = tw(d, ln, f)
        d.text((MARGIN - ox, y - oy), ln, font=f, fill=col)
        y += int(size * 1.18) + gap - 14
    return y


def swipe(d, text="SWIPE"):
    # Barlow has no arrow glyph, so the arrow is drawn.
    f = font(BOLD, 42)
    w, h, ox, oy = tw(d, text, f)
    aw, gap = 46, 18
    x = W - MARGIN - aw - gap - w
    y = H - 172
    d.text((x - ox, y - oy), text, font=f, fill=GOLD)
    ax, ay = W - MARGIN - aw, y + h // 2
    d.rectangle([ax, ay - 4, ax + aw - 16, ay + 4], fill=GOLD)
    d.polygon([(ax + aw - 22, ay - 16), (ax + aw, ay), (ax + aw - 22, ay + 16)], fill=GOLD)


def versus(d, y, left, right, h=520):
    """Two panels side by side. left/right: (label, colour, lines[])."""
    gap = 64
    pw = (W - 2 * MARGIN - gap) // 2
    label_mid = y
    for i, (label, col, lines) in enumerate((left, right)):
        x = MARGIN + i * (pw + gap)
        d.rounded_rectangle([x, y, x + pw, y + h], radius=18, fill=(34, 32, 30))
        d.rectangle([x, y, x + pw, y + 12], fill=col)
        f = fit(d, label, ANTON, pw - 60, 96)
        w, hh, ox, oy = tw(d, label, f)
        d.text((x + 30 - ox, y + 50 - oy), label, font=f, fill=col)
        label_mid = y + 50 + hh // 2
        yy = y + 50 + hh + 44
        bf = font(SEMI, 52)
        for line in lines:
            for ln in wrap(d, line, bf, pw - 60):
                w2, h2, ox2, oy2 = tw(d, ln, bf)
                d.text((x + 30 - ox2, yy - oy2), ln, font=bf, fill=WHITE)
                yy += 62
            yy += 22
    # VS badge sits in the gutter, level with the labels, clear of the text.
    vf = font(ANTON, 50)
    t = "VS"
    w, hh, ox, oy = tw(d, t, vf)
    cx, cy = W // 2, label_mid
    r = 46
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GOLD)
    d.text((cx - w // 2 - ox, cy - hh // 2 - oy), t, font=vf, fill=BG)
    return y + h
