"""
Load reviews into PostgreSQL.
"""

from datetime import datetime

from src.database.connection import create_connection


def load_reviews(reviews, bank_name):
    """
    Insert reviews into PostgreSQL.
    """

    connection = create_connection()

    cursor = connection.cursor()

    query = """
    INSERT INTO reviews
    (
        bank_name,
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
    );
    """

    for review in reviews:

        rating = review["rating"]

        if rating:

            rating = int(rating.split()[0])

        else:

            rating = None

        cursor.execute(

            query,

            (
                bank_name,
                review["author"],
                rating,
                review["date"],
                review["review"],
                datetime.now()
            )

        )

    connection.commit()

    cursor.close()

    connection.close()

    print(f"{len(reviews)} reviews inserted successfully.")