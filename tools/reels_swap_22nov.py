#!/usr/bin/env python3
"""Reel cards for the 22 Nov swap: 03 Japan school safai (C2), 04 Taiwan kachra gaadi (C3)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from post_week_23nov import hook_banner, end_card, WHITE, SAFFRON, GOLD  # noqa

ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
d3 = os.path.join(ROOT, "reels", "03-japan-school-safai"); os.makedirs(d3, exist_ok=True)
hook_banner("SCHOOL KI SAFAI?", "Japan mein karte hain bachche.", os.path.join(d3, "hook_banner.png"))
end_card([("SAFAI NAUKRI", WHITE), ("NAHI, AADAT HAI.", SAFFRON)],
         [("Bhejo us parents group", WHITE), ("mein jahan sab", WHITE), ("sirf shikayat karte hain.", GOLD)],
         os.path.join(d3, "end_card.png"))
d4 = os.path.join(ROOT, "reels", "04-taiwan-kachra-gaadi"); os.makedirs(d4, exist_ok=True)
hook_banner("6% SE 50% TAK.", "Taiwan ne kachre ke saath ye kiya.", os.path.join(d4, "hook_banner.png"))
end_card([("GAADI KA", WHITE), ("INTEZAAR KARO.", WHITE), ("PLOT MEIN NAHI.", SAFFRON)],
         [("Bhejo apne society", WHITE), ("group mein.", GOLD)],
         os.path.join(d4, "end_card.png"))
