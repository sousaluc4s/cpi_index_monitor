# sources/transparency_cpi.py

from datetime import datetime
from bs4 import BeautifulSoup
from cpi_index_monitor.core.http import get


BASE = "https://www.transparency.org"

class TransparencyCPI:

    def __init__(self, year=None):
        if year:
            self.year = year
        else:
            self.year = datetime.now().year - 1

    def get_page_url(self):
        return f"{BASE}/en/cpi/{self.year}"

    def exists(self):
        try:
            res = get(self.get_page_url())
            return res.status_code == 200
        except:
            return False

    def find_results_page(self):
        res = get(self.get_page_url())
        soup = BeautifulSoup(res.text, "html.parser")

        for a in soup.find_all("a", href=True):
            text = a.get_text(strip=True).lower()

            # more robust check for the results page
            if "results" in text and "trend" in text:
                href = a["href"]

                if not href.startswith("http"):
                    href = BASE + href

                return href

        return None

    def extract_file(self, results_url):
        res = get(results_url)
        soup = BeautifulSoup(res.text, "html.parser")

        for a in soup.find_all("a", href=True):
            href = a["href"]

            # ensure that the file comes from the CDN
            if "transparencycdn.org/images" in href:
                return href

        return None

    def get_latest_file(self):
        if not self.exists():
            return None

        results_page = self.find_results_page()
        if not results_page:
            return None

        # if it is file, it returns the file
        if "transparencycdn.org/images" in results_page:
            return results_page

        return self.extract_file(results_page)