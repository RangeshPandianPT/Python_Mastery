# =============================================================================
# PANDAS PART 5 - MERGING & JOINING (Intermediate-Advanced)
# =============================================================================
# Combining data from multiple sources is essential in real-world analysis.
# This covers all the ways to merge, join, and concatenate DataFrames.

import pandas as pd
import numpy as np

# =============================================================================
# 1. SAMPLE DATA
# =============================================================================

# Employees table
employees = pd.DataFrame({
    'EmpID': [101, 102, 103, 104, 105],
    'Name': ['Rahul', 'Priya', 'Amit', 'Sneha', 'Vikram'],
    'DeptID': [1, 2, 1, 3, 2]
})

# Departments table
departments = pd.DataFrame({
    'DeptID': [1, 2, 3, 4],
    'DeptName': ['IT', 'HR', 'Finance', 'Marketing'],
    'Location': ['Mumbai', 'Delhi', 'Chennai', 'Pune']
})

# Salaries table
salaries = pd.DataFrame({
    'EmpID': [101, 102, 103, 106],  # Note: 106 doesn't exist in employees
    'Salary': [50000, 65000, 55000, 45000],
    'Bonus': [5000, 7000, 6000, 4000]
})

print("Employees Table:")
print(employees)
print("\nDepartments Table:")
print(departments)
print("\nSalaries Table:")
print(salaries)
print()

# =============================================================================
# 2. MERGE - INNER JOIN (Default)
# =============================================================================
print("--- Inner Join ---")
# Only keeps rows where key exists in BOTH tables

result = pd.merge(employees, departments, on='DeptID')
print("\nEmployees with Department info (inner join):")
print(result)

# With salaries - note that 104, 105 are dropped (no salary record)
# and 106 is dropped (no employee record)
emp_sal = pd.merge(employees, salaries, on='EmpID')
print("\nEmployees with Salary (inner join):")
print(emp_sal)

# =============================================================================
# 3. LEFT JOIN
# =============================================================================
print("\n--- Left Join ---")
# Keep ALL rows from left table, match from right

result = pd.merge(employees, salaries, on='EmpID', how='left')
print("\nAll employees with available salaries:")
print(result)
# Note: Sneha and Vikram have NaN for salary/bonus

# =============================================================================
# 4. RIGHT JOIN
# =============================================================================
print("\n--- Right Join ---")
# Keep ALL rows from right table, match from left

result = pd.merge(employees, salaries, on='EmpID', how='right')
print("\nAll salary records with employee info:")
print(result)
# Note: EmpID 106 has NaN for name and dept

# =============================================================================
# 5. OUTER JOIN (FULL JOIN)
# =============================================================================
print("\n--- Outer Join ---")
# Keep ALL rows from BOTH tables

result = pd.merge(employees, salaries, on='EmpID', how='outer')
print("\nComplete outer join:")
print(result)
# Includes all employees and all salary records

# =============================================================================
# 6. MERGING ON DIFFERENT COLUMN NAMES
# =============================================================================
print("\n--- Merging with Different Column Names ---")

# Create table with different column name
emp_records = pd.DataFrame({
    'EmployeeID': [101, 102, 103],  # Different name but same meaning
    'Performance': ['A', 'B', 'A']
})
print("\nPerformance table (note EmployeeID column):")
print(emp_records)

# Merge using left_on and right_on
result = pd.merge(employees, emp_records, 
                  left_on='EmpID', right_on='EmployeeID')
print("\nMerged with different column names:")
print(result)

# =============================================================================
# 7. MERGING ON INDEX
# =============================================================================
print("\n--- Merging on Index ---")

# Set index for demonstration
emp_indexed = employees.set_index('EmpID')
sal_indexed = salaries.set_index('EmpID')

print("\nEmployees with EmpID as index:")
print(emp_indexed)

# Merge using index
result = pd.merge(emp_indexed, sal_indexed, 
                  left_index=True, right_index=True, how='left')
print("\nMerged on index:")
print(result)

# Mix of index and column
result = pd.merge(emp_indexed, salaries, 
                  left_index=True, right_on='EmpID')
