# ============================================================
# PANDAS BASICS - Data Analysis with Python
# ============================================================
# This file covers essential pandas concepts including:
# - Installing pandas
# - Series and DataFrames
# - Reading/Writing Data (CSV, Excel, JSON)
# - Data Selection and Indexing
# - Data Cleaning and Handling Missing Values
# - Data Manipulation (Sorting, Filtering, Grouping)
# - Statistical Operations
# - Merging and Joining DataFrames
# - Data Visualization with pandas
# ============================================================
# Install: pip install pandas
# ============================================================


import pandas as pd
import numpy as np

print("=" * 60)
print("PANDAS BASICS - Data Analysis Library")
print("=" * 60)
print(f"Pandas version: {pd.__version__}")


# ============================================================
# 1. PANDAS SERIES - 1D Labeled Array
# ============================================================
"""
A Series is a one-dimensional labeled array capable of holding
any data type (integers, strings, floats, objects, etc.)
"""

print("\n" + "=" * 60)
print("1. PANDAS SERIES")
print("=" * 60)

# Creating a Series from a list
data = [10, 20, 30, 40, 50]
series = pd.Series(data)
print("Simple Series:")
print(series)

# Series with custom index
series_indexed = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
print("\nSeries with custom index:")
print(series_indexed)

# Series from a dictionary
dict_data = {'apple': 100, 'banana': 200, 'orange': 150}
series_dict = pd.Series(dict_data)
print("\nSeries from dictionary:")
print(series_dict)

# Accessing elements
print(f"\nFirst element: {series_indexed['a']}")
print(f"Multiple elements: {series_indexed[['a', 'c', 'e']].tolist()}")
print(f"Slicing: {series_indexed['b':'d'].tolist()}")

# Series operations
print(f"\nSum: {series.sum()}")
print(f"Mean: {series.mean()}")
print(f"Max: {series.max()}")
print(f"Min: {series.min()}")

# Vectorized operations
print(f"\nSeries * 2: {(series * 2).tolist()}")


# ============================================================
# 2. PANDAS DATAFRAME - 2D Labeled Data Structure
# ============================================================
"""
A DataFrame is a 2-dimensional labeled data structure with columns
of potentially different types. Think of it as a spreadsheet or
SQL table.
"""

print("\n" + "=" * 60)
print("2. PANDAS DATAFRAME")
print("=" * 60)

# Creating DataFrame from dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Salary': [50000, 60000, 75000, 55000, 65000]
}
df = pd.DataFrame(data)

print("DataFrame from dictionary:")
print(df)

# Basic DataFrame info
print(f"\nShape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"Data types:\n{df.dtypes}")
print(f"\nInfo:")
print(df.info())

# Creating DataFrame from list of dictionaries
records = [
    {'product': 'Laptop', 'price': 999, 'quantity': 5},
    {'product': 'Mouse', 'price': 29, 'quantity': 50},
    {'product': 'Keyboard', 'price': 79, 'quantity': 30}
]
df_products = pd.DataFrame(records)
print("\nDataFrame from list of dictionaries:")
print(df_products)

# Creating DataFrame from numpy array
array_data = np.random.randint(1, 100, size=(4, 3))
df_numpy = pd.DataFrame(array_data, 
                         columns=['A', 'B', 'C'],
                         index=['row1', 'row2', 'row3', 'row4'])
print("\nDataFrame from numpy array:")
print(df_numpy)


# ============================================================
# 3. READING AND WRITING DATA
# ============================================================
"""
Pandas supports many file formats including CSV, Excel, JSON,
SQL databases, and more.
"""

print("\n" + "=" * 60)
print("3. READING AND WRITING DATA")
print("=" * 60)

# Create sample data for file operations
sample_df = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'name': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
    'price': [19.99, 29.99, 39.99, 49.99, 59.99],
    'in_stock': [True, True, False, True, False]
})

# Writing to CSV
sample_df.to_csv('sample_data.csv', index=False)
print("Saved to CSV: sample_data.csv")

# Reading from CSV
df_csv = pd.read_csv('sample_data.csv')
print("\nRead from CSV:")
print(df_csv)

