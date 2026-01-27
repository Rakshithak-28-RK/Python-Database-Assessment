import requests
from bs4 import BeautifulSoup
import json
import re

class BookScraper:
    def __init__(self, url):
        self.url = url
        self.books = []

    def fetch_page(self):
        try:
            response = requests.get(self.url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching page: {e}")
            return None

    def parse_books(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        # Example: Assume books are in <div class="book"> with title, author, year
        book_divs = soup.find_all('div', class_='book')
        for div in book_divs:
            title = div.find('h2').text.strip() if div.find('h2') else 'Unknown'
            author = div.find('p', class_='author').text.strip() if div.find('p', class_='author') else 'Unknown'
            year_match = re.search(r'\b(19|20)\d{2}\b', div.text)
            year = int(year_match.group()) if year_match else 0
            self.books.append({'title': title, 'author': author, 'year': year})

    def save_to_json(self, filename='scraped_books.json'):
        with open(filename, 'w') as f:
            json.dump(self.books, f, indent=4)
        print(f"Saved {len(self.books)} books to {filename}")

# Usage
scraper = BookScraper('https://example.com/books')  # Replace with a real scraping URL (e.g., a book site)
html = scraper.fetch_page()
if html:
    scraper.parse_books(html)
    scraper.save_to_json()
