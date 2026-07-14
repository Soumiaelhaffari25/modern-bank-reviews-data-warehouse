"""
topics.py

Topic classification.
"""

from src.nlp.models import topic_model

TOPICS = [
    "Customer Service",
    "Waiting Time",
    "ATM",
    "Mobile App",
    "Online Banking",
    "Loan",
    "Credit Card",
    "Branch Cleanliness",
    "Security",
    "General Experience",
]

def predict_topic(text: str) -> str:
    """
    Predict the main topic of a review.
    """

    if text is None or not text.strip():
        return "Unknown"

    prediction = topic_model(
        text,
        candidate_labels=TOPICS,
    )

    return prediction["labels"][0]
