# =============================================================================
# PANDAS PART 6 - ADVANCED TOPICS (Advanced)
# =============================================================================
# This covers advanced features for real-world data processing:
# Missing data, time series, file I/O, performance, and best practices.

import pandas as pd
import numpy as np

# =============================================================================
# 1. HANDLING MISSING DATA
# =============================================================================
print("--- Handling Missing Data ---")

# Create DataFrame with missing values
data = {
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [1, 2, 3, 4, 5],
    'D': [np.nan, np.nan, np.nan, 4, 5]
}
df = pd.DataFrame(data)
print("DataFrame with missing values:")
print(df)

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

print("\nTotal missing:", df.isnull().sum().sum())
print("Percentage missing:", (df.isnull().sum().sum() / df.size * 100).round(2), "%")

# ----- Dropping Missing Values -----
print("\nDrop rows with ANY missing:")
print(df.dropna())

print("\nDrop rows where ALL values missing:")
print(df.dropna(how='all'))

print("\nDrop columns with missing values:")
print(df.dropna(axis=1))

print("\nKeep rows with at least 3 non-NA values:")
print(df.dropna(thresh=3))

# ----- Filling Missing Values -----
print("\nFill with constant (0):")
print(df.fillna(0))

print("\nFill with mean:")
print(df.fillna(df.mean()))

print("\nForward fill (use previous value):")
print(df.fillna(method='ffill'))

print("\nBackward fill (use next value):")
print(df.fillna(method='bfill'))

# Fill different values for different columns
fill_values = {'A': 0, 'B': df['B'].median(), 'D': -1}
print("\nFill with different values per column:")
print(df.fillna(fill_values))

# Interpolation
print("\nLinear interpolation:")
print(df.interpolate())

# =============================================================================
# 2. STRING OPERATIONS
# =============================================================================
print("\n--- String Operations ---")

str_df = pd.DataFrame({
    'Name': ['  John Smith  ', 'JANE DOE', 'bob wilson', 'Alice Brown'],
    'Email': ['john@email.com', 'jane@company.org', 'bob@email.com', 'alice@company.org']
})
print("String DataFrame:")
print(str_df)

# All string methods are accessed via .str accessor
print("\nStripped and Title Case:")
print(str_df['Name'].str.strip().str.title())

print("\nName lengths:")
print(str_df['Name'].str.len())

print("\nSplit names:")
names_split = str_df['Name'].str.strip().str.split(' ', expand=True)
names_split.columns = ['First', 'Last']
print(names_split)

print("\nEmail domains:")
print(str_df['Email'].str.split('@').str[1])

print("\nContains 'company':")
print(str_df['Email'].str.contains('company'))

print("\nReplace email domain:")
print(str_df['Email'].str.replace('email.com', 'newemail.com'))

# Extract with regex
print("\nExtract username (before @):")
print(str_df['Email'].str.extract(r'(\w+)@'))

# =============================================================================
# 3. DATE AND TIME
# =============================================================================
print("\n--- Date and Time ---")

# Create date range
dates = pd.date_range(start='2024-01-01', periods=10, freq='D')
print("Date range:")
print(dates)

# Parse string dates
date_strings = ['2024-01-15', '2024-02-20', '15/03/2024', 'March 25, 2024']
parsed_dates = pd.to_datetime(date_strings, dayfirst=False)
print("\nParsed dates:")
print(parsed_dates)

# Time series DataFrame
ts_df = pd.DataFrame({
    'Date': pd.date_range('2024-01-01', periods=12, freq='M'),
    'Value': np.random.randint(100, 500, 12)
})
print("\nTime Series DataFrame:")
print(ts_df)

# ----- Datetime Accessors -----
print("\nYear:", ts_df['Date'].dt.year.tolist())
print("Month:", ts_df['Date'].dt.month.tolist())
print("Day:", ts_df['Date'].dt.day.tolist())
print("Day Name:", ts_df['Date'].dt.day_name().tolist()[:3])
print("Quarter:", ts_df['Date'].dt.quarter.tolist())

