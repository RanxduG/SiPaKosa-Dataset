# SiPaKosa Dataset Card

## Dataset Description

- **Homepage**: [Will be added after review]
- **Repository**: [This anonymous repository]
- **Paper**: [Anonymous submission under review]
- **Point of Contact**: [Will be added after review]

## Dataset Summary

SiPaKosa is a large-scale corpus of Sinhala Buddhist literature comprising 786,839 sentences from two complementary sources:

1. **Historical Archives**: 16 copyright-cleared books (247,513 sentences)
2. **Web-scraped Canonical Texts**: Complete Tripitaka Sutta Pitaka (539,326 sentences)

## Supported Tasks

- Language Modeling
- Text Classification
- Information Retrieval
- Question Answering
- Machine Translation (Sinhala-Pali)
- Code-switching Analysis

## Languages

- Sinhala (sin)
- Pali (pli)
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
- `book_metadata.csv`: Book-level information
- `page_metadata.csv`: Page-level OCR confidence and language classification
- `corpus_manifest.json`: Complete corpus provenance

### Data Splits

|       | Train   | Validation | Test   |
|-------|---------|------------|--------|
| Sinhala | 80% | 10% | 10% |
| Mixed   | 80% | 10% | 10% |


## Dataset Creation

### Source Data

#### Historical Archives
- **Source**: IFBCnet Library (Internet Archive)
- **Copyright**: Public domain (70-year rule)
- **Processing**: OCR with Google Document AI (99.8% retention)

#### Canonical Texts
- **Source**: tripitaka.online
- **Coverage**: 5 Nikayas of Sutta Pitaka
- **Processing**: Web scraping with structural metadata preservation

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
- Digital humanities research
- Educational applications
- Low-resource NLP advancement

### Other Known Limitations

- OCR errors in degraded historical documents
- Variable orthographic standards across centuries
- Code-switching complexity in mixed texts

## Additional Information

### Dataset Curators

[Anonymous for review]

### Licensing Information

- **Corpus**: CC-BY-4.0
- **Code**: MIT License

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

### Contributions

[Will be added after review]
