"""
update_reviews.py

Update NLP information in PostgreSQL.
"""

from src.database.connection import create_connection


def update_review(
    review_id: int,
    language: str,
    sentiment: str,
    keywords: str,
    topic: str,
    connection=None,
):
    """
    Update a review with NLP results.
    """

    own_connection = False

    if connection is None:
        connection = create_connection()
        own_connection = True

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE reviews
        SET
            language = %s,
            sentiment = %s,
            keywords = %s,
            topic = %s
        WHERE review_id = %s
        """,
        (
            language,
            sentiment,
            keywords,
            topic,
            review_id,
        ),
    )

    connection.commit()

    cursor.close()

    if own_connection:
        connection.close()