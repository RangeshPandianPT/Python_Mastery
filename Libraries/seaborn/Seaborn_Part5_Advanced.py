# =============================================================================
# SEABORN PART 5 - ADVANCED TOPICS (Advanced)
# =============================================================================
# Advanced visualization: heatmaps, FacetGrid, customization, and more.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sns.set_theme(style="whitegrid")
tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')
penguins = sns.load_dataset('penguins').dropna()

# =============================================================================
# 1. HEATMAP
# =============================================================================
print("--- Heatmap ---")

# Correlation matrix
corr = tips[['total_bill', 'tip', 'size']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, 
            fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.savefig('seaborn_heatmap_corr.png', dpi=100)
plt.close()

# Pivot table heatmap
flights_pivot = flights.pivot(index='month', columns='year', values='passengers')
plt.figure(figsize=(12, 8))
sns.heatmap(flights_pivot, cmap='YlGnBu', annot=True, fmt='d')
plt.title('Flight Passengers by Month and Year')
plt.savefig('seaborn_heatmap_flights.png', dpi=100)
plt.close()
print("Saved heatmaps")

# =============================================================================
# 2. CLUSTERMAP
# =============================================================================
print("\n--- Clustermap ---")

# Clustered heatmap with dendrogram
g = sns.clustermap(flights_pivot, cmap='viridis', 
                   figsize=(10, 10), standard_scale=1)
plt.savefig('seaborn_clustermap.png', dpi=100)
plt.close()
print("Saved clustermap")

# =============================================================================
# 3. FACETGRID
# =============================================================================
print("\n--- FacetGrid ---")

# Custom grid with any function
g = sns.FacetGrid(tips, col='time', row='sex', height=4, aspect=1.2)
g.map_dataframe(sns.scatterplot, x='total_bill', y='tip')
g.add_legend()
plt.savefig('seaborn_facetgrid.png', dpi=100)
plt.close()

# With histogram
g = sns.FacetGrid(tips, col='day', height=3, aspect=1)
g.map(plt.hist, 'total_bill', bins=15, color='steelblue')
plt.savefig('seaborn_facetgrid_hist.png', dpi=100)
plt.close()
print("Saved FacetGrid plots")

# =============================================================================
# 4. PAIRGRID
# =============================================================================
print("\n--- PairGrid ---")

# Custom pair plot
g = sns.PairGrid(penguins, hue='species', 
                 vars=['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm'])
g.map_upper(sns.scatterplot, alpha=0.6)
g.map_lower(sns.kdeplot)
g.map_diag(sns.histplot)
g.add_legend()
plt.savefig('seaborn_pairgrid.png', dpi=100)
plt.close()
print("Saved PairGrid")

# =============================================================================
# 5. CUSTOMIZING PLOTS
# =============================================================================
print("\n--- Customization ---")

# Custom color palette
custom_palette = {'Lunch': '#FF6B6B', 'Dinner': '#4ECDC4'}
plt.figure(figsize=(10, 6))
sns.boxplot(data=tips, x='day', y='total_bill', hue='time', 
            palette=custom_palette)
plt.title('Custom Colors', fontsize=14, fontweight='bold')
plt.xlabel('Day of Week', fontsize=12)
plt.ylabel('Total Bill ($)', fontsize=12)
plt.legend(title='Meal Time', loc='upper right')
plt.savefig('seaborn_custom_colors.png', dpi=100)
plt.close()

# Figure with multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Complete Analysis Dashboard', fontsize=16, fontweight='bold')

sns.histplot(data=tips, x='total_bill', kde=True, ax=axes[0, 0])
axes[0, 0].set_title('Distribution')

sns.boxplot(data=tips, x='day', y='tip', ax=axes[0, 1])
axes[0, 1].set_title('Tips by Day')

sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time', ax=axes[1, 0])
axes[1, 0].set_title('Bill vs Tip')

sns.barplot(data=tips, x='day', y='total_bill', hue='sex', ax=axes[1, 1])
axes[1, 1].set_title('Average Bill')

plt.tight_layout()
plt.savefig('seaborn_dashboard.png', dpi=100)
plt.close()
print("Saved customized plots")

# =============================================================================
# 6. BEST PRACTICES
# =============================================================================
print("\n--- Best Practices ---")

"""
SEABORN BEST PRACTICES:

1. CHOOSE THE RIGHT PLOT
   - Categorical comparison: barplot, boxplot, violinplot
   - Distribution: histplot, kdeplot, ecdfplot
   - Relationship: scatterplot, lineplot, regplot
   - Correlation: heatmap

2. FIGURE-LEVEL vs AXES-LEVEL
   - Figure-level (catplot, relplot, displot): Create own figure, support col/row
   - Axes-level (barplot, scatterplot): For subplots, use ax parameter

3. STYLING TIPS
   - Use set_theme() at the start
   - Keep consistent color palette
   - Add clear titles and labels
   - Use appropriate figure size

4. SAVE HIGH QUALITY
   - plt.savefig('plot.png', dpi=300, bbox_inches='tight')
"""

print("\n" + "=" * 55)
print("SEABORN PART 5 - ADVANCED TOPICS COMPLETE!")
print("=" * 55)
print("\nCongratulations! You've completed the Seaborn series!")
