import pandas as pd
import requests
import os
import sys
import time

# Setup logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from Python.Logging_Config import setup_logger
logger = setup_logger("ETL_Pipeline")

API_URL = os.environ.get("API_URL", "http://localhost:8000/books/")

def extract_data(file_path):
    """Extract data from the scraped CSV file."""
    logger.info(f"Extracting data from {file_path}...")
    df = pd.read_csv(file_path)
    logger.info(f"Extracted {len(df)} rows.")
    return df

def transform_data(df):
    """Transform the scraped data to match the API schema."""
    logger.info("Transforming data...")
    # Scraper gives: Title, Price_GBP, Rating, Availability
    # API needs: title, author, price
    
    # Map columns
    transformed_df = pd.DataFrame()
    transformed_df['title'] = df['Title']
    transformed_df['price'] = df['Price_GBP']
    # Author is not available from the main page, so set a default
    transformed_df['author'] = "Unknown"
    
    logger.info("Transformation complete.")
    return transformed_df

def load_data(df):
    """Load the transformed data into the API via POST requests."""
    logger.info(f"Loading data to API at {API_URL}...")
    
    success_count = 0
    for _, row in df.iterrows():
        payload = {
            "title": row['title'],
            "author": row['author'],
            "price": row['price']
        }
        try:
            response = requests.post(API_URL, json=payload)
            if response.status_code == 201:
                success_count += 1
            else:
                logger.warning(f"Failed to load book '{row['title']}'. Status: {response.status_code}, Response: {response.text}")
        except Exception as e:
            logger.error(f"Error making request for book '{row['title']}': {e}")
            
    logger.info(f"Successfully loaded {success_count} books into the database via API.")

if __name__ == "__main__":
    # Define file paths
    # When running in docker, we expect the data to be in /data
    csv_file = "/data/scraped_books.csv" if os.path.exists("/data") else os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'shared_data', 'scraped_books.csv'))
    
    logger.info("--- Starting ETL Pipeline ---")
    
    # Let's wait a bit to make sure scraper is finished if they are running concurrently
    # docker-compose depends_on with condition: service_completed_successfully should handle this,
    # but we add a safety check just in case.
    max_retries = 10
    for _ in range(max_retries):
        if os.path.exists(csv_file):
            break
        logger.info(f"Waiting for {csv_file} to be created by the scraper...")
        time.sleep(3)
        
    if os.path.exists(csv_file):
        # 1. Extract
        raw_data = extract_data(csv_file)
        
        # 2. Transform
        transformed_data = transform_data(raw_data)
        logger.info(f"\nTransformed Data Preview:\n{transformed_data.head()}")
        
        # 3. Load
        load_data(transformed_data)
        
        logger.info("--- ETL Pipeline Completed Successfully ---")
    else:
        logger.error(f"Could not find {csv_file}. Please ensure the Web Scraper has run.")
