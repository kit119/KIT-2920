KIT-2920
CBETA Humanitarium Automated Transliteration (CHAT)
🌏 Overview

KIT-2920 is a reading-oriented, machine-friendly corpus layer built upon the Taishō Tripiṭaka (大正新脩大藏經), covering:

Volumes: 1–85

Texts: 2,920 works

This project does not produce a new canonical edition.
Instead, it provides a structured transliteration layer to improve:

📖 Readability

🌐 Cross-script accessibility

🤖 Machine processing compatibility

If a scripture cannot be read easily, it gradually retreats behind its own script.

KIT-2920 seeks to restore accessibility through systematic automation.

📦 Repository Contents

This GitHub repository includes:

convert.py – Core transliteration engine

Dictionary override system

Batch processing utilities

Script conversion pipelines

Sample data (demonstration only)

Full corpus releases are mirrored separately (see Internet Archive releases).

📚 Source Materials

Taishō Tripiṭaka Vol. 1–85 assembled from:

CBETA 2025r3 (Vol. 1–55, 85)

SAT 2018 Edition (Vol. 56–84, alternate Vol. 85)

Editorial differences between traditions are preserved.
No canonical text is modified in this project.

🏗 Architecture

KIT-2920 follows a layered structure:

1️⃣ Canonical Layer

Original digital source texts (CBETA / SAT)

2️⃣ Reading Layer

Automated transliteration outputs
(Pinyin, Kana, Hangul, Vietnamese, Thai, Indic scripts, etc.)

3️⃣ Research Layer

Clean flat text suitable for:

NLP

Alignment studies

Corpus analysis

4️⃣ Community Layer (Planned)

Contribution and correction workflow

🔤 Supported Output Scripts (Phase 1)
Core East Asia

Hanyu Pinyin

Zhuyin

Japanese Kana

Korean Hangul

Vietnamese (Latin-based Han-Viet layer)

Additional Script Layers

Thai

Lao

Myanmar

Devanagari

Siddham

Sinhala

Cyrillic

IPA

Braille

Experimental scripts

🧭 Project Position

KIT-2920 does not attempt:

Critical textual revision

Doctrinal interpretation

Translation of meaning

It focuses strictly on:

Script transformation

Reading accessibility

Structural preservation

🌐 Internet Archive Releases

Full corpus editions (clean text and multi-script layers) are published separately.

Release links are documented in the GitHub Releases section.

⚖ Disclaimer

This project is not a critical edition.
For academic citation, please consult the original CBETA or SAT sources.

中文版
🌏 概述

KIT-2920 為建立於《大正新脩大藏經》之上的閱讀優先語料工程，涵蓋：

第 1–85 冊

共 2,920 部經論

本計畫 不建立新的校勘版本。
其目標為提供可讀轉寫層，以提升：

閱讀可及性

跨文字系統使用

機器處理能力

若經典無法被順利閱讀，終將被文字形式所掩埋。

📦 本倉庫內容

包含：

轉寫核心程式 convert.py

字典覆寫系統

批次處理工具

範例資料

完整語料將另行發佈。

📚 語料來源

CBETA 2025r3（第 1–55 冊、85 冊）

SAT 2018（第 56–84 冊、85 冊對應版本）

不同版本差異保持透明，不進行強制合併。

🏗 架構分層

典籍層（Canonical Layer）

閱讀層（Reading Layer）

研究層（Research Layer）

社群層（規劃中）

🔤 支援文字系統（第一階段）

漢語拼音

注音

日文假名

韓文

越南拉丁轉寫

泰文、寮文、緬文

天城體、悉曇

IPA、點字等

⚖ 聲明

本工程並非校勘版本。
學術引用請以 CBETA 或 SAT 原始文本為準。

ถ้าคุณต้องการ ผมสามารถทำเพิ่มอีกหนึ่ง section:

🧪 Technical Notes (Engine Design & Han-Viet fallback logic)

หรือ 🔧 Example Usage + CLI Examples

หรือ 🚀 Internet Archive Release Template

บอกผมว่าจะเอาโทน “วิศวกรรมล้วน” หรือ “มนุษยศาสตร์ดิจิทัล” เดี๋ยวจัดให้เหมาะกับภาพลักษณ์ที่คุณอยากให้โปรเจกต์ออกไปครับ

HOWTORUN.md พร้อมตัวอย่างพื้นฐานจนถึง advance

ดีมากครับ 👍
ด้านล่างคือ HOWTORUN.md แบบ มี Markdown เต็ม, โทนสุภาพเชิงเทคนิค และเรียงจาก Basic → Advanced → Power User

