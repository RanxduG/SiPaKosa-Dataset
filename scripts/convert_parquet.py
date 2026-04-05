import pandas as pd
from pathlib import Path

for lang in ['sinhala', 'mixed']:
    for split in ['train', 'validation', 'test']:
        csv_path = Path(f"data/{lang}/{split}.csv")
        parquet_path = Path(f"data/{lang}/{split}.parquet")
        
        df = pd.read_csv(csv_path, encoding='utf-8-sig')
        df.to_parquet(parquet_path, index=False)
        print(f"✓ {lang}/{split}.parquet saved ({len(df):,} rows)")