"""
scraper.py

Main module responsible for interacting with Google Maps
using Playwright.
"""
from src.utils.location import extract_coordinates
from playwright.sync_api import sync_playwright
from src.scraping.config import GOOGLE_MAPS_URL
from src.scraping.selectors import (
    SEARCH_BOX,
    REVIEWS_TAB,
    REVIEW_CONTAINER,
    SEE_MORE_BUTTON,
    REVIEW_AUTHOR,
    REVIEW_RATING,
    REVIEW_DATE,
    REVIEW_TEXT,
    BANK_NAME,
    BANK_RATING,
    BANK_ADDRESS,
    TOTAL_REVIEWS,
)
from src.export import export_to_csv
from src.database.load_reviews import load_reviews

class GoogleMapsScraper:
    """
    Google Maps scraper.

    This class is responsible for:
    - Launching the browser
    - Opening Google Maps
    - (Later) Searching for bank branches
    - (Later) Collecting customer reviews
    """

    def __init__(self):
        """
        Initialize the scraper.
        """

        self.playwright = None
        self.browser = None
        self.page = None

    def launch_browser(self):
        """
        Launch Chromium and open Google Maps.
        """

        print("Launching browser...")

        # Start Playwright
        self.playwright = sync_playwright().start()

        # Launch Chromium
        self.browser = self.playwright.chromium.launch(
            headless=True
        )

        # Create a new browser tab
        self.page = self.browser.new_page()
        
        # Increase timeout
        self.page.set_default_timeout(60000)

        print("Google Maps opened successfully!")

    def extract_all_reviews(self):
        """
        Extract all visible reviews and return them as a list of dictionaries.
        """

        print("\nExtracting all visible reviews...")

        reviews = []
        seen_reviews = set()

        review_cards = self.page.locator(REVIEW_CONTAINER)

        count = review_cards.count()

        print(f"{count} review(s) found.\n")

        for i in range(count):

            review = review_cards.nth(i)

            try:

            # -------------------------
            # Author
            # -------------------------
                author_locator = review.locator(REVIEW_AUTHOR)

                if author_locator.count() > 0:
                    author = author_locator.first.inner_text()
                else:
                    author = ""

            # -------------------------
            # Rating
            # -------------------------
                rating_locator = review.locator(REVIEW_RATING)

                if rating_locator.count() > 0:
                    rating = rating_locator.first.get_attribute("aria-label")
                else:
                    rating = ""

            # -------------------------
            # Date
            # -------------------------
                date_locator = review.locator(REVIEW_DATE)

                if date_locator.count() > 0:
                    date = date_locator.first.inner_text()
                else:
                    date = ""

            # -------------------------
            # Review text
            # -------------------------
                comment_locator = review.locator(REVIEW_TEXT)

                if comment_locator.count() > 0:
                    comment = comment_locator.first.inner_text()
                else:
                    comment = ""

            # -------------------------
            # Remove duplicates
            # -------------------------
                review_key = (author, date)

                if review_key in seen_reviews:
                    continue

                seen_reviews.add(review_key)

                review_data = {
                    "author": author,
                    "rating": rating,
                    "date": date,
                    "review": comment,
                }

                reviews.append(review_data)

            except Exception as e:

                print(f"\nReview {i + 1} skipped.")
                print(e)

                continue

        print(f"\n{len(reviews)} review(s) extracted successfully.\n")

        return reviews

    def close_browser(self):
        """
        Close the browser and stop Playwright.
        """

        print("Closing browser...")

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()

        print("Browser closed successfully!")

      
    def extract_bank_information(self):
        """
        Extract bank information.
        """

        print("\nExtracting bank information...")

    # -------------------------
    # Bank name
    # -------------------------
        try:
            bank_name = (
                self.page.title()
                .replace(" - Google Maps", "")
                .strip()
            )
        except:
            bank_name = ""

    # -------------------------
    # Google Maps URL
    # -------------------------
        bank_url = self.page.url

    # -------------------------
    # Address
    # -------------------------
        try:
            address = (
                self.page
                .locator(BANK_ADDRESS)
                .inner_text()
                .replace("", "")
                .strip()
            )
        except:
            address = ""

    # -------------------------
    # City
    # -------------------------
        city = "Rabat"

    # -------------------------
    # Coordinates
    # -------------------------
        current_url = self.page.url
        latitude, longitude = extract_coordinates(current_url)

    # -------------------------
    # Build dictionary
    # -------------------------
        bank = {
            "bank_name": bank_name,
            "address": address,
            "city": city,
            "latitude": latitude,
            "longitude": longitude,
        }

        print("\n========== BANK ==========")

        for key, value in bank.items():
            print(f"{key:15}: {value}")

        print("==========================\n")

        return bank
    def open_reviews(self):
        
        print("Opening Reviews tab...")
        try:
            tabs = self.page.locator(REVIEWS_TAB)

            review_tab = tabs.nth(1)

            review_tab.wait_for(state="visible", timeout=10000)

            review_tab.click()

            self.page.wait_for_timeout(3000)
            
            print("Reviews tab opened.")

            return True

        except:
            print("No Reviews tab found.")
            return False

    def expand_reviews(self):
        """
        Expand all truncated reviews.
        """

        print("Expanding reviews...")

        while True:

            buttons = self.page.locator(SEE_MORE_BUTTON)

            count = buttons.count()

            if count == 0:
                break

            try:
                buttons.first.click(timeout=2000)
                self.page.wait_for_timeout(300)

            except:
                break

        print("Reviews expanded.")
        
    def open_bank(self, url):
        """
        Open a bank directly from its Google Maps URL.
        """

        print(f"\nOpening bank...\n")

        self.page.goto(
            url,
            wait_until="commit",
            timeout=60000
        )

        self.page.wait_for_timeout(5000)

        print("Bank opened successfully.")
        print(f"Current URL: {self.page.url}")

def main():
    """
    Main function.
    """

    scraper = GoogleMapsScraper()

    scraper.launch_browser()
    
    url= input("Enter Google Maps URL:")
    
    scraper.open_bank(url)
    
    bank = scraper.extract_bank_information()
    
    scraper.open_reviews()

    scraper.expand_reviews()

    reviews = scraper.extract_all_reviews()
    
    load_reviews(
        reviews,
        bank["bank_url"]
    )

    print(f"\n{len(reviews)} review(s) scraped successfully.")

    input("\nPress ENTER to close...")

    scraper.close_browser()


if __name__ == "__main__":
    main()