# ----- Date Filtering -----
print("\nRecords from 2024:")
print(ts_df[ts_df['Date'].dt.year == 2024].head())

print("\nQ1 2024 records:")
print(ts_df[ts_df['Date'].dt.quarter == 1])

# ----- Resampling -----
ts_df = ts_df.set_index('Date')
print("\nQuarterly sum:")
print(ts_df.resample('Q').sum())

# =============================================================================
# 4. READING AND WRITING FILES
# =============================================================================
print("\n--- File I/O ---")

# Simulating file operations (commented for demo)
"""
# ----- CSV -----
df = pd.read_csv('data.csv')
df = pd.read_csv('data.csv', index_col=0)           # First column as index
df = pd.read_csv('data.csv', usecols=['A', 'B'])    # Select columns
df = pd.read_csv('data.csv', nrows=100)             # First 100 rows
df = pd.read_csv('data.csv', skiprows=[1, 2])       # Skip rows
df = pd.read_csv('data.csv', na_values=['NA', '?']) # Custom NA values

df.to_csv('output.csv', index=False)

# ----- Excel -----
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
df = pd.read_excel('data.xlsx', sheet_name=0)       # By index

with pd.ExcelWriter('output.xlsx') as writer:
    df1.to_excel(writer, sheet_name='Sheet1')
    df2.to_excel(writer, sheet_name='Sheet2')

# ----- JSON -----
df = pd.read_json('data.json')
df.to_json('output.json', orient='records')

# ----- SQL (requires SQLAlchemy) -----
from sqlalchemy import create_engine
engine = create_engine('sqlite:///database.db')
df = pd.read_sql('SELECT * FROM table', engine)
df.to_sql('table_name', engine, if_exists='replace')

# ----- Chunked Reading for Large Files -----
for chunk in pd.read_csv('large_file.csv', chunksize=10000):
    process(chunk)
"""

print("File I/O examples shown as comments (no actual files)")

# =============================================================================
# 5. MEMORY OPTIMIZATION
# =============================================================================
print("\n--- Memory Optimization ---")

# Create sample large DataFrame
large_df = pd.DataFrame({
    'Int_Col': np.random.randint(0, 100, 10000),
    'Float_Col': np.random.random(10000),
    'Cat_Col': np.random.choice(['A', 'B', 'C'], 10000),
    'Str_Col': np.random.choice(['apple', 'banana', 'cherry'], 10000)
})

print("Original memory usage:")
print(large_df.memory_usage(deep=True))
print(f"Total: {large_df.memory_usage(deep=True).sum() / 1024:.2f} KB")

# Optimize data types
large_df['Int_Col'] = large_df['Int_Col'].astype('int8')  # Small integers
large_df['Cat_Col'] = large_df['Cat_Col'].astype('category')
large_df['Str_Col'] = large_df['Str_Col'].astype('category')

print("\nOptimized memory usage:")
print(large_df.memory_usage(deep=True))
print(f"Total: {large_df.memory_usage(deep=True).sum() / 1024:.2f} KB")

# =============================================================================
# 6. PERFORMANCE TIPS
# =============================================================================
print("\n--- Performance Tips ---")

"""
VECTORIZED OPERATIONS (DO THIS):
    df['C'] = df['A'] + df['B']
    df['D'] = df['A'].apply(lambda x: x * 2)
    
AVOID LOOPS (DON'T DO THIS):
    for i in range(len(df)):
        df.loc[i, 'C'] = df.loc[i, 'A'] + df.loc[i, 'B']

USE QUERY FOR FILTERING:
    df.query('A > 10 and B < 20')  # Faster than boolean indexing

USE eval() FOR COMPLEX EXPRESSIONS:
    df.eval('C = A + B')
    df.eval('D = (A - B) / C')

INPLACE OPERATIONS (use sparingly):
    df.drop(columns=['X'], inplace=True)  # Slightly faster but less readable
"""

