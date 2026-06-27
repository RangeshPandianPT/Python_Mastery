import pandas as pd
import sqlite3
import os

def extract_data(file_path):
    """Extract data from a CSV file."""
    print(f"Extracting data from {file_path}...")
    df = pd.read_csv(file_path)
    print(f"Extracted {len(df)} rows.")
    return df

def transform_data(df):
    """Transform the data: Calculate total revenue per transaction and group by product."""
    print("Transforming data...")
    # Calculate TotalRevenue for each row
    df['TotalRevenue'] = df['Quantity'] * df['Price']
    
    # Group by Product to see total sales and revenue
    summary_df = df.groupby('Product').agg(
        Total_Quantity_Sold=('Quantity', 'sum'),
        Total_Revenue=('TotalRevenue', 'sum')
    ).reset_index()
    
    print("Transformation complete.")
    return summary_df

def load_data(df, db_path, table_name):
    """Load the transformed data into a SQLite database."""
    print(f"Loading data into {db_path} (table: {table_name})...")
    conn = sqlite3.connect(db_path)
    
    # Save the dataframe to SQLite, replace if exists
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    
    # Verify the load
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    row_count = cursor.fetchone()[0]
    print(f"Successfully loaded {row_count} rows into the database.")
    
    conn.close()

if __name__ == "__main__":
    # Define file paths
    # We use absolute or directory-relative paths so it runs well from the folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(current_dir, "sample_sales.csv")
    sqlite_db = os.path.join(current_dir, "sales_warehouse.db")
    
    print("--- Starting ETL Pipeline ---")
    
    # 1. Extract
    if os.path.exists(csv_file):
        raw_data = extract_data(csv_file)
        
        # 2. Transform
        transformed_data = transform_data(raw_data)
        print("\nTransformed Data Preview:")
        print(transformed_data)
        print()
        
        # 3. Load
        load_data(transformed_data, sqlite_db, "product_sales_summary")
        
        print("--- ETL Pipeline Completed Successfully ---")
    else:
        print(f"Error: Could not find {csv_file}. Please ensure it exists in the directory.")
