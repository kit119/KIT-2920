# FORGEEK.md
Technical Notes for Developers, Researchers, and Digital Humanists

---

# 0. What KIT-2920 Actually Is

KIT-2920 is NOT:

- a critical edition
- a theological project
- a doctrinal correction
- a UI layer
- an NLP research paper

It is:

- a machine-friendly corpus layer
- a reading-first flattened text release
- a reproducible transliteration pipeline
- a large-scale CJK canonical processing experiment

---

# 1. Why This Exists

CBETA provides XML-P5.

SAT provides structured academic database.

Both are excellent for:

- citation
- markup integrity
- scholarly apparatus
- textual comparison

But:

They are not optimized for:

- grep
- fast loading
- lightweight distribution
- transliteration pipelines
- NLP preprocessing
- low-resource environments
- large-scale batch conversion

Nested XML inside nested XML inside nested XML
is correct for academia,
but computationally heavy for developers.

KIT-2920 builds a flat corpus layer on top.

---

# 2. Design Philosophy

## 2.1 Reading First

No UI.
No JavaScript.
No database dependency.
No proprietary format.

Just:

- UTF-8
- flat .txt
- deterministic output
- reproducible CLI

---

## 2.2 Determinism Over Cleverness

If you run:

```
kit -t pyin input.zip
```

You should get identical output anywhere.

No hidden AI model.
No stochastic variation.
No remote API calls.

Pure local processing.

---

## 2.3 Separation Policy

Where CBETA and SAT differ:

We do NOT merge.
We do NOT "harmonize".
We do NOT editorialize.

We separate.

Volume 85 remains separate.
Editorial decisions remain traceable.

---

# 3. Architecture Overview

## Pipeline (Simplified)

```
ZIP
 └─ XML / Text
     └─ Clean Hanzi Extraction
         └─ Optional Dictionary Override
             └─ pypinyin Engine
                 └─ Script Converter
                     └─ Flat Text Output
```

Core layers:

1. Input detection (HANZI mode)
2. XML parsing & cleaning
3. Hanzi token extraction
4. Phrase-level override dictionary
5. Character-level fallback (pypinyin)
6. Script transformation
7. Archive packaging

---

# 4. Dictionary Strategy

Important:

More dictionary ≠ better output.

Large phrase dictionaries:

- create collisions
- override unintended segments
- increase memory pressure
- destabilize parsing

Current philosophy:

1. Small curated override dict (Buddhist technical terms)
2. Engine fallback for everything else
3. No blank output
4. No partial failure cascade

---

# 5. Why Not Full NLP?

Because:

- Taishō is not modern Mandarin
- Sentence segmentation is unreliable
- Punctuation is editorial
- Word boundaries are ambiguous
- Variant characters exist

Over-interpretation increases corruption.

KIT-2920 stays conservative.

---

# 6. Corpus Scope

Current verified stable runs:

- Taishō 1–85
- 2920 individual texts
- CBETA + SAT split preserved
- Additional canons tested:
  - Qianlong
  - Dongguk (Korean)
  - Other CJK corpora

Performance example:

```
3012 files
121 MB → 361 MB
~53 seconds
Fully local
```

---

# 7. Release Strategy

GitHub:

- Code
- Small samples
- Documentation

Internet Archive:

- Full corpus
- Heavy releases
- Multi-script expansions

Reason:

GitHub is for developers.
IA is for preservation.

---

# 8. What This Is Not Responsible For

- Doctrinal correctness
- Sectarian disputes
- Philological harmonization
- Variant reconciliation
- Religious authority

This is a transport layer.

Nothing more.
Nothing less.

---

# 9. For Contributors

If you fork:

Please:

- Preserve source attribution
- Preserve volume separation
- Do not silently merge editions
- Document transformation rules
- Keep processing deterministic

If you improve:

- segmentation
- script conversion
- dictionary design
- performance

Document methodology clearly.

Reproducibility > speed.

---

# 10. The Hard Truth

Most digital canons are:

- locked behind markup
- hard to parse
- too heavy for casual access
- intimidating for new developers

KIT-2920 lowers the barrier.

Not by simplifying the canon.

But by simplifying access.

---

# 11. Future Possibilities

- Clean PDF export
- EPUB generation
- Parallel script alignment
- Minimal web viewer
- Corpus API layer
- Zenodo DOI snapshot
- Academic citation pack

---

# 12. Final Note

The canon does not need redesign.

It needs passage.

If XML is the archive layer,
KIT-2920 is the transit layer.

If SAT is the structure,
KIT-2920 is the bridge.

If CBETA is the preservation,
KIT-2920 is the distribution.

---

# End
