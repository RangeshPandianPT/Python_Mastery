# =============================================================================
# PANDAS PART 4 - GROUPING & AGGREGATION (Intermediate)
# =============================================================================
# GroupBy is one of the most powerful features in Pandas.
# It follows the split-apply-combine pattern for data analysis.

import pandas as pd
import numpy as np

# =============================================================================
# 1. SAMPLE DATA
# =============================================================================

# Sales data for examples
sales = pd.DataFrame({
    'Date': pd.date_range('2024-01-01', periods=12, freq='M'),
    'Region': ['North', 'South', 'North', 'South', 'East', 'West',
               'North', 'South', 'East', 'West', 'North', 'South'],
    'Product': ['Laptop', 'Laptop', 'Phone', 'Phone', 'Laptop', 'Phone',
                'Tablet', 'Tablet', 'Phone', 'Laptop', 'Phone', 'Laptop'],
    'Quantity': [10, 15, 25, 30, 12, 20, 8, 11, 18, 14, 22, 16],
    'Revenue': [50000, 75000, 25000, 30000, 60000, 20000, 
                24000, 33000, 18000, 70000, 22000, 80000],
    'Salesperson': ['Rahul', 'Priya', 'Rahul', 'Amit', 'Sneha', 'Priya',
                    'Rahul', 'Amit', 'Sneha', 'Vikram', 'Amit', 'Vikram']
})
print("Sales Data:")
print(sales)
print()

# =============================================================================
# 2. BASIC GROUPBY
# =============================================================================
print("--- Basic GroupBy ---")

# Group by single column
region_groups = sales.groupby('Region')
print("\nGroupBy object:", type(region_groups))

# Get sum of all numeric columns per group
print("\nRevenue and Quantity by Region:")
print(sales.groupby('Region')[['Revenue', 'Quantity']].sum())

# Get mean
print("\nAverage Revenue by Region:")
print(sales.groupby('Region')['Revenue'].mean())

# Common aggregations
print("\nRegion statistics:")
print(sales.groupby('Region')['Revenue'].agg(['sum', 'mean', 'min', 'max', 'count']))

# =============================================================================
# 3. GROUPBY WITH MULTIPLE COLUMNS
# =============================================================================
print("\n--- GroupBy Multiple Columns ---")

# Group by two columns
print("\nRevenue by Region and Product:")
print(sales.groupby(['Region', 'Product'])['Revenue'].sum())

# Unstack for better readability
print("\nSame data unstacked:")
print(sales.groupby(['Region', 'Product'])['Revenue'].sum().unstack(fill_value=0))

# =============================================================================
# 4. AGGREGATION METHODS
# =============================================================================
print("\n--- Aggregation Methods ---")

# Multiple aggregations with agg()
print("\nMultiple aggregations:")
print(sales.groupby('Region').agg({
    'Revenue': ['sum', 'mean'],
    'Quantity': ['sum', 'count']
}))

# Named aggregations (cleaner output)
print("\nNamed aggregations:")
result = sales.groupby('Region').agg(
    Total_Revenue=('Revenue', 'sum'),
    Avg_Revenue=('Revenue', 'mean'),
    Total_Units=('Quantity', 'sum'),
    Num_Transactions=('Quantity', 'count')
)
print(result)

# Custom aggregation function
def revenue_range(x):
    return x.max() - x.min()

print("\nRevenue range by Region:")
print(sales.groupby('Region')['Revenue'].agg(revenue_range))

# Lambda functions
print("\nTop 2 revenues per region:")
print(sales.groupby('Region')['Revenue'].agg(lambda x: x.nlargest(2).sum()))

# =============================================================================
# 5. TRANSFORM
# =============================================================================
print("\n--- Transform ---")
# transform() returns data with same shape as original

# Add group mean as new column
sales['Region_Avg'] = sales.groupby('Region')['Revenue'].transform('mean')
print("\nWith Region Average:")
print(sales[['Region', 'Revenue', 'Region_Avg']])

# Calculate deviation from group mean
sales['Deviation'] = sales['Revenue'] - sales['Region_Avg']
print("\nWith Deviation from Region Average:")
print(sales[['Region', 'Revenue', 'Region_Avg', 'Deviation']])

