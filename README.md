# KIT-2920
## Taishō Tripiṭaka Clean Reading Layer

---

# Overview

KIT-2920 is a **reading-first transliteration infrastructure** for the Chinese Buddhist Canon.

It converts large Hanzi corpora (CBETA / SAT / Taishō / other editions) into:

- Clean plain text
- Fully Latin-readable Pinyin layer
- Machine-friendly ZIP corpus
- No XML nesting
- No TEI parsing required

This project does NOT compete with CBETA or SAT.

It builds a **machine-friendly reading layer** on top of them.

---

# Why This Exists

CBETA XML-P5 is excellent for scholarship.

But:

- Deep TEI nesting
- Editorial markup
- Complex structural tags

For most developers and general readers:

> Parsing becomes the barrier.

KIT-2920 removes that barrier.

The canon does not need UI.
It needs a clear passage.

---

# About SAT (Saṃgha Academic Taishō)

The SAT Daizōkyō Text Database (SAT 大正新脩大藏經テキストデータベース)  
is one of the most important digital editions of the Taishō Tripiṭaka.

SAT provides:

- High-quality digital transcription of Taishō volumes
- Careful editorial structure
- Stable academic references
- Page/column line alignment with printed Taishō edition
- Long-term institutional maintenance (University of Tokyo)

SAT is widely used in:

- Japanese Buddhist studies
- East Asian textual research
- Citation-standard academic publications
- Digital humanities projects

---

# Relationship Between KIT-2920 and SAT

KIT-2920 does NOT modify SAT content.

It:

- Extracts readable Hanzi text
- Preserves editorial separation
- Does not merge or overwrite SAT decisions
- Respects Volume 85 distinctions

Where CBETA and SAT differ,
KIT-2920 keeps them separate.

No forced harmonization.

---

# Why SAT Matters Here

Taishō volumes 56–84 rely heavily on SAT digital sources.

Without SAT:

- Many later Taishō texts would not be easily accessible
- Cross-reference alignment would be difficult
- Machine-scale processing would be unstable

SAT provides structural integrity.

KIT-2920 provides reading accessibility.

They serve different but complementary purposes.

---

# Acknowledgment

This project acknowledges the immense scholarly labor behind:

- The SAT Daizōkyō Database
- CBETA editorial teams
- The original Taishō compilers

KIT-2920 stands on their foundation.

It only builds a bridge for broader access.


# What Is Included

## Main Corpus

```
1-cbeta-sat-taisho-dzk-85vol-text-Hanzi.zip
2-cbeta-sat-taisho-dzk-85vol-text-Hanzi.zip
3-cbeta-sat-taisho-dzk-85vol-text-Hanzi.zip

4-cbeta-sat-taisho-dzk-2920n-text-Hanzi.zip
5-cbeta-sat-taisho-dzk-2920n-text-Hanzi.zip
6-cbeta-sat-taisho-dzk-2920n-text-Hanzi.zip
```

Characteristics:

- Flat UTF-8 text
- No forced unification of CBETA/SAT differences
- Volume 85 separated honestly
- Grep/search friendly
- Archive-ready

---

# Transliteration Layer

Currently stable:

```
Hanzi → Pinyin (Tone)
```

Output example:

```
佛說阿彌陀經
fó shuō ā mí tuó jīng
```

Properties:

- Space-separated syllables
- Tone marks preserved
- No blank output
- No raw Hanzi leakage
- Dictionary override supported

---

# Architecture

Processing flow:

```
ZIP corpus
→ extract
→ phrase dictionary override
→ word dictionary override
→ pypinyin fallback
→ clean UTF-8 text
→ repackage ZIP
```

Dictionary priority:

1. dict-viet-phrase.json
2. dict-viet.json
3. dict-budda.json
4. pypinyin fallback

---

# Performance Snapshot

Example (Taishō full corpus):

```
Files: 2457
Size: 82 MB → 249 MB
Time: ~33 seconds
```

Example (Qianlong):

```
Files: 1778
Time: ~19 seconds
```

Heavy mode supported.

---

# Project Structure

```
github/
│
├── convert.py
├── requirements.txt
├── dict/
│   ├── dict-budda.json
│   ├── dict-fgs.json
│   ├── dict-viet.json
│   └── dict-viet-phrase.json
│
├── output/
│
└── corpus *.zip
```

---

# Design Principles

## 1. Reading First
The corpus must be readable immediately.

## 2. Machine Friendly
Flat text > XML nesting.

## 3. Honest Editorial Separation
Volume 85 not forcibly merged.

## 4. No Blank Policy
If dictionary fails → fallback to pinyin.
Never output empty.
Never block reading.

---

# Not a Critical Edition

KIT-2920:

- Does NOT replace CBETA
- Does NOT edit canonical text
- Does NOT claim textual authority

It is a:

> Script bridge and reading infrastructure layer.

---

# Roadmap

Near-term:

- Multi-script expansion (CJKV)
- Vietnamese smoothing layer
- Archive publishing (IA / Zenodo)
- SHA256 checksum release

Mid-term:

- Multi-layer output (Hanzi + Pinyin)
- Cross-edition alignment mode
- Phrase refinement system

Long-term:

- Full script-bridge platform

---

# Intended Impact

If CBETA XML reaches scholars,
KIT-2920 aims to reach:

- Developers
- General readers
- Overseas Chinese communities
- Latin-script users
- AI systems
- Archive platforms

Removing XML complexity can increase accessibility dramatically.

---

# License & Attribution

Source corpus:
- CBETA
- SAT Daizōkyō
- Taishō Shinshū Daizōkyō

This project redistributes processed text.
It does not modify canonical content.

Respect original editorial sources.

---

# Core Statement

The canon does not need protection from readers.

It needs protection from barriers.

# 關於 SAT（Saṃgha Academic Taishō）

SAT 大正新脩大藏經テキストデータベース  
是目前最重要的大正藏數位版本之一。

SAT 提供：

- 高品質的大正藏數位文本
- 嚴謹的學術編輯結構
- 穩定的學術引用基準
- 與紙本大正藏對應的頁碼、欄位與行號
- 長期由東京大學等機構維護

SAT 被廣泛使用於：

- 日本佛教研究
- 東亞佛典文本研究
- 學術引用與標準出版
- 數位人文計畫

---

# KIT-2920 與 SAT 的關係

KIT-2920 不修改 SAT 的原始內容。

本專案：

- 僅提取可閱讀的漢字文本
- 保留不同版本的編輯差異
- 不強制合併 CBETA 與 SAT
- 對於第 85 卷保持獨立處理

當 CBETA 與 SAT 有差異時，  
KIT-2920 採取「並存而不混合」的原則。

不進行強制統一。

---

# 為何 SAT 在此專案中重要

大正藏第 56–84 卷主要依賴 SAT 數位資料。

若無 SAT：

- 後期卷冊的數位取得將更加困難
- 頁碼對應與學術引用將不穩定
- 大規模機器處理將缺乏結構依據

SAT 提供的是學術結構的穩定性。

KIT-2920 提供的是閱讀層與機器友善層。

兩者角色不同，但互補。

---

# 致謝

本專案對以下學術團隊深表敬意：

- SAT 大正藏資料庫團隊
- CBETA 編輯團隊
- 原大正藏編纂者

KIT-2920 只是建立在這些基礎之上的  
一個閱讀與轉寫橋樑。

Users should verify upstream licensing conditions before redistribution.