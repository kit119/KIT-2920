# Taisho Jingo-ji Tripitaka Rendering Experiment 

An experimental archive exploring the transformation of the Taisho Tripitaka across scripts, formats, and visual systems.

---

Taisho Jingo-ji Tripitaka Rendering Experiment  
*A Generative Archive*

https://archive.org/details/taisho-jingoji-tripitaka-experiment

This project reinterprets the Taisho Tripitaka as a generative visual system.

Instead of reproducing historical pages, it reconstructs them through code:
- XML text extraction
- Character normalization (CJK focus)
- Grid-based vertical composition
- Programmatic pagination
- Image rendering via Python (Pillow)

Each page is not scanned, but **rendered** — a synthetic reconstruction of textual space.

---

## Method

The entire pipeline is implemented in a minimal Python script:

- Parse TEI XML
- Normalize characters into a controlled glyph space
- Paginate into fixed grid (30 × 17)
- Render vertical layout
- Export high-resolution images

No external dependencies beyond Pillow.

---

## Concept

This repository is not a reproduction project.

It is an attempt to:
- Decouple scripture from script
- Explore cross-script legibility
- Treat text as a generative visual structure

See [HOWCOME](HOWCOME.md)

---


## Usage

pip install Pillow

```bash
python taisho-render.py