print("\nLeft on index, right on column:")
print(result)

# =============================================================================
# 8. HANDLING DUPLICATE COLUMNS
# =============================================================================
print("\n--- Handling Duplicate Columns ---")

# Both tables have 'Location' column
offices = pd.DataFrame({
    'EmpID': [101, 102, 103],
    'Location': ['Office A', 'Office B', 'Office A']
})
emp_with_loc = employees.copy()
emp_with_loc['Location'] = ['Mumbai', 'Delhi', 'Chennai', 'Pune', 'Mumbai']

print("\nBoth have 'Location' column")
result = pd.merge(emp_with_loc, offices, on='EmpID', suffixes=('_home', '_work'))
print("\nWith custom suffixes:")
print(result)

# =============================================================================
# 9. CONCATENATION
# =============================================================================
print("\n--- Concatenation ---")

# Vertical concatenation (stacking rows)
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
print("\nDF1:")
print(df1)
print("\nDF2:")
print(df2)

# Stack vertically
stacked = pd.concat([df1, df2], ignore_index=True)
print("\nVertically concatenated:")
print(stacked)

# Horizontal concatenation
side_by_side = pd.concat([df1, df2], axis=1)
print("\nHorizontally concatenated:")
print(side_by_side)

# Concatenate with different columns
df3 = pd.DataFrame({'A': [9, 10], 'C': [11, 12]})  # Has 'C' instead of 'B'
result = pd.concat([df1, df3], ignore_index=True)
print("\nWith different columns (NaN filled):")
print(result)

# =============================================================================
# 10. MULTIPLE DATAFRAME MERGE
# =============================================================================
print("\n--- Chaining Multiple Merges ---")

# Merge three tables at once
result = (employees
    .merge(departments, on='DeptID')
    .merge(salaries, on='EmpID', how='left'))
print("\nThree-way merge:")
print(result)

# =============================================================================
# 11. JOIN METHOD
# =============================================================================
print("\n--- Join Method ---")
# join() is for index-based joining (convenient alternative)

emp_indexed = employees.set_index('EmpID')
sal_indexed = salaries.set_index('EmpID')

# Default is left join
result = emp_indexed.join(sal_indexed, how='left')
print("\nUsing .join() method:")
print(result)

# =============================================================================
# 12. INDICATOR COLUMN
# =============================================================================
print("\n--- Merge Indicator ---")
# Shows which table each row came from

result = pd.merge(employees, salaries, on='EmpID', 
                  how='outer', indicator=True)
print("\nWith merge indicator:")
print(result)

# Find unmatched records
left_only = result[result['_merge'] == 'left_only']
print("\nEmployees without salary:")
print(left_only[['EmpID', 'Name']])

right_only = result[result['_merge'] == 'right_only']
print("\nSalary records without employee:")
print(right_only[['EmpID', 'Salary']])

# =============================================================================
# 13. VALIDATE MERGE
# =============================================================================
print("\n--- Validate Merge ---")

# Ensure merge is one-to-one, one-to-many, etc.
try:
    result = pd.merge(employees, departments, on='DeptID', validate='one_to_one')
except Exception as e:
    print(f"Validation failed: {e}")
    print("(Expected - multiple employees can be in same department)")

# This should work - each dept has one record
unique_depts = departments.drop_duplicates(subset='DeptID')
result = pd.merge(employees, unique_depts, on='DeptID', validate='many_to_one')
print("\nmany_to_one validation passed!")

# =============================================================================
# 14. PRACTICAL EXAMPLE - COMPLETE EMPLOYEE REPORT
# =============================================================================
print("\n--- Practical Example ---")

# Full employee report
full_report = (employees
    .merge(departments, on='DeptID', how='left')
    .merge(salaries, on='EmpID', how='left'))

# Add total compensation
full_report['Total_Comp'] = full_report['Salary'].fillna(0) + full_report['Bonus'].fillna(0)

print("\nComplete Employee Report:")
print(full_report)

print("\n" + "=" * 55)
print("PANDAS PART 5 - MERGING & JOINING COMPLETE!")
print("=" * 55)
