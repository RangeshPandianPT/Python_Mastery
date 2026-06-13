# =============================================================================
# PANDAS PART 3 - DATA MANIPULATION (Intermediate)
# =============================================================================
# Learn how to transform, clean, and reshape your data effectively.
# These operations form the core of data wrangling with Pandas.

import pandas as pd
import numpy as np

# =============================================================================
# 1. ADDING AND REMOVING COLUMNS
# =============================================================================
print("--- Adding and Removing Columns ---")

df = pd.DataFrame({
    'Name': ['Rahul', 'Priya', 'Amit', 'Sneha'],
    'Age': [25, 30, 28, 35],
    'Salary': [50000, 65000, 55000, 70000]
})
print("Original DataFrame:")
print(df)

# Add column - direct assignment
df['Department'] = ['IT', 'HR', 'IT', 'Finance']
print("\nAfter adding Department:")
print(df)

# Add column with calculation
df['Tax'] = df['Salary'] * 0.1
print("\nAfter adding Tax column:")
print(df)

# Insert at specific position
df.insert(2, 'City', ['Mumbai', 'Delhi', 'Chennai', 'Pune'])
print("\nAfter inserting City at position 2:")
print(df)

# Drop columns
df_dropped = df.drop(columns=['Tax'])
print("\nAfter dropping Tax:")
print(df_dropped)

# Drop multiple columns
df_clean = df.drop(columns=['Tax', 'City'])
print("\nAfter dropping Tax and City:")
print(df_clean)

# =============================================================================
# 2. ADDING AND REMOVING ROWS
# =============================================================================
print("\n--- Adding and Removing Rows ---")

# Add single row using loc
df.loc[4] = ['Vikram', 32, 'Bangalore', 60000, 'IT', 6000]
print("\nAfter adding Vikram:")
print(df)

# Add row using concat (preferred for multiple rows)
new_row = pd.DataFrame([{
    'Name': 'Anjali', 'Age': 27, 'City': 'Kolkata',
    'Salary': 52000, 'Department': 'HR', 'Tax': 5200
}])
df = pd.concat([df, new_row], ignore_index=True)
print("\nAfter adding Anjali with concat:")
print(df)

# Drop rows by index
df_no_first = df.drop(index=[0])
print("\nAfter dropping first row:")
print(df_no_first)

# Drop rows by condition
df_high_salary = df[df['Salary'] >= 55000]
print("\nKeeping only salary >= 55000:")
print(df_high_salary)

# =============================================================================
# 3. MODIFYING VALUES
# =============================================================================
print("\n--- Modifying Values ---")

# Modify single cell
df.loc[0, 'Salary'] = 52000
print("\nAfter updating Rahul's salary:")
print(df)

# Modify entire column
df['Salary'] = df['Salary'] * 1.1  # 10% raise for all
print("\nAfter 10% raise for all:")
print(df)

# Conditional modification
df.loc[df['Department'] == 'IT', 'Salary'] *= 1.05  # Extra 5% for IT
print("\nAfter extra 5% for IT:")
print(df)

# =============================================================================
# 4. RENAMING COLUMNS AND INDEX
# =============================================================================
print("\n--- Renaming ---")

# Rename specific columns
df_renamed = df.rename(columns={'Name': 'Employee', 'Salary': 'Annual_Salary'})
print("\nRenamed columns:")
print(df_renamed.head(2))

# Rename all columns at once
df.columns = ['Emp_Name', 'Emp_Age', 'Emp_City', 'Emp_Salary', 'Dept', 'Tax_Amount']
print("\nAll columns renamed:")
print(df.head(2))

# Reset to original names
df.columns = ['Name', 'Age', 'City', 'Salary', 'Department', 'Tax']

# Rename index
df_indexed = df.set_index('Name')
df_indexed = df_indexed.rename(index={'Rahul': 'Rahul_K', 'Priya': 'Priya_S'})
print("\nRenamed index:")
print(df_indexed.head(2))

# =============================================================================
# 5. SORTING DATA
# =============================================================================
print("\n--- Sorting Data ---")

# Sort by single column
print("\nSorted by Age (ascending):")
print(df.sort_values('Age'))

# Sort descending
print("\nSorted by Salary (descending):")
print(df.sort_values('Salary', ascending=False))

# Sort by multiple columns
print("\nSorted by Department, then Salary:")
print(df.sort_values(['Department', 'Salary'], ascending=[True, False]))

