---
license: mit
task_categories:
  - text-generation
  - text-classification
language:
  - si
pretty_name: SiPaKosa
size_categories:
  - 100K<n<1M
configs:
  - config_name: sinhala_metadata
    data_files:
      - split: train
        path: data/sinhala/train.csv
      - split: validation
        path: data/sinhala/validation.csv
      - split: test
        path: data/sinhala/test.csv
  - config_name: mixed_metadata
    data_files:
      - split: train
        path: data/mixed/train.csv
      - split: validation
        path: data/mixed/validation.csv
      - split: test
        path: data/mixed/test.csv
---

# SiPaKosa: Sinhala-Pali Buddhist Corpus

A comprehensive corpus of canonical and classical Buddhist texts in Sinhala and Pali, compiled from historical archives and web-scraped canonical scriptures.

## Dataset Statistics

- **Total Sentences**: 786,344
- **Sinhala Sentences**: 465,539 (59.2%)
- **Mixed Sinhala-Pali**: 320,805 (40.8%)
- **Sources**: 16 historical books (IFBC) + 5 Nikayas (Tripitaka)

## Dataset Configs

There are four configs available:

| Config | Format | Columns | Best for |
|---|---|---|---|
| `sinhala` | txt | text only | model training |
| `mixed` | txt | text only | model training |
| `sinhala_metadata` | csv | sentence_id, book_category, book_name_si, book_name_en, source, text, language | filtering by book or source |
| `mixed_metadata` | csv | sentence_id, book_category, book_name_si, book_name_en, source, text, language | filtering by book or source |

## Dataset Structure

```
data/
├── sinhala/
│   ├── train.txt
│   ├── train.csv
│   ├── validation.txt
│   ├── validation.csv
│   ├── test.txt
│   └── test.csv
└── mixed/
    ├── train.txt
    ├── train.csv
    ├── validation.txt
    ├── validation.csv
    ├── test.txt
    └── test.csv
```

## CSV Columns

| Column | Description | Example |
|---|---|---|
| `sentence_id` | Globally unique sentence ID | 1 |
| `book_category` | Category of the source book | books-related-to-the-tipitaka |
| `book_name_si` | Sinhala book name (IFBC only) | විශුද්ධිමාර්ගය |
| `book_name_en` | English book name (Tripitaka only) | Digha Nikaya |
| `source` | Data source | IFBC or Tripitaka |
| `text` | The sentence | මා හට අසන්නට ලැබුණේ... |
| `language` | Language classification | sinhala or mixed |

## Metadata Structure

The `metadata/` folder contains two sub-folders: `pdf/` and `tripitaka/`.

### `metadata/pdf/`

Holds statistics and manifest data for the 16 digitised Buddhist books in the PDF corpus.

- `corpus_manifest.json` — lists each book with its name (Sinhala and English), category, and file paths.
- `corpus_statistics.json` — high-level summary: total books (16), total pages (7,064), language split (Sinhala vs. mixed), and category distribution.
- `detailed_corpus_statistics.json` — per-book and per-category breakdown including word counts, character counts, and averages per page. Covers three categories: `books-related-to-the-tipitaka`, `old-books`, and `buddhist-characters`.

### `metadata/tripitaka/`

Contains scraped sutta data from [tripitaka.online](https://tripitaka.online), organised by nikaya. Each nikaya has its own sub-folder (e.g., `digha/`, `majjhima/`, `anguttara/`).

Inside each sub-folder:

- `suttas_batch_{number}.json` — batched sutta records. Each entry contains the URL, title, Sinhala content, Pali content, word counts, nikaya info, scraping method, and timestamp.
- `error_log.json` — records any suttas that failed to scrape.
- `scraping_progress.json` — tracks how many suttas were scraped vs. errored.

## Quick Start
```python
from datasets import load_dataset

# Load plain text for model training
sinhala_ds = load_dataset("RaniduG/SiPaKosa", "sinhala")
print(sinhala_ds["train"][0])

mixed_ds = load_dataset("RaniduG/SiPaKosa", "mixed")
print(mixed_ds["train"][0])

# Load with metadata for filtering by book or source
sinhala_meta = load_dataset("RaniduG/SiPaKosa", "sinhala_metadata")
print(sinhala_meta["train"][0])

# Filter by source
import pandas as pd
df = pd.DataFrame(sinhala_meta["train"])
ifbc_only = df[df["source"] == "IFBC"]
tripitaka_only = df[df["source"] == "Tripitaka"]

# Filter by book
book_df = df[df["book_name_si"] == "විශුද්ධිමාර්ගය"]
```

## Documentation

- [Citation](docs/CITATION.bib) - How to cite this work

## License

This dataset is released under MIT for research purposes.

## Paper

**https://arxiv.org/abs/2603.29221**
