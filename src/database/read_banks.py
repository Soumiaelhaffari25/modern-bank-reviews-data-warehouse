"""
read_banks.py

Read banks from PostgreSQL.
"""

from src.database.connection import create_connection


def get_banks(limit=None):
    """
    Read banks from PostgreSQL.

    Args:
        limit (int, optional): Maximum number of banks to return.

    Returns:
        list[tuple]: List of (name, url).
    """

    connection = create_connection()

    cursor = connection.cursor()

    if limit is None:

        cursor.execute("""
            SELECT
                bank_name,
                url
            FROM banks;
        """)

    else:

        cursor.execute("""
            SELECT
                bank_name,
                url
            FROM banks
            LIMIT %s;
        """, (limit,))

    banks = cursor.fetchall()

    cursor.close()
    connection.close()

    return banks