"""Regenerates assets/og-image.png (1200x630) in the site's Apple-system look. Run before build_dist.py."""
from PIL import Image, ImageDraw, ImageFont
import os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = 2; W, H = 1200 * S, 630 * S
INK, BLUE, PAPER = (10, 27, 54), (11, 92, 255), (251, 252, 255)

def font(size, weight=700):
    f = ImageFont.truetype("/System/Library/Fonts/SFNS.ttf", int(size * S))
    f.set_variation_by_axes([100, 28, 400, weight])
    return f

im = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(im)
# left blue bar gradient
for y in range(H):
    t = y / H
    d.line([(0, y), (22 * S, y)], fill=(int(40 + 40 * t), int(100 + 80 * t), 255))
# logo
logo = Image.open(f"{R}/assets/img/cips-logo-dark.png").convert("RGBA")
lw = 175 * S; logo = logo.resize((lw, int(lw * logo.height / logo.width)), Image.LANCZOS)
im.paste(logo, (84 * S, 60 * S), logo)
# kicker + rule
d.text((84 * S, 152 * S), "CIPS INTERNATIONAL", font=font(17, 700), fill=BLUE)
d.text((84 * S, 180 * S), "PROCUREMENT & SUPPLY CHAIN SUMMIT 2027", font=font(19, 800), fill=INK)
d.line([(84 * S, 222 * S), (724 * S, 222 * S)], fill=INK, width=2 * S)
# headline
y = 258
for i, (txt, col) in enumerate([("Where Procurement", INK), ("Leaders Shape What", INK), ("Comes Next", BLUE)]):
    d.text((84 * S, y * S), txt, font=font(60, 800), fill=col); y += 70
# facts
x = 84
for lab, w in [("07 January 2027", 190), ("ITC Maratha, Mumbai", 240), ("www.cips2027.online", 240)]:
    d.rectangle([x * S, 540 * S, (x + w - 10) * S, 543 * S], fill=BLUE)
    d.text((x * S, 560 * S), lab, font=font(21, 700), fill=INK)
    x += w + 14
# pass card
cx0, cy0, cx1, cy1 = 790, 50, 1130, 580
card = Image.new("RGB", (W, H)); cd = ImageDraw.Draw(card)
for y in range(cy0 * S, cy1 * S):
    t = (y - cy0 * S) / ((cy1 - cy0) * S)
    cd.line([(cx0 * S, y), (cx1 * S, y)], fill=(int(46 - 36 * t), int(104 - 76 * t), int(255 - 120 * t)))
mask = Image.new("L", (W, H), 0)
ImageDraw.Draw(mask).rounded_rectangle([cx0 * S, cy0 * S, cx1 * S, cy1 * S], radius=26 * S, fill=255)
shadow = Image.new("L", (W, H), 0)
ImageDraw.Draw(shadow).rounded_rectangle([cx0 * S, (cy0 + 22) * S, cx1 * S, (cy1 + 22) * S], radius=26 * S, fill=70)
from PIL import ImageFilter
shadow = shadow.filter(ImageFilter.GaussianBlur(26 * S))
im.paste((11, 60, 200), mask=shadow)
im.paste(card, mask=mask)
d = ImageDraw.Draw(im)
white = (255, 255, 255); soft = (170, 214, 255)
ll = Image.open(f"{R}/assets/img/cips-logo-light.png").convert("RGBA")
lw = 118 * S; ll = ll.resize((lw, int(lw * ll.height / ll.width)), Image.LANCZOS)
im.paste(ll, (822 * S, 84 * S), ll)
d.text((822 * S, 168 * S), "DELEGATE PASS", font=font(15, 700), fill=soft)
d.text((822 * S, 196 * S), "2027", font=font(108, 800), fill=white)
d.text((822 * S, 336 * S), "CIPS INTERNATIONAL", font=font(14, 700), fill=soft)
for i, t in enumerate(["Procurement &", "Supply Chain", "Summit"]):
    d.text((822 * S, (362 + i * 36) * S), t, font=font(30, 800), fill=white)
for x in range(822, 1100, 14):
    d.line([(x * S, 500 * S), ((x + 7) * S, 500 * S)], fill=(120, 160, 255), width=S)
d.text((822 * S, 520 * S), "07 JAN 2027", font=font(13, 700), fill=white)
t = "ITC MARATHA, MUMBAI"; tw = d.textlength(t, font=font(13, 700))
d.text((1098 * S - tw, 520 * S), t, font=font(13, 700), fill=white)
im.resize((1200, 630), Image.LANCZOS).save(f"{R}/assets/og-image.png", optimize=True)
print("og-image.png written")
