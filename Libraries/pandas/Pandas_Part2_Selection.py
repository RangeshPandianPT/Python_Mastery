# =============================================================================
# PANDAS PART 2 - DATA SELECTION & FILTERING (Beginner-Intermediate)
# =============================================================================
# Mastering data selection is key to working effectively with Pandas.
# This covers all the ways to access and filter your data.

import pandas as pd
import numpy as np

# Sample DataFrame for this tutorial
data = {
    'Name': ['Rahul', 'Priya', 'Amit', 'Sneha', 'Vikram', 'Anjali'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'IT', 'HR'],
    'Age': [25, 30, 28, 35, 32, 27],
    'Salary': [50000, 65000, 55000, 70000, 60000, 52000],
    'Experience': [2, 5, 3, 8, 6, 4]
}
df = pd.DataFrame(data)
print("Sample DataFrame:")
print(df)
print()

# =============================================================================
# 1. COLUMN SELECTION REVISITED
# =============================================================================
print("--- Column Selection ---")

# Single column (two ways)
print("\nUsing bracket notation:")
print(df['Name'])

print("\nUsing dot notation (only works for simple column names):")
print(df.Name)

# Note: Dot notation doesn't work if column name has spaces or matches a method

# Multiple columns - order matters!
print("\nSelect specific columns in order:")
print(df[['Salary', 'Name', 'Department']])

# =============================================================================
# 2. iloc - INTEGER LOCATION BASED SELECTION
# =============================================================================
print("\n--- iloc: Position-Based Selection ---")
# Think of iloc as "integer location"
# Uses row/column NUMBERS (0-based indexing)

# Single cell: iloc[row, column]
print("\nCell at row 0, column 1:")
print(df.iloc[0, 1])  # 'IT'

# Single row (returns Series)
print("\nRow 2:")
print(df.iloc[2])

# Multiple rows
print("\nRows 1, 3, and 4:")
print(df.iloc[[1, 3, 4]])

# Row slicing
print("\nRows 1 to 3 (not including 4):")
print(df.iloc[1:4])

# Specific rows and columns
print("\nRows 0-2, Columns 0-2:")
print(df.iloc[0:3, 0:3])

# All rows, specific columns
print("\nAll rows, columns 1 and 3:")
print(df.iloc[:, [1, 3]])

# Last row
print("\nLast row:")
print(df.iloc[-1])

# Last 2 rows, last 2 columns
print("\nLast 2 rows, last 2 columns:")
print(df.iloc[-2:, -2:])

# =============================================================================
# 3. loc - LABEL BASED SELECTION
# =============================================================================
print("\n--- loc: Label-Based Selection ---")
# Think of loc as "location by label"
# Uses row INDEX and column NAMES

# First, let's set a meaningful index
df_indexed = df.set_index('Name')
print("\nDataFrame with Name as index:")
print(df_indexed)

# Single row by label
print("\nRow for 'Amit':")
print(df_indexed.loc['Amit'])

# Multiple rows by label
print("\nRows for Rahul and Sneha:")
print(df_indexed.loc[['Rahul', 'Sneha']])

# Specific cell
print("\nAmit's Salary:")
print(df_indexed.loc['Amit', 'Salary'])

# Row range by label (inclusive on both ends!)
print("\nRows from Priya to Sneha:")
print(df_indexed.loc['Priya':'Sneha'])

# Specific rows and columns
print("\nSelected rows and columns:")
print(df_indexed.loc[['Rahul', 'Vikram'], ['Department', 'Salary']])

# Back to original index for other examples
df = df.reset_index(drop=True) if 'Name' not in df.columns else df

# =============================================================================
# 4. BOOLEAN FILTERING
# =============================================================================
print("\n--- Boolean Filtering ---")

# Basic condition
print("\nEmployees older than 28:")
print(df[df['Age'] > 28])

# Equality check
print("\nIT Department employees:")
print(df[df['Department'] == 'IT'])

# Not equal
print("\nNon-IT employees:")
print(df[df['Department'] != 'IT'])

# Multiple conditions - use & (and), | (or)
# IMPORTANT: Wrap each condition in parentheses!
print("\nIT employees earning more than 55000:")
print(df[(df['Department'] == 'IT') & (df['Salary'] > 55000)])

print("\nHR or Finance department:")
print(df[(df['Department'] == 'HR') | (df['Department'] == 'Finance')])

# Using isin() for multiple values
print("\nEmployees in IT or Finance:")
print(df[df['Department'].isin(['IT', 'Finance'])])

# Negation with ~
print("\nEmployees NOT in IT or Finance:")
print(df[~df['Department'].isin(['IT', 'Finance'])])

# =============================================================================
# 5. QUERY METHOD
# =============================================================================
print("\n--- Query Method (cleaner syntax) ---")

# query() lets you write SQL-like conditions
print("\nUsing query - Age > 28:")
print(df.query('Age > 28'))

print("\nQuery with multiple conditions:")
print(df.query('Department == "IT" and Salary > 55000'))

# Using variables in query
min_salary = 55000
print(f"\nQuery with variable (salary > {min_salary}):")
print(df.query('Salary > @min_salary'))

# =============================================================================
# 6. STRING FILTERING
# =============================================================================
print("\n--- String Filtering ---")

# Names starting with 'A'
print("\nNames starting with 'A':")
print(df[df['Name'].str.startswith('A')])

# Names containing 'a' (case insensitive)
print("\nNames containing 'a':")
print(df[df['Name'].str.lower().str.contains('a')])

# Names with exactly 5 characters
print("\nNames with 5 characters:")
print(df[df['Name'].str.len() == 5])

# =============================================================================
# 7. SELECTING WITH WHERE
# =============================================================================
print("\n--- Where Method ---")

# where() keeps shape but replaces non-matching with NaN
print("\nSalaries where > 55000 (others become NaN):")
print(df['Salary'].where(df['Salary'] > 55000))

# With replacement value
print("\nReplace low salaries with 0:")
print(df['Salary'].where(df['Salary'] > 55000, 0))

# =============================================================================
# 8. SELECTING TOP/BOTTOM VALUES
# =============================================================================
print("\n--- Top/Bottom Selection ---")

# Top 3 by Salary
print("\nTop 3 highest salaries:")
print(df.nlargest(3, 'Salary'))

# Bottom 2 by Age
print("\nYoungest 2 employees:")
print(df.nsmallest(2, 'Age'))

# =============================================================================
# 9. RANDOM SAMPLING
# =============================================================================
print("\n--- Random Sampling ---")

# Random rows
print("\n3 random employees:")
print(df.sample(n=3))

# Fraction of data
print("\n50% random sample:")
print(df.sample(frac=0.5))

# With replacement (for bootstrapping)
print("\n3 samples with replacement:")
print(df.sample(n=3, replace=True))

# =============================================================================
# 10. COMBINING SELECTION METHODS
# =============================================================================
print("\n--- Combining Methods ---")

# Chain operations for complex selection
result = (df
    [df['Department'] == 'IT']     # Filter IT
    [['Name', 'Salary']]           # Select columns
    .sort_values('Salary', ascending=False)  # Sort
)
print("\nIT employees sorted by salary:")
print(result)

print("\n" + "=" * 55)
print("PANDAS PART 2 - SELECTION & FILTERING COMPLETE!")
print("=" * 55)