# Writing to JSON
sample_df.to_json('sample_data.json', orient='records', indent=2)
print("\nSaved to JSON: sample_data.json")

# Reading from JSON
df_json = pd.read_json('sample_data.json')
print("\nRead from JSON:")
print(df_json)

# Note: For Excel operations, install openpyxl: pip install openpyxl
"""
# Writing to Excel
sample_df.to_excel('sample_data.xlsx', index=False, sheet_name='Products')

# Reading from Excel
df_excel = pd.read_excel('sample_data.xlsx', sheet_name='Products')
"""

# Cleanup demo files
import os
os.remove('sample_data.csv')
os.remove('sample_data.json')
print("\nDemo files cleaned up!")


# ============================================================
# 4. DATA SELECTION AND INDEXING
# ============================================================
"""
Different ways to select and access data in a DataFrame.
"""

print("\n" + "=" * 60)
print("4. DATA SELECTION AND INDEXING")
print("=" * 60)

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Salary': [50000, 60000, 75000, 55000, 65000]
})

print("Original DataFrame:")
print(df)

# Selecting columns
print("\n--- Column Selection ---")
print(f"Single column (as Series):\n{df['Name']}")
print(f"\nMultiple columns:\n{df[['Name', 'Salary']]}")

# Selecting rows by index with iloc (integer-based)
print("\n--- Row Selection with iloc (integer-based) ---")
print(f"First row:\n{df.iloc[0]}")
print(f"\nRows 1-3:\n{df.iloc[1:4]}")
print(f"\nSpecific cell [2, 1]: {df.iloc[2, 1]}")

# Selecting rows by label with loc (label-based)
print("\n--- Row Selection with loc (label-based) ---")
print(f"Row at index 0:\n{df.loc[0]}")
print(f"\nRows 0-2 with specific columns:\n{df.loc[0:2, ['Name', 'Age']]}")

# Boolean indexing
print("\n--- Boolean Indexing ---")
print(f"People older than 28:\n{df[df['Age'] > 28]}")
print(f"\nPeople in New York or Chicago:\n{df[df['City'].isin(['New York', 'Chicago'])]}")

# Multiple conditions
condition = (df['Age'] > 25) & (df['Salary'] > 55000)
print(f"\nAge > 25 AND Salary > 55000:\n{df[condition]}")

# Query method (SQL-like)
print(f"\nUsing query method:\n{df.query('Age > 28 and Salary > 60000')}")


# ============================================================
# 5. HANDLING MISSING DATA
# ============================================================
"""
Real-world data often contains missing values. Pandas provides
tools to detect, fill, or drop missing data.
"""

print("\n" + "=" * 60)
print("5. HANDLING MISSING DATA")
print("=" * 60)

# Create DataFrame with missing values
df_missing = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, np.nan, 5],
    'C': [1, 2, 3, 4, np.nan],
    'D': ['a', 'b', None, 'd', 'e']
})

print("DataFrame with missing values:")
print(df_missing)

# Detecting missing values
print(f"\nMissing value check:\n{df_missing.isnull()}")
print(f"\nCount of missing values per column:\n{df_missing.isnull().sum()}")
print(f"\nTotal missing values: {df_missing.isnull().sum().sum()}")

# Dropping missing values
print(f"\nDrop rows with any NaN:\n{df_missing.dropna()}")
print(f"\nDrop rows where all values are NaN:\n{df_missing.dropna(how='all')}")
print(f"\nDrop columns with NaN:\n{df_missing.dropna(axis=1)}")

# Filling missing values
print(f"\nFill with specific value:\n{df_missing.fillna(0)}")
print(f"\nFill with mean (numeric columns):\n{df_missing.fillna(df_missing.mean(numeric_only=True))}")

# Forward fill and backward fill
print(f"\nForward fill:\n{df_missing.ffill()}")
print(f"\nBackward fill:\n{df_missing.bfill()}")


# ============================================================
# 6. DATA MANIPULATION
# ============================================================
"""
Common data manipulation operations: sorting, adding/removing
columns, renaming, and applying functions.
"""

