
"""
preprocess_dataset.py

Creates a text representation of every product that will later
be converted into embeddings for semantic search.
"""

import pandas as pd


TEXT_COLUMNS = [
    "productDisplayName",
    "gender",
    "masterCategory",
    "subCategory",
    "articleType",
    "baseColour",
    "season",
    "usage",
]


def create_product_text(row):
    """
    Combine important product attributes into one descriptive string.
    """

    fields = []

    mapping = {
        "productDisplayName": "Product",
        "gender": "Gender",
        "masterCategory": "Category",
        "subCategory": "Subcategory",
        "articleType": "Article Type",
        "baseColour": "Colour",
        "season": "Season",
        "usage": "Usage",
    }

    for column in TEXT_COLUMNS:

        value = row.get(column)

        if pd.notna(value):
            fields.append(f"{mapping[column]}: {value}")

    return ". ".join(fields)


def preprocess_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create an embedding text column.

    Args:
        df: Balanced dataset.

    Returns:
        DataFrame with an additional 'embedding_text' column.
    """

    df = df.copy()

    df["embedding_text"] = df.apply(
        create_product_text,
        axis=1
    )

    return df


if __name__ == "__main__":

    from load_dataset import load_dataset
    from balance_dataset import balance_dataset

    df = load_dataset()
    df = balance_dataset(df)
    df = preprocess_dataset(df)

    print(df[["productDisplayName", "embedding_text"]].head())
