"""
Extract geographic coordinates from a Google Maps URL.
"""

import re


def extract_coordinates(url):
    """
    Extract latitude and longitude from a Google Maps URL.

    Returns:
        tuple(latitude, longitude)
    """

    pattern = r"!3d(-?\d+\.\d+)!4d(-?\d+\.\d+)"

    match = re.search(pattern, url)

    if match:
        latitude = float(match.group(1))
        longitude = float(match.group(2))
        return latitude, longitude

    return None, None