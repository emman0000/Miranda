"""
run_pipeline.py

Runs the complete data preparation pipeline for Miranda.

Pipeline:
1. Load raw dataset
2. Clean dataset
3. Balance categories
4. Preprocess dataset
5. Save final processed dataset
"""

from pathlib import Path

from src.data.load_dataset import load_dataset
from src.data.clean_dataset import clean_dataset
from src.data.balance_dataset import balance_dataset
from src.data.preprocess_dataset import preprocess_dataset


# -----------------------------
# Paths
# -----------------------------

RAW_DATASET = Path("data/raw/styles.csv")
IMAGE_FOLDER = Path("data/raw/images")
OUTPUT_DATASET = Path("data/processed/miranda_dataset.csv")


def main():

    print("=" * 50)
    print("Starting Miranda Data Pipeline")
    print("=" * 50)

    # -----------------------------
    # Load
    # -----------------------------
    print("\n[1/4] Loading dataset...")

    df = load_dataset(RAW_DATASET)

    print(f"Loaded {len(df):,} products.")

    # -----------------------------
    # Clean
    # -----------------------------
    print("\n[2/4] Cleaning dataset...")

    df = clean_dataset(df, IMAGE_FOLDER)

    print(f"Remaining products: {len(df):,}")

    # -----------------------------
    # Balance
    # -----------------------------
    print("\n[3/4] Balancing dataset...")

    df = balance_dataset(df)

    print(f"Balanced dataset size: {len(df):,}")

    # -----------------------------
    # Preprocess
    # -----------------------------
    print("\n[4/4] Preprocessing dataset...")

    df = preprocess_dataset(df)

    # -----------------------------
    # Save
    # -----------------------------
    OUTPUT_DATASET.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(OUTPUT_DATASET, index=False)

    print("\nPipeline completed successfully!")
    print(f"Processed dataset saved to:\n{OUTPUT_DATASET}")


if __name__ == "__main__":
    main()
