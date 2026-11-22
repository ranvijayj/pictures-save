#!/usr/bin/env python3
"""Week of 23 Nov: four carousels + reel cards for 'Selfie bhi yahin' (C2 hypocrisy couplet).
Slide 2 of each carousel is an AI photo added in Buffer."""
import os, sys
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from intense import *  # noqa
import intense
_argv = sys.argv
sys.argv = [_argv[0], "/tmp/post_week_import_scratch"]  # post_week renders its own posts on import
from post_week import hook, vs, fix, cta, TOTAL  # noqa: E402
sys.argv = _argv


def fact(big, lines, src, bigsize=330, label="SACH", labcol=GOLD):
    im = base(); d = ImageDraw.Draw(im)
    chip(d, MARGIN, 120, label, labcol)
    f = fit(d, big, ANTON, W - 2 * MARGIN, bigsize)
    w, h, ox, oy = tw(d, big, f)
    d.text((MARGIN - ox, 230 - oy), big, font=f, fill=CRIMSON)
    y = 230 + h + 50
    y = body(d, y, lines[0], col=WHITE, size=56, path=SEMI)
    body(d, y + 30, lines[1], col=GREY, size=50)
    body(d, H - 210, src, col=DIM, size=30)
    footer(d, 4, TOTAL)
    return im


def hook_day(chiptext, lines, sub):
    im = base(); d = ImageDraw.Draw(im)
    chip(d, MARGIN, 120, chiptext, SAFFRON)
    y = headline_stack(d, 300, lines, start=190, gap=22)
    rule(d, MARGIN, y + 20, 160, CRIMSON)
    body(d, y + 70, sub, col=GOLD, size=62, path=BOLD)
    swipe(d); footer(d, 1, TOTAL)
    return im


def fix_chip(label, lines, ask, text):
    im = base(); d = ImageDraw.Draw(im)
    chip(d, MARGIN, 120, label, SAFFRON)
    y = headline_stack(d, 240, lines, start=170, gap=22)
    rule(d, MARGIN, y + 20, 160, GOLD)
    y = body(d, y + 80, ask, col=GOLD, size=56, path=BOLD)
    body(d, y + 6, text, col=WHITE, size=54, path=SEMI)
    footer(d, 5, TOTAL)
    return im


