"""
SiPaKosa Dataset Loading Utilities
"""

def load_sipakosa(filepath, encoding='utf-8'):
    """
    Load SiPaKosa corpus file.
    
    Args:
        filepath: Path to .txt file
        encoding: Text encoding (default: utf-8)
        
    Returns:
        List of sentences
    """
    with open(filepath, 'r', encoding=encoding) as f:
        sentences = [line.strip() for line in f if line.strip()]
    return sentences


def load_split(corpus_type='sinhala', split='train'):
    """
    Load a specific corpus split.
    
    Args:
        corpus_type: 'sinhala', 'mixed', or 'pali'
        split: 'train', 'validation', or 'test'
        
    Returns:
        List of sentences
    """
    filepath = f'data/{corpus_type}/{split}.txt'
    return load_sipakosa(filepath)


if __name__ == '__main__':
    # Example usage
    train = load_split('pali', 'train')
    print(f"Loaded {len(train):,} training sentences")