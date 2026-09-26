import datetime
import requests
from bs4 import BeautifulSoup

def main():
    print(f"Scraper started at: {datetime.datetime.now()}")

    # Example target
    url = "https://example.com"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.select_one("h1").text
        print(f"Successfully scraped title: {title}")
    else:
        print(f"Failed to fetch page. Status: {response.status_code}")

if __name__ == "__main__":
    main()
