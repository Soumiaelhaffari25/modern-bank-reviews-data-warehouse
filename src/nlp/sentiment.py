"""
sentiment.py

Review sentiment analysis.
"""

from src.nlp.models import sentiment_model


def predict_sentiment(text: str) -> str:
    """
    Predict review sentiment.

    Args:
        text (str): Review text.

    Returns:
        str: Positive, Negative or Neutral.
    """

    if not text.strip():
        return "Unknown"

    prediction = sentiment_model(text)[0]

    label = prediction["label"]

    mapping = {
        "positive": "Positive",
        "negative": "Negative",
        "neutral": "Neutral"
    }

    return mapping.get(label.lower(), "Unknown")

