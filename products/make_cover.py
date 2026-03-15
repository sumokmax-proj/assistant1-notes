from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1280, 720
BG      = (15, 15, 25)
ACCENT  = (99, 102, 241)   # indigo
ACCENT2 = (16, 185, 129)   # emerald
WHITE   = (255, 255, 255)
GRAY    = (160, 160, 180)
CARD_BG = (28, 28, 42)

img  = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# gradient-like top bar
for i in range(6):
    alpha = 1.0 - i / 6
    c = tuple(int(ACCENT[j] * alpha + BG[j] * (1 - alpha)) for j in range(3))
    draw.rectangle([0, i * 2, W, i * 2 + 2], fill=c)

# top accent line
draw.rectangle([0, 0, W, 4], fill=ACCENT)

# left side vertical bar
draw.rectangle([60, 100, 64, 620], fill=ACCENT)

# --- TITLE ---
try:
    font_big   = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 64)
    font_med   = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
    font_tag   = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
    font_code  = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf", 22)
except:
    font_big = font_med = font_small = font_tag = font_code = ImageFont.load_default()

draw.text((88, 108), "Python Automation", font=font_big, fill=WHITE)
draw.text((88, 182), "Scripts Pack", font=font_big, fill=ACCENT)
draw.text((88, 262), "v1.0", font=font_med, fill=ACCENT2)

draw.text((88, 310), "4 ready-to-run scripts  ·  Save hours every week", font=font_small, fill=GRAY)

# --- SCRIPT CARDS ---
cards = [
    ("[FILE]",  "file_organizer.py",  "Auto-sort files"),
    ("[MAIL]",  "email_drafter.py",   "Email templates"),
    ("[PRICE]", "price_monitor.py",   "Price tracking"),
    ("[PDF]",   "pdf_extractor.py",   "PDF extraction"),
]

card_w, card_h = 240, 110
card_y = 390
gap = 20
start_x = 88

for i, (icon, name, desc) in enumerate(cards):
    cx = start_x + i * (card_w + gap)
    draw.rounded_rectangle([cx, card_y, cx + card_w, card_y + card_h], radius=12, fill=CARD_BG)
    draw.rounded_rectangle([cx, card_y, cx + card_w, card_y + 3], radius=2, fill=ACCENT2)
    draw.text((cx + 14, card_y + 12), icon,  font=font_tag,  fill=ACCENT2)
    draw.text((cx + 14, card_y + 44), name,  font=font_code, fill=WHITE)
    draw.text((cx + 14, card_y + 78), desc,  font=font_tag,  fill=GRAY)

# --- PRICE BADGE ---
draw.rounded_rectangle([88, 528, 210, 578], radius=10, fill=ACCENT)
draw.text((108, 540), "Only $9", font=font_med, fill=WHITE)

# --- PYTHON BADGE ---
draw.rounded_rectangle([228, 528, 400, 578], radius=10, fill=CARD_BG)
draw.text((248, 540), "Python 3.10+", font=font_med, fill=ACCENT2)

# --- BOTTOM LINE ---
draw.text((88, 610), "file_organizer  ·  email_drafter  ·  price_monitor  ·  pdf_extractor", font=font_tag, fill=(80, 80, 100))

out = "/home/ubuntu/hustle1/products/cover.png"
img.save(out, "PNG")
print(f"Saved: {out}  ({W}x{H})")