# eval() example
df = pd.DataFrame({'A': range(1000), 'B': range(1000)})
df = df.eval('C = A + B')
df = df.eval('D = A * B / 100')
print("eval() result sample:")
print(df.head())

# =============================================================================
# 7. MULTI-INDEX
# =============================================================================
print("\n--- Multi-Index ---")

# Create multi-index DataFrame
arrays = [
    ['East', 'East', 'West', 'West'],
    ['Q1', 'Q2', 'Q1', 'Q2']
]
index = pd.MultiIndex.from_arrays(arrays, names=['Region', 'Quarter'])
multi_df = pd.DataFrame({'Sales': [100, 150, 120, 180]}, index=index)
print("\nMulti-Index DataFrame:")
print(multi_df)

# Access data
print("\nEast region:")
print(multi_df.loc['East'])

print("\nEast Q1:")
print(multi_df.loc[('East', 'Q1')])

# Reset to regular index
print("\nReset index:")
print(multi_df.reset_index())

# =============================================================================
# 8. WINDOW FUNCTIONS
# =============================================================================
print("\n--- Window Functions ---")

window_df = pd.DataFrame({
    'Value': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
})
print("Original:")
print(window_df)

# Rolling window
window_df['Rolling_Mean_3'] = window_df['Value'].rolling(window=3).mean()
window_df['Rolling_Sum_3'] = window_df['Value'].rolling(window=3).sum()
print("\nWith rolling calculations:")
print(window_df)

# Expanding window (cumulative)
window_df['Cumulative_Mean'] = window_df['Value'].expanding().mean()
print("\nWith cumulative mean:")
print(window_df)

# Shift (lag/lead)
window_df['Previous'] = window_df['Value'].shift(1)
window_df['Next'] = window_df['Value'].shift(-1)
print("\nWith shift (lag/lead):")
print(window_df)

# Percentage change
window_df['Pct_Change'] = window_df['Value'].pct_change()
print("\nWith percentage change:")
print(window_df)

# =============================================================================
# 9. STYLING OUTPUT
# =============================================================================
print("\n--- Styling (in Jupyter Notebooks) ---")

"""
In Jupyter Notebooks, you can style DataFrame output:

# Highlight max values
df.style.highlight_max()

# Apply gradient
df.style.background_gradient(cmap='Blues')

# Format numbers
df.style.format({'Price': '${:,.2f}', 'Percentage': '{:.1%}'})

# Apply bar charts
df.style.bar(subset=['Value'], color='lightblue')

# Multiple styles
(df.style
    .highlight_max(color='lightgreen')
    .highlight_min(color='lightcoral')
    .format('{:.2f}')
)
"""
print("Styling examples shown as comments (works in Jupyter)")

# =============================================================================
# 10. BEST PRACTICES SUMMARY
# =============================================================================
print("\n--- Best Practices Summary ---")

best_practices = """
1. USE VECTORIZED OPERATIONS
   - Avoid loops; use built-in pandas/numpy operations

2. USE APPROPRIATE DATA TYPES
   - Convert to 'category' for repeated strings
   - Use smaller int types (int8, int16) when possible

3. CHAIN OPERATIONS FOR READABILITY
   - (df.query('A > 10')
       .groupby('B')
       .agg({'C': 'sum'})
       .sort_values('C'))

4. USE .copy() WHEN MODIFYING SLICES
   - df_subset = df[df['A'] > 10].copy()

5. PREFER query() FOR COMPLEX FILTERS
   - More readable and often faster

6. USE CHUNKING FOR LARGE FILES
   - pd.read_csv('large.csv', chunksize=10000)

7. ALWAYS HANDLE MISSING DATA
   - Check with .isnull().sum() before analysis

8. USE MEANINGFUL INDEX
   - Set appropriate index for faster lookups
"""
print(best_practices)

print("\n" + "=" * 55)
print("PANDAS PART 6 - ADVANCED TOPICS COMPLETE!")
print("=" * 55)
print("\nCongratulations! You've completed the full Pandas series!")
