# =============================================================================
# SEABORN PART 2 - CATEGORICAL PLOTS (Beginner-Intermediate)
# =============================================================================
# Categorical plots visualize data across categories.
# Great for comparing groups and understanding distributions.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set theme
sns.set_theme(style="whitegrid")

# Load datasets
tips = sns.load_dataset('tips')
titanic = sns.load_dataset('titanic')

print("Tips dataset shape:", tips.shape)
print(tips.head())

# =============================================================================
# 1. BAR PLOT (Mean with Confidence Interval)
# =============================================================================
print("\n--- Bar Plot ---")

# Basic bar plot - shows mean by default
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Simple bar plot
sns.barplot(data=tips, x='day', y='total_bill', ax=axes[0])
axes[0].set_title('Average Bill by Day')

# With grouping (hue)
sns.barplot(data=tips, x='day', y='total_bill', hue='sex', ax=axes[1])
axes[1].set_title('Average Bill by Day and Gender')

plt.tight_layout()
plt.savefig('seaborn_barplot.png', dpi=100)
plt.close()
print("Saved bar plots")

# Custom estimator (median instead of mean)
plt.figure(figsize=(8, 5))
sns.barplot(data=tips, x='day', y='total_bill', estimator=np.median)
plt.title('Median Bill by Day')
plt.savefig('seaborn_barplot_median.png', dpi=100)
plt.close()

# =============================================================================
# 2. COUNT PLOT (Frequency)
# =============================================================================
print("\n--- Count Plot ---")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Basic count
sns.countplot(data=tips, x='day', ax=axes[0])
axes[0].set_title('Visit Count by Day')

# Stacked-like with hue
sns.countplot(data=tips, x='day', hue='time', ax=axes[1])
axes[1].set_title('Visit Count by Day and Time')

plt.tight_layout()
plt.savefig('seaborn_countplot.png', dpi=100)
plt.close()
print("Saved count plots")

# Order categories
plt.figure(figsize=(8, 5))
order = ['Thur', 'Fri', 'Sat', 'Sun']
sns.countplot(data=tips, x='day', order=order)
plt.title('Ordered Count Plot')
plt.savefig('seaborn_countplot_ordered.png', dpi=100)
plt.close()

# =============================================================================
# 3. BOX PLOT (Distribution Summary)
# =============================================================================
print("\n--- Box Plot ---")
"""
Box plots show:
    - Median (line in box)
    - Q1 and Q3 (box edges)
    - Whiskers (1.5 * IQR from edges)
    - Outliers (points beyond whiskers)
"""

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Basic box plot
sns.boxplot(data=tips, x='day', y='total_bill', ax=axes[0])
axes[0].set_title('Bill Distribution by Day')

# With hue
sns.boxplot(data=tips, x='day', y='total_bill', hue='sex', ax=axes[1])
axes[1].set_title('Bill Distribution by Day and Gender')

plt.tight_layout()
plt.savefig('seaborn_boxplot.png', dpi=100)
plt.close()
print("Saved box plots")

# Horizontal box plot
plt.figure(figsize=(8, 5))
sns.boxplot(data=tips, y='day', x='total_bill', orient='h')
plt.title('Horizontal Box Plot')
plt.savefig('seaborn_boxplot_horizontal.png', dpi=100)
plt.close()

# =============================================================================
# 4. VIOLIN PLOT (Distribution Shape)
# =============================================================================
print("\n--- Violin Plot ---")
"""
Violin plots show the full distribution shape.
Combines box plot info with kernel density estimation.
"""

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Basic violin plot
sns.violinplot(data=tips, x='day', y='total_bill', ax=axes[0])
axes[0].set_title('Bill Distribution (Violin)')

# Split violins by hue
sns.violinplot(data=tips, x='day', y='total_bill', hue='sex', 
               split=True, ax=axes[1])
axes[1].set_title('Split Violin by Gender')

plt.tight_layout()
plt.savefig('seaborn_violinplot.png', dpi=100)
plt.close()
print("Saved violin plots")

# With inner detail (quartiles, points, stick)
plt.figure(figsize=(8, 5))
sns.violinplot(data=tips, x='day', y='total_bill', inner='quartile')
plt.title('Violin with Quartile Lines')
plt.savefig('seaborn_violinplot_inner.png', dpi=100)
plt.close()

# =============================================================================
# 5. STRIP PLOT (Individual Points)
# =============================================================================
print("\n--- Strip Plot ---")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Basic strip plot
sns.stripplot(data=tips, x='day', y='total_bill', ax=axes[0])
axes[0].set_title('Strip Plot')

# With jitter (spread points)
sns.stripplot(data=tips, x='day', y='total_bill', 
              jitter=True, alpha=0.6, ax=axes[1])
axes[1].set_title('Strip Plot with Jitter')

