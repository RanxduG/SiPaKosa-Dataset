# SiPaKosa Dataset Card

## Dataset Description
- **Repository**: https://github.com/RanxduG/SiPaKosa-Dataset
- **Paper**: https://arxiv.org/abs/2603.29221
- **Point of Contact**: ranidu.20222198@iit.ac.lk

## Dataset Summary

SiPaKosa is a large-scale corpus of Sinhala Buddhist literature comprising 786,344 sentences from two complementary sources:

1. **Historical Archives**: 16 copyright-cleared books
2. **Web-scraped Canonical Texts**: Complete Tripitaka Sutta Pitaka (5 Nikayas)

## Supported Tasks
- Language Modeling
- Text Classification
- Information Retrieval
- Question Answering
- Machine Translation (Sinhala-Pali)
- Code-switching Analysis

## Languages
- Sinhala (`si`)
- Pali (`pli`)
- Mixed Sinhala-Pali (code-switched)

## Dataset Structure

### Data Instances

Example from `sinhala/train.txt`:
```
බුද්ධ ධර්මය ත්‍රිපිටකයෙහි සංග්‍රහ වී ඇත.
```

Example from `mixed/train.txt`:
```
සබ්බං දුක්ඛං යන පාලි වචනයෙහි අර්ථය සියල්ල දුකයි යන්නයි.
```

### Data Fields

Each `.txt` file contains one sentence per line in UTF-8 encoding.

Metadata files contain:
- `corpus_manifest.json`: Complete corpus provenance (book names, categories, file paths)
- `corpus_statistics.json`: High-level summary of pages, language split, and category distribution
- `detailed_corpus_statistics.json`: Per-book and per-category breakdown with word and character counts

### Data Splits

|         | Train | Validation | Test |
|---------|-------|------------|------|
| Sinhala | 80%   | 10%        | 10%  |
| Mixed   | 80%   | 10%        | 10%  |

### Configs
```python
# Load Sinhala config
from datasets import load_dataset
ds = load_dataset("RaniduG/SiPaKosa", "sinhala")

# Load Mixed config
ds = load_dataset("RaniduG/SiPaKosa", "mixed")
```

### Corpus Statistics

| Split | Sentences | Percentage |
|-------|-----------|------------|
| Sinhala | 465,539 | 59.2% |
| Mixed Sinhala-Pali | 320,805 | 40.8% |
| **Total** | **786,344** | **100%** |

### File Structure
```
data/
├── sinhala/
│   ├── train.txt
│   ├── validation.txt
│   └── test.txt
└── mixed/
├── train.txt
├── validation.txt
└── test.txt
metadata/
├── pdf/
│   ├── corpus_manifest.json
│   ├── corpus_statistics.json
│   └── detailed_corpus_statistics.json
└── tripitaka/
├── digha/
│   ├── suttas_batch_0001.json
│   ├── error_log.json
│   └── scraping_progress.json
├── majjhima/
├── anguttara/
├── samyutta/
└── khuddaka/
```

## Dataset Creation

### Source Data

#### Historical Archives (PDF)
- **Source**: IFBCnet Library (Internet Archive)
- **Coverage**: 16 digitised Buddhist books
- **Copyright**: Public domain (70-year rule)
- **Processing**: OCR with Google Document AI (99.8% retention)
- **Categories**: Books related to the Tipitaka, Old Books, Buddhist Characters
- **Total Pages**: 7,064

#### Canonical Texts (Tripitaka)
- **Source**: [tripitaka.online](https://tripitaka.online)
- **Coverage**: 5 Nikayas of the Sutta Pitaka (Digha, Majjhima, Samyutta, Anguttara, Khuddaka)
- **Processing**: Web scraping with structural metadata preservation
- **Format**: Each sutta stored with URL, title, Sinhala content, Pali content, word counts, nikāya info, and timestamp

### Annotations

#### Language Classification
- Automated lexicon-based classification
- 70% confidence threshold
- Categories: Sinhala, Pali, Mixed

### Personal and Sensitive Information

This dataset contains religious and philosophical texts from public domain sources. No personal or sensitive information is included.

## Considerations for Using the Data

### Social Impact

This dataset preserves Sinhala Buddhist cultural heritage and enables:
- Digital humanities research on canonical Buddhist literature
- Educational applications for Sinhala and Pali language learning
- Low-resource NLP advancement for the Sinhala language

### Other Known Limitations
- OCR errors may be present in degraded historical documents
- Variable orthographic standards across centuries in historical texts
- Code-switching complexity in mixed Sinhala-Pali texts
- Some suttas may have been skipped during scraping where no Sinhala or Pali content was found (logged in `error_log.json`)

## Additional Information

### Dataset Curators
Ranidu Gurusinghe
Nevidu Jayatilleke


### Licensing Information
- **Corpus**: MIT License

### Citation Information
```bibtex
@misc{gurusinghe2026sipakosacomprehensivecorpuscanonical,
      title={SiPaKosa: A Comprehensive Corpus of Canonical and Classical Buddhist Texts in Sinhala and Pali}, 
      author={Ranidu Gurusinghe and Nevidu Jayatilleke},
      year={2026},
      eprint={2603.29221},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2603.29221}, 
}
```
