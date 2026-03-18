import os, re, zipfile
from xml.etree import ElementTree as ET
from multiprocessing import Pool, cpu_count
from PIL import Image, ImageDraw, ImageFont
BASE = os.path.dirname(os.path.abspath(__file__))
# ---------------- CONFIG ----------------
W, H = 4320, 2880
COLS, ROWS = 30, 17
MARGIN = 150
FONT_PATH = os.path.join(BASE, "font/NotoSerifTC-Regular.ttf")
# ---------------- GLOBAL ----------------
FONT = None
def init():
    global FONT
    try:
        FONT = ImageFont.truetype(FONT_PATH, 100)
    except:
        FONT = ImageFont.load_default()
# ---------------- TEXT ----------------
def norm(t):
    return re.sub(r"[^\u3400-\u9FFF]", "", t)
def parse_xml(f):
    try:
        root = ET.parse(f).getroot()
    except:
        return "", ""
    for e in root.iter():
        if "}" in e.tag:
            e.tag = e.tag.split("}", 1)[1]
    body = root.find(".//body")
    if body is None:
        return "", ""
    text = []
    for el in body.iter():
        if el.tag in ("p", "l"):
            text.append("".join(el.itertext()))
    title_el = root.find(".//jhead")
    title = "".join(title_el.itertext()) if title_el is not None else ""
    return title, norm("".join(text))
def pages(title, text):
    full = title + text
    size = COLS * ROWS
    return [full[i:i+size] for i in range(0, len(full), size)]
# ---------------- RENDER ----------------
def draw_page(job):
    txt, path = job
    img = Image.new("RGB", (W, H), (3,24,48))
    draw = ImageDraw.Draw(img)
    cw = (W-2*MARGIN)/COLS
    rh = (H-2*MARGIN)/ROWS
    i = 0
    for c in range(COLS):
        x = W - MARGIN - (c+0.5)*cw
        for r in range(ROWS):
            if i >= len(txt): break
            ch = txt[i]
            if ch != " ":
                draw.text((x, MARGIN+r*rh), ch, font=FONT, fill=(160,130,40))
            i += 1
    img.save(path, "JPEG")
# ---------------- MAIN ----------------
def main():
    z = zipfile.ZipFile("xml.zip")
    os.makedirs("out", exist_ok=True)
    for name in z.namelist():
        if not name.endswith(".xml"): continue
        with z.open(name) as f:
            title, text = parse_xml(f)
        pgs = pages(title, text)
        folder = os.path.join("out", os.path.splitext(os.path.basename(name))[0])
        os.makedirs(folder, exist_ok=True)
        jobs = [(p, os.path.join(folder, f"{i:04}.jpg")) for i,p in enumerate(pgs)]
        with Pool(max(1, cpu_count()-1), initializer=init) as pool:
            pool.map(draw_page, jobs)
if __name__ == "__main__":
    main()