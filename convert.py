# KIT-81258
# Hanja -> Hangul -> Roman
# Experimental transliteration for reading & chanting aids
# No accuracy, authority, or canonical claim is made.
# Intended for reading and chanting continuity only.
import sys
import os
import zipfile
import re

import hanja
from korean_romanizer.romanizer import Romanizer

# -------------------------------------------------
# Core transforms
# -------------------------------------------------

def hanja_to_hangul(text: str) -> str:
    """
    Convert Hanja to Hangul using Sino-Korean substitution.
    Unknown characters are left untouched.
    """
    return hanja.translate(text, 'substitution')

def hangul_to_roman(text: str) -> str:
    """
    Chant-readable Romanization:
    - Preserve line breaks
    - Romanize per Hangul syllable
    """

    lines = text.splitlines()
    out_lines = []

    for line in lines:
        result = []
        buffer = []

        for ch in line:
            # Hangul syllable block
            if '\uAC00' <= ch <= '\uD7A3':
                buffer.append(Romanizer(ch).romanize())
            else:
                if buffer:
                    result.append(' '.join(buffer))
                    buffer = []
                if ch.strip():
                    result.append(ch)

        if buffer:
            result.append(' '.join(buffer))

        # normalize spaces INSIDE the line only
        roman_line = ' '.join(result)
        roman_line = re.sub(r'[ \t]+', ' ', roman_line).strip()

        out_lines.append(roman_line)

    # rejoin with original line structure
    return '\n'.join(out_lines)


# -------------------------------------------------
# Processing
# -------------------------------------------------

def process_text(text: str):
    hangul = hanja_to_hangul(text)
    roman = hangul_to_roman(hangul)
    return hangul, roman


def process_zip(zip_path: str):
    if not zipfile.is_zipfile(zip_path):
        raise RuntimeError("Input is not a valid zip file")

    base = os.path.splitext(zip_path)[0]
    out_dir = "output"
    os.makedirs(out_dir, exist_ok=True)

    with zipfile.ZipFile(zip_path, "r") as z:
        for name in z.namelist():
            if not name.lower().endswith(".txt"):
                continue

            raw = z.read(name).decode("utf-8", "replace")
            hangul, roman = process_text(raw)

            stem = os.path.splitext(os.path.basename(name))[0]

            with open(os.path.join(out_dir, stem + "-hangul.txt"),
                      "w", encoding="utf-8") as f:
                f.write(hangul)

            with open(os.path.join(out_dir, stem + "-roman.txt"),
                      "w", encoding="utf-8") as f:
                f.write(roman)

    return out_dir


# -------------------------------------------------
# CLI
# -------------------------------------------------

def main():
    if len(sys.argv) != 2:
        print("Usage: python convert.py koreana.zip")
        sys.exit(1)

    zip_path = sys.argv[1]
    out = process_zip(zip_path)

    print("Done.")
    print(f"Output directory: {out}/")


if __name__ == "__main__":
    main()