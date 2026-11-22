#!/usr/bin/env python3
"""Carousel 49 (Sat 5 Dec): India vs Rwanda polythene ban. Slide 2 is an AI photo added at scheduling time."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from post_week_23nov import *  # noqa
ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
name = "49-india-vs-rwanda-polythene"
P = {
 1: lambda: hook("RWANDA", [("EK DESH NE", WHITE), ("POLYTHENE", SAFFRON), ("BAND KIYA.", WHITE)], "Poora. Sach mein."),
 3: lambda: vs([("EK THAILI,", WHITE), ("DO DESH", SAFFRON)],
        ("INDIA", SAFFRON, ["Sabzi ke saath thaila.", "Thaila phir nali mein.", "Nali phir jaam."]),
        ("RWANDA", CRIMSON, ["Kapde ya kagaz ka bag.", "Polythene par rok.", "Aadat bag ki, thaili ki nahi."]), h=700),
 4: lambda: fact("2008", ["Rwanda ne 2008 ke kanoon (Law No. 57/2008) mein polythene bags banana, import, use aur bechna band kar diya.",
        "Baad mein ye rok single-use plastic tak badhayi gayi."],
        "Source: UNEP LEAP; UNDP Rwanda; World Bank", bigsize=330, label="KANOON", labcol=GOLD),
 5: lambda: fix([("BAG SAATH", WHITE), ("RAKHO.", SAFFRON)],
        "Aaj se ek kaam:", "Ek kapde ka bag gaadi ya bag mein rakho. Dukaan par bolo: 'thaila nahi chahiye.'"),
 6: lambda: cta([("KANOON KA", WHITE), ("INTEZAAR KYUN?", SAFFRON)], "Aadat aaj se shuru ho sakti hai.",
        "Us dost ko bhejo jo har baar thaila maangta hai."),
}
d = os.path.join(ROOT, "posts", name); os.makedirs(d, exist_ok=True)
for n, f in P.items():
    f().save(os.path.join(d, f"slide_{n}.png"))
print("done", d)
