from transformers import pipeline
from keybert import KeyBERT

print("Loading sentiment model...")

sentiment_model = pipeline(
    task="sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)

print("Sentiment model loaded.")

print("Loading keyword model...")

keyword_model = KeyBERT()

print("Keyword model loaded.")

print("Loading topic model...")

topic_model = pipeline(

    task="zero-shot-classification",

    model="facebook/bart-large-mnli"

)

print("Topic model loaded.")