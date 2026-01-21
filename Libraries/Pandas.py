# =============================================================================
# PANDAS LIBRARY - COMPREHENSIVE GUIDE
# =============================================================================
# Pandas is a powerful data manipulation and analysis library for Python.
# It provides data structures like DataFrame and Series for handling
# structured data efficiently.

# =============================================================================
# 1. IMPORTING PANDAS
# =============================================================================
import pandas as pd
import numpy as np

# =============================================================================
# 2. PANDAS DATA STRUCTURES
# =============================================================================

# ----- Series (1D labeled array) -----
# Creating a Series from a list
s = pd.Series([1, 3, 5, 7, 9])
print("Basic Series:")
print(s)

# Series with custom index
s_indexed = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print("\nSeries with custom index:")
print(s_indexed)

# Series from dictionary
s_dict = pd.Series({'apple': 100, 'banana': 200, 'cherry': 300})
print("\nSeries from dictionary:")
print(s_dict)

# ----- DataFrame (2D labeled data structure) -----
# Creating DataFrame from dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'City': ['New York', 'Paris', 'London', 'Tokyo'],
    'Salary': [50000, 60000, 70000, 55000]
}
df = pd.DataFrame(data)
print("\nBasic DataFrame:")
print(df)

# DataFrame with custom index
df_indexed = pd.DataFrame(data, index=['emp1', 'emp2', 'emp3', 'emp4'])
print("\nDataFrame with custom index:")
print(df_indexed)

# =============================================================================
# 3. READING AND WRITING DATA
# =============================================================================

# ----- Reading CSV -----
# df = pd.read_csv('filename.csv')
# df = pd.read_csv('filename.csv', index_col=0)  # Use first column as index
# df = pd.read_csv('filename.csv', header=None)   # No header row
# df = pd.read_csv('filename.csv', usecols=['col1', 'col2'])  # Select columns

# ----- Writing CSV -----
# df.to_csv('output.csv')
# df.to_csv('output.csv', index=False)  # Without index
# df.to_csv('output.csv', columns=['Name', 'Age'])  # Select columns

# ----- Other formats -----
# df = pd.read_excel('filename.xlsx')
# df = pd.read_json('filename.json')
# df = pd.read_sql('SELECT * FROM table', connection)
# df.to_excel('output.xlsx')
# df.to_json('output.json')

# =============================================================================
# 4. EXPLORING DATA
# =============================================================================
print("\n--- Exploring Data ---")

# Basic info
print("\nFirst 2 rows:")
print(df.head(2))

print("\nLast 2 rows:")
print(df.tail(2))

print("\nShape (rows, columns):", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nData types:")
print(df.dtypes)

print("\nDataFrame Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMemory usage:")
print(df.memory_usage())

# =============================================================================
# 5. SELECTING DATA
# =============================================================================
print("\n--- Selecting Data ---")

# ----- Selecting columns -----
print("\nSelect single column (as Series):")
print(df['Name'])

print("\nSelect multiple columns:")
print(df[['Name', 'Age']])

# ----- Selecting rows by index -----
print("\nSelect rows by index (iloc - integer location):")
print(df.iloc[0])      # First row
print(df.iloc[0:2])    # First two rows
print(df.iloc[[0, 2]]) # First and third rows

# ----- Selecting by label (loc) -----
df_indexed = df.set_index('Name')
print("\nSelect by label (loc):")
print(df_indexed.loc['Alice'])

# ----- Selecting specific cells -----
print("\nSelect specific cell:")
print(df.iloc[0, 1])       # First row, second column
print(df.loc[0, 'Age'])    # Row 0, 'Age' column

# =============================================================================
# 6. FILTERING DATA
# =============================================================================
print("\n--- Filtering Data ---")

# Boolean filtering
print("\nEmployees older than 28:")
print(df[df['Age'] > 28])

print("\nEmployees in New York or Paris:")
print(df[df['City'].isin(['New York', 'Paris'])])

print("\nMultiple conditions (AND):")
print(df[(df['Age'] > 25) & (df['Salary'] > 55000)])

print("\nMultiple conditions (OR):")
print(df[(df['Age'] < 26) | (df['Salary'] > 65000)])

# Query method (more readable)
print("\nUsing query method:")
print(df.query('Age > 28 and Salary > 55000'))

# =============================================================================
# 7. ADDING AND MODIFYING DATA
# =============================================================================
print("\n--- Adding and Modifying Data ---")

# Add new column
df['Bonus'] = df['Salary'] * 0.1
print("\nDataFrame with Bonus column:")
print(df)

# Modify existing column
df['Salary'] = df['Salary'] * 1.05  # 5% raise
print("\nAfter 5% salary raise:")
print(df)

# Add column based on condition
df['Senior'] = df['Age'] >= 30
print("\nWith Senior status:")
print(df)

# Using apply() for custom functions
df['Name_Upper'] = df['Name'].apply(lambda x: x.upper())
print("\nWith uppercase names:")
print(df)

# Insert column at specific position
df.insert(2, 'Country', ['USA', 'France', 'UK', 'Japan'])
print("\nWith Country column inserted:")
print(df)

# =============================================================================
# 8. REMOVING DATA
# =============================================================================
print("\n--- Removing Data ---")

# Drop columns
df_dropped = df.drop(columns=['Bonus', 'Name_Upper', 'Senior'])
print("\nAfter dropping columns:")
print(df_dropped)

# Drop rows by index
df_dropped_rows = df.drop(index=[0, 2])
print("\nAfter dropping rows 0 and 2:")
print(df_dropped_rows)

# Drop duplicates
df_no_dupes = df.drop_duplicates()

# Drop based on subset of columns
# df_no_dupes = df.drop_duplicates(subset=['Name', 'City'])

# =============================================================================
# 9. HANDLING MISSING DATA
# =============================================================================
print("\n--- Handling Missing Data ---")

# Create DataFrame with missing values
data_with_nan = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, 11, 12]
}
df_nan = pd.DataFrame(data_with_nan)
print("\nDataFrame with NaN values:")
print(df_nan)

