"""
Database connection.
"""
from pathlib import Path
from dotenv import load_dotenv
import os
import psycopg2

BASE_DIR = Path(__file__).resolve().parents[2]
ENV_PATH = BASE_DIR / ".env"
# Load environment variables
load_dotenv(ENV_PATH)


def create_connection():
    """
    Create a PostgreSQL connection.
    """

    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )

    return connection


if __name__ == "__main__":

    conn = create_connection()

    print("Connected successfully!")

    conn.close()

    print("Connection closed.")