POSTS = {
 "45-india-vs-netherlands-cycle": {
  1: lambda: hook("NETHERLANDS", [("CYCLE WALA", WHITE), ("SADAK PE", SAFFRON), ("KAHAN JAAYE?", WHITE)], "Ek desh ne uske liye raasta banaya."),
  3: lambda: vs([("EK CYCLE,", WHITE), ("DO DESH", SAFFRON)],
        ("INDIA", SAFFRON, ["Horn maaro, side karo.", "Cycle lane pe bike parked.", "Cyclist? Raaste ka kaanta."]),
        ("NETHERLANDS", CRIMSON, ["Alag cycle track.", "Gaadi wale rukte hain.", "Cyclist ko pehle jagah."]), h=700),
  4: lambda: fact("35,000 KM", ["Netherlands mein lagbhag 35,000 km cycle track gaadiyon se alag banaya gaya hai.",
        "Wahan saare safar ka 27% cycle se hota hai."],
        "Source: Wikipedia, 'Cycling in the Netherlands'", bigsize=250),
  5: lambda: fix([("CYCLE KO", WHITE), ("JAGAH DO.", SAFFRON)],
        "Aaj se ek kaam:", "Cyclist dikhe to horn nahi, doori. Cycle lane pe gaadi mat lagao."),
  6: lambda: cta([("HUM BHI KAR", WHITE), ("SAKTE HAIN.", SAFFRON)], "Track baad mein banega. Izzat abhi de sakte hain.",
        "Us dost ko bhejo jo roz cycle se office jaata hai."),
 },
 "46-india-vs-japan-school-safai": {
  1: lambda: hook("JAPAN", [("SCHOOL KI", WHITE), ("SAFAI KAUN", SAFFRON), ("KARTA HAI?", WHITE)], "Japan mein jawab hai: bachche."),
  3: lambda: vs([("CLASS GANDI,", WHITE), ("ZIMMEDAAR KAUN?", SAFFRON)],
        ("INDIA", SAFFRON, ["Wrapper bench ke neeche.", "'Koi aur saaf karega.'", "Wahi aadat sadak pe."]),
        ("JAPAN", CRIMSON, ["Bachche khud safai karte.", "Class, corridor, washroom.", "Aadat bachpan se."]), h=700),
  4: lambda: fact("KHUD", ["Japan ke schools mein students apni classroom khud saaf karte hain.",
        "Sirf class nahi: corridor, schoolyard aur bathroom bhi."],
        "Source: Kids Web Japan (web-japan.org); The Japan Forum (tjf.or.jp)", bigsize=300),
  5: lambda: fix([("BACHCHON KO", WHITE), ("SAFAI SIKHAO.", SAFFRON)],
        "Aaj se ek kaam:", "Ghar pe bachcha apni plate khud uthaye, apna wrapper khud dustbin tak le jaaye."),
  6: lambda: cta([("SAFAI NAUKRI", WHITE), ("NAHI, AADAT HAI.", SAFFRON)], "Jo bachpan mein seekha, wahi sadak pe dikhega.",
        "School wale parents group mein bhejo."),
 },
 "47-samvidhan-diwas-kartavya": {
  1: lambda: hook_day("26 NOVEMBER", [("ADHIKAR SAB", WHITE), ("YAAD HAIN.", WHITE), ("KARTAVYA?", SAFFRON)], "Samvidhan mein woh bhi likha hai."),
  3: lambda: vs([("ADHIKAR", WHITE), ("AUR KARTAVYA", SAFFRON)],
        ("ADHIKAR", SAFFRON, ["Bolne ki azaadi.", "Barabari.", "Sabko yaad hai."]),
        ("KARTAVYA", CRIMSON, ["Paryavaran bachao.", "Public property sambhalo.", "Yaad hai?"]), h=700),
  4: lambda: fact("51A", ["1976 ke 42nd Amendment se Article 51A mein Fundamental Duties jode gaye. Aaj kul 11 hain.",
        "51A(g): natural environment ki raksha. 51A(i): public property ki hifazat."],
        "Source: knowindia.india.gov.in; Constitution of India, Part IVA", bigsize=330, label="KANOON", labcol=GOLD),
  5: lambda: fix_chip("TAMEEZ", [("BUS STOP, PARK,", WHITE), ("DEEWAR:", WHITE), ("SAB HAMARA.", SAFFRON)],
        "Aaj se ek kaam:", "Public cheez ko apni samjho. Na todo, na likho, na gandagi."),
  6: lambda: cta([("ADHIKAR KE SAATH,", WHITE), ("KARTAVYA BHI.", SAFFRON)], "Samvidhan Diwas ki shubhkamnayein.",
        "Adhikar wale dost ko bhejo."),
 },
 "48-india-vs-taiwan-kachra-gaadi": {
  1: lambda: hook("TAIWAN", [("KACHRA GAADI", WHITE), ("GAANA BAJAAYE,", SAFFRON), ("TO?", WHITE)], "Taiwan mein roz yehi hota hai."),
  3: lambda: vs([("KACHRA GAADI", WHITE), ("AAYI, PHIR?", SAFFRON)],
        ("INDIA", SAFFRON, ["Gaadi nikal gayi.", "Thaili khaali plot mein.", "Ya kone mein jala do."]),
        ("TAIWAN", CRIMSON, ["Music suno, bahar aao.", "Kachra seedha truck mein.", "Recycling alag."]), h=700),
  4: lambda: fact("5.87%", ["1997 mein Taiwan ka recycling rate sirf 5.87% tha. 2017 tak ghar ka recycling 50% se zyada.",
        "Kachra gaadi 'Fur Elise' jaisi dhun bajaati hai, taaki log kachra le kar aayein."],
        "Source: Wikipedia, 'Recycling in Taiwan'", bigsize=300),
  5: lambda: fix([("PLOT NAHI,", WHITE), ("GAADI KA", WHITE), ("INTEZAAR.", SAFFRON)],
        "Aaj se ek kaam:", "Gaadi ka time pata karo. Gila-sookha alag, seedha gaadi mein. Khaali plot pe kabhi nahi."),
  6: lambda: cta([("HUM BHI KAR", WHITE), ("SAKTE HAIN.", SAFFRON)], "Gaana baje na baje. Aadat badal sakti hai.",
        "Apne society group mein bhejo."),
 },
}


