# =============================================================================
# PANDAS PART 1 - BASICS (Beginner Level)
# =============================================================================
# Pandas is the go-to library for data manipulation and analysis in Python.
# Built on top of NumPy, it provides fast and flexible data structures.

import pandas as pd
import numpy as np

# =============================================================================
# 1. WHAT IS PANDAS?
# =============================================================================
"""
Pandas provides two main data structures:
    - Series: 1-dimensional labeled array (like a column)
    - DataFrame: 2-dimensional labeled table (like a spreadsheet)

Why use Pandas?
    - Handles missing data gracefully
    - Easy data alignment and merging
    - Powerful grouping and aggregation
    - Built-in file reading (CSV, Excel, SQL, etc.)
"""

# =============================================================================
# 2. CREATING A SERIES
# =============================================================================

# ----- From a Python List -----
s = pd.Series([10, 20, 30, 40, 50])
print("Basic Series:")
print(s)
print()

# Notice the index on the left (0, 1, 2, 3, 4)
print("Index:", s.index.tolist())
print("Values:", s.values)

# ----- With Custom Index -----
temps = pd.Series([22.5, 24.1, 19.8, 21.3], 
                  index=['Mon', 'Tue', 'Wed', 'Thu'])
print("\nTemperatures with custom index:")
print(temps)

# Access by label
print("\nTuesday temp:", temps['Tue'])

# ----- From a Dictionary -----
population = pd.Series({
    'Delhi': 29000000,
    'Mumbai': 21000000,
    'Kolkata': 15000000,
    'Chennai': 11000000
})
print("\nPopulation Series from dict:")
print(population)

# =============================================================================
# 3. SERIES OPERATIONS
# =============================================================================

prices = pd.Series([100, 200, 150, 300], index=['A', 'B', 'C', 'D'])
print("\nProduct Prices:")
print(prices)

# Basic stats
print("\nTotal:", prices.sum())
print("Average:", prices.mean())
print("Max:", prices.max())
print("Min:", prices.min())

# Arithmetic (applies to all elements)
discounted = prices * 0.9  # 10% off
print("\nAfter 10% discount:")
print(discounted)

# Boolean filtering
expensive = prices[prices > 150]
print("\nItems over 150:")
print(expensive)

# =============================================================================
# 4. CREATING A DATAFRAME
# =============================================================================

# ----- From a Dictionary of Lists -----
# Most common way to create a DataFrame

data = {
    'Name': ['Rahul', 'Priya', 'Amit', 'Sneha'],
    'Age': [25, 30, 28, 35],
    'City': ['Mumbai', 'Delhi', 'Chennai', 'Pune'],
    'Salary': [50000, 65000, 55000, 70000]
}
df = pd.DataFrame(data)
print("\nEmployee DataFrame:")
print(df)

# ----- From List of Dictionaries -----
# Useful when each row is a separate record

records = [
    {'Product': 'Laptop', 'Price': 50000, 'Stock': 10},
    {'Product': 'Phone', 'Price': 20000, 'Stock': 25},
    {'Product': 'Tablet', 'Price': 30000, 'Stock': 15}
]
products_df = pd.DataFrame(records)
print("\nProducts DataFrame:")
print(products_df)

# ----- From 2D NumPy Array -----
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df_numpy = pd.DataFrame(arr, columns=['X', 'Y', 'Z'])
print("\nDataFrame from NumPy array:")
print(df_numpy)

# =============================================================================
# 5. DATAFRAME ATTRIBUTES
# =============================================================================
print("\n--- DataFrame Attributes ---")
print("Shape (rows, cols):", df.shape)
print("Columns:", df.columns.tolist())
print("Index:", df.index.tolist())
print("Data Types:")
print(df.dtypes)

# Number of elements
print("\nTotal cells:", df.size)
print("Dimensions:", df.ndim)

# =============================================================================
# 6. VIEWING DATA
# =============================================================================
print("\n--- Viewing Data ---")

# First N rows
print("\nFirst 2 rows:")
print(df.head(2))

# Last N rows
print("\nLast 2 rows:")
print(df.tail(2))

# Random sample
print("\n2 Random rows:")
print(df.sample(2))

# Quick info about DataFrame
print("\nDataFrame Info:")
print(df.info())

# Statistical summary (numeric columns only)
print("\nStatistical Summary:")
print(df.describe())

# =============================================================================
# 7. BASIC COLUMN SELECTION
# =============================================================================
print("\n--- Column Selection ---")

# Single column (returns Series)
names = df['Name']
print("\nNames (as Series):")
print(names)
print("Type:", type(names))

# Multiple columns (returns DataFrame)
subset = df[['Name', 'Salary']]
print("\nName and Salary (as DataFrame):")
print(subset)
print("Type:", type(subset))

# =============================================================================
# 8. ADDING NEW COLUMNS
# =============================================================================
print("\n--- Adding Columns ---")

# Direct assignment
df['Experience'] = [2, 5, 3, 8]
print("\nWith Experience column:")
print(df)

# Calculated column
df['Monthly_Salary'] = df['Salary'] / 12
print("\nWith Monthly Salary:")
print(df)

# Based on condition
df['Senior'] = df['Age'] >= 30
print("\nWith Senior flag:")
print(df)

# =============================================================================
# 9. BASIC ROW SELECTION
# =============================================================================
print("\n--- Row Selection ---")

# First row
print("\nFirst row:")
print(df.iloc[0])

# Multiple rows by position
print("\nRows 0 and 2:")
print(df.iloc[[0, 2]])

# Slice of rows
print("\nRows 1 to 2:")
print(df.iloc[1:3])

# =============================================================================
# 10. QUICK DATA EXPLORATION
# =============================================================================
print("\n--- Quick Exploration ---")

# Unique values in a column
print("\nUnique cities:", df['City'].unique())
print("Number of unique cities:", df['City'].nunique())

# Value counts
print("\nAge distribution:")
print(df['Age'].value_counts())

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

print("\n" + "=" * 55)
print("PANDAS PART 1 - BASICS COMPLETE!")
print("=" * 55)
