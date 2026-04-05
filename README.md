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

## 📊 Dataset Statistics

- **Total Sentences**: 786,344
- **Sinhala Sentences**: 465,539 (59.2%)
- **Mixed Sinhala-Pali**: 320,805 (40.8%)
- **Sources**: 16 historical books + 5 Nikayas (Tripitaka)

## 📁 Dataset Structure
```
data/
├── sinhala/          # Pure Sinhala corpus
└── mixed/             # Language Mix Sinhala-Pali
```

## 🚀 Quick Start
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
