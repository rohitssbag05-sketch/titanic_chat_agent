

import pandas as pd
from pathlib import Path

class DataLoader:
    _df = None

    @classmethod
    def get_dataframe(cls):
        if cls._df is None:
            # Go from:
            # backend/app/services/data_loader.py
            # up to project root
            BASE_DIR = Path(__file__).resolve().parents[3]

            data_path = BASE_DIR / "data" / "titanic.csv"
            print(f"Loading Titanic dataset from: {data_path}")

            if not data_path.exists():
                raise FileNotFoundError(
                    f"Titanic CSV not found at: {data_path}"
                )

            cls._df = pd.read_csv(data_path)

        return cls._df