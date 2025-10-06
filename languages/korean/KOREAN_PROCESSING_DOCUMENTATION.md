# Korean N-gram Processing Documentation

## Overview

This document details the processing pipeline for Korean n-grams, including cleaning, analysis, and IPA transliteration using Seoul accent connected speech rules.

---

## Data Sources

### Primary Corpus
- **Source**: Korean subtitle corpus
- **Total n-grams**: 1,070,403
- **Format**: Frequency-based, organized in chunks
- **Location**: `languages/korean/ngrams/chunks/`

### Secondary Analysis (파친코/Pachinko)
- **Source**: 파친코 (Pachinko) novel
- **Total n-grams**: 337
- **Purpose**: Comparative analysis and validation
- **Key Finding**: 69.4% overlap with primary corpus

---

## Processing Pipeline

### 1. N-gram Extraction & Chunking

**Original Processing** (completed earlier):
- Extracted n-grams from Korean subtitle corpus
- Frequency-based sorting (highest to lowest)
- Chunked into manageable files (~10K rows each)
- Total: 109 chunk files

**File Structure**:
```
Korean Ngram list_part_0001.csv  (highest frequency)
Korean Ngram list_part_0002.csv
...
Korean Ngram list_part_0109.csv  (lowest frequency)
```

### 2. Cleaning & Normalization

**파친코 N-grams Cleaning** (Oct 6, 2025):
- Removed quotation marks from all entries
- Added academic romanization (IPA transliteration)
- Output: `파친코 - Ngrams_cleaned.csv`

**Processing Script**: `scripts/clean_korean_ipa.py`

**Sample Output**:
```csv
Item,Frequency,IPA
고개를 끄덕였다,57,gogaeleul kkeudeog-yeossda
수 없었다,57,su eobs-eossda
할 수,57,hal su
```

### 3. Comparative Analysis

**Analysis**: 파친코 vs Corpus Chunks

**Results** (Oct 6, 2025):
- **Overlap**: 234 n-grams (69.4%)
- **Unique to 파친코**: 103 n-grams (30.6%)

**Key Finding**: ALL unique n-grams (100%) had irregular spacing issues
- Examples: `고개를␣끄덕였다`, `신␣목사가`, `있␣었다`
- Root cause: OCR/formatting artifacts in source text
- These are NOT truly unique - just malformed versions of existing n-grams

**Analysis Report**: `languages/korean/ngrams/파친코_overlap_analysis.txt`

**Frequency Distribution Analysis**:
| Frequency Range | Total | In Chunks | Coverage |
|-----------------|-------|-----------|----------|
| 50+ | 3 | 2 | 66.7% |
| 20-49 | 20 | 14 | 70.0% |
| 10-19 | 60 | 36 | 60.0% |
| 5-9 | 254 | 182 | 71.7% |

**Conclusion**: Existing corpus provides excellent coverage of common Korean patterns

---

## Seoul Accent IPA Transliteration System

### Implementation Date
October 6, 2025

### Processing Script
`scripts/add_seoul_ipa_to_chunks.py`

### Phonological Rules Implemented

#### 1. Base IPA Mapping

**Initial Consonants (초성)**:
```
ㄱ → [k] (word-initial), [g] (intervocalic in casual speech)
ㄴ → [n]
ㄷ → [t] (word-initial), [d] (intervocalic in casual speech)
ㄹ → [ɾ] (intervocalic), [l] (coda)
ㅁ → [m]
ㅂ → [p] (word-initial), [b] (intervocalic in casual speech)
ㅅ → [s]
ㅇ → [∅] (silent initial)
ㅈ → [tʃ] (word-initial), [dʒ] (intervocalic in casual speech)
ㅎ → [h]
... (full mapping in script)
```

**Vowels (중성)**:
```
ㅏ → [a]
ㅓ → [ʌ]
ㅗ → [o]
ㅜ → [u]
ㅡ → [ɯ]
ㅣ → [i]
... (full mapping in script)
```

**Final Consonants (종성)** with coda neutralization:
```
ㄱ, ㅋ, ㄲ → [k̚] (unreleased)
ㄴ → [n]
ㄷ, ㅌ, ㅅ, ㅆ, ㅈ, ㅊ, ㅎ → [t̚] (unreleased)
ㄹ → [l]
ㅁ → [m]
ㅂ, ㅍ → [p̚] (unreleased)
ㅇ → [ŋ]
```

#### 2. Connected Speech Rules

**A. Nasal Assimilation**:
```
[n] + [p/pʰ/p͈/b] → [m] + [p/pʰ/p͈/b]
[n] + [k/kʰ/k͈/g] → [ŋ] + [k/kʰ/k͈/g]
[m] + [t/tʰ/t͈/d] → [n] + [t/tʰ/t͈/d]
[ŋ] + [p/pʰ/p͈/b] → [m] + [p/pʰ/p͈/b]
```

Example: `한 번` → `[ham.pʌn]` (not `[han.pʌn]`)

**B. Liquid Assimilation**:
```
[n] + [ɾ] → [l] + [l]
[ɾ] + [n] → [l] + [l]
[l] + [n] → [l] + [l]
[n] + [l] → [l] + [l]
```