print("\n" + "=" * 60)
print("6. DATA MANIPULATION")
print("=" * 60)

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'Salary': [50000, 60000, 75000, 55000, 65000],
    'Department': ['HR', 'IT', 'IT', 'Sales', 'HR']
})

print("Original DataFrame:")
print(df)

# Sorting
print("\n--- Sorting ---")
print(f"Sort by Age:\n{df.sort_values('Age')}")
print(f"\nSort by Salary (descending):\n{df.sort_values('Salary', ascending=False)}")
print(f"\nSort by multiple columns:\n{df.sort_values(['Department', 'Salary'])}")

# Adding new columns
print("\n--- Adding Columns ---")
df['Bonus'] = df['Salary'] * 0.10
df['Tax'] = df['Salary'] * 0.25
print(df)

# Removing columns
print("\n--- Removing Columns ---")
df_dropped = df.drop(columns=['Tax'])
print(df_dropped)

# Renaming columns
print("\n--- Renaming Columns ---")
df_renamed = df.rename(columns={'Name': 'Employee', 'Salary': 'Annual_Salary'})
print(df_renamed.columns.tolist())

# Applying functions
print("\n--- Applying Functions ---")
df['Name_Upper'] = df['Name'].apply(lambda x: x.upper())
df['Age_Category'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Senior')
print(df[['Name', 'Name_Upper', 'Age', 'Age_Category']])

# Apply to entire DataFrame
print(f"\nApply function to numeric columns:\n{df[['Age', 'Salary']].apply(lambda x: x.max())}")


# ============================================================
# 7. GROUPBY AND AGGREGATION
# ============================================================
"""
Grouping data and performing aggregate operations is essential
for data analysis. Similar to SQL GROUP BY.
"""

print("\n" + "=" * 60)
print("7. GROUPBY AND AGGREGATION")
print("=" * 60)

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Department': ['HR', 'IT', 'IT', 'Sales', 'HR', 'Sales'],
    'Salary': [50000, 60000, 75000, 55000, 52000, 58000],
    'Years': [2, 5, 8, 3, 4, 6]
})

print("Original DataFrame:")
print(df)

# Basic groupby
print("\n--- Basic GroupBy ---")
grouped = df.groupby('Department')
print(f"Mean salary by department:\n{grouped['Salary'].mean()}")

# Multiple aggregations
print("\n--- Multiple Aggregations ---")
agg_result = grouped.agg({
    'Salary': ['mean', 'sum', 'count'],
    'Years': ['mean', 'max']
})
print(agg_result)

# Named aggregations (pandas 0.25+)
print("\n--- Named Aggregations ---")
named_agg = df.groupby('Department').agg(
    avg_salary=('Salary', 'mean'),
    total_salary=('Salary', 'sum'),
    employee_count=('Name', 'count'),
    max_years=('Years', 'max')
)
print(named_agg)

# Group by multiple columns
print("\n--- Group by Multiple Columns ---")
df['Performance'] = ['Good', 'Excellent', 'Good', 'Good', 'Excellent', 'Good']
multi_group = df.groupby(['Department', 'Performance'])['Salary'].mean()
print(multi_group)

# Value counts
print(f"\n--- Value Counts ---")
print(f"Department distribution:\n{df['Department'].value_counts()}")


# ============================================================
# 8. MERGING AND JOINING DATAFRAMES
# ============================================================
"""
Combining DataFrames is similar to SQL JOIN operations.
"""

print("\n" + "=" * 60)
print("8. MERGING AND JOINING DATAFRAMES")
print("=" * 60)

# Create sample DataFrames
employees = pd.DataFrame({
    'emp_id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'dept_id': [101, 102, 101, 103, 102]
})

departments = pd.DataFrame({
    'dept_id': [101, 102, 103, 104],
    'dept_name': ['HR', 'IT', 'Sales', 'Marketing']
})

salaries = pd.DataFrame({
    'emp_id': [1, 2, 3, 4, 6],
    'salary': [50000, 60000, 55000, 58000, 70000]
})

