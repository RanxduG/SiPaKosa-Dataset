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
  - config_name: sinhala
    data_files:
      - split: train
        path: data/sinhala/train.txt
      - split: validation
        path: data/sinhala/validation.txt
      - split: test
        path: data/sinhala/test.txt
  - config_name: mixed
    data_files:
      - split: train
        path: data/mixed/train.txt
      - split: validation
        path: data/mixed/validation.txt
      - split: test
        path: data/mixed/test.txt
---

# SiPaKosa: Sinhala-Pali Buddhist Corpus

A comprehensive corpus of canonical and classical Buddhist texts in Sinhala and Pali, compiled from historical archives and web-scraped canonical scriptures.

## Dataset Statistics

- **Total Sentences**: 786,344
- **Sinhala Sentences**: 465,539 (59.2%)
- **Mixed Sinhala-Pali**: 320,805 (40.8%)
- **Sources**: 16 historical books + 5 Nikayas (Tripitaka)

## Dataset Structure
```
data/
├── sinhala/          # Pure Sinhala corpus
└── mixed/             # Language Mix Sinhala-Pali
```

## Metadata Structure

The `metadata/` folder contains two sub-folders: `pdf/` and `tripitaka/`.

### `metadata/pdf/`

Holds statistics and manifest data for the 16 digitised Buddhist books in the PDF corpus.

- `corpus_manifest.json` — lists each book with its name (Sinhala and English), category, and file paths.
- `corpus_statistics.json` — high-level summary: total books (16), total pages (7,064), language split (Sinhala vs. mixed), and category distribution.
- `detailed_corpus_statistics.json` — per-book and per-category breakdown including word counts, character counts, and averages per page. Covers three categories: `books-related-to-the-tipitaka`, `old-books`, and `buddhist-characters`.

### `metadata/tripitaka/`

Contains scraped sutta data from [tripitaka.online](https://tripitaka.online), organised by nikāya (collection). Each nikāya has its own sub-folder (e.g., `digha/`, `majjhima/`, `anguttara/`).

Inside each sub-folder:

- `suttas_batch_{number}.json` — batched sutta records. Each entry contains the URL, title, Sinhala content, Pali content, word counts, nikāya info, scraping method, and timestamp.
- `error_log.json` — records any suttas that failed to scrape (e.g., pages with no Sinhala or Pali content found).
- `scraping_progress.json` — tracks how many suttas were scraped vs. errored, along with start time and last update timestamp.

## Quick Start
```python
# Load the dataset
from datasets import load_dataset

# Load Sinhala training set
train_ds = load_dataset("RaniduG/SiPaKosa", "mixed")
print(train_ds["train"][0])

# Load mixed training set
mixed_ds = load_dataset("RaniduG/SiPaKosa", "mixed")
print(mixed_ds["train"][0])
```

## Documentation

- [Dataset Card](docs/DATASET_CARD.md) - Detailed documentation
- [Citation](docs/CITATION.bib) - How to cite this work

## License

This dataset is released under MIT for research purposes.

## Paper

**https://arxiv.org/abs/2603.29221**
