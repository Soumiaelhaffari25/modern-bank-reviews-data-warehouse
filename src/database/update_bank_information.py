"""
update_bank_information.py

Update bank information in PostgreSQL.
"""

from src.database.connection import create_connection


def update_bank_information(bank):
    """
    Update bank information.
    """

    connection = create_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE banks
        SET
            bank_name = %s,
            address = %s,
            latitude = %s,
            longitude = %s
        WHERE url = %s;
        """,
        (   
            bank["bank_name"],
            bank["address"],
            bank["latitude"],
            bank["longitude"],
            bank["bank_url"],
        ),
    )
    
    print(f"Rows updated:{cursor.rowcount}")

    connection.commit()

    cursor.close()
    connection.close()