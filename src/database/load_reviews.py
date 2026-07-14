"""
Load reviews into PostgreSQL.
"""

from datetime import datetime

from src.database.connection import create_connection


def load_reviews(reviews, bank_url):
    """
    Insert reviews into PostgreSQL.
    """

    connection = create_connection()

    cursor = connection.cursor()

    query = """
    INSERT INTO reviews
    (
        bank_url,
        author,
        rating,
        review_date,
        review_text,
        scraped_at
    )
    VALUES
    (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
    )
    ON CONFLICT DO NOTHING;
    """
    inserted = 0
    
    for review in reviews:

        rating = review["rating"]

        if rating:
            rating = int(rating.split()[0])
        else:
            rating = None

        cursor.execute(
            query,
            (
                bank_url,
                review["author"],
                rating,
                review["date"],
                review["review"],
                datetime.now(),
            ),
        )
        
        if cursor.rowcount == 1:
            inserted += 1

    connection.commit()

    cursor.close()
    connection.close()

    print(f"{inserted} new review(s) inserted.")
    
    return inserted