print("Employees DataFrame:")
print(employees)
print("\nDepartments DataFrame:")
print(departments)
print("\nSalaries DataFrame:")
print(salaries)

# Inner join (default)
print("\n--- Inner Join ---")
inner_merge = pd.merge(employees, departments, on='dept_id')
print(inner_merge)

# Left join
print("\n--- Left Join ---")
left_merge = pd.merge(employees, salaries, on='emp_id', how='left')
print(left_merge)

# Right join
print("\n--- Right Join ---")
right_merge = pd.merge(employees, salaries, on='emp_id', how='right')
print(right_merge)

# Outer join
print("\n--- Outer Join ---")
outer_merge = pd.merge(employees, salaries, on='emp_id', how='outer')
print(outer_merge)

# Concatenating DataFrames
print("\n--- Concatenating DataFrames ---")
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
concatenated = pd.concat([df1, df2], ignore_index=True)
print(f"Vertically concatenated:\n{concatenated}")

# Horizontal concatenation
horizontal = pd.concat([df1, df2], axis=1)
print(f"\nHorizontally concatenated:\n{horizontal}")


# ============================================================
# 9. STATISTICAL OPERATIONS
# ============================================================
"""
Pandas provides comprehensive statistical functions for data analysis.
"""

print("\n" + "=" * 60)
print("9. STATISTICAL OPERATIONS")
print("=" * 60)

df = pd.DataFrame({
    'A': [10, 20, 30, 40, 50],
    'B': [15, 25, 35, 45, 55],
    'C': [100, 200, 150, 300, 250]
})

print("DataFrame:")
print(df)

# Descriptive statistics
print("\n--- Descriptive Statistics ---")
print(df.describe())

# Individual statistics
print(f"\n--- Individual Statistics ---")
print(f"Mean:\n{df.mean()}")
print(f"\nMedian:\n{df.median()}")
print(f"\nStandard Deviation:\n{df.std()}")
print(f"\nVariance:\n{df.var()}")
print(f"\nMin:\n{df.min()}")
print(f"\nMax:\n{df.max()}")

# Correlation and covariance
print(f"\n--- Correlation Matrix ---")
print(df.corr())

print(f"\n--- Covariance Matrix ---")
print(df.cov())

# Cumulative operations
print(f"\n--- Cumulative Operations ---")
print(f"Cumulative sum:\n{df['A'].cumsum()}")
print(f"\nCumulative max:\n{df['A'].cummax()}")

# Percentiles
print(f"\n--- Percentiles ---")
print(f"25th percentile: {df['C'].quantile(0.25)}")
print(f"50th percentile: {df['C'].quantile(0.50)}")
print(f"75th percentile: {df['C'].quantile(0.75)}")


# ============================================================
# 10. DATA TRANSFORMATION
# ============================================================
"""
Transform and reshape data for different analytical needs.
"""

print("\n" + "=" * 60)
print("10. DATA TRANSFORMATION")
print("=" * 60)

df = pd.DataFrame({
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
    'City': ['NYC', 'LA', 'NYC', 'LA'],
    'Temperature': [32, 65, 35, 68],
    'Humidity': [45, 30, 50, 35]
})

print("Original DataFrame:")
print(df)

# Pivot table
print("\n--- Pivot Table ---")
pivot = df.pivot_table(
    values='Temperature',
    index='Date',
    columns='City',
    aggfunc='mean'
)
print(pivot)

# Melting (wide to long format)
print("\n--- Melting ---")
df_wide = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'Math': [90, 85],
    'Science': [88, 92],
    'English': [95, 78]
})
print(f"Wide format:\n{df_wide}")

df_long = pd.melt(df_wide, id_vars=['Name'], var_name='Subject', value_name='Score')
print(f"\nLong format (melted):\n{df_long}")

# Crosstab
print("\n--- Crosstab ---")
df_survey = pd.DataFrame({
    'Gender': ['M', 'F', 'M', 'F', 'M', 'F'],
    'Response': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes']
})
print(pd.crosstab(df_survey['Gender'], df_survey['Response']))

