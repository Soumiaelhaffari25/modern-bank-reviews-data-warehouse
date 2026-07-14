"""
keywords.py

Keyword extraction.
"""

from src.nlp.models import keyword_model


def extract_keywords(text: str) -> str:
    """
    Extract keywords from a review.

    Args:
        text (str): Review text.

    Returns:
        str: Comma-separated keywords.
    """

    if text is None or not text.strip():
        return ""

    keywords = keyword_model.extract_keywords(
        text,
        top_n=5,
        stop_words="english",
    )

    return ", ".join(
        keyword
        for keyword, score in keywords
    )
    