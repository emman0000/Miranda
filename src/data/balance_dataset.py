"""
balance_dataset.py

Curates the cleaned fashion dataset by:
1. Keeping only supported fashion article types.
2. Limiting overrepresented categories using predefined caps.

This helps reduce representation bias during retrieval and creates
a balanced knowledge base for Miranda.
"""

import pandas as pd

# --------------------------------------------------
# Fashion categories supported by Miranda
# --------------------------------------------------

SELECTED_ARTICLES = [
    # Tops
    "Tshirts",
    "Shirts",
    "Tops",
    "Kurtas",
    "Kurtis",
    "Tunics",
    "Sweatshirts",
    "Sweaters",
    "Jackets",

    # Bottoms
    "Jeans",
    "Trousers",
    "Shorts",
    "Track Pants",

    # Dresses
    "Dresses",
    "Sarees",

    # Footwear
    "Casual Shoes",
    "Sports Shoes",
    "Formal Shoes",
    "Heels",
    "Flats",
    "Sandals",
    "Flip Flops"
]

# --------------------------------------------------
# Maximum samples per article type
# --------------------------------------------------

CATEGORY_CAPS = {
    "Tshirts": 500,
    "Shirts": 500,
    "Casual Shoes": 500,
    "Sports Shoes": 500,
    "Kurtas": 500,
    "Tops": 500,
    "Heels": 400,
    "Flip Flops": 300,
    "Sandals": 300,
    "Formal Shoes": 300,
    "Jeans": 500,
    "Shorts": 400,
    "Trousers": 400,
    "Flats": 300,
}


def balance_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Balance the dataset by filtering supported article types
    and limiting overrepresented categories.

    Args:
        df (pd.DataFrame): Cleaned fashion dataset.

    Returns:
        pd.DataFrame: Balanced dataset.
    """

    # Keep only categories Miranda supports
    df = df[df["articleType"].isin(SELECTED_ARTICLES)]

    balanced_groups = []

    # Apply category caps
    for article, group in df.groupby("articleType"):

        limit = CATEGORY_CAPS.get(article)

        if limit is not None:
            group = group.sample(
                n=min(len(group), limit),
                random_state=42
            )

        balanced_groups.append(group)

    balanced_df = (
        pd.concat(balanced_groups)
        .sample(frac=1, random_state=42)
        .reset_index(drop=True)
    )

    return balanced_df


if __name__ == "__main__":

    from load_dataset import load_dataset

    df = load_dataset()
    balanced_df = balance_dataset(df)

    print(f"Original dataset: {len(df)} rows")
    print(f"Balanced dataset: {len(balanced_df)} rows")
    print("\nCategory distribution:\n")
    print(balanced_df["articleType"].value_counts())
