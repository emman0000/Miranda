
import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/processed/fashion_dataset.csv")


def load_dataset(path=DATA_PATH):
    """
    Load the processed fashion dataset.

    Args:
        path (str | Path): Path to the dataset.

    Returns:
        pd.DataFrame
    """

    if not Path(path).exists():
        raise FileNotFoundError(f"Dataset not found: {path}")

    return pd.read_csv(path)


if __name__ == "__main__":
    df = load_dataset()

    print("Dataset loaded successfully.")
    print(df.shape)
