"""
scraper.py

Main module responsible for interacting with Google Maps
using Playwright.
"""

from playwright.sync_api import sync_playwright
from src.scraping.config import GOOGLE_MAPS_URL
from src.scraping.selectors import SEARCH_BOX
from src.scraping.selectors import REVIEWS_TAB

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
            headless=False
        )

        # Create a new browser tab
        self.page = self.browser.new_page()
        
        # Increase timeout
        self.page.set_default_timeout(60000)

        print("Google Maps opened successfully!")

    def open_google_maps(self):
        """
        Open Google Maps.
        """

        print("Opening Google Maps...")

        self.page.goto(
           GOOGLE_MAPS_URL,
           wait_until="commit",
           timeout=60000
        )
        
        self.page.wait_for_selector(
            'input[name="q"]',
            timeout=60000
        )

        print("Google Maps loaded succesfully.")

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

    def search_bank(self, bank_name: str):
       """
       Search for a bank on Google Maps.

       Args:
           bank_name (str): Name of the bank branch.
       """

       print(f"Searching for: {bank_name}")

       search_box = self.page.locator(SEARCH_BOX)

       search_box.wait_for(state="visible")

       search_box.fill(bank_name)

       search_box.press("Enter")

       self.page.wait_for_timeout(5000)

       print("Search completed.")

    def click_first_result(self):
      """
      Click on the first search result.
      """

      print("Opening first result...")

      first_result = self.page.locator("a.hfpxzc").first

      first_result.wait_for(state="visible")

      first_result.click()

      self.page.wait_for_timeout(3000)

      print("First result opened.")

    def open_reviews(self):
      """
      Open the Reviews tab.
      """

      print("Opening Reviews tab...")

      tabs = self.page.locator(REVIEWS_TAB)

      review_tab = tabs.nth(1)

      review_tab.wait_for(state="visible")

      review_tab.click()

      self.page.wait_for_timeout(3000)

      print("Reviews tab opened.")


def main():
    """
    Main function.
    """

    scraper = GoogleMapsScraper()

    scraper.launch_browser()

    scraper.open_google_maps()

    scraper.search_bank("Attijariwafa Bank Agdal Rabat")

    scraper.click_first_result()

    scraper.open_reviews()

    input("\nPress ENTER to close the browser...")

    scraper.close_browser()


if __name__ == "__main__":
    main()