def hook_banner(head, sub, path):
    """1000x300 transparent PNG: dark rounded box, Anton white headline, Barlow gold line, saffron bar."""
    bw, bh = 1000, 300
    im = Image.new("RGBA", (bw, bh), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, bw - 1, bh - 1], radius=36, fill=(17, 16, 16, 235))
    d.rectangle([40, 50, 52, bh - 50], fill=SAFFRON)
    f = fit(d, head, ANTON, bw - 130, 120)
    w, h, ox, oy = tw(d, head, f)
    d.text((80 - ox, 52 - oy), head, font=f, fill=WHITE)
    f2 = fit(d, sub, BOLD, bw - 130, 64)
    w2, h2, ox2, oy2 = tw(d, sub, f2)
    d.text((80 - ox2, 52 + h + 34 - oy2), sub, font=f2, fill=GOLD)
    im.save(path)


def end_card(lines, ask_lines, path):
    """1080x1920 end card; everything (incl. handle + wordmark) above y=1400."""
    RW, RH = 1080, 1920
    saved = intense.W, intense.H
    intense.W, intense.H = RW, RH
    im = intense.base(); d = ImageDraw.Draw(im)
    intense.W, intense.H = saved
    y = 300
    for text, col in lines:
        f = fit(d, text, ANTON, RW - 2 * MARGIN, 190)
        w, h, ox, oy = tw(d, text, f)
        d.text((MARGIN - ox, y - oy), text, font=f, fill=col); y += h + 26
    d.rectangle([MARGIN, y + 30, MARGIN + 180, y + 40], fill=GOLD)
    y += 90
    fb = font(BOLD, 74)
    for text, col in ask_lines:
        w, h, ox, oy = tw(d, text, fb)
        d.text((MARGIN - ox, y - oy), text, font=fb, fill=col); y += 92
    y += 60
    fh = font(ANTON, 84)
    w, h, ox, oy = tw(d, HANDLE, fh)
    d.text((MARGIN - ox, y - oy), HANDLE, font=fh, fill=SAFFRON); y += h + 40
    f1 = font(ANTON, 44)
    t1, t2 = "CIVIC SENSE ", "INDIA"
    w1, h1, ox1, oy1 = tw(d, t1, f1)
    d.rectangle([MARGIN, y, MARGIN + 12, y + h1 + 4], fill=SAFFRON)
    d.text((MARGIN + 30 - ox1, y - oy1), t1, font=f1, fill=WHITE)
    d.text((MARGIN + 30 + w1 - ox1, y - oy1), t2, font=f1, fill=SAFFRON)
    print("end card bottom y =", y + h1)
    im.save(path)


if __name__ == "__main__":
    ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
    for slug, slides in POSTS.items():
        out = os.path.join(ROOT, "posts", slug); os.makedirs(out, exist_ok=True)
        for n, fn in slides.items():
            p = os.path.join(out, f"slide_{n}.png"); fn().save(p, optimize=True); print(p)
    rd = os.path.join(ROOT, "reels", "02-selfie-bhi-yahin"); os.makedirs(rd, exist_ok=True)
    hook_banner("SELFIE BHI YAHIN.", "Aur chips ka packet bhi yahin?", os.path.join(rd, "hook_banner.png"))
    end_card([("PAHAAD TUMHE", WHITE), ("YAAD RAKHEGA.", WHITE), ("KACHRE SE NAHI.", SAFFRON)],
             [("Bhejo us dost ko", WHITE), ("jo agle weekend", WHITE), ("trip pe ja raha hai.", GOLD)],
             os.path.join(rd, "end_card.png"))
