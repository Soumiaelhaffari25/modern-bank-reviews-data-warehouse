"""
Export utilities.
"""

import pandas as pd


def export_to_csv(reviews, output_path):
    """
    Export reviews to a CSV file.

    Args:
        reviews (list): List of dictionaries.
        output_path (str): Destination CSV file.
    """

    df = pd.DataFrame(reviews)

    df.to_csv(
        output_path,
        index=False,
        encoding="utf-8-sig"
    )

    print(f"\nCSV exported successfully:\n{output_path}")