# Sort and reset index
df_sorted = df.sort_values('Salary', ascending=False).reset_index(drop=True)
print("\nSorted with reset index:")
print(df_sorted)

# Sort by index
print("\nSorted by index:")
print(df.sort_index())

# =============================================================================
# 6. HANDLING DUPLICATES
# =============================================================================
print("\n--- Handling Duplicates ---")

# Create data with duplicates
dup_data = pd.DataFrame({
    'Name': ['Rahul', 'Priya', 'Rahul', 'Amit', 'Priya'],
    'Score': [85, 90, 85, 78, 92]
})
print("\nData with duplicates:")
print(dup_data)

# Check for duplicates
print("\nDuplicate rows:", dup_data.duplicated().sum())
print("\nWhich rows are duplicates:")
print(dup_data.duplicated())

# Drop all duplicates
print("\nAfter dropping duplicates:")
print(dup_data.drop_duplicates())

# Keep last occurrence
print("\nKeeping last occurrence:")
print(dup_data.drop_duplicates(keep='last'))

# Check duplicates in specific column
print("\nDuplicate names:")
print(dup_data[dup_data.duplicated(subset=['Name'], keep=False)])

# =============================================================================
# 7. APPLY AND MAP FUNCTIONS
# =============================================================================
print("\n--- Apply and Map ---")

# apply() - apply function to column or row
df['Salary_Grade'] = df['Salary'].apply(
    lambda x: 'High' if x > 60000 else 'Medium' if x > 50000 else 'Low'
)
print("\nWith Salary Grade:")
print(df[['Name', 'Salary', 'Salary_Grade']])

# apply() on entire row (axis=1)
def summarize(row):
    return f"{row['Name']} from {row['City']}"

df['Summary'] = df.apply(summarize, axis=1)
print("\nWith Summary column:")
print(df[['Name', 'City', 'Summary']])

# map() - map values using dictionary
dept_codes = {'IT': 'D01', 'HR': 'D02', 'Finance': 'D03'}
df['Dept_Code'] = df['Department'].map(dept_codes)
print("\nWith Department Codes:")
print(df[['Department', 'Dept_Code']])

# replace() - replace specific values
df['Department'] = df['Department'].replace({'IT': 'Technology', 'HR': 'Human Resources'})
print("\nAfter replacing department names:")
print(df['Department'].unique())

# =============================================================================
# 8. CHANGING DATA TYPES
# =============================================================================
print("\n--- Changing Data Types ---")

# Check current types
print("\nCurrent data types:")
print(df.dtypes)

# Convert to string
df['Age_str'] = df['Age'].astype(str)
print("\nAge as string type:", df['Age_str'].dtype)

# Convert to category (memory efficient for repeated values)
df['Department'] = df['Department'].astype('category')
print("Department as category:", df['Department'].dtype)

# Convert to numeric (handles errors)
mixed_series = pd.Series(['1', '2', 'three', '4'])
numeric_series = pd.to_numeric(mixed_series, errors='coerce')  # 'three' becomes NaN
print("\nMixed to numeric (errors coerced):")
print(numeric_series)

# =============================================================================
# 9. CREATING BINS
# =============================================================================
print("\n--- Binning/Discretization ---")

# cut() - create bins with specified edges
age_bins = [0, 25, 30, 35, 100]
age_labels = ['Young', 'Mid', 'Senior', 'Veteran']
df['Age_Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)
print("\nWith Age Groups:")
print(df[['Name', 'Age', 'Age_Group']])

# qcut() - create bins with equal frequency
df['Salary_Quartile'] = pd.qcut(df['Salary'], q=4, labels=['Q1', 'Q2', 'Q3', 'Q4'])
print("\nWith Salary Quartiles:")
print(df[['Name', 'Salary', 'Salary_Quartile']])

# =============================================================================
# 10. COPYING DATAFRAMES
# =============================================================================
print("\n--- Copying DataFrames ---")

# IMPORTANT: Assignment creates a reference, not a copy!
df_ref = df  # Both point to same data

# Create independent copy
df_copy = df.copy()
print("Created independent copy with .copy()")

# Clean up extra columns for final view
final_df = df[['Name', 'Age', 'City', 'Salary', 'Department']].copy()
print("\nFinal cleaned DataFrame:")
print(final_df)

print("\n" + "=" * 55)
print("PANDAS PART 3 - DATA MANIPULATION COMPLETE!")
print("=" * 55)
