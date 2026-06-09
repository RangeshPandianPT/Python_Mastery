"""
Requests_Part3_BeautifulSoup.py
Introduction to Web Scraping using requests and BeautifulSoup (bs4).
You need to install beautifulsoup4: `pip install beautifulsoup4`
"""

import requests
from bs4 import BeautifulSoup

def scrape_wikipedia_python():
    print("=== WEB SCRAPING WIKIPEDIA ===")
    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    
    # 1. Fetch the HTML
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the webpage.")
        return
        
    html_content = response.text
    
    # 2. Parse the HTML with BeautifulSoup
    # 'html.parser' is built-in. 'lxml' is faster but requires pip install lxml
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 3. Extracting Data
    print("\n--- Extracting Title ---")
    page_title = soup.title.string
    print(f"Page Title: {page_title}")
    
    print("\n--- Extracting Headings (H2) ---")
    # find_all returns a list of all matching elements
    h2_tags = soup.find_all('h2')
    # Print first 5 headings, extracting the text
    for i, tag in enumerate(h2_tags[:5]):
        print(f"{i+1}. {tag.text.strip()}")
        
    print("\n--- Extracting the First Paragraph ---")
    # Find the main content div, then find paragraphs
    content_div = soup.find(id='mw-content-text')
    paragraphs = content_div.find_all('p')
    
    # The first few paragraphs might be empty or short (infobox), find the first substantial one
    for p in paragraphs:
        text = p.text.strip()
        if len(text) > 100: # Assuming main intro paragraph is long
            print(f"First Main Paragraph:\n{text}")
            break
            
    print("\n--- Extracting Links ---")
    # Finding all <a> tags with an href attribute inside the first paragraph
    first_p = content_div.find('p', class_=False) # Simple way to skip some infobox paragraphs
    links = soup.find_all('a', href=True)
    
    print(f"Total links found on page: {len(links)}")
    print("First 5 internal Wikipedia links:")
    internal_links = [link['href'] for link in links if link['href'].startswith('/wiki/')]
    for link in internal_links[:5]:
        print(f" - https://en.wikipedia.org{link}")

if __name__ == "__main__":
    # Note: Web scraping should be done ethically and in accordance with the site's robots.txt
    scrape_wikipedia_python()
