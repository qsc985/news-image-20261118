#!/usr/bin/env python3
"""Draw the 18 November 2026 world-news front page (1024x1024 PNG).

Run once, in this session, to produce entry.png. The submitted entry
program (main.py) only copies entry.png to /output/entry.png, so the
graded runs are byte-identical and need no network or third-party libs.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (251, 248, 241)
INK = (26, 26, 26)
NAVY = (20, 33, 61)
GOLD = (201, 162, 39)
RED = (180, 35, 24)
GRAY = (85, 85, 85)
TEAL = (14, 107, 107)
BLUE = (31, 78, 121)
GREEN = (46, 125, 50)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = FONT_DIR + "DejaVuSerif-Bold.ttf"
SANS = FONT_DIR + "DejaVuSans.ttf"
SANS_B = FONT_DIR + "DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_globe(d, cx, cy, r, color, width=4):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=width)
    d.ellipse([cx - r * 0.45, cy - r, cx + r * 0.45, cy + r],
              outline=color, width=width - 1)
    d.line([cx - r, cy, cx + r, cy], fill=color, width=width - 1)
    d.arc([cx - r, cy - r * 0.55, cx + r, cy + r * 0.55],
          200, 340, fill=color, width=width - 1)
    d.arc([cx - r, cy - r * 0.55, cx + r, cy + r * 0.55],
          20, 160, fill=color, width=width - 1)


def draw_bridge(d, x, y, s, color):
    # simple suspension-bridge pictogram in a s x s box
    d.line([x, y + s * 0.8, x + s, y + s * 0.8], fill=color, width=5)
    d.line([x + s * 0.2, y + s * 0.15, x + s * 0.2, y + s * 0.8],
           fill=color, width=5)
    d.line([x + s * 0.8, y + s * 0.15, x + s * 0.8, y + s * 0.8],
           fill=color, width=5)
    d.arc([x + s * 0.2, y + s * 0.05, x + s * 0.8, y + s * 0.75],
          180, 360, fill=color, width=4)


def draw_dome(d, x, y, s, color):
    # parliament dome: pediment + columns
    d.polygon([(x, y + s * 0.35), (x + s / 2, y), (x + s, y + s * 0.35)],
              fill=color)
    d.rectangle([x + s * 0.1, y + s * 0.45, x + s * 0.9, y + s * 0.55],
                fill=color)
    for i in range(4):
        cx = x + s * (0.18 + i * 0.21)
        d.rectangle([cx, y + s * 0.6, cx + s * 0.09, y + s * 0.95],
                    fill=color)
    d.rectangle([x, y + s * 0.95, x + s, y + s], fill=color)


def draw_chip(d, x, y, s, color):
    d.rectangle([x + s * 0.25, y + s * 0.25, x + s * 0.75, y + s * 0.75],
                outline=color, width=5)
    d.rectangle([x + s * 0.42, y + s * 0.42, x + s * 0.58, y + s * 0.58],
                fill=color)
    for i in range(3):
        off = s * (0.32 + i * 0.18)
        d.line([x + off, y + s * 0.08, x + off, y + s * 0.25],
               fill=color, width=4)
        d.line([x + off, y + s * 0.75, x + off, y + s * 0.92],
               fill=color, width=4)
        d.line([x + s * 0.08, y + off, x + s * 0.25, y + off],
               fill=color, width=4)
        d.line([x + s * 0.75, y + off, x + s * 0.92, y + off],
               fill=color, width=4)


def draw_ball(d, x, y, s, color):
    d.ellipse([x + s * 0.15, y + s * 0.15, x + s * 0.85, y + s * 0.85],
              outline=color, width=5)
    d.arc([x + s * 0.15, y + s * 0.15, x + s * 0.85, y + s * 0.85],
          300, 60, fill=color, width=3)
    d.arc([x + s * 0.15, y + s * 0.15, x + s * 0.85, y + s * 0.85],
          120, 240, fill=color, width=3)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ----
    d.rectangle([0, 0, W, 148], fill=NAVY)
    f_mast = font(SERIF_B, 78)
    t = "WORLD NEWS"
    d.text(((W - d.textlength(t, font=f_mast)) / 2, 14), t,
           font=f_mast, fill=(255, 255, 255))
    f_date = font(SANS_B, 30)
    t2 = "WEDNESDAY  ·  18 NOVEMBER 2026"
    d.text(((W - d.textlength(t2, font=f_date)) / 2, 100), t2,
           font=f_date, fill=GOLD)
    d.rectangle([0, 148, W, 154], fill=GOLD)

    # ---- lead story ----
    x0, x1 = 44, 980
    d.rectangle([x0, 178, x0 + 8, 388], fill=RED)
    f_kick = font(SANS_B, 23)
    d.text((x0 + 26, 176), "ASIA-PACIFIC  •  DIPLOMACY",
           font=f_kick, fill=RED)
    f_head = font(SERIF_B, 50)
    d.text((x0 + 26, 206), "Trump lands in Manila", font=f_head, fill=INK)
    d.text((x0 + 26, 264), "for Quad talks", font=f_head, fill=INK)
    f_body = font(SANS, 25)
    lead = ("The US president arrived for Quad talks, ahead of a "
            "visit to China to meet Xi Jinping.")
    lines = wrap(d, lead, f_body, 680)
    y = 330
    for ln in lines:
        d.text((x0 + 26, y), ln, font=f_body, fill=(40, 40, 40))
        y += 34
    draw_globe(d, 872, 290, 58, NAVY, 5)
    d.line([x0, 404, x1, 404], fill=(200, 190, 170), width=2)

    # ---- 2x2 grid of stories ----
    stories = [
        ("WAR", RED, draw_bridge,
         "Ukraine hits the Crimean bridge",
         "Kyiv said it damaged the bridge linking Russia to Crimea "
         "for a second day, as Russian strikes pounded bridges in Kyiv."),
        ("MIDDLE EAST", TEAL, draw_dome,
         "Israel taps Eisenkot to form government",
         "President Herzog asked ex-army chief Gadi Eisenkot to try "
         "to form a government, bypassing Benjamin Netanyahu."),
        ("BUSINESS", BLUE, draw_chip,
         "Nvidia posts bumper results",
         "The chipmaker reported strong quarterly earnings and said "
         "former chief Jensen Huang will not return."),
        ("SPORT", GREEN, draw_ball,
         "Dhoni retires from the IPL",
         "MS Dhoni ended his playing career and will become a mentor "
         "at Chennai Super Kings."),
    ]
    f_tag = font(SANS_B, 20)
    f_ghead = font(SERIF_B, 29)
    f_gbody = font(SANS, 21)
    gx0, gx1 = 44, 980
    gy0 = 424
    cell_w = (gx1 - gx0 - 28) // 2
    cell_h = 204
    for i, (tag, color, icon, head, body) in enumerate(stories):
        cx = gx0 + (i % 2) * (cell_w + 28)
        cy = gy0 + (i // 2) * (cell_h + 16)
        # tag chip
        tw = d.textlength(tag, font=f_tag) + 22
        d.rectangle([cx, cy, cx + tw, cy + 30], fill=color)
        d.text((cx + 11, cy + 3), tag, font=f_tag, fill=(255, 255, 255))
        icon(d, cx + cell_w - 52, cy + 2, 44, color)
        # headline (up to 2 lines)
        hlines = wrap(d, head, f_ghead, cell_w - 8)
        hy = cy + 42
        for ln in hlines[:2]:
            d.text((cx, hy), ln, font=f_ghead, fill=INK)
            hy += 36
        # body (up to 3 lines)
        blines = wrap(d, body, f_gbody, cell_w - 8)
        by = hy + 6
        for ln in blines[:3]:
            d.text((cx, by), ln, font=f_gbody, fill=(60, 60, 60))
            by += 27
        if i % 2 == 0:
            d.line([cx + cell_w + 14, cy, cx + cell_w + 14,
                    cy + cell_h - 8], fill=(215, 205, 185), width=2)
    d.line([gx0, 852, gx1, 852], fill=(200, 190, 170), width=2)

    # ---- briefs strip ----
    f_brief = font(SANS_B, 22)
    briefs = [
        (RED, "UK and Australia sanction firms over West Bank settlements."),
        (TEAL, "Cyclone Akvan set to turn severe over the Bay of Bengal."),
    ]
    by = 872
    for color, text in briefs:
        d.rectangle([44, by + 6, 58, by + 20], fill=color)
        d.text((70, by), text, font=f_brief, fill=INK)
        by += 38

    # ---- footer ----
    d.line([44, 956, 980, 956], fill=(200, 190, 170), width=2)
    f_foot = font(SANS, 18)
    t3 = "Every event reported on Wednesday 18 November 2026  •  One day, six stories"
    d.text(((W - d.textlength(t3, font=f_foot)) / 2, 972), t3,
           font=f_foot, fill=GRAY)

    img.save("entry.png", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
