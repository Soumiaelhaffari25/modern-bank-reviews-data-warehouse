"""
language.py

Detect review language.
"""

from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException


def detect_language(text: str) -> str:
    """
    Detect the language of a review.

    Args:
        text (str): Review text.

    Returns:
        str: Language code (en, fr, ar, ...)
    """

    if not text or not text.strip():
        return "unknown"

    try:
        return detect(text)

    except LangDetectException:
        return "unknown"
    
