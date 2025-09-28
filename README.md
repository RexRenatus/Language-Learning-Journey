# Language Learning Journey - Multilingual N-grams

Purpose: curated n-gram datasets per language for personal language learning and analysis.

Repository URL: https://github.com/RexRenatus/Language-Learning-Journey

Directory layout

languages/
├─ korean/
│  ├─ source/
│  │  └─ Korean Ngram list.csv
│  ├─ ngrams/
│  │  ├─ chunks/            ← 10k-row chunks from the source
│  │  └─ clean/             ← Korean-only rows, no quotes
│  └─ reports/              ← split/clean validation reports
├─ spanish/
│  ├─ source/               (.gitkeep)
│  ├─ ngrams/
│  │  ├─ chunks/            (.gitkeep)
│  │  └─ clean/             (.gitkeep)
│  └─ reports/              (.gitkeep)
└─ mandarin/
   ├─ source/               (.gitkeep)
   ├─ ngrams/
   │  ├─ chunks/            (.gitkeep)
   │  └─ clean/             (.gitkeep)
   └─ reports/              (.gitkeep)

scripts/
└─ clean_korean.ps1         ← cleaning pipeline for Korean chunks

Journal_Entries/            ← personal notes (kept as-is)

Korean data details

- Source CSV: languages/korean/source/Korean Ngram list.csv
- Chunked (10k each): languages/korean/ngrams/chunks/
- Cleaned (Korean-only, no quotes): languages/korean/ngrams/clean/
- Reports:
  - split_report.csv (moved to chunks/)
  - clean_report.csv
  - validation_summary.txt
  - FINAL_REPORT.txt

Processing scripts

- scripts/clean_korean.ps1
  - Splits by header-aware parsing, keeps rows containing Hangul (and no A–Z), removes quotes, writes clean CSVs
  - Produces per-file and overall validation reports

How to add a new language (example: Spanish)

1) Put your raw source CSV(s) under: languages/spanish/source/
2) Split into 10k chunks (PowerShell example uses the Korean script as a template)
3) Copy clean_korean.ps1 to a new script (e.g., clean_spanish.ps1) and adjust the regex to Spanish rules if needed
4) Write outputs to:
   - languages/spanish/ngrams/chunks/
   - languages/spanish/ngrams/clean/
   - languages/spanish/reports/
5) Commit and push:
   - git add .
   - git commit -m "feat(es): add Spanish n-grams"
   - git push origin main

Notes on validation

- Each cleaned CSV should contain only language-appropriate characters and have no quotes in data cells.
- Validation summaries aggregate size checks and quote/ASCII checks.

Roadmap

- Generalize the cleaning script to a parameterized tool that accepts:
  - input directory, language regex, ascii exclusion rules, output directory
- Add CI to validate new datasets on PRs (GitHub Actions)
- Add README files per language explaining data source and processing notes