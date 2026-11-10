#!/usr/bin/env python3
"""India vs Japan: dustbins. Text slides 1,3,4,5,6. Slide 2 is an AI photo
hosted by HeyGen and added to the Buffer post directly."""
import os
import sys
from PIL import ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from intense import *  # noqa

OUT = sys.argv[1] if len(sys.argv) > 1 else "out/42-india-vs-japan-dustbin"
os.makedirs(OUT, exist_ok=True)
TOTAL = 6


def s1():
    im = base(); d = ImageDraw.Draw(im)
    x, _ = chip(d, MARGIN, 120, "INDIA", SAFFRON)
    f = font(BOLD, 38); d.text((x + 18, 128), "vs", font=f, fill=GREY)
    chip(d, x + 70, 120, "JAPAN", CRIMSON, fg=WHITE)
    y = headline_stack(d, 300, [
        ("JAPAN MEIN", WHITE),
        ("DUSTBIN", SAFFRON),
        ("DHOONDHNA", WHITE),
        ("MUSHKIL HAI.", WHITE),
    ], start=190, gap=22)
    rule(d, MARGIN, y + 20, 160, CRIMSON)
    body(d, y + 70, "Phir bhi sadak saaf. Kaise?", col=GOLD, size=62, path=BOLD)
    swipe(d); footer(d, 1, TOTAL)
    return im


def s3():
    im = base(); d = ImageDraw.Draw(im)
    y = headline_stack(d, 120, [("WRAPPER KA", WHITE), ("SAFAR", SAFFRON)], start=150)
    versus(d, y + 50,
           ("INDIA", SAFFRON, ["Chips khatam.", "Packet haath se seedha sadak pe.", "Dustbin? Door tha."]),
           ("JAPAN", CRIMSON, ["Chips khatam.", "Packet jeb ya bag mein.", "Ghar pahunch ke dustbin."]),
           h=640)
    footer(d, 3, TOTAL)
    return im


def s4():
    im = base(); d = ImageDraw.Draw(im)
    chip(d, MARGIN, 120, "SACH", GOLD)
    f = fit(d, "1995", ANTON, W - 2 * MARGIN, 330)
    w, h, ox, oy = tw(d, "1995", f)
    d.text((MARGIN - ox, 230 - oy), "1995", font=f, fill=CRIMSON)
    y = 230 + h + 50
    y = body(d, y, "Tokyo subway attack ke baad Japan ne public jagahon se dustbins hata diye.",
             col=WHITE, size=62, path=SEMI)
    y = body(d, y + 40, "Aaj bhi wahan log bahar ka kachra ghar le jaate hain, aur wahin chhaant ke phenkte hain.",
             col=GREY, size=56)
    body(d, H - 190, "Source: Wikipedia, 'Waste management in Japan'", col=DIM, size=30)
    footer(d, 4, TOTAL)
    return im


def s5():
    im = base(); d = ImageDraw.Draw(im)
    chip(d, MARGIN, 120, "TAMEEZ", SAFFRON)
    y = headline_stack(d, 240, [
        ("FARQ DUSTBIN", WHITE),
        ("KA NAHI.", WHITE),
        ("AADAT KA HAI.", SAFFRON),
    ], start=170, gap=22)
    rule(d, MARGIN, y + 20, 160, GOLD)
    y = body(d, y + 80, "Aaj se ek kaam:", col=GOLD, size=56, path=BOLD)
    body(d, y + 6, "Bag ya jeb mein ek chhoti thaili. Wrapper usmein. Ghar pe dustbin. Bas.",
         col=WHITE, size=54, path=SEMI)
    footer(d, 5, TOTAL)
    return im


def s6():
    im = base(); d = ImageDraw.Draw(im)
    y = headline_stack(d, 200, [
        ("JAPAN JAISA", WHITE),
        ("SAAF HO SAKTA", WHITE),
        ("HAI.", SAFFRON),
    ], start=170, gap=22)
    y = body(d, y + 40, "Koi naya rule nahi chahiye. Bas ek nayi aadat.", col=GREY, size=54, path=SEMI)
    rule(d, MARGIN, y + 40, W - 2 * MARGIN, (44, 41, 39), h=3)
    y = body(d, y + 90, "SAVE karo.", col=WHITE, size=64, path=BOLD)
    body(d, y, "Us dost ko bhejo jo wrapper sadak pe phenkta hai.", col=GOLD, size=54, path=SEMI)
    f = font(ANTON, 64)
    w, h, ox, oy = tw(d, HANDLE, f)
    d.text((MARGIN - ox, H - 230 - oy), HANDLE, font=f, fill=SAFFRON)
    footer(d, 6, TOTAL)
    return im


for n, fn in ((1, s1), (3, s3), (4, s4), (5, s5), (6, s6)):
    p = os.path.join(OUT, f"slide_{n}.png")
    fn().save(p, optimize=True)
    print(p)
