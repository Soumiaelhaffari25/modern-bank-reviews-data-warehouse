"""
read_reviews.py

Read reviews from PostgreSQL.
"""

from src.database.connection import create_connection


def read_reviews():
    """
    Read all reviews from PostgreSQL.

    Returns:
        list[tuple]
    """

    connection = create_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            review_id,
            review_text
        FROM reviews
        WHERE sentiment IS NULL
        ORDER BY review_id
    """)

    reviews = cursor.fetchall()

    cursor.close()
    connection.close()

    return reviews

if __name__ == "__main__":

    reviews = read_reviews()

    print(reviews[:5])