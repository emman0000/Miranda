
from pathlib import Path
import os

import pandas as pd


# -----------------------------
# Configuration
# -----------------------------

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
    "Flip Flops",
]


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


def clean_dataset(df: pd.DataFrame, image_folder: str) -> pd.DataFrame:
    """
    Clean and curate the fashion dataset for Miranda.
    """

    # Keep only apparel and footwear
    df = df[df["masterCategory"].isin(["Apparel", "Footwear"])]

    # Remove missing values
    df = df.dropna()

    # Remove duplicate products
    df = df.drop_duplicates(subset="id")

    # Keep only supported article types
    df = df[df["articleType"].isin(SELECTED_ARTICLES)]

    # Balance categories
    balanced = []

    for article, group in df.groupby("articleType"):

        if article in CATEGORY_CAPS:

            balanced.append(
                group.sample(
                    n=min(len(group), CATEGORY_CAPS[article]),
                    random_state=42
                )
            )

        else:
            balanced.append(group)

    df = pd.concat(balanced, ignore_index=True)

    # Keep only products with images
    df["image_exists"] = df["id"].apply(
        lambda x: os.path.exists(
            Path(image_folder) / f"{x}.jpg"
        )
    )

    df = (
        df[df["image_exists"]]
        .drop(columns="image_exists")
    )

    # Remove unnecessary column
    if "year" in df.columns:
        df = df.drop(columns="year")

    return df
