# SiPaKosa: Sinhala-Pali Buddhist Corpus

**[ANONYMOUS SUBMISSION - Under Review]**

A comprehensive corpus of canonical and classical Buddhist texts in Sinhala and Pali, compiled from historical archives and web-scraped canonical scriptures.

## 📊 Dataset Statistics

- **Total Sentences**: 786,839
- **Sinhala Sentences**: 465,539 (59.2%)
- **Mixed Sinhala-Pali**: 320,805 (40.8%)
- **Pali Sentences**: 495 (0.1%)
- **Sources**: 16 historical books + 5 Nikayas (Tripitaka)
- **Time Period**: Late 19th - mid 20th century

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