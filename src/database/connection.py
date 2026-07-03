"""
Database connection.
"""

import psycopg2


def create_connection():
    """
    Create a PostgreSQL connection.
    """

    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        database="bank_reviews",
        user="postgres",
        password="1234"
    )

    return connection

if __name__ == "__main__":

    conn = create_connection()

    print("Connected successfully!")

    conn.close()

    print("Connection closed.")