# Binning/Discretization
print("\n--- Binning ---")
ages = pd.Series([22, 35, 45, 28, 55, 18, 65, 40])
bins = [0, 25, 40, 60, 100]
labels = ['Young', 'Adult', 'Middle-aged', 'Senior']
age_groups = pd.cut(ages, bins=bins, labels=labels)
print(f"Ages: {ages.tolist()}")
print(f"Age groups: {age_groups.tolist()}")


# ============================================================
# 11. STRING OPERATIONS
# ============================================================
"""
Pandas provides vectorized string operations through the .str accessor.
"""

print("\n" + "=" * 60)
print("11. STRING OPERATIONS")
print("=" * 60)

df = pd.DataFrame({
    'Name': ['Alice Smith', 'Bob Jones', 'Charlie Brown', 'Diana Prince'],
    'Email': ['alice@email.com', 'BOB@EMAIL.COM', 'charlie@email.com', 'diana@email.com']
})

print("Original DataFrame:")
print(df)

# String methods
print("\n--- String Methods ---")
print(f"Uppercase:\n{df['Name'].str.upper()}")
print(f"\nLowercase:\n{df['Email'].str.lower()}")
print(f"\nName length:\n{df['Name'].str.len()}")

# Split and extract
print("\n--- Split and Extract ---")
df['First_Name'] = df['Name'].str.split(' ').str[0]
df['Last_Name'] = df['Name'].str.split(' ').str[1]
print(df[['Name', 'First_Name', 'Last_Name']])

# Contains
print(f"\n--- Contains ---")
print(f"Names containing 'a':\n{df['Name'].str.contains('a', case=False)}")

# Replace
print(f"\n--- Replace ---")
print(f"Replace email domain:\n{df['Email'].str.replace('email.com', 'newdomain.com')}")

# Strip whitespace
messy = pd.Series(['  hello  ', ' world ', '  python  '])
print(f"\nStrip whitespace: {messy.str.strip().tolist()}")


# ============================================================
# 12. DATETIME OPERATIONS
# ============================================================
"""
Pandas has extensive support for datetime operations.
"""

print("\n" + "=" * 60)
print("12. DATETIME OPERATIONS")
print("=" * 60)

# Create datetime data
df = pd.DataFrame({
    'date_string': ['2024-01-15', '2024-03-20', '2024-06-10', '2024-09-25', '2024-12-31']
})

# Convert to datetime
df['date'] = pd.to_datetime(df['date_string'])
print("DataFrame with datetime:")
print(df)
print(f"\nData types:\n{df.dtypes}")

# Extract datetime components
print("\n--- Datetime Components ---")
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['day_name'] = df['date'].dt.day_name()
df['quarter'] = df['date'].dt.quarter
print(df[['date', 'year', 'month', 'day', 'day_name', 'quarter']])

# Date arithmetic
print("\n--- Date Arithmetic ---")
df['next_week'] = df['date'] + pd.Timedelta(days=7)
df['prev_month'] = df['date'] - pd.DateOffset(months=1)
print(df[['date', 'next_week', 'prev_month']])

# Date range
print("\n--- Date Range ---")
date_range = pd.date_range(start='2024-01-01', periods=5, freq='W')
print(f"Weekly dates: {date_range.tolist()}")

date_range_monthly = pd.date_range(start='2024-01-01', end='2024-06-01', freq='MS')
print(f"Monthly start dates: {date_range_monthly.tolist()}")

# Filtering by date
print("\n--- Filtering by Date ---")
df_filtered = df[df['date'] > '2024-06-01']
print(f"Dates after June 2024:\n{df_filtered[['date']]}")


# ============================================================
# 13. PRACTICAL EXAMPLES
# ============================================================
"""
Real-world examples combining multiple pandas concepts.
"""

print("\n" + "=" * 60)
print("13. PRACTICAL EXAMPLES")
print("=" * 60)

# Example 1: Sales Data Analysis
print("\n--- Example 1: Sales Data Analysis ---")
sales = pd.DataFrame({
    'Date': pd.date_range('2024-01-01', periods=10, freq='D'),
    'Product': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],
    'Region': ['East', 'West', 'East', 'West', 'East', 'West', 'East', 'West', 'East', 'West'],
    'Units': [100, 150, 200, 120, 180, 90, 160, 200, 140, 110],
    'Price': [10.0, 15.0, 10.0, 20.0, 15.0, 10.0, 20.0, 15.0, 10.0, 20.0]
})
sales['Revenue'] = sales['Units'] * sales['Price']

