# ============================================================
# WEB SCRAPING TO DATA PIPELINE PROJECT
# ============================================================
# This script scrapes data from a public test website,
# parses it, saves it to a CSV, and performs basic analysis.
# 
# Target: http://books.toscrape.com/ (A site specifically for scraping practice)
# ============================================================

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

print("=" * 50)
print("1. SCRAPING DATA FROM BOOKS.TOSCRAPE.COM")
print("=" * 50)

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"
scraped_books = []
pages_to_scrape = 3  # We'll just scrape the first 3 pages for this example

for page in range(1, pages_to_scrape + 1):
    url = BASE_URL.format(page)
    print(f"Scraping page {page}: {url}")
    
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve page {page}. Status Code: {response.status_code}")
        continue
        
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all book articles on the page
    books = soup.find_all('article', class_='product_pod')
    
    for book in books:
        # Title is inside an <h3> tag, inside an <a> tag. 'title' attribute holds full text.
        title = book.find('h3').find('a')['title']
        
        # Price is inside a <p> with class 'price_color'
        price_text = book.find('p', class_='price_color').text
        # Price comes with a £ sign (e.g., '£51.77'), we strip it and convert to float
        price = float(price_text.replace('£', '').replace('Â', '').strip())
        
        # Rating is inside a <p> with class 'star-rating'
        # Classes are like ['star-rating', 'Three'], we want the second one.
        rating_classes = book.find('p', class_='star-rating')['class']
        rating = rating_classes[1] if len(rating_classes) > 1 else 'None'
        
        # In stock availability
        availability = book.find('p', class_='instock availability').text.strip()
        
        scraped_books.append({
            'Title': title,
            'Price_GBP': price,
            'Rating': rating,
            'Availability': availability
        })
        
    # Polite delay between requests
    time.sleep(1)

print(f"\nSuccessfully scraped {len(scraped_books)} books.")


print("\n" + "=" * 50)
print("2. SAVING DATA TO CSV")
print("=" * 50)

# Convert list of dictionaries to a Pandas DataFrame
df = pd.DataFrame(scraped_books)

# Save to CSV
csv_filename = "scraped_books.csv"
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