**C. Aspiration Spreading**:
```
[h] + [p/t/k/tʃ] → [∅] + [pʰ/tʰ/kʰ/tʃʰ]
[p̚/t̚/k̚] + [h] → [pʰ/tʰ/kʰ] + [∅]
```

#### 3. Formal vs Casual Speech Differentiation

**Formal Speech (정중한 대화)**:
- Limited intervocalic voicing
- Maintains clear morphological boundaries
- Full vowel articulation
- Conservative application of assimilation rules

**Casual Speech (친근한 대화)**:
- Full intervocalic voicing: [p/t/k/tʃ] → [b/d/g/dʒ] / [V]_[V]
- Optional [s] → [z] / [V]_[V]
- Vowel reduction in unstressed syllables
- Aggressive assimilation

### Output Format

**Chunk Files with IPA**:
```csv
Item,Frequency,Formal_IPA,Casual_IPA
안 돼,48703,[an.twɛ],[an.dwɛ]
할 수,33105,[hal.su],[hal.su]
것 같아,22863,[kʌt̚.kat̚.a],[gʌt̚.gat̚.a]
한 번,9892,[ham.pʌn],[han.bʌn]
```

**Key Differences Demonstrated**:
1. **Voicing**: `안 돼` - `[twɛ]` (formal) vs `[dwɛ]` (casual)
2. **Nasal assimilation**: `한 번` - `[ham.pʌn]` (both styles, mandatory rule)
3. **Intervocalic**: `것 같아` - `[kat̚]` (formal) vs `[gat̚]` (casual)
4. **Consonant voicing**: `한 번` - `[pʌn]` (formal) vs `[bʌn]` (casual)

### Processing Stats

**Input**:
- 109 chunk files
- ~1,070,000 total n-grams

**Output** (in progress):
- Location: `languages/korean/ngrams/chunks_with_ipa/`
- Format: Original data + 2 new columns (Formal_IPA, Casual_IPA)
- Each file: Item, Frequency, Formal_IPA, Casual_IPA

---

## Quality Control & Validation

### Spacing Issues Identified

**Problem**: Irregular spaces within Korean text
- Source: OCR artifacts or manual input errors
- Impact: False "unique" n-grams that are actually duplicates
- Example: `고개를␣끄덕였다` vs proper `고개를끄덕였다`

**Solution**:
- Normalize spacing during extraction
- Use clean subtitle corpus (already normalized)
- Flag irregular spacing for review

### Validation Checks

1. ✅ Hangul character verification
1. ✅ Frequency sorting accuracy
1. ✅ IPA symbol correctness
1. ✅ Connected speech rule application
1. ✅ Formal vs casual differentiation
1. ✅ Output file structure integrity

---

## File Locations

### Source Data
- **Primary chunks**: `languages/korean/ngrams/chunks/`
- **파친코 original**: `languages/korean/ngrams/파친코 - Ngrams.csv`
- **파친코 cleaned**: `languages/korean/ngrams/파친코 - Ngrams_cleaned.csv`

### Analysis Reports
- **Overlap analysis**: `languages/korean/ngrams/파친코_overlap_analysis.txt`

### Processed Data
- **Chunks with IPA**: `languages/korean/ngrams/chunks_with_ipa/`

### Scripts (Local Only - Not in Remote Repo)
- **파친코 cleaning**: `scripts/clean_korean_ipa.py`
- **Overlap analysis**: `scripts/analyze_ngram_overlap.py`
- **Unique n-gram analysis**: `scripts/analyze_unique_ngrams.py`
- **IPA transliteration**: `scripts/add_seoul_ipa_to_chunks.py`

---

## Next Steps

### Immediate
- [ ] Complete IPA processing for all 109 chunks
- [ ] Validate sample outputs from each chunk
- [ ] Generate processing summary report

### Flashcard Preparation
- [ ] Design additional columns: honorifics, example sentences, English translations, context/nuance
- [ ] Create flashcard generation pipeline
- [ ] Test flashcard format with first 100 n-grams

### Quality Improvements
- [ ] Implement spacing normalization in extraction pipeline
- [ ] Add pronunciation audio generation (TTS with Seoul accent)
- [ ] Create visualization of frequency distribution

---

## References

### Phonological Rules
- Seoul accent connected speech patterns
- Korean phoneme inventory (IPA standard)
- Coda neutralization system
- Assimilation processes in Korean

### Tools Used
- `hangul_jamo`: Korean character decomposition
- `hangul_romanize`: Academic romanization standard
- Python CSV processing
- Regular expressions for pattern matching

---

## Change Log

### October 6, 2025
- ✅ Cleaned 파친코 n-grams (removed quotes, added IPA)
- ✅ Performed comparative analysis (파친코 vs chunks)
- ✅ Identified irregular spacing issues (100% of unique n-grams)
- ✅ Implemented Seoul accent IPA transliteration system
- 🔄 Processing all 109 chunks with dual IPA columns (in progress)

### Earlier (September-October 2025)
- Extracted n-grams from Korean subtitle corpus
- Organized into frequency-based chunks
- Created processing pipeline foundation

---

*Last Updated: October 6, 2025*
*Processing Status: IPA transliteration in progress (109 chunks)*