print("Sales Data:")
print(sales)

print(f"\nTotal Revenue: ${sales['Revenue'].sum():,.2f}")
print(f"\nRevenue by Product:\n{sales.groupby('Product')['Revenue'].sum()}")
print(f"\nRevenue by Region:\n{sales.groupby('Region')['Revenue'].sum()}")

# Example 2: Data Cleaning Pipeline
print("\n--- Example 2: Data Cleaning Pipeline ---")
dirty_data = pd.DataFrame({
    'name': ['  Alice  ', 'bob', 'CHARLIE', None, 'Diana'],
    'age': [25, -5, 150, 30, 28],
    'email': ['alice@email.com', 'invalid', 'charlie@email.com', 'diana@email.com', 'eve@email.com']
})

print("Dirty data:")
print(dirty_data)

# Clean the data
cleaned = dirty_data.copy()
cleaned['name'] = cleaned['name'].str.strip().str.title()  # Clean names
cleaned.loc[cleaned['age'] < 0, 'age'] = np.nan  # Invalid ages
cleaned.loc[cleaned['age'] > 120, 'age'] = np.nan  # Invalid ages
cleaned = cleaned.dropna()  # Remove rows with missing values

print("\nCleaned data:")
print(cleaned)


# ============================================================
# SUMMARY AND CHEAT SHEET
# ============================================================
"""
PANDAS QUICK REFERENCE:

CREATING DATAFRAMES:
├── pd.DataFrame(dict)           - From dictionary
├── pd.DataFrame(list)           - From list of lists
├── pd.read_csv('file.csv')      - From CSV file
├── pd.read_excel('file.xlsx')   - From Excel file
└── pd.read_json('file.json')    - From JSON file

SELECTION:
├── df['column']                 - Select column
├── df[['col1', 'col2']]         - Select multiple columns
├── df.iloc[row, col]            - Select by integer position
├── df.loc[label, column]        - Select by label
└── df[df['col'] > value]        - Boolean indexing

MANIPULATION:
├── df.sort_values('col')        - Sort by column
├── df.drop(columns=['col'])     - Drop column
├── df.rename(columns={})        - Rename columns
├── df.apply(func)               - Apply function
└── df.assign(new_col=values)    - Add new column

AGGREGATION:
├── df.groupby('col').mean()     - Group and aggregate
├── df.agg({'col': ['sum']})     - Multiple aggregations
├── df.pivot_table()             - Create pivot table
└── df.value_counts()            - Count values

MISSING DATA:
├── df.isnull()                  - Check for missing
├── df.dropna()                  - Drop missing values
├── df.fillna(value)             - Fill missing values
└── df.interpolate()             - Interpolate missing

MERGING:
├── pd.merge(df1, df2)           - SQL-style join
├── pd.concat([df1, df2])        - Concatenate DataFrames
└── df1.join(df2)                - Join on index

STATISTICS:
├── df.describe()                - Summary statistics
├── df.mean(), df.std()          - Mean, standard deviation
├── df.corr()                    - Correlation matrix
└── df.quantile()                - Percentiles
"""

print("\n" + "=" * 60)
print("PANDAS BASICS COMPLETE!")
print("=" * 60)
print("""
Key Takeaways:
1. Series = 1D labeled array
2. DataFrame = 2D labeled table (like Excel/SQL)
3. Use .loc for label-based, .iloc for position-based selection
4. GroupBy for aggregation (like SQL GROUP BY)
5. merge/concat for combining DataFrames
6. Handle missing data with dropna/fillna
7. Use .str for string operations, .dt for datetime

Next Steps:
- Practice with real datasets (Kaggle, UCI ML Repository)
- Explore matplotlib/seaborn for visualization
- Learn advanced pandas (MultiIndex, window functions)
""")
print("=" * 60)
