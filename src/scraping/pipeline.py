"""
pipeline.py

Complete scraping pipeline.

Workflow:
1. Read bank branches from PostgreSQL.
2. Open each branch on Google Maps.
3. Extract branch information.
4. Extract customer reviews.
5. Save everything into PostgreSQL.
"""

import time

from src.database.read_banks import get_banks
from src.database.load_reviews import load_reviews
from src.scraping.scraper import GoogleMapsScraper
from src.database.update_bank_information import update_bank_information


def main():
    """
    Run the complete scraping pipeline.
    """

    scraper = GoogleMapsScraper()

    scraper.launch_browser()

    banks = get_banks()

    total = len(banks)

    success = 0
    failed = 0

    for index, (name, url) in enumerate(banks, start=1):

        print("\n" + "=" * 70)
        print(f"[{index}/{total}] Processing: {name}")
        print("=" * 70)

        try:

            # Open branch
            scraper.open_bank(url)

            # Extract branch information
            bank = scraper.extract_bank_information()
            
            bank["bank_url"] = url
            
            update_bank_information(bank)

         
            if not scraper.open_reviews():
                print(f"No reviews available for {name}")
                success += 1
                continue
            
            # Expand all reviews
            scraper.expand_reviews()

            # Extract reviews
            reviews = scraper.extract_all_reviews()

            # Save reviews
            new_reviews = load_reviews(
                reviews,
                url,
            )

            if new_reviews == 0:
                print(f"No new reviews for {name}.")
                success += 1
                continue

            print(f"{new_reviews} new review(s) added.")

            success += 1

            print(f"✓ {name} completed successfully.")

            time.sleep(3)

        except Exception as e:

            failed += 1

            print(f"✗ Error while processing {name}")
            print(e)

    scraper.close_browser()

    print("\n" + "=" * 70)
    print("SCRAPING PIPELINE FINISHED")
    print("=" * 70)
    print(f"Total banks : {total}")
    print(f"Successful : {success}")
    print(f"Failed      : {failed}")
    print("=" * 70)


if __name__ == "__main__":
    main()