คุณสามารถวางทั้งหมดลงไฟล์ HOWTORUN.md ได้เลย

HOWTORUN.md
KIT-2920 – Usage Guide
1️⃣ Requirements
Python Version
Python 3.10+

Install Dependencies
pip install -r requirements.txt


If installing manually:

pip install pypinyin tqdm

2️⃣ Directory Structure

Expected project structure:

github/
│
├── convert.py
├── requirements.txt
├── dict/
│   ├── dict-budda.json
│   ├── dict-viet.json
│   ├── dict-viet-phrase.json
│   └── dict-fgs.json
│
├── output/
│
└── input files (*.zip)

3️⃣ Basic Usage
🔹 Example 1 — Convert a Single ZIP Corpus
python convert.py taisho-dzk-text-Hanzi.zip


Output:

Extracts all text files

Applies dictionary overrides

Converts Hanzi → Pinyin

Repackages result into:

output/zout-[text]-[pyin]-<timestamp>.zip

🔹 Example 2 — Explicit Mode (CLI wrapper example)

If using your kit wrapper:

kit -t pyin -s " " taisho-dzk-text-Hanzi.zip


Parameters:

Flag	Meaning
-t pyin	Transliteration target: Pinyin
-s " "	Separator between syllables
4️⃣ Intermediate Usage
🔹 Using Dictionary Override (Recommended)

The system loads:

dict-viet-phrase.json (highest priority)

dict-viet.json

dict-budda.json

Fallback → pypinyin

Override logic:

phrase match → word match → single char → fallback pinyin


To modify behavior:

Edit:

dict/dict-viet-phrase.json


Example entry:

{
  "般若波羅蜜": "bát-nhã-ba-la-mật"
}

🔹 Choosing Pinyin Style

In convert.py, change:

Style.TONE


Options:

Style	Result
Style.NORMAL	No tone marks
Style.TONE	Tone marks (mā, má, mǎ)
Style.TONE3	Numeric tone (ma1, ma2)

Recommended for readability:

Style.TONE


Reason:
Latin-based scripts (Vietnamese readers included) recognize tone marks more intuitively than numeric tone.

5️⃣ Advanced Usage
🔹 Heavy Corpus Mode (Large Archive)

For corpora 50–200MB:

kit -t pyin -s " " qianlong-dzj-text-Hanzi.zip


Expected:

1500–2500 files

15–35 seconds processing

Output ~3× original size

Processing indicator:

Shared Processing: 100%|████████████| 2457/2457

🔹 Phrase-Level Optimization

To improve smoothness:

Expand dict-viet-phrase.json

Prioritize multi-character Buddhist terminology

Avoid single-character overrides unless necessary

Bad:

"法": "pháp"


Better:

"佛法": "phật-pháp"


Phrase-first strategy reduces fragmentation.

🔹 Han-Viet Hybrid Fallback Strategy

Recommended workflow:

Load Vietnamese phrase dictionary

Load Vietnamese word dictionary

Use pypinyin fallback (Latin readable)

Avoid blank or raw Hanzi leakage

Goal:

Never output blank. Never leave raw Hanzi. Always produce readable Latin layer.

6️⃣ Batch Processing Multiple Archives

Example (Windows PowerShell):

Get-ChildItem *.zip | ForEach-Object {
    python convert.py $_.FullName
}


Linux/macOS:

for f in *.zip; do
  python convert.py "$f"
done

7️⃣ Output Structure

Example output ZIP:

zout-[text]-[pyin]-1770737705.zip


Inside:

0001-xxx.txt
0002-xxx.txt
...


Each file:

Pure UTF-8 text

No XML nesting

Machine-friendly

Space-separated syllables

8️⃣ Performance Notes
Corpus	Files	Time
Taisho	~2450	~30 sec
Qianlong	~1700	~20 sec
Dongguk	~1500	~25 sec

Memory usage: moderate
CPU-bound process

9️⃣ Troubleshooting
❗ Output too large?

Expected.
Pinyin layer expands size ~2.5–3× original.

Solution:
Archive with 7-Zip (Ultra compression).

❗ Mixed Hanzi still appears?

Check:

Phrase dictionary coverage

Unmapped rare characters

Unicode compatibility characters

❗ Tone marks look broken?

Ensure:

Terminal supports UTF-8

Windows codepage = UTF-8

chcp 65001

🔟 Future Expansion

Planned:

Vietnamese smoothing engine

Multi-layer parallel output

Alignment mode (Hanzi + Pinyin side-by-side)

IA auto-upload integration

📜 Philosophy

KIT-2920 prioritizes:

Readability

Script accessibility

Structural fidelity

It is not a critical edition.
It is a reading infrastructure.