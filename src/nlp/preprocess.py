"""
preprocess.py

Text preprocessing utilities for NLP.
"""

import re


def clean_text(text: str) -> str:
    """
    Clean review text before NLP processing.

    Args:
        text (str): Raw review text.

    Returns:
        str: Cleaned review text.
    """

    if text is None:
        return ""

    text = str(text)

    # Lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove punctuation (keep letters/numbers/spaces)
    text = re.sub(r"[^\w\s]", "", text)

    return text.strip()