plt.tight_layout()
plt.savefig('seaborn_stripplot.png', dpi=100)
plt.close()
print("Saved strip plots")

# =============================================================================
# 6. SWARM PLOT (Non-overlapping Points)
# =============================================================================
print("\n--- Swarm Plot ---")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Basic swarm plot
sns.swarmplot(data=tips, x='day', y='total_bill', ax=axes[0])
axes[0].set_title('Swarm Plot')

# With hue
sns.swarmplot(data=tips, x='day', y='total_bill', 
              hue='sex', dodge=True, ax=axes[1])
axes[1].set_title('Swarm Plot by Gender')

plt.tight_layout()
plt.savefig('seaborn_swarmplot.png', dpi=100)
plt.close()
print("Saved swarm plots")

# =============================================================================
# 7. COMBINING PLOTS
# =============================================================================
print("\n--- Combined Plots ---")

# Box plot + Strip plot (show distribution + individual points)
plt.figure(figsize=(10, 6))
sns.boxplot(data=tips, x='day', y='total_bill', color='lightblue')
sns.stripplot(data=tips, x='day', y='total_bill', color='darkblue', alpha=0.5)
plt.title('Box Plot with Individual Points')
plt.savefig('seaborn_combined_box_strip.png', dpi=100)
plt.close()
print("Saved combined plot")

# Violin + Swarm
plt.figure(figsize=(10, 6))
sns.violinplot(data=tips, x='day', y='total_bill', color='lightgreen', inner=None)
sns.swarmplot(data=tips, x='day', y='total_bill', color='darkgreen', size=4)
plt.title('Violin with Swarm Points')
plt.savefig('seaborn_combined_violin_swarm.png', dpi=100)
plt.close()

# =============================================================================
# 8. POINT PLOT (Mean with Error Bars)
# =============================================================================
print("\n--- Point Plot ---")

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Basic point plot
sns.pointplot(data=tips, x='day', y='total_bill', ax=axes[0])
axes[0].set_title('Average Bill with CI')

# With hue - shows interaction
sns.pointplot(data=tips, x='day', y='total_bill', hue='sex', ax=axes[1])
axes[1].set_title('Comparison by Gender')

plt.tight_layout()
plt.savefig('seaborn_pointplot.png', dpi=100)
plt.close()
print("Saved point plots")

# Custom markers and lines
plt.figure(figsize=(8, 5))
sns.pointplot(data=tips, x='day', y='total_bill', hue='time',
              markers=['o', 's'], linestyles=['-', '--'])
plt.title('Point Plot with Custom Styles')
plt.savefig('seaborn_pointplot_custom.png', dpi=100)
plt.close()

# =============================================================================
# 9. CATPLOT (CATEGORICAL FIGURE-LEVEL FUNCTION)
# =============================================================================
print("\n--- Catplot (Unified Interface) ---")

# catplot provides a unified interface with kind parameter
# kind options: strip, swarm, box, violin, bar, count, point

# Box plots in a grid
g = sns.catplot(
    data=tips, 
    x='day', 
    y='total_bill', 
    col='time',       # Separate columns
    kind='box',       # Plot type
    height=4,
    aspect=1.2
)
g.fig.suptitle('Bills by Time of Day', y=1.02)
plt.savefig('seaborn_catplot_box.png', dpi=100)
plt.close()
print("Saved catplot (box)")

# Violin plots in a grid with hue
g = sns.catplot(
    data=tips, 
    x='day', 
    y='total_bill', 
    hue='sex',
    col='time',
    kind='violin',
    split=True,
    height=4,
    aspect=1.2
)
plt.savefig('seaborn_catplot_violin.png', dpi=100)
plt.close()
print("Saved catplot (violin)")

# =============================================================================
# 10. PRACTICAL EXAMPLE - TITANIC ANALYSIS
# =============================================================================
print("\n--- Practical Example: Titanic Data ---")

# Clean data
titanic_clean = titanic.dropna(subset=['age', 'fare'])

# Survival by class and gender
plt.figure(figsize=(10, 6))
sns.barplot(
    data=titanic_clean, 
    x='class', 
    y='survived', 
    hue='sex',
    palette='Set2'
)
plt.title('Titanic Survival Rate by Class and Gender', fontsize=14)
plt.ylabel('Survival Rate')
plt.xlabel('Passenger Class')
plt.savefig('seaborn_titanic_survival.png', dpi=100)
plt.close()
print("Saved Titanic analysis")

# Age distribution by class
plt.figure(figsize=(10, 6))
sns.boxplot(data=titanic_clean, x='class', y='age', hue='survived')
plt.title('Age Distribution by Class and Survival')
plt.savefig('seaborn_titanic_age.png', dpi=100)
plt.close()

print("\n" + "=" * 55)
print("SEABORN PART 2 - CATEGORICAL PLOTS COMPLETE!")
print("=" * 55)
