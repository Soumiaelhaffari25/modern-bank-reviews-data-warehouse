"""
load_banks.py

Insert discovered banks into PostgreSQL.
"""

from datetime import datetime

from src.database.connection import create_connection


def load_banks(banks):
    """
    Insert discovered banks into PostgreSQL.
    """

    connection = create_connection()

    cursor = connection.cursor()

    inserted = 0

    query = """
    INSERT INTO banks
    (
        bank_name,
        url,
        city,
        scraped_at
    )
    VALUES
    (
        %s,
        %s,
        %s,
        %s
    )
    ON CONFLICT (url) DO NOTHING;
    """

    for bank in banks:

        cursor.execute(
            query,
            (
                bank["name"],
                bank["url"],
                "Rabat",
                datetime.now(),
            ),
        )

        inserted += cursor.rowcount

    connection.commit()

    cursor.close()
    connection.close()

    print(f"{inserted} bank(s) inserted successfully.")

    return inserted