# Normalize within group
sales['Normalized'] = sales.groupby('Region')['Revenue'].transform(
    lambda x: (x - x.min()) / (x.max() - x.min()) if x.max() != x.min() else 0
)
print("\nNormalized Revenue within Region:")
print(sales[['Region', 'Revenue', 'Normalized']])

# =============================================================================
# 6. FILTER GROUPS
# =============================================================================
print("\n--- Filter Groups ---")

# Keep only groups where sum > 100000
print("\nRegions with total revenue > 100000:")
filtered = sales.groupby('Region').filter(lambda x: x['Revenue'].sum() > 100000)
print(filtered)

# Keep groups with at least 3 records
print("\nRegions with 3+ transactions:")
filtered2 = sales.groupby('Region').filter(lambda x: len(x) >= 3)
print(filtered2['Region'].unique())

# =============================================================================
# 7. ITERATING OVER GROUPS
# =============================================================================
print("\n--- Iterating Over Groups ---")

# Sometimes you need to work with each group separately
for name, group in sales.groupby('Region'):
    print(f"\n{name} Region ({len(group)} records):")
    print(f"  Total Revenue: {group['Revenue'].sum():,}")
    print(f"  Top Product: {group.loc[group['Revenue'].idxmax(), 'Product']}")

# =============================================================================
# 8. PIVOT TABLES
# =============================================================================
print("\n--- Pivot Tables ---")

# Basic pivot table
pivot = pd.pivot_table(
    sales,
    values='Revenue',
    index='Region',
    columns='Product',
    aggfunc='sum',
    fill_value=0
)
print("\nPivot Table - Revenue by Region and Product:")
print(pivot)

# Pivot with multiple aggregations
pivot_multi = pd.pivot_table(
    sales,
    values=['Revenue', 'Quantity'],
    index='Region',
    columns='Product',
    aggfunc='sum',
    fill_value=0
)
print("\nPivot with multiple values:")
print(pivot_multi)

# Pivot with margins (totals)
pivot_margins = pd.pivot_table(
    sales,
    values='Revenue',
    index='Region',
    columns='Product',
    aggfunc='sum',
    fill_value=0,
    margins=True,
    margins_name='Total'
)
print("\nPivot with totals:")
print(pivot_margins)

# =============================================================================
# 9. CROSSTAB
# =============================================================================
print("\n--- Crosstab ---")

# Count occurrences
print("\nTransaction count by Region and Product:")
print(pd.crosstab(sales['Region'], sales['Product']))

# With margins
print("\nWith totals:")
print(pd.crosstab(sales['Region'], sales['Product'], margins=True))

# With custom aggregation
print("\nRevenue crosstab:")
print(pd.crosstab(
    sales['Region'], 
    sales['Product'], 
    values=sales['Revenue'], 
    aggfunc='sum',
    margins=True
))

# =============================================================================
# 10. GROUPBY WITH TIME DATA
# =============================================================================
print("\n--- GroupBy with Time ---")

# Set date as index
sales_ts = sales.set_index('Date')

# Group by month
print("\nMonthly Revenue:")
print(sales_ts.resample('M')['Revenue'].sum())

# Group by quarter
print("\nQuarterly Revenue:")
print(sales_ts.resample('Q')['Revenue'].sum())

# Reset for final view
sales = sales.drop(columns=['Region_Avg', 'Deviation', 'Normalized'])

# =============================================================================
# 11. PRACTICAL EXAMPLE - SALES REPORT
# =============================================================================
print("\n--- Practical Example: Sales Report ---")

report = sales.groupby('Salesperson').agg(
    Total_Sales=('Revenue', 'sum'),
    Avg_Sale=('Revenue', 'mean'),
    Transactions=('Revenue', 'count'),
    Biggest_Sale=('Revenue', 'max')
).round(2)

report = report.sort_values('Total_Sales', ascending=False)
print("\nSalesperson Performance Report:")
print(report)

print("\n" + "=" * 55)
print("PANDAS PART 4 - GROUPING & AGGREGATION COMPLETE!")
print("=" * 55)
