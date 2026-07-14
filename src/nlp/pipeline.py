"""
pipeline.py

Run the complete NLP pipeline.
"""
from tqdm import tqdm
from src.database.read_reviews import read_reviews
from src.database.update_reviews import update_review

from src.nlp.preprocess import clean_text
from src.nlp.language import detect_language
from src.nlp.sentiment import predict_sentiment
from src.nlp.keywords import extract_keywords
from src.nlp.topics import predict_topic


def run_pipeline():
    """
    Run the NLP pipeline.
    """

    reviews = read_reviews()

    print(f"\n{len(reviews)} reviews found.\n")

    success = 0
    failed = 0

    for review_id, review_text in tqdm(
        reviews,
        desc="Processing Reviews",
        unit="review"
    ):

        try:

            # Skip empty reviews
            if not review_text:
                print(f"Review {review_id} skipped (empty review).")
                continue

            # Clean text
            cleaned_text = clean_text(review_text)

            # Detect language
            language = detect_language(cleaned_text)

            # Predict sentiment
            sentiment = predict_sentiment(cleaned_text)

            # Keywords
            keywords = extract_keywords(cleaned_text)

            # Topic
            topic = predict_topic(cleaned_text)

            # Update PostgreSQL
            update_review(
                review_id=review_id,
                language=language,
                sentiment=sentiment,
                keywords=keywords,
                topic=topic,
            )

            success += 1

            print(
                f"✔ Review {review_id}"
                f"\n   Language : {language}"
                f"\n   Sentiment: {sentiment}"
                f"\n   Topic    : {topic}"
                f"\n   Keywords : {keywords}\n"
            )

        except Exception as e:

            failed += 1

            print(
                f"✘ Review {review_id} failed."
            )

            print(e)

    print("\n========== SUMMARY ==========")
    print(f"Processed : {success}")
    print(f"Failed    : {failed}")
    print("=============================")


if __name__ == "__main__":

    run_pipeline()