# Check for missing values
print("\nMissing values per column:")
print(df_nan.isnull().sum())

print("\nTotal missing values:", df_nan.isnull().sum().sum())

# Fill missing values
print("\nFill with 0:")
print(df_nan.fillna(0))

print("\nFill with mean:")
print(df_nan.fillna(df_nan.mean()))

print("\nForward fill (use previous value):")
print(df_nan.fillna(method='ffill'))

# Drop rows with missing values
print("\nDrop rows with any NaN:")
print(df_nan.dropna())

print("\nDrop rows where all values are NaN:")
print(df_nan.dropna(how='all'))

# =============================================================================
# 10. SORTING DATA
# =============================================================================
print("\n--- Sorting Data ---")

# Sort by single column
print("\nSort by Age (ascending):")
print(df.sort_values('Age'))

print("\nSort by Salary (descending):")
print(df.sort_values('Salary', ascending=False))

# Sort by multiple columns
print("\nSort by multiple columns:")
print(df.sort_values(['City', 'Age'], ascending=[True, False]))

# Sort by index
print("\nSort by index:")
print(df.sort_index())

# =============================================================================
# 11. GROUPING DATA
# =============================================================================
print("\n--- Grouping Data ---")

# Sample data for grouping
sales_data = {
    'Product': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Region': ['North', 'North', 'South', 'South', 'North', 'South'],
    'Sales': [100, 200, 150, 250, 120, 180],
    'Quantity': [10, 20, 15, 25, 12, 18]
}
sales_df = pd.DataFrame(sales_data)
print("\nSales Data:")
print(sales_df)

# Group by single column
print("\nSum by Product:")
print(sales_df.groupby('Product').sum())

# Group by multiple columns
print("\nSum by Product and Region:")
print(sales_df.groupby(['Product', 'Region']).sum())

# Multiple aggregations
print("\nMultiple aggregations:")
print(sales_df.groupby('Product').agg({
    'Sales': ['sum', 'mean', 'max'],
    'Quantity': ['sum', 'count']
}))

# Named aggregations (cleaner output)
print("\nNamed aggregations:")
print(sales_df.groupby('Product').agg(
    Total_Sales=('Sales', 'sum'),
    Avg_Sales=('Sales', 'mean'),
    Total_Qty=('Quantity', 'sum')
))

# =============================================================================
# 12. MERGING AND JOINING DATA
# =============================================================================
print("\n--- Merging and Joining Data ---")

# Sample DataFrames
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 3, 5],
    'Salary': [50000, 60000, 70000, 80000]
})

print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)

# Inner join (default)
print("\nInner Join:")
print(pd.merge(df1, df2, on='ID'))

# Left join
print("\nLeft Join:")
print(pd.merge(df1, df2, on='ID', how='left'))

# Right join
print("\nRight Join:")
print(pd.merge(df1, df2, on='ID', how='right'))

# Outer join
print("\nOuter Join:")
print(pd.merge(df1, df2, on='ID', how='outer'))

# Concatenate DataFrames
print("\nConcatenate (vertical):")
print(pd.concat([df1, df1], ignore_index=True))

# =============================================================================
# 13. PIVOT TABLES
# =============================================================================
print("\n--- Pivot Tables ---")

print("\nSales Data:")
print(sales_df)

# Create pivot table
pivot = pd.pivot_table(
    sales_df,
    values='Sales',
    index='Product',
    columns='Region',
    aggfunc='sum'
)
print("\nPivot Table (Sales by Product and Region):")
print(pivot)

# Pivot with multiple aggregations
pivot_multi = pd.pivot_table(
    sales_df,
    values='Sales',
    index='Product',
    columns='Region',
    aggfunc=['sum', 'mean']
)
print("\nPivot with multiple aggregations:")
print(pivot_multi)

# =============================================================================
# 14. STRING OPERATIONS
# =============================================================================
print("\n--- String Operations ---")

# Create DataFrame with string data
str_df = pd.DataFrame({
    'Name': ['John Smith', 'Jane Doe', 'Bob Johnson'],
    'Email': ['john@email.com', 'jane@email.com', 'bob@email.com']
})
print("\nString DataFrame:")
print(str_df)

# String methods (accessed via .str accessor)
print("\nUppercase names:")
print(str_df['Name'].str.upper())

print("\nLowercase names:")
print(str_df['Name'].str.lower())

print("\nName length:")
print(str_df['Name'].str.len())

print("\nSplit names:")
print(str_df['Name'].str.split(' ', expand=True))

print("\nExtract username from email:")
print(str_df['Email'].str.split('@').str[0])

print("\nContains 'John':")
print(str_df['Name'].str.contains('John'))

print("\nReplace 'John' with 'Jonathan':")
print(str_df['Name'].str.replace('John', 'Jonathan'))

# =============================================================================
# 15. DATE AND TIME OPERATIONS
# =============================================================================
print("\n--- Date and Time Operations ---")

# Create DataFrame with dates
date_df = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Value': [100, 150, 120, 180, 200]
})
print("\nDate DataFrame:")
print(date_df)

# Extract date components
date_df['Year'] = date_df['Date'].dt.year
date_df['Month'] = date_df['Date'].dt.month
date_df['Day'] = date_df['Date'].dt.day
date_df['DayOfWeek'] = date_df['Date'].dt.day_name()
print("\nWith extracted date components:")
print(date_df)

# Parse string dates
dates_str = pd.Series(['2024-01-15', '2024-02-20', '2024-03-25'])
dates_parsed = pd.to_datetime(dates_str)
print("\nParsed dates:")
print(dates_parsed)

# Date arithmetic
print("\nDate + 7 days:")
print(dates_parsed + pd.Timedelta(days=7))

# =============================================================================
# 16. USEFUL TIPS AND TRICKS
# =============================================================================
print("\n--- Useful Tips and Tricks ---")

# Chaining methods for readability
result = (df
          .drop(columns=['Senior', 'Name_Upper'])
          .sort_values('Salary', ascending=False)
          .head(3))
print("\nChained operations result:")
print(result)

# Value counts
print("\nValue counts for City:")
print(df['City'].value_counts())

# Unique values
print("\nUnique cities:")
print(df['City'].unique())
print("Number of unique cities:", df['City'].nunique())

# Setting display options
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_rows', 100)       # Show max 100 rows
pd.set_option('display.float_format', '{:.2f}'.format)  # Float format

# Reset display options
pd.reset_option('all')

# =============================================================================
# 17. PERFORMANCE TIPS
# =============================================================================
"""
Performance Best Practices:

1. Use vectorized operations instead of loops
   - df['C'] = df['A'] + df['B']  ✓
   - for i in range(len(df)):     ✗
       df.loc[i, 'C'] = df.loc[i, 'A'] + df.loc[i, 'B']

2. Use appropriate data types
   - Convert object columns to category if few unique values
   - df['Category'] = df['Category'].astype('category')

3. Use chunking for large files
   - for chunk in pd.read_csv('large.csv', chunksize=10000):
       process(chunk)

4. Use query() for complex filtering (faster than boolean indexing)
   - df.query('A > 10 and B < 20')

5. Use inplace=True sparingly (often not faster)
   - df = df.drop(columns=['col'])  (preferred)
   - df.drop(columns=['col'], inplace=True)

6. Use eval() for complex column calculations
   - df.eval('C = A + B')
"""

print("\n" + "="*60)
print("PANDAS COMPREHENSIVE GUIDE COMPLETE!")
print("="*60)
