#!/usr/bin/env python3
"""Week of 17 Nov: three India-vs carousels. Slide 2 (AI photo) is added in Buffer."""
import os, sys
from PIL import ImageDraw
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from intense import *  # noqa

ROOT = sys.argv[1] if len(sys.argv) > 1 else "out"
TOTAL = 6

def hook(country, lines, sub):
    im = base(); d = ImageDraw.Draw(im)
    x, _ = chip(d, MARGIN, 120, "INDIA", SAFFRON)
    f = font(BOLD, 38); d.text((x + 18, 128), "vs", font=f, fill=GREY)
    chip(d, x + 70, 120, country, CRIMSON, fg=WHITE)
    y = headline_stack(d, 300, lines, start=190, gap=22)
    rule(d, MARGIN, y + 20, 160, CRIMSON)
    body(d, y + 70, sub, col=GOLD, size=62, path=BOLD)
    swipe(d); footer(d, 1, TOTAL)
    return im

def vs(title, left, right, h=640):
    im = base(); d = ImageDraw.Draw(im)
    y = headline_stack(d, 120, title, start=150)
    versus(d, y + 50, left, right, h=h)
    footer(d, 3, TOTAL)
    return im

def fact(big, lines, src, bigsize=330):
    im = base(); d = ImageDraw.Draw(im)
    chip(d, MARGIN, 120, "SACH", GOLD)
    f = fit(d, big, ANTON, W - 2 * MARGIN, bigsize)
    w, h, ox, oy = tw(d, big, f)
    d.text((MARGIN - ox, 230 - oy), big, font=f, fill=CRIMSON)
    y = 230 + h + 50
    y = body(d, y, lines[0], col=WHITE, size=60, path=SEMI)
    body(d, y + 36, lines[1], col=GREY, size=54)
    body(d, H - 200, src, col=DIM, size=30)
    footer(d, 4, TOTAL)
    return im

def fix(lines, ask, text):
    im = base(); d = ImageDraw.Draw(im)
    chip(d, MARGIN, 120, "TAMEEZ", SAFFRON)
    y = headline_stack(d, 240, lines, start=170, gap=22)
    rule(d, MARGIN, y + 20, 160, GOLD)
    y = body(d, y + 80, ask, col=GOLD, size=56, path=BOLD)
    body(d, y + 6, text, col=WHITE, size=54, path=SEMI)
    footer(d, 5, TOTAL)
    return im

def cta(lines, sub, ask):
    im = base(); d = ImageDraw.Draw(im)
    y = headline_stack(d, 200, lines, start=170, gap=22)
    y = body(d, y + 40, sub, col=GREY, size=54, path=SEMI)
    rule(d, MARGIN, y + 40, W - 2 * MARGIN, (44, 41, 39), h=3)
    y = body(d, y + 90, "SAVE karo.", col=WHITE, size=64, path=BOLD)
    body(d, y, ask, col=GOLD, size=54, path=SEMI)
    f = font(ANTON, 64)
    w, h, ox, oy = tw(d, HANDLE, f)
    d.text((MARGIN - ox, H - 230 - oy), HANDLE, font=f, fill=SAFFRON)
    footer(d, 6, TOTAL)
    return im

