#!/usr/bin/env python3
"""Reel cards for pre-built week 29 Nov: 05 Indore 8 saal (C3), 06 Bachche dekhte hain (C2)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from post_week_23nov import hook_banner, end_card, WHITE, SAFFRON, GOLD  # noqa
ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
d = os.path.join(ROOT, "reels", "05-indore-8-saal"); os.makedirs(d, exist_ok=True)
hook_banner("8 SAAL SE NUMBER 1.", "Indore ne kachra kaise haraya?", os.path.join(d, "hook_banner.png"))
end_card([("SHAHAR KO", WHITE), ("CLEAN BANATE HAIN", WHITE), ("LOG.", SAFFRON)],
         [("Bhejo apne shahar", WHITE), ("ke group mein.", GOLD)], os.path.join(d, "end_card.png"))
d = os.path.join(ROOT, "reels", "06-bachche-dekhte-hain"); os.makedirs(d, exist_ok=True)
hook_banner("BACHCHA DEKH RAHA HAI.", "Aap kya sikha rahe ho?", os.path.join(d, "hook_banner.png"))
end_card([("BACHCHE WAHI", WHITE), ("KARTE HAIN", WHITE), ("JO DEKHTE HAIN.", SAFFRON)],
         [("Bhejo us parent ko", WHITE), ("jo gaadi se", WHITE), ("kachra fenkta hai.", GOLD)], os.path.join(d, "end_card.png"))
