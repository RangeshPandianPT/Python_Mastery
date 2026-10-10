# ============================================================
# WEB SCRAPING TO DATA PIPELINE PROJECT
# ============================================================
# This script scrapes data from a public test website,
# parses it, saves it to a CSV, and performs basic analysis.
# 
# Target: http://books.toscrape.com/ (A site specifically for scraping practice)
# ============================================================

import aiohttp
import asyncio
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

print("=" * 50)
print("1. SCRAPING DATA FROM BOOKS.TOSCRAPE.COM")
print("=" * 50)

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"
pages_to_scrape = 3

async def fetch_page(session, url, page):
    print(f"Scraping page {page}: {url}")
    async with session.get(url) as response:
        if response.status != 200:
            print(f"Failed to retrieve page {page}. Status Code: {response.status}")
            return None
        return await response.text()

def parse_books(html_content):
    if not html_content:
        return []
        
    soup = BeautifulSoup(html_content, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    page_books = []
    
    for book in books:
        title = book.find('h3').find('a')['title']
        price_text = book.find('p', class_='price_color').text
        price = float(price_text.replace('£', '').replace('Â', '').strip())
        
        rating_classes = book.find('p', class_='star-rating')['class']
        rating = rating_classes[1] if len(rating_classes) > 1 else 'None'
        
        availability = book.find('p', class_='instock availability').text.strip()
        
        page_books.append({
            'Title': title,
            'Price_GBP': price,
            'Rating': rating,
            'Availability': availability
        })
    return page_books

async def main():
    scraped_books = []
    
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        tasks = []
        for page in range(1, pages_to_scrape + 1):
            url = BASE_URL.format(page)
            tasks.append(fetch_page(session, url, page))
            
        html_contents = await asyncio.gather(*tasks)
        
        for html_content in html_contents:
            books_on_page = parse_books(html_content)
            scraped_books.extend(books_on_page)
            
    print(f"\nSuccessfully scraped {len(scraped_books)} books in {time.time() - start_time:.2f} seconds.")
    return scraped_books

if __name__ == "__main__":
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    scraped_books = asyncio.run(main())

print("\n" + "=" * 50)
print("2. SAVING DATA TO CSV")
print("=" * 50)

# Convert list of dictionaries to a Pandas DataFrame
df = pd.DataFrame(scraped_books)

# Save to CSV
output_dir = "/data" if os.path.exists("/data") else os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'shared_data'))
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
csv_filename = os.path.join(output_dir, "scraped_books.csv")
df.to_csv(csv_filename, index=False, encoding='utf-8')
print(f"Data saved to {os.path.abspath(csv_filename)}")


print("\n" + "=" * 50)
print("3. QUICK DATA ANALYSIS WITH PANDAS")
print("=" * 50)

print("\nFirst 5 rows of the dataset:")
print(df.head())

print("\nSummary Statistics:")
print(df.describe())

print("\nAverage Price by Rating:")
# Map text ratings to numbers for sorting purposes
rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
df['Numeric_Rating'] = df['Rating'].map(rating_map)
avg_price_by_rating = df.groupby('Rating')['Price_GBP'].mean().sort_values()
print(avg_price_by_rating)