POSTS = {
 "42-india-vs-singapore-gum": {
  1: lambda: hook("SINGAPORE", [("GUM CHABAKE", WHITE), ("KAHAN", SAFFRON), ("PHENKTE HO?", WHITE)], "Ek sheher ne iska jawab dhoondha."),
  3: lambda: vs([("EK GUM,", WHITE), ("DO SHEHER", SAFFRON)],
        ("INDIA", SAFFRON, ["Chabaya. Swaad gaya.", "Seedha zameen pe.", "Chappal pe chipka."]),
        ("SINGAPORE", CRIMSON, ["Gum ki bikri hi band.", "Sirf doctor wali allowed.", "Rule sakht, sabko pata."])),
  4: lambda: fact("1992", ["Singapore ne 3 January 1992 se chewing gum ki bikri par ban lagaya.",
        "2004 se sirf doctor ya pharmacist se milne wali dental aur therapeutic gum allowed hai."],
        "Source: Wikipedia, 'Chewing gum sales ban in Singapore'"),
  5: lambda: fix([("BAN KI ZAROORAT", WHITE), ("NAHI PADEGI,", WHITE), ("AADAT BADLO.", SAFFRON)],
        "Aaj se ek kaam:", "Gum khatam? Usi ke kagaz mein lapeto. Dustbin mein daalo. Bas dus second."),
  6: lambda: cta([("HUM BHI KAR", WHITE), ("SAKTE HAIN.", SAFFRON)], "Kisi ban ke bina. Sirf ek chhoti aadat se.",
        "Us dost ko bhejo jo gum sadak pe thookta hai."),
 },
 "43-india-vs-germany-bottle": {
  1: lambda: hook("GERMANY", [("BOTTLE KA", WHITE), ("PAISA", SAFFRON), ("WAPAS MILE,", WHITE), ("TO?", WHITE)], "Wahan yehi hota hai."),
  3: lambda: vs([("BOTTLE KHATAM,", WHITE), ("AAGE KYA?", SAFFRON)],
        ("INDIA", SAFFRON, ["Bottle road pe.", "Ya dustbin ke bagal mein.", "Uthayega koi aur."]),
        ("GERMANY", CRIMSON, ["Bottle machine mein.", "Deposit wapas.", "Phir se recycle."])),
  4: lambda: fact("96%+", ["Germany mein deposit wali bottles aur cans mein se 96% se zyada wapas aati hain.",
        "Deposit lagbhag 8 se 25 cent har bottle ya can par."],
        "Source: DPG Pfandsystem; Secret Berlin", bigsize=300),
  5: lambda: fix([("BOTTLE KABADI", WHITE), ("WALE TAK", WHITE), ("PAHUNCHAO.", SAFFRON)],
        "Aaj se ek kaam:", "Khali bottle phenko mat. Ghar pe ikattha karo, kabadi wale ko do. Unki kamai hai."),
  6: lambda: cta([("PAISA NA MILE,", WHITE), ("TO BHI", WHITE), ("SAHI JAGAH.", SAFFRON)], "Deposit system baad mein. Aadat abhi.",
        "Us dost ko bhejo jo bottle sadak pe phenkta hai."),
 },
 "44-india-vs-rwanda-umuganda": {
  1: lambda: hook("RWANDA", [("HAR MAHINE", WHITE), ("EK SHANIVAR", SAFFRON), ("SAFAI KE NAAM.", WHITE)], "Rwanda ka Umuganda."),
  3: lambda: vs([("SHANIVAR", WHITE), ("KAISE KATTE HAIN?", SAFFRON)],
        ("INDIA", SAFFRON, ["Der tak sona.", "Mall ya phone.", "Gali ka kachra? Koi aur dekhega."]),
        ("RWANDA", CRIMSON, ["Aakhri Shanivar, 8 se 11.", "Poora mohalla saath.", "Saath mein safai."]), h=700),
  4: lambda: fact("8 - 11", ["Rwanda mein Umuganda har mahine ke aakhri Shanivar, subah 8 se 11 baje hota hai.",
        "18 se 65 saal ke log hissa lete hain. Mukhya kaam: community clean-up."],
        "Source: Wikipedia, 'Umuganda'", bigsize=300),
  5: lambda: fix([("EK GHANTA", WHITE), ("MOHALLE", WHITE), ("KE NAAM.", SAFFRON)],
        "Is mahine ek Shanivar:", "Gali ya society ke paanch log. Jhaadu, thaili, ek ghanta. Photo daalo, hume tag karo."),
  6: lambda: cta([("HUM BHI KAR", WHITE), ("SAKTE HAIN.", SAFFRON)], "Koi naya rule nahi. Bas paanch log aur ek Shanivar.",
        "Apne mohalle ke group mein bhejo."),
 },
}
for slug, slides in POSTS.items():
    out = os.path.join(ROOT, slug); os.makedirs(out, exist_ok=True)
    for n, fn in slides.items():
        p = os.path.join(out, f"slide_{n}.png"); fn().save(p, optimize=True)
        print(p)
