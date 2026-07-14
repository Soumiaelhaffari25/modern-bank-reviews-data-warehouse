"""
crawler.py

Discover bank branches from Google Maps.

This module is responsible for:
- Opening Google Maps
- Searching for banks in a city
- (Later) Collecting all bank branches
"""

from playwright.sync_api import sync_playwright
from src.scraping.selectors import (
    RESULT_CARD,
    RESULT_LINK,
)
from src.database.load_banks import load_banks

GOOGLE_MAPS_URL = "https://www.google.com/maps"


class GoogleMapsCrawler:
    """
    Google Maps crawler.
    """

    def __init__(self):

        self.playwright = None
        self.browser = None
        self.page = None

    def launch_browser(self):
        """
        Launch Chromium.
        """

        print("Launching browser...")

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=False
        )

        self.page = self.browser.new_page()

        self.page.set_default_timeout(60000)

        print("Browser launched successfully.")

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
            'input[name="q"]'
        )

        print("Google Maps loaded.")

    def search_banks(self, city):
        """
        Search all banks in a city.
        """

        print(f"\nSearching banks in {city}...\n")

        search_box = self.page.locator(
            'input[name="q"]'
        )

        search_box.fill(
            f"Banks in {city}"
        )

        search_box.press("Enter")

        self.page.wait_for_timeout(5000)

        print("Search completed.")

    def close_browser(self):
        """
        Close browser.
        """

        print("\nClosing browser...")

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()

        print("Browser closed.")
        
    def discover_banks(self):
        """
        Discover all banks currently visible in the search results.
        """

        print("\nDiscovering banks...\n")

        banks = []

        cards = self.page.locator(RESULT_CARD)

        count = cards.count()

        print(f"{count} result(s) found.\n")

        for i in range(count):

            card = cards.nth(i)

            try:

                link = card.locator(RESULT_LINK)

                name = link.get_attribute("aria-label")

                url = link.get_attribute("href")

                bank = {
                    "name": name,
                    "url": url
                }

                banks.append(bank)

                print(bank)

            except Exception:
                pass

        print(f"\n{len(banks)} bank(s) discovered.\n")

        return banks
    
    def scroll_results(self):
        """
        Scroll until all bank results are loaded.
        """

        print("\nScrolling results...\n")

        results = self.page.locator('div[role="feed"]')

        previous_count = 0

        no_change = 0

        while True:

            current_count = self.page.locator(RESULT_CARD).count()

            print(f"{current_count} banks loaded...")

            if current_count == previous_count:

                no_change += 1

            else:

                no_change = 0

            if no_change >= 5:
                break

            previous_count = current_count

            results.evaluate(
                "(element) => element.scrollBy(0, 1500)"
            )

            self.page.wait_for_timeout(3000)

        print("\nFinished scrolling.\n")

def main():

    crawler = GoogleMapsCrawler()

    crawler.launch_browser()

    crawler.open_google_maps()

    crawler.search_banks("Rabat")
    
    crawler.page.wait_for_timeout(5000)
    
    crawler.scroll_results()
    
    banks = crawler.discover_banks()
    
    load_banks(banks)

    print("\n========== BANKS ==========\n")

    for bank in banks:
        print(bank)

    input("\nPress ENTER to close...")

    crawler.close_browser()


if __name__ == "__main__":
    main()