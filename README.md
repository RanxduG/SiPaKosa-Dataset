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

**[ANONYMOUS SUBMISSION - Under Review]**

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
├── mixed/            # Language Mix Sinhala-Pali
└── pali/             # Pure Pali corpus
```

## 🚀 Quick Start
```python
# Load the dataset
from scripts.load_dataset import load_sipakosa

# Load Sinhala training set
train_data = load_sipakosa('data/sinhala/train.txt')

# Load mixed corpus
mixed_data = load_sipakosa('data/mixed/train.txt')
```

## 📖 Documentation

- [Dataset Card](docs/DATASET_CARD.md) - Detailed documentation
- [Evaluation Guide](docs/EVALUATION.md) - Reproduce baseline results
- [Citation](docs/CITATION.bib) - How to cite this work

## 📜 License

This dataset is released under MIT for research purposes.

## 🔗 Paper

**[Anonymous Submission - Link will be added after review]**

## ⚠️ Note

This repository is anonymized for double-blind review. Author information and institutional